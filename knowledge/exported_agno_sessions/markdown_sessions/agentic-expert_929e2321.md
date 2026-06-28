# Agentic Expert

| Field | Value |
|-------|-------|
| **Session** | `929e2321...` |
| **Type** | agent |
| **Agent** | Agentic Expert |
| **User** | pete@peterargent.com |
| **Created** | 2026-04-14T00:49:11 |
| **Runs** | 4 completed / 4 total |

## Run 1 — Agentic Expert ✓ COMPLETED

*2026-04-14T00:49:11* · `glm-5.1:cloud` · `98acc822...`

### Prompt

I would like you to decompose the task of marking an assignment into a list of subtasks that need to be completed successfully.

It should be adaptable to any assignment for any class.

The standard inputs will be:
1. Assignment brief (markdown)
2. Rubric criteria with scoring guidance (csv)
3. Student submissions (markdown)

The standard outputs will be:
1. Student report: a score for each rubric, total score, feedback on each rubric, overall feedback (markdown)
2. Cohort report (markdown)

### Response

Now let me search the knowledge base for any prior decomposition work the user has done, to ensure alignment.Now let me present the decomposition.

---

# Universal Assignment Marking — Task Decomposition

## Design Principles

This decomposition is designed to be **assignment-agnostic** and **class-agnostic**. It identifies what *must* happen for any marking process to produce reliable, fair outputs from the specified inputs. Domain-specific variation points are marked with 🔀.

---

## Input → Output Trace

```
INPUTS                              OUTPUTS
┌─────────────────────┐             ┌──────────────────────┐
│ Assignment brief    │             │ Student report       │
│ (markdown)          │──┐     ┌──▶│ (score × rubric,     │
├─────────────────────┤  │     │   │  feedback × rubric,  │
│ Rubric + scoring    │  ├─────┤   │  overall feedback)   │
│ guidance (csv)      │  │     │   ├──────────────────────┤
├─────────────────────┤  │     │   │ Cohort report        │
│ Student submissions │──┘     └──▶│ (markdown)           │
│ (markdown)          │             └──────────────────────┘
└─────────────────────┘
```

---

## Subtask Inventory

### Phase 0 — Comprehension & Calibration `[One-Time]`

*You cannot mark reliably until you understand what you're marking against and have resolved every ambiguity in the marking instruments.*

| ID | Subtask | Description | Dependencies |
|----|---------|-------------|--------------|
| 0.1 | **Parse assignment brief** | Extract requirements, constraints, deliverable format, word limits, deadline, and any conditional instructions from the brief. | — |
| 0.2 | **Parse rubric** | Extract all criteria, score levels/bands, weightings, and scoring guidance per criterion from the CSV. | — |
| 0.3 | **Map brief ↔ rubric alignment** | Verify every rubric criterion connects to a brief requirement, and every brief requirement is captured by at least one criterion. **Flag gaps in both directions.** | 0.1, 0.2 |
| 0.4 | **Resolve ambiguities** | Identify any ambiguous, conflicting, or underspecified language in the brief or rubric. Resolve or flag before marking begins. Resolution is a gate: marking cannot proceed with unresolved conflicts. | 0.1, 0.2 |
| 0.5 | **Establish scoring anchors** | For each criterion at each score level, define concrete indicators of what constitutes that level. This produces the **Calibration Reference** — the shared standard against which all marking is done. | 0.2, 0.4 |
| 0.6 🔀 | **Identify domain-specific evaluation dimensions** | Determine whether any criterion requires specialised knowledge, external reference standards, or multi-dimensional assessment (e.g., code correctness + style, or argument strength + evidence quality). This is where the decomposition adapts to the assignment's domain. | 0.2 |

**Phase Gate:** Before proceeding, the Calibration Reference must be complete. Unresolved ambiguities from 0.4 block all downstream work.

---

### Phase 1 — Submission Intake `[Per-Submission, Parallelisable]`

*Understand what was submitted before evaluating it. This phase is structurally separate from evaluation: it extracts and structures, it never judges.*

| ID | Subtask | Description | Dependencies |
|----|---------|-------------|--------------|
| 1.1 | **Verify completeness** | Check the submission against brief requirements: are all required sections/deliverables present? Missing items are **flagged**, not penalised — penalty is a Phase 2 decision. | 0.1 |
| 1.2 | **Verify format compliance** | Check against format requirements: word count, file type, structural requirements. Non-compliance is **flagged**, not penalised. | 0.1 |
| 1.3 | **Extract structure** | Identify the submission's sections, headings, key structural elements, and overall organisation. Produces a structural map. | — |
| 1.4 | **Extract substantive content** | Identify the core content: claims, arguments, evidence, analysis, positions taken, solutions offered. Produces a content map aligned to the structural map. | 1.3 |
| 1.5 | **Extract metadata** | Student ID, word count, submission timestamp, and any other non-content identifiers. | — |
| 1.6 🔀 | **Screen for integrity concerns** | Flag potential plagiarism, AI-generated content, or other integrity issues. The scope of this subtask varies by institutional policy. In some contexts it may be minimal; in others, substantive. **Flags are not findings** — they trigger investigation, not penalty. | 1.4 |

**Output:** Enhanced Submission Package per student — structural map, content map, metadata, and any flags.

---

### Phase 2 — Per-Criterion Evaluation `[Per-Submission × Per-Criterion]`

*The core evaluation work. For each rubric criterion independently, locate evidence, assess it, score it, and draft feedback.*

| ID | Subtask | Description | Dependencies |
|----|---------|-------------|--------------|
| 2.1 | **Locate criterion evidence** | For each rubric criterion, identify which parts of the submission are relevant. This is an extraction operation — it does not assess quality, it identifies where the student addressed (or failed to address) the criterion. | 0.5, 1.4 |
| 2.2 | **Assess evidence against scoring guidance** | For each criterion, evaluate the located evidence against the Calibration Reference (0.5) and rubric scoring guidance. This is the judgment operation — the marker decides which score band the evidence falls into. | 0.5, 2.1 |
| 2.3 | **Assign criterion score** | Record the score for the criterion based on the assessment. This is a **recommendation** at this stage — it is subject to consistency review in Phase 3 and cohort calibration in Phase 4. | 2.2 |
| 2.4 | **Draft criterion feedback** | For each criterion, draft specific feedback that: (a) cites the evidence on which the score is based, (b) explains why the evidence meets (or falls short of) the next score band, and (c) identifies what would improve performance. Feedback must be traceable to evidence, not vague. | 2.2, 2.3 |
| 2.5 🔀 | **Evaluate cross-criterion dimensions** | For assignments where criteria overlap or interact (e.g., "critical analysis" and "use of evidence"), assess whether scores across related criteria are coherent. This is conditional — some rubrics have fully independent criteria, others have interdependencies. | 2.3 |

**Output per student:** A set of criterion scores + criterion feedback drafts + any cross-criterion coherence notes.

---

### Phase 3 — Submission Integration & Review `[Per-Submission]`

*After evaluating each criterion independently, integrate across criteria and verify internal coherence before the submission is finalised.*

| ID | Subtask | Description | Dependencies |
|----|---------|-------------|--------------|
| 3.1 | **Calculate total score** | Sum or weight the individual criterion scores per the rubric specification. | 2.3 |
| 3.2 | **Check internal consistency** | Verify: (a) each criterion's feedback aligns with its score, (b) scores across criteria are mutually coherent, (c) flag+penalty decisions from Phase 1 have been correctly applied. **Inconsistencies trigger re-evaluation of specific criteria** — back to 2.2/2.3, not forward with known errors. | 2.3, 2.4, 1.1, 1.2 |
| 3.3 | **Draft overall feedback** | Synthesise criterion-level feedback into coherent overall feedback. This is NOT a summary — it should identify the submission's strongest dimension, weakest dimension, and the single most impactful improvement the student could make. | 2.4, 3.1 |
| 3.4 | **Verify feedback-score alignment** | The acid test: could a student reading only the overall feedback correctly predict the total score band? If not, the feedback is incomplete or misleading. | 3.1, 3.3 |
| 3.5 🔀 | **Apply penalty/bonus adjustments** | If the rubric or brief specifies penalty structures (e.g., late submission penalties, format violation penalties) or bonus structures, apply them. This is conditional — not all assignments have these. | 1.1, 1.2, 3.1 |

**Output per student:** Finalised criterion scores, total score, criterion feedback, overall feedback — the complete student-level result set.

---

### Phase 4 — Cohort Quality Assurance `[Cohort-Level]`

*After all submissions are individually evaluated, verify fairness and consistency across the cohort. A per-submission evaluation that is internally consistent can still be externally unfair if equivalent work received different scores.*

| ID | Subtask | Description | Dependencies |
|----|---------|-------------|--------------|
| 4.1 | **Compile score distributions** | For each criterion and for total scores, produce the statistical distribution across the cohort (mean, median, SD, min, max, quartiles). | 3.1 (all students) |
| 4.2 | **Identify distribution anomalies** | Flag criteria with unexpected distributions: all high (floor effect), all low (ceiling effect), bimodal, heavily skewed, or with variance that differs significantly from other criteria. Anomalies don't prove a problem — they signal one. | 4.1 |
| 4.3 | **Detect marking drift** | Compare early-marked submissions to late-marked submissions to detect systematic drift in scoring patterns. Drift is a known cognitive bias — the 50th submission is not marked by the same marker as the 1st. | 3.1 (all students, ordered) |
| 4.4 | **Flag outlier submissions** | Identify submissions whose scores deviate significantly from the cohort distribution. Outliers require review — they may be correctly scored exceptional/poor work, or they may be marking errors. | 4.1 |
| 4.5 | **Verify cross-submission equivalence** | Check that substantively equivalent work received equivalent scores. This is the fairness test — it requires comparing submission content, not just scores. | 1.4 (all students), 3.1 (all students) |
| 4.6 | **Review integrity flags** | Aggregate all integrity flags from Phase 1 across the cohort. Determine which require investigation and which can be explained (e.g., common source material). | 1.6 (all students) |

