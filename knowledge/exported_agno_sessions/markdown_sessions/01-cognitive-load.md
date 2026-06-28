<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# I want to keep this exploration applicable to all applications. It should not be focused on the Lif3 app.

I need to develop a set of rules that other designers can follow and know that their designs will empower users, especially when designing AI+human collaborative tools but also for any tool for humans.

We should make sure it aligns with other accessible design principles and that applications built with our design framework consciously build trust with all users from onboarding to end-of-use.

Let's look at each of your 12 principles and further examine the implications and nuances so we can create that set of rules.

Starting with 'Cognitive load as a budget'.

1. What is the definition of the principle? What is an example of a good implementation in common UIs? An example of a bad implementation?
2. Why is it important to neurodiverse users? Is it also an issue for neurotypicals? Other populations? Implications of bad design? Benefits of good design?
3. Which common user interface elements does this principle apply to?
4. What is the 'job to be done' for users when they encounter this issue?
5. How can we test if this principle is being implemented well? What questions do we ask?
6. Are there strategies or frameworks that already exist to assist with designing for this principle? Any research or prior work to consider?
7. Other factors that impact or challenge this principle being implemented well?
8. Provide synthesis of your findings into a list of insights


This is a rich question that deserves a thorough, referenced answer. No new research needed — here's the deep exploration of Principle 1.

***

# Principle 1: Cognitive Load as a Budget


***

## 1. Definition and Examples

**Definition**

Cognitive load refers to the total amount of mental effort being used in working memory at any given moment. The theory was formalised by educational psychologist John Sweller in the late 1980s and distinguishes three additive types of cognitive load:[^1][^2][^3]

- **Intrinsic load** — the inherent complexity of the task itself (e.g. writing a legal contract is intrinsically harder than writing a grocery list). Designers cannot reduce this without changing the task.
- **Extraneous load** — load imposed by *how* the interface presents information, rather than by the task itself. This is entirely under the designer's control, and reducing it is the primary lever of cognitive-load-aware design.[^4][^3]
- **Germane load** — the mental effort devoted to building understanding and schema from the task. This is productive cognitive work; designers should *protect* space for it by eliminating extraneous load.[^2]

The **budget metaphor** captures the critical constraint: working memory is not expandable. Research has consistently revised the functional capacity of working memory in real-world tasks downward — closer to **four items**, not seven. When the sum of intrinsic + extraneous load exhausts working memory capacity, germane load — actual learning, decision-making, creative thinking — collapses first.[^5][^4][^2]

For UI designers, the rule is: **every element on screen that is not serving the user's current task is spending from a budget they may not have**.

***

**Good implementation: Apple's iOS Settings**
Settings are hierarchically layered — the top level shows only major categories, sub-screens reveal deeper options only when selected. Progressive disclosure is the operative pattern: users face low-load decisions at each level and navigate into complexity only when they choose to. The intrinsic load of changing a setting is preserved; the extraneous load of having every option visible simultaneously is eliminated.[^6][^7]

**Bad implementation: A legacy CRM onboarding screen**
Many CRMs (older Salesforce configurations, for example) present a form with 20+ fields on first use, with no guidance about which are required, which are optional, and what order matters. Every field name is a mini-decision; many are jargon-dense ("Lead Source", "Account Record Type", "Opportunity Stage"). The intrinsic load of populating CRM data is moderate; the extraneous load of parsing the form layout is enormous — and the two stack, reliably exhausting new users before they complete onboarding.[^8]

***

## 2. Importance Across User Populations

**For neurodivergent users (ADHD, dyslexia, autism, anxiety disorders)**

Neurodivergent users have systematically reduced working memory capacity or less efficient executive control over it. For ADHD specifically, neuroimaging research shows that increased cognitive load produces disproportionately degraded performance, greater reaction time variability, and reduced brain network efficiency compared to non-ADHD controls — and the performance gap *widens* as load increases. This means high-extraneous-load interfaces don't just equally slow down ADHD users — they functionally exclude them. An interface a neurotypical user navigates with friction becomes one an ADHD user abandons.[^9][^10][^8]

For autistic users, the processing of unexpected, ambiguous, or visually complex interfaces requires significantly more cognitive effort due to differences in top-down attention filtering — a surplus of visual information demands more active parsing. For users with dyslexia, decoding text is itself a higher-load task, which means there is less budget available for processing the content meaning. For users with anxiety disorders, uncertain interfaces (unclear affordances, ambiguous error states) create an emotional cognitive tax on top of the functional task load.[^11]

**For neurotypical users**

Cognitive overload is universal — it is not a neurodivergent-only experience. Every neurotypical user has a working memory ceiling; they simply have a higher tolerance before hitting it. Neurotypical users experiencing high extraneous load typically slow down, make more errors, feel frustrated, and sometimes abandon tasks — all measurable in standard usability testing. They compensate through strategies (re-reading, taking notes, returning later) that neurodivergent users cannot as reliably deploy.[^12][^8]

**Other affected populations:**

- **Older adults**: Working memory capacity declines with age. The same extraneous load that is uncomfortable for a 30-year-old is functionally prohibitive for a 70-year-old.[^13]
- **Users under stress or time pressure**: Cortisol and stress hormones directly reduce working memory capacity — a customer service agent using a tool during a live call, or a nurse using medical software in an emergency, is neurotypically capable but situationally cognitively constrained.[^8]
- **Users in second-language environments**: Reading and interpreting text in a non-native language consumes intrinsic cognitive resources — less budget remains for task execution.
- **Mobile users in distracted environments**: Walking, commuting, or multitasking while using an interface reduces available working memory — effectively simulating a cognitively impaired state for any user.[^14]

