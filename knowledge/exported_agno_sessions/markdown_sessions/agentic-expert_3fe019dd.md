# Agentic Expert

| Field | Value |
|-------|-------|
| **Session** | `3fe019dd...` |
| **Type** | agent |
| **Agent** | Agentic Expert |
| **User** | pete@peterargent.com |
| **Created** | 2026-06-11T23:17:47 |
| **Runs** | 10 completed / 10 total |

## Run 1 — Agentic Expert ✓ COMPLETED

*2026-06-11T23:17:47* · `glm-5.1:cloud` · `82536c08...`

### Prompt

Help me run CAWDP on the workflow use case of marking students' assignment submissions. Start with a backcasting exercise based on the ideal outcomes to understand the task dependencies.

## The ideal outcomes for each stakeholder group:

1. Students receive grades that accurately reflect their achievement in meeting the project brief and rubrics.
2. Students receive feedback that is encouraging, brief and helpful so they can improve their capabilities.
3. The university has satisfied students with no one unhappy with the grades they received.
4. The tutor marking is able to review the scores and feedback given and enter the data into the LMS easily.
5. The tutor marking doesn't need to correct any scores or rewrite any feedback.
6. The turor should be able to mark any assignment with this workflow.
7. The final output should be a single markdown file with all students' scores and feedback.


## The inputs will be:

1. Assignment brief (markdown, different for each assignment - example below)
2. Assignment rubrics (CSV, different for each assignment - example below)
3. Marking Report format (markdown example below - rubrics and scoring will be different for each assignment)
4. Student submissions in PDF, docx or pptx formats.

## Assignment brief example:

```
Assessment 1: In-Class Task

Type: Professional Briefing Deck | Individual
Length: 60 minutes
Weighting: 20%
Due Date: Week 6, in your scheduled class (you MUST attend your timetabled class to access the prescribed assessment task)

Context:

Imagine you are working for a small investment firm.  Your line manager knows very little about crypto assets and has asked you for an introductory briefing deck addressing specific questions, and they given you 60 minutes to provide it.  Your manager also wants you to test how helpful AI is in this type of task so judicious use of AI with a critical lens will help you in the task.

A good quality brief will :

- Only draw on reliable information sources (for this task the materials in canvas will be sufficient, but you may draw on others). Reference the particular pages used on Canvas
- Include charts where applicable. (Copy and paste images from a Website are acceptable with an appropriate time and date)
- Critically evaluate any AI output you use in your submission (Answer this in question 5). 
```

## Rubrics example:

```
Criteria,HD >80%,DI 70-79%,CR 60-69%,PA 50-59%
"C1 (30%) Accurately curates and reports relevant technical information about blockchain, crypto, and cryptofinance.","Creates a comprehensive report detailing relevant technical information about blockchain, crypto and cryptofinance concepts and their application.","Constructs an effective report detailing relevant technical information about blockchain, crypto and cryptofinance concepts and their application.","Formulates a clear report detailing technical information about blockchain, crypto and cryptofinance concepts and generally their application.","Produces a basic report detailing technical information about blockchain, crypto and cryptofinance concepts and vague inferences of their application."
"C2 (30%) Effectively synthesises and interprets technical, ecosystem, and market information for non-specialist audience.","Discusses technical, ecosystem and market information synthesised from relevant sources, translating complex ideas into clear, insightful and accessible explanations tailored to a non-specialist audience.","Explains technical, ecosystem and market information extracted from relevant sources, translating complex ideas into reasonably clear, insightful and accessible explanations tailored to a non-specialist audience.","Describes technical, ecosystem and market information extracted from reasonably relevant sources, translating ideas into understandable explanations for a non-specialist audience.","Selects technical, ecosystem and market information from limited sources, translating ideas into limited explanations for a non-specialist audience."
C3 (20%) Appropriately uses and critically evaluates AI tools in completing the task.,"Generates a critical and reflective evaluation of AI outputs including accuracy, bias, limitations and verification processes through a transparent and sophisticated use of AI tools.","Constructs a comprehensive evaluation of AI outputs including accuracy, bias, limitations and verification processes through a reasonably transparent and sophisticated use of AI tools.","Formulates a clear evaluation of AI outputs including accuracy, bias, limitations and verification processes through a considered use of AI tools.","Produces a basic evaluation of AI outputs including accuracy, bias, limitations and verification processes through a limited use of AI tools."
"C4 (20%) Communicates information clearly, concisely, and accurately in a professional format.","Creates a visually coherent briefing deck, logically structured and effectively communicates the intended key messages","Designs a visually effective briefing deck, reasonably logically structured and professionally communicates the intended key messages.","Executes a visually clear briefing deck, suitably structured and sufficiently communicates the intended key messages.","Produces a visually basic briefing deck, simple structure and vaguely communicates the intended key messages"
```

## Example report table:

```
| Field | Value |
| :--- | :--- |
| Student name | Tu Anh Lam |
| Student number | Not provided |
| C1 score out of 30 | 22 |
| C1 feedback | You've done a solid job covering a range of technical concepts, your definitions for decentralised consensus, private keys, mining, and token standards are accurate and well-paired with "why it matters" explanations. To push into HD territory, you'd need more depth on DeFi protocols and smart contract mechanics, which are currently quite light. |
| C2 score out of 30 | 22 |
| C2 feedback | Your explanations are clear and accessible for a non-specialist audience, I particularly liked the dollar bill analogy for fungible tokens. The main limitation is that sources are cited individually rather than synthesised into an integrated narrative, and the ecosystem domain (regulatory context, key participants) is thinner than your technical and market coverage. |
| C3 score out of 20 | 11 |
| C3 feedback | This is the area that needs the most work, your AI reflection is missing any discussion of bias, which is a required element. You identified one good error in Q4 about price underperformance as a proxy, but you need to go deeper on verification processes and be more transparent about what prompts you gave Claude. |
| C4 score out of 20 | 14 |
| C4 feedback | Your deck is well-structured with clear section headings and effective bullet points that make it easy to follow. Watch out for minor grammatical slips like "due to allows" and make sure your charts include proper timestamps as specified in the brief, these small fixes would lift your score. |
| Total score out of 100 | 69 |
| Overall feedback | You've got strong technical content and clear explanations that serve your non-specialist audience well, the main thing holding you back is the AI reflection in Q5. Add a proper discussion of bias, describe your verification process more explicitly, and you'll see a significant improvement in your overall grade. |
```

### Response

# CAWDP Backcasting: Assignment Marking Workflow

## Phase 1: Output Specification (What Must Exist When We're Done)

Working from your 7 ideal outcomes, I'll define the concrete outputs — both the final deliverable and everything that must exist to produce it.

### Final Deliverable

| ID | Output | Stakeholder | Derived From |
|---|---|---|---|
| **O1** | Final Markdown Report | Tutor | All per-student reports assembled |

### Per-Student Outputs (produced for each of the N students)

| ID | Output | Purpose | Quality Constraint |
|---|---|---|---|
| **O2** | Student Marking Entry | Complete row in the report table | Matches report format exactly |
| **O3** | Per-Criterion Score (×4) | C1/30, C2/30, C3/20, C4/20, Total/100 | Accurately reflects achievement (Ideal 1) |
| **O4** | Per-Criterion Feedback (×4) | Specific, evidence-cited, constructive | Encouraging, brief, helpful (Ideal 2) |
| **O5** | Overall Feedback | Synthesis with priority improvement | Encouraging, brief, helpful (Ideal 2) |

### Per-Criterion Analysis Outputs (produced for each criterion × each student)

| ID | Output | Purpose | Feeds Into |
|---|---|---|---|
| **O6** | Evidence Extraction | What the student actually did for this criterion | O3, O4 |
| **O7** | Rubric Level Match | Which rubric descriptor best fits the evidence | O3, O4 |

### Quality Assurance Outputs (produced once for the cohort)

| ID | Output | Purpose | Quality Constraint |
|---|---|---|---|
| **O8** | Score-Feedback Alignment Check | Score matches evidence, feedback matches score | No corrections needed (Ideal 5) |
| **O9** | Cohort Consistency Report | Similar work gets similar scores | Satisfied students (Ideal 3) |

### Configuration Outputs (produced once per assignment)

| ID | Output | Purpose | Quality Constraint |
|---|---|---|---|
| **O10** | Assignment Configuration | Structured brief + rubrics for processing | Works for any assignment (Ideal 6) |

---

## Phase 2: Backcasting (Tracing Dependency Chains Backward)

Starting from O1 (the final markdown file) and working backward through every dependency to the inputs.

### Chain 1: Final Report ← Per-Student Data

```
O1 Final Markdown Report
  ← O2 Student Marking Entry (×N students)
    ← O3 Per-Criterion Score (×4 criteria × N students)
      ← O7 Rubric Level Match (×4 criteria × N students)
        ← O6 Evidence Extraction (×4 criteria × N students)
          ← I4 Student Submissions
          ← O10 Assignment Configuration
            ← I1 Assignment Brief
            ← I2 Assignment Rubrics
        ← O10 Assignment Configuration (rubric descriptors)
    ← O4 Per-Criterion Feedback (×4 criteria × N students)
      ← O6 Evidence Extraction (already produced above)
      ← O7 Rubric Level Match (already produced above)
      ← O10 Assignment Configuration (brief requirements)
    ← O5 Overall Feedback (×N students)
      ← O3 Per-Criterion Scores (already produced above)
      ← O4 Per-Criterion Feedback (already produced above)
```

### Chain 2: Quality Assurance ← Per-Student Data

```
O8 Score-Feedback Alignment Check
  ← O3 Per-Criterion Scores
  ← O4 Per-Criterion Feedback
  ← O6 Evidence Extraction

O9 Cohort Consistency Report
  ← O3 Per-Criterion Scores (all students)
  ← O6 Evidence Extraction (all students, for comparison)
```

### Chain 3: Configuration ← Raw Inputs

```
O10 Assignment Configuration
  ← I1 Assignment Brief
  ← I2 Assignment Rubrics
  ← I3 Marking Report Format
```

---

## Dependency DAG (Visual)

```
I1 Brief ─────────┐
                   ├─→ O10 Config ─→ O6 Evidence ─→ O7 Rubric Match ─→ O3 Score ─┐
I2 Rubrics ────────┤                                                            ├─→ O2 Entry ─→ O1 Report
                   │                                        O4 Feedback ───────┤
I3 Report Format ──┘                                        ↑                   │
                                     O6 Evidence + O7 Match ┘                  O5 Overall ─┘
I4 Submissions ──→ O6 Evidence                                                ↑
                                                                  O3 + O4 ──┘

Quality Assurance Layer (runs after per-student outputs):
O3 + O4 + O6 ─→ O8 Score-Feedback Alignment
O3 (all students) ─→ O9 Cohort Consistency
```

---

## Input Requirements Map

Each output has specific input requirements. Here's what each needs:

| Output | Required Inputs | Why |
|---|---|---|
| **O10** Assignment Configuration | I1 Brief, I2 Rubrics, I3 Report Format | Parse brief requirements, rubric criteria/descriptors/weightings, report structure |
| **O6** Evidence Extraction | I4 Submission, O10 Config | Extract what the student did for each criterion from their submission |
| **O7** Rubric Level Match | O6 Evidence, O10 Config | Match extracted evidence against rubric level descriptors |
| **O3** Per-Criterion Score | O7 Rubric Level Match, O10 Config | Assign numerical score from matched rubric level × weighting |
| **O4** Per-Criterion Feedback | O6 Evidence, O7 Rubric Level Match, O10 Config | Write feedback citing evidence, referencing rubric gaps, suggesting improvements |
| **O5** Overall Feedback | O3 Scores, O4 Per-Criterion Feedback | Synthesize criterion findings into prioritized improvement narrative |
| **O2** Student Marking Entry | O3 Scores, O4 Feedback, O5 Overall, I3 Report Format | Assemble into report table format |
| **O1** Final Markdown Report | O2 (all students) | Concatenate all student entries |
| **O8** Score-Feedback Alignment | O3, O4, O6 | Verify score aligns with evidence, feedback aligns with score |
| **O9** Cohort Consistency | O3 (all students) | Compare score distributions, flag outliers |

---

## Critical Path Analysis

The critical path through the dependency graph:

```
I1+I2+I3 → O10 → O6 → O7 → O3 → O2 → O1
                                  ↓
                              O4 → O5 → O2
```

**Longest dependency chain:**
1. Parse configuration from brief + rubrics (O10)
2. Extract evidence per criterion per student (O6) — **this is the bottleneck** (4 criteria × N students)
3. Match evidence to rubric levels (O7)
4. Assign scores (O3)
5. Write feedback (O4) — **this is the second bottleneck** (4 criteria × N students)
6. Write overall feedback (O5)
7. Assemble entry (O2)
8. Assemble report (O1)

**Parallel opportunities:**
- O6 (evidence extraction) can run in parallel across students
- O7→O3 (rubric match → score) can run in parallel across criteria for the same student
- O4 (feedback) can run in parallel across criteria for the same student
- O8 (alignment check) can run per student independently
- O9 (consistency) must wait for all students' O3

---

## Key Questions the Backcasting Surfaces

These are decisions that affect the architecture — I need your input:

**Q1: Verification timing.** Should O8 (score-feedback alignment check) happen per-student (catch errors early) or after all students (batch check)? Per-student catches problems sooner but costs more. Batch is cheaper but problems cascade.

**Q2: Consistency gate.** Should O9 (cohort consistency) be a gate before O1 (final report)? If an outlier is found, do we go back and re-score, or flag it for your review?

**Q3: Feedback generation approach.** O4 needs evidence + rubric match. Should feedback be generated per-criterion independently, or should the agent see all four criteria's evidence before writing any feedback (to avoid contradiction and to prioritize overall)?

**Q4: The "no corrections" bar.** Ideal 5 says you don't need to correct scores or rewrite feedback. What's the acceptable threshold? Is "minor wording tweak" acceptable? Or does it need to be literally copy-paste ready?

**Q5: Student count.** How many students per assignment? This determines whether parallelization matters (10 students = sequential is fine; 50+ = parallel is essential).

**Q6: Submission format handling.** PDF, docx, and pptx all need different extraction. Is this a solved problem (existing tools) or a design challenge?

---

Shall I proceed to Phase 3 (Task Decomposition) based on your answers, or do you want to refine the output specification and dependency chains first?The backcasting is complete. The dependency graph is clean — O10 (configuration from brief/rubrics) feeds everything, O6 (evidence extraction) is the main bottleneck, and the quality assurance layer sits logically after the per-student layer.

The six questions at the end are the architectural decision points. Your answers will determine the workflow shape, agent composition, and human gates. Want to work through them?

---

## Run 2 — Agentic Expert ✓ COMPLETED

*2026-06-11T23:37:46* · `glm-5.1:cloud` · `0ce00240...`

### Prompt

1. Verification should happen per student. I have found that it can be better to compare the scores awarded to at least two submissions as they are produced to improve consistency.
2. Any inconsistencies found via this verification should be flagged and if more than 3 inconsistencies are found in a run, the batch should be halted to identify the issue. 
3. The agent should see all evidence before writing feedback so that it is cohesive and doesn't repeat.
4. It needs to be copy-paste ready. 
5. Batches may have 30 or more student submissions.
6. Existing tools for extraction are available and proven.

Continue with task decomposition

### Response

# Phase 3: Task Decomposition

## How Your Answers Shape the Architecture

Before decomposing, let me surface what your six answers structurally require:

| Answer | Structural Implication |
|---|---|
| **Q1**: Per-student verification + compare pairs | O8 runs inside the per-student loop; rolling consistency check compares each student against at least 2 previous students |
| **Q2**: >3 inconsistencies → halt the batch | System-level halt condition; running inconsistency counter; requires state across students |
| **Q3**: Holistic feedback (see all evidence first) | O4/O5 cannot start until ALL criterion evidence is extracted and rubric-matched for that student; feedback is written as one cohesive piece |
| **Q4**: Copy-paste ready | Very high quality bar; O8 (alignment check) must catch everything before the human sees it |
| **Q5**: 30+ students | Parallelization essential; per-student processing should be independent |
| **Q6**: Existing extraction tools | O6 (evidence extraction) is partially solved; the challenge is structuring extracted content for rubric matching, not the extraction itself |

---

## Task Decomposition

### Wave 0: Configuration (once per assignment)

| Task | Description | Cognitive Type | Failure Mode | Output |
|---|---|---|---|---|
| **T1** | Parse assignment brief into structured format (criteria names, weightings, requirements, references to Canvas) | Mechanical | Missing or misread requirements; weightings not extracted | Structured brief object |
| **T2** | Parse rubrics CSV into structured criteria (criterion name, weighting, level descriptors per grade band) | Mechanical | Level descriptors conflated; weightings don't sum to 100 | Structured rubrics object |
| **T3** | Parse report format markdown into template (field names, order, formatting rules) | Mechanical | Format structure not captured; field names misread | Structured template object |
| **T4** | Validate configuration: brief criteria match rubric criteria; weightings sum to 100; report format fields cover all criteria; no gaps or contradictions | Analytical | Inconsistencies between brief and rubrics not caught; misaligned weightings | O10 Assignment Configuration |

### Wave 1: Per-Student Evidence (parallel across students)

| Task | Description | Cognitive Type | Failure Mode | Output |
|---|---|---|---|---|
| **T5** | Extract submission content from PDF/docx/pptx using existing tools | Mechanical | Extraction failure; formatting lost; images/charts not captured | Raw submission text |
| **T6** | Extract evidence for each criterion: identify what the student did that's relevant to C1, C2, C3, C4 | Analytical | Relevant evidence missed; irrelevant content included; evidence attributed to wrong criterion | O6 Evidence Extraction per criterion |
| **T7** | Match each criterion's evidence to rubric level descriptors: which level (HD/DI/CR/PA) best fits the evidence for this criterion | Evaluative | Wrong level selected; evidence misread to fit a level; level descriptors applied too literally or too loosely | O7 Rubric Level Match per criterion |

### Wave 2: Per-Student Scoring (depends on T7 for all criteria)

| Task | Description | Cognitive Type | Failure Mode | Output |
|---|---|---|---|---|
| **T8** | Assign scores for each criterion based on rubric level match and weighting: e.g., DI for C1 → score in DI range for C1/30 | Analytical | Score doesn't match the rubric level; scores at grade boundary treated inconsistently; total doesn't sum correctly | O3 Per-Criterion Scores |

### Wave 3: Per-Student Feedback (depends on T6 + T7 + T8 for ALL criteria — Q3)

| Task | Description | Cognitive Type | Failure Mode | Output |
|---|---|---|---|---|
| **T9** | Write cohesive per-criterion feedback and overall feedback: sees ALL evidence and rubric matches before writing any feedback. Cites specific evidence. References rubric gaps. Prioritises improvements. Does not repeat across criteria. | Generative | Repetition across criteria; vague feedback without evidence citations; feedback contradicts score; generic advice not tied to student's actual work; tone not encouraging | O4 Per-Criterion Feedback + O5 Overall Feedback |

### Wave 4: Per-Student Verification (depends on T8 + T9)

| Task | Description | Cognitive Type | Failure Mode | Output |
|---|---|---|---|---|
| **T10** | Verify score-feedback alignment: does each score match its evidence? Does feedback cite evidence accurately? Does overall feedback synthesise correctly? | Evaluative | Misalignment not caught; contradictory feedback and score not flagged | O8 Score-Feedback Alignment Check per student |

### Wave 5: Per-Student Assembly + Rolling Consistency (depends on T8 + T9)

| Task | Description | Cognitive Type | Failure Mode | Output |
|---|---|---|---|---|
| **T11** | Assemble student marking entry: scores, per-criterion feedback, overall feedback into report table format | Mechanical | Formatting errors; field names wrong; total score calculation error | O2 Student Marking Entry |
| **T12** | Rolling consistency check: compare current student's scores against at least 2 previous students' scores. Flag inconsistencies where similar evidence received different scores. Increment running inconsistency counter. If >3 inconsistencies, HALT the batch. | Evaluative | False positive (flagging legitimate differences); false negative (missing real inconsistencies); batch not halted when it should be | Consistency flags + running counter |

### Wave 6: Cohort Quality Assurance (after all students)

| Task | Description | Cognitive Type | Failure Mode | Output |
|---|---|---|---|---|
| **T13** | Generate cohort consistency report: score distributions, outlier students, criterion-level patterns, any remaining flags | Analytical | Statistical errors; outliers not flagged; patterns missed | O9 Cohort Consistency Report |
| **T14** | Assemble final markdown report: all student entries in order, with consistency report appended | Mechanical | Missing students; wrong order; formatting broken | O1 Final Markdown Report |

---

## Failure Mode Summary

| Failure Mode | What Goes Wrong | Worst Case That Looks Like Success | Tasks Affected |
|---|---|---|---|
| **Rubric level mis-match** | Evidence assigned to wrong level | Student gets DI score but their work reads as HD; marker doesn't notice because feedback "sounds right" | T7, T8 |
| **Score-feedback misalignment** | Score says one thing, feedback says another | Feedback is encouraging about areas where score is low; marker copies both without noticing contradiction | T9, T10 |
| **Vague or generic feedback** | Feedback doesn't cite specific evidence | Feedback could apply to any student; sounds professional but isn't actionable | T9 |
| **Repetition across criteria** | Same point made in multiple criteria feedback | Wastes student's reading time; marker doesn't notice because each criterion looks fine individually | T9 |
| **Consistency failure not caught** | Similar work gets different scores | Two students with similar work get different grades; no flag raised | T12 |
| **Batch not halted** | >3 inconsistencies but pipeline continues | Entire cohort has systematic scoring drift; marker doesn't discover until manual review | T12 |
| **Evidence missed** | Relevant student work not extracted | Student did the work but agent didn't see it; score lower than deserved | T6 |
| **Extraction failure** | PDF/docx/pptx content not captured | Student submission appears empty or garbled; agent marks based on incomplete evidence | T5 |

---

## Critical Dependency Chain