**Phase Gate:** Any submissions requiring re-evaluation (outliers, drift-affected, integrity-flagged) return to Phase 2/3 before proceeding.

---

### Phase 5 — Report Production `[Cohort-Level]`

*Produce the two specified output documents.*

| ID | Subtask | Description | Dependencies |
|----|---------|-------------|--------------|
| 5.1 | **Generate student reports** | For each student, produce the markdown student report containing: score per rubric criterion, total score, feedback per rubric criterion, overall feedback. Format must match the specified output schema. | 3.1–3.5 (finalised) |
| 5.2 | **Generate cohort report** | Produce the markdown cohort report containing: score distributions, distribution anomalies, drift analysis, outliers, integrity summary, cross-submission consistency findings, and any recommendations for rubric/brief revision. | 4.1–4.6 |

---

## Subtask Summary

| Phase | Subtasks | Scope | Parallelisable? |
|-------|----------|-------|-----------------|
| **0 — Comprehension & Calibration** | 0.1–0.6 | One-Time | Partial (0.1 ∥ 0.2) |
| **1 — Submission Intake** | 1.1–1.6 | Per-Submission | Yes (across students) |
| **2 — Per-Criterion Evaluation** | 2.1–2.5 | Per-Submission × Per-Criterion | Partial (within student: criteria can be parallel; across students: fully parallel) |
| **3 — Integration & Review** | 3.1–3.5 | Per-Submission | Sequential within submission |
| **4 — Cohort QA** | 4.1–4.6 | Cohort-Level | Partial (4.1 must complete first) |
| **5 — Report Production** | 5.1–5.2 | Cohort-Level | Yes (5.1 ∥ 5.2) |

**Total: 6 phases, 25 subtasks** (20 universal + 5 variable 🔀)

---

## Feedback Loops

The decomposition is not strictly linear. Three feedback loops exist by design:

```
3.2 (internal consistency) ──▶ back to 2.2/2.3 (re-evaluate specific criteria)
4.4 (outlier flagging)  ───▶ back to 2.2/2.3 (re-evaluate flagged submissions)
4.3 (drift detection)   ───▶ back to 2.2/2.3 (re-evaluate drift-affected range)
```

These loops are features, not bugs. A decomposition that assumes all subtasks complete once would produce internally inconsistent or externally unfair results.

---

## Adaptation Points (🔀)

The five variable subtasks are where the decomposition adapts to specific assignments:

| Subtask | What Varies | Adaptation Question |
|---------|-------------|---------------------|
| **0.6** Domain-specific dimensions | What knowledge or standards are required to evaluate? | "Does any criterion require specialised expertise or external references?" |
| **1.6** Integrity screening | How thorough, and what tools are available? | "What integrity checks does institutional policy require?" |
| **2.5** Cross-criterion evaluation | Are criteria independent or interdependent? | "Do any criteria overlap or interact such that a score on one constrains the possible scores on another?" |
| **3.5** Penalty/bonus adjustments | Are there adjustments beyond the rubric? | "Does the brief specify any penalties or bonuses outside the rubric?" |
| — | Submission content type | What counts as "evidence" varies dramatically by discipline | "What does evidence look like for this assignment type?" |

The 20 universal subtasks execute identically regardless of assignment. The 5 variable subtasks are filled in per assignment using the adaptation questions.

---

Shall I proceed to any of these next steps?

1. **Define the data schemas** that flow between phases (the "Enhanced Submission Package," "Calibration Reference," etc.)
2. **Apply CAWDP** to this decomposition — assign Human/Agent/System actors and complementarity scores to each subtask
3. **Stress-test the decomposition** against a specific assignment type (e.g., code submission, design portfolio, lab report) to validate universality

---

## Run 2 — Agentic Expert ✓ COMPLETED

*2026-04-14T00:55:17* · `glm-5.1:cloud` · `de3931eb...`

### Prompt

Firstly, identify stakeholders associated with the marking outcomes.
What the ideal outcomes for each stakeholder group?
What are the associated risks for each stakeholder group?
Which subtasks are most important for achieving ideal outcomes (highest value)?, lowest value?, highest risk?, lowest risk?

### Response

---

# Stakeholder Analysis of Assignment Marking

## 1. Stakeholder Identification

Six stakeholder groups are directly affected by marking outcomes. They are listed in order of **proximity to impact** — the student experiences consequences most directly; the institution most structurally.

| # | Stakeholder | Role in the Process | Power Over Process |
|---|-------------|---------------------|-------------------|
| **S1** | **Students** | Submit work; receive scores and feedback | Lowest — no control over marking |
| **S2** | **Markers / Assessors** | Execute the marking process | Moderate — interpret rubric, apply judgment |
| **S3** | **Course Coordinators** | Design brief & rubric; set standards; review cohort outcomes | High — define instruments and calibration |
| **S4** | **Program / Institution** | Accredit outcomes; enforce standards; use grades for progression decisions | High — set policy and consequences |
| **S5** | **Future Employers / Credential Consumers** | Rely on grades as signals of capability | None — trust the credential without visibility |
| **S6** | **Academic Integrity Board** | Investigate and adjudicate integrity cases | Conditional — activated by flags, not routine |

---

## 2. Ideal Outcomes per Stakeholder

| Stakeholder | Ideal Outcome | What "Done Right" Looks Like |
|-------------|--------------|------------------------------|
| **S1 — Students** | **A grade that accurately reflects their work, and feedback that enables improvement** | They can read their report and understand exactly what they did well, what they didn't, and what to do differently. The score feels fair — even when it's low. |
| **S2 — Markers** | **Efficient, defensible marking with minimal rework** | They can mark consistently without cognitive overload. Edge cases are rare. Their professional judgment is respected, not second-guessed. No appeals upheld. |
| **S3 — Course Coordinators** | **A cohort distribution that validates the rubric and informs iteration** | The distribution reveals student learning, not rubric ambiguity. They can identify what worked and what didn't in the assignment design. They can improve the rubric for next time. |
| **S4 — Program / Institution** | **Defensible, auditable outcomes that pass accreditation review** | Any grade can be traced to evidence against published criteria. No systemic bias. No integrity scandals. Statistical norms are within expected ranges. |
| **S5 — Credential Consumers** | **Grades that reliably signal capability** | A student who scored highly can actually do what the grade claims. The credential has predictive validity. |
| **S6 — Integrity Board** | **Clean cases built on evidence, not suspicion** | Integrity flags are well-founded and include supporting evidence. False positives are rare. Investigations are conclusive, not ambiguous. |

### Tension Map

The ideal outcomes **conflict** at three critical seams:

| Tension | Stakeholders in Conflict | Nature of Conflict |
|---------|--------------------------|-------------------|
| **Richness vs. Efficiency** | S1 (wants detailed feedback) vs. S2 (wants streamlined marking) | More feedback = more marker time per submission. Less time = vaguer feedback. |
| **Fairness vs. Efficiency** | S1 (wants consistent marking) vs. S2 (wants to finish on time) | Cohort QA (Phase 4) is essential for fairness but time-intensive. Skipping it saves time but produces inconsistency. |
| **Auditability vs. Usability** | S4 (wants full audit trail) vs. S1 (wants readable feedback, not forensic data) | Audit requirements add metadata overhead. Student-facing reports and audit records are different documents serving different masters. |
| **Signal Fidelity vs. Grade Inflation** | S5 (wants grades to mean something) vs. S1/S2 (pressure toward higher grades) | Generous marking benefits students and reduces complaints but degrades the signal for everyone downstream. |

---

## 3. Risks per Stakeholder

| Stakeholder | Risk | Severity | Trigger |
|-------------|------|----------|---------|
| **S1 — Students** | **Inaccurate score** — grade doesn't reflect work quality | 🔴 High | Scoring error, rubric misinterpretation, drift |
| **S1 — Students** | **Unactionable feedback** — feedback is vague, generic, or score-justifying rather than improvement-oriented | 🔴 High | Feedback drafted without citing evidence |
| **S1 — Students** | **Unfair treatment** — equivalent work scored differently than peers | 🔴 High | Inconsistent marking, no cohort QA |
| **S1 — Students** | **Wrongful integrity accusation** | 🟡 Medium | Over-sensitive integrity screening, false positive |
| **S2 — Markers** | **Inconsistency exposure** — internal/external review catches inconsistent marking | 🔴 High | No calibration, no drift detection |
| **S2 — Markers** | **Cognitive fatigue** — quality degrades across large cohorts | 🔴 High | No drift mitigation, no workload management |
| **S2 — Markers** | **Appeal upheld** — marking decision overturned on review | 🟡 Medium | Scoring not traceable to evidence/rubric |
| **S3 — Course Coordinators** | **Rubric validated as broken** — cohort distribution reveals rubric cannot discriminate | 🔴 High | All students cluster at one score level |
| **S3 — Course Coordinators** | **Missing the improvement signal** — cohort report doesn't reveal what to change | 🟡 Medium | Cohort report is descriptive, not diagnostic |
| **S4 — Program / Institution** | **Accreditation gap** — marking process fails audit requirements | 🔴 High | No audit trail, no calibration evidence |
| **S4 — Program / Institution** | **Systemic bias** — cohort-level patterns reveal group-level scoring disparities | 🔴 High | No distribution analysis, no cross-submission verification |
| **S5 — Credential Consumers** | **Credential inflation** — grades no longer predict capability | 🟡 Medium | Systematic overmarking, no calibration |
| **S6 — Integrity Board** | **Ambiguous case** — integrity flag lacks supporting evidence | 🟡 Medium | Poor integrity screening, flag without evidence |

---

## 4. Subtask Value & Risk Classification

### Method

Each subtask is rated on two dimensions:
- **Value**: How much does successful completion contribute to stakeholder ideal outcomes? (H/M/L)
- **Risk**: How severe are the consequences if it fails? (H/M/L)
- **Primary beneficiary**: Which stakeholder benefits most from this subtask done well?
- **Conflict flag**: ⚡ = this subtask serves one stakeholder at the expense of another

### Full Classification

| ID | Subtask | Value | Risk | Primary Beneficiary | Conflict |
|----|---------|-------|------|---------------------|----------|
| **0.1** | Parse assignment brief | M | M | S3 | — |
| **0.2** | Parse rubric | M | M | S2, S3 | — |
| **0.3** | Map brief ↔ rubric alignment | **H** | **H** | S3, S1 | — |
| **0.4** | Resolve ambiguities | **H** | **H** | S1, S2 | — |
| **0.5** | Establish scoring anchors | **H** | **H** | S1, S2, S4 | — |
| **0.6** 🔀 | Identify domain-specific dimensions | M | M | S2 | — |
| **1.1** | Verify completeness | M | M | S2, S3 | — |
| **1.2** | Verify format compliance | L | L | S2 | — |
| **1.3** | Extract structure | M | M | S2 | — |
| **1.4** | Extract substantive content | **H** | **H** | S2, S1 | — |
| **1.5** | Extract metadata | L | L | S4 | — |
| **1.6** 🔀 | Screen for integrity concerns | M | **H** | S6, S4 | ⚡ S1 (false positives) |
| **2.1** | Locate criterion evidence | **H** | **H** | S1, S2 | — |
| **2.2** | Assess evidence against scoring guidance | **H** | **H** | S1, S5 | — |
| **2.3** | Assign criterion score | **H** | **H** | S1, S4 | ⚡ S5 (inflation pressure) |
| **2.4** | Draft criterion feedback | **H** | M | S1 | ⚡ S2 (time cost) |
| **2.5** 🔀 | Evaluate cross-criterion dimensions | M | M | S1 | — |
| **3.1** | Calculate total score | M | **H** | S1, S4 | — |
| **3.2** | Check internal consistency | **H** | **H** | S1, S2 | ⚡ S2 (rework cost) |
| **3.3** | Draft overall feedback | **H** | M | S1 | ⚡ S2 (time cost) |
| **3.4** | Verify feedback-score alignment | M | M | S1 | ⚡ S2 (time cost) |
| **3.5** 🔀 | Apply penalty/bonus adjustments | M | **H** | S4 | ⚡ S1 (penalty impact) |
| **4.1** | Compile score distributions | M | L | S3 | — |
| **4.2** | Identify distribution anomalies | **H** | M | S3, S4 | — |
| **4.3** | Detect marking drift | **H** | **H** | S1, S2 | ⚡ S2 (fatigue exposure) |
| **4.4** | Flag outlier submissions | **H** | M | S1 | — |
| **4.5** | Verify cross-submission consistency | **H** | **H** | S1, S5 | — |
| **4.6** | Review integrity flags | M | **H** | S6, S4 | ⚡ S1 (wrongful accusation) |
| **5.1** | Generate student reports | **H** | M | S1 | — |
| **5.2** | Generate cohort report | **H** | L | S3 | — |

---

## 5. Analysis: Value × Risk Quadrants

```
                    HIGH VALUE
                         │
         0.3  0.4  0.5   │   2.1  2.2  2.3
         1.4             │   3.2       4.3  4.5
         2.4  3.3  4.2   │
         4.4  5.1  5.2   │
    ─────────────────────┼───────────────────────
         1.1  1.3  0.6   │   1.6  2.5
         0.1  0.2  2.4*  │   3.1       4.6
         3.4             │   3.5
                         │
                    LOW VALUE
                    LOW RISK              HIGH RISK

* 2.4 shown in both quadrants: high value for S1, medium for others
    
    🔴 CRITICAL (High Value + High Risk)    ⚠️ VULNERABLE (Low Value + High Risk)
    🟢 LEVERAGE (High Value + Low Risk)      ⬜ LOW PRIORITY (Low Value + Low Risk)
```

### The Quadrants

| Quadrant | Subtasks | Interpretation |
|----------|----------|----------------|
| 🔴 **CRITICAL** — High Value, High Risk | **0.3, 0.4, 0.5, 1.4, 2.1, 2.2, 2.3, 3.2, 4.3, 4.5** | These are the 10 subtasks where failure causes the most damage AND success creates the most value. **These are the non-negotiables.** They require the strongest quality controls, the most capable actors, and the most rigorous verification. |
| 🟢 **LEVERAGE** — High Value, Low Risk | **2.4, 3.3, 4.2, 4.4, 5.1, 5.2** | These 6 subtasks create high value with relatively low failure risk. They are the efficiency opportunities — automate, streamline, optimise. Getting these right produces disproportionate returns. |
| ⚠️ **VULNERABLE** — Low/Med Value, High Risk | **1.6, 3.1, 3.5, 4.6** | These 4 subtasks have asymmetric risk: they don't create much value day-to-day, but when they fail, the consequences are severe (false integrity accusations, wrong total score, penalty misapplication, integrity case collapse). **They are landmines.** |
| ⬜ **LOW PRIORITY** — Low Value, Low Risk | **1.2, 1.5** | These 2 subtasks are the safest to simplify or automate. Format verification and metadata extraction are mechanistic. |

---

## 6. Direct Answers

### Highest Value Subtasks

| Rank | Subtask | Why |
|------|---------|-----|
| 1 | **2.2 — Assess evidence against scoring guidance** | This is the judgment core. Every stakeholder's ideal outcome depends on this being done well. It is the single most consequential cognitive operation in the entire process. |
| 2 | **0.5 — Establish scoring anchors** | Without calibration, 2.2 is unanchored judgment. Anchors are the precondition for every score being defensible. |
| 3 | **2.1 — Locate criterion evidence** | If evidence is missed or misidentified, every downstream judgment is built on incomplete or wrong foundations. |
| 4 | **3.2 — Check internal consistency** | The last quality gate before a student receives results. Catches scoring errors that per-criterion evaluation cannot. |
| 5 | **4.5 — Verify cross-submission consistency** | The fairness test. Without it, the system can be internally consistent per submission but externally unfair across the cohort. |

### Lowest Value Subtasks

| Rank | Subtask | Why |
|------|---------|-----|
| 1 | **1.2 — Verify format compliance** | Mechanistic check with low judgment content. Important only when penalties apply; otherwise procedural. |
| 2 | **1.5 — Extract metadata** | Administrative data extraction. Necessary for record-keeping but contributes nothing to evaluation quality. |
| 3 | **0.1 — Parse assignment brief** | Necessary but low-difficulty. The brief is a structured document; extraction is mechanical. |
| 4 | **2.5 — Evaluate cross-criterion dimensions** 🔀 | Conditional subtask that only activates when rubric criteria are interdependent. Often not needed. |

### Highest Risk Subtasks

| Rank | Subtask | Risk | Who Bears It |
|------|---------|------|-------------|
| 1 | **2.2 — Assess evidence against scoring guidance** | Wrong judgment → wrong score for every student on every criterion | S1 (wrong grade), S5 (degraded signal) |
| 2 | **2.3 — Assign criterion score** | Systematic bias or inflation/deflation across all students | S1, S4, S5 |
| 3 | **3.1 — Calculate total score** | Arithmetic error affects final grade directly | S1, S4 |
| 4 | **1.6 — Screen for integrity concerns** 🔀 | False positive → wrongful accusation; false negative → integrity failure | S1, S6, S4 |
| 5 | **4.6 — Review integrity flags** | Aggregate review either over-escalates (wasting board time, student distress) or under-escalates (missing real cases) | S6, S1 |

### Lowest Risk Subtasks

| Rank | Subtask | Why Low Risk |
|------|---------|-------------|
| 1 | **1.2 — Verify format compliance** | Binary, mechanistic check. Failure is easily caught and corrected. |
| 2 | **1.5 — Extract metadata** | Factual extraction with no judgment. Error is trivially detectable. |
| 3 | **5.2 — Generate cohort report** | Aggregation of already-completed analysis. Failure is cosmetic, not substantive. |
| 4 | **4.1 — Compile score distributions** | Mechanical statistics. No judgment involved. Error is self-evident. |

---

## 7. The Critical Insight: Value and Risk Are Not Distributed Equally

The most important finding of this analysis is **not** the ranking — it is the asymmetry:

```
THE 10 CRITICAL SUBTASKS (H Value + H Risk) are where:
  • 80% of stakeholder impact is created or destroyed
  • 100% of the judgment work lives
  • 0% of the mechanistic work lives

THE 4 VULNERABLE SUBTASKS (L/M Value + H Risk) are where:
  • Day-to-day value is low
  • But failure consequences are catastrophic (wrongful accusation, grade error)
  • They are LANDMINES — invisible until triggered

THE 6 LEVERAGE SUBTASKS (H Value + L Risk) are where:
  • Automation and efficiency gains produce the most return
  • These are the "do more of this" opportunities
```

**Implication for actor assignment:** The Critical and Vulnerable subtasks demand the most careful allocation. The Leverage subtasks are the automation candidates. The Low Priority subtasks are the simplification candidates.

Shall I proceed to apply CAWDP's complementarity analysis and actor assignment to this decomposition, using the stakeholder value/risk data to inform Human/Agent/System allocation?

---

## Run 3 — Agentic Expert ✓ COMPLETED

*2026-04-14T01:10:46* · `glm-5.1:cloud` · `5e6a530c...`

### Prompt

apply CAWDP's complementarity analysis and actor assignment to this decomposition, using the stakeholder value/risk data to inform Human/Agent/System allocation

### Response

---

# CAWDP Phase 2: Complementarity Analysis & Actor Assignment

## Scoring Framework

### Capability Dimensions

| Dim | Name | Human Advantage | Agent Advantage |
|-----|------|----------------|----------------|
| **AP** | Analytical Precision | Applying criteria with contextual judgment | Applying criteria with literal consistency |
| **DE** | Domain Expertise | Knowing what matters in this subject | Following domain guidance in rubric text |
| **CS** | Consistency | Maintaining standard across few instances | Maintaining standard across unlimited instances |
| **ND** | Nuance Detection | Recognising subtle qualities, student intent, edge cases | Recognising pattern deviations from expected structure |
| **EJ** | Ethical Judgment | Decisions with moral/professional weight | Not applicable — has none |
| **CG** | Constructive Generation | Producing feedback from experience | Producing feedback from rubric language |

### Scale: 1–10

| Score | Meaning |
|-------|---------|
| 1–3 | Low capability — errors likely |
| 4–6 | Moderate — usable with oversight |
| 7–8 | Strong — reliable for most cases |
| 9–10 | Exceptional — reliable even for edge cases |

### Allocation Rules (CAWDP v2)

| Rule | Threshold | Allocation |
|------|-----------|------------|
| **System-first** | Task is mechanical/routine | → System |
| **Gap ≥ 6 (Human)** | Human has decisive advantage | → Human-Only |
| **Gap ≥ 4 (Agent)** | Agent has meaningful advantage | → Agent-led, Human oversight |
| **Gap < 4 both ways** | No decisive advantage either way | → Collaborative |
| **Stakeholder Risk Override** | Subtask is 🔴 Critical (H Value + H Risk) | → Upgrade human authority regardless of gap |
| **Reversibility gate** | Irreversible action | → Human presence structurally required |

---

## Complementarity Matrix — Full Scoring

### Phase 0 — Comprehension & Calibration [One-Time]

| ID | Subtask | Primary Dims | H Avg | A Avg | Gap | Rev | Stakeholder Override | Allocation |
|----|---------|-------------|-------|-------|-----|-----|---------------------|------------|
| 0.1 | Parse assignment brief | AP, CS | 5.5 | 8.5 | A+3.0 | ✅ | — | **System** |
| 0.2 | Parse rubric | AP, CS | 5.5 | 8.5 | A+3.0 | ✅ | — | **System** |
| 0.3 | Map brief ↔ rubric alignment | AP, DE, ND | 7.3 | 5.0 | H+2.3 | ✅ | — | **Collaborative** |
| 0.4 | Resolve ambiguities | DE, ND, EJ | 8.7 | 2.7 | **H+6.0** | ❌ | 🔴 | **Human-Only** |
| 0.5 | Establish scoring anchors | DE, ND, CG | 8.0 | 5.0 | H+3.0 | ✅ | 🔴 | **Collaborative** |
| 0.6 🔀 | Identify domain-specific dimensions | DE, ND | 8.5 | 3.0 | **H+5.5** | ✅ | — | **Human-Only** |

### Phase 1 — Submission Intake [Per-Submission, Parallelisable]

| ID | Subtask | Primary Dims | H Avg | A Avg | Gap | Rev | Stakeholder Override | Allocation |
|----|---------|-------------|-------|-------|-----|-----|---------------------|------------|
| 1.1 | Verify completeness | AP, CS | 6.0 | 9.0 | A+3.0 | ✅ | — | **Agent** |
| 1.2 | Verify format compliance | AP, CS | 6.0 | 9.5 | A+3.5 | ✅ | — | **System** |
| 1.3 | Extract structure | AP, CS | 5.5 | 8.5 | A+3.0 | ✅ | — | **Agent** |
| 1.4 | Extract substantive content | AP, ND, DE | 7.0 | 5.7 | H+1.3 | ✅ | 🔴 | **Agent-led, Human edge-case review** |
| 1.5 | Extract metadata | AP, CS | 5.0 | 9.5 | A+4.5 | ✅ | — | **System** |
| 1.6 🔀 | Screen for integrity concerns | ND, CS, EJ | 6.3 | 5.7 | H+0.6 | ✅ | ⚠️ Vulnerable | **Agent-led, Human adjudicates flags** |

### Phase 2 — Per-Criterion Evaluation [Per-Submission × Per-Criterion]

| ID | Subtask | Primary Dims | H Avg | A Avg | Gap | Rev | Stakeholder Override | Allocation |
|----|---------|-------------|-------|-------|-----|-----|---------------------|------------|
| 2.1 | Locate criterion evidence | AP, CS, DE | 6.7 | 7.3 | A+0.6 | ✅ | 🔴 | **Agent-led, Human reviews gaps** |
| 2.2 | Assess evidence against scoring guidance | DE, ND, AP | 7.7 | 5.3 | H+2.4 | ✅ | 🔴 Critical | **Collaborative** — ⚡ upgraded from Agent-led |
| 2.3 | Assign criterion score | EJ, DE, ND | 8.0 | 4.0 | **H+4.0** | ❌ | 🔴 Critical | **Collaborative** — Agent recommends, Human decides |
| 2.4 | Draft criterion feedback | CG, DE, ND | 7.7 | 6.0 | H+1.7 | ✅ | 🔴 | **Agent-led, Human reviews** |
| 2.5 🔀 | Evaluate cross-criterion dimensions | ND, DE | 7.5 | 4.5 | H+3.0 | ✅ | — | **Collaborative** |

### Phase 3 — Integration & Review [Per-Submission]

| ID | Subtask | Primary Dims | H Avg | A Avg | Gap | Rev | Stakeholder Override | Allocation |
|----|---------|-------------|-------|-------|-----|-----|---------------------|------------|
| 3.1 | Calculate total score | AP, CS | 7.0 | 9.5 | A+2.5 | ❌ | ⚠️ Vulnerable | **System** — with audit lock |
| 3.2 | Check internal consistency | AP, ND | 7.5 | 6.5 | H+1.0 | ✅ | 🔴 | **Agent-led, Human reviews flags** |
| 3.3 | Draft overall feedback | CG, ND, DE | 7.3 | 6.0 | H+1.3 | ✅ | 🔴 | **Agent-led, Human reviews** |
| 3.4 | Verify feedback-score alignment | AP, ND | 7.5 | 7.0 | H+0.5 | ✅ | — | **Agent-led, Human reviews** |
| 3.5 🔀 | Apply penalty/bonus adjustments | EJ, AP | 8.0 | 4.5 | H+3.5 | ❌ | ⚠️ Vulnerable | **Collaborative** — Agent calculates, Human authorises |

### Phase 4 — Cohort Quality Assurance [Cohort-Level]

| ID | Subtask | Primary Dims | H Avg | A Avg | Gap | Rev | Stakeholder Override | Allocation |
|----|---------|-------------|-------|-------|-----|-----|---------------------|------------|
| 4.1 | Compile score distributions | CS, AP | 5.5 | 9.5 | A+4.0 | ✅ | — | **System** |
| 4.2 | Identify distribution anomalies | CS, ND | 6.5 | 7.0 | A+0.5 | ✅ | 🔴 | **Agent-led, Human interprets** |
| 4.3 | Detect marking drift | CS, AP, ND | 6.0 | 7.7 | A+1.7 | ✅ | 🔴 Critical | **Agent-led, Human reviews** |
| 4.4 | Flag outlier submissions | CS, AP | 5.5 | 8.5 | A+3.0 | ✅ | 🔴 | **Agent** — flagging is reversible |
| 4.5 | Verify cross-submission consistency | DE, ND, CS | 6.7 | 5.7 | H+1.0 | ✅ | 🔴 Critical | **Collaborative** — Agent clusters, Human evaluates equivalence |
| 4.6 | Review integrity flags | EJ, ND | 8.5 | 3.0 | **H+5.5** | ❌ | ⚠️ Vulnerable | **Collaborative** — Agent aggregates, Human adjudicates |

### Phase 5 — Report Production [Cohort-Level]

| ID | Subtask | Primary Dims | H Avg | A Avg | Gap | Rev | Stakeholder Override | Allocation |
|----|---------|-------------|-------|-------|-----|-----|---------------------|------------|
| 5.1 | Generate student reports | CS, CG | 5.5 | 8.0 | A+2.5 | ✅ | 🟢 Leverage | **System** — template fill from finalised data |
| 5.2 | Generate cohort report | CS, CG | 5.5 | 7.5 | A+2.0 | ✅ | 🟢 Leverage | **Agent** — synthesis from Phase 4 outputs |

---

## Allocation Summary

### By Actor

| Actor | Subtask Count | IDs |
|-------|--------------|-----|
| **System** | 6 | 0.1, 0.2, 1.2, 1.5, 3.1, 4.1, 5.1 |
| **Agent-led** | 7 | 1.1, 1.3, 1.4, 2.1, 2.4, 3.2, 3.3, 3.4, 4.2, 4.3, 4.4, 5.2 |
| **Collaborative** | 7 | 0.3, 0.5, 2.2, 2.3, 2.5, 3.5, 4.5, 4.6 |
| **Human-Only** | 3 | 0.4, 0.6, (partially) 2.3's decision authority |

### By Agent Class

| Agent Class | Subtasks | Characteristic Operation | Authority Boundary |
|-------------|----------|--------------------------|-------------------|
| **Extractor** | 1.3, 1.4, 2.1 | Extract and locate — never evaluate | Must not assess quality |
| **Measurer** | 3.2, 3.4, 4.2, 4.3, 4.4 | Measure and flag — never interpret | Must not decide what's acceptable |
| **Assessor** | 1.6, 2.2, 2.5 | Assess and recommend — never finalise | Must not assign final score |
| **Generator** | 2.4, 3.3, 5.2 | Draft and generate — never approve | Must not approve own output |
| **Aggregator** | 1.1, 4.5, 4.6 | Aggregate and cluster — never adjudicate | Must not make final determination |

### Authority Boundaries — The Inverse of Failure Modes

This is the CAWDP structural principle: **what an agent is worst at is what it must be structurally prevented from doing.**

| Agent Class | Characteristic Failure Mode | Authority Boundary (Inverse) |
|-------------|----------------------------|-------------------------------|
| **Extractor** | Hallucination — extracting what isn't there, missing what is | Cannot assess quality or relevance of extracted content |
| **Measurer** | Noise-as-signal — flagging statistical artifacts as meaningful | Cannot decide whether a flagged anomaly requires action |
| **Assessor** | Overconfidence — recommending a score with false certainty | Cannot assign a final score — recommends only |
| **Generator** | Fabrication / Vagueness — inventing feedback or being uselessly generic | Cannot approve own draft for delivery — every statement must cite evidence |
| **Aggregator** | Omission — losing important signals in aggregation | Cannot adjudicate — must preserve all individual flags in aggregate |

---

## Stakeholder Risk Override Analysis

The complementarity gap alone would allocate some 🔴 Critical subtasks to Agent-led. The stakeholder risk data overrides three key allocations:

| Subtask | Gap-Based Allocation | Stakeholder Override | Final Allocation | Rationale |
|---------|---------------------|---------------------|-----------------|-----------|
| **2.2** Assess evidence against scoring guidance | Agent-led (A+0.6 on AP/CS) | 🔴 Critical: #1 value + #1 risk for S1, S5 | **Collaborative** | Agent prepares assessment; Human makes judgment. The most consequential cognitive operation in the pipeline cannot be delegated. |
| **2.3** Assign criterion score | Collaborative (H+4.0) — already correct | 🔴 Critical: #2 risk for S1, S4, S5 | **Collaborative** with Human decision authority | Agent recommends; Human decides. Score is irreversible for student outcomes. |
| **4.5** Verify cross-submission consistency | Agent-led (A+1.0 on CS) | 🔴 Critical: fairness is #1 risk for S1 | **Collaborative** | Agent clusters by score pattern; Human evaluates whether clustered submissions represent equivalent work. Agent cannot make this judgment. |
| **1.6** Screen for integrity concerns | Agent-led (gap neutral) | ⚠️ Vulnerable: false positive = wrongful accusation | **Agent-led + Human adjudicates** | Agent flags; Human investigates. Flags are never findings. Integrity determination is exclusively human. |
| **3.5** Apply penalty/bonus | Agent-led (A+2.5 on AP) | ⚠️ Vulnerable: wrong penalty = grade error | **Collaborative** | System calculates; Human authorises. Penalty application is structurally gated on human approval. |

---

## The Core Operating Principle: Who Prepares, Who Decides

Every allocation resolves to a single question: **who prepares the decision input, and who makes the decision?**

| Subtask Category | Preparation | Decision | Why |
|------------------|-------------|----------|-----|
| **System** tasks | System executes | System outputs (no decision) | Mechanical — no judgment required |
| **Agent-led** tasks | Agent executes | Human reviews only on flag | Agent is reliable; human reviews exceptions |
| **Collaborative** tasks | Agent prepares structured recommendation | Human makes final determination | Judgment is required; agent prepares it efficiently |
| **Human-only** tasks | Human prepares | Human decides | Agent lacks the capability entirely |

### The Decision Flow Within a Collaborative Subtask

```
┌─────────────────────────────────────────────────────┐
│                COLLABORATIVE SUBTASK                 │
│                                                      │
│  ┌──────────┐    structured      ┌──────────┐       │
│  │          │    recommendation  │          │       │
│  │  AGENT   │──────────────────▶│  HUMAN   │       │
│  │ prepares │   + evidence      │ decides  │       │
│  │          │   + confidence     │          │       │
│  │          │   + alternatives   │          │       │
│  └──────────┘                    └──────────┘       │
│       │                              │               │
│       │    ┌──────────────────┐      │               │
│       │    │ if confidence <  │      │               │
│       │    │ threshold, flag  │      │               │
│       │    │ for human review │      │               │
│       │    └──────────────────┘      │               │
│       │                              │               │
│       ▼                              ▼               │
│  ┌──────────────────────────────────────────┐       │
│  │           SYSTEM (audit log)              │       │
│  │  recommendation + decision + rationale   │       │
│  └──────────────────────────────────────────┘       │
└─────────────────────────────────────────────────────┘
```

---

## Allocation Heatmap: Where Human Time Goes

```
HUMAN EFFORT REQUIRED (per subtask, at cohort of 50)

         HIGH ┃                             ██ 2.2 ██
              ┃                             ██ 2.3 ██
              ┃           ██ 0.4 ██         ██ 2.5 ██
              ┃           ██ 0.6 ██  ██ 0.5 ██
              ┃                                   ██ 3.5 ██
              ┃                                           ██ 4.5 ██
              ┃                                                   ██ 4.6 ██
         LOW  ┃
              ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
               Phase 0            Phase 2            Phase 3    Phase 4

HUMAN-ONLY:  0.4, 0.6          (the judgment gate)
COLLABORATIVE: 0.3, 0.5, 2.2, 2.3, 2.5, 3.5, 4.5, 4.6  (the decision points)
AGENT-LED:   Everything else   (human reviews flags only)
SYSTEM:      0.1, 0.2, 1.2, 1.5, 3.1, 4.1, 5.1  (no human involvement)
```

**Critical insight:** Human time concentrates at **2.2 and 2.3** — the judgment core. This is correct: these are the 2 subtasks where every stakeholder's ideal outcome is created or destroyed. Everything else either feeds into these decisions efficiently (Agent/System) or catches their failures (Phase 3/4 QA).

---

## Reversibility Classification

| Class | Subtasks | Structural Requirement |
|-------|----------|----------------------|
| **Read-only** | 0.1, 0.2, 1.3, 1.4, 1.5, 2.1, 4.1 | Agent/System can execute freely |
| **Reversible** | 0.3, 0.5, 0.6, 1.1, 1.2, 1.6, 2.4, 2.5, 3.2, 3.3, 3.4, 4.2, 4.3, 4.4, 4.5, 5.1, 5.2 | Agent can execute with safeguards and rollback |
| **Irreversible** | 0.4, 2.3, 3.1, 3.5, 4.6 | Human presence structurally required — these produce outcomes that cannot be undone once delivered |

**Three irreversible subtasks are Collaborative (already have human authority):**
- 0.4 — Resolve ambiguities → Human-Only ✅
- 2.3 — Assign criterion score → Agent recommends, Human decides ✅
- 3.5 — Apply penalties → Agent calculates, Human authorises ✅
- 4.6 — Review integrity flags → Agent aggregates, Human adjudicates ✅

**One irreversible subtask is System:**
- 3.1 — Calculate total score → **System** but with audit lock

This is the one structural gap: **3.1 is irreversible (a wrong total score directly affects the final grade) but allocated to System.** The resolution: **System calculates but the result is audit-locked** — it cannot be modified without a human unlock event. The calculation is deterministic (arithmetic), so System is correct, but the output is treated as irreversible once locked.

---

## The Five Tensions Resolved (or Not)

Recall the stakeholder tension map. Here is how each tension is addressed:

| Tension | Resolution | Where It Lives | Unresolved? |
|---------|-----------|---------------|-------------|
| **Richness vs. Efficiency** | Agent drafts feedback (2.4, 3.3); Human reviews. Draft quality enforced by "every statement must cite evidence" Generator constraint. | 2.4, 3.3 | Partially — agent feedback quality depends on calibration quality (0.5). If 0.5 is poor, 2.4 cannot compensate. |
| **Fairness vs. Efficiency** | Agent does all scale work (Phase 1, 4.1-4.4); Human does only equivalence judgment (4.5) and integrity adjudication (4.6). | Phase 4 | Resolved — efficiency at scale, fairness at the two decision points that matter. |
| **Auditability vs. Usability** | System produces audit trail for every subtask; Agent produces student-facing reports. These are different documents. | 3.1 (audit lock), 5.1 (student report) | Resolved — the audit trail is a System output, the student report is a separate production. |
| **Signal Fidelity vs. Grade Inflation** | 2.3 (score assignment) is Collaborative with Human decision authority. Agent recommends but cannot inflate. | 2.3 | Resolved structurally — the agent's assessment cannot become the final score without human gate. |
| **Integrity Accuracy vs. Student Distress** | 1.6 (screen) flags only; 4.6 (review) adjudicates with human authority. Flags ≠ findings. | 1.6, 4.6 | Resolved — two-phase integrity process prevents false accusations from becoming actions. |

---

## Summary: What the Data Reveals