**Implications of bad design:**

- Task abandonment and drop-off at key flows (checkout, onboarding, form completion)
- Increased error rates and support ticket volume
- User anxiety, frustration, and loss of trust in the product
- Exclusion of neurodivergent, elderly, and situationally impaired users
- For AI+human tools specifically: users who cannot process the AI's output due to cognitive overload make worse decisions than if they had received no AI assistance at all

**Benefits of good design:**

- Faster task completion across all user segments
- Reduced errors and re-dos
- Better decision quality (more germane load available for actual reasoning)
- Lower cognitive fatigue = longer productive sessions
- Accessible to a wider population without assistive technology overlays

***

## 3. UI Elements This Principle Applies To

Cognitive load management applies to virtually every interface layer, but the highest-leverage elements are:


| UI Element | Cognitive Load Risk | Design Lever |
| :-- | :-- | :-- |
| **Navigation menus** | Too many top-level items force held-in-memory scanning | Hierarchical grouping, progressive disclosure, clear labels[^2] |
| **Forms** | Each field = a decision + memory task | Reduce to minimum necessary, use smart defaults, autofill[^5] |
| **Onboarding flows** | Dumping all features at once front-loads extraneous load | Staged revelation, contextual tutorials, task-led discovery[^7] |
| **Dashboards** | Every widget competes for attention simultaneously | Default to single primary view; let users add complexity[^8] |
| **Notification systems** | Multiple concurrent alerts = forced task-switching | Batch, prioritise, allow granular user control[^15] |
| **Modal dialogs** | Interrupts working memory context, requires new context loading | Minimise use; when necessary, make action obvious and reversible |
| **Toolbars and ribbons** | Feature-dense surfaces overwhelm by forcing visual scanning | Contextual toolbars (appear when needed), collapsible advanced options |
| **Error messages** | Unclear errors force users to hold error + task in mind simultaneously | Plain language, specific cause, concrete next step[^11] |
| **AI output formatting** | Large walls of unstructured text force parsing overhead | Structured responses, chunked sections, progressive detail levels |
| **Search and filtering** | Complex filter UIs require holding multiple criteria in mind | Smart defaults, saved filters, plain-language search |
| **Settings/preferences panels** | Flat list of 100 options = scanning overhead without task relevance | Group by task/context, surface most-used options, hide advanced settings |
| **Typography and visual hierarchy** | Undifferentiated text density forces users to identify priority themselves | Clear H1/H2/body hierarchy, whitespace, scannable layouts |


***

## 4. The Job to Be Done

When users encounter cognitive overload in a UI, their actual job to be done is not the stated task. The stated task might be "submit an expense report" or "set up an integration" — but the real job they're having to do is:

> **"Figure out what this interface is asking of me right now, so I can get back to the actual task I came here for."**

The design failure is the gap between the two. When interfaces impose high extraneous load, they create an unmandated *meta-task* — a secondary job of interpreting the interface — that sits on top of the primary task and draws from the same cognitive budget.

This is particularly destructive in AI+human collaborative tools, where the primary task is already cognitively demanding (interpreting AI outputs, making decisions based on generated content, exercising judgement over recommendations). When the interface *itself* adds extraneous load on top of that already-demanding primary task, users either:

1. Make worse decisions (less cognitive capacity available for judgement), or
2. Stop engaging with the AI outputs altogether and revert to simpler, known workflows

The job to be done that good cognitive-load design serves is therefore: **"Let me spend all my mental energy on the thing that actually matters."**

***

## 5. Testing Whether This Principle Is Being Implemented Well

**Questions to ask in design review:**

- Can a new user identify the single most important action on this screen within 5 seconds without reading anything?
- How many decisions does the user need to make before they can complete the primary task?
- Which elements on this screen are present for the user's benefit right now, versus for the product team's benefit (marketing messages, feature prompts, upsells)?
- What happens to this screen when you remove every element that isn't essential to the primary task? Does anything critical disappear?
- Does this screen present options that require prior knowledge to understand?

**Formal testing methods**:[^16][^17][^18]

- **NASA-TLX (Task Load Index)**: The most widely validated subjective workload scale — asks users to rate mental demand, temporal demand, effort, frustration, performance, and physical demand after completing a task. Quick to administer post-task; gives a workload score that can be compared across designs.[^16]
- **Eye-tracking**: Measures fixation patterns, saccades, and areas of interest. High extraneous load shows as scattered fixation patterns, long time-on-non-task elements, and revisitation of areas the user should have processed once. Reveals where cognitive effort is being spent involuntarily.[^17]
- **Think-aloud usability testing**: When users verbalise thoughts during a task, confusion and reorientation ("Wait, where is...?", "I'm not sure which...") are direct extraneous load signals.[^19]
- **Task completion time + error rate**: While not a direct measure of cognitive load, elevated error rates and completion times relative to task complexity are a reliable indirect signal of excess extraneous load.
- **5-second test**: Show the screen for 5 seconds, hide it, ask users what they remember and what they think the primary action is. High recall of irrelevant elements = high extraneous load design.
- **Cognitive walkthrough**: A structured expert review method where evaluators step through a task asking "Would a user know what to do here? Would they know if they did it correctly?"[^19]
- **Secondary task paradigms**: Ask users to perform a simple reaction-time task simultaneously with the primary UI task. When reaction time to the secondary task drops, primary task cognitive load is high — this reveals cognitive load in real time rather than retrospectively.[^17]