```
T1+T2+T3 → T4 (Configuration)
                    ↓
T5 → T6 → T7 → T8 → T9 (Per-Student Evidence → Scoring → Feedback)
                              ↓
                         T10 (Verification)
                              ↓
                         T11 (Assembly)
                              ↓
                         T12 (Rolling Consistency Check)
                              ↓
                    [HALT if >3 inconsistencies]
                              ↓
                    T13+T14 (Cohort QA + Final Report)
```

**Parallel opportunity:** T5→T6→T7→T8→T9→T10→T11→T12 can run independently for each student, with T12 comparing against the rolling window of previous students.

**Serial constraint:** T9 (feedback) cannot start until T6+T7+T8 for ALL criteria are complete for that student (Q3: holistic feedback).

---

Ready for Phase 4 (Capability Allocation) where I assign Human/Agent/System to each task? This is where the "agent prepares judgment, human makes judgment" principle gets specific — particularly for T7 (rubric matching) and T8 (scoring), which are evaluative but have rubric descriptors to constrain judgment.

---

## Run 3 — Agentic Expert ✓ COMPLETED

*2026-06-11T23:43:14* · `glm-5.1:cloud` · `6c4b8571...`

### Prompt

Yes, phase 4 now

### Response

# Phase 4: Capability Allocation

## Ternary Complementarity Analysis

For each task: who should do what? The principle is **"agent prepares judgment, human makes judgment."**

### Allocation Table

| Task | Description | Cognitive Type | Agent (1-10) | Human (1-10) | Gap (H-A) | Reversibility | Allocation |
|---|---|---|---|---|---|---|---|
| **T1** | Parse assignment brief | Mechanical | 9 | 3 | -6 | High | **System** |
| **T2** | Parse rubrics CSV | Mechanical | 9 | 2 | -7 | High | **System** |
| **T3** | Parse report format | Mechanical | 9 | 2 | -7 | High | **System** |
| **T4** | Validate configuration | Analytical | 8 | 7 | -1 | High | **Agent-primary** |
| **T5** | Extract submission content | Mechanical | 9 | 2 | -7 | High | **System** |
| **T6** | Extract evidence per criterion | Analytical | 7 | 8 | 1 | High | **Collaborative** |
| **T7** | Match evidence to rubric levels | Evaluative | 6 | 9 | 3 | Moderate | **Collaborative** — HUMAN DECIDES |
| **T8** | Assign scores within rubric ranges | Analytical | 7 | 8 | 1 | Moderate | **Collaborative** — HUMAN CONFIRMS |
| **T9** | Write cohesive feedback | Generative | 7 | 8 | 1 | High | **Collaborative** — HUMAN REVIEWS |
| **T10** | Verify score-feedback alignment | Evaluative | 8 | 5 | -3 | High | **Agent-primary** |
| **T11** | Assemble student entry | Mechanical | 9 | 1 | -8 | High | **System** |
| **T12** | Rolling consistency check | Evaluative | 7 | 8 | 1 | Moderate | **Collaborative** — HUMAN JUDGES FLAGS |
| **T13** | Cohort consistency report | Analytical | 8 | 4 | -4 | High | **Agent-primary** |
| **T14** | Assemble final report | Mechanical | 9 | 1 | -8 | High | **System** |

### What Each Allocation Means

**System** — Automated function, no agent or human judgment needed. The task is pure computation, parsing, or template-filling.

**Agent-primary** — Agent does the work, human sees results. Agent PREPARES; human may spot-check but isn't required to review every item.

**Collaborative** — Agent PREPARES options; human DECIDES. The agent never finalizes. The human never starts from blank.

---

## Human Gate Design

Three human interaction points in the workflow. Not after every task — that would be unusable for 30+ students. Strategically placed where human judgment adds irreplaceable value.

### Gate 1: Score & Feedback Review (per student)

**After:** T7 (rubric match) + T8 (scoring) + T9 (feedback) + T10 (alignment check) complete for one student.

**Human sees:**
- Proposed rubric level for each criterion, with evidence cited
- Proposed score for each criterion, with reasoning within the range
- Draft per-criterion feedback + overall feedback
- Alignment check results (any score-feedback mismatches flagged)

**Human decides:**
- Accept, adjust, or reject each rubric level match
- Accept, adjust, or reject each score
- Accept, edit, or reject each piece of feedback

**Agent captures:** The human's decisions and any reasoning provided, for T12 consistency tracking.

**Time budget:** ~3-5 minutes per student. The agent has done the heavy lifting; the human confirms judgment calls.

### Gate 2: Consistency Flag Review (as flagged)

**When:** T12 flags a consistency issue between current student and previous students.

**Human sees:**
- Current student's evidence + scores
- 2+ previous students' evidence + scores for the same criterion
- The specific inconsistency flagged

**Human decides:**
- Is this a genuine inconsistency (same quality, different score)?
- Or a legitimate difference (different quality, different score)?

**Agent captures:** The decision, which feeds back into the inconsistency counter.

### Gate 3: Batch Halt Investigation (conditional)

**When:** T12's running inconsistency counter exceeds 3.

**Human sees:**
- All flagged inconsistencies in the batch so far
- Pattern analysis: is there a systematic issue?

**Human decides:**
- Investigate and fix the issue (then resume)
- Or accept the inconsistencies as legitimate differences (then resume with counter reset)

---

## Authority Boundaries

| Role | CAN Do | NEVER Does |
|---|---|---|
| **System (T1-T3, T5, T11, T14)** | Parse, extract, compute, assemble, format | Judge quality, assign levels, write feedback |
| **Configuration Agent (T4)** | Check brief-rubric consistency, validate weightings, flag contradictions | Override human configuration, skip validation checks |
| **Evidence Agent (T6)** | Extract relevant text for each criterion, cite locations in submission | Judge whether evidence meets a rubric level, interpret evidence quality |
| **Rubric Agent (T7)** | Propose rubric level matches with evidence citations and rationale | **Finalize rubric level matches** — the core professional judgment |
| **Scoring Agent (T8)** | Propose specific scores within rubric ranges with reasoning | **Finalize scores** — the human confirms or adjusts |
| **Feedback Agent (T9)** | Draft per-criterion and overall feedback citing evidence | **Finalize feedback** — the human reviews for copy-paste readiness |
| **Alignment Agent (T10)** | Flag score-feedback mismatches, cite specific contradictions | Override human judgments, suppress flags |
| **Consistency Agent (T12)** | Compare scores across students, flag statistical outliers, count inconsistencies | **Decide if a flag is a real inconsistency** — human decides |
| **Cohort Agent (T13)** | Generate score distributions, identify criterion-level patterns, flag outliers | Override human decisions about grade adjustments |

---

## Decision Presentation at Gates

Using the Decision Presentation Pattern: the agent presents structured options, never open questions.

### Gate 1 — Per Student

For each criterion, the agent presents:

```
C1 (30%) — Accurately curates and reports relevant technical information

EVIDENCE EXTRACTED:
• [Specific quote from submission about blockchain concepts]
• [Specific quote about application to crypto]
• [Gap identified: DeFi protocols mentioned but not explained]

PROPOSED LEVEL: DI (70-79%)
Reasoning: Technical information is effective and generally well-applied, 
but lacks depth in DeFi protocols and smart contract mechanics.

PROPOSED SCORE: 22/30
Reasoning: Solid DI performance. At the lower end of DI range due to 
thin coverage of DeFi and smart contracts.

Options:
  A) Accept DI, 22/30 (agent recommendation)
  B) Accept DI, adjust score to [___]/30
  C) Adjust to different level: HD / CR / PA
  D) I need to review the submission directly
```

For overall feedback, the agent presents a draft and the human can:
- Accept as-is
- Edit inline
- Request redraft with specific direction

### Gate 2 — Consistency Flags

```
CONSISTENCY FLAG:

Student 3, C2 score: 18/30 (CR level)
Student 1, C2 score: 22/30 (DI level)

Evidence comparison:
• Student 3: [key evidence excerpts showing CR-level synthesis]
• Student 1: [key evidence excerpts showing DI-level synthesis]

The same quality of synthesis appears present in both, 
but scores differ by 4 points.

Options:
  A) Legitimate difference — the quality IS different
  B) Inconsistency — adjust Student 3's score
  C) Inconsistency — adjust Student 1's score
  D) Need to review both submissions directly
```

---

## Reversibility Classification

| Task | Reversibility | Impact if Wrong | Who Catches It |
|---|---|---|---|
| T1-T3 Config | **High** | Can re-parse at any time | T4 validation |
| T5 Extraction | **High** | Can re-extract | T6 evidence review |
| T6 Evidence | **High** | Missing evidence catchable at Gate 1 | Human at Gate 1 |
| T7 Rubric match | **Moderate** | Wrong level → wrong grade → student impact | Human at Gate 1 |
| T8 Scoring | **Moderate** | Wrong score → wrong grade → student impact | Human at Gate 1 |
| T9 Feedback | **High** | Can edit feedback at Gate 1 | Human at Gate 1 |
| T10 Alignment | **High** | Flags are informational, not binding | Human at Gate 1 |
| T11 Assembly | **High** | Can re-assemble at any time | T12 consistency |
| T12 Consistency | **Moderate** | Missed inconsistency → unfair grades | Human at Gate 2 |
| T13 Cohort | **High** | Report is informational | Human at end |
| T14 Final | **High** | Can re-assemble at any time | Human at end |

---

## Per-Student Processing Flow

```
T5 (extract) → T6 (evidence) → T7 (rubric match) → T8 (scores) → T9 (feedback)
                                                                              ↓
                                                                        T10 (alignment check)
                                                                              ↓
                                                              ╔═══ GATE 1: Review ═══╗
                                                              ║ Rubric matches         ║
                                                              ║ Scores                 ║
                                                              ║ Feedback               ║
                                                              ║ Alignment flags        ║
                                                              ╚═══════════╤════════════╝
                                                                          ↓
                                                              T11 (assemble entry)
                                                                          ↓
                                                              T12 (consistency check)
                                                                          ↓
                                                              ╔═══ GATE 2: Flag Review ═══╗  (only if flagged)
                                                              ║ Is this a real             ║
                                                              ║ inconsistency?              ║
                                                              ╚═══════════╤════════════════╝
                                                                          ↓
                                                              [If >3 flags: GATE 3: HALT]
                                                                          ↓
                                                              Next student →
```

---

## Batch-Level Flow

```
T1+T2+T3 → T4 (Configuration — once per assignment)
                    ↓
    ┌──────── Per-Student Loop (30+ students) ────────┐
    │  T5 → T6 → T7 → T8 → T9 → T10 → GATE 1        │
    │                                → T11 → T12       │
    │              ┌── GATE 2 (if flagged) ──┐        │
    │              └── GATE 3 (if >3 flags) ───┘        │
    └──────────────────────────────────────────────────┘
                          ↓
              T13 (Cohort Consistency Report)
                          ↓
              T14 (Final Markdown Report)
```

---

## Why This Allocation Works for 30+ Students

| Concern | How This Design Addresses It |
|---|---|
| **Speed** | System and Agent tasks run fast. Human only touches 3 gates per student at most. Gate 1 is ~3-5 min (agent did the heavy lifting). Gate 2 is ~1 min (quick comparison). Gate 3 is rare (batch halt). |
| **Quality** | Human decides on every rubric match, score, and feedback (Gate 1). The agent PREPARES; the human JUDGES. Copy-paste ready is the quality bar. |
| **Consistency** | T12 rolling consistency catches grade drift in real time. >3 flags halts the batch before systematic bias compounds. |
| **No corrections needed** | The agent proposes; human confirms at Gate 1. Output should be copy-paste ready because human has already reviewed and approved every judgment. |
| **Portable across assignments** | T1-T3 configuration makes the workflow assignment-agnostic. Change the brief, rubrics, and format — everything else stays the same. |

---

Ready for Phase 2.5 (Event Storming) or Phase 5 (Event Storming — conditional for multi-agent workflows), or shall we continue to Phase 6 (System Architecture)?

---

## Run 4 — Agentic Expert ✓ COMPLETED

*2026-06-11T23:49:35* · `glm-5.1:cloud` · `44db6bc1...`

### Prompt

phase 5 event storming

### Response

# Phase 2.5: Event Storming

## Domain Events (Normal Workflow Progression)

### Configuration Events

| Event | What Happens | Trigger | Data Produced | Recovery |
|---|---|---|---|---|
| **E1** Configuration Parsed | Brief, rubrics, and format successfully parsed and structured | Human provides I1, I2, I3 inputs | O10 Assignment Configuration | Re-parse with corrected input |
| **E2** Configuration Validated | Brief criteria match rubric criteria; weightings sum to 100; format covers all fields | E1 completion | Validated config object | Flag inconsistencies for human review |

### Per-Student Events

| Event | What Happens | Trigger | Data Produced | Recovery |
|---|---|---|---|---|
| **E3** Submission Extracted | PDF/docx/pptx content successfully extracted into text | Human provides student submission file | Raw submission text | Try alternative extraction method |
| **E4** Evidence Extracted | Relevant content identified and attributed to each criterion | E3 + E2 completion | O6 Evidence Extraction per criterion | Flag missing evidence for human review |
| **E5** Rubric Level Matched | Evidence mapped to best-fit rubric level descriptor | E4 completion | O7 Rubric Level Match per criterion | Present options to human at Gate 1 |
| **E6** Score Proposed | Specific numerical score assigned within rubric range | E5 completion | O3 Per-Criterion Scores | Present range to human at Gate 1 |
| **E7** Feedback Drafted | Per-criterion and overall feedback written, citing evidence | E4 + E5 + E6 for ALL criteria (Q3 constraint) | O4 + O5 Feedback | Present draft to human at Gate 1 |
| **E8** Alignment Checked | Score-feedback consistency verified | E6 + E7 completion | O8 Alignment Check per student | Flag misalignments for human review |
| **E9** Human Review Completed | Human accepts/adjusts/rejects rubric matches, scores, and feedback | E8 completion | Human decisions + reasoning | Record decisions for consistency tracking |
| **E10** Entry Assembled | Scores, feedback, and formatting combined into report table row | E9 completion | O2 Student Marking Entry | Re-assemble if any values changed |
| **E11** Consistency Checked | Current student compared against rolling window of previous students | E10 completion | Consistency flags + running counter | Present flags to human at Gate 2 |

### Batch-Level Events

| Event | What Happens | Trigger | Data Produced | Recovery |
|---|---|---|---|---|
| **E12** Cohort Report Generated | Score distributions, outliers, criterion patterns | All E10 completions | O9 Cohort Consistency Report | N/A (informational) |
| **E13** Final Report Assembled | All student entries + cohort report in single markdown | E12 completion | O1 Final Markdown Report | Re-assemble |

---

## Failure Events (Things That Go Wrong)

### Configuration Failures

| Failure | What Goes Wrong | Detection | Impact | Recovery Path |
|---|---|---|---|---|
| **F1** Brief-rubric mismatch | Criteria in brief don't match rubric columns | T4 validation check | Cannot proceed until resolved — scoring depends on alignment | **HALT.** Present mismatch to human. Resume after correction. |
| **F2** Weightings don't sum to 100 | Rubric weightings total to something other than 100 | T4 validation check | Scores will be calculated on wrong basis | **HALT.** Present weighting error to human. Resume after correction. |
| **F3** Format-rubric field mismatch | Report format expects fields that rubrics don't provide | T4 validation check | Report will have empty or misaligned columns | Flag to human. Proceed if human confirms format is acceptable. |

### Extraction Failures

| Failure | What Goes Wrong | Detection | Impact | Recovery Path |
|---|---|---|---|---|
| **F4** Extraction failure | PDF/docx/pptx content cannot be extracted or is garbled | T5 output is empty, very short, or contains extraction artifacts (garbled text, missing sections) | Student appears to have submitted nothing or very little | **HALT for this student.** Present extraction failure to human. Human can: (a) re-upload submission in different format, (b) manually confirm extraction, (c) skip student for now. |
| **F5** Missing charts/tables | Submission includes charts or tables that extraction loses | T6 evidence check finds references to visual content but no extracted content | C1 and C4 scores may be unfairly low because evidence is missing | Flag to human at Gate 1: "Submission references visual content that may not have been fully extracted. Please verify C1 and C4 evidence." |

### Evidence Failures

| Failure | What Goes Wrong | Detection | Impact | Recovery Path |
|---|---|---|---|---|
| **F6** No evidence for a criterion | Student didn't address a criterion at all | T6 finds zero relevant content for a criterion | Student should receive PA or NA for that criterion, but agent must confirm | Agent proposes PA-level match with "No evidence found for this criterion." **Human confirms at Gate 1.** |
| **F7** Evidence attributed to wrong criterion | Content relevant to C2 is attributed to C1 or vice versa | T7 rubric match doesn't fit well; human notices at Gate 1 | Wrong criterion scored; cascading misalignment | **Flag at Gate 1.** Human reassigns evidence to correct criterion. Agent re-runs T7-T10 for affected criteria. |
| **F8** Evidence fits multiple rubric levels | Student's work sits at a boundary between DI and CR, or CR and PA | T7 confidence is low; rubric level proposal shows ambiguity | Score could go either way; consistency risk across cohort | **Present both options at Gate 1 with reasoning.** Human decides. |

### Scoring Failures

| Failure | What Goes Wrong | Detection | Impact | Recovery Path |
|---|---|---|---|---|
| **F9** Score outside rubric range | Proposed score doesn't fall within the range for the matched rubric level | T8 self-check: score must fall within HD/DI/CR/PA range | Grade calculation error | **Auto-correct.** System forces score into matched level's range. Flag to human at Gate 1. |
| **F10** Total doesn't sum to 100 | C1+C2+C3+C4 ≠ 100 or total is miscalculated | T11 assembly check | Report shows wrong total | **Auto-correct.** System recalculates total. Flag to human at Gate 1. |

### Feedback Failures

| Failure | What Goes Wrong | Detection | Impact | Recovery Path |
|---|---|---|---|---|
| **F11** Feedback contradicts score | Feedback says "strong work" but score is CR-level | T10 alignment check | Student confused; tutor needs to correct | **Flag at Gate 1.** Human edits feedback or adjusts score. Must be resolved before proceeding. |
| **F12** Feedback is generic | Feedback could apply to any student; no specific evidence cited | T10 checks: does feedback reference specific evidence from T6? | Not actionable; violates "helpful" ideal outcome | **Redraft.** Agent re-generates with explicit instruction to cite specific evidence. Human reviews redraft at Gate 1. |
| **F13** Feedback repeats across criteria | Same point made in C1 feedback and C2 feedback | T10 checks: does C1-C4 feedback have overlap? | Wastes student's reading time; not cohesive | **Redraft.** Agent re-generates with instruction to avoid repetition across criteria. Human reviews redraft at Gate 1. |

### Consistency Failures

| Failure | What Goes Wrong | Detection | Impact | Recovery Path |
|---|---|---|---|---|
| **F14** Genuine inconsistency | Similar quality work scored differently across students | T12 rolling consistency check | Unfair grades; student complaints | **Flag at Gate 2.** Human decides: legitimate difference or adjust scores. |
| **F15** False positive flag | Different quality work flagged as inconsistent | T12 compares evidence alongside scores | Human wastes time reviewing | **Human dismisses at Gate 2.** Flag counter increments but no score adjustment. |
| **F16** Batch halt triggered | >3 inconsistencies accumulated in the run | T12 inconsistency counter exceeds 3 | Entire batch stopped; systematic issue suspected | **GATE 3.** Human reviews all flags. If systematic: fix issue (e.g., rubric interpretation), reset counter, resume. If not systematic: accept flags, reset counter, resume. |

### Human Gate Failures

| Failure | What Goes Wrong | Detection | Impact | Recovery Path |
|---|---|---|---|---|
| **F17** Human adjusts score significantly | Human changes score by more than one rubric level | Human adjustment exceeds expected range | May create new inconsistency with other students | **Feed back into T12.** Adjustment is recorded. If it creates a new inconsistency, it will be flagged in the rolling check. |
| **F18** Human rewrites feedback substantially | Human edits more than 30% of feedback text | Human edits exceed threshold | Agent feedback quality signal; may indicate systematic feedback issue | Log the edit percentage. If >3 students require substantial rewrites, flag for batch review: feedback agent may need adjustment. |

---

## System-Enforced Triggers

These are automatic checks the system runs without human intervention. They prevent known failure modes structurally.

| Trigger | What It Checks | When | Action If Failed |
|---|---|---|---|
| **ST1** | Brief criteria = rubric criteria | After T4 | Halt. Present mismatch to human. |
| **ST2** | Weightings sum to 100 | After T4 | Halt. Present error to human. |
| **ST3** | Format fields cover all rubric criteria | After T4 | Warn. Proceed if human confirms. |
| **ST4** | Score falls within matched rubric level range | After T8 | Auto-correct to boundary. Flag at Gate 1. |
| **ST5** | Total score = sum of criterion scores | After T11 | Auto-correct. Flag at Gate 1. |
| **ST6** | Feedback references specific evidence | After T9 | Redraft if generic. Human reviews redraft. |
| **ST7** | No repetition across C1-C4 feedback | After T9 | Redraft if >30% overlap. Human reviews redraft. |
| **ST8** | Score-feedback alignment | After T10 | Flag misalignments at Gate 1. Must resolve before proceeding. |
| **ST9** | Inconsistency counter ≤ 3 | After T12 each student | If >3: GATE 3 halt. Present all flags. |
| **ST10** | All students processed | After final E11 | Proceed to T13 (cohort report). |

---

## Event Flow Diagram