| Finding | Detail |
|---------|--------|
| **Human concentration** | Human judgment concentrates at 5 decision points: 0.4, 0.6, 2.2, 2.3, and the Phase 4 adjudications (4.5, 4.6). Everything else is Agent/System with human exception handling. |
| **Agent sweet spot** | Phases 1 and 4.1–4.4 — high-volume, consistency-critical, pattern-oriented work. This is where agents create the most value: doing at scale what humans do poorly (consistent, tireless execution). |
| **System sweet spot** | Parsing (0.1, 0.2), arithmetic (3.1, 4.1), formatting (1.2, 1.5, 5.1). Mechanical operations with zero judgment content. |
| **The structural gap** | 3.1 (calculate total score) is irreversible but System-allocated. Resolved by audit lock. |
| **The highest-leverage investment** | 0.5 (scoring anchors) — this one-time subtask determines the quality of every downstream assessment. If calibration is wrong, every score is wrong regardless of who assigns it. |
| **The landmine** | 1.6 (integrity screening) — low day-to-day value but catastrophic if it produces false positives. Agent-led with human adjudication is the correct allocation, but the System must enforce "flags ≠ findings" as a structural boundary, not a prompt instruction. |

Shall I proceed to Phase 3 (System Architecture) — designing the pipeline structure, orchestration, and handoff schemas for this allocation?

---

## Run 4 — Agentic Expert ✓ COMPLETED

*2026-04-14T01:22:52* · `glm-5.1:cloud` · `85fef3c9...`

### Prompt

proceed

### Response

---

# CAWDP Phase 3: System Architecture

## 1. Pipeline Architecture

### Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         ASSIGNMENT MARKING PIPELINE                       │
│                                                                          │
│  ┌───────────┐   ┌──────────────┐   ┌──────────────┐   ┌─────────────┐  │
│  │  PHASE 0  │──▶│   PHASE 1    │──▶│   PHASE 2    │──▶│   PHASE 3   │  │
│  │Calibration│   │  Intake      │   │  Evaluation  │   │ Integration │  │
│  │ [Once]    │   │ [×N ∥]      │   │ [×N×C ∥]    │   │ [×N seq]    │  │
│  └───────────┘   └──────────────┘   └──────────────┘   └──────┬──────┘  │
│                                                             │          │
│  ┌───────────┐   ┌──────────────┐                          │          │
│  │  PHASE 5  │◀──│   PHASE 4    │◀─────────────────────────┘          │
│  │  Reports  │   │  Cohort QA   │                                      │
│  │ [Cohort]  │   │  [Cohort]    │                                      │
│  └───────────┘   └──────────────┘                                      │
└─────────────────────────────────────────────────────────────────────────┘
```

### Execution Waves

---

#### Phase 0 — Calibration Workflow [Once, Sequential with Gates]

```
WAVE 0A  ┌────────┐ ┌────────┐
  ∥      │ 0.1    │ │ 0.2    │     System ∥ System
         │ Parse  │ │ Parse  │
         │ Brief  │ │ Rubric │
         └────┬───┘ └───┬────┘
              │         │
WAVE 0B      └────┬─────┘
                 ▼
         ┌────────────┐
         │    0.3     │        Collaborative
         │ Map Align  │        (Agent structures, Human validates)
         └──────┬─────┘
                │
WAVE 0C         ▼
         ┌────────────┐
         │    0.4     │  🔒IRREVERSIBLE GATE
         │  Resolve   │  Human-Only
         │ Ambiguities│  ⛔ Cannot proceed without human resolution
         └──────┬─────┘
                │
WAVE 0D         ▼
         ┌────────────┐
         │    0.5     │  Collaborative
         │  Scoring   │  (Agent drafts, Human calibrates)
         │  Anchors   │  🔒 CALIBRATION GATE — anchors must be locked before Phase 1
         └──────┬─────┘
                │
WAVE 0E         ▼
         ┌────────────┐
         │    0.6 🔀  │  Human-Only
         │  Domain    │
         │  Dimensions│
         └────────────┘
```

**Output:** `Calibration Reference` — the immutable standard for all downstream marking.

---

#### Phase 1 — Submission Intake [Per-Student, Parallelisable]

```
FOR EACH STUDENT (parallel):

WAVE 1A  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐
  ∥      │ 1.1  │ │ 1.2  │ │ 1.3  │ │ 1.5  │
         │Comp- │ │Fmt   │ │Struc │ │Meta  │
         │lete  │ │Check │ │Extract│ │data  │
         │Agent │ │System│ │Agent │ │System│
         └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘
            │        │        │        │
WAVE 1B    │        │        ▼        │
            │        │  ┌──────────┐│
            │        │  │   1.4    ││     Agent-led (Extractor)
            │        │  │ Content  ││     Human reviews flagged cases
            │        │  │ Extract  ││
            │        │  └────┬─────┘│
            │        │       │      │
WAVE 1C    └────────┴───────┼──────┘
                            ▼
                     ┌──────────┐
                     │   1.6 🔀 │     Agent-led
                     │ Integrity│     ⚠️ FLAGS ≠ FINDINGS
                     │ Screen   │     enforced by System
                     └──────────┘
```

**Output:** `Enhanced Submission Package` per student — structural map, content map, metadata, flags.

---

#### Phase 2 — Per-Criterion Evaluation [Per-Student × Per-Criterion, Bimodal Routing]

This is the architectural core. The **Confidence-Based Routing** mechanism creates two execution paths.

```
FOR EACH STUDENT (sequential across students, parallel across criteria):

                    ┌──────────────────┐
                    │  BRIEFING        │
                    │  COMPOSER        │  Assembles: Calibration Ref
                    │  (Meta-Agent)    │  + Enhanced Submission Pkg
                    └────────┬─────────┘  + Criterion-specific guidance
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
         ┌─────────┐  ┌─────────┐  ┌─────────┐
         │ Crit A  │  │ Crit B  │  │ Crit C  │   All criteria ∥
         │ 2.1→2.4 │  │ 2.1→2.4 │  │ 2.1→2.4 │   per student
         └────┬────┘  └────┬────┘  └────┬────┘
              │             │             │
              ▼             ▼             ▼
         ┌──────────────────────────────────────┐
         │     CONFIDENCE-BASED ROUTER (System)  │
         │                                       │
         │  confidence ≥ 8 ──▶ FAST PATH         │
         │  confidence 5-7 ──▶ SLOW PATH         │
         │  confidence < 5 ──▶ SLOW PATH (pri)   │
         │  always-review  ──▶ SLOW PATH         │
         └──────────┬──────────────┬──────────────┘
                    │              │
           ┌────────▼──┐   ┌─────▼──────────┐
           │ FAST PATH │   │   SLOW PATH    │
           │           │   │                │
           │ Auto-     │   │ Human Review   │
           │ approve   │   │ Queue          │
           │           │   │                │
           │ + random  │   │ Agent presents │
           │ sampling  │   │ recommendation │
           │ (10-20%)  │   │ + evidence     │
           │           │   │ + reasoning    │
           └─────┬─────┘   │                │
                 │         │ Human decides: │
                 │         │ Accept / Modify│
                 │         │ / Reject       │
                 │         └───────┬────────┘
                 │                 │
                 └────────┬────────┘
                          ▼
                   ┌─────────────┐
                   │    2.5 🔀    │    Collaborative
                   │  Cross-     │    (if criteria are
                   │  criterion  │     interdependent)
                   └──────┬──────┘
                          │
                          ▼
                   FINALISED PER-CRITERION
                   ASSESSMENT PACKAGE
```

**Confidence Thresholds:**

| Confidence | Route | Human Action | Sampling Rate |
|-----------|-------|--------------|---------------|
| **≥ 8** | Fast path | None (auto-approve) | 10–20% random sample for quality monitoring |
| **5–7** | Slow path | Review required | 100% |
| **< 5** | Slow path (priority) | Review required, flagged urgent | 100% |
| **Designated always-review** 🔀 | Slow path | Review required | 100% |

**The "always-review" designation** is set by the Course Coordinator during Phase 0.6. Certain high-stakes or domain-sensitive criteria are never auto-approved regardless of confidence.

**Output:** `Criterion Assessment Package` per student — scores, feedback, confidence, routing history.

---

#### Phase 3 — Integration & Review [Per-Student, Sequential with Feedback Loops]

```
FOR EACH STUDENT (sequential):

  ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
  │   3.1    │────▶│   3.2    │────▶│   3.3    │────▶│   3.4    │
  │ Total    │     │ Consist- │     │ Overall  │     │ Feedback │
  │ Score    │     │ ency     │     │ Feedback │     │ Align    │
  │ System   │     │ Agent-led│     │ Agent-led│     │ Agent-led│
  │ 🔒AUDIT  │     │          │     │          │     │          │
  │ LOCK     │     └────┬─────┘     └──────────┘     └────┬─────┘
  └──────────┘          │                                 │
                   FLAGS?                                FLAGS?
                        │                                 │
                   ┌────▼─────┐                      ┌───▼──────┐
                   │ RE-EVAL  │                      │ REVISE   │
                   │ Back to  │                      │ Feedback │
                   │ 2.2/2.3  │                      │ Draft    │
                   └──────────┘                      └──────────┘
                                                            │
                                                            ▼
                                                     ┌──────────┐
                                                     │   3.5 🔀  │
                                                     │ Penalty/  │
                                                     │ Bonus     │
                                                     │ Collab    │
                                                     │ 🔒 HUMAN  │
                                                     │ AUTHORISE │
                                                     └──────────┘
```

**Output:** `Finalised Student Result` — all scores, all feedback, total, audit trail.

---

#### Phase 4 — Cohort Quality Assurance [Cohort-Level, After All Students Complete Phase 3]

```
WAVE 4A  ┌──────────┐
         │   4.1    │     System (must complete first)
         │ Compile  │
         │ Distr.   │
         └────┬─────┘
              │
WAVE 4B      ▼
   ┌──────────┐ ┌──────────┐ ┌──────────┐
   │   4.2    │ │   4.3    │ │   4.4    │     All Agent-led ∥
   │ Distrib. │ │  Drift   │ │ Outlier  │
   │ Anomalies│ │ Detection│ │ Flagging │
   └────┬─────┘ └────┬─────┘ └────┬─────┘
        │             │             │
WAVE 4C└──────┬────────┴──────┬──────┘
              ▼               ▼
   ┌──────────────┐  ┌──────────────┐
   │    4.5       │  │    4.6       │     Both Collaborative
   │ Cross-       │  │ Integrity    │
   │ Submission   │  │ Flag Review  │
   │ Consistency  │  │              │
   │ Agent        │  │ Agent        │
   │ clusters,    │  │ aggregates,  │
   │ Human judges │  │ Human        │
   │ equivalence  │  │ adjudicates  │
   └──────┬───────┘  └──────┬───────┘
          │                 │
WAVE 4D  └────────┬────────┘
                   ▼
         ┌────────────────┐
         │  HUMAN REVIEW  │
         │  SESSIONS       │
         │                 │
         │  • Outlier      │
         │    disposition  │
         │  • Drift-       │
         │    affected     │
         │    re-eval      │
         │  • Integrity    │
         │    decisions    │
         │  • Equivalence  │
         │    disputes     │
         └────────┬───────┘
                  │
                  ▼
         RE-EVALUATION LOOP
         (flagged students
          back to Phase 2/3)
```

**Output:** `Cohort QA Report` — distributions, anomalies, drift analysis, flags, human decisions.

---

#### Phase 5 — Report Production [Cohort-Level, Parallel]

```
   ┌──────────────┐     ┌──────────────┐
   │    5.1       │  ∥  │    5.2       │
   │ Student      │     │ Cohort       │
   │ Reports      │     │ Report       │
   │ System       │     │ Agent        │
   │ (template    │     │ (synthesis   │
   │  fill)       │     │  from Phase  │
   │              │     │  4 outputs)  │
   └──────────────┘     └──────────────┘
```

---

## 2. Handoff Schemas

Each handoff is a typed, versioned data structure. No handoff is prose — every one is a schema.

### H-1: Calibration Reference [Phase 0 → Phase 2]

```
CalibrationReference
├── brief: ParsedBrief
│   ├── requirements: List[Requirement]
│   ├── constraints: List[Constraint]
│   ├── deliverable_spec: DeliverableSpec
│   └── word_limits: WordLimits
├── rubric: ParsedRubric
│   ├── criteria: List[Criterion]
│   │   ├── id: str
│   │   ├── name: str
│   │   ├── weight: float
│   │   ├── score_levels: List[ScoreLevel]
│   │   │   ├── score: numeric
│   │   │   ├── label: str
│   │   │   └── guidance: str
│   │   └── always_review: bool  🔀
│   └── total_possible: numeric
├── alignment_map: AlignmentMap
│   ├── criterion_to_requirement: List[Mapping]
│   ├── uncovered_requirements: List[str]  ← flags
│   └── uncovered_criteria: List[str]     ← flags
├── resolved_ambiguities: List[AmbiguityResolution]
│   ├── original_text: str
│   ├── resolution: str
│   ├── resolved_by: "human"
│   └── timestamp: datetime
├── scoring_anchors: List[CriterionAnchor]
│   ├── criterion_id: str
│   ├── level_examples: List[LevelExample]
│   │   ├── score: numeric
│   │   ├── concrete_indicators: List[str]
│   │   ├── source: "agent_draft" | "human_validated"
│   │   └── confidence: float
│   └── lock_status: "draft" | "locked"
└── domain_dimensions: List[DomainDimension] 🔀
    ├── dimension_name: str
    ├── evaluation_guidance: str
    └── source: "human"
```

### H-2: Enhanced Submission Package [Phase 1 → Phase 2]

```
EnhancedSubmissionPackage
├── student_id: str
├── metadata: SubmissionMetadata
│   ├── word_count: int
│   ├── submission_timestamp: datetime
│   └── format_compliance: ComplianceReport
│       ├── is_compliant: bool
│       └── violations: List[str]
├── completeness: CompletenessReport
│   ├── is_complete: bool
│   └── missing_elements: List[str]
├── structural_map: StructuralMap
│   ├── sections: List[Section]
│   │   ├── heading: str
│   │   ├── level: int
│   │   ├── word_count: int
│   │   └── content_hash: str
│   └── total_sections: int
├── content_map: ContentMap
│   ├── claims: List[Claim]
│   │   ├── text: str
│   │   ├── section: str
│   │   ├── type: "argument" | "evidence" | "position" | "analysis" | "reflection"
│   │   └── extraction_confidence: float
│   ├── evidence_instances: List[Evidence]
│   └── key_positions: List[Position]
└── integrity_flags: List[IntegrityFlag]
    ├── flag_type: "plagiarism" | "ai_generated" | "other"
    ├── confidence: float
    ├── evidence: str
    ├── status: "flag" ← never "finding"
    └── flagged_by: "agent"
```

### H-3: Criterion Assessment Package [Phase 2 → Phase 3]

```
CriterionAssessmentPackage
├── student_id: str
├── assessments: List[CriterionAssessment]
│   ├── criterion_id: str
│   ├── criterion_name: str
│   ├── evidence_located: List[EvidenceReference]
│   │   ├── section: str
│   │   ├── text_excerpt: str
│   │   └── relevance: float
│   ├── assessment: Assessment
│   │   ├── score_recommendation: numeric
│   │   ├── confidence: float  ← ROUTING SIGNAL
│   │   ├── reasoning_trace: str
│   │   ├── alternatives_considered: List[str]
│   │   └── assumptions: List[str]
│   ├── score: Score
│   │   ├── recommended: numeric
│   │   ├── final: numeric | null  ← null until human gate
│   │   ├── set_by: "agent" | "human"
│   │   └── modification_rationale: str | null
│   ├── feedback: Feedback
│   │   ├── draft: str
│   │   ├── evidence_citations: List[str]
│   │   ├── improvement_suggestion: str
│   │   └── approved: bool
│   └── routing: RoutingRecord
│       ├── path: "fast" | "slow"
│       ├── human_reviewed: bool
│       └── review_outcome: "accepted" | "modified" | "rejected" | null
├── cross_criterion_notes: List[CrossCriterionNote] 🔀
└── routing_summary: RoutingSummary
    ├── total_criteria: int
    ├── fast_path: int
    ├── slow_path: int
    └── human_sampled: int
```

### H-4: Finalised Student Result [Phase 3 → Phase 4]

```
FinalisedStudentResult
├── student_id: str
├── criterion_results: List[CriterionResult]
│   ├── criterion_id: str
│   ├── final_score: numeric
│   ├── final_feedback: str
│   ├── score_set_by: "agent" | "human"
│   └── audit_trail: List[AuditEntry]
├── total_score: TotalScore
│   ├── value: numeric
│   ├── calculation: str  ← formula trace
│   ├── audit_locked: bool
│   └── lock_timestamp: datetime | null
├── overall_feedback: str
├── consistency_check: ConsistencyReport
│   ├── flags: List[ConsistencyFlag]
│   └── resolved: bool
├── penalty_bonus: PenaltyBonus 🔀
│   ├── adjustments: List[Adjustment]
│   │   ├── type: "penalty" | "bonus"
│   │   ├── reason: str
│   │   ├── value: numeric
│   │   └── authorised_by: "human" ← structural requirement
│   └── adjusted_total: numeric
└── phase_2_routing_summary: RoutingSummary
```

### H-5: Cohort QA Package [Phase 4 → Phase 5]

```
CohortQAPackage
├── distributions: ScoreDistributions
│   ├── per_criterion: List[CriterionDistribution]
│   │   ├── criterion_id: str
│   │   ├── mean: float
│   │   ├── median: float
│   │   ├── sd: float
│   │   ├── min: float
│   │   ├── max: float
│   │   └── quartiles: [float, float, float]
│   └── total_scores: CriterionDistribution
├── anomalies: List[AnomalyFlag]
│   ├── criterion_id: str
│   ├── type: "floor_effect" | "ceiling_effect" | "bimodal" | "high_variance" | "low_variance"
│   ├── description: str
│   └── severity: "info" | "warning" | "critical"
├── drift_report: DriftReport
│   ├── drift_detected: bool
│   ├── affected_range: str  ← "submissions 35-50"
│   ├── direction: "leniency" | "severity" | null
│   └── magnitude: float
├── outliers: List[OutlierRecord]
│   ├── student_id: str
│   ├── deviation_sd: float
│   ├── direction: "high" | "low"
│   └── disposition: "confirmed_valid" | "flagged_for_review" | "re_evaluated"
├── cross_submission_consistency: ConsistencyReport
│   ├── cluster_analysis: List[Cluster]
│   ├── equivalence_disputes: List[Dispute]
│   └── human_decisions: List[EquivalenceDecision]
├── integrity_aggregate: IntegrityAggregate
│   ├── total_flags: int
│   ├── escalated: int
│   ├── dismissed: int
│   ├── adjudicated: List[IntegrityDecision]
│   │   ├── student_id: str
│   │   ├── finding: "substantiated" | "unsubstantiated" | "inconclusive"
│   │   └── decided_by: "human"
│   └── false_positive_rate: float
└── re_evaluation_summary: List[ReEvalRecord]
    ├── student_id: str
    ├── trigger: "outlier" | "drift" | "consistency" | "integrity"
    ├── original_scores: List[numeric]
    └── revised_scores: List[numeric] | null
```

---

## 3. Composition Decisions

| Phase | Composition | Agno Mechanism | Rationale |
|-------|-------------|---------------|-----------|
| **0** | **Workflow** | `Workflow` with conditional gates | Sequential with gates; mixed actors; one-time execution |
| **1** | **Team (coordinate)** | `Team(mode="coordinate")` | Parallel agents per student; no dependencies between students |
| **2** | **Workflow + Agent pool** | `Workflow` calling criterion evaluation `Agent` ×N per student | Same agent called repeatedly with different criterion context; human gate on routing |
| **3** | **Workflow** | `Workflow` with feedback loops | Sequential with conditional re-evaluation paths |
| **4** | **Team → Human sessions** | `Team(mode="coordinate")` for Wave 4B → human review | Parallel analysis agents, then human judgment sessions |
| **5** | **Parallel** | Two independent agents | System fills template; Agent synthesises cohort report |

---

## 4. FMEA — Failure Mode and Effects Analysis

| ID | Failure Mode | Effect | Severity | Detection | Mitigation | System Enforcement |
|----|-------------|--------|----------|-----------|------------|-------------------|
| **FM-1** | Calibration anchors are wrong | All scores systematically biased — every student affected | 🔴 Catastrophic | Distribution anomaly in Phase 4 (all scores cluster at wrong level) | Phase 0 calibration gate requires human lock. Phase 4 distribution check validates anchor quality. | **SP-1**: Anchors cannot be modified after lock without explicit human unlock event |
| **FM-2** | Content extraction misses key evidence | Phase 2 evaluates incomplete evidence → wrong score | 🔴 High | Agent flags low extraction confidence. Phase 3.2 flags score-feedback inconsistency | Extraction confidence threshold. Low-confidence extractions flagged for human review. | **SP-2**: If extraction confidence < 6, submission is auto-routed to slow path |
| **FM-3** | Agent overconfidence on assessment | Low-quality recommendation auto-approves → wrong score | 🔴 High | Human sampling catches errors. Phase 4 drift/outlier detection | Sampling rate (10-20%) of fast-path items. Sample errors trigger confidence model recalibration. | **SP-3**: System enforces minimum sampling rate; sample results feed back into confidence threshold |
| **FM-4** | Human review bottleneck | Slow path backs up → time pressure → degraded human decisions | 🟡 Medium | Queue depth monitoring | Prioritised queue (low-confidence first). Batch presentation to reduce context-switching cost. | **SP-4**: System presents review items in priority order, not FIFO |
| **FM-5** | Integrity false positive | Wrongful accusation → student harm | 🔴 High | Integrity flag has low confidence. Phase 4.6 review catches it | Two-phase integrity process (screen → adjudicate). Flags ≠ findings enforced structurally. | **SP-5**: Integrity flags CANNOT trigger any action without human adjudication. This is not a prompt instruction — it is an infrastructure boundary. |
| **FM-6** | Score calculation error | Wrong total → wrong final grade | 🟡 Medium | Arithmetic is deterministic — error is self-evident on verification | System calculates with audit trail. Manual spot-check protocol. | **SP-6**: Audit lock on total score. Any modification requires human unlock. |
| **FM-7** | Cross-submission inconsistency | Same quality, different score → unfairness | 🔴 High | Phase 4.5 cluster analysis detects it | Agent clusters submissions by score pattern; Human evaluates equivalence. | **SP-7**: If cluster analysis reveals >2SD variance within equivalent-score clusters, auto-flag for human review |
| **FM-8** | Feedback-score mismatch | Student receives misleading information | 🟡 Medium | Phase 3.4 explicitly checks this | Measurer agent (3.2, 3.4) flags mismatches. | **SP-8**: Feedback draft must contain ≥1 evidence citation per claim. System validates before approving. |
| **FM-9** | Drift undetected | Early vs late submissions marked to different standards | 🟡 Medium | Phase 4.3 drift detection | Statistical comparison of score distributions across submission order. | **SP-9**: Drift detection runs automatically; results are non-dismissible — must be acknowledged or addressed |
| **FM-10** | System failure mid-pipeline | Partial data loss → rework from last checkpoint | 🟡 Medium | System health monitoring | Checkpoint after each phase. Resumable pipeline. | **SP-10**: All intermediate results persisted after each wave. Pipeline can resume from last completed phase. |

---

## 5. System Enforcement Points

These are **infrastructure-enforced boundaries**, not prompt instructions. They cannot be bypassed by any agent.

| SP | Enforcement | What It Prevents | Implementation |
|----|-------------|-----------------|----------------|
| **SP-1** | Calibration lock | Modifying anchors after marking begins | `scoring_anchors.lock_status = "locked"` — System rejects writes after lock event |
| **SP-2** | Confidence routing | Agent self-approving low-confidence work | System reads `confidence` field and routes; Agent cannot set own routing path |
| **SP-3** | Minimum sampling | Skipping human quality monitoring | System enforces `sampling_rate ≥ 0.10` on fast-path items; cannot be set to 0 |
| **SP-4** | Review queue priority | Human reviewing easy items first | System sorts queue by `confidence ASC` before presenting to human |
| **SP-5** | Integrity flag isolation | Flags becoming findings without adjudication | `integrity_flags.status` can only transition from `"flag"` → `"substantiated"/"unsubstantiated"/"inconclusive"` via human-only API endpoint |
| **SP-6** | Audit lock on total score | Unauthorized score modification | `total_score.audit_locked = true` — write blocked; requires `human_unlock()` |
| **SP-7** | Cluster variance alert | Missing equivalence problems | If `cluster_variance > 2SD`, System auto-creates mandatory human review item |
| **SP-8** | Citation minimum | Vague feedback without evidence | System validates `evidence_citations.length ≥ 1` per feedback paragraph before approving |
| **SP-9** | Non-dismissible drift | Ignoring drift evidence | Drift report appears as mandatory acknowledgment in Phase 4 human session |
| **SP-10** | Checkpoint persistence | Data loss on failure | All phase outputs written to persistent storage before next phase begins |

---

## 6. Template Architecture

CAWDP defines 7 template types. Here is how each applies:

| Template Type | Where Used | Schema |
|--------------|-----------|--------|
| **Input Template** | Phase 0 inputs (brief, rubric) | `ParsedBrief`, `ParsedRubric` — standardised extraction from raw markdown/CSV |
| **Output Template** | Phase 5 outputs (student report, cohort report) | `StudentReport`, `CohortReport` — markdown with mandatory sections |
| **Handoff Template** | Between all phases | H-1 through H-5 above — typed, versioned schemas |
| **Verification Template** | Phase 3.2, 3.4 | `ConsistencyCheck` — structured pass/fail with evidence |
| **Decision Template** | Phase 2.3, 3.5, 4.6 | `DecisionRecord` — recommendation + decision + rationale + authority |
| **Feedback Template** | Phase 2.4, 3.3 | `FeedbackDraft` — claim + evidence citation + improvement suggestion per paragraph |
| **Escalation Template** | Phase 1.6 → 4.6, Phase 4 flags → human | `EscalationRecord` — flag + evidence + confidence + required action + authority |

---

## 7. Fallback Model Tiers

What happens when the primary actor fails?

| Actor | Failure Mode | Fallback Tier 1 | Fallback Tier 2 |
|-------|-------------|------------------|------------------|
| **Agent** | Model timeout / API failure | Retry with exponential backoff (max 3) | Route to human queue with "agent unavailable" flag |
| **Agent** | Low confidence across all criteria | Route entire submission to slow path | Flag for priority human review |
| **Agent** | Hallucination detected (cites non-existent text) | System validates citations against source document | If citation invalid, mark assessment as "unreliable" and route to human |
| **System** | Infrastructure failure | Resume from last checkpoint (SP-10) | Manual mode — human performs System subtasks with paper/spreadsheet |
| **Human** | Review queue overload | Batch presentation with triage (low-confidence first) | Extend deadline; fast-path sampling rate temporarily increased |
| **Human** | Single marker unavailable | Second marker assigned (if available) | Pipeline pauses at human gate until marker available |

---

## 8. The Architectural Signature

Three properties distinguish this pipeline from a naïve "agent marks everything" approach:

### 1. Confidence-Based Bimodal Routing
The pipeline does not force a binary choice between "agent marks" and "human marks." It creates **two execution paths** based on assessed confidence, with human sampling as the quality bridge between them. This is the operationalisation of "agent prepares judgment; human makes judgment" at scale.

### 2. Infrastructure-Enforced Boundaries
Every authority boundary is enforced by System infrastructure, not by prompt instructions. SP-5 (integrity flag isolation) is the clearest example: an integrity flag **cannot** become a finding through any agent action. The data model makes it structurally impossible — the `status` field only transitions through a human-only API.

### 3. Checkpointed Resumability
The pipeline is designed for the reality that marking large cohorts takes hours or days. Every phase produces a persisted checkpoint. If the system fails mid-execution, it resumes from the last checkpoint, not from the beginning. This is FM-10 mitigation, but it also serves a second purpose: **Phase 4's drift detection relies on ordering data** — the checkpoint includes submission order, enabling the drift analyser to compare early vs. late submissions accurately.

---

Shall I proceed to Phase 4 (Agent Design) — defining the agent roster, job descriptions, and authority boundaries for each agent class in this pipeline?

---