**For AI+human tools specifically:**

- Does the user correctly understand what the AI did and why, after reading its output? (Tests whether AI explanation generates extraneous load through ambiguity.)
- Does the user change their decision quality when AI assistance is added? (Paradoxically, AI output that adds cognitive load can *degrade* decision quality below the unaided baseline.)

***

## 6. Existing Frameworks and Prior Research

**Cognitive Load Theory (Sweller, 1988; Sweller, van Merriënboer \& Paas, 1998/2019)**[^20][^1][^4]
The foundational research from which all practical design applications derive. The core design principles it generates:

- Reduce extraneous load by eliminating irrelevant information (Coherence Principle)
- Align modality with content (Modality Principle — audio for narration, visuals for spatial information)
- Avoid redundant presentation of the same content in two modes simultaneously (Redundancy Principle)
- Present related information spatially together (Spatial Contiguity Principle)[^21]

**Miller's Law (1956) — correctly applied**[^22][^23][^5]
George Miller's "Magical Number Seven, Plus or Minus Two" is frequently misapplied in UI design (e.g. "never have more than 7 menu items"). The correct application is: working memory can hold approximately 4 items in parallel real-world tasks. The important nuance: this applies to *recall* tasks (items held in memory without visual reference) not *recognition* tasks (choosing from visible options). The limit is not about how many items you show — it's about how many items a user must hold in mind simultaneously without reference.[^23][^5]

**W3C Cognitive Accessibility (COGA) Task Force**[^24][^25][^26][^27]
The W3C's Cognitive and Learning Disabilities Accessibility Task Force has produced "Making Content Usable for People with Cognitive and Learning Disabilities" — a companion document to WCAG that addresses cognitive accessibility in practical depth. Key patterns directly relevant to cognitive load:

- Help users focus by limiting unnecessary content and interruptions
- Use clear and understandable words and short sentences
- Make it easy to identify the purpose and importance of each section
- Ensure users can complete essential tasks without needing to understand, remember, or compute things that are not necessary

**WCAG 2.2 and the gap**[^28][^29][^24]
Current WCAG 2.2 addresses some cognitive load concerns — error prevention (3.3), consistent navigation (3.2), readable content (3.1) — but the most substantive cognitive accessibility criteria sit at Level AAA, which legal compliance frameworks do not require. WCAG 3.0 (in development) explicitly elevates cognitive accessibility as a primary concern, moving cognitive load reduction from aspirational to required. Designers building to the spirit of accessibility — not just legal minimum — should treat COGA guidance as a current design requirement.[^28][^24]

**Nielsen Norman Group — Cognitive Heuristics**[^30]
NN/G's 10 Usability Heuristics include several that are directly cognitive-load-related: \#6 (Recognition over Recall — keep options visible rather than requiring memory), \#8 (Aesthetic and Minimalist Design — remove irrelevant information that competes with relevant information), and \#9 (Help users recognise, diagnose, and recover from errors). These are the most widely used practical design heuristics in industry and provide a minimum floor for cognitive load consideration.

**Progressive Disclosure as a pattern**[^7][^6]
Formalised by UX research at Apple and later codified by NN/G, progressive disclosure is the most practical operational technique for reducing extraneous load in complex UIs. The principle: present only the information needed for the current decision; reveal more only when the user signals readiness. Particularly powerful in onboarding, settings, and advanced feature surfaces.

**Dual-coding Theory (Paivio, 1971)**
Directly complementary to Sweller: information presented in both verbal and visual channels simultaneously (when the channels are complementary, not redundant) reduces cognitive load by distributing processing across multiple systems. Application: diagrams with narration are easier to process than diagrams with on-screen text labels. Relevant for AI output design: a structured visual overview of AI reasoning alongside text reduces load compared to text alone.

***

## 7. Factors That Challenge Good Implementation

**Commercial pressure and feature creep**
Every team in a product organisation wants their feature surfaced. The result is interface surfaces that reflect internal organisational politics rather than user cognitive budgets. Marketing wants upsell prompts; product wants feature discovery; customer success wants help prompts. Each individually justified addition compounds extraneous load. Cognitive load management requires institutional authority — a named design principle with teeth — not just individual designer advocacy.

**The expertise reversal effect**[^3]
A design that reduces cognitive load for novices can *increase* it for experts. An expert user who has automated certain tasks through schema formation finds explicit guidance (instruction text, progressive step-by-step flows) cognitively intrusive — they must now suppress the guidance to perform the task they already know. This is known as the Expertise Reversal Effect, and it means cognitive load management must account for user expertise — the correct design is adaptive to experience level, not fixed.

**Responsive and multi-device complexity**
A design that achieves appropriate cognitive load on desktop may impose dramatically different load on mobile — smaller screens force trade-offs between information density and navigability. Context of use matters: a dashboard that works on a desk monitor may be cognitively overwhelming on a phone during a commute.

**AI output formatting as an emerging challenge**
AI-generated content is a particularly acute cognitive load problem. LLM outputs tend toward verbosity — long paragraphs, exhaustive lists, hedge-heavy language — precisely the format most costly to process under cognitive load. Designing AI tools requires deliberate output formatting standards: length limits, structural hierarchy, progressive detail levels. Without these, AI assistance can paradoxically reduce decision quality by overwhelming users with information they cannot process efficiently.[^31]