```
START
  │
  ├─ E1 + E2 → [ST1, ST2, ST3] ── Fail → HALT (F1, F2, F3)
  │                                    ── Pass ↓
  │
  │  ┌─────────── Per Student (×30+) ───────────┐
  │  │                                          │
  │  │  E3 → [F4: extraction fail?] ── Yes → HALT student
  │  │         ── No ↓                          │
  │  │  E4 → [F5,F6,F7: evidence issues?]       │
  │  │         ── Flag at Gate 1 ↓              │
  │  │  E5 → [F8: level ambiguous?]             │
  │  │         ── Present options at Gate 1 ↓    │
  │  │  E6 → [F9: score out of range?]           │
  │  │         ── Auto-correct + flag ↓         │
  │  │  E7 → [F11,F12,F13: feedback issues?]    │
  │  │         ── Redraft if needed ↓            │
  │  │  E8 → [ST8: alignment] ── Flag ↓        │
  │  │                                          │
  │  │  ═══ GATE 1: Review ═══                 │
  │  │  Human reviews scores, feedback,          │
  │  │  alignment flags. Accepts/adjusts.        │
  │  │  [F17: significant adjustment?]           │
  │  │  [F18: substantial rewrite?]              │
  │  │                                          │
  │  │  E9 (human decisions recorded)            │
  │  │  E10 → [ST5: total] ── Auto-correct    │
  │  │  E11 → [ST9: inconsistency count]       │
  │  │         ── If >3: ═══ GATE 3: HALT ═══ │
  │  │         ── If flag: ═══ GATE 2: Review ═══│
  │  │                                          │
  │  └──────────────────────────────────────────┘
  │
  │  E12 (cohort report)
  │  E13 (final report)
  │
  END
```

---

## Key Event Storming Insights

**1. Three halt conditions, not one.**
- **Config halt** (F1, F2): Before any marking starts. Wrong configuration = wrong everything.
- **Extraction halt** (F4): Per-student. Can't mark what you can't read.
- **Batch halt** (F16): Systematic inconsistency. Stop the line before bias compounds.

**2. Two redraft triggers, not just "human edits".**
- F12 (generic feedback) and F13 (repetitive feedback) trigger automatic redrafting BEFORE the human sees them. This is the agent preparing judgment — it catches its own quality issues before presenting to the human.

**3. The consistency counter is a system-enforced safety net.**
- ST9 doesn't ask "is this inconsistent?" — it counts flags and halts at 3. The human decides whether flags are genuine (Gate 2), but the halt is structural.

**4. Human adjustments feed back into the system.**
- F17 (significant score adjustment) and F18 (substantial feedback rewrite) aren't just logged — they're fed back into the consistency check. If the human adjusts a score, that adjustment is now the standard against which future students are compared.

**5. F8 (ambiguous rubric level) is the most common edge case.**
- Boundaries between HD/DI, DI/CR, CR/PA are inherently subjective. Presenting both options at Gate 1 with reasoning is the correct response — the agent prepares the judgment, the human makes it.

---

Ready for Phase 6 (System Architecture) where I'll define the pipeline composition, orchestration, and fallback model?

---

## Run 5 — Agentic Expert ✓ COMPLETED

*2026-06-12T00:02:21* · `glm-5.1:cloud` · `5f0c4001...`

### Prompt

yes, phase 6 now

### Response

# Phase 6: System Architecture

## Pipeline Architecture

### Stage Overview

| Stage | Purpose | Tasks | Runs | Human Gate |
|---|---|---|---|---|
| **Stage 0** | Configuration | T1→T2→T3→T4 | Once per assignment | None (failure = halt) |
| **Stage 1** | Per-Student Processing | T5→T6→T7→T8→T9→T10→T11→T12 | Per student (30+) | Gate 1 (review), Gate 2 (flags), Gate 3 (halt) |
| **Stage 2** | Cohort Quality Assurance | T13→T14 | Once per batch | None |

### Pipeline Diagram

```
STAGE 0: CONFIGURATION
═════════════════════════
T1(Parse Brief) → T2(Parse Rubrics) → T3(Parse Format) → T4(Validate Config)
    │                                      │                          │
    │  [ST1/ST2/ST3: validation checks]    │                          │
    │  FAIL → HALT (F1/F2/F3)             │                          │
    │  PASS ──────────────────────────────┘                          │
    ↓                                                                  │
O10 Assignment Configuration                                           │
                                                                       │
STAGE 1: PER-STUDENT PROCESSING (×30+)                                 │
═════════════════════════════════════════                               │
                                                                       │
┌─ T5(Extract) ─→ T6(Evidence) ─→ T7(Rubric Match) ─→ T8(Scores) ─┐  │
│                                              │                    │  │
│                              [ST4: score range check]             │  │
│                                              │                    │  │
│                              T9(Feedback) ←──┘ (waits for ALL    │  │
│                                              │   criteria T6+T7) │  │
│                              [ST6/ST7: feedback quality]         │  │
│                                              │                    │  │
│                              T10(Alignment) ─┘                    │  │
│                                              │                    │  │
│                              [ST8: alignment check]              │  │
│                                              │                    │  │
│                              ═══ GATE 1 ═══                      │  │
│                              Human reviews:                       │  │
│                              • Rubric level matches               │  │
│                              • Proposed scores                    │  │
│                              • Draft feedback                    │  │
│                              • Alignment flags                    │  │
│                              ══════════════                       │  │
│                                              │                    │  │
│                              T11(Assemble Entry)                   │  │
│                                              │                    │  │
│                              [ST5: total check]                   │  │
│                                              │                    │  │
│                              T12(Consistency Check)               │  │
│                                              │                    │  │
│                              [ST9: inconsistency counter]         │  │
│                                              │                    │  │
│                         ┌── Flag? ── GATE 2: Flag Review ──┐    │  │
│                         │                                   │    │  │
│                         └── >3 flags? ── GATE 3: HALT ─────┘    │  │
│                                              │                    │  │
│                              Next student ←───────────────────────┘  │
                                                                       │
STAGE 2: COHORT QUALITY ASSURANCE                                     │
═══════════════════════════════════════                                 │
                                                                       │
T13(Cohort Report) → T14(Final Report)                                │
                                                                       │
O1 Final Markdown Report ──────────────────────────────────────────────┘
```

### Stage 1 Internal Flow (Detail)

The per-student loop has a specific execution order governed by Q3 (holistic feedback):

```
                    T5 (Extract)
                         │
                    T6 (Evidence per criterion)
                    │    │    │    │
                    C1   C2   C3   C4  ← all 4 criteria extracted
                    │    │    │    │
                    T7 (Rubric Match per criterion)
                    │    │    │    │
                    C1   C2   C3   C4  ← all 4 rubric levels matched
                    │    │    │    │
                    T8 (Scores per criterion)
                    │    │    │    │
                    C1   C2   C3   C4  ← all 4 scores proposed
                    │    │    │    │
                    └────┴────┴────┘
                          │
                    ╔═══════════════╗
                    ║ WAIT: All C1-C4 ║  ← Q3 constraint
                    ║ evidence+match ║
                    ║ +scores ready ║
                    ╚═══════════════╝
                          │
                    T9 (Feedback — sees ALL evidence)
                    │    Writes C1-C4 feedback + overall
                    │    as one cohesive piece
                    │
                    T10 (Alignment Check)
                    │
                    ═══ GATE 1 ═══
                    │
                    T11 (Assemble Entry)
                    │
                    T12 (Rolling Consistency)
                    │
                    Continue or Flag/Halt
```

---

## Composition Decision

**Decision: Agno Workflow** (not Team, not single Agent)

| Option | Assessment |
|---|---|
| **Single Agent** | ✗ — Too many distinct cognitive operations (extraction, evaluation, generation, verification, aggregation). A single agent would need to context-switch between Measurer, Assessor, Generator, and Aggregator modes. Authority boundaries become prompt-level, not structural. |
| **Agno Team** | ✗ — Teams are for collaborative tasks where agents work together on the same problem. This is a pipeline: tasks flow sequentially with gates. Agents don't need to collaborate; they hand off. |
| **Agno Workflow** | ✓ — Sequential stages with human gates, conditional paths (flag/halt), and clear handoffs. Each stage has a defined input/output. The `requires_output_review=True` parameter enables the human gates. |

### Specialist Agent Roster

| Agent | Class | Orientation | Responsibility | Authority Boundary |
|---|---|---|---|---|
| **Configurator** | Aggregator | Constraint | Parse and validate brief + rubrics + format into structured configuration | **Never overrides** human configuration. **Never skips** validation checks. Flags all mismatches. |
| **Curator** | Measurer | Constraint | Extract and categorise evidence from submission per criterion | **Never judges** quality. **Never matches** to rubric levels. Reports what is there. |
| **Assessor** | Assessor | Constraint | Match evidence to rubric level descriptors; propose scores within ranges | **Never finalizes** rubric matches or scores. Proposes with reasoning. Presents options at boundaries. |
| **Drafter** | Generator | Constraint | Write cohesive per-criterion and overall feedback citing evidence | **Never fabricates** evidence. **Never repeats** across criteria. **Never contradicts** scores. Cites specific evidence or flags gaps. |
| **Verifier** | Assessor | Adversarial | Check score-feedback alignment; check feedback quality (specificity, repetition); check consistency across students | **Never adjusts** scores or rewrites feedback. **Flags only.** Presents mismatches and inconsistencies for human decision. |
| **Compiler** | Aggregator | Constraint | Assemble entries and final report from verified components | **Never adds** content. **Never changes** scores or feedback. Assembles exactly what was approved. |

### Why This Roster

1. **Curator ≠ Assessor** (CC-1 Verification Independence): The agent that extracts evidence does not evaluate it. This prevents confirmation bias — the Curator reports what's there, the Assessor evaluates it against rubrics.

2. **Assessor ≠ Verifier** (CC-1 Verification Independence): The agent that proposes scores is not the same agent that checks alignment. The Verifier catches what the Assessor might miss — especially score-feedback contradictions.

3. **Drafter is separate** (CC-1 for generative tasks): Writing feedback is a different cognitive operation from scoring. The Drafter sees all evidence holistically (Q3) but doesn't assign scores.

4. **Compiler never adds** (Aggregator authority boundary): Assembly is mechanical. The Compiler never fabricates, never adjusts, never interprets. It puts approved components into the template.

---

## Orchestration Design

### Workflow Structure

```
Agno Workflow: Assignment_Marking_Pipeline

Step 1: Configuration
  Agent: Configurator (Aggregator)
  Input: I1 Brief + I2 Rubrics + I3 Format
  Output: O10 Assignment Configuration
  System triggers: ST1, ST2, ST3
  On failure: HALT

Step 2: Per-Student Loop (for each student)
  
  Step 2a: Extraction
    Agent: Curator (Measurer) — T5 + T6
    Input: Student submission + O10 Config
    Output: O6 Evidence Extraction (per criterion)
    On failure (F4): HALT for this student

  Step 2b: Rubric Match + Scoring
    Agent: Assessor (Assessor) — T7 + T8
    Input: O6 Evidence + O10 Config
    Output: O7 Rubric Level Match + O3 Proposed Scores
    System trigger: ST4 (score range check)
    On boundary case (F8): Present both options at Gate 1

  Step 2c: Feedback Drafting
    Agent: Drafter (Generator) — T9
    Input: O6 Evidence + O7 Rubric Match + O3 Scores (ALL criteria)
    Output: O4 + O5 Draft Feedback
    System triggers: ST6 (specificity), ST7 (repetition)
    On failure (F12/F13): Auto-redraft before Gate 1

  Step 2d: Alignment Check
    Agent: Verifier (Assessor) — T10
    Input: O3 Scores + O4 Feedback + O6 Evidence
    Output: O8 Alignment Check
    System trigger: ST8 (alignment check)
    Flags presented at Gate 1

  Step 2e: Gate 1 — Human Review
    Human reviews: O7 rubric matches, O3 scores, O4+O5 feedback, O8 alignment flags
    Human decides: Accept/Adjust/Reject each
    System captures: Human decisions + reasoning
    On significant adjustment (F17/F18): Feed back into consistency tracking

  Step 2f: Assembly
    Agent: Compiler (Aggregator) — T11
    Input: Approved O3 + O4 + O5 + O10 Format
    Output: O2 Student Marking Entry
    System trigger: ST5 (total check)

  Step 2g: Consistency Check
    Agent: Verifier (Assessor) — T12
    Input: Current O3 + Rolling window of previous O3s
    Output: Consistency flags + running counter
    System trigger: ST9 (>3 inconsistencies → Gate 3)
    On flag: Gate 2
    On >3 flags: Gate 3 (batch halt)

  Step 2h: Gate 2 — Flag Review (conditional)
    Only triggered if T12 flags an inconsistency
    Human decides: Legitimate difference or real inconsistency

  Step 2i: Gate 3 — Batch Halt (conditional)
    Only triggered if inconsistency counter > 3
    Human decides: Fix systematic issue or accept flags

Step 3: Cohort Quality Assurance
  Agent: Compiler (Aggregator) — T13 + T14
  Input: All O2 entries + all O3 scores
  Output: O9 Cohort Report + O1 Final Markdown Report
```

### Orchestrator Decisions

| Decision Point | Condition | Action |
|---|---|---|
| After Step 1 | Config validation fails | HALT workflow. Present errors to human. |
| After Step 2a | Extraction fails (F4) | HALT for this student. Offer re-upload or skip. |
| After Step 2d | Alignment flags exist | Present flags at Gate 1 alongside scores/feedback. |
| After Gate 1 | Human makes significant adjustment | Feed adjustment into consistency tracking (F17). |
| After Step 2f | Total score ≠ sum of criteria | Auto-correct. Present at Gate 1 for confirmation. |
| After Step 2g | 1-3 inconsistencies flagged | Present at Gate 2 for human review. |
| After Step 2g | >3 inconsistencies | Trigger Gate 3 (batch halt). |
| After Gate 2 | Human confirms legitimate difference | Decrement counter. Continue. |
| After Gate 3 | Human fixes systematic issue | Reset counter. Resume. |
| After Gate 3 | Human accepts flags | Reset counter. Resume. |

---

## FMEA (Failure Mode and Effects Analysis)

| ID | Failure Mode | Severity (1-10) | Occurrence (1-10) | Detection (1-10) | RPN | Mitigation | Recovery |
|---|---|---|---|---|---|---|---|
| **F1** | Brief-rubric mismatch | 10 | 3 | 8 | 240 | ST1 validation at configuration | HALT before marking starts |
| **F2** | Weightings don't sum to 100 | 10 | 2 | 9 | 180 | ST2 validation at configuration | HALT before marking starts |
| **F3** | Format-rubric field mismatch | 6 | 3 | 7 | 126 | ST3 validation at configuration | Flag; proceed if human confirms |
| **F4** | Extraction failure | 8 | 2 | 9 | 144 | Alternative extraction methods | HALT for this student |
| **F5** | Missing charts/tables | 5 | 4 | 6 | 120 | Flag at Gate 1 for C1/C4 | Human verifies visual content |
| **F6** | No evidence for a criterion | 7 | 3 | 9 | 189 | Propose PA-level at Gate 1 | Human confirms |
| **F7** | Evidence attributed to wrong criterion | 7 | 3 | 5 | 105 | Flag at Gate 1; human reassigns | Re-run T7-T10 for affected criteria |
| **F8** | Ambiguous rubric level (boundary) | 6 | 5 | 4 | 120 | Present both options at Gate 1 | Human decides |
| **F9** | Score outside rubric range | 10 | 2 | 9 | 180 | ST4 auto-correct | Flag at Gate 1 |
| **F10** | Total miscalculation | 10 | 1 | 10 | 100 | ST5 auto-correct | Flag at Gate 1 |
| **F11** | Feedback contradicts score | 8 | 3 | 7 | 168 | T10 alignment check (ST8) | Human resolves at Gate 1 |
| **F12** | Generic/unsupported feedback | 6 | 4 | 5 | 120 | ST6 specificity check; auto-redraft | Human reviews redraft at Gate 1 |
| **F13** | Repetitive feedback across criteria | 5 | 3 | 5 | 75 | ST7 repetition check; auto-redraft | Human reviews redraft at Gate 1 |
| **F14** | Genuine inconsistency (same work, different scores) | 8 | 3 | 4 | 96 | T12 rolling consistency check | Gate 2 review |
| **F15** | False positive consistency flag | 3 | 4 | 6 | 72 | Human review at Gate 2 | Dismiss; counter still increments |
| **F16** | Batch halt triggered | 9 | 2 | 8 | 144 | ST9 counter limit | Gate 3: human investigates |
| **F17** | Human adjusts score significantly | 4 | 3 | 8 | 96 | Feed adjustment back into T12 | Re-check consistency |
| **F18** | Human rewrites feedback substantially | 3 | 4 | 7 | 84 | Log edit percentage | If >3 students: flag for batch review |

### Top 5 Risks (by RPN)

1. **F1 (240)** — Brief-rubric mismatch. Mitigated by ST1 validation at configuration. Severity is highest because wrong config cascades to every student.

2. **F6 (189)** — No evidence for a criterion. Moderate severity (student gets low score but it's correct), moderate occurrence (some students skip criteria), high detection (easy to spot empty evidence). Propose PA-level at Gate 1.

3. **F2 (180)** — Weightings don't sum to 100. High severity (affects all scoring), low occurrence (CSV is usually correct), high detection (simple math check). ST2 catches it.

4. **F9 (180)** — Score outside rubric range. High severity (wrong grade), low occurrence (agent should stay in range), high detection (ST4 auto-correct). Mitigated structurally.

5. **F11 (168)** — Feedback contradicts score. High severity (confuses student), moderate occurrence (generative feedback can drift from scores), moderate detection (T10 alignment check catches most). Human resolves at Gate 1.

---

## Template Architecture

Seven template types provide structural enforcement for typed, consistent outputs.

### T1: Configuration Template

```python
class AssignmentConfiguration(BaseModel):
    brief_criteria: list[str]         # ["C1", "C2", "C3", "C4"]
    brief_requirements: list[str]    # Parsed from brief
    brief_references: list[str]      # Canvas references mentioned
    rubric_criteria: list[RubricCriterion]
    rubric_weightings: dict[str, int]  # {"C1": 30, "C2": 30, "C3": 20, "C4": 20}
    report_format: list[ReportField]
    total_weighting: int              # Must equal 100
    criteria_match: bool              # Brief criteria = rubric criteria?

class RubricCriterion(BaseModel):
    name: str                        # "C1"
    description: str                 # Full description
    weighting: int                   # 30
    levels: dict[str, str]           # {"HD": "...", "DI": "...", "CR": "...", "PA": "..."}

class ReportField(BaseModel):
    field_name: str                   # "C1 score out of 30"
    format_rule: str                 # "integer"
    source: str                      # "criterion_score"
```

### T2: Evidence Template

```python
class CriterionEvidence(BaseModel):
    student_id: str
    criterion: str                   # "C1"
    evidence_items: list[EvidenceItem]
    gaps_identified: list[str]        # What's missing
    visual_content_flagged: bool     # Charts/tables referenced but not extracted
    overall_assessment: str          # "strong" | "adequate" | "thin" | "absent"
    confidence: str                  # "high" | "medium" | "low"
    
class EvidenceItem(BaseModel):
    quote: str                       # Specific text from submission
    location: str                    # "slide 3, paragraph 2"
    relevance: str                   # "directly addresses" | "partially addresses" | "tangentially related"
```

### T3: Rubric Match Template

```python
class RubricLevelMatch(BaseModel):
    student_id: str
    criterion: str
    proposed_level: str              # "HD" | "DI" | "CR" | "PA"
    proposed_level_justification: str # Why this level
    alternative_level: str | None     # For boundary cases (F8)
    alternative_justification: str | None
    supporting_evidence: list[str]    # Quotes from submission
    gaps_against_higher: list[str]    # What's missing for next level up
    confidence: str                  # "high" | "medium" | "low"
```

### T4: Score Template

```python
class CriterionScore(BaseModel):
    student_id: str
    criterion: str
    level: str                       # "DI"
    level_range: tuple[int, int]     # (21, 24) for DI in C1/30
    proposed_score: int               # 22
    score_justification: str          # Why this specific number
    total_check: int | None           # Must equal sum of all criteria
```

### T5: Feedback Template

```python
class StudentFeedback(BaseModel):
    student_id: str
    criterion_feedback: dict[str, str] # {"C1": "...", "C2": "...", "C3": "...", "C4": "..."}
    overall_feedback: str
    evidence_citations: dict[str, list[str]]  # Per-criterion evidence references
    repetition_check: float          # Overlap % between criteria feedback
    specificity_check: bool           # Does feedback cite specific evidence?
    
class CriterionFeedbackDetail(BaseModel):
    criterion: str
    feedback: str
    evidence_cited: list[str]          # Specific quotes referenced
    rubric_gap_addressed: str         # What improvement is needed
    tone: str                         # "encouraging" — hardcoded
```

### T6: Alignment Check Template

```python
class AlignmentCheck(BaseModel):
    student_id: str
    checks: list[AlignmentItem]
    overall_aligned: bool
    flags: list[str]                   # Misalignments found

class AlignmentItem(BaseModel):
    criterion: str
    score_level: str                   # "DI"
    score_value: int                  # 22
    feedback_tone: str                 # "positive" | "neutral" | "negative" | "mixed"
    feedback_claims: list[str]         # Key claims in feedback
    alignment: str                    # "aligned" | "contradiction" | "weak"
    contradiction_detail: str | None  # Specific contradiction if found
```

### T7: Consistency Flag Template

```python
class ConsistencyFlag(BaseModel):
    current_student: str
    compared_students: list[str]       # At least 2 previous students
    criterion: str
    current_score: int
    compared_scores: list[int]
    current_evidence_summary: str
    compared_evidence_summaries: list[str]
    flag_type: str                     # "similarity_mismatch" | "boundary_inconsistency"
    running_inconsistency_count: int
    halt_threshold: int                # 3
    
class ConsistencyReport(BaseModel):
    total_flags: int
    inconsistency_count: int
    halt_triggered: bool
    flags: list[ConsistencyFlag]
```

---

## Fallback Model

Three tiers of fallback, escalating from self-correction to human intervention.

### Tier 1: Agent Self-Correction (no human involvement)

| Failure | Fallback | Condition |
|---|---|---|
| F9 (Score out of range) | Auto-correct score to nearest boundary | Always |
| F10 (Total miscalculation) | Auto-correct total | Always |
| F12 (Generic feedback) | Redraft with specificity instruction | ST6 triggers |
| F13 (Repetitive feedback) | Redraft with anti-repetition instruction | ST7 triggers |
| F8 (Ambiguous rubric level) | Present both options at Gate 1 | Low confidence match |

### Tier 2: Flag for Human Review (human decides, agent waits)

| Failure | Fallback | Condition |
|---|---|---|
| F3 (Format mismatch) | Flag; proceed if human confirms | ST3 trigger |
| F5 (Missing charts) | Flag at Gate 1 for C1/C4 | Visual content detected but not extracted |
| F6 (No evidence) | Propose PA-level at Gate 1 | Empty evidence for a criterion |
| F7 (Wrong criterion) | Flag at Gate 1 | Evidence seems misattributed |
| F11 (Feedback contradicts score) | Flag at Gate 1 | T10 alignment check detects |
| F14 (Genuine inconsistency) | Flag at Gate 2 | T12 rolling check detects |
| F15 (False positive flag) | Human dismisses at Gate 2 | Human decides |

### Tier 3: Halt and Wait for Human (workflow cannot proceed)

| Failure | Fallback | Condition |
|---|---|---|
| F1 (Brief-rubric mismatch) | HALT before marking starts | ST1 trigger |
| F2 (Weighting error) | HALT before marking starts | ST2 trigger |
| F4 (Extraction failure) | HALT for this student | Empty/garbled extraction |
| F16 (Batch halt) | GATE 3: halt entire batch | >3 inconsistencies |

### Recovery After Tier 3

| Halt Condition | Recovery Action | Resume Point |
|---|---|---|
| F1/F2: Config error | Human fixes brief or rubrics. Re-run T1-T4. | Stage 0 |
| F4: Extraction failure | Human re-uploads in different format or confirms manual extraction. | Step 2a |
| F16: Batch halt | Human reviews all flags. If systematic: fix root cause (e.g., rubric interpretation), reset counter. If not: accept flags, reset counter. | Current student |

---

## Cost Budget

### Per-Student Token Estimates

| Agent | Task | Estimated Tokens | Notes |
|---|---|---|---|
| Curator | T5+T6: Extract + evidence | 2,000-5,000 | Depends on submission length |
| Assessor | T7+T8: Rubric match + score | 3,000-6,000 | 4 criteria, each with evidence + rubric |
| Drafter | T9: Feedback (all criteria) | 4,000-8,000 | Holistic feedback for 4 criteria + overall |
| Verifier | T10: Alignment check | 1,500-3,000 | Comparing scores vs feedback vs evidence |
| Verifier | T12: Consistency check | 1,500-3,000 | Comparing against 2+ previous students |
| Compiler | T11+T13+T14: Assembly | 1,000-2,000 | Formatting only |
| **Per student total** | | **13,000-27,000** | |

### Batch-Level Estimates

| Component | Tokens |
|---|---|
| Configuration (T1-T4) | 3,000-5,000 |
| 30 students × 20,000 avg | 600,000 |
| Cohort report (T13-T14) | 5,000-8,000 |
| **Total batch** | **~608,000-613,000** |

### Budget Controls

| Control | Mechanism |
|---|---|
| Per-student ceiling | 30,000 tokens max per student. HALT if exceeded. |
| Per-criterion ceiling | 8,000 tokens max per criterion feedback. |
| Batch total ceiling | 700,000 tokens for 30-student batch. |
| Cost tracking | Track cumulative tokens per student and per batch. |

---

## Key Architectural Insight

**The three-tier fallback model mirrors the three human gates:**

- **Tier 1 (self-correction)** = no gate. Agent fixes its own mistakes without human involvement.
- **Tier 2 (flag for review)** = Gate 1 and Gate 2. Agent prepares judgment; human makes judgment.
- **Tier 3 (halt)** = Gate 3. System stops. Human must intervene before proceeding.

This is CAWDP's core principle structurally embedded in the fallback model: **the agent prepares, the human decides.** The system doesn't guess at boundaries — it escalates.

---

Ready for Phase 7 (Agent Design) where I'll write job descriptions for the 6 specialist agents?

---

## Run 6 — Agentic Expert ✓ COMPLETED

*2026-06-12T00:07:17* · `glm-5.1:cloud` · `d31d3576...`

### Prompt

Yes, agent job descriptions now

### Response

# Phase 7: Agent Design

## Agent Job Descriptions

---

## Agent 1: Configurator

### Identity

**Q1: What IS this agent?**
A structural validator that parses assignment configuration and checks alignment between brief, rubrics, and format. It never judges content quality — only structural consistency.

**Q2: What is its stance toward possibility?**
Constraint-oriented. It operates within declared boundaries (brief criteria, rubric weightings, format rules). It does not explore what the assignment could be; it validates what it is.

**Q3: What would VIOLATE its identity?**
Judging whether a criterion is well-designed. Approving misaligned configuration. Skipping a validation check because "it's probably fine." Modifying human-provided configuration without flagging.

**Q4: What would it mean for this agent to be WRONG?**
Missing a mismatch between brief and rubrics (worst case: all 30+ students marked against wrong criteria). Approving configuration that is internally inconsistent. The worst failure that looks like success is a configuration that passes validation but has a subtle weighting error that cascades through every student's grade.

**Q5: What's the hardest boundary moment?**
A configuration where brief criteria and rubric criteria almost match but differ in one criterion name or one percentage point. The temptation is to "close enough" rather than flag the mismatch.

### Specification

| Field | Value |
|---|---|
| **Class** | Aggregator |
| **Orientation** | Constraint |
| **Principal** | Human (lecturer) |
| **Inputs** | I1 Assignment brief markdown, I2 Rubrics CSV, I3 Report format markdown |
| **Outputs** | O10 Assignment Configuration |
| **Authority Boundary** | Validates and flags. **Never overrides** human configuration. **Never skips** validation checks. **Never modifies** human input. |
| **Hardest Boundary Moment** | Near-match criteria or weightings. Must flag, not auto-correct. |
| **Null State** | "No configuration provided. Please upload brief, rubrics, and format." |
| **Progressive Autonomy** | Shadow (first 2 assignments) → Advisory (next 2) → Supervised (next 2) → Autonomous (after 6 verified configurations). Per-dimension: criteria parsing = fast autonomous, weighting validation = always supervised, format alignment = advisory after 2. |

### Per-Dimension Progressive Autonomy

| Dimension | Shadow | Advisory | Supervised | Autonomous |
|---|---|---|---|---|
| Criteria parsing | Runs alongside, human confirms | Proposes, human confirms | Proposes, human spot-checks | Runs, flags anomalies |
| Weighting validation | Human checks every total | Proposes total, human confirms | Proposes total, human spot-checks | Runs, flags anomalies |
| Format alignment | Human checks every field | Proposes match, human confirms | Proposes match, human spot-checks | Runs, flags anomalies |

### Failure Mode & Recovery

| Failure Mode | What Goes Wrong | Detection | Recovery |
|---|---|---|---|
| Near-match not flagged | Criteria names differ by one word or punctuation | ST1 exact match check | **HALT.** Present mismatch to human. |
| Weighting off by 1% | Total is 99 or 101 | ST2 sum check | **HALT.** Present error to human. |
| Format field missed | Report format missing a criterion column | ST3 coverage check | **Warn.** Present missing fields. |

### Cost Budget

| Task | Token Estimate |
|---|---|
| T1 Parse brief | 1,000-2,000 |
| T2 Parse rubrics | 1,000-2,000 |
| T3 Parse format | 500-1,000 |
| T4 Validate config | 500-1,000 |
| **Total** | **3,000-6,000** |

### Information Boundaries

| Boundary | Regime | Enforcement |
|---|---|---|
| Never judges content quality | Declare | Prompt-level (Regime 1) |
| Never modifies human input | Prevent | Schema validation (Regime 3) — output must match input structure |
| Never skips validation | Prevent | System trigger (Regime 3) — ST1/ST2/ST3 are mandatory, not optional |

### Epistemic Metadata Profile

| Field | Profile |
|---|---|
| Confidence | Binary — configuration is valid or it isn't |
| Provenance | "Parsed from [filename]" for each field |
| Assumptions | "Assumed CSV delimiter is comma" |
| Limitations | "Cannot validate rubric content quality, only structural alignment" |
| Recency | Timestamp of configuration parse |
| Uncertainty | None for structural checks; "Near match: [detail]" for F1-type edge cases |

---

## Agent 2: Curator

### Identity

**Q1: What IS this agent?**
An evidence extractor that identifies and categorises what the student wrote relevant to each criterion. It reports what is there and what is missing. It never evaluates quality, never matches to rubrics, and never assigns levels.

**Q2: What is its stance toward possibility?**
Constraint-oriented. It operates within the boundaries of each criterion definition. It does not interpret whether evidence is "good enough" — it reports presence and relevance.

**Q3: What would VIOLATE its identity?**
Evaluating whether evidence is "strong" or "weak" (that's the Assessor's job). Matching evidence to a rubric level (that's the Assessor's job). Omitting evidence because it "doesn't seem important." Fabricating evidence that isn't in the submission.

**Q4: What would it mean for this agent to be WRONG?**
Missing relevant evidence (worst case: student gets a lower score because the Assessor never saw their work). Including irrelevant content (the Assessor wastes time reading material that doesn't address the criterion). Attributing evidence to the wrong criterion (cascading misalignment through scoring and feedback).

**Q5: What's the hardest boundary moment?**
Evidence that's relevant to two criteria. The temptation is to assign it to the one where it "fits better" rather than flagging it for both and letting the Assessor (and human at Gate 1) decide.

### Specification

| Field | Value |
|---|---|
| **Class** | Measurer |
| **Orientation** | Constraint |
| **Principal** | Human (lecturer) via Assessor |
| **Inputs** | O10 Assignment Configuration, student submission |
| **Outputs** | O6 Evidence Extraction per criterion |
| **Authority Boundary** | Extracts and categorises. **Never judges** quality. **Never matches** to rubric levels. **Never omits** relevant evidence. Reports what is there and what is missing. |
| **Hardest Boundary Moment** | Evidence relevant to multiple criteria. Flag for both, don't choose. |
| **Null State** | "No evidence found for [criterion name]. The submission may not address this criterion, or the relevant content may not have been extracted (see extraction note)." |
| **Progressive Autonomy** | Shadow (first 5 students) → Advisory (next 10) → Supervised (next 15) → Autonomous (after 30 verified). Per-dimension: extraction accuracy = fast autonomous, evidence categorisation = advisory after 10, gap identification = supervised after 15. |

### Per-Dimension Progressive Autonomy

| Dimension | Shadow | Advisory | Supervised | Autonomous |
|---|---|---|---|---|
| Extraction accuracy | Human checks every quote | Human checks key quotes | Human spot-checks | Runs, flags anomalies |
| Evidence categorisation | Human confirms every criterion assignment | Proposes categorisation, human confirms | Proposes, human spot-checks | Runs, flags anomalies |
| Gap identification | Human confirms every gap | Proposes gaps, human confirms | Proposes, human spot-checks | Runs, flags gaps |

### Failure Mode & Recovery

| Failure Mode | What Goes Wrong | Detection | Recovery |
|---|---|---|---|
| Missing relevant evidence | Student's work not extracted | Evidence count per criterion; cross-reference with submission length | **Flag at Gate 1.** Human verifies. |
| Irrelevant content included | Non-relevant text categorised under a criterion | Relevance check against criterion description | **Auto-filter** with low relevance scores. Flag uncertain items. |
| Evidence attributed to wrong criterion | Content for C2 filed under C1 | Cross-reference: does the quote address the criterion it's filed under? | **Flag at Gate 1.** Human reassigns. Re-run T7-T10 for affected criteria. |
| Multi-criterion evidence assigned to one | Evidence relevant to both C1 and C2 filed only under C1 | Overlap detection between criterion evidence | **Flag for both criteria.** Let Assessor and human decide. |
| Visual content not extracted | Charts/tables referenced but not captured | Detection of image/table references without corresponding text | **Flag at Gate 1** for C1 and C4 verification. |

### Cost Budget

| Task | Token Estimate |
|---|---|
| T5 Extraction | 1,000-3,000 |
| T6 Evidence per criterion | 1,000-2,000 |
| **Total** | **2,000-5,000** |

### Information Boundaries

| Boundary | Regime | Enforcement |
|---|---|---|
| Never judges quality | Declare | Prompt-level (Regime 1) |
| Never matches to rubric levels | Prevent | Output schema — no rubric level field in O6 (Regime 3) |
| Never omits relevant evidence | Detect | Evidence count per criterion flagged if 0 (Regime 2) |
| Never fabricates evidence | Prevent | Quote extraction — every evidence item must include direct quote (Regime 3) |

### Epistemic Metadata Profile

| Field | Profile |
|---|---|
| Confidence | Per-criterion: "high" (multiple strong matches), "medium" (some matches, some gaps), "low" (few matches, large gaps) |
| Provenance | "Extracted from submission page/paragraph [X]" |
| Assumptions | "Assumed relevance to [criterion] based on keyword/topic match" |
| Limitations | "Visual content (charts/tables) may not be fully represented" |
| Recency | Timestamp of extraction |
| Uncertainty | "Evidence for [criterion] is tangential — may not directly address the criterion" |

---

## Agent 3: Assessor

### Identity

**Q1: What IS this agent?**
A rubric level matcher and score proposer that evaluates extracted evidence against rubric descriptors. It proposes rubric levels and scores with reasoning. It never finalizes — the human decides at Gate 1.

**Q2: What is its stance toward possibility?**
Constraint-oriented. It operates within the boundaries of rubric level descriptors. It does not invent levels, stretch ranges, or propose scores outside defined boundaries.

**Q3: What would VIOLATE its identity?**
Finalizing a rubric match or score (human decides at Gate 1). Proposing a score outside the rubric level's range. Inventing a rubric level that doesn't exist. Marking down evidence to "make it fit" a lower level.

**Q4: What would it mean for this agent to be WRONG?**
Proposing the wrong rubric level (worst case: student gets DI when their work is HD, or vice versa). The worst failure that looks like success is a plausible-but-wrong level match — the reasoning sounds reasonable, the evidence seems to support it, but a domain expert would disagree.

**Q5: What's the hardest boundary moment?**
A student whose work sits at the boundary between two levels (e.g., high DI vs low HD). The temptation is to "round up" or "round down" rather than presenting both options with reasoning and letting the human decide.

### Specification

| Field | Value |
|---|---|
| **Class** | Assessor |
| **Orientation** | Constraint |
| **Principal** | Human (lecturer) |
| **Inputs** | O6 Evidence Extraction, O7 Rubric Level Match (own output), O10 Assignment Configuration |
| **Outputs** | O7 Rubric Level Match, O3 Per-Criterion Scores |
| **Authority Boundary** | Proposes levels and scores with reasoning. **Never finalizes.** **Never proposes outside rubric range.** Presents boundary cases as options. |
| **Hardest Boundary Moment** | Boundary between two rubric levels. Present both options. |
| **Null State** | "Insufficient evidence to propose a rubric level for [criterion]. Recommend PA (Pass) or flag for human review." |
| **Progressive Autonomy** | Shadow (first 5 students) → Advisory (next 10) → Supervised (next 15) → Autonomous (after 30 verified). Per-dimension: rubric matching = supervised after 15, score proposing = supervised after 15, boundary case handling = always present options. |

### Per-Dimension Progressive Autonomy

| Dimension | Shadow | Advisory | Supervised | Autonomous |
|---|---|---|---|---|
| Rubric level matching | Human confirms every level | Proposes levels, human confirms | Proposes, human spot-checks | Proposes, human reviews flags |
| Score within range | Human confirms every score | Proposes scores, human confirms | Proposes, human spot-checks | Proposes, human reviews flags |
| Boundary case handling | Always presents both options | Always presents both options | Always presents both options | Always presents both options — **never autonomous** |

### Failure Mode & Recovery

| Failure Mode | What Goes Wrong | Detection | Recovery |
|---|---|---|---|
| Wrong rubric level | Evidence matched to wrong level descriptor | Human at Gate 1 | Human adjusts. Record adjustment for consistency tracking. |
| Score outside rubric range | Proposed score doesn't fit the level | ST4 auto-correct | Auto-correct to boundary. Flag at Gate 1. |
| Boundary case forced to one level | Ambiguous work assigned to one level without options | Low confidence flag | Present both options at Gate 1. |
| Level justified by cherry-picked evidence | Only supporting evidence cited; contradictory evidence omitted | Verifier checks (T10) | Flag at Gate 1. |

### Cost Budget

| Task | Token Estimate |
|---|---|
| T7 Rubric match per criterion × 4 | 2,000-4,000 |
| T8 Score per criterion × 4 | 1,000-2,000 |
| **Total** | **3,000-6,000** |

### Information Boundaries

| Boundary | Regime | Enforcement |
|---|---|---|
| Never finalizes | Prevent | Output schema includes `proposed_level` not `final_level` (Regime 3) |
| Never proposes outside rubric range | Prevent | ST4 system trigger auto-corrects (Regime 3) |
| Presents boundary cases as options | Prevent | Schema includes `alternative_level` for low-confidence matches (Regime 3) |
| Never cherry-picks evidence | Detect | Verifier checks evidence completeness (Regime 2) |

### Epistemic Metadata Profile

| Field | Profile |
|---|---|
| Confidence | Per-criterion: "high" (clear match), "medium" (reasonable match), "low" (boundary case) |
| Provenance | "Based on evidence item [X] from Curator extraction" |
| Assumptions | "Assumed student intended [X] based on context" |
| Limitations | "Level match is provisional — human confirmation required at Gate 1" |
| Recency | Timestamp of assessment |
| Uncertainty | "This criterion sits at the boundary between DI and HD. Both options presented." |

---

## Agent 4: Drafter

### Identity

**Q1: What IS this agent?**
A feedback writer that produces cohesive per-criterion and overall feedback citing specific evidence from the student's submission. It sees ALL evidence before writing any feedback (Q3 constraint). It never fabricates evidence, never repeats across criteria, and never contradicts scores.

**Q2: What is its stance toward possibility?**
Constraint-oriented. It operates within the boundaries of: specific evidence (what the student actually wrote), the proposed rubric levels and scores, and the rubric descriptors. It does not invent compliments, invent criticisms, or write generic advice that could apply to any student.

**Q3: What would VIOLATE its identity?**
Fabricating evidence not in the submission. Repeating the same point across multiple criteria. Writing feedback that contradicts the proposed score (e.g., praising work that scored CR). Writing generic feedback that could apply to any student. Using a discouraging or condescending tone.

**Q4: What would it mean for this agent to be WRONG?**
Feedback that contradicts the score (worst case: student sees "strong work" but score is CR, trusts the feedback over the score). The worst failure that looks like success is feedback that sounds specific and professional but could apply to any student — it cites the rubric but not the student's actual evidence.

**Q5: What's the hardest boundary moment?**
A student whose work is genuinely weak across all criteria. The temptation is to soften feedback with vague encouragement rather than honestly stating what's missing with specific evidence — while maintaining an encouraging tone that doesn't condescend.

### Specification

| Field | Value |
|---|---|
| **Class** | Generator |
| **Orientation** | Constraint |
| **Principal** | Human (lecturer) |
| **Inputs** | O6 Evidence (ALL criteria), O7 Rubric Matches (ALL criteria), O3 Scores (ALL criteria), O10 Configuration |
| **Outputs** | O4 Per-Criterion Feedback, O5 Overall Feedback |
| **Authority Boundary** | Drafts feedback citing specific evidence. **Never fabricates.** **Never repeats.** **Never contradicts scores.** **Never uses discouraging tone.** Every claim must cite evidence. |
| **Hardest Boundary Moment** | Genuinely weak student work — maintaining honest specificity without condescension. |
| **Null State** | "Unable to draft feedback for [criterion] — insufficient evidence extracted. Recommend human review of raw submission." |
| **Progressive Autonomy** | Shadow (first 5 students) → Advisory (next 10) → Supervised (next 15) → Autonomous (after 30 verified). Per-dimension: evidence citation = fast autonomous, tone calibration = advisory after 10, boundary case feedback = always present options. |

### Per-Dimension Progressive Autonomy

| Dimension | Shadow | Advisory | Supervised | Autonomous |
|---|---|---|---|---|
| Evidence citation | Human verifies every citation | Human checks key citations | Human spot-checks | Runs, flags uncited claims |
| Tone calibration | Human reviews tone | Proposes tone, human confirms | Proposes, human spot-checks | Runs, flags tone issues |
| Boundary case feedback | Always presents two options | Always presents two options | Always presents two options | Always presents two options — **never autonomous** |
| Cohesion (no repetition) | Human checks for repetition | ST7 auto-check + human spot-check | ST7 auto-check + human spot-check | ST7 auto-check, flags to human |

### Failure Mode & Recovery

| Failure Mode | What Goes Wrong | Detection | Recovery |
|---|---|---|---|
| Fabricated evidence | Feedback cites content not in submission | Verifier cross-checks citations against O6 | **Auto-redraft** with explicit instruction to cite only O6 evidence. Flag to human. |
| Generic/unsupported feedback | Feedback could apply to any student | ST6 specificity check: does feedback reference specific evidence? | **Auto-redraft** with explicit instruction to cite specific quotes. |
| Repetitive feedback | Same point made across C1-C4 | ST7 repetition check: overlap >30% between criteria | **Auto-redraft** with instruction to differentiate across criteria. |
| Score-feedback contradiction | Feedback praises what the score penalises | T10 alignment check | **Flag at Gate 1.** Human resolves. Must fix before proceeding. |
| Discouraging tone | Feedback is harsh or condescending | Tone check against rubric level (PA feedback should still be constructive) | **Auto-redraft** with explicit instruction to maintain encouraging but honest tone. |

### Cost Budget

| Task | Token Estimate |
|---|---|
| T9 Feedback (all criteria + overall) | 4,000-8,000 |
| **Total** | **4,000-8,000** |

### Information Boundaries

| Boundary | Regime | Enforcement |
|---|---|---|
| Never fabricates evidence | Prevent | Output schema requires `evidence_cited` field referencing O6 items (Regime 3) |
| Never repeats across criteria | Prevent | ST7 repetition check with auto-redraft (Regime 3) |
| Never contradicts scores | Detect | T10 alignment check (Regime 2) |
| Never uses discouraging tone | Declare | Prompt-level (Regime 1) — reinforced by tone check in output schema |

### Epistemic Metadata Profile

| Field | Profile |
|---|---|
| Confidence | Per-criterion: "high" (specific evidence cited, clear feedback), "medium" (some evidence cited, some generic), "low" (limited evidence, mostly generic) |
| Provenance | "Based on evidence item [X] from Curator extraction, rubric level [Y] from Assessor" |
| Assumptions | "Assumed student's intent based on context" |
| Limitations | "Visual content (charts/tables) not fully extracted — feedback may be incomplete for C1 and C4" |
| Recency | Timestamp of draft |
| Uncertainty | "Feedback for [criterion] is based on limited evidence — human review recommended" |

---

## Agent 5: Verifier

### Identity

**Q1: What IS this agent?**
An alignment and consistency checker that verifies score-feedback alignment within a student and consistency across students. It flags mismatches, contradictions, and statistical outliers. It never adjusts scores, never rewrites feedback, and never decides if a flag is a real inconsistency — it prepares judgment, the human decides.

**Q2: What is its stance toward possibility?**
Adversarial — but constructively. It actively looks for problems. Its job is to find what might be wrong, not to confirm what's right. It is the quality control layer.

**Q3: What would VIOLATE its identity?**
Adjusting scores or rewriting feedback (that's the human's role at gates). Suppressing a flag because "it's probably fine." Deciding that a consistency flag is a real inconsistency (that's the human's role at Gate 2). Letting a genuine inconsistency pass because the batch is almost done.

**Q4: What would it mean for this agent to be WRONG?**
Missing a score-feedback contradiction (the student gets contradictory information). Missing a genuine consistency issue (two students with similar work get different grades). The worst failure that looks like success is flagging everything — creating noise that trains the human to ignore flags, which means genuine issues get dismissed.

**Q5: What's the hardest boundary moment?**
A consistency flag that might be a legitimate difference or might be a real inconsistency. The temptation is to either over-flag (creating noise) or under-flag (missing issues). The correct action is to present the comparison with evidence and let the human decide at Gate 2.

### Specification

| Field | Value |
|---|---|
| **Class** | Assessor (adversarial orientation) |
| **Orientation** | Adversarial (constructive) |
| **Principal** | Human (lecturer) |
| **Inputs** | T10: O3 Scores + O4/O5 Feedback + O6 Evidence (per-student alignment); T12: Current O3 + Previous O3s (cross-student consistency) |
| **Outputs** | T10: O8 Alignment Check; T12: Consistency Flags + running counter |
| **Authority Boundary** | Flags only. **Never adjusts** scores. **Never rewrites** feedback. **Never decides** if a flag is a real inconsistency. Presents comparisons with evidence. Counts inconsistencies. |
| **Hardest Boundary Moment** | Ambiguous consistency flag — present comparison, let human decide. |
| **Null State** | "No alignment issues found for [student]. No consistency flags in this batch." |
| **Progressive Autonomy** | Shadow (first 5 students) → Advisory (next 10) → Supervised (next 15) → Autonomous (after 30 verified). Per-dimension: alignment checking = supervised after 10, consistency checking = supervised after 15, flag counting = always autonomous (it's mechanical). |

### Per-Dimension Progressive Autonomy

| Dimension | Shadow | Advisory | Supervised | Autonomous |
|---|---|---|---|---|
| Score-feedback alignment | Human checks every flag | Proposes flags, human confirms | Proposes, human spot-checks | Proposes, human reviews flags |
| Cross-student consistency | Human checks every comparison | Proposes flags, human confirms | Proposes, human spot-checks | Proposes, human reviews flags |
| Inconsistency counting | Always autonomous | Always autonomous | Always autonomous | Always autonomous — it's mechanical |

### Failure Mode & Recovery

| Failure Mode | What Goes Wrong | Detection | Recovery |
|---|---|---|---|
| Missed alignment issue | Score says DI but feedback says "needs improvement" | Cross-reference score level vs feedback tone/claims | **Increase detection sensitivity.** Flag at Gate 1. |
| Over-flagging | Every minor variation flagged as inconsistency | Human dismisses flags (F15 false positive) | **Calibrate threshold.** Only flag when evidence similarity is high AND score difference is significant. |
| Under-flagging | Real inconsistency not caught | Two students with similar evidence get very different scores, no flag raised | **Lower similarity threshold.** Human catches it in manual review. |
| False positive consistency flag | Different quality work flagged as inconsistent | Human reviews at Gate 2 and dismisses | **No action needed.** This is the system working correctly — human decides. |

### Cost Budget

| Task | Token Estimate |
|---|---|
| T10 Alignment check | 1,500-3,000 |
| T12 Consistency check | 1,500-3,000 |
| **Total** | **3,000-6,000** |

### Information Boundaries

| Boundary | Regime | Enforcement |
|---|---|---|
| Never adjusts scores | Prevent | Output schema has no score field in O8 (Regime 3) |
| Never rewrites feedback | Prevent | Output schema has no feedback field in O8 (Regime 3) |
| Never decides if flag is real | Prevent | Output schema includes `flag_type` and `evidence_comparison` but no `is_real_inconsistency` field (Regime 3) |
| Flags everything above threshold | Detect | Similarity threshold calibrated during progressive autonomy (Regime 2) |

### Epistemic Metadata Profile

| Field | Profile |
|---|---|
| Confidence | Per-flag: "high" (clear misalignment or inconsistency), "medium" (possible issue), "low" (borderline — may be legitimate difference) |
| Provenance | "Based on comparison between [Student A] and [Students B, C]" or "Based on cross-reference of O3 and O4/O5 for [student]" |
| Assumptions | "Assumed similar evidence quality based on [rubric level match]" |
| Limitations | "Consistency check is based on rubric level matches, not direct submission comparison" |
| Recency | Timestamp of check |
| Uncertainty | "This flag may be a legitimate difference in quality — human review recommended" |

---

## Agent 6: Compiler

### Identity

**Q1: What IS this agent?**
A structural assembler that compiles approved components into the final report format. It formats, calculates totals, and assembles entries. It never adds content, never changes scores, and never interprets — it puts approved pieces in the right places.

**Q2: What is its stance toward possibility?**
Constraint-oriented. It operates within the format template. It does not add, modify, or interpret content — it assembles exactly what was approved at the gates.

**Q3: What would VIOLATE its identity?**
Adding content that wasn't in the approved components. Modifying a score that the human approved. Changing feedback text. Interpreting ambiguous data instead of flagging it. Omitting an entry that was approved.

**Q4: What would it mean for this agent to be WRONG?**
Formatting errors that make the report unusable (worst case: wrong student data in the wrong row). The worst failure that looks like success is a report that looks correct but has a total that doesn't sum correctly — it looks professional but the math is wrong.

**Q5: What's the hardest boundary moment?**
A score that was adjusted by the human at Gate 1 but the old score is still in the pipeline. The temptation is to "use the newer number" without verifying the full entry was updated consistently.

### Specification

| Field | Value |
|---|---|
| **Class** | Aggregator |
| **Orientation** | Constraint |
| **Principal** | Human (lecturer) |
| **Inputs** | Approved O3 Scores, O4+O5 Feedback, O10 Configuration, O9 Cohort Report |
| **Outputs** | O2 Student Marking Entry, O1 Final Markdown Report |
| **Authority Boundary** | Assembles only. **Never adds** content. **Never changes** scores or feedback. **Never interprets** ambiguous data. **Never omits** approved entries. |
| **Hardest Boundary Moment** | Human-adjusted score that hasn't propagated to all dependent fields. Verify all fields are consistent. |
| **Null State** | "No approved entries to assemble. Complete Gate 1 for all students before assembly." |
| **Progressive Autonomy** | Shadow (first 5 entries) → Advisory (next 10) → Supervised (next 15) → Autonomous (after 30 verified entries). Per-dimension: formatting = fast autonomous, total calculation = always verified, entry assembly = supervised after 15, report assembly = supervised after 15. |

### Per-Dimension Progressive Autonomy

| Dimension | Shadow | Advisory | Supervised | Autonomous |
|---|---|---|---|---|
| Entry formatting | Human checks every entry | Proposes, human confirms | Proposes, human spot-checks | Runs, flags anomalies |
| Total calculation | Human checks every total | Proposes, human confirms | Proposes, human spot-checks | Runs, auto-verifies with ST5 |
| Report assembly | Human checks full report | Proposes, human confirms | Proposes, human spot-checks | Runs, flags anomalies |

### Failure Mode & Recovery

| Failure Mode | What Goes Wrong | Detection | Recovery |
|---|---|---|---|
| Wrong student data in wrong row | Student A's data appears in Student B's row | ST5 total check; cross-reference student IDs | **HALT assembly.** Re-verify all entries. |
| Total doesn't sum correctly | C1+C2+C3+C4 ≠ total | ST5 total check | **Auto-correct.** Flag for human verification. |
| Missing entry | Approved student not in final report | Entry count vs approved count | **HALT assembly.** Identify missing entry. |
| Human adjustment not propagated | Score changed at Gate 1 but old score in assembly | Cross-reference approved scores vs assembled scores | **Auto-update.** Flag for human verification. |

### Cost Budget

| Task | Token Estimate |
|---|---|
| T11 Assemble entry | 500-1,000 |
| T13 Cohort report | 2,000-4,000 |
| T14 Final report | 1,000-2,000 |
| **Total** | **3,500-7,000** |

### Information Boundaries

| Boundary | Regime | Enforcement |
|---|---|---|
| Never adds content | Prevent | Output schema has no free-text fields beyond approved components (Regime 3) |
| Never changes scores | Prevent | Assembly uses approved O3 scores directly (Regime 3) |
| Never omits entries | Detect | Entry count check against approved count (Regime 2) |
| Never interprets | Prevent | No interpretation fields in output schema (Regime 3) |

### Epistemic Metadata Profile

| Field | Profile |
|---|---|
| Confidence | Binary — assembly is deterministic. Either all entries assembled correctly or not. |
| Provenance | "Assembled from approved O3, O4, O5, O10 components" |
| Assumptions | "All components were approved at Gate 1" |
| Limitations | "Cannot verify content accuracy — only structural correctness" |
| Recency | Timestamp of assembly |
| Uncertainty | None — assembly is deterministic |

---

## Agent Roster Summary

| Agent | Class | Orientation | Worst Failure That Looks Like Success | Hardest Boundary Moment | Null State |
|---|---|---|---|---|---|
| **Configurator** | Aggregator | Constraint | Config that passes validation but has subtle weighting error | Near-match criteria/weightings — flag, don't auto-correct | "No configuration provided" |
| **Curator** | Measurer | Constraint | Complete evidence extraction that misses relevant content | Evidence relevant to two criteria — flag for both | "No evidence found for [criterion]" |
| **Assessor** | Assessor | Constraint | Plausible-but-wrong rubric level with reasonable justification | Boundary between two levels — present both options | "Insufficient evidence to propose level" |
| **Drafter** | Generator | Constraint | Specific-sounding feedback that could apply to any student | Genuinely weak work — honest specificity without condescension | "Unable to draft feedback — recommend human review" |
| **Verifier** | Assessor | Adversarial | Over-flagging that trains humans to ignore flags | Ambiguous consistency flag — present comparison, let human decide | "No issues found" |
| **Compiler** | Aggregator | Constraint | Professional-looking report with wrong total | Human-adjusted score not propagated — verify consistency | "No approved entries to assemble" |

### CC-1 Verification Independence Enforcement

| Production | Verification |
|---|---|
| Curator (extracts evidence) | Assessor (matches evidence to rubrics) |
| Assessor (proposes levels + scores) | Verifier (checks alignment + consistency) |
| Drafter (writes feedback) | Verifier (checks feedback vs scores) |

**No agent verifies its own output.** The Curator's evidence is verified by the Assessor's rubric matching. The Assessor's scores are verified by the Verifier's alignment check. The Drafter's feedback is verified by the Verifier's alignment check. The Compiler's assembly is verified by ST5 (total check).

---

Ready for Phase 8 (Human Experience Design)?

---

## Run 7 — Agentic Expert ✓ COMPLETED

*2026-06-12T00:13:37* · `glm-5.1:cloud` · `45bb51c0...`

### Prompt

Continue to phase 8

### Response

# Phase 8: Human Experience Design

## Cognitive Load Budget

### Decision Budget Per Session

| Session | Decisions | Time | Notes |
|---|---|---|---|
| Configuration (once) | 2-3 | 5-10 min | Verify brief-rubric alignment, confirm weightings, confirm format |
| Gate 1 (per student) | 12-16 | 3-5 min | 4 criteria × 3-4 decisions each (level, score, feedback) |
| Gate 2 (conditional) | 1-2 | 1-2 min | Is this flag a real inconsistency? |
| Gate 3 (rare) | 1-3 | 5-10 min | Is there a systematic issue? Fix or accept? |
| Cohort review (once) | 2-3 | 5-10 min | Review distributions, confirm outliers, approve final report |

### Per-Student Decision Breakdown (Gate 1)

For a 4-criterion assignment, the human makes these decisions at Gate 1:

| Decision Type | Count | Cognitive Load | Notes |
|---|---|---|---|
| Rubric level confirmation | 4 | Low-Medium | Confirm or adjust each criterion level |
| Score confirmation | 4 | Low | Confirm or adjust each score (usually quick if level is right) |
| Feedback review | 1-2 | Medium | Review overall feedback; per-criterion usually scan-only |
| Alignment flags | 0-2 | Low | Usually 0; quick check if flagged |
| **Total Gate 1** | **~12** | **Medium** | 3-5 minutes with agent prep |

### Session-Level Budget (30 Students)

| Segment | Decisions | Time | Cognitive Load |
|---|---|---|---|
| Configuration | 2-3 | 5-10 min | Low |
| Students 1-10 | ~120-160 | 30-50 min | Medium (fresh, learning pattern) |
| Break (recommended) | — | 10 min | — |
| Students 11-20 | ~120-160 | 30-50 min | Medium (pattern established) |
| Break (recommended) | — | 10 min | — |
| Students 21-30 | ~120-160 | 30-50 min | Medium-High (fatigue factor) |
| Gate 2 reviews | 0-5 | 0-10 min | Low (most won't trigger) |
| Gate 3 review | 0-1 | 0-10 min | High (rare, but requires deep review) |
| Cohort review | 2-3 | 5-10 min | Medium |
| **Total** | **~250-330** | **~2-3.5 hrs** | |

### Cognitive Load Management

| Principle | Implementation |
|---|---|
| **One clear next step** | Gate 1 always presents one student at a time. No need to hold multiple students in working memory. |
| **Visibility as memory** | Previous students' scores visible as rolling reference (not full comparison — just score + level). |
| **Zero-friction capture** | Human decisions at Gate 1 are single clicks: Accept / Adjust / Reject. Adjust opens inline edit. No navigation required. |
| **Shame-free failure states** | "I need to review the submission directly" is a first-class option at every decision point. No penalty. |
| **Replanning as normal** | Significant adjustments at Gate 1 feed back into consistency tracking. No need to undo previous decisions — the system adapts. |
| **Engagement over priority** | The agent prepares all options. The human makes judgment calls — the interesting part. Mechanical work (assembly, totals, formatting) is invisible. |
| **Predictability as safety** | Every student follows the same Gate 1 pattern. Same structure, same options, same layout. Predictable reduces cognitive load. |

---

## Interface Specification

### Gate 0: Configuration Review

**When:** Once per assignment, before any marking begins.

**What the human sees:**

```
══════════════════════════════════════════════════
CONFIGURATION REVIEW
══════════════════════════════════════════════════

BRIEF SUMMARY:
  Criteria: C1, C2, C3, C4
  References: [list of Canvas references from brief]

RUBRIC ALIGNMENT:
  ✅ Brief criteria match rubric criteria
  ✅ Weightings sum to 100: C1=30, C2=30, C3=20, C4=20
  ✅ Format covers all rubric criteria

WEIGHTINGS:
  C1 (30%) — Accurately curates and reports relevant technical information
  C2 (30%) — Critically analyses and synthesises concepts
  C3 (20%) — Applies concepts to real-world contexts
  C4 (20%) — Presents information clearly and cohesively

FORMAT FIELDS:
  [list of fields the report will include]

══════════════════════════════════════════════════
OPTIONS:
  A) ✅ Configuration confirmed — proceed to marking
  B) ⚠️ Configuration needs changes — [describe]
══════════════════════════════════════════════════
```

**If alignment fails:**

```
══════════════════════════════════════════════════
⚠️ CONFIGURATION ISSUE
══════════════════════════════════════════════════

BRIEF has criterion: "critical_analysis"
RUBRIC has criterion: "C2_critical_analyss"
                    ^--- spelling mismatch

Weightings: C1=30, C2=30, C3=20, C4=20, Total = 98
                                                    ^^--- doesn't sum to 100

══════════════════════════════════════════════════
This must be fixed before marking can begin.

Options:
  A) I'll fix the brief/rubrics and re-upload
  B) I'll proceed anyway (not recommended)
══════════════════════════════════════════════════
```

---

### Gate 1: Per-Student Review

**When:** After T10 (alignment check) for each student.

**What the human sees (one criterion at a time, scrollable):**

```
══════════════════════════════════════════════════
STUDENT: [Name/ID]                    [3/30] 🟢
══════════════════════════════════════════════════

C1 (30%) — Accurately curates and reports relevant technical information
──────────────────────────────────────────────────

EVIDENCE EXTRACTED:
  • "Blockchain is a distributed ledger technology..." (slide 2)
  • "Smart contracts enable automated execution..." (slide 3)
  • Gap identified: DeFi protocols mentioned but not explained

PROPOSED LEVEL: DI (70-79%)
  Reasoning: Technical information is effective and generally well-applied,
  but lacks depth in DeFi protocols and smart contract mechanics.

PROPOSED SCORE: 22/30
  Reasoning: Solid DI performance. Lower end of DI range due to
  thin coverage of DeFi and smart contracts.

Options:
  A) ✅ Accept DI, 22/30
  B) 🔄 Accept DI, adjust score to ___/30
  C) 🔄 Adjust to different level:
     [HD] [CR] [PA]
  D) 📄 I need to review the submission directly

──────────────────────────────────────────────────

C2 (30%) — Critically analyses and synthesises concepts
──────────────────────────────────────────────────

EVIDENCE EXTRACTED:
  • "The decentralised nature of blockchain provides trust..." (slide 4)
  • "However, this comes at the cost of scalability..." (slide 4)
  • Gap: Limited synthesis across multiple sources

PROPOSED LEVEL: CR (60-69%)
  Reasoning: Analysis is present but tends toward description rather
  than deep synthesis. Connection across concepts is developing.

PROPOSED SCORE: 19/30
  Reasoning: Mid-range CR. Some analysis present but synthesis
  could be deeper.

Options:
  A) ✅ Accept CR, 19/30
  B) 🔄 Accept CR, adjust score to ___/30
  C) 🔄 Adjust to different level:
     [HD] [DI] [PA]
  D) 📄 I need to review the submission directly

──────────────────────────────────────────────────

[... C3, C4 ...]

OVERALL FEEDBACK DRAFT:
──────────────────────────────────────────────────
Your report demonstrates a solid understanding of blockchain
fundamentals, with effective coverage of distributed ledger
technology and smart contracts. The analysis in Section 2
shows developing critical thinking, particularly around the
trust-scalability trade-off. To strengthen the work:
(1) deepen coverage of DeFi protocols, (2) build synthesis
across multiple sources rather than analysing each separately,
(3) connect theoretical concepts more explicitly to the
Australian financial services context you mention.

Options:
  A) ✅ Accept feedback as-is
  B) 🔄 Edit feedback inline: [text area]
  C) 🔄 Redraft with direction: [text area]
  D) 📄 I need to review the submission directly

══════════════════════════════════════════════════
ALIGNMENT CHECK: ✅ No issues | ⚠️ 1 flag
[If flagged: C2 feedback tone doesn't match CR score]
══════════════════════════════════════════════════

[◄ Previous Student]  [Save & Continue ►]
══════════════════════════════════════════════════
```

**Key design decisions:**

1. **Decision Presentation Pattern**: Every judgment point offers 2-4 structured options (Accept/Adjust/Reject/Review directly). Never an open question.

2. **Evidence always visible**: The human never has to trust the agent's word. Evidence quotes are shown for every rubric level match.

3. **Alignment flag inline**: If T10 detects a score-feedback contradiction, it appears at the bottom of the same screen. No separate navigation.

4. **Progress indicator**: `[3/30]` shows position in batch. Green/yellow/red based on consistency counter.

5. **"Review submission directly" is always available**: A first-class option at every decision point. No penalty, no shame.

6. **Inline editing**: "Adjust score" opens a number input inline. "Edit feedback" opens a text area inline. No page navigation.

---

### Gate 2: Consistency Flag Review (Conditional)

**When:** Only if T12 flags a consistency issue between current and previous students.

**What the human sees:**

```
══════════════════════════════════════════════════
⚠️ CONSISTENCY FLAG
══════════════════════════════════════════════════

C2 (30%) — Critically analyses and synthesises concepts

CURRENT STUDENT: [Student 3]
  Score: 19/30 (CR level)
  Evidence: "developing analysis, limited synthesis across sources"

COMPARED TO: [Student 1]
  Score: 22/30 (DI level)
  Evidence: "developing analysis, limited synthesis across sources"

The quality of analysis appears similar, but scores differ by 3 points.

══════════════════════════════════════════════════
Options:
  A) ✅ Legitimate difference — the quality IS different
  B) 🔄 Inconsistency — adjust [Student 3]'s score to ___/30
  C) 🔄 Inconsistency — adjust [Student 1]'s score to ___/30
  D) 📄 I need to review both submissions directly
══════════════════════════════════════════════════
```

**Design decisions:**

1. **Both students' evidence shown side-by-side**: The human can compare directly without navigating.

2. **Options include adjusting EITHER student**: The inconsistency might be in either direction.

3. **"Review both submissions" available**: Same first-class option as Gate 1.

4. **Decision is recorded**: Whatever the human decides feeds back into the consistency counter.

---

### Gate 3: Batch Halt (Rare)

**When:** Inconsistency counter exceeds 3.

**What the human sees:**

```
══════════════════════════════════════════════════
🛑 BATCH HALT: 4 CONSISTENCY FLAGS
══════════════════════════════════════════════════

The consistency counter has exceeded 3 flags.
This may indicate a systematic issue with rubric interpretation.

FLAGS SUMMARY:
  1. Students 2 vs 1, C1: Similar evidence, 4-point difference (DI vs CR)
  2. Students 3 vs 1, C2: Similar evidence, 3-point difference
  3. Students 5 vs 2, C3: Similar description, different scores
  4. Students 7 vs 3, C2: Similar analysis, 3-point difference

PATTERN ANALYSIS:
  3 of 4 flags involve C2 (synthesis criterion)
  Average score difference: 3.5 points
  Possible systematic issue: C2 rubric interpretation

══════════════════════════════════════════════════
Options:
  A) 🔧 Fix systematic issue — I'll review C2 interpretation
     (Counter resets. Affected students will be re-assessed.)
  B) ✅ Accept flags as legitimate differences
     (Counter resets. Continue marking.)
  C) 📄 I need to review all flagged submissions
══════════════════════════════════════════════════
```

**Design decisions:**

1. **Pattern analysis provided**: The agent doesn't just flag — it analyses whether there's a systematic issue (3 of 4 flags on C2).

2. **Fix is the preferred option**: The system suggests reviewing the systematic issue, not just accepting flags.

3. **Counter resets either way**: After the halt, the counter resets. This prevents compounding from the same root cause.

---

### Cohort Review Screen

**When:** After all students processed.

**What the human sees:**

```
══════════════════════════════════════════════════
COHORT QUALITY ASSURANCE
══════════════════════════════════════════════════

SCORE DISTRIBUTION (30 students):
  C1 (30%):  Mean 21.3 | HD: 4 | DI: 12 | CR: 10 | PA: 4
  C2 (30%):  Mean 18.7 | HD: 2 | DI: 8  | CR: 14 | PA: 6
  C3 (20%):  Mean 13.2 | HD: 3 | DI: 9  | CR: 12 | PA: 6
  C4 (20%):  Mean 12.8 | HD: 2 | DI: 7  | CR: 15 | PA: 6

TOTAL:       Mean 66.0 | HD: 1 | DI: 7  | CR: 15 | PA: 7

OUTLIERS FLAGGED:
  • Student 15: Total 89 (HD) — 2+ SD above mean
  • Student 28: Total 45 (PA) — 2+ SD below mean

CONSISTENCY SUMMARY:
  Flags raised: 4 (3 legitimate differences, 1 adjusted)
  Adjustments made: 1 (Student 3, C2: CR 18 → DI 21)
  Batch halts: 1 (C2 interpretation reviewed)

══════════════════════════════════════════════════
Options:
  A) ✅ Approve final report
  B) 🔄 Review outliers before approving
  C) 📄 Export cohort data for manual analysis
══════════════════════════════════════════════════
```

---

## Override Mechanisms

### Override Types

| Override | When | How | System Response |
|---|---|---|---|
| **Adjust Score** | Gate 1 | Select option B, enter new score within rubric range | System validates range, records adjustment, feeds into consistency tracking |
| **Adjust Level** | Gate 1 | Select option C, choose different level | System recalculates score range, presents range for new level |
| **Edit Feedback** | Gate 1 | Select option B under feedback | System keeps evidence citations, records edit percentage |
| **Redraft Feedback** | Gate 1 | Select option C under feedback, provide direction | System re-generates with specific direction |
| **Review Submission** | Any gate | Select option D ("I need to review the submission directly") | System pauses workflow, opens submission for human review |
| **Dismiss Flag** | Gate 2 | Select option A ("Legitimate difference") | System records dismissal, increments counter but marks as resolved |
| **Adjust Previous Student** | Gate 2 | Select option B or C | System records adjustment, flags for consistency re-check |
| **Fix Systematic Issue** | Gate 3 | Select option A | System resets counter, marks affected students for re-assessment |
| **Accept All Flags** | Gate 3 | Select option B | System resets counter, continues marking |

### Override Capture

Every human override is recorded with:

| Field | Value |
|---|---|
| `student_id` | Which student |
| `criterion` | Which criterion (if applicable) |
| `override_type` | score_adjustment, level_change, feedback_edit, flag_dismissal, systematic_fix |
| `original_value` | What the agent proposed |
| `override_value` | What the human decided |
| `reasoning` | Optional: human can provide reasoning |
| `timestamp` | When the override occurred |
| `consistency_impact` | Whether this creates a new consistency flag |

This data feeds into:
- T12 rolling consistency check (significant adjustments may create new flags)
- Progressive autonomy promotion decisions (patterns in overrides indicate where the agent needs improvement)
- Specification aging (if overrides cluster in a specific area, the agent's specification needs review)

---

## System Empowerment Assessment

### System Empowerment Index (SEI)

| Dimension | Level | Evidence |
|---|---|---|
| **Time saved** | Amplifying | Agent handles extraction, evidence matching, rubric level proposals, score proposals, feedback drafting, alignment checking, consistency tracking. Human handles judgment calls only. Estimated 35-50% time reduction vs fully manual marking. |
| **Decision quality** | Enabling | Evidence is always cited. Rubric levels are proposed with reasoning. Consistency is tracked across students. The human makes better decisions because relevant information is surfaced, not because decisions are made for them. |
| **Cognitive load** | Enabling | 3-5 minutes per student at Gate 1 (vs 15-20 minutes fully manual). Decisions are structured (Accept/Adjust/Reject/Review). Evidence is pre-extracted and displayed. |
| **Consistency** | Amplifying | Rolling consistency check catches grade drift that individual markers miss. Batch halt prevents systematic bias from compounding. |
| **Creative freedom** | Liberating | Human focuses on judgment — the interesting part of marking. Mechanical work (extraction, assembly, totals, formatting) is invisible. Human has full control over every rubric level, score, and feedback decision. |
| **Error reduction** | Amplifying | ST1-ST10 catch structural errors (mismatched criteria, wrong totals, score-feedback contradictions, consistency drift). The system catches errors that humans miss in repetitive tasks. |

**Overall SEI: Enabling → Amplifying**

The system amplifies human capability (faster, more consistent) while enabling better decisions (evidence surfaced, consistency tracked). It liberates the human from mechanical work (extraction, assembly, formatting) to focus on judgment (rubric levels, scores, feedback quality).

### What the System Does NOT Do

| The system does NOT | Because |
|---|---|
| Finalize rubric level matches | Human judgment at Gate 1 |
| Finalize scores | Human judgment at Gate 1 |
| Finalize feedback | Human review at Gate 1 |
| Decide if a flag is a real inconsistency | Human judgment at Gate 2 |
| Decide if a systematic issue exists | Human judgment at Gate 3 |
| Adjust marks without human approval | Human override required for all changes |
| Make marking faster by skipping judgment | Judgment is the point; speed comes from preparation |

### What the System DOES Do (That Humans Can't Easily Do Alone)

| The system DOES | Because |
|---|---|
| Extract evidence from 30+ submissions consistently | Humans miss evidence in repetitive tasks |
| Match evidence to rubric levels with reasoning | Humans apply rubrics inconsistently over long marking sessions |
| Check score-feedback alignment for every student | Humans can't easily verify their own consistency across 30+ students |
| Track consistency across students in real-time | Humans can't hold 30+ students in working memory |
| Flag statistical outliers automatically | Humans don't naturally calculate distributions while marking |
| Calculate totals without error | Humans make arithmetic mistakes in repetitive tasks |
| Format 30+ student entries into a consistent report | Humans make formatting errors in repetitive tasks |

---

## Key Design Insight

**The three human gates mirror the three-tier fallback model from Phase 6:**

- **Gate 1** (per-student review) = Tier 2 (flag for human review). Agent prepares; human decides.
- **Gate 2** (consistency flag) = Tier 2 (flag for human review). Agent flags; human decides.
- **Gate 3** (batch halt) = Tier 3 (halt for human intervention). System stops; human must intervene.

This is CAWDP's core principle structurally embedded in the experience design: **the agent prepares judgment, the human makes judgment.** The human never starts from blank. The agent never finalizes.

The cognitive load budget (3-5 min per student, ~2-3.5 hours total) is realistic because the agent has done the heavy lifting (extraction, matching, scoring, feedback drafting) and the human makes ~12 structured decisions per student — all judgment calls, no mechanical work.

---

Ready for Phase 9 (Validation & Iteration)?

---

## Run 8 — Agentic Expert ✓ COMPLETED

*2026-06-12T00:17:16* · `glm-5.1:cloud` · `f014085b...`

### Prompt

Yes. Phase 9

### Response

# Phase 9: Validation & Iteration

## Testable Hypotheses

### H1: Typed Extraction Reduces Verification Time

**Hypothesis:** Curator's typed evidence extraction (per-criterion, with quotes and gaps) reduces the human's verification time compared to reading the full submission for each criterion.

**Test:** Mark 5 students manually (read full submission per criterion), then mark the same 5 students using the pipeline (review pre-extracted evidence at Gate 1). Measure time per criterion and accuracy of level matches.

**Success criterion:** ≥30% reduction in verification time with ≥95% accuracy retention (human doesn't miss evidence that agent extracted).

**Failure mode:** Agent misses relevant evidence (F6) or attributes evidence to wrong criterion (F7) at a rate that increases human correction time beyond the time saved.

---

### H2: Alignment Checking Catches Contradictions Humans Miss

**Hypothesis:** Verifier's alignment check (T10) catches score-feedback contradictions that a human marking alone would miss in a 30-student batch.

**Test:** After manual marking of 10 students, check for score-feedback contradictions. Then run the same 10 through the pipeline and compare Verifier-detected contradictions vs manually-detected contradictions.

**Success criterion:** Verifier detects ≥80% of contradictions that a human would flag in review, and ≥1 contradiction per 10 students that the human missed.

**Failure mode:** Verifier generates too many false positives (F15), training the human to ignore flags. Target: ≤1 false positive per 10 students.

---

### H3: Consistency Tracking Reduces Grade Drift

**Hypothesis:** Rolling consistency checking (T12) reduces grade drift across a 30-student batch compared to unassisted marking.

**Test:** Mark 30 students manually, then mark the same 30 using the pipeline. Compare score variance for similar-quality work across the batch.

**Success criterion:** ≤15% reduction in score variance for similar-quality work (measured by comparing students with similar evidence profiles).

**Failure mode:** Consistency flags are too noisy (F15 >3 per 10 students), or the human dismisses flags too often (>50% dismissal rate), undermining the safety net.

---

### H4: Decision Presentation Reduces Cognitive Load

**Hypothesis:** Presenting structured options (Accept/Adjust/Reject/Review) at Gate 1 reduces decision time per criterion compared to free-form marking.

**Test:** Time each criterion decision at Gate 1 (structured options) vs manual marking (open decision). Measure decision time and decision confidence (post-hoc survey: "how confident are you in this decision? 1-5").

**Success criterion:** ≥20% reduction in decision time per criterion with ≥equal decision confidence.

**Failure mode:** Structured options feel constraining, reducing confidence or increasing overrides. Target: ≥90% acceptance rate for agent-proposed levels.

---

### H5: Self-Correction Reduces Human Correction Burden

**Hypothesis:** Auto-redraft (F12, F13) and auto-correct (F9, F10) reduce the number of human corrections needed per student.

**Test:** Count human corrections per student (overrides of agent proposals) with and without self-correction enabled.

**Success criterion:** ≤2 human corrections per student on average (excluding Gate 1 acceptances, which are confirmations not corrections). Self-correction handles ≥60% of feedback quality issues before the human sees them.

**Failure mode:** Auto-redraft produces feedback that's still generic or repetitive, requiring human redraft. Target: ≤1 feedback redraft needed per 5 students after auto-redraft.

---

### H6: Progressive Autonomy Metrics Track Trust Accurately

**Hypothesis:** Override rate, verification pass rate, and cost variance are sufficient metrics to determine promotion between autonomy levels.

**Test:** Track overrides per autonomy level (Shadow → Advisory → Supervised → Autonomous). Correlate override patterns with promotion criteria.

**Success criterion:** Override rate decreases predictably across autonomy levels: Shadow ≤50%, Advisory ≤30%, Supervised ≤15%, Autonomous ≤10%.

**Failure mode:** Override rate doesn't decrease (agent isn't learning from corrections), or overrides cluster in specific criteria (indicating specification aging needed for that criterion).

---

## Progressive Autonomy Deployment

### Promotion Criteria

| Agent | Dimension | Shadow | Advisory | Supervised | Autonomous |
|---|---|---|---|---|---|
| **Configurator** | Criteria parsing | Human confirms every field | Proposes, human confirms | Proposes, human spot-checks | Runs, flags anomalies |
| | Weighting validation | Human checks every total | Proposes total, human confirms | Proposes total, human spot-checks | Runs, flags anomalies |
| | Format alignment | Human checks every field | Proposes match, human confirms | Proposes match, human spot-checks | Runs, flags anomalies |
| | **Promotion trigger** | 2 verified configurations | 2 verified configurations | 6 verified configurations | — |
| **Curator** | Extraction accuracy | Human checks every quote | Human checks key quotes | Human spot-checks | Runs, flags anomalies |
| | Evidence categorisation | Human confirms every assignment | Proposes, human confirms | Proposes, human spot-checks | Runs, flags anomalies |
| | Gap identification | Human confirms every gap | Proposes gaps, human confirms | Proposes, human spot-checks | Runs, flags gaps |
| | **Promotion trigger** | 5 verified students | 10 verified students | 15 verified students | 30 verified students |
| **Assessor** | Rubric matching | Human confirms every level | Proposes, human confirms | Proposes, human spot-checks | Proposes, human reviews flags only |
| | Score proposing | Human confirms every score | Proposes, human confirms | Proposes, human spot-checks | Proposes, human reviews flags only |
| | Boundary case handling | Always presents both options | Always presents both options | Always presents both options | **Always presents both options — never autonomous** |
| | **Promotion trigger** | 5 verified students | 10 verified students | 15 verified students | 30 verified students |
| **Drafter** | Evidence citation | Human verifies every citation | Human checks key citations | Human spot-checks | Runs, flags uncited claims |
| | Tone calibration | Human reviews tone | Proposes, human confirms | Proposes, human spot-checks | Runs, flags tone issues |
| | Boundary case feedback | Always presents two options | Always presents two options | Always presents two options | **Always presents two options — never autonomous** |
| | Cohesion (no repetition) | Human checks for repetition | ST7 auto-check + human spot-check | ST7 auto-check + human spot-check | ST7 auto-check, flags to human |
| | **Promotion trigger** | 5 verified students | 10 verified students | 15 verified students | 30 verified students |
| **Verifier** | Score-feedback alignment | Human checks every flag | Proposes, human confirms | Proposes, human spot-checks | Proposes, human reviews flags |
| | Cross-student consistency | Human checks every comparison | Proposes, human confirms | Proposes, human spot-checks | Proposes, human reviews flags |
| | Inconsistency counting | Always autonomous | Always autonomous | Always autonomous | Always autonomous |
| | **Promotion trigger** | 5 verified students | 10 verified students | 15 verified students | 30 verified students |
| **Compiler** | Entry formatting | Human checks every entry | Proposes, human confirms | Proposes, human spot-checks | Runs, flags anomalies |
| | Total calculation | Human checks every total | Proposes, human confirms | Proposes, human spot-checks | Runs, auto-verifies with ST5 |
| | Report assembly | Human checks full report | Proposes, human confirms | Proposes, human spot-checks | Runs, flags anomalies |
| | **Promotion trigger** | 5 verified entries | 10 verified entries | 15 verified entries | 30 verified entries |

### Promotion Process

| Step | Action |
|---|---|
| 1 | Agent completes minimum number of verified tasks at current level |
| 2 | Override rate for that dimension is below threshold |
| 3 | No critical failures (F1-F4, F16) at current level |
| 4 | Human confirms promotion readiness |
| 5 | Promotion recorded in specification aging log |
| 6 | Agent operates at new level for next batch |
| 7 | If override rate increases after promotion, **demote one level** and review specification |

### Demotion Criteria

| Condition | Action |
|---|---|
| Override rate exceeds level threshold for 3 consecutive students | Demote one level, review specification |
| Critical failure (F1-F4, F16) caused by agent | Demote one level, investigate root cause |
| Human explicitly requests demotion | Demote one level, no questions asked |
| Override rate increases after promotion (regression) | Demote one level, review specification for aging |

---

## Health Monitoring

### Integrity Diagnostic Score (IDS)

| Metric | Formula | Weight | Target |
|---|---|---|---|
| **Extraction completeness** | (criteria with evidence) / (total criteria) | 0.20 | ≥ 0.95 |
| **Alignment pass rate** | (aligned criterion scores) / (total criterion scores) | 0.20 | ≥ 0.95 |
| **Consistency pass rate** | (students without flags) / (total students) | 0.20 | ≥ 0.85 |
| **Override acceptance rate** | (accepted proposals) / (total proposals) | 0.15 | ≥ 0.80 |
| **Auto-correction rate** | (auto-corrections successful) / (total auto-corrections) | 0.10 | 1.0 |
| **Feedback specificity** | (feedback with citations) / (total feedback) | 0.15 | ≥ 0.90 |

**IDS = Σ(metric × weight)**

**IDS Thresholds:**

| IDS | Status | Action |
|---|---|---|
| ≥ 0.90 | 🟢 Healthy | Continue normal operation |
| 0.75–0.89 | 🟡 Attention | Review override patterns, check for specification aging |
| < 0.75 | 🔴 Unhealthy | Halt batch, review all agents, consider demotion |

### Utilisation Performance Ratio (UPR)

| Metric | Formula | Target |
|---|---|---|
| **Time per student (pipeline)** | Total Gate 1 time / Number of students | ≤ 5 min |
| **Time per student (manual baseline)** | Total manual marking time / Number of students | 15-20 min |
| **Time savings** | 1 - (pipeline time / manual time) | ≥ 35% |
| **Override rate** | Total overrides / Total decisions | ≤ 20% at Supervised |
| **False positive flag rate** | Dismissed flags / Total flags | ≤ 30% |
| **Cost per student** | Total tokens per student | ≤ 27,000 |
| **Cost per batch** | Total tokens for 30-student batch | ≤ 700,000 |

### Override Tracking

| Override Type | What to Track | Specification Aging Signal |
|---|---|---|
| Score adjustment >1 level | Frequency, criterion, direction | Assessor specification needs review for that criterion |
| Level change | Frequency, criterion | Assessor rubric matching specification needs review |
| Feedback edit >30% | Frequency, criterion, edit type | Drafter specification needs review for that criterion |
| Flag dismissal | Frequency, criterion | Verifier consistency threshold needs review |
| Batch halt trigger | Frequency, root cause | Systematic issue with rubric interpretation |

---

## Specification Aging Schedule

### Review Cadences by Agent

| Agent | Review Cadence | Trigger for Early Review |
|---|---|---|
| **Configurator** | Per assignment (every new brief/rubric/format) | Criteria mismatch that wasn't caught; weightings that needed manual correction |
| **Curator** | Every 10 students | Missing evidence for a criterion that should have been extractable; wrong criterion attribution |
| **Assessor** | Every 15 students | Boundary case handling not matching human judgment; level proposals consistently adjusted in one direction |
| **Drafter** | Every 15 students | Feedback edits >30%; generic feedback redrafts; repetitive feedback across criteria |
| **Verifier** | Every 20 students | False positive rate >30%; missed alignment issues; consistency flag pattern changes |
| **Compiler** | Every 30 students | Total calculation errors; missing entries; formatting issues |

### Specification Aging Triggers

| Trigger | What to Review | When |
|---|---|---|
| Override rate >20% for 3 consecutive students | Agent specification for that dimension | Immediately |
| Override rate increases after promotion | Agent specification + promotion criteria | Immediately |
| New criterion type not in rubric | Configurator + Curator specifications | When new brief is uploaded |
| Student submission format change | Curator extraction specification | When new format encountered |
| Rubric structure change | All agent specifications | When new rubric is uploaded |
| Consistency flag pattern changes | Verifier consistency thresholds | When flag dismissal rate changes |
| Batch halt triggered | Root cause analysis + affected agent specifications | When Gate 3 is triggered |

---

## EVOLVE Mode

### EVOLVE Signals and Re-Entry Points

| Signal | What It Indicates | CAWDP Re-Entry Point | Action |
|---|---|---|---|
| **Override rate exceeds threshold** | Agent proposals don't match human judgment | P4 (Capability Allocation) → P7 (Agent Design) | Review agent authority boundaries and never-rules |
| **Consistency flag pattern shifts** | Rubric interpretation has changed or drifted | P3 (Task Decomposition) → P5 (Event Storming) | Review consistency check thresholds |
| **Cost exceeds budget** | Token usage per student is too high | P6 (System Architecture) → CC-7 (Cost Budget) | Review agent prompts for efficiency |
| **Human skips Gate 1** | Human trusts agent proposals without review | P6 (Progressive Autonomy) | Consider promoting to next autonomy level |
| **Human adjusts >30% of proposals** | Agent proposals consistently don't match | P7 (Agent Design) | Review and adjust agent specifications |
| **New failure mode discovered** | Unanticipated failure not in FMEA | P3 (Task Decomposition) → P5 (Event Storming) | Add to failure event list, add recovery path |
| **Assignment format change** | New brief structure, rubric format, or submission type | P0 (Purpose & Vision) → P3 (Task Decomposition) | Re-verify configuration validation |
| **Specification aging threshold reached** | Cadence or trigger threshold | P7 (Agent Design) | Review and update agent specifications |

### Re-Entry Protocol

1. **Monitor**: IDS and UPR metrics are tracked automatically per student and per batch.
2. **Review**: When an EVOLVE signal fires, review the affected agent specification.
3. **ReEnter**: If specification changes are needed, update the specification and re-verify at the appropriate autonomy level (typically demoting one level during re-verification).
4. **Validate**: After specification changes, run 5 students at the demoted level to verify the changes are effective.
5. **Promote**: If override rate returns to acceptable levels, promote back to the previous level.

---

## MVP Testing Plan

### Phase 1: Configuration Validation (1 day)

| Test | What | Success Criterion |
|---|---|---|
| T1 | Upload brief + rubrics + format | Configuration parsed without error |
| T2 | Brief-rubric mismatch (deliberate) | ST1 fires, HALT with clear error message |
| T3 | Weightings don't sum to 100 (deliberate) | ST2 fires, HALT with clear error message |
| T4 | Format-rubric field mismatch (deliberate) | ST3 fires, warning with option to proceed |

### Phase 2: Single-Student Walkthrough (2-3 days)

| Test | What | Success Criterion |
|---|---|---|
| T5 | Process one student in Shadow mode | Human reviews every decision |
| T6 | Extraction completeness | All 4 criteria have evidence extracted |
| T7 | Rubric level match accuracy | ≥3/4 criteria match human judgment |
| T8 | Score range accuracy | All scores within human's expected range |
| T9 | Feedback quality | ≥1 criterion has specific, evidence-cited, non-generic feedback |
| T10 | Alignment check | No score-feedback contradictions |
| T11 | Assembly correctness | Total = sum of criteria, correct format |
| T12 | Gate 1 experience | Human completes review in ≤5 minutes |

### Phase 3: 5-Student Batch (1 week)

| Test | What | Success Criterion |
|---|---|---|
| T13 | Process 5 students in Shadow mode | All decisions reviewed, all flags examined |
| T14 | Consistency tracking | T12 fires for ≥1 pair of similar students |
| T15 | Auto-correction | ST4 or ST5 fires at least once (score range or total) |
| T16 | Auto-redraft | ST6 or ST7 fires at least once (generic or repetitive feedback) |
| T17 | Override capture | All overrides recorded with reasoning |
| T18 | IDS calculation | IDS ≥ 0.80 after 5 students |
| T19 | Cost tracking | Per-student cost ≤ 27,000 tokens |

### Phase 4: 30-Student Batch (2-3 weeks)

| Test | What | Success Criterion |
|---|---|---|
| T20 | Full batch processing in Shadow/Advisory mode | Complete 30 students with Gate 1 for each |
| T21 | Gate 2 triggers | ≥1 consistency flag correctly identified |
| T22 | Gate 3 trigger | Batch halt fires if >3 inconsistencies |
| T23 | Cohort report | Distribution, outliers, and consistency summary generated correctly |
| T24 | Time savings | ≥35% reduction vs manual baseline |
| T25 | Override rate | ≤50% at Shadow, ≤30% at Advisory |
| T26 | H1-H6 hypothesis testing | All hypotheses tested with quantitative results |
| T27 | Progressive autonomy | ≥1 agent promoted from Shadow to Advisory |

### Go/No-Go Criteria

| Criterion | Go | Iterate | No-Go |
|---|---|---|---|
| H1: Typed extraction reduces verification time | ≥30% reduction | 15-30% reduction | <15% reduction |
| H2: Alignment checking catches contradictions | ≥80% detection rate | 60-80% detection rate | <60% detection rate |
| H3: Consistency tracking reduces drift | ≤15% variance reduction | 15-25% variance | >25% variance |
| H4: Decision presentation reduces cognitive load | ≥20% time reduction | 10-20% time reduction | <10% time reduction |
| H5: Self-correction reduces human burden | ≤2 corrections/student | 2-3 corrections/student | >3 corrections/student |
| H6: Progressive autonomy metrics track trust | Predictable decrease in overrides | Inconsistent decrease | No decrease or increase |
| Override acceptance rate | ≥80% | 60-80% | <60% |
| IDS after 30 students | ≥0.85 | 0.75-0.85 | <0.75 |
| Cost per batch | ≤700K tokens | 700K-1M tokens | >1M tokens |

---

## Key Phase 9 Insights

**1. Boundary case handling is NEVER autonomous.**
Both the Assessor and Drafter have boundary case dimensions that are permanently supervised — rubric level boundaries (F8) and genuinely weak student feedback (Drafter Q5). These are judgment calls that benefit from agent preparation but require human decision.

**2. Progressive autonomy is per-dimension, per-agent.**
The Configurator reaches Autonomous faster (6 verified configurations) than the Assessor (30 verified students) because configuration validation is more deterministic than rubric matching. This is the right approach — different dimensions earn trust at different rates.

**3. The IDS includes a feedback specificity metric.**
This directly measures whether the Drafter is citing specific evidence (CC-3 epistemic metadata operationalised). If feedback specificity drops below 0.90, it triggers a specification aging review for the Drafter.

**4. EVOLVE signals map to specific CAWDP re-entry points.**
Override rate → P7 (Agent Design). Consistency patterns → P3/P5. Cost → P6/CC-7. Human skipping gates → P6. Human adjusting proposals → P7. New failure mode → P3/P5. Format change → P0/P3. This is the specification aging protocol made operational.

**5. The 5-Student Batch is the critical validation point.**
Before processing 30 students, 5 students in Shadow mode tests the entire pipeline with human review at every step. If hypotheses H1-H5 fail at 5 students, there's no point scaling to 30.

**6. Demotion is as important as promotion.**
If override rate increases after promotion, the agent is demoted one level and its specification is reviewed. Progressive autonomy means trust is earned and can be lost — it's not a one-way ratchet.

---

**Phase 9 complete.** This assignment marking workflow is now fully specified through all CAWDP phases (P0-P9). The key structural insight: **the agent prepares judgment at every step, the human makes judgment at three gates.** The pipeline doesn't skip judgment — it surfaces judgment points with prepared options, evidence, and reasoning. The human's role is concentrated at the points where judgment matters most, and the mechanical work is invisible.

---

## Run 9 — Agentic Expert ✓ COMPLETED

*2026-06-12T00:31:22* · `glm-5.1:cloud` · `5c170706...`

### Prompt

Conduct a retro on this CAWDP process. What insights, patterns or learnings can help improve CAWDP? 
Was there any particular strengths or weakness of this process today?

### Response

# CAWDP Application Retrospective

## Strengths

### 1. Phase Order Validated — Direction → Destination → Path → Work

The revised phase order worked as intended. P0 gave us clear targets ("accurate grades, helpful feedback, no corrections needed"). P1 produced 10 concrete outputs with schemas. P2 revealed the critical path and parallelization opportunities (T9 must wait for ALL criteria evidence). P3 decomposed toward known outputs, not into a vacuum. P4's complementarity analysis directly produced the 6 human-only tasks matching 6 human gates.

**The backcasting in P2 was the highest-value phase.** Tracing the dependency chain from O1 (Final Report) backward through O2→O3+O4+O5→O7+O8→O6→O10 revealed that T9 (feedback) must wait for ALL criteria evidence — a structural constraint that shaped the entire Stage 1 flow. Without backcasting, we might have designed feedback as per-criterion (running T9 after each criterion independently), which would have produced fragmented feedback instead of the holistic feedback Q3 specified.

### 2. Identity-First Design Was the Strongest Phase

Every agent's 5 identity questions produced a distinct personality that made everything else flow:

- **Configurator**: "Structural validator that never judges content quality" → authority boundary is clear
- **Curator**: "Reports what is there and what is missing, never evaluates" → Measurer class is obvious
- **Assessor**: "Proposes levels with reasoning, never finalizes" → the hardest boundary moment (rubric level boundaries) directly shaped Gate 1's dual-option presentation
- **Drafter**: "Writes feedback citing evidence, never fabricates" → the null state ("Unable to draft — recommend human review") is the natural consequence
- **Verifier**: "Flags only, never adjusts" → this is the purest expression of "agent prepares judgment, human makes judgment"
- **Compiler**: "Assembles exactly what was approved, never adds" → Aggregator class with the tightest authority boundary

Q5 ("What's the hardest boundary moment?") was the single most valuable question. Every agent's hardest moment became the design pressure point that shaped the fallback model and human gate design.

### 3. FMEA Directly Shaped Architecture

The 18 failure modes with RPN scores produced concrete mitigations that became structural:

- F1 (brief-rubric mismatch, RPN 240) → Gate 0 configuration review
- F6 (no evidence, RPN 189) → Gate 1 null-state handling
- F11 (feedback contradicts score, RPN 168) → T10 alignment check + Gate 1 flag
- F14-F16 (consistency) → Gate 2 and Gate 3

This wasn't planned — it emerged from the FMEA exercise. The three-tier fallback model and three human gates are direct structural responses to the failure modes.

### 4. "Worst Failure That Looks Like Success" Is a Genuinely Useful Pattern

Every agent produced a distinctive worst failure:

| Agent | Worst Failure That Looks Like Success |
|---|---|
| Configurator | Config that passes validation but has a subtle weighting error cascading through 30+ students |
| Curator | Complete evidence extraction that misses relevant content |
| Assessor | Plausible-but-wrong rubric level with reasonable justification |
| Drafter | Specific-sounding feedback that could apply to any student |
| Verifier | Over-flagging that trains humans to ignore flags |
| Compiler | Professional-looking report with wrong totals |

These are qualitatively different from "the agent crashes" — they're the failures that are hardest to detect because they look like the agent is working correctly. This pattern should be standard in every agent job description.

### 5. Decision Presentation Pattern Embedded Throughout

Every judgment point uses structured options:

- Gate 1: Accept / Adjust / Reject / Review submission directly
- Gate 2: Legitimate difference / Inconsistency (adjust either student)
- Gate 3: Fix systematic issue / Accept flags / Review all flagged submissions
- Gate 0: Confirm configuration / Needs changes

This is type collision resolution at the interaction layer — decisions are typed objects with defined options, not open questions. The human never faces a blank text field for a judgment call.

### 6. "Agent Prepares, Human Decides" Is the Architectural Invariant

This principle appeared at every level:

- **Fallback tiers**: Tier 1 (self-correction, no human), Tier 2 (flag for review), Tier 3 (halt for human)
- **Human gates**: Gate 1 (per-student judgment), Gate 2 (consistency flag review), Gate 3 (batch halt)
- **Agent authority boundaries**: Proposes, never finalizes. Flags, never decides. Assembles, never adds.
- **Decision presentation**: 2-4 structured options, not open questions

The principle isn't just stated — it's structurally enforced.

---

## Weaknesses

### 1. P2.5 Event Storming Was Skipped

This was conditional for multi-agent workflows and we judged it unnecessary. In hindsight, it would have produced trigger conditions and failure events more systematically than the FMEA alone. The FMEA covered what goes wrong, but Event Storming would have covered what triggers state changes in the pipeline.

**Improvement**: Make P2.5 recommended (not conditional) for all multi-agent workflows. The FMEA covers failure modes; Event Storming covers state transitions and triggers — they're complementary, not redundant.

### 2. P3 Task Decomposition Lacked Per-Subtask Gap Scores

We did complementarity analysis at the architecture level (identifying 6 human-only tasks) but didn't produce a per-subtask complementarity matrix with gap scores. The 6+ threshold for human-only was applied intuitively rather than systematically.

**Improvement**: Add a complementarity matrix as a standard P4 output. Every subtask gets an H/A/S allocation with a gap score. Tasks with gap ≥ 6 are human-only. This would have made the 6 human gates more rigorously justified.

### 3. P8 Contract Formalization Was Abbreviated

For a high-stakes workflow (producing grades), we should have done the full 10×10 mapping matrix from specification sections to contract primitives. We did authority boundaries and information boundaries, but we didn't formally classify each boundary as Regime 3 (prevent), Regime 2 (detect), or Regime 1 (declare).

The current enforcement is a mix:
- Regime 3 (schema validation, system triggers): ST1-ST10, output schema constraints
- Regime 2 (flagging): alignment checks, consistency flags
- Regime 1 (prompt-level): "never fabricates," "never judges quality"

But we didn't do the systematic mapping. For a grading workflow, this matters — a Regime 1 boundary ("never fabricates evidence") is only as strong as the prompt, not structurally enforced.

**Improvement**: For high-stakes workflows (anything producing grades, legal assessments, medical recommendations), P8 should be mandatory, not optional. The 10×10 mapping matrix and Unenforceable Elements Register should be produced.

### 4. Per-Student Cognitive Load Budget Is Theoretical

The 3-5 minutes per student estimate is based on decision count (12-16 decisions), not measured data. We don't know if Gate 1 actually takes 3-5 minutes or if it takes 10.

**Improvement**: Phase 9 testing should measure actual decision time per gate, not just override rates. Add time-per-gate as a UPR metric.

### 5. No Agno Implementation Plan

We decided on Agno Workflow composition and specified 6 agents, but we didn't produce an implementation plan (file structure, code architecture, session state management, how HumanReview gates are implemented, how the per-student loop is coded).

**Improvement**: Add a "P6.5 Implementation Planning" step that produces file structure, agent configuration code, workflow code, and test infrastructure. This is where the specification meets the framework.

### 6. The Q3 Answer Shaped Architecture — But This Wasn't Traced

The decision that feedback should be holistic (seeing ALL evidence before writing) directly created the synchronization point in Stage 1 (T9 waits for ALL criteria T6+T7 before running). This is a human experience design decision (P8) that shaped system architecture (P6). But we didn't formally trace this dependency.

**Improvement**: Add a "Human Experience → Architecture Trace" as a standard P6 output. When a human experience decision shapes the pipeline architecture, document it explicitly. This traces the "why" behind structural decisions.

---

## Patterns Worth Codifying

### Pattern 1: "Worst Failure That Looks Like Success" as Standard P7 Question

Every agent's worst failure was distinctive and shaped the fallback model, null states, and human gate design. This should be a required question in every agent job description, not an optional insight.

### Pattern 2: Batch Consistency Check with Threshold

The rolling consistency check (T12) with a 3-flag threshold before batch halt is a general pattern for any workflow that processes multiple similar items. This should be a standard system trigger pattern in CAWDP, not just this workflow.

### Pattern 3: "Prepares, Never Finalizes" as Architectural Invariant

The Assessor proposes, never finalizes. The Verifier flags, never decides. The Compiler assembles, never adds. The Curator extracts, never judges. Every agent has a "never" that is the inverse of its authority boundary. This pattern should be formalized: **authority boundary = inverse of failure mode, expressed as a "never" rule.**

### Pattern 4: Human Experience Decision → Architecture Constraint

The Q3 answer (holistic feedback) created a synchronization point in the pipeline. This is a general pattern: human experience design decisions (how should the output feel?) can create structural constraints in the pipeline (when can this step run?). This should be traced and documented.

### Pattern 5: Three-Tier Fallback Mirrors Three Human Gates

This structural parallelism wasn't planned — it emerged from the FMEA. Tier 1 (self-correction) = no gate. Tier 2 (flag for review) = Gate 1/2. Tier 3 (halt) = Gate 3. This pattern should be codified: **fallback tiers and human gates should be designed together, not independently.**

---

## CAWDP Improvement Recommendations

| # | Improvement | Priority | Rationale |
|---|---|---|---|
| **I1** | Make P2.5 Event Storming recommended (not conditional) for all multi-agent workflows | Medium | Complementary to FMEA; covers state transitions and triggers that FMEA misses |
| **I2** | Add complementarity matrix as standard P4 output | High | Makes H/A/S allocation and gap scores systematic, not intuitive |
| **I3** | Make P8 Contract Formalization mandatory for high-stakes workflows | High | Grades, legal, medical — Regime 3 enforcement of authority boundaries is essential |
| **I4** | Add "worst failure that looks like success" as required P7 question | High | Most valuable identity question; shapes null states, fallback model, and gate design |
| **I5** | Add Decision Presentation Pattern as standard P8 output | Medium | Type collision resolution at the interaction layer; every human gate should use structured options |
| **I6** | Add "batch consistency check with threshold" as standard system trigger pattern | Medium | General pattern for any workflow processing multiple similar items |
| **I7** | Add time-per-gate as standard UPR metric | Low | Measured decision time, not just override rate |
| **I8** | Add "Human Experience → Architecture Trace" as standard P6 output | Medium | Documents why structural decisions were made, traces them to human experience design |
| **I9** | Add P6.5 Implementation Planning step | High | Produces file structure, agent configuration, workflow code, test infrastructure |
| **I10** | Make progressive autonomy with demotion the standard, not just promotion | Medium | Trust is earned and can be lost; demotion criteria should be part of every progressive autonomy spec |

---

## Honest Assessment

**The process validated that CAWDP's phase order works.** Starting with outputs (P1) and backcasting (P2) before decomposition (P3) meant every task had a clear purpose — it produced an output that was needed by a downstream task. Without this, we would have been decomposing into a vacuum.

**The biggest gap was P8 Contract Formalization.** For a grading workflow, the Regime 1 boundaries ("never fabricates evidence," "never judges quality") are only as strong as the prompt. In a high-stakes domain, these should be Regime 3 (structurally enforced through output schema constraints). We did this for some boundaries (output schemas that don't include `final_level` fields) but not systematically.

**The biggest strength was identity-first design (P7).** Every agent has a clear identity, stance, authority boundary, worst failure, and hardest moment. This made everything else flow — null states, fallback tiers, progressive autonomy, and human gate design all derived naturally from the 5 identity questions.

**The most important next step is testing.** The P9 testing plan (Phase 1: Configuration Validation, Phase 2: Single-Student Walkthrough, Phase 3: 5-Student Batch, Phase 4: 30-Student Batch) is the right approach. But no amount of process design substitutes for putting this in front of a real user. The methodology says: five conversations with real students, not five more designs.

**One honest concern: we may have over-specified for a first implementation.** 6 agents, 18 failure modes, 7 templates, 6 progressive autonomy tables, IDS/UPR metrics, EVOLVE signals, 10 hypotheses — this is comprehensive but potentially overwhelming for a first build. The implementation plan should start with the MVP (Configurator + Curator + Assessor for 5 students in Shadow mode) and expand incrementally.

---

## Run 10 — Agentic Expert ✓ COMPLETED

*2026-06-12T00:41:49* · `glm-5.1:cloud` · `ebbe3c77...`

### Prompt

This is great work. Draft a new version of CAWDP that incorporates your recommended improvements. Note any areas that would be strengthened with further testing, what tests these should be, and what success looks like for each.

### Response

# CAWDP v2.2 — Complementarity-Driven Agentic Workflow Design Process

## What Changed from v2.1

| # | Improvement | What Changed |
|---|---|---|
| I1 | P2.5 Event Storming recommended (not conditional) | Now recommended for all multi-agent workflows, not just "when needed" |
| I2 | Complementarity matrix as standard P4 output | Per-subtask H/A/S allocation with gap scores, systematic threshold identification |
| I3 | P8 Contract Formalization mandatory for high-stakes | Grades, legal, medical → full 10×10 mapping + Unenforceable Elements Register required |
| I4 | "Worst failure that looks like success" as required P7 question | Q5 is now standard, not optional. Every agent job description includes it |
| I5 | Decision Presentation Pattern as standard P9 output | Every human gate uses 2-4 structured options, not open questions |
| I6 | Batch consistency threshold as standard system trigger | General pattern for any workflow processing multiple similar items |
| I7 | Time-per-gate as standard UPR metric | Measured decision time at each human gate |
| I8 | Human Experience → Architecture Trace as standard P6 output | Documents why structural decisions were made |
| I9 | P6.5 Implementation Planning step | Produces file structure, agent configuration, workflow code, test infrastructure |
| I10 | Progressive autonomy includes demotion | Trust is earned and can be lost; demotion criteria are part of every spec |

Additionally, from the fractal structure analysis:

| # | Improvement | What Changed |
|---|---|---|
| R1 | Production Method column in output catalogue | Every P1 output tagged as Shallow/Medium/Deep |
| R2 | Standard production methods by depth | Shallow (3 steps), Medium (5 steps), Deep (4-wave) |
| R3 | Automate Shallow outputs in Design Studio | Design guidance for implementation |
| R4 | Semi-automate Medium outputs via judgment propagation | One human decision fills 3-5 downstream outputs |
| R5 | Design Deep output workflows explicitly | P10 validated template (Compiler/Analyst/Deriver, 4 waves, 5/4/4 enforcement) |
| R6 | Output depth estimates effort per phase | Shallow = 0.5-1 hr, Medium = 2-4 hrs, Deep = 5-8 hrs |

And from the assignment marking application:

| # | Insight | Codified As |
|---|---|---|
| P1 | Authority boundary = inverse of failure mode | Standard P7 principle |
| P2 | Fallback tiers mirror human gates | Standard P6/P9 design pattern |
| P3 | Human experience decisions shape architecture | P8 trace output |
| P4 | Decision Presentation at every human judgment point | Standard P9 output |
| P5 | Worst failure that looks like success shapes null states, fallbacks, gates | Required P7 question |

---

## Revised Phase Sequence (v2.2)

| Phase | Name | Cognitive Mode | Key Change from v2.1 |
|---|---|---|---|
| P0 | Purpose & Vision | IMAGINE | Q5 now required |
| P1 | Output Specification | SPECIFY | Production Method column added |
| P2 | Backcasting | TRACE | No change |
| P2.5 | Event Storming | STRESS-TEST | Now **recommended** for all multi-agent workflows |
| P3 | Task Decomposition | DECOMPOSE | No change |
| P4 | Capability Allocation | ALLOCATE | Complementarity matrix now standard output |
| P5 | Event Storming (detailed) | STRESS-TEST | Merged with P2.5 — single phase, two depth levels |
| P6 | System Architecture | ARCHITECT | Human Experience → Architecture Trace added |
| P6.5 | Implementation Planning | ARCHITECT | **NEW** — file structure, agent config, workflow code |
| P7 | Agent Design | DESIGN | Q5 worst failure required, null states, "never" rules |
| P8 | Contract Formalization | FORMALIZE | Mandatory for high-stakes workflows |
| P9 | Human Experience Design | EMPATHIZE | Decision Presentation Pattern, time-per-gate metric |
| P10 | Validation & Iteration | VERIFY → EVOLVE | Batch consistency threshold pattern, demotion criteria |

---

## P0: Purpose & Vision

### 5 Identity Questions (Required)

Every agent in the workflow answers these before any behavioral specification:

**Q1: What IS this agent?**
Essence statement. One sentence that captures what the agent is, not what it does.

**Q2: What is its stance toward possibility?**
Determined by phase position. P0 agents are possibility-oriented (pure discovery). P8+ agents are constraint-oriented (enforcement). The stance must match the phase.

**Q3: What would VIOLATE its identity?**
Existential "never" statements. The inverse of what the agent is. These become authority boundaries.

**Q4: What would it mean for this agent to be WRONG?**
The failure mode that IS the identity boundary. For Extractors, wrong means "extracted wrong evidence." For Assessors, wrong means "proposed wrong level." For Generators, wrong means "fabricated or vague."

**Q5: What's the hardest boundary moment — where pressure would push this agent past its boundary?** *(NEW: Required in v2.2, was optional in v2.1)*

This bridges P0 to P8. It identifies the moment where the agent is most likely to violate its identity. This moment becomes the design anchor for:
- Authority boundaries (P7)
- Enforcement regime (P8)
- Human gate design (P9)
- Fallback tiers (P6)
- Null states (P7)

**Pattern observed**: Q5 produces a distinctive, memorable pressure point that shapes the entire agent design. Configurator's "near-match criteria." Curator's "evidence relevant to two criteria." Assessor's "boundary between two rubric levels." Drafter's "genuinely weak student work." Verifier's "ambiguous consistency flag." Compiler's "human-adjusted score not propagated." These are the moments that define the agent's character and the human experience.

### Target State Vision

Same as v2.1: 25 characteristics across 4 dimensions (Agent, Specification, Human, Ecosystem). No change.

---

## P1: Output Specification

### Production Method Column (NEW in v2.2)

Every output now includes a Production Method column indicating depth and production approach:

| Depth | Definition | Production Method | Estimated Effort |
|---|---|---|---|
| **Shallow** | Single extraction or computation | Extract → Validate → Record | 0.5-1 hr |
| **Medium** | Multiple steps, judgment required | Gather → Apply judgment → Validate → Check contamination → Record | 2-4 hrs |
| **Deep** | Multi-step, multi-agent, synthesis required | 4-wave Compiler/Analyst/Deriver (Data → Analysis → Derivation → Compilation) | 5-8 hrs |

This replaces the implicit understanding of depth with explicit classification. It enables:
- Effort estimation per phase (sum of output depths)
- Implementation priority (Shallow outputs are automatable; Deep outputs need the most design work)
- Pattern Library compression (Shallow and Medium outputs pre-fill from patterns; Deep outputs use the validated P10 template)

### Output Catalogue Format (v2.2)

Each output now includes:

| Field | Description |
|---|---|
| ID | Unique identifier (O1, O2, etc.) |
| Name | Descriptive name |
| Purpose | Why this output exists |
| Depth | Shallow / Medium / Deep |
| Production Method | Standard method by depth |
| Schema | Fields, types, required/optional |
| Epistemic Profile | Deterministic / Probabilistic / Elicited |
| Dependencies | Which outputs this depends on |
| Quality Gate | What validates this output |
| Target State Links | Which P0 characteristics this serves |

---

## P2.5: Event Storming (Now Recommended for All Multi-Agent Workflows)

**Change from v2.1**: Was conditional ("only for multi-agent workflows where needed"). Now **recommended** for all workflows with multiple agents.

**Rationale**: The assignment marking workflow (6 agents, sequential pipeline) still benefited from thinking through events and failure triggers, even though it was simpler than the original 23-agent pipeline. Event Storming complements FMEA — FMEA covers what goes wrong, Event Storming covers what triggers state changes.

**Two depth levels**:

| Level | When | What |
|---|---|---|
| **Light** | Single agent or simple pipeline (3 or fewer agents, sequential) | 5-10 domain events, 5-10 failure events, recovery paths |
| **Full** | Multi-agent workflow (4+ agents, parallel or complex) | Full event storming with domain events, failure events, recovery paths, system triggers, trigger conditions |

---

## P4: Capability Allocation

### Complementarity Matrix (Now Standard Output)

**Change from v2.1**: Complementarity analysis now produces a per-subtask matrix with gap scores, not just overall H/A/S allocation.

| Subtask | Cognitive Type | Human Score | Agent Score | System Score | Gap | Allocation |
|---|---|---|---|---|---|---|
| T1 | Mechanical | 3 | 8 | 2 | 5 | Agent-primary |
| T7 | Evaluative | 8 | 4 | 1 | 4 | Human-primary |
| T10 | Evaluative | 9 | 5 | 1 | 4 | Human-only (gap ≥ 6) |

**Gap threshold**: Tasks with gap ≥ 6 are human-only (the human's advantage is overwhelming). Tasks with gap 4-5 are collaborative. Tasks with gap ≤ 3 are agent-primary or system-primary.

**This replaces** the intuitive "6+ = human-only" with a systematic assessment that can be reviewed and challenged.

---

## P6: System Architecture

### Human Experience → Architecture Trace (NEW in v2.2)

When a human experience decision (P8/P9) creates a structural constraint in the pipeline, document it explicitly:

| Decision | Source | Structural Constraint | Affected Tasks |
|---|---|---|---|
| Feedback must be holistic (see ALL evidence before writing) | P8 Q3 answer | T9 must wait for ALL criteria T6+T7 before running | Stage 1 synchronization point |
| Human reviews every student | P9 Gate 1 design | Pipeline is per-student sequential, not batch-parallel | Stage 2 loop structure |
| Batch halt at 3 inconsistencies | P9 Gate 3 design | Running inconsistency counter with threshold trigger | T12 counter, Gate 3 |

**Rationale**: This traces the "why" behind structural decisions. Without it, future maintainers might remove the synchronization point without understanding that it exists because holistic feedback was a human experience decision.

### Fallback Tier Design (Standardized)

Fallback tiers and human gates are now designed together, not independently:

| Tier | Agent Action | Human Involvement | Gate |
|---|---|---|---|
| Tier 1: Self-correct | Agent detects and fixes own error | None | No gate |
| Tier 2: Flag for review | Agent detects issue, presents to human | Human reviews and decides | Gate 1 or 2 |
| Tier 3: Halt | Agent stops pipeline, presents issue | Human must intervene | Gate 3 |

**Pattern**: Every human gate corresponds to a fallback tier. Gate 1 = Tier 2 (agent flags, human decides). Gate 2 = Tier 2 (consistency flags). Gate 3 = Tier 3 (system halts).

---

## P6.5: Implementation Planning (NEW)

**Rationale**: The gap between a CAWDP specification and working code is significant. P6.5 bridges this gap by producing implementation-ready artifacts.

**Outputs**:

| ID | Name | Purpose |
|---|---|---|
| IP1 | File Structure | Directory layout, module organization, file naming conventions |
| IP2 | Agent Configuration | Agno Agent definitions (model, tools, instructions, session state) |
| IP3 | Workflow Code | Agno Workflow definitions (steps, human gates, session management) |
| IP4 | Schema Definitions | Pydantic models for inter-agent data passing |
| IP5 | Tool Definitions | User-action-level tools (not CRUD) |
| IP6 | Test Infrastructure | Unit tests, integration tests, E2E tests mapping to FMEA failure modes |
| IP7 | Seed Data | Realistic test data for validation |
| IP8 | Progressive Autonomy Plan | Promotion/demotion criteria per agent per dimension |

**Priority**: High. Without P6.5, specifications are elegant but not implementable. The assignment marking workflow was fully specified but had no implementation plan — making the transition to code significantly harder.

---

## P7: Agent Design

### Required Elements (v2.2)

Every agent job description now MUST include:

1. **5 Identity Questions** (Q1-Q5, with Q5 now required)
2. **Class and Orientation** (from 5×3 taxonomy)
3. **Authority Boundary** expressed as "never" rules (inverse of failure mode)
4. **Worst Failure That Looks Like Success** (from Q5)
5. **Hardest Boundary Moment** (from Q5)
6. **Null State** (class-specific)
7. **Per-Dimension Progressive Autonomy** with **demotion criteria**
8. **Failure Mode & Recovery** table
9. **Cost Budget** per task
10. **Information Boundaries** with enforcement regime (Declare/Detect/Prevent)
11. **Epistemic Metadata Profile**

### Authority Boundary = Inverse of Failure Mode (Codified Pattern)

This pattern was observed in the assignment marking workflow and should be standard:

| Agent | Worst Failure | Authority Boundary ("never" rule) |
|---|---|---|
| Configurator | Config that passes validation but has subtle weighting error | Never overrides human configuration |
| Curator | Complete extraction that misses relevant content | Never judges quality |
| Assessor | Plausible-but-wrong rubric level | Never finalizes |
| Drafter | Specific-sounding feedback that could apply to any student | Never fabricates, never repeats, never contradicts scores |
| Verifier | Over-flagging that trains humans to ignore flags | Never adjusts scores, never decides if flag is real |
| Compiler | Professional-looking report with wrong totals | Never adds content, never changes scores |

**The pattern**: Identify the worst failure that looks like success → express its inverse as the authority boundary → encode as a "never" rule.

### Per-Dimension Progressive Autonomy with Demotion (v2.2)

**Change from v2.1**: Every progressive autonomy table now includes demotion criteria:

| Dimension | Shadow | Advisory | Supervised | Autonomous | Demotion Trigger |
|---|---|---|---|---|---|
| Rubric matching | Human confirms every level | Proposes, human confirms | Proposes, human spot-checks | Proposes, human reviews flags | Override rate >50% for 3 consecutive students → demote |

**Demotion criteria are part of the specification**, not an afterthought. Trust is earned and can be lost.

---

## P8: Contract Formalization

### Mandatory for High-Stakes Workflows (NEW in v2.2)

**Change from v2.1**: P8 was recommended for all workflows. In v2.2, it's **mandatory** for workflows producing grades, legal assessments, medical recommendations, or any output with significant real-world consequences.

**High-stakes threshold**: If the worst failure that looks like success could cause significant harm (financial, legal, reputational, physical), P8 is mandatory.

**For the assignment marking workflow**: Produces grades → high-stakes → P8 mandatory.

**10×10 Mapping Matrix** (standard P8 output):

| | Contract | Principal | Schema | Guard | Budget | Invocation | Revert | Event | Identity | Knowledge |
|---|---|---|---|---|---|---|---|---|---|---|
| Identity section | ✦ | ✦ | | ✦ | | | ✦ | ✦ | ✦ | |
| Task Map section | | | ✦ | ✦ | | | | ✦ | | |
| Output Specs section | | | ✦ | | | ✦ | | | | |
| Failure section | | | ✦ | ✦ | | | ✦ | ✦ | | ✦ |
| Verification section | ✦ | ✦ | ✦ | ✦ | | | ✦ | ✦ | ✦ | |
| Contracts section | ✦ | | ✦ | ✦ | ✦ | ✦ | ✦ | ✦ | | |
| Human Experience | | ✦ | | | ✦ | ✦ | | ✦ | | |
| Monitoring section | | | | ✦ | ✦ | | ✦ | ✦ | | ✦ |
| Workflow Diagram | | | ✦ | ✦ | | ✦ | | ✦ | | |

(✦ = explicit mapping with enforcement regime)

**Unenforceable Elements Register** (for this workflow):

| Element | Regime | Justification | Mitigation |
|---|---|---|---|
| "Never fabricates evidence" | Declare (Regime 1) | Cannot structurally prevent fabrication in LLM output | Prompt-level + output schema requires citation field + Verifier cross-check |
| "Never judges content quality" | Declare (Regime 1) | Cannot structurally prevent judgment in LLM output | Prompt-level + Verifier checks for judgment language |
| "Never uses discouraging tone" | Declare (Regime 1) | Cannot structurally prevent tone in LLM output | Prompt-level + tone check in Drafter output schema |
| "Never decides if flag is real inconsistency" | Detect (Regime 2) | Can detect via output schema (no `is_real_inconsistency` field) but can't prevent agent from making implicit judgment | Schema enforcement + flag review at Gate 2 |

**Enforcement regime summary**:
- 4 Regime 3 (Prevent): Schema validation (no final_level field), system triggers (ST1-ST10), score range enforcement, total calculation verification
- 4 Regime 2 (Detect): Alignment check (T10), consistency check (T12), tone check, flag judgment detection
- 4 Regime 1 (Declare): "Never fabricates," "never judges quality," "never uses discouraging tone," "never decides if flag is real"

---

## P9: Human Experience Design

### Decision Presentation Pattern (Standard Output)

Every human judgment point uses the Decision Presentation Pattern:

**Pattern**: 2-4 structured options with benefits and risks. Never an open question. Always a "I need to review directly" escape hatch.

**Standard option set for assessment**:
- A) ✅ Accept [proposed level], [proposed score]
- B) 🔄 Accept [level], adjust score to ___/max
- C) 🔄 Adjust to different level: [level options]
- D) 📄 I need to review the submission directly

**Standard option set for flags**:
- A) ✅ Legitimate difference
- B) 🔄 Inconsistency — adjust [student]
- C) 📄 I need to review both directly

**Standard option set for batch halt**:
- A) 🔧 Fix systematic issue — I'll review [criterion]
- B) ✅ Accept flags as legitimate differences
- C) 📄 I need to review all flagged submissions

### Time-Per-Gate Metric (NEW in v2.2)

UPR now includes measured decision time at each human gate:

| Metric | Formula | Target |
|---|---|---|
| Time per Gate 1 | Total Gate 1 time / Number of students | ≤ 5 min |
| Time per Gate 2 | Total Gate 2 time / Number of flags | ≤ 2 min |
| Time per Gate 3 | Total Gate 3 time / Number of halts | ≤ 10 min |
| Time per cohort review | Total cohort review time | ≤ 10 min |

**This replaces estimated decision time with measured decision time.** The 3-5 min per student estimate was theoretical; actual measurement validates or corrects it.

---

## P10: Validation & Iteration

### Batch Consistency Threshold Pattern (NEW in v2.2)

**Pattern**: For any workflow that processes multiple similar items (students, patients, cases, documents):

1. **Rolling consistency check** between current and previous items
2. **Threshold** before batch halt (default: 3 flags, configurable per domain)
3. **Pattern analysis** at batch halt (identifies systematic issues)
4. **Three options** at batch halt: Fix systematic issue / Accept flags / Review all flagged items

