<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

## The Provocation First

The current design is a well-executed wizard. It respects Jordan's time, avoids jargon, and collects structured data cleanly. But it is still fundamentally a form with better clothes — sequential, input-driven, completion-oriented. The mental model it gives Jordan is *"I am answering questions so the system can build something."*

The most interesting alternative paradigm inverts that entirely: *"The system has already made its best attempt. Your job is to correct it."*

Everything below explores that inversion and other departures from the wizard model.

***

## Alternative Paradigms

**Confidence-first / edit-down**
The system makes a complete best-guess analysis immediately from the task description alone, presents the full result, and Jordan's job is to correct what's wrong rather than build from scratch. This respects expertise — Jordan knows their business; the system is the one catching up. Every correction teaches the system rather than just completing a field. The experience feels like reviewing a draft, not filling a form.

**Outcome-led validation**
Rather than asking questions that feed invisible processing, the system surfaces its conclusions at each stage and asks Jordan to validate them. Jordan never sees the questions — only the answers the system derived, with the ability to accept, reject, or modify. The work is done by the system; Jordan audits it. This collapses the perception of effort dramatically.

**Reverse design**
Show Jordan a completed example decomposition for a similar task — a worked example — before asking anything. Jordan's first action is to identify what's different about their situation. The system then asks targeted questions only about the differences. Starting from something concrete rather than a blank slate reduces cognitive load and anchors the conversation.

**Progressive commitment**
Rather than a linear flow where nothing is real until the end, each section becomes a permanent artifact the moment Jordan approves it. Outcomes exist as a card Jordan can return to and modify at any time, independent of the rest of the flow. Risks can be approved before decomposition is complete. The session is not a pipeline — it is a living document that grows in completeness over time.

**The asynchronous draft**
Jordan writes a description, submits it, and is told: *"Come back in a few minutes — we'll have a draft ready for you."* Jordan returns to a complete analysis draft and reviews it at their own pace. Removes the pressure of interactive completion. Better matches how Jordan actually works — not sitting down for 20 minutes of focused flow, but returning to something between other tasks.

**Task archetype matching**
Before any questions, Jordan sees a gallery of 8–12 task archetypes — illustrated cards representing common automation patterns (weekly report, client communication, approval workflow, data aggregation, etc.). Jordan picks the closest match. The system loads a pre-built template for that archetype and asks only the questions that differentiate Jordan's specific context. The session starts 70% complete rather than 0% complete.

***

## Alternative User Flows

**Template-first, difference-only**
Jordan selects a task archetype → system loads a complete template → system asks 3–5 questions that are specific to what makes Jordan's context different from the template default → Jordan reviews and approves a pre-populated analysis. A weekly internal report might require 2 questions. An external client report with a sign-off step might require 5.

**Import and extract**
Jordan pastes an existing SOP, process document, email thread, or meeting notes. The system extracts the task description, infers the structure, and produces a draft analysis. Jordan's first interaction is with a document that already knows their language, their terminology, and their existing process. This is dramatically more contextually accurate than answering abstract questions.

**The "what if" comparison flow**
After completing the analysis, Jordan is presented with a toggle: *"See how this changes if [key variable] is different."* Change external clients to internal team — watch how risk scores, gate placements, and executor recommendations shift in real time. This builds intuition about the system's logic, creates genuine understanding, and surfaces decisions Jordan hadn't considered.

**Collaborative session**
Jordan starts the session and assigns sections to team members. The person who actually runs the reports fills in the pain point and frequency questions. Jordan confirms the risk and executor recommendations. The final analysis reflects multiple perspectives and has broader team buy-in before deployment. Each participant's contributions are attributed.

**Abbreviated fast-track**
For returning users or simple tasks, a three-question flow: what's the task, who sees the output, what would make this wrong. The system produces a "good enough" analysis in under 60 seconds with lower confidence scores on all recommendations. Jordan can refine any section or proceed directly to agent design. The abbreviated analysis is flagged as a starting point, not a finished document.

**Parallel non-linear navigation**
Rather than a fixed sequence, Jordan sees all five sections as tabs — Outcomes, Risks, Subtasks, Inputs/Outputs, Team Design — and can work in any order. The system tracks dependencies and warns Jordan when a section relies on incomplete upstream data. Users who already know their risks can start there. Users who think in terms of the final output can start with the output template. The sequence is a default, not a constraint.

***

## Alternative UI Patterns

**Single-surface unfolding**
No page transitions, no steps. A single scrolling surface that grows as Jordan progresses. The task description sits at the top. Below it, sections appear as they become relevant. Each new section animates in with a gentle expansion. Jordan always has the full context of everything above visible while working on what's below. The session feels like drafting a document, not completing a form.

**Inline consequence preview**
As Jordan makes selections, a small consequence strip appears: *"This means AI will need a human approval gate before sending."* or *"This increases the risk score for client-facing errors."* Jordan sees implications in real time, not after the fact. This builds genuine understanding rather than deferred discovery.

**Live human/agent ratio indicator**
A persistent visual — a simple proportional bar — that shows the current human/agent work split as the analysis builds. As Jordan answers questions, the bar shifts. Selecting "it involves irreversible client communications" moves the bar toward human. Selecting "it's highly repetitive with consistent structure" moves it toward agent. Jordan can feel the logic working in real time rather than waiting for a recommendation at the end.

**Assertion cards instead of question cards**
Rather than *"Who receives the output?"*, the system makes a statement: *"We think this output goes directly to clients."* Jordan's response is agreement, disagreement, or modification. This is psychologically faster — reacting to a claim requires less cognitive effort than generating an answer from scratch — and it gives Jordan the system's reasoning rather than asking them to supply it.