**The invisible nature of cognitive load**
Unlike visual accessibility failures (which are often immediately apparent) or functional failures (which produce error states), high cognitive load manifests as fatigue, slow task completion, and user frustration — outcomes that are easily attributed to other causes. This makes cognitive load easy to overlook in design reviews and hard to argue for in stakeholder conversations without usability test data.

**Personalisation as a genuine tension**
Different users have genuinely different cognitive profiles and preferences — what is a clean, low-load interface for one user is an under-powered, feature-sparse experience for another. Resolving this tension requires user-controlled density and configurable information architecture, which creates design and engineering complexity. The short-term pressure to ship a single fixed design is real; the long-term cost of that choice falls on users, not the product team.

**The WCAG compliance floor problem**[^32][^24]
AA-level WCAG compliance does not adequately address cognitive load — research from W3C itself confirms that "AA level conformance to WCAG does not significantly help reduce cognitive load". Designers relying on WCAG compliance as a proxy for cognitive accessibility are meeting a legal minimum that falls well short of meaningful support for neurodivergent and cognitively diverse users. The COGA Task Force guidance provides the more relevant standard, but it carries no legal enforcement weight.[^24][^32]
<span style="display:none">[^33][^34][^35][^36][^37][^38][^39][^40]</span>

<div align="center">⁂</div>

[^1]: https://education.nsw.gov.au/content/dam/main-education/about-us/educational-data/cese/2017-cognitive-load-theory.pdf

[^2]: https://litfl.com/cognitive-load-theory/

[^3]: https://en.wikipedia.org/wiki/Cognitive_load

[^4]: https://www.sciencedirect.com/topics/psychology/cognitive-load-theory

[^5]: https://atticusli.com/blog/posts/millers-law-form-design-working-memory-checkout/

[^6]: https://www.usetools.design/glossary/progressive-disclosure

[^7]: https://versions.com/collective/ui-ux-design-progressive-disclosure/

[^8]: https://asabharwal.com/designing-for-the-neurodivergent/

[^9]: https://nbackboost.com/blog/working-memory-and-adhd/

[^10]: https://direct.mit.edu/netn/article/7/4/1483/117485/Cognitive-and-perceptual-load-have-opposing

[^11]: https://www.uxmatters.com/mt/archives/2024/04/embracing-neurodiversity-in-ux-design-crafting-inclusive-digital-environments.php