**This is now a standard system trigger pattern** in CAWDP, not just an assignment marking pattern.

### Testable Hypotheses Template (v2.2)

Every workflow should define testable hypotheses. Standard template:

| ID | Hypothesis | Test | Success Criterion | Failure Criterion |
|---|---|---|---|---|
| H1 | [Claim] | [How to test] | [≥ threshold] | [< threshold] |
| H2 | ... | ... | ... | ... |

**Go/No-Go criteria** are defined per hypothesis, not just overall.

### Demotion Criteria (Standard in v2.2)

Progressive autonomy now includes demotion as a standard part of the specification:

| Condition | Action |
|---|---|
| Override rate exceeds threshold for 3 consecutive items | Demote one level, review specification |
| Critical failure caused by agent | Demote one level, investigate root cause |
| Human explicitly requests demotion | Demote one level, no questions asked |
| Override rate increases after promotion (regression) | Demote one level, review specification for aging |

---

## Output Production Methods (NEW Section)

### Standard Production Methods by Depth

**Shallow** (single extraction or computation):
1. Extract/compute from source data
2. Validate against quality criteria
3. Record with epistemic metadata

**Medium** (multiple steps, judgment required):
1. Gather inputs
2. Apply judgment/computation
3. Validate against quality criteria
4. Check contamination (am I introducing anything not in the input?)
5. Record with epistemic metadata

**Deep** (multi-agent, synthesis required):
1. **Data wave** (System): Query PRISM, extract relevant data, validate completeness
2. **Analysis wave** (Analyst): Calculate, correlate, surface anomalies, identify tensions
3. **Derivation wave** (Deriver): Derive recommendations from evidence, formalise patterns, generate review questions
4. **Compilation wave** (Compiler): Assemble, organise, de-duplicate, flag sparse sections

**Judgment Propagation** (key compression mechanism for Medium outputs):
When a human makes a judgment (e.g., "this boundary is Regime 3 Prevent"), it propagates to all dependent outputs automatically:
- Regime → Guard configuration → enforcement mechanism → verification protocol → contract primitive → audit trail requirements

One judgment fills 3-5 downstream outputs. This is where the fractal structure compresses: 309-618 Medium tasks → ~130-250 human decisions.

---

## Areas Needing Further Testing

### Area 1: Per-Subtask Complementarity Scoring

**What needs testing**: The 6+ gap threshold for human-only tasks. Is this the right threshold? Does it produce correct allocations?

**Test**: Apply complementarity analysis to 5 different workflows (the assignment marking workflow + 4 new ones across different domains). Compare the allocations produced by the gap threshold against expert human judgment.

**Success**: ≥80% agreement between gap-threshold allocations and expert judgment. ≥90% agreement on human-only tasks (gap ≥ 6).

**Failure**: <60% agreement, or systematic misallocation in a specific domain.

---

### Area 2: Decision Presentation Pattern Effectiveness

**What needs testing**: Does the structured options pattern (2-4 options with benefits/risks) actually reduce cognitive load and improve decision quality compared to open questions?

**Test**: A/B test with real users. Group A uses structured options at judgment points. Group B uses open questions. Measure: decision time, decision confidence, override rate, error rate.

**Success**: ≥20% reduction in decision time with ≥equal decision confidence. ≥90% acceptance rate for agent-proposed options.

**Failure**: No reduction in decision time, or lower decision confidence in the structured group.

---

### Area 3: "Worst Failure That Looks Like Success" Predictive Validity

**What needs testing**: Does Q5 predict actual failure modes during testing? Do agents that identify their hardest boundary moment actually fail there?

**Test**: Track whether the worst failure identified in Q5 matches the most common failure observed during progressive autonomy testing.

**Success**: ≥70% correlation between Q5-predicted failures and observed failures.

**Failure**: <40% correlation, indicating Q5 is not a reliable predictor.

---

### Area 4: Batch Consistency Threshold Effectiveness

**What needs testing**: Does the 3-flag threshold for batch halt catch genuine systematic issues without over-interrupting?

**Test**: Run 3 different batches of 30+ items through the pipeline. Measure: false positive rate (flags dismissed as legitimate), false negative rate (genuine inconsistencies not flagged), and batch halt frequency.

**Success**: ≤1 false positive per 10 items. ≥1 genuine inconsistency caught per batch. Batch halt triggered only when there's a systematic issue.

**Failure**: >3 false positives per 10 items (humans start ignoring flags). <50% genuine inconsistency detection. Batch halt triggered too frequently or never.

---

### Area 5: P8 Contract Formalization for High-Stakes Workflows

**What needs testing**: Does the 10×10 mapping matrix and Unenforceable Elements Register actually improve enforcement? Are Regime 3 boundaries more reliable than Regime 1?

**Test**: Run the workflow with P8 (full contract formalization) vs without P8 (prompt-level boundaries only). Measure: boundary violation rate, detection rate, prevention rate.

**Success**: Regime 3 boundaries have 0% violation rate. Regime 1 boundaries have <5% violation rate with detection. Regime 2 boundaries have <2% undetected violation rate.

**Failure**: Regime 3 boundaries violated at >5% rate. Regime 1 boundaries violated at >20% rate.

---

### Area 6: Progressive Autonomy with Demotion

**What needs testing**: Does demotion actually improve agent performance after specification review? Or does it just slow things down?

**Test**: Track agents that are demoted. After specification review, measure: override rate at demoted level, override rate after re-promotion, time to re-promotion.

**Success**: Override rate decreases after specification review. Re-promotion within 2x the original promotion timeline. <5% re-regression rate (demotion followed by promotion followed by another demotion).

**Failure**: Override rate doesn't decrease after review. Re-promotion takes >3x the original timeline. >20% re-regression rate.

---

### Area 7: Human Experience → Architecture Trace

**What needs testing**: Are the traced structural constraints actually necessary? Would removing them degrade the human experience?

**Test**: Remove the traced constraint (e.g., make feedback per-criterion instead of holistic) and measure: human decision time, decision quality, override rate, user satisfaction.

**Success**: Removing the constraint increases decision time by ≥15% or decreases decision quality (measured by override rate).

**Failure**: Removing the constraint has no measurable effect, suggesting the constraint was unnecessary.

---

### Area 8: Judgment Propagation Accuracy

**What needs testing**: When a human makes a judgment (e.g., "this boundary is Regime 3 Prevent"), do the 3-5 downstream outputs get filled correctly?

**Test**: Track 10 human judgments through the dependency chain. Measure: propagation accuracy (% of downstream outputs correctly filled), propagation completeness (% of downstream outputs that should be filled that are filled), propagation time (how long propagation takes).

**Success**: ≥95% propagation accuracy. 100% propagation completeness. <5 seconds propagation time.

**Failure**: <80% propagation accuracy. <90% propagation completeness. >30 seconds propagation time.

---

### Area 9: Production Method Depth Classification

**What needs testing**: Is the Shallow/Medium/Deep classification accurate? Does it predict actual effort?

**Test**: Classify 30 outputs from a workflow as Shallow/Medium/Deep. Measure actual production time for each. Compare estimated effort (0.5-1 hr / 2-4 hrs / 5-8 hrs) with actual effort.

**Success**: ≥80% of outputs fall within their depth's estimated effort range. Mean absolute error ≤1 hour for Shallow, ≤2 hours for Medium, ≤3 hours for Deep.

**Failure**: <60% of outputs fall within their depth's estimated range. Mean absolute error >2 hours for Shallow, >4 hours for Medium, >6 hours for Deep.

---

### Area 10: Event Storming Value for Simple Workflows

**What needs testing**: Does P2.5 Event Storming add value for simple workflows (3 or fewer agents, sequential pipeline)?

**Test**: Design 3 simple workflows with and without P2.5. Compare: number of failure events identified, number of recovery paths defined, number of system triggers designed.

**Success**: Workflows with P2.5 identify ≥20% more failure events and ≥30% more recovery paths than workflows without P2.5.

**Failure**: No significant difference in failure event or recovery path identification. P2.5 adds effort without adding value for simple workflows.

---