**Similarity cues**
After each major decision, a subtle data point: *"Most consultancies with external-facing reports keep this step human."* Not prescriptive — informational. It contextualises Jordan's choices without overriding them. It also builds trust that the system has seen tasks like this before.

**Drag-to-prioritise**
For the concerns and pain points screens, rather than multi-select checkboxes, Jordan drags cards into a priority order. The act of ranking is more cognitively engaging than selecting, produces richer signal (ordinal rather than binary), and gives Jordan a stronger sense of authorship over the result.

**Confidence indicators on agent inferences**
Every inference the system makes is shown with a subtle confidence marker — a small filled bar or a label like *"High confidence"* / *"Check this"*. Jordan immediately knows which inferences need attention and which can be accepted quickly. Low-confidence inferences are visually prominent; high-confidence ones are visually quiet.

**The undo stack as a visible artifact**
Rather than a simple back button, Jordan can see a brief history of their last 3–5 decisions in a persistent strip. Tapping any of them returns to that point. This removes anxiety about commitment and encourages bolder, more exploratory decision-making.

**Contextual task profile card**
As the session progresses, a persistent "task profile" card builds in a sidebar or collapsible panel. Not the builder strip — a richer characterisation: task type, variability, emotional content, risk profile, likely executor split. It uses plain language: *"This is a high-judgment, variable task — AI is best used as a support, not an autonomous processor."* Jordan can see the system's mental model of the task at any point, not just at the end.

**Friction-free annotation**
At any point in the session, Jordan can tap a note icon on any card, inference, or recommendation and add a free-form annotation. These annotations don't change the analysis — they capture context that doesn't fit the structured schema. They surface in the final output document and in the session log. This gives Jordan a release valve for nuance without breaking the structured flow.

**The "show your working" toggle**
Any agent-generated inference has an expandable *"How did we get here?"* section. It lists the clarification answers that contributed to this conclusion. Jordan can inspect the logic chain without being forced to read it by default. Transparency on demand rather than by default.

***

## Alternative Metaphors

**The design brief**
The session is framed as writing a design brief — the document you give an architect or agency before they start work. The language shifts from *"answering questions about your task"* to *"briefing your team."* The output is called a brief. Jordan is the client; the agents are the creative team. This metaphor has well-understood norms: be clear about outcomes, be honest about constraints, be explicit about what you don't want.

**The job description**
The task analysis is framed as writing a job spec for the agent team. What does the role require? What are the KPIs? What authority does the person have? What do they escalate? What are the red lines? Jordan already knows how to write job descriptions — or at least how to think about them. This metaphor makes the structural decisions (executor, gate, friction type) feel natural rather than technical.

**The expedition brief**
Planning a journey with multiple legs, hazards, and contingencies. Where are we going, what are the risks en route, who leads each leg, what do we do if something goes wrong? This metaphor naturally accommodates the multi-agent, multi-stage structure of the analysis and gives Jordan a vocabulary for uncertainty and risk that doesn't feel bureaucratic.

**The recipe card**
Simple, familiar, domestic. The task has ingredients (inputs), method (subtask sequence), and a result (output). The risks are things that could go wrong with the recipe. The executor split is about which steps need a skilled cook versus which can be done by an assistant. This metaphor lowers the stakes and reduces the perceived complexity of the session.

**Triage, not diagnosis**
The system approaches the task like a medical triage — rapid assessment, structured questions, severity classification, immediate routing. The metaphor gives Jordan permission to be direct and decisive rather than exhaustive. Triage doesn't require complete information — it requires the right information. The session feels efficient and purposeful rather than comprehensive and effortful.

***

## UI Elements Worth Exploring

- **Animated progress that reflects understanding, not completion** — rather than *"Step 4 of 8"*, a progress label that reads *"We understand the task, the audience, and the frequency — still building: difficulty, concerns"*. Completion described in terms of what has been understood, not what has been filled in.
- **A task complexity indicator** — a live scalar that shows how complex the agent design for this task is likely to be, updating as Jordan answers. Simple tasks stay low; tasks with irreversibility, high variability, or external stakeholders climb. Sets expectations before the decomposition stage.
- **The "skip ahead" button for confident users** — after Screen 2, confident users can tap *"Make your best guess on the rest"* and the system auto-completes the remaining intake screens from its inferences, presenting a complete draft for review. The skip is reversible — Jordan can return to any screen.
- **Session warmth indicators** — small, contextually placed phrases that acknowledge what Jordan has contributed: *"That's a useful distinction — most people don't mention the Monday send."* Not praise, but acknowledgment that the input was noticed and used.
- **A "this will matter later" marker** — when Jordan provides a piece of information that will directly influence a gate or executor decision later, a subtle marker appears: *"We'll use this when we design the human oversight steps."* Creates narrative continuity across the session.
- **Real-time risk counter** — a small persistent badge that shows the current number of identified risk factors, updating as Jordan selects concerns and describes difficulties. Not alarming — informational. *"3 risk factors identified so far."*
- **The "done for now" exit** — at any point, Jordan can save and exit. On return, the session opens at exactly the last confirmed step with a one-sentence summary of what was established and what remains. Partial completion is first-class, not a failure state.
- **Keyboard navigation throughout** — number keys to select options, Enter to confirm, Escape to cancel an edit. For users who think faster than they click, the entire flow is completable without a mouse.