[^12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11020716/

[^13]: https://universaldesignaustralia.net.au/reducing-cognitive-load/

[^14]: https://testparty.ai/blog/inclusive-design-benefits-everyone

[^15]: https://www.cannelevate.com.au/article/context-switching-productivity-hidden-cost-modern-work/

[^16]: https://pubmed.ncbi.nlm.nih.gov/41849193/

[^17]: https://www.puxlab.com/post/how-to-measure-cognitive-load-in-ux-research

[^18]: https://arxiv.org/abs/2402.11820

[^19]: https://www.nngroup.com/articles/cognitive-walkthroughs/

[^20]: https://www.mcw.edu/-/media/MCW/Education/Academic-Affairs/OEI/Faculty-Quick-Guides/Cognitive-Load-Theory.pdf

[^21]: https://lemonlearning.com/blog/cognitive-load-theory-types-and-principles-for-reduction

[^22]: https://blog.prototypr.io/the-most-important-rule-in-ux-design-that-everyone-breaks-1c1cb188931

[^23]: https://stephaniewalter.design/blog/your-menu-doesnt-need-millers-7-plus-minus-2-rule/

[^24]: https://uservision.co.uk/thoughts/the-cognitive-and-learning-disabilities-accessibility-task-force-coga

[^25]: https://www.w3.org/WAI/about/groups/task-forces/coga/work-statement/

[^26]: https://www.w3.org/WAI/cognitive/

[^27]: https://www.w3.org/TR/coga-usable/

[^28]: https://mivibzzz.com/resources/accessibility/wcag-3-guide

[^29]: https://accessibilityjobs.net/wcag

[^30]: https://www.nngroup.com/articles/inclusive-design/

[^31]: https://asdnext.org/blog/need-to-embrace-ai/

[^32]: https://w3c.github.io/wai-coga/coga-draft/research

[^33]: https://aaate2023.eu/how-to-make-content-usable-for-people-with-cognitive-and-learning-disabilities/

[^34]: https://www.clickvieweducation.com/en-au/blog/teaching-strategies/cognitive-load-theory

[^35]: https://www.tecnoaccesible.net/en/documents/making-content-usable-people-cognitive-and-learning-disabilities

[^36]: https://www.youtube.com/watch?v=Wx-dGAx0d8o

[^37]: https://www.youtube.com/watch?v=nf85Xaj98io

[^38]: https://www.youtube.com/watch?v=8_fgzJvgYX0

[^39]: https://www.youtube.com/watch?v=bjlB6Yj_Ypo

[^40]: https://blog.logrocket.com/ux-design/millers-law-ux-design/

---

This is pure synthesis — no new research needed beyond the one confirmatory search I just ran. Let me work through what's genuinely surprising and then tackle the single testable rule question directly.

***

## Synthesis: The Unexpected and Novel Insights

### Insight 1: The AI Paradox — The Most Alarming Finding

The most unexpected result across this entire examination is not about neurodivergent users at all. It's about AI tools, and it applies to everyone.

Research published in 2025–2026 confirms that AI tools are generating a new and specific category of cognitive overload. A large-scale survey of nearly 1,500 full-time workers found that 14% report "AI brain fry" — mental fog, impaired decision-making, and a feeling of "a dozen browser tabs open, all fighting for attention". Critically, the research shows that AI *simultaneously* reduces and amplifies cognitive load: it may offload some tasks while overloading the evaluation of its own output. Greater AI dependence is associated with measurably lower critical thinking, partially mediated by cognitive fatigue. [pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC12367725/)

The implication is radical: **an AI tool with high extraneous load doesn't just fail to help — it degrades the user's decision quality below the unaided baseline**. You would be better off not having the AI at all than having it badly designed. This makes cognitive load management the single most important design variable in the entire AI+human collaboration space — not a nice-to-have, but a prerequisite for the tool's value to exist at all.

There is now empirical support for the mechanism: bullet-point format AI output reduces cognitive load by 11.8% in high-demand contexts compared to prose. The format of AI output is a measurable performance variable. No other single design intervention in this examination has a published quantitative effect size attached to it. [nature](https://www.nature.com/articles/s41598-026-45101-3)

***

### Insight 2: The Real Goal Is Germane Load, Not "Low Load"

The most important conceptual reframe in Cognitive Load Theory is consistently missed in product design conversations: the goal is **not to minimise cognitive load** — it is to **eliminate extraneous load so that germane load can expand**.

Research on creative work in architectural design studios makes this explicit: "Greater specificity and explicit instruction facilitates a deliberate reduction in the amount of extraneous information, thereby providing greater capacity for working memory to be devoted to creative exploration and discovery." Every unit of cognitive budget freed from interface navigation by eliminating extraneous load does not sit idle — it becomes available for thinking, creating, and deciding. Reducing extraneous load is not about simplifying for struggling users; it is about **maximising the cognitive bandwidth available for the highest-value work any user does**. [archscience](https://archscience.org/wp-content/uploads/2025/03/Through-the-forest-of-extraneous-things_Exploring-cognitive-load-theory-and-architectural-design-studio-andragogy.pdf)

This reframe is commercially significant. "Accessibility accommodation" is a cost-centre framing. "Releasing cognitive capacity for creativity and strategic thinking" is a competitive advantage framing. They are the same design action. The industry has been selling the wrong version of the argument.

***

### Insight 3: Perceptual and Cognitive Load Are Opposites — and Designers Confuse Them

The neuroimaging research on ADHD performance reveals a finding that almost no design guidance captures: **perceptual load and cognitive load have opposite effects on ADHD performance**. High perceptual load (visually rich, high-contrast, distinct elements) *reduces* the ADHD performance gap relative to neurotypical users. High cognitive load (decisions, ambiguity, working memory demands) *widens* it. [direct.mit](https://direct.mit.edu/netn/article/7/4/1483/117485/Cognitive-and-perceptual-load-have-opposing)

This destroys a common design intuition. Many designers believe that visual richness = cognitive complexity. The research says the opposite. A visually rich, high-contrast, clearly differentiated interface is *easier* for ADHD brains to process than a minimal, low-contrast, visually ambiguous one — provided the visual richness serves perceptual clarity rather than adding decision complexity. The principle isn't "use less" — it's "make what is there *clearer and more distinct*, and remove what requires a decision the user shouldn't have to make."

***

### Insight 4: Cognitive Overload Is an Organisational Failure, Not a Design Failure

The analysis surfaces a governance paradox that no individual design heuristic can solve: feature-bloated, cognitively overloaded interfaces are not failures of designer skill. They are accurate reflections of internal organisational politics. Every team wants its feature surfaced; every stakeholder wants their message visible. The resulting interface is a political document, not a cognitive design.

This means cognitive load management cannot be solved at the designer level alone. It requires institutional authority — a named, enforced principle that gives design decision-makers the power to remove elements over stakeholder objection. Without that authority, any designer can articulate Cognitive Load Theory perfectly and still ship a cognitively overloaded product. The design principle is necessary but not sufficient. The governance structure is what makes it possible to act on it.

***

### Insight 5: WCAG Compliance Is a False Floor — and the Industry Doesn't Know

AA-level WCAG compliance — the standard most organisations target as their accessibility ceiling — was found by W3C researchers themselves to provide no meaningful reduction in cognitive load. The W3C COGA Task Force guidance provides substantive cognitive accessibility criteria, but it carries no legal enforcement weight, is rarely referenced in compliance audits, and is largely unknown in mainstream product teams. The industry has built a compliance infrastructure that systematically fails the very population it claims to protect. Designers who believe they've "done accessibility" by meeting AA compliance have received false assurance on cognitive accessibility. [w3c.github](https://w3c.github.io/wai-coga/coga-draft/research)

***

### Insight 6: The Creativity Connection Is the Commercial Case

The link between extraneous load reduction and creative capacity is the key that unlocks the commercial argument for this entire design framework. The design choices that protect neurodivergent users from cognitive exclusion are the same choices that release creative capacity in every user. The designer who eliminates extraneous load from a workflow tool is not accommodating a disability — they are removing friction from every knowledge worker's creative process. This is not an accessibility argument; it is a product quality argument. The two audiences are served by identical design decisions. [archscience](https://archscience.org/wp-content/uploads/2025/03/Through-the-forest-of-extraneous-things_Exploring-cognitive-load-theory-and-architectural-design-studio-andragogy.pdf)

***

## The Single Testable Rule

Now to the harder question. Can this be reduced to a single testable rule, like words per unit of screen size?

**Why a density metric fails:** The cognitive cost of an interface is not a function of information density — it is a function of *decision density*. Two screens with identical word counts can have completely different cognitive loads. A screen with 200 words of clear narrative has lower cognitive load than a screen with 50 words across 15 button labels, each requiring interpretation. Words per area measures the wrong variable.

**The right variable:** Extraneous cognitive decisions per primary task.

This produces a testable rule:

***

> ### The Decision Purity Rule
> **Every screen state should require exactly one primary decision from the user. Count the number of "what should I do now?" moments a user faces on any given screen. The target is one. Each additional decision point above one is a measurable unit of design debt.**

***

This is:
- **Testable**: Walk through any screen with a cognitive walkthrough or think-aloud session. Count the moments a user is uncertain about what to do next or what something means.
- **Quantitative**: The output is a number — "this screen has 4 decision points; the target is 1."
- **Grounded in working memory research**: Real-world working memory capacity is approximately 4 items, and a single decision with its relevant context saturates a meaningful portion of that capacity. Stacking decisions multiplies load non-linearly. [atticusli](https://atticusli.com/blog/posts/millers-law-form-design-working-memory-checkout/)
- **Scalable**: Applies equally to a form, a dashboard, a settings panel, an AI output, a modal dialog, or an onboarding step.
- **Applicable to AI tools**: "Each AI output should present exactly one primary choice to the user." This directly addresses the verbosity, option-overload, and evaluation-complexity problems driving AI brain fry. [innovativehumancapital](https://www.innovativehumancapital.com/article/when-ai-assistance-becomes-cognitive-overload-understanding-and-managing-brain-fry-in-the-modern)

The practical audit question this generates is sharp: **"After seeing this screen for the first time, does a user know immediately and unambiguously what one thing they should do?"** If not, the screen has more than one primary decision embedded in it, and the designer's job is to resolve the ambiguity — either by removing the competing decisions, or by separating them into sequential screens.

***

### A Practical Companion: The Removal Test

The Decision Purity Rule pairs with a destructive audit that serves as its implementation tool:

> **Remove every element on this screen not directly required for the user's current primary task. If anything removed was load-bearing for the task, restore it. The optimal state is reached when no further element can be removed without breaking the task.**

This is the design equivalent of code refactoring — a discipline of elimination. The screen that survives this process has zero extraneous load by construction. Every element that *is* present is there because the task required it. The cognitive footprint of the interface itself approaches zero.

Together, the Decision Purity Rule (as a numeric audit) and the Removal Test (as a design process) form a complete, testable, and implementable framework for Principle 1 — one that applies to any screen, any application, any user population, with particular force for neurodivergent users and AI+human collaboration tools.

---

Good catch — the user is entirely right. A wall of text with a single decision at the bottom is still cognitively catastrophic. The Decision Purity Rule addresses *decision count* but misses *information processing cost* — the work of parsing content before you even reach the decision. This is a good insight to push into. Let me work through all the layers.

***

## Why One Rule Can't Do It: A Three-Source Model

Cognitive load on a screen has three independent sources that each need their own rules:

1. **Decision load** — how many choices does the user have to make? *(The Decision Purity Rule addresses this)*
2. **Parsing load** — how much cognitive work is required to read and interpret the content before any decision? *(A wall of text violates this entirely)*
3. **Integration load** — how much effort does the user need to mentally connect disparate elements into a coherent picture? *(Poor hierarchy, no chunking, scattered information violates this)*

A screen can score well on decision load and catastrophically on parsing load. All three must be addressed. This expands the rule set — and makes the case for a tiered framework.

***

## A Ranked Rule Set — Ordered by Severity of Impact

The following tiers represent the cognitive load cost if each rule is violated. Tier 1 violations cause functional failure — the user cannot complete the task. Tier 4 violations are real but individually minor; they compound.

### Tier 1 — Critical (Functional Failure)
Violations here prevent task completion or force complete disorientation. No amount of good design elsewhere compensates.

- **The Primary Action Rule**: Every screen state must have exactly one visually dominant primary action. If a user cannot identify what to do next within 5 seconds, the screen has failed at Tier 1. [pubmed.ncbi.nlm.nih](https://pubmed.ncbi.nlm.nih.gov/41849193/)
- **The Hierarchy Existence Rule**: There must be a detectable visual hierarchy — at minimum one level of heading differentiation — so the user can scan before reading. [litfl](https://litfl.com/cognitive-load-theory/)
- **The Coherence Rule** (Sweller): Remove all content not directly relevant to the primary task. Every extraneous word, image, or element adds cognitive cost with zero return. [sciencedirect](https://www.sciencedirect.com/topics/psychology/cognitive-load-theory)
- **The Affordance Clarity Rule**: Any interactive element must be visually distinguishable from non-interactive content. Users must never have to guess whether something is clickable.

### Tier 2 — Significant (High Friction, Meaningful Error Risk)
Violations here cause measurable slowdown, increased errors, and frustration. Users can push through but at real cost.

- **The Chunking Rule**: Related information must be visually grouped together (proximity, containment, or consistent styling). Users should never have to mentally assemble a group that the design left scattered. [lemonlearning](https://lemonlearning.com/blog/cognitive-load-theory-types-and-principles-for-reduction)
- **The Progressive Disclosure Rule**: Present only the information needed for the current decision. Detail that serves a later decision should be reachable but not visible by default. [versions](https://versions.com/collective/ui-ux-design-progressive-disclosure/)
- **The Plain Language Rule**: Every label, heading, error message, and instruction must be legible to a first-time user with no prior product knowledge. Jargon, abbreviations, and internal terminology each add parsing cost. [thinkequitable](https://thinkequitable.com/plain-language-accessibility/)
- **The Memory Dependency Rule**: No element should require the user to recall information displayed elsewhere on screen, or on a previous screen. All necessary context for a decision must be co-located with that decision. [atticusli](https://atticusli.com/blog/posts/millers-law-form-design-working-memory-checkout/)
- **The Scannable Text Rule**: Any text block longer than two sentences must be broken with headings, bullets, or white space. Unbroken prose forces linear reading, which is the highest-cost parsing mode. [litfl](https://litfl.com/cognitive-load-theory/)

### Tier 3 — Moderate (Meaningful Friction That Compounds)
Individual violations are manageable; combinations are not.

- **The Visual Weight Proportionality Rule**: Visual emphasis (size, colour, contrast, motion) should be proportional to task importance. High-weight elements that are low-task-importance steal attention budget.
- **The Density Budget Rule**: Each screen has a maximum information density threshold. Whitespace is not waste — it is the structural mechanism that separates signal from noise and allows the visual hierarchy to function. [asabharwal](https://asabharwal.com/designing-for-the-neurodivergent/)
- **The Completion Feedback Rule**: Every user action must produce an immediate, clear system response. Silence after an action forces the user to hold uncertainty in working memory.
- **The Consistent Interaction Rule**: The same visual pattern must always produce the same interaction behaviour. Unpredictable affordances force constant re-evaluation of familiar elements. [wcag](https://www.wcag.com/blog/digital-accessibility-and-neurodiversity/)

### Tier 4 — Minor (Polish-Level, But Cumulative)
These individually have small impact but compound with each other and with higher-tier violations.

- Suboptimal typography (size, line height, contrast below threshold)
- Decorative animation not serving an informational purpose
- Marginally ambiguous iconography (icon meaning not immediately clear)
- Redundant content (same information presented twice in different forms)
- Overly long labels where a shorter label would be equally clear

***

## The Element Audit: Common Rules + Type-Specific Rules

This is the genuinely useful structural move. Every element on screen answers two sets of questions: one universal set, and one that is specific to what type of element it is.

### Universal Rules — Applied to Every Element

An AI agent or designer should ask these about every single element on a screen:

1. **Presence test**: Is this element necessary for the user's primary task on this screen *right now*? If removed, would the task break?
2. **Clarity test**: Is the element's purpose immediately self-evident without reading any supporting text?
3. **Memory dependency test**: Does using this element require the user to hold information from another part of the screen (or page) in working memory?
4. **Decision imposition test**: Does this element force the user to make a decision that isn't inherent to the task?
5. **Weight proportionality test**: Does this element's visual weight match its task importance?
6. **Interaction predictability test**: Does this element behave consistently with how the same visual pattern behaves elsewhere in this product?

***

### Type-Specific Rules

**Navigation (menus, tabs, breadcrumbs)**
- ≤5 top-level items visible simultaneously without scrolling or interaction [stephaniewalter](https://stephaniewalter.design/blog/your-menu-doesnt-need-millers-7-plus-minus-2-rule/)
- Labels are task-based (what the user will *do* or *find*), not product-based (internal feature names)
- The user's current location is always visible
- Depth of hierarchy is communicated (breadcrumbs or persistent context)
- No item appears in more than one category

**Forms (inputs, fields, dropdowns)**
- Each field has exactly one unambiguous expected answer
- Labels are positioned above the field (not inside as placeholder — placeholder text disappears on focus and can't be referenced while typing) [w3](https://www.w3.org/TR/coga-usable/)
- Only fields required for this step of the task are shown
- Validation is immediate and adjacent to the field it addresses
- Required vs. optional fields are distinguished at the field level, not only in small print at the top

**Text blocks (body copy, descriptions, instructions)**
- Maximum 60–75 characters per line (optimal reading width for all users) [litfl](https://litfl.com/cognitive-load-theory/)
- No paragraph longer than 5 sentences before a structural break
- Information sequence follows the user's decision sequence (most important first)
- No information present that doesn't directly serve the current task (Coherence Principle) [sciencedirect](https://www.sciencedirect.com/topics/psychology/cognitive-load-theory)
- Bullet lists used when items are parallel and the user may need to find a specific one; prose used when logical flow between ideas matters

**Dashboards and data displays**
- Each widget/card answers exactly one question
- Primary metric is the most visually prominent element within its card
- Default state shows the minimum data necessary to act — additional data is accessible but not front-loaded
- No two widgets compete equally for primary visual attention
- Data is labelled in plain language, not in metric codes or internal identifiers

**Modal dialogs and overlays**
- One consequence per modal: what will happen is stated in plain language before the user confirms
- One primary action, one exit action — no third option that adds ambiguity
- All context needed for the decision is inside the modal (no needing to check behind it)
- Non-destructive modals should be dismissible by clicking outside
- The consequence of dismissal is clear (does dismissing cancel? defer? ignore?)

**Notifications and alerts**
- Urgency levels are visually distinct: critical, informational, and ambient alerts must look different
- Each notification contains: what happened, why it matters to the user, and what (if anything) to do
- Non-urgent notifications are not styled as urgent
- Alerts that require no action are visually differentiated from those that do
- Batch-available notifications (non-urgent) should never appear individually in real time if a digest pattern is possible

**AI outputs (generated text, summaries, recommendations)**
- Primary conclusion or recommendation appears first, in the first sentence or visually highlighted — not at the end of a reasoning chain [nature](https://www.nature.com/articles/s41598-026-45101-3)
- Supporting reasoning is accessible but collapsed or de-emphasised by default
- Uncertainty is expressed inline and immediately (not in a separate disclaimer)
- One call to action per output — not a list of options the user must evaluate simultaneously
- Output length is proportional to the complexity of the task, not to the AI's confidence that more is better
- Bullet format preferred over prose for multi-item outputs in high-cognitive-demand contexts (11.8% lower load) [nature](https://www.nature.com/articles/s41598-026-45101-3)

**Toolbars and action surfaces**
- Only actions relevant to the current task context are visible at full visual weight
- Advanced/infrequent actions are accessible but deprioritised (collapsed, behind a "more" affordance)
- Icon + label pairs used for primary tools; icon-only only for well-established universal affordances
- Actions are grouped by task relationship (not by feature category or internal team ownership)
- Destructive actions are visually distinguished and require confirmation

**Error and feedback states**
- Plain language — no error codes, no technical stack information surfaced to users
- Specific cause stated (not "An error occurred")
- Specific resolution path provided (one actionable next step)
- Tone is neutral to supportive — never assigns blame, never escalates urgency beyond what the situation requires
- Error appears adjacent to the element that caused it — not in a banner disconnected from the interaction

**Onboarding and guided flows**
- One concept or capability introduced per step
- Progress indicator present and accurate (user knows how much remains)
- Exit path always visible (no step in onboarding should trap the user)
- Each step delivers functional value before asking for input (the system gives before it asks)
- Prior steps remain accessible if the user needs to reference them

***

## From Element Rules to Screen-Level Assessment

Now to the synthesis: once each element has been individually audited, how do we assess the screen as a cumulative object?

The screen adds three interaction effects that don't exist at the element level:

**1. Competition load** — elements competing for the same attentional tier undermine each other's clarity. Even if each button individually passes its type-specific rules, five equally-weighted buttons on the same screen create a choice paralysis problem. The screen-level check: *Is there a single visually dominant hierarchy from most-important to least-important across all elements?*

**2. Memory dependency chains** — element A requires information from element B to make sense. Even if A and B each pass their individual audits, the mental arc between them is a load cost. The screen-level check: *Can any element be understood in isolation, or does it depend on the user holding something from elsewhere in mind?*

**3. Cumulative density** — individually-acceptable elements can combine to exceed the total cognitive budget. Even if each form field, each label, each status indicator, each CTA individually passes, the sheer volume of them on one screen can exceed working memory's ~4-item simultaneous processing limit. The screen-level check: *What is the total number of distinct content units requiring attention above the fold? The functional maximum for neurodivergent users is 4; for neurotypical users under stress, approximately 7.* [atticusli](https://atticusli.com/blog/posts/millers-law-form-design-working-memory-checkout/)

***

## The Complete AI Agent Assessment Protocol

This gives us a practical, completeable checklist for an AI agent to evaluate any screen:

**Pass 1: Element Inventory**
- List every distinct element on the screen
- Classify each by type
- For each element: run the 6 universal tests + the type-specific rules
- Flag each violation by tier

**Pass 2: Screen-Level Integration**
- Is there a single visually dominant primary action? (Tier 1)
- Can a first-time user identify the primary action within 5 seconds without reading? (5-second test)
- Count: total distinct content units requiring attention above the fold (target: ≤4 for neurodivergent, ≤7 for neurotypical under stress)
- Count: total decisions required before primary task completion (target: 1 at each screen state)
- Identify: any memory dependencies across elements
- Identify: any elements competing for the same visual weight tier
- Identify: any violations of the Progressive Disclosure Rule (information present that belongs to a later decision)

**Pass 3: Tier-Weighted Score**
- Sum violations by tier: Tier 1 × 10 + Tier 2 × 5 + Tier 3 × 2 + Tier 4 × 1
- A score of 0 = fully compliant
- Any Tier 1 violation = immediate redesign required (no cumulative scoring can compensate)
- A score above 15 = significant redesign required regardless of tier distribution

**Pass 4: AI+Human Tool Specific (when applicable)**
- Does the AI output surface its primary recommendation first?
- Does the AI output provide exactly one primary user action?
- Is uncertainty visible without the user needing to ask?
- Does the format of the AI output minimise parsing cost (structured, chunked, appropriately brief)?

***

## The Resulting Pair of Governing Rules

With all of this established, the single testable rule from earlier can be upgraded to a more complete governing pair:

> **Rule A — The Decision Purity Rule**: Every screen state should require exactly one primary decision. Count decision points. Target: 1.

> **Rule B — The Parsing Cost Rule**: Every content element must earn its presence by directly serving the primary task. Count content units requiring attention above the fold. Target: ≤4 for neurodivergent users; ≤7 for neurotypical users under stress.

Together: if a screen has one decision and four or fewer attention-requiring content units, it is almost certainly cognitively well-managed. If it has more of either, it has measurable design debt — and the element-level audit framework above tells you exactly where to start cutting. [archscience](https://archscience.org/wp-content/uploads/2025/03/Through-the-forest-of-extraneous-things_Exploring-cognitive-load-theory-and-architectural-design-studio-andragogy.pdf)