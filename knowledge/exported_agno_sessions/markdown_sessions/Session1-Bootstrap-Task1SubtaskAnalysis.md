<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Let's examine the bootstrapping phase Step 1 policy document.

Ensuring we are in alignment with the  framework principles (v2) and cross-cutting policy decisions, let's map out each subtask.
We will use a simple hypothetical project to use as a case study so that our decisions and understanding is grounded in proximity to a "real world" project.
Firstly, write an example brief that might be given by the human director if they want to build a single (landing) page static website on their registered domain with AstroJS tooling, using Shadcn components, and deployed to Cloudflare Workers.
The example brief should be high quality to minimise issues in our design phase, and I'm expecting that we will find gaps that we need to answer anyway. The outcomes of this design process for step 1 could help us define the required format and information for the initial brief to be Step 1 ready, and could lead to us designing a Step 0 later - but not now.
Once you have written the brief, focus on Task 1.1 (Brief Inventory) and unpack each subtask.
For each, describe what is happening in the subtask, what skills are required to do it to a high standard, examples of excellence, examples of poor performance. List any uncovered questions or gaps. List any opportunities to improve the Step One policy document. List risks.

[https://github.com/futuresedge/nexus-experiments/blob/main/.framework/policies/bootrapping-policies/01-step-one-policy.md](https://github.com/futuresedge/nexus-experiments/blob/main/.framework/policies/bootrapping-policies/01-step-one-policy.md)

[https://github.com/futuresedge/nexus-experiments/blob/main/.framework/policies/bootrapping-policies/framework-cross-cutting-policies-v0.1.md](https://github.com/futuresedge/nexus-experiments/blob/main/.framework/policies/bootrapping-policies/framework-cross-cutting-policies-v0.1.md)

I have the full Step 1 policy, the cross-cutting policies (FC-1 through FC-9), and all supporting framework documents. Here is the full analysis — beginning with a high-quality example brief, then an unpacking of each Task 1.1 subtask.

***

# Example Project Brief

> **Note:** This brief is written as it might arrive from a human director in practice — structured but naturally incomplete in places. The gaps are intentional and realistic.

***

```
PROJECT BRIEF
Prepared by: Alex Chen
Date: 2026-03-06

Project Name
Meridian Consulting — Launch Landing Page

What I Want to Build
I need a single-page marketing website for my consulting practice, Meridian
Consulting. This will be the public-facing presence for the business and needs
to look professional and modern. The page should have sections for: a hero
introduction, a services overview, an about section, and a contact form that
routes inquiries to my email. I want it to feel clean, minimal, and credible —
think Linear.app or Stripe's marketing pages: clean typography, bold headings,
lots of whitespace.

Technology
I want to build this with AstroJS using Shadcn components for the UI. I expect
this means I'll need the React integration for Astro. Deploy to Cloudflare
Workers on my domain.

Domain
My domain meridianconsulting.com.au is already registered through Cloudflare.
I have a Cloudflare account set up and DNS control.

Environment
I work on a MacBook Pro M2, macOS Sonoma. I use VS Code. I have Node.js
installed but I don't know the exact version off the top of my head. I
normally use npm but I'm open to pnpm if it's better suited to this stack.

People
Alex Chen — project owner, decision-maker, and final approver. That's me.
No other stakeholders.

Scale
Small project. I'd like it done within a week. Just the single page — nothing
else for now.

Constraints
- The contact form must not require a dedicated backend. I want to use a
  third-party form handler — I'm thinking Formspree but I'm open to
  alternatives.
- The site must be fully static — no server-side rendering.
- Must score 90+ on Lighthouse Performance.
- Keep the dependency footprint minimal; avoid unnecessary packages.

Out of Scope (explicitly)
- CMS or any content management capability
- Blog or additional pages
- Analytics integration
- Any server-side logic beyond what Cloudflare Workers provides at the edge

What Success Looks Like
The site is live on meridianconsulting.com.au, passes 90+ Lighthouse
Performance, looks professional, the contact form works, and I can hand it off
to a developer friend later without it being a mess.
```


***

# Task 1.1 — Brief Inventory: Full Subtask Analysis

The Step 1 policy defines Task 1.1 as the first unit of work inside Step 1 (Project Intent Capture).  Its question: *what is in the brief, and does it map to the required schema?* The output is a classified inventory — every element of the brief mapped to a manifest field (PRESENT / ABSENT / AMBIGUOUS), or flagged as non-mappable, with apparent contradictions noted.[^1_1]

***

## Subtask A — Read the Brief in Full Before Any Classification

### What Is Happening

This is an orientation-before-action constraint. The agent must read the complete brief as a coherent statement of human intent before touching the schema. The purpose is to prevent a specific failure mode: pattern-matching the first occurrence of a keyword (e.g., "AstroJS") and immediately populating a field, while missing context that comes later in the brief that changes how that field should be classified.  In the example above, the phrase "no server-side rendering" appears in the constraints section — after the technology declaration. An agent that began classifying `deploymenttarget` mid-read might miss the tension between Cloudflare Workers and the static constraint.[^1_1]

### Skills Required to Do This to a High Standard

- **Patient, non-reactive reading** — the ability to resist acting on the first classification signal
- **Holistic comprehension** — reading the brief as a whole statement, not a data extraction exercise
- **Brief-form recognition** — recognising the form of the brief (email, structured doc, voice transcript, etc.) and understanding what completeness norms are reasonable for that form
- **Prior-knowledge bracketing** — reading the brief as-is, without overlaying domain assumptions; the agent must notice what the human said, not what the agent "knows" to be correct


### Examples of Excellence

The agent reads the full brief, forms a holistic picture, notes the overall quality and structure, and identifies first-impression signals of what might be present vs. absent before a single field is classified. For our example brief, an excellent first read would note: *"Tech stack is named but versions are absent; there is an apparent tension between Cloudflare Workers and the 100% static constraint; the appetite is stated in informal terms not schema vocabulary; Formspree is mentioned tentatively, not declared definitively."*

### Examples of Poor Performance

Beginning to classify after the first section. The agent reads *"AstroJS using Shadcn components"* and mentally marks `techstack = PRESENT`, then reads *"Deploy to Cloudflare Workers"* and marks `deploymenttarget = PRESENT` — and by the time they reach *"The site must be fully static"* in the constraints, they have already formed a classification that doesn't flag the Workers/static tension.[^1_1]

### Uncovered Questions / Gaps

- The policy does not say what to do if the brief is extremely long or arrives as multiple documents (e.g., an email thread + a separate notes file). There is no guidance on how to treat a multi-part brief.
- There is no instruction to note the *form* of the brief. A voice memo transcript has different completeness norms than a structured brief document. This matters for calibrating which gaps are systemic (the format doesn't support this information) vs. missing (the human had the information but didn't include it).


### Opportunities to Improve the Step 1 Policy

- Add an explicit first micro-step: *"Note the form and source of the brief before reading."* Brief form is relevant context for every classification that follows.
- Add guidance for multi-part briefs: if the brief arrives as multiple documents or a thread, define which source is canonical and how conflicts between sources are treated.


### Risks

- **Premature classification lock-in:** Starting to classify mid-read creates implicit commitments that bias the rest of the inventory. This is especially dangerous for AMBIGUOUS fields, where late-brief context (constraints, out-of-scope sections) often changes the classification.
- **Brief form misread:** Treating a high-quality structured brief as complete when it's actually incomplete is more likely than with a rough email brief — the quality of the writing creates a false impression of completeness.

***

## Subtask B — For Each Required Field, Identify Whether the Brief Contains Sufficient Information to Populate It

### What Is Happening

A systematic, field-by-field walk through the manifest schema. For each required field, the agent asks: *does the brief contain specific, usable information for this field?* The output is a three-way classification — PRESENT (sufficient, usable), ABSENT (no information at all), or AMBIGUOUS (present but unclear or incomplete enough to fail if used as-is).[^1_1]

Applied to the example brief against the manifest schema:[^1_1]


| Field | Classification | Reason |
| :-- | :-- | :-- |
| `projectname` | PRESENT | Clearly stated: "Meridian Consulting — Launch Landing Page" |
| `projectid` | PRESENT by derivation | Derived from projectname via kebab-case rule: `meridian-consulting-launch-landing-page` |
| `description` | PRESENT | Sufficient content for 2–4 sentences |
| `techstack` | AMBIGUOUS | AstroJS and Shadcn are named, but no versions specified; the React integration is implied but not explicitly named as a stack element; npm vs. pnpm is unresolved |
| `deploymenttarget` | AMBIGUOUS | "Cloudflare Workers" is named, but this conflicts with "100% static" — the more typical static AstroJS deployment target is Cloudflare Pages, not Workers; the domain is named |
| `devenvironment` | AMBIGUOUS | OS and editor named; runtime named but version explicitly unknown ("don't know the exact version"); package manager ambiguous |
| `humanactors` | PRESENT | "Alex Chen — project owner, decision-maker, and final approver" — one humandirector present, clearly named |
| `appetite` | AMBIGUOUS | "Small project, within a week" is present but doesn't map to the schema's enum vocabulary (SMALL / MEDIUM / LARGE); needs explicit confirmation |

### Skills Required to Do This to a High Standard

- **Schema literacy** — complete familiarity with every required field: its type, format rules, valid values, and downstream use in Steps 2 and 3
- **Classification discipline** — distinguishing PRESENT, ABSENT, and AMBIGUOUS without collapsing AMBIGUOUS into PRESENT to avoid asking questions
- **No-invention discipline** — the most critical skill: not filling in the blanks with reasonable assumptions. The agent may know that AstroJS 5.x is the current stable version — this knowledge must not silently populate a version field that the human did not state
- **Technical awareness for tension detection** — for the Workers/static case, detecting that "Cloudflare Workers" and "100% static" may be technically in tension requires enough domain knowledge to recognise the distinction between Cloudflare Workers (edge functions) and Cloudflare Pages (static asset hosting)


### Examples of Excellence

- Classifying `techstack` as AMBIGUOUS (not PRESENT) with a specific note: *"AstroJS: named, version absent. Shadcn: named, version absent. React integration: implied by Shadcn dependency, not explicitly stated. Package manager: ambiguous — npm stated as default, pnpm mentioned as acceptable alternative."*
- Classifying `deploymenttarget` as AMBIGUOUS with note: *"Cloudflare Workers named. Potential tension with 'fully static' constraint — Workers requires AstroJS Cloudflare adapter; Cloudflare Pages may be the intended target. Requires clarification."*
- Classifying `appetite` as AMBIGUOUS rather than mapping "within a week" to SMALL without human confirmation.


### Examples of Poor Performance

- Classifying `techstack` as PRESENT because AstroJS and Shadcn are named, without noting the version gaps or the implied React dependency.
- Classifying `deploymenttarget` as PRESENT because "Cloudflare Workers" is explicitly stated, without recognising the technical tension — effectively silently resolving a contradiction using domain knowledge.[^1_1]
- Classifying `appetite` as PRESENT by inferring SMALL from "a week" — this is an undocumented derivation, not a confirmed field value.


### Uncovered Questions / Gaps

- The policy defines the classification vocabulary (PRESENT / ABSENT / AMBIGUOUS) but does not specify what "sufficient information" means per field type. For `techstack`, the schema rule *("Named technologies only, not categories — AstroJS 5.x is valid, modern frontend stack is not")* effectively defines sufficiency for that field. But for `devenvironment` or `appetite`, no equivalent sufficiency rule exists in the policy. This leaves classification judgment to the agent.
- The `projectid` field is derived from `projectname` via the kebab-case rule — the policy documents this as a permitted derivation. But the policy doesn't address what happens if the projectname contains characters that make the derivation ambiguous (e.g., special characters, non-ASCII).


### Opportunities to Improve the Step 1 Policy

- Add field-level sufficiency rules to the manifest schema definition — not just format rules, but explicit statements of what makes a value "sufficient" vs. "ambiguous." For `techstack`, this already exists; extend it to `devenvironment`, `appetite`, and `deploymenttarget`.
- Add a note acknowledging that contradiction detection in this subtask may require domain expertise, and specifying what to do when it does (flag as a potential contradiction for human confirmation — do not silently resolve).


### Risks

- **Version ambiguity carrying forward silently:** If `techstack` is classified PRESENT because technology names are stated, Task 1.2 won't generate a clarification request for versions. Step 2's environment contract will then need to resolve versions without a clear brief source — either inventing them (FC-1 violation) or failing to produce a complete contract.[^1_1]
- **Technical knowledge substituting for human confirmation:** An agent with AstroJS expertise may classify the Workers/static tension as "not a real contradiction" and mark `deploymenttarget` PRESENT. This violates the no-invention invariant — the agent's technical knowledge is not a valid source type.[^1_1]
- **AMBIGUOUS used as a catch-all:** If the classification is AMBIGUOUS without a specific note explaining *what* is ambiguous, Task 1.2 cannot produce a well-formed clarification question. The inventory becomes a list of vague flags rather than actionable inputs.

***

## Subtask C — For Each Optional Field, Identify Whether the Brief Contains Relevant Information

### What Is Happening

The agent repeats the field-by-field check for optional fields. The purpose is to prevent information the human *did* provide from being lost because it didn't trigger a BLOCKING classification.  Optional fields that are PRESENT but missed here result in a manifest that discards human-provided content — a failure of fidelity, even if not a blocking structural error.[^1_1]

Applied to the example brief:


| Optional Field | Classification | Reason |
| :-- | :-- | :-- |
| `constraints` | PRESENT | Four explicit constraints stated: no backend, fully static, 90+ Lighthouse, minimal dependencies |
| `outofscope` | PRESENT | Four explicit out-of-scope items stated: CMS, blog/pages, analytics, server-side logic |
| `existingassets` | ABSENT | Not mentioned |
| `referenceexamples` | PRESENT | Linear.app and Stripe marketing pages named, with quality descriptors |
| `integrationrequirements` | AMBIGUOUS | Formspree named tentatively ("I'm thinking Formspree but open to alternatives") — present but not a confirmed integration requirement |

### Skills Required to Do This to a High Standard

- **Completeness orientation** — not stopping after required fields; treating the optional field sweep as equally important
- **Information vs. confirmation distinction** — recognising that "I'm thinking Formspree" is not a confirmed integration requirement but is still information that must be captured, not discarded
- **Downstream consequence awareness** — understanding that `referenceexamples` (Linear, Stripe) has direct bearing on design standards and pattern seeding in Step 4, even though it's optional


### Examples of Excellence

Capturing Formspree as an AMBIGUOUS optional integration requirement, with a note: *"Third-party form handler mentioned tentatively; specific provider unconfirmed. Downstream impact: if no provider is confirmed, the environment contract cannot specify integration details. Classify as WARNING."*

Noting that the reference examples (Linear, Stripe) include specific quality descriptors ("bold typography, lots of whitespace") that exceed what the `referenceexamples` field is designed to hold — flagging this as non-mappable content for Subtask D.

### Examples of Poor Performance

- Stopping after required fields — treating the optional sweep as a lower-priority step to be skipped if time is short.
- Classifying `integrationrequirements` as ABSENT because no firm decision was made about Formspree.
- Capturing `referenceexamples` as PRESENT without noting the additional design-intent descriptors that accompany them.


### Uncovered Questions / Gaps

- The policy's optional field list does not include a field for "existing infrastructure readiness" — in this brief, the human mentions their Cloudflare account is set up and DNS control is available. This is operationally relevant (it affects Step 2's environment contract) but no optional field exists for it.
- The AMBIGUOUS classification for optional fields is not addressed in the policy — it defines PRESENT and ABSENT for optional fields, but the Formspree case is neither. The handling of AMBIGUOUS optional fields is implied but not stated.


### Opportunities to Improve the Step 1 Policy

- Add an "existing infrastructure" or "pre-configured services" optional field to the manifest schema to capture information about accounts, DNS control, and third-party service access that affects the environment contract.
- Clarify the AMBIGUOUS classification for optional fields — specify that it maps to a WARNING openquestion entry, with the same structure as BLOCKING items but lower severity.


### Risks

- **Reference examples treated as decorative:** If `referenceexamples` is noted as PRESENT but the quality descriptors (typography, whitespace) are not also captured, the human's design intent is partially lost. This may not surface until Step 4 (pattern seeding) when the lack of design direction becomes apparent.
- **Formspree ambiguity ignored:** If the form handler ambiguity is not captured as an AMBIGUOUS optional field, there will be no openquestion entry for it in the manifest. The environment contract in Step 2 will then either invent an integration choice or produce an incomplete contract.[^1_1]

***

## Subtask D — Note Any Information in the Brief That Does Not Map to Any Field

### What Is Happening

This is the "overflow" pass — the agent scans the brief for content that was noted but doesn't fit neatly into any manifest schema field.  The policy notes this "may indicate scope, constraints, or out-of-scope material not yet captured." This subtask is the safety net for schema incompleteness: it exists because no schema perfectly covers all human-provided information.[^1_1]

From the example brief, non-mappable content includes:

- *"meridianconsulting.com.au is already registered through Cloudflare"* — domain registration status and registrar identity. Partially relevant to `deploymenttarget` but not fully captured by the field's format rules.
- *"I have a Cloudflare account set up and DNS control"* — access/credential readiness. No manifest field exists for this.
- *"I can point it wherever needed"* — DNS management capability. Not in the schema.
- *"What Success Looks Like"* section — the human's explicit success criteria include "looks professional," "the contact form works," and "I can hand it off to a developer friend later without it being a mess." The last element is a handoff/maintainability requirement that no manifest field captures.
- Design quality descriptors attached to reference examples — "clean typography, bold headings, lots of whitespace."


### Skills Required to Do This to a High Standard

- **Schema humility** — the active recognition that the schema may not capture everything of value, and that the agent's job is fidelity to the brief, not mapping to the schema
- **Operational relevance judgment** — distinguishing between non-mappable content that has downstream consequence (Cloudflare account access) and non-mappable content that is contextual (the quality descriptors)
- **Structured capture** — recording non-mappable items with enough specificity that they can be actioned downstream


### Examples of Excellence

Creating a clearly labelled "non-mappable information" section in the inventory with entries like: *"Domain registered through Cloudflare — registrar and DNS control available. No manifest field; relevant to Step 2 environment contract (no domain procurement task needed, DNS configuration is self-managed)."* And *"Maintainability requirement: 'handoff to a developer friend' — implies code quality standards not captured in any manifest field. Flag for consideration as an optional constraints entry."*

### Examples of Poor Performance

Not performing this subtask at all because "the schema is the schema." This is the most commonly skipped subtask — it produces no manifest field values, so the output feels less actionable than subtasks B and C. But it is where the most structurally important gaps in the schema become visible.[^1_1]

### Uncovered Questions / Gaps

- **No downstream home for non-mappable information.** The policy says to note non-mappable content "for consideration" but no subsequent task (1.2 through 1.5) explicitly picks it up. The non-mappable list is produced but its fate is unclear. Does it feed into the `openquestions` field? Does it become a schema improvement recommendation? Does it disappear?
- **No distinction between "not in the schema yet" and "not appropriate for the schema."** Some non-mappable content (Cloudflare account access) arguably belongs in the manifest schema; some (typography quality descriptors) probably doesn't. The policy doesn't help the agent make this distinction.


### Opportunities to Improve the Step 1 Policy

- Add an explicit instruction in Task 1.4 (Manifest Drafting) to review the non-mappable list and determine whether any entries should be added as `openquestions` or `constraints` entries.
- Consider adding a "non-mappable notes" optional field to the manifest schema, or a separate companion document analogous to the traceability record, so this information has a formal place to live.
- Connect Subtask D outputs to a schema evolution feedback mechanism — recognising that the example brief has already revealed two candidate new fields (`existingInfrastructure`, `successCriteria`) that the current schema doesn't accommodate.


### Risks

- **Operational readiness gaps in Step 2:** If the Cloudflare account/DNS control information is not captured anywhere, Step 2's environment contract cannot reference it. An agent writing the environment contract will either invent an assumption about DNS management (FC-1 violation) or produce a contract with a gap.[^1_1]
- **Schema appears more complete than it is:** The existence of Subtask D implies the schema is a work in progress. If non-mappable outputs are consistently discarded, the schema never improves — and every future brief will have the same gaps.

***

## Subtask E — Note Any Apparent Contradictions Between Elements of the Brief

### What Is Happening

The agent cross-references the brief's elements against each other, testing for internal consistency. The policy is explicit: *"Contradictions in the brief are surfaced before the record is written, not silently resolved."*  Any contradiction identified here is classified as BLOCKING in Task 1.2 — it cannot be downgraded.[^1_1]

The example brief contains one significant contradiction:

**"Deploy to Cloudflare Workers" + "The site must be fully static — no server-side rendering"**

These two statements are not inherently incompatible — Cloudflare Workers can serve static files. But the relationship is technically non-trivial:

- AstroJS's Cloudflare integration (`@astrojs/cloudflare`) targets Cloudflare Workers as an edge runtime, which requires the AstroJS `server` or `hybrid` output mode — not `static`
- Cloudflare Pages is the appropriate Cloudflare product for fully static AstroJS deployment
- The human may have conflated "Cloudflare Workers" (a compute product) with "Cloudflare hosting" in general

This is not a contradiction that can be resolved by technical knowledge — it must be surfaced as a BLOCKING clarification request to confirm what the human intended.

A secondary inconsistency: *"no server-side rendering"* is listed in constraints, but the "Out of Scope" section includes *"any server-side logic beyond what Cloudflare Workers provides at the edge"* — this hedge implies the human is aware Workers has some edge compute capability, which suggests they may intend a Workers deployment with edge functions for the form handler, not purely static hosting. This further reinforces the need for clarification.

### Skills Required to Do This to a High Standard

- **Technical domain knowledge** — detecting the Workers/Pages distinction requires knowledge of Cloudflare's product lineup and AstroJS's output modes
- **Consistency checking under uncertainty** — the ability to hold two statements in tension and flag them rather than collapsing them into a single interpretation
- **Surfacing without resolving** — the critical discipline: note the contradiction and pass it to Task 1.2 as BLOCKING; do not decide which element "wins"


### Examples of Excellence

Flagging: *"CONTRADICTION: deploymenttarget = 'Cloudflare Workers' conflicts with constraint 'fully static / no server-side rendering.' AstroJS static output mode is not compatible with the Cloudflare Workers adapter. The intended deployment target may be Cloudflare Pages. The out-of-scope note 'beyond what Cloudflare Workers provides at the edge' may indicate the human intends to use Workers edge functions for the form handler. Both elements require clarification before `deploymenttarget` can be populated. Classify as BLOCKING."*

### Examples of Poor Performance

- Not detecting the contradiction because "Workers can serve static files, so it's fine" — silently resolving the tension using technical knowledge rather than surfacing it for human confirmation.
- Detecting the contradiction but classifying it as AMBIGUOUS rather than BLOCKING — allowing the manifest to be drafted with an unresolved architectural tension baked in.
- Noting the contradiction in `deploymenttarget` but not also noting its implication for `techstack` (the AstroJS output mode configuration is part of the stack, not just the deployment target).


### Uncovered Questions / Gaps

- The policy does not address contradictions that can only be detected with domain expertise. If the agent lacks knowledge of Cloudflare's product lineup, the Workers/static tension is invisible. The policy assumes the classifier has sufficient technical knowledge, but this assumption is not stated.
- The policy does not address contradictions that span optional and required fields. The out-of-scope note about "edge logic" is in an optional section; the static constraint is in a required-adjacent section. The policy's focus on "required field" classification may cause the agent to miss cross-section contradictions.


### Opportunities to Improve the Step 1 Policy

- Add an explicit note that technical contradictions — those which can only be detected with domain knowledge — should be flagged as *potential* contradictions for human confirmation, rather than either silently resolved or definitively classified. This introduces a fourth classification category for this subtask only: *POTENTIAL CONTRADICTION (requires domain expertise to confirm)*.
- Specify that contradiction detection must scan across all sections of the brief, not only between required fields.


### Risks

- **Silent architectural decisions:** The most dangerous risk in this subtask. An agent with strong technical knowledge is more likely to silently resolve contradictions than an agent with less knowledge — because they "know" the right answer. But the right answer may not match what the human intended. The no-invention invariant is precisely designed to prevent this, but Task 1.1's subtasks don't explicitly invoke FC-1 at the contradiction-detection stage.[^1_1]
- **Downstream architecture locked on wrong assumption:** If the Workers/static contradiction is not surfaced here, the `deploymenttarget` field will be populated with "Cloudflare Workers." Step 2's environment contract will then be written for a Workers deployment. By the time the error surfaces (likely during Step 5's smoke test or during actual deployment), the entire environment specification has been built on a false premise.

***

# Cross-Cutting Observations for Task 1.1

## Output Format Gap (Applies to All Subtasks)

The policy defines the *content* of Task 1.1's output (a classified inventory) but not its *format*.  Task 1.2 consumes this inventory — but if the inventory format is not standardised, Task 1.2 cannot be reliably implemented. A recommended addition to the policy: specify a canonical schema for the classified inventory document, e.g.:[^1_1]

```
field | classification | brief_reference | notes
```

This would make the output machine-readable, testable, and consistent across runs.

## Vocabulary Mismatch Between Task 1.1 and FC-2

Task 1.1 uses PRESENT / ABSENT / AMBIGUOUS.  FC-2's gap classification taxonomy uses BLOCKING / WARNING / LOWRISK.  These are different vocabularies that operate at different stages — 1.1 classifies what exists in the brief; Task 1.2 translates that into FC-2 terms. This relationship is correct but implicit. Making it explicit in the policy ("Task 1.1 outputs are translated into FC-2 classifications by Task 1.2; they are not the same vocabulary") would prevent the two classification systems from being conflated or collapsed.[^1_1]

## The No-Invention Invariant Is Active from Subtask B Onwards

FC-1 (no-invention invariant) requires that every output field value trace to a named source.  Task 1.1 is not a drafting step — it produces a classification, not field values. But the *notes* attached to classifications are proto-values: they begin to shape how fields will be populated. The policy should note that FC-1 applies to the inventory notes, not only to the manifest drafting step. An inventory note that says *"techstack: AstroJS 5.x, Shadcn 2.x"* (with invented versions) violates FC-1 even though no manifest field has been drafted yet.[^1_1]

## Recommendation: Explicit Step 0 Signals from This Brief

The gaps surfaced by Task 1.1 on this brief provide strong evidence for what a Step 0 brief template should require:

- Explicit technology versions for all named stack elements
- Confirmation of deployment target at the product level (Cloudflare Workers vs Pages vs R2, not just "Cloudflare")
- Explicit package manager selection
- Appetite stated in schema vocabulary (SMALL / MEDIUM / LARGE)
- Third-party integrations declared explicitly, not tentatively
- A field for existing infrastructure readiness (domain registrar, hosting accounts)

These are not design decisions to be made now — but they are findings from this analysis that belong in the record as future Step 0 design inputs.[^1_1]
<span style="display:none">[^1_10][^1_2][^1_3][^1_4][^1_5][^1_6][^1_7][^1_8][^1_9]</span>

<div align="center">⁂</div>

[^1_1]: i-am-making-progress-in-creati-fuGLU8hCRLyka3xtBTVglA.md

[^1_2]: i-want-to-focus-now-on-the-boo-c1wm6o9LR_iWkCkK9hz5qQ.md

[^1_3]: zone-uncertainty-analysis.md

[^1_4]: context-curation-pattern.md

[^1_5]: agent-creation-policy-v0.1.md

[^1_6]: OpenQuestions.md

[^1_7]: ONE-Ontology.md

[^1_8]: NexusModelOverview.md

[^1_9]: NexusDecisionsRationale.md

[^1_10]: nexus-suggested-resources.md


---

# My notes:

- Let's not concern ourselves with the form of the brief. We can develop a standardised brief for acceptance as valid input for Step one. We could publish a web form that a human can fill out - or an agent can fill from parsing an uploaded brief - but this will be Step 0 and is therefore out of scope at the moment.
- Could it be beneficial to decompose the prose into a list of declarative statements? Each statement can be assessed/scored for its clarity or ambiguity, can be categorised by associated fields, and sorted, inconsistencies or contradictions linked for easier review. Is this a new subtask or part of Subtask A? I suspect this will simplify the following subtasks.
- I used the terminology `BLOCKING / WARNING / LOWRISK` in an earlier response, as a suggestion or option only - not as a directive.  I prefer to conform to generally accepted terminology where possible.
- Do we need to make any decisions before continuing to Task 1.2?

If yes, what are they? If no, continue to Task 1.2 and repeat this process

Good notes. Addressing each before stating whether decisions are needed.

***

## Note Responses

**On brief form:** Agreed — Step 0 is out of scope. This simplifies Subtask A. The policy should not prescribe how a brief arrives. Step 1 receives it in whatever form and proceeds.[^2_1]

**On decomposing prose into declarative statements:** This is a strong idea and warrants a decision (see below). The short answer is it should be a distinct, new subtask — not folded into Subtask A. Subtask A is orientation (read, form a whole-picture impression before acting). The decomposition is an active transformation with a structured output. Collapsing them conflates reading with processing.[^2_1]

**On terminology:** Agreed — the policy should use widely accepted vocabulary. The concepts in FC-2 are settled (three tiers, two terminal states) but the labels should be reviewed before they propagate into every subsequent task, step policy, and skill file.[^2_1]

**On whether decisions are needed before Task 1.2:** Yes — two decisions. Task 1.2 is entirely about gap classification. If the vocabulary isn't settled and the Task 1.1 output structure isn't confirmed, Task 1.2 cannot be precisely defined. Both decisions are low-effort but high-leverage.

***

## Decision 1 — Subtask Structure for Task 1.1

**The question:** Where does the declarative statement decomposition sit?

The proposed insertion is a new subtask between the current Subtask A (Read in full) and Subtask B (Field-by-field classification). Under this structure, all subsequent subtasks operate on a pre-processed statement list rather than raw prose — making them faster, more reliable, and easier to test.

**Proposed revised Task 1.1 subtask sequence:**


| \# | Subtask | Input | Output |
| :-- | :-- | :-- | :-- |
| A | **Brief Orientation** — read in full; form a holistic impression before classifying anything | Raw brief | Mental/noted whole-picture impression; no output document |
| **B (new)** | **Statement Decomposition** — parse the brief into discrete, atomic declarative statements; tag each with candidate field(s); score each for clarity vs. ambiguity; link apparent contradictions | Raw brief + schema | Structured statement list: `[statement_text, candidate_fields[], clarity_score, linked_statements[]]` |
| C | **Required Field Mapping** — for each required field, identify supporting statements; classify as PRESENT / ABSENT / AMBIGUOUS | Statement list | Required field inventory |
| D | **Optional Field Mapping** — same for optional fields | Statement list | Optional field inventory |
| E | **Non-Mappable Statements** — identify statements with no field match | Statement list | Non-mappable list |
| F | **Contradiction Review** — review pre-linked statement pairs; confirm or dismiss each as a contradiction | Linked statements from B | Contradiction list |

**Options:**

- **Option A** — Add the decomposition as a new distinct Subtask B, shifting existing subtasks to C–F. *(Recommended)*
- **Option B** — Fold the decomposition into Subtask A, making A a combined "read + decompose" step. Simpler on paper, but the skills and outputs of reading and decomposing are different. Orientation is passive; decomposition is structured production — merging them obscures both.
- **Option C** — Keep the current subtask sequence unchanged; treat decomposition as an optional technique the agent may use internally rather than a formal step. This sacrifices the traceability and testability benefits the idea offers.

**Recommendation:** Option A. The decomposition's output (the statement list) is itself a reviewable, testable intermediate artefact. It forms the input to four subsequent subtasks, making it load-bearing — not just a technique. Making it explicit protects against incomplete or inconsistent classification by ensuring every part of the brief is processed before any field is mapped.

***

## Decision 2 — Gap Classification Vocabulary

**The question:** What labels should the three-tier FC-2 taxonomy use?[^2_1]

The three concepts and their decision rules are settled. Only the labels need confirming. The current labels are `BLOCKING / WARNING / LOWRISK`.

**Options:**


| Option | Tier 1 (stops work) | Tier 2 (quality impact) | Tier 3 (noted only) | Notes |
| :-- | :-- | :-- | :-- | :-- |
| **A** — Current labels | `BLOCKING` | `WARNING` | `LOWRISK` | Internally consistent; `LOWRISK` is less standard than the others |
| **B** — Jira/GitHub standard | `BLOCKER` | `WARNING` | `INFO` | `BLOCKER` and `WARNING` are universally understood in software tooling; `INFO` is standard in log-level vocabulary |
| **C** — Risk management | `CRITICAL` | `HIGH` | `LOW` | Familiar in risk/QA contexts; `CRITICAL` and `BLOCKER` have different connotations — critical implies severity, blocker implies progress impact |
| **D** — RFC 2119 inspired | `MUST` | `SHOULD` | `MAY` | Precise; widely used in technical specifications; but these read as requirement strength, not gap severity — they fit what the brief *must contain*, less well as gap labels |

**Terminal states** (currently `BLOCKING-RESOLVED` and `BLOCKING-CONFIRMED-UNKNOWN`) become under each option:

- **Option A:** `BLOCKING:RESOLVED` / `BLOCKING:CONFIRMED-UNKNOWN`
- **Option B:** `BLOCKER:RESOLVED` / `BLOCKER:CONFIRMED-UNKNOWN`
- **Option C/D:** Similar compound forms

**Recommendation:** Option B — `BLOCKER / WARNING / INFO`. Rationale:

- `BLOCKER` is the noun form used natively in GitHub, Linear, Jira, and most project tooling — engineers recognise it immediately without a definition
- `WARNING` is already the standard term in compilers, linters, CI output, and log levels
- `INFO` replaces `LOWRISK` — it drops the risk-assessment connotation (these are gaps, not risks) and aligns with the log-level tier structure (`ERROR / WARNING / INFO`) which is as widely understood as any vocabulary in software

The existing FC-2 decision record should be amended to update the labels only — the classification rules, behaviour, and terminal states remain identical.[^2_1]

***

**Please confirm or redirect on each decision and I'll continue to Task 1.2.**

<div align="center">⁂</div>

[^2_1]: i-am-making-progress-in-creati-fuGLU8hCRLyka3xtBTVglA.md


---

## Decision 1 — Your amendment is correct

The proposed structure is stronger. Here is why the "read in full" as a universal precondition is better than as a standalone first subtask: it encodes the discipline without making an unverifiable act into a formal step. A precondition instruction ("before beginning this subtask, read the complete input in full") is testable by the agent's own behaviour — if a subtask produces output that misses a late-brief element, the audit log will reveal it. A dedicated Subtask A with no output is simply unauditable.[^3_1]

**Finalised Task 1.1 Structure:**

*Standing instruction applied to all subtasks: read the complete input for this subtask before producing any output.*


| \# | Subtask | Input | Output |
| :-- | :-- | :-- | :-- |
| 1 | Statement Decomposition | Raw brief + manifest schema | Structured statement list |
| 2 | Required Field Mapping | Statement list | Required field inventory (PRESENT / ABSENT / AMBIGUOUS per field) |
| 3 | Optional Field Mapping | Statement list | Optional field inventory |
| 4 | Non-Mappable Identification | Statement list | Non-mappable statement list |
| 5 | Contradiction Review | Statement list + linked statement pairs from Subtask 1 | Confirmed contradiction list |

## Decision 2 — Confirmed

`BLOCKER / WARNING / INFO` is now the canonical vocabulary for gap severity across all step policies. FC-2 terminal states become `BLOCKER:RESOLVED` and `BLOCKER:CONFIRMED-UNKNOWN`.[^3_1]

***

No further decisions are needed before Task 1.2. The classification rules (FC-2), the input structure (finalised Task 1.1 output), the vocabulary, and the downstream context (what Steps 2 and 3 require) are all stable enough to proceed.

***

# Task 1.2 — Gap Classification: Full Subtask Analysis

Task 1.2's question: *which gaps are blocking and which can be surfaced as open questions?*  It receives the five classified outputs of Task 1.1 and applies the FC-2 taxonomy to produce the first entries in the shared open questions register — the persistent FC-8 record that travels through all six bootstrap steps.[^3_1]

***

## Subtask 1 — Classify Each ABSENT or AMBIGUOUS Required Field

### What Is Happening

Each ABSENT or AMBIGUOUS required field from Task 1.1's Required Field Mapping (Subtask 2) is tested against the FC-2 classification rule:[^3_1]

> *Would proceeding without this information, or getting it wrong, cause a subsequent step to fail or produce a materially incorrect output?*
> - YES → BLOCKER
> - NO → apply second test: does the absence have a known, specific downstream impact?
>   - YES → WARNING
>   - NO → INFO

Applied to our case study (ABSENT/AMBIGUOUS required fields only):


| Field | Task 1.1 Status | Classification Test | Classification |
| :-- | :-- | :-- | :-- |
| `techstack` — versions absent | AMBIGUOUS | Step 2's environment contract requires exact or minimum versions for `runtime.version` and `framework.version`. Without them, those fields either cannot be populated or must be invented — an FC-1 violation. | **BLOCKER** |
| `techstack` — React integration implicit | AMBIGUOUS | Step 2 cannot write a complete framework section if one stack dependency is undeclared. A missing adapter (`@astrojs/react`) means missing install commands, config entries, and version fields in the contract. | **BLOCKER** |
| `deploymenttarget` — Workers vs. Pages unclear | AMBIGUOUS | The entire deployment section of Step 2's environment contract is conditioned on this. A Workers contract and a Pages contract are structurally different documents. Proceeding with either assumption produces an incorrect contract. | **BLOCKER** |
| `devenvironment.runtime.version` — unknown | AMBIGUOUS | The human stated they don't know the version. Step 2 needs it for `runtime.version`. This is likely to become `BLOCKER:CONFIRMED-UNKNOWN` after clarification — the human genuinely may not know — but it's still a BLOCKER to attempt. | **BLOCKER** |
| `devenvironment.packagemanager` — ambiguous | AMBIGUOUS | Step 2's `runtime.packagemanager` and `runtime.installcommand` fields depend on this directly. "npm or pnpm" is not a valid contract value. | **BLOCKER** |
| `appetite` — informal value | AMBIGUOUS | `appetite` is a REQUIRED schema field. "Within a week" is present but doesn't match any valid enum value. Step 2 and Step 3 do not consume `appetite` directly, so the downstream step failure test returns NO. But see Gap note below. | **See gap ↓** |

### Skills Required to Do This to a High Standard

- **Step 2 schema knowledge** — the classifier must know what Step 2's environment contract needs, field by field, to assess whether a gap causes Step 2 to fail. This knowledge is not embedded in Task 1.2's description; it is a prerequisite competency
- **Worst-case reasoning** — the classification test is about what happens if the gap is not resolved; this requires imagining Step 2 executing with the gap in place, not imagining the most charitable resolution
- **Strict separation of classification from resolution** — the classifier must not simultaneously classify and propose an answer. "This is BLOCKER because Step 2 needs a version number; we should assume AstroJS 5.x" is two acts merged into one. Only the first belongs in Task 1.2
- **FC-1 awareness** — the classifier must recognise that any classification of a required field as non-BLOCKER must be grounded in evidence that Step 2 can proceed without it, not in the assumption that it will be resolved later


### Examples of Excellence

Classifying `techstack` versions as BLOCKER with the specific impact statement: *"Step 2 environment contract sections `framework.version` and `runtime.version` cannot be completed. Those fields require exact or minimum version values; populating them from assumed current-stable versions would violate FC-1."*

Treating the `appetite` enum mismatch as a separate and distinct classification question rather than collapsing it into the techstack issues — each field gets its own classification entry.

### Examples of Poor Performance

- Classifying `devenvironment.runtime.version` as WARNING because "Node.js version can be checked later during environment setup." This mistakes a deployment-time resolution for a contract-time requirement. Step 2 needs the version to write the contract, not to run the environment.
- Classifying `appetite` as non-BLOCKER and leaving it unaddressed — because it doesn't affect Step 2 or 3 — without flagging that it is a REQUIRED field that can't be left empty in the manifest.
- Writing compound classification entries: one entry for "techstack issues" covering versions, package manager, and React integration together. Each gap must be a separate entry in the open questions register with its own `questionid`, `field`, and `impact`.[^3_1]


### Uncovered Questions / Gaps

**The classification test has a scope limit.** The FC-2 test asks whether the gap would cause "a subsequent step to fail."  Applied strictly, this means Step 2 or Step 3. But `appetite` is a REQUIRED field whose absence makes the manifest structurally incomplete — yet it has no direct bearing on Steps 2 or 3. The test as written would classify it as non-BLOCKER. But an empty REQUIRED field is an invalid manifest, and an invalid manifest fails DoD 3 (all required fields non-empty).[^3_1]

**Resolution:** The classification test needs a third entry point:

> Is the field REQUIRED in the manifest schema and unable to be validly populated from the current brief?
> - YES → BLOCKER (the manifest cannot pass its DoD without it)

This is not covered by FC-2 and should be raised as an improvement to the cross-cutting policies.

**No guidance on AMBIGUOUS vs. ABSENT classification difference.** Both feed into the same downstream test, but AMBIGUOUS fields require a different question format than ABSENT ones. An ABSENT field needs: *"What is your X?"* An AMBIGUOUS field needs: *"You stated X — can you confirm whether you mean Y or Z?"* The policy doesn't distinguish these in the classification subtask or in FC-3's question formulation rules.[^3_1]

### Opportunities to Improve the Step 1 Policy

- Add the third entry point to the FC-2 classification test: REQUIRED schema fields that cannot be validly populated are BLOCKER regardless of downstream step dependency.
- Explicitly distinguish ABSENT-triggered and AMBIGUOUS-triggered BLOCKER entries in the open questions register — they require different question structures in Task 1.3.


### Risks

- **Appetite field left as an empty REQUIRED field:** If classified as non-BLOCKER and no clarification is sought, the manifest either fails DoD 3 or the field is populated by inference — an FC-1 violation. Neither outcome is acceptable.[^3_1]
- **Single BLOCKER entry for multiple gaps in one field:** If `techstack` generates one BLOCKER entry rather than separate entries for "AstroJS version," "React integration," and "package manager," Task 1.3 will ask one compound question and receive a compound answer that is difficult to individually attribute in the traceability record.

***

## Subtask 2 — Classify Each ABSENT Optional Field

### What Is Happening

Each ABSENT (and AMBIGUOUS) optional field is tested against the second and third tiers of FC-2:[^3_1]

> Does the absence have a known, specific impact on the quality of any downstream output?
> - YES → WARNING
> - NO → INFO

Applied to the case study:


| Field | Task 1.1 Status | Classification | Reason |
| :-- | :-- | :-- | :-- |
| `constraints` | PRESENT | — | Not absent; no entry needed |
| `outofscope` | PRESENT | — | Not absent |
| `existingassets` | ABSENT | **INFO** | No downstream step uses existing assets in bootstrap; absence has no quality impact |
| `referenceexamples` | PRESENT | — | Not absent |
| `integrationrequirements` — Formspree tentative | AMBIGUOUS | **WARNING** | Step 2's services section requires a named integration. An unconfirmed provider means that section cannot be completed, or must be written as "TBD" — a known quality degradation |
| Infrastructure readiness (non-mappable — Cloudflare account, DNS) | Not in schema | **→ Non-mappable path** | See Task 1.1 Subtask 4 output; handled separately |

### Skills Required to Do This to a High Standard

- **Downstream quality reasoning** — distinguishing a gap that "might matter" from a gap with a *known, specific* downstream impact. The FC-2 standard requires specificity: "WARNING" is not "this could be a problem." It requires naming the downstream field or step that degrades.
- **Optional-field discipline** — the tendency to dismiss all optional field gaps as INFO because "they're optional." An optional field in the manifest schema is optional as input; once present, it becomes an input that downstream steps consume. Formspree being AMBIGUOUS is not optional to Step 2 — it's a gap with a concrete contract consequence.
- **Separation from resolution** — same as Subtask 1. Classifying Formspree as WARNING and simultaneously proposing "we'll use Formspree as the default" conflates classification with drafting.


### Examples of Excellence

Formspree classified as WARNING with the specific impact: *"Step 2 environment contract section `services.name`, `services.type`, and `services.integration` cannot be completed without a confirmed provider. These fields are REQUIRED in the services section when the tech stack references a third-party form handler. Downstream impact: if left as WARNING, the environment contract will have an open services section. This will carry forward to Step 3 (role configuration) where the integration scope of work cannot be defined."*

### Examples of Poor Performance

- Classifying Formspree as INFO because "it's just a form tool." The agent knows enough about the stack to know this is a concrete integration with real environment implications — downgrading it to INFO trades accuracy for brevity.
- Treating the `referenceexamples` field as fully PRESENT without noting that the quality descriptors (typography, whitespace) exceed the field's schema definition and are captured only in the non-mappable list. If those descriptors aren't carried forward, they silently disappear. Flagging this as INFO — *"design intent descriptors present but exceed reference example field schema; captured in non-mappable list; not carried into manifest"* — protects that signal.


### Uncovered Questions / Gaps

**The classification test for optional fields applies the same downstream impact question as for required fields, but with no "schema completeness" safety net.** For required fields, a REQUIRED field that can't be populated is BLOCKER regardless of downstream use. For optional fields, there is no equivalent floor. An optional field that is legally absent in the manifest but whose absence creates a known WARNING is handled correctly by the taxonomy — but there's no check for optional fields that become de facto required once the tech stack is known. In this project, `services` is an optional section *in general* but becomes conditionally required when the brief explicitly references a third-party form handler. The policy should state that conditional requirements surfaced by the tech stack declaration elevate optional fields to WARNING automatically.

### Opportunities to Improve the Step 1 Policy / FC-2

- Add a rule: when a tech stack declaration implies an optional section (services, performance targets, etc.), that section's fields are reclassified as WARNING-or-higher for this project. The manifest template should include this conditional logic as a lookup table.


### Risks

- **Formspree ambiguity lost:** If classified as INFO and not flagged at the human gate, Step 2 produces an incomplete environment contract without any signal that the services section is outstanding. The issue surfaces at Step 3 or later — by which point multiple downstream documents are affected.
- **Non-mappable items not entering the register:** Task 1.2 classifies fields that Task 1.1 mapped. Items in the non-mappable list (infrastructure readiness, maintainability requirement, design intent descriptors) have no field to classify against — so they risk falling through the gap between Subtask 2 (optional fields) and Subtask 3 (contradictions) without entering the open questions register.[^3_1]

***

## Subtask 3 — Classify Each Contradiction as BLOCKER

### What Is Happening

Every contradiction surfaced in Task 1.1 Subtask 5 (Contradiction Review) is unconditionally classified as BLOCKER.  The policy is explicit: *"contradictions are never downgraded."* This subtask is a mechanical application of that rule — there is no classification decision to make, only a confirmation that each contradiction has a BLOCKER entry in the output gap list.[^3_1]

Applied to the case study:


| Contradiction | BLOCKER entry |
| :-- | :-- |
| "Deploy to Cloudflare Workers" conflicts with "fully static — no server-side rendering" | **BLOCKER** — `deploymenttarget` and `constraints[static]`. Impact: entire Step 2 deployment section depends on resolution; the AstroJS output mode (`static` vs `server`) is determined by this. |

### Skills Required to Do This to a High Standard

- **No-downgrade discipline** — the most important skill in this subtask is resistance to the impulse to reason a contradiction into a non-problem. Technical knowledge creates pressure to resolve contradictions silently; the framework's invariant exists precisely to resist that pressure.[^3_1]
- **Impact specificity** — even though the BLOCKER classification is automatic, the impact statement must be specific. A contradiction that affects two fields in two different steps needs an impact statement that names both.
- **Linkage to the related required field entry** — the Workers/static contradiction is also reflected in the `deploymenttarget` BLOCKER entry from Subtask 1. The open questions register should link these two entries so that Task 1.3 handles them in a single clarification exchange rather than producing two separate questions about the same underlying issue.


### Examples of Excellence

Creating a BLOCKER entry for the contradiction that explicitly references both affected fields (`deploymenttarget` and `constraints`), names the two competing interpretations without choosing between them (*"Cloudflare Workers (edge compute, requires `@astrojs/cloudflare` adapter in `server` or `hybrid` mode) vs. Cloudflare Pages (static hosting, compatible with `output: static`)"*), and links to the `deploymenttarget` BLOCKER entry from Subtask 1 with a note: *"Resolve these two BLOCKER entries with a single clarification question."*

### Examples of Poor Performance

- Creating a BLOCKER entry but writing the impact as: *"Contradiction between deployment target and static constraint — needs clarification."* This tells Task 1.3 that clarification is needed but not what the clarification must determine. Task 1.3 cannot formulate a precise question from a vague impact statement.
- Failing to link the contradiction BLOCKER to the related `deploymenttarget` BLOCKER — leading to Task 1.3 asking two separate questions that the human experiences as the same question asked twice.


### Uncovered Questions / Gaps

**The policy gives no guidance on contradictions between fields that span different manifest sections.** The Workers/static contradiction involves `deploymenttarget` (a required field) and an item in `constraints` (an optional field). It is clear these conflict, but the policy's contradiction-as-BLOCKER rule doesn't address whether the BLOCKER is assigned to the required field, the optional field, or both. In this case, `deploymenttarget` is the load-bearing field — Step 2 cannot proceed without a resolved deployment target. The `constraints[static]` entry, being optional, would normally not be a BLOCKER on its own. The contradiction elevates it. This interaction between field type and contradiction classification should be formalised.

**No guidance on how to handle contradictions that are only potential — requiring domain expertise to confirm.** Surfaced in the Task 1.1 analysis: the Workers/static case requires technical knowledge to identify as a contradiction. The policy assumes the classifier has this knowledge. For contradictions where the classifier is uncertain, there is no "potential contradiction" status — only BLOCKER or not.[^3_1]

### Opportunities to Improve the Step 1 Policy

- Add a rule for linking related BLOCKER entries: when a contradiction involves the same field as an existing BLOCKER from Subtask 1, the contradiction entry must reference the Subtask 1 entry and Task 1.3 must consolidate them into a single clarification question.
- Add a `POTENTIAL-CONTRADICTION` classification for cases where technical domain knowledge is required to confirm a contradiction. This is classified as WARNING (not BLOCKER) until confirmed — but it is presented to the human alongside BLOCKER items with a note that it requires technical confirmation.


### Risks

- **Duplicate clarification questions:** Without linkage between the `deploymenttarget` BLOCKER (Subtask 1) and the Workers/static BLOCKER (Subtask 3), Task 1.3 asks Alex: *"Which Cloudflare product are you targeting?"* and separately: *"You stated the site must be fully static — do you mean no server-side rendering at all?"* These are the same question and the human recognises them as such. This damages trust in the process and produces a partial answer to each question instead of a complete answer to one.[^3_1]
- **Technical contradictions passing through undetected:** If the classifier lacks the technical knowledge to identify the Workers/Pages distinction, the contradiction never enters the register. Step 2 then receives a manifest with `deploymenttarget: "Cloudflare Workers"` and `constraints: ["fully static"]` and must independently detect and handle the conflict — with no record of it having been identified. This is a broader risk of Task 1.1 Subtask 5, but it manifests in Task 1.2 as a silent classification gap.

***

## Cross-Cutting Observations for Task 1.2

### The Open Questions Register Is Born Here

Task 1.2 is the step that creates the FC-8 open questions register.  This is not stated in the Task 1.2 description — the policy says Task 1.2 produces "a two-tier gap list" but doesn't name it as the register's creation point. The policy should be explicit: Task 1.2's output IS the initial population of the open questions register, filed at `.framework/open-questions-register.md`. The "gap list" is not a separate intermediate document; it is the register.[^3_1]

### The Non-Mappable List Has No Classification Path

Task 1.2's three subtasks cover required fields, optional fields, and contradictions. Non-mappable statements (from Task 1.1 Subtask 4) have no classification subtask. They fall through. This should be addressed by adding a fourth subtask to Task 1.2:

**Proposed Subtask 4:** *For each non-mappable statement, determine: (a) does it represent information that belongs in the manifest but has no current schema field? If yes, create a WARNING entry with a schema gap note. (b) Does it represent operational information with downstream consequences? If yes, create a WARNING or INFO entry referencing the relevant downstream step.*

This ensures that statements like "Cloudflare account is set up and DNS control is available" enter the register and eventually reach Step 2's environment contract rather than disappearing.

### The Classification Test Requires Step 2 and Step 3 Knowledge

The FC-2 classification test asks whether a gap causes a *subsequent step* to fail.  Applying this test correctly requires the Task 1.2 executor to know what Steps 2 and 3 need. This is a knowledge dependency that should be explicit in the policy — either as a required input (Step 2 and Step 3 policy documents as reference) or as a skill file entry that the executing agent loads. Without this knowledge, the executor is guessing, not classifying.[^3_1]

<div align="center">⁂</div>

[^3_1]: i-am-making-progress-in-creati-fuGLU8hCRLyka3xtBTVglA.md


---

# ok. I just realised I was mixed up in the last couple of chats.

Let's revisit the entirety of Task 1.1 as I want to question the outputs for all subtasks.

When you suggested that the skills required for reading the brief were different than decomposing, it started my mind thinking that each subtask would be done by a new agent. And perhaps it will end up being that way.  That's why I noticed the lack of concrete output for subtask 1.

Now that I look at the other subtasks, I'm wondering if any of their outputs are meaningful.

Perhaps the decomposing of the prose is the output of Task 1.1 and the subtasks are parts of that categorization, sorting, highlighting etc

Then the following tasks can use that output as their input.

If I ask questions or make statements that you are unsure about, please question me. I make mistakes, I don't know everything and I'm ok with being wrong.

Your instinct is right, and it's worth working through carefully because the output structure of Task 1.1 determines the input structure for every subsequent task.

## The Core Design Question

The current structure has five subtasks each producing a separate intermediate artefact. But none of those intermediate artefacts are meaningful on their own — they only become useful when considered together. Task 1.2 doesn't need a "required field inventory" and a "contradiction list" as separate documents. It needs to know, *for each gap, what statements from the brief are relevant to it*. That question can only be answered by a document that holds both the statements AND their field associations AND their contradiction links simultaneously.

The user's reframe is correct: **the subtasks are operations that build a single output document, not separate documents.**

## Proposed: The Brief Inventory Document

Task 1.1's output is a single document — the **Brief Inventory** — with four sections. Each section corresponds to one subtask. The document is produced as a whole and handed to Task 1.2 in full.

```
brief-inventory.md
│
├── Section 1: Statement List
│   Each discrete statement extracted from the brief
│   Per statement: ID, text, source location, clarity, candidate field(s)
│
├── Section 2: Field Coverage
│   Each schema field (required and optional)
│   Per field: coverage status (PRESENT / ABSENT / AMBIGUOUS), supporting statement IDs
│
├── Section 3: Non-Mappable Statements
│   Statements with no schema field association
│   Per entry: statement ID, text, downstream relevance note
│
└── Section 4: Contradictions
    Conflicting statement pairs
    Per entry: statement IDs, description, affected field(s)
```

The subtasks map directly to sections:


| Subtask | Produces section | Dependencies |
| :-- | :-- | :-- |
| 1 — Statement Decomposition | Section 1 | Raw brief |
| 2 — Field Coverage Analysis | Section 2 | Section 1 |
| 3 — Non-Mappable Identification | Section 3 | Section 1 |
| 4 — Contradiction Review | Section 4 | Section 1 |

Sections 2, 3, and 4 are all derived from Section 1. They are essentially different queries over the same statement list, formatted for human navigability and Task 1.2 consumption.

## On the Multi-Agent Question

You're right to notice the question — and I want to flag a concern before it becomes an assumption.

Task 1.1 is an analytical task that requires holistic comprehension of a short document. The contradiction detection in Subtask 4 only works reliably if the classifier has the entire brief in view — a contradiction between a statement in paragraph 2 and a constraint in paragraph 7 is only visible to an agent that processed both. Distributing across multiple agents creates handoff risk: each agent loads the brief fresh, and the coherence of the whole depends on their intermediate outputs being exactly right before the next agent begins.

The counter-argument — that each subtask requires different skills and could benefit from specialisation — is real but weaker at this scale. The brief in our case study is a single short document. The "skills" for decomposition (precise parsing) and field mapping (schema knowledge) are not so different that specialisation outweighs the cost of coordination overhead and handoff risk.

**My position:** Task 1.1 is best executed by a single agent producing one artefact. The subtasks are sequential operations within that agent's execution cycle, not separate agent invocations.

This is also more consistent with the framework's write-authority model: one agent holds write authority over one artefact — `brief-inventory.md`. No handoffs, no merge conflicts, no partial-document states.

If you have a different view on this, I'd want to understand what's driving it — because it's a design decision that affects the agent roster for Step 1. Push back if I'm wrong.

## Revised Task 1.1 Structure

**Task 1.1 — Brief Inventory**

- *Question:* What is in the brief, and how does it map to the manifest schema?
- *Input:* Raw project brief, manifest schema
- *Output:* `brief-inventory.md` — a single structured document with four sections
- *Subtasks:*

1. **Statement Decomposition** — parse the brief into discrete, atomic declarative statements; tag each with source location, clarity rating (CLEAR / AMBIGUOUS), and candidate field associations
2. **Field Coverage Analysis** — for each required and optional schema field, identify which statements support it; classify coverage as PRESENT, ABSENT, or AMBIGUOUS
3. **Non-Mappable Identification** — identify statements with no schema field association; note any downstream relevance
4. **Contradiction Review** — identify statement pairs that conflict; record the affected fields
- *Done when:* All four sections are complete, every statement from the brief appears in at least one section, every schema field appears in Section 2, and no statement is silently discarded


## What This Changes for Task 1.2

Task 1.2 now receives `brief-inventory.md` as its sole input. It reads Section 2 (Field Coverage) for gap classification, Section 3 (Non-Mappable) for the new proposed Subtask 4, and Section 4 (Contradictions) for the automatic BLOCKER classification. The question of whether these sections need to be separate documents disappears.

***

One question back to you: the Section 2 field coverage view and the Section 1 statement list are two representations of the same data. A machine agent querying `brief-inventory.md` might find a flat statement list with field properties more efficient than a section-based document. A human reviewing it would find the section-based layout more navigable. Which matters more for this document — or do we need both?

---

# i understand better now.

prioritise agent efficiency for the brief-inventory. if we decide later that a human needs to read this at this point, we will revisit.

Good. Prioritising agent efficiency resolves the format question cleanly.

## What Agent Efficiency Requires

An agent consuming `brief-inventory.md` in Task 1.2 needs to make specific lookups:

- *"Give me all fields with ABSENT or AMBIGUOUS coverage"*
- *"Which statements support field X?"*
- *"Are there any contradictions involving field X?"*
- *"Are there non-mappable statements with downstream consequences?"*

A section-based human-readable layout requires the agent to parse prose structure to answer these. A flat, normalised, ID-referenced structure answers them directly.

## Revised Output Format

The document becomes a structured YAML file. Four flat arrays. Cross-references use IDs — no data duplication.

```yaml
# brief-inventory.yaml
# Produced by: Task 1.1 | Input to: Task 1.2

statements:
  - id: S-01
    text: "I need a single-page marketing website for my consulting practice, Meridian Consulting."
    clarity: CLEAR
    candidate_fields: [projectname, description]

  - id: S-02
    text: "Deploy to Cloudflare Workers on my domain."
    clarity: AMBIGUOUS
    candidate_fields: [deploymenttarget]

  - id: S-03
    text: "The site must be fully static — no server-side rendering."
    clarity: CLEAR
    candidate_fields: [constraints]

  - id: S-04
    text: "I want to build this with AstroJS using Shadcn components for the UI."
    clarity: AMBIGUOUS          # named but unversioned
    candidate_fields: [techstack]

  # ... all statements from the brief

fields:
  - field: projectname
    required: true
    coverage: PRESENT
    supporting_statements: [S-01]

  - field: techstack
    required: true
    coverage: AMBIGUOUS         # named, unversioned; React integration implicit
    supporting_statements: [S-04, S-05]

  - field: deploymenttarget
    required: true
    coverage: AMBIGUOUS
    supporting_statements: [S-02]

  - field: devenvironment
    required: true
    coverage: AMBIGUOUS         # OS and editor present; runtime version unknown
    supporting_statements: [S-10, S-11, S-12]

  - field: appetite
    required: true
    coverage: AMBIGUOUS         # "within a week" present but not valid enum value
    supporting_statements: [S-15]

  - field: integrationrequirements
    required: false
    coverage: AMBIGUOUS         # Formspree mentioned tentatively
    supporting_statements: [S-08]

  - field: existingassets
    required: false
    coverage: ABSENT
    supporting_statements: []

  # ... all schema fields

non_mappable:
  - statement_id: S-13
    downstream_note: "Cloudflare account active, DNS control available — relevant to Step 2 deployment section"

  - statement_id: S-16
    downstream_note: "Maintainability for handoff — no schema field; candidate constraint entry"

  - statement_id: S-17
    downstream_note: "Design intent descriptors (typography, whitespace) attached to reference examples — exceed field schema"

contradictions:
  - id: C-01
    statement_ids: [S-02, S-03]
    description: "Cloudflare Workers implies edge compute adapter (incompatible with static output mode); static constraint requires output:static"
    affected_fields: [deploymenttarget, constraints]
```


## What This Changes

**The document is now a `.yaml` file, not `.md`.** The framework's other artefacts are `.md` but those are human-authored or human-reviewed documents. `brief-inventory` is an intermediate working document — produced by an agent, consumed by an agent, never presented to the human director. `.yaml` is the right format. This is a file-type precedent worth noting: artefacts with a human gate use `.md`; agent-to-agent intermediate artefacts may use `.yaml`.

**The subtask execution model is clean.** One agent, four sequential operations, one write action at the end. The agent builds the four arrays in memory and writes the complete document once. No partial writes, no intermediate files.

**Task 1.2's job is now a direct query over this structure** — no parsing, no inference. It reads `fields` for gap classification, `non_mappable` for the proposed Subtask 4, and `contradictions` for automatic BLOCKER assignment.

***

Task 1.1 is now stable. Ready to proceed to Task 1.2 with the revised structure?

---

# Task 1.2 — Gap Classification: Full Subtask Analysis

**Task 1.2's question:** Which gaps are blocking and which can be surfaced as open questions?[^6_1]

**Input:** `brief-inventory.yaml` from Task 1.1
**Output:** `open-questions-register.yaml` — initial population, created here, persisting through all six bootstrap steps per FC-8[^6_1]

*Standing instruction: read the complete input before producing any output.*

***

## Revised Subtask Structure

The policy's original three subtasks covered required fields, optional fields, and contradictions. Our Task 1.1 analysis surfaced a fourth category — non-mappable statements — that has no classification path in the original policy. Revised structure:


| \# | Subtask | Source array in `brief-inventory.yaml` |
| :-- | :-- | :-- |
| 1 | Classify ABSENT/AMBIGUOUS required fields | `fields` where `required: true` and `coverage` is not PRESENT |
| 2 | Classify ABSENT/AMBIGUOUS optional fields | `fields` where `required: false` and `coverage` is not PRESENT |
| 3 | Classify contradictions | `contradictions` |
| 4 | Classify non-mappable statements | `non_mappable` |


***

## Subtask 1 — Classify ABSENT/AMBIGUOUS Required Fields

### What Is Happening

Each required field with coverage ABSENT or AMBIGUOUS is passed through the FC-2 classification test.  The test has three gates, applied in order:[^6_1]

> **Gate 1:** Would proceeding without this information, or getting it wrong, cause a subsequent step to fail or produce a materially incorrect output?
> - YES → **BLOCKER**
>
> **Gate 2:** Does the absence have a known, specific impact on the quality of any downstream output?
> - YES → **WARNING**
> - NO → **INFO**
>
> **Gate 3 (addition from Task 1.1 analysis):** Is this a REQUIRED schema field that cannot be validly populated from the current brief?
> - YES → **BLOCKER** regardless of Gates 1 and 2

Gate 3 is the new addition. Without it, `appetite` (REQUIRED, enum-constrained, no valid value in brief) would pass Gates 1 and 2 as non-BLOCKER — because Step 2 doesn't consume `appetite` directly. But a manifest with an empty REQUIRED field fails DoD 3. Gate 3 catches this.[^6_1]

Applied to the case study required fields with non-PRESENT coverage:


| Field | Coverage | Gate reached | Classification | Impact statement |
| :-- | :-- | :-- | :-- | :-- |
| `techstack` — AstroJS version | AMBIGUOUS | Gate 1 YES | **BLOCKER** | Step 2 `framework.version` cannot be completed; populating from assumed current-stable is an FC-1 violation |
| `techstack` — React integration implicit | AMBIGUOUS | Gate 1 YES | **BLOCKER** | Step 2 install commands and config entries cannot be written for an undeclared dependency |
| `techstack` — package manager ambiguous | AMBIGUOUS | Gate 1 YES | **BLOCKER** | Step 2 `runtime.packagemanager` and `runtime.installcommand` require a single confirmed value |
| `deploymenttarget` — Workers vs Pages | AMBIGUOUS | Gate 1 YES | **BLOCKER** | Step 2 deployment section structure differs entirely between Workers and Pages; AstroJS output mode depends on resolution |
| `devenvironment.runtime.version` | AMBIGUOUS | Gate 1 YES | **BLOCKER** | Step 2 `runtime.version` requires an exact or minimum version; human stated they don't know |
| `appetite` — informal value | AMBIGUOUS | Gate 3 YES | **BLOCKER** | REQUIRED field; "within a week" is not a valid enum value; manifest fails DoD 3 without a valid entry |

Each becomes a separate entry in the register — not grouped by theme. Six BLOCKER entries from this subtask alone.

### Skills Required to Do This to a High Standard

- **Step 2 schema knowledge as a prerequisite** — Gate 1 cannot be applied without knowing what Step 2 needs, field by field. This is the most critical competency in this subtask and is not provided by the brief or the manifest schema alone. It must be loaded from an external reference — the Step 2 policy or an agent skill file. Without it, Gate 1 becomes guesswork.
- **One gap, one entry discipline** — `techstack` has three distinct gaps (version, React integration, package manager). Each has a different field association, a different impact statement, and will produce a different clarification question in Task 1.3. Collapsing them into one entry degrades every downstream task.
- **Gate 3 awareness** — recognising that REQUIRED field validity is an independent classification criterion, not covered by the downstream-failure test. An agent that only applies Gates 1 and 2 will miss the `appetite` case.
- **No resolution during classification** — the most common failure mode. Classifying `techstack` versions as BLOCKER and simultaneously noting "AstroJS latest stable is 5.x" is two acts. Only the classification belongs here.


### Examples of Excellence

Six separate register entries produced. Each has a specific `gap` (one sentence, one field, one missing piece), a specific `impact` (names the Step 2 field or DoD criterion that fails), and a source reference to the relevant statement ID(s) from `brief-inventory.yaml`. The `appetite` entry explicitly invokes Gate 3 in its impact statement so the reviewer can see why a field with no downstream step dependency is still BLOCKER.

### Examples of Poor Performance

- One entry for `techstack` reading: *"Technology stack is ambiguous — versions and configuration not fully specified."* This produces one clarification question in Task 1.3 that asks for everything at once. The human provides a paragraph-length answer. Task 1.4 (Manifest Drafting) then has to decompose that answer back into individual field values, re-establishing the structure that should have been created here.
- Classifying `appetite` as non-BLOCKER because "Step 2 doesn't use appetite" — Gate 3 not applied.
- Classifying `devenvironment.runtime.version` as WARNING because "the human can check later." The human stated they don't know the version. This is likely a `CONFIRMED-UNKNOWN` outcome from Task 1.3, but it must be attempted as BLOCKER first — the classification is not informed by the expected outcome of clarification.


### Uncovered Questions / Gaps

**Gate 1 requires knowledge this subtask's policy doesn't supply.** The test asks whether a gap causes "a subsequent step to fail." The executor needs to know Steps 2 and 3's requirements to answer this. The policy describes Task 1.2 as if this knowledge is implicit. It isn't. The Step 1 agent's context card or skill file must explicitly include the downstream step requirements as loaded reference material, and the policy should state this.[^6_1]

**The AMBIGUOUS coverage status conflates two different gap types.** `techstack` versions are AMBIGUOUS because information is present but incomplete. `appetite` is AMBIGUOUS because information is present but in the wrong format. These require different question forms in Task 1.3: version gaps need *"what version?"* and format gaps need *"you said X — which of these valid values best matches?"* The policy doesn't distinguish them, but the open questions register should.

### Opportunities to Improve the Policy

- Add Gate 3 to the FC-2 classification rule in the cross-cutting policies.
- Add a `gap_type` field to the register: `ABSENT` (no information), `AMBIGUOUS-INCOMPLETE` (partial information), `AMBIGUOUS-FORMAT` (information present, wrong form). This shapes the question formulation in Task 1.3 without requiring Task 1.3 to re-derive the gap type.
- Make the downstream step knowledge dependency explicit in the policy: *"Applying Gate 1 requires the executor to have loaded the Step 2 and Step 3 policy documents as reference material."*


### Risks

- **Under-classification of `appetite`:** If Gate 3 is not applied, `appetite` produces no BLOCKER entry. Task 1.3 is never triggered for it. Task 1.4 populates the field by inference. The manifest fails DoD 5 (no invented values).[^6_1]
- **Gate 1 guessing:** An agent without Step 2 knowledge applies Gate 1 based on intuition. Some BLOCKERs are downgraded to WARNING. Step 2 then receives a manifest with unresolved gaps that were never flagged as blocking, producing either FC-1 violations or an incomplete environment contract.

***

## Subtask 2 — Classify ABSENT/AMBIGUOUS Optional Fields

### What Is Happening

Optional fields with non-PRESENT coverage are passed through Gates 2 and 3 only — Gate 1 is not applicable because optional fields are legally absent from the manifest.  The practical consequence: optional fields can only be WARNING or INFO, never BLOCKER. The exception is the **conditional requirement rule** surfaced in Task 1.1: when the tech stack declaration implies an optional section, that section's fields become WARNING automatically, regardless of the Gate 2 test result.[^6_1]

Applied to the case study:


| Field | Coverage | Conditional? | Classification | Impact |
| :-- | :-- | :-- | :-- | :-- |
| `integrationrequirements` — Formspree tentative | AMBIGUOUS | YES — form handler referenced in brief | **WARNING** | Step 2 `services` section conditionally required when a third-party form handler is referenced; leaving unconfirmed produces an incomplete contract section |
| `existingassets` | ABSENT | NO | **INFO** | No downstream step requires existing assets in bootstrap; noted for completeness |
| `referenceexamples` descriptors | PRESENT (field) + non-mappable (descriptors) | NO | Handled in Subtask 4 | Design intent descriptors overflow schema; main field is PRESENT |

### Skills Required to Do This to a High Standard

- **Conditional requirement detection** — recognising when an optional field becomes functionally required given the specific tech stack. This requires knowing which manifest sections have conditional trigger rules (services section is triggered by third-party integrations, performance targets section is triggered by measurable performance constraints). These triggers should be enumerated in the manifest template's metadata, not left to the executor's judgment.
- **INFO ≠ ignorable** — INFO entries still enter the open questions register. They travel through all subsequent steps. They are presented to the human director at Step 6. The discipline is: INFO gaps are documented with the same rigour as BLOCKER gaps; they just don't trigger the clarification protocol.


### Examples of Excellence

The `integrationrequirements` entry clearly invokes the conditional requirement rule: *"Tech stack references a third-party form handler (brief statement S-08). This triggers the services section in the Step 2 environment contract. Provider name and integration method are REQUIRED within that section once it is triggered. Classification: WARNING — step proceeds, but Step 2 will have an incomplete services section unless this is resolved."*

### Examples of Poor Performance

Classifying Formspree as INFO because "it's not a required field." This is the conditional requirement blind spot — a field that is optional in general but mandatory given the specific brief context.

### Uncovered Questions / Gaps

**The conditional requirement triggers are not documented in the manifest template.** The executor has to know, from domain knowledge, that a referenced form handler triggers the services section. This belongs as metadata in the manifest template itself — a lookup table: *if `techstack` contains a form handler reference → `services` section required; if `constraints` contains a measurable performance target → `performance_targets` section required.* Without this, the conditional rule is applied inconsistently.[^6_1]

### Opportunities to Improve the Policy

- Add a **conditional sections table** to the manifest template schema: tech stack patterns that trigger optional sections. This makes Subtask 2 a table lookup rather than a judgment call, and makes the results reproducible.


### Risks

- **Formspree ambiguity reaching Step 2 unclassified:** If not entered as WARNING here, Step 2 has no signal that the services section is expected. The contract is produced without it. This is a silent quality degradation that doesn't surface until someone tries to implement the contact form and discovers the integration was never specced.

***

## Subtask 3 — Classify Contradictions

### What Is Happening

Every entry in the `contradictions` array of `brief-inventory.yaml` receives an automatic BLOCKER classification. No test is applied — contradictions are never downgraded.[^6_1]

This subtask has one additional operation beyond simple classification: **deduplication linking**. The Workers/static contradiction (C-01) involves `deploymenttarget` — the same field that already has a BLOCKER entry from Subtask 1. These two entries must be linked in the register so that Task 1.3 consolidates them into a single clarification question rather than asking about the same underlying issue twice.

```yaml
# Register entries after Subtask 3:

- questionid: OQ-1-05
  field: deploymenttarget
  gap: "Contradiction: 'Cloudflare Workers' conflicts with 'fully static — no server-side rendering'"
  impact: "AstroJS output mode and adapter selection depend entirely on resolution; Step 2 deployment section cannot be written until resolved"
  source_statements: [S-02, S-03]
  contradiction_ref: C-01
  classification: BLOCKER
  linked_questions: [OQ-1-04]  # links to the deploymenttarget BLOCKER from Subtask 1
  raisedbystep: 1
  currentowner: 1
  resolutionstatus: OPEN
```

The `linked_questions` field signals to Task 1.3: *"These two entries are related — ask one question, not two."*

### Skills Required to Do This to a High Standard

- **No-downgrade discipline** — resisting the urge to apply technical knowledge to resolve contradictions internally. The agent may know that Cloudflare Pages is the correct interpretation. That knowledge must not influence the classification or the register entry.[^6_1]
- **Deduplication detection** — cross-referencing the `affected_fields` in each contradiction entry against the entries already created in Subtasks 1 and 2. If any affected field already has a register entry, the linking relationship must be recorded.
- **Two-interpretation impact statements** — the impact statement for a contradiction BLOCKER must describe both competing interpretations and what each implies downstream, without choosing between them.


### Examples of Excellence

The register entry for C-01 names both interpretations: *"If Cloudflare Workers: requires `@astrojs/cloudflare` adapter, AstroJS output mode `server` or `hybrid`, edge function capability active — incompatible with static constraint. If Cloudflare Pages: AstroJS output mode `static`, no adapter required, contact form must use external handler only — consistent with static constraint."* Task 1.3 can translate this directly into a precise question.

### Examples of Poor Performance

- A contradiction entry with impact: *"Deployment target unclear — needs clarification."* Task 1.3 cannot formulate a useful question from this. It will ask something vague like *"Can you clarify your deployment preference?"* — which produces a vague answer.
- Not detecting that C-01 and the `deploymenttarget` BLOCKER from Subtask 1 are related. Task 1.3 asks two separate questions. The human responds to the first, Task 1.3 records it, then asks the second — which the human has already answered. This is a trust-damaging process failure.


### Uncovered Questions / Gaps

**`POTENTIAL-CONTRADICTION` status is still unresolved.** Our Task 1.1 analysis proposed a `POTENTIAL-CONTRADICTION` classification for technical contradictions that require domain expertise to confirm. The policy as written gives no path for this. The current design forces a binary: either it's a contradiction (BLOCKER) or it isn't (no entry). The correct approach for domain-knowledge-dependent contradictions is to classify them as **WARNING with a `contradiction_flag: true` annotation** — they enter the register, are presented at the human gate, but don't block drafting. This preserves the signal without over-blocking. This should be raised as an addition to FC-2.

### Opportunities to Improve the Policy

- Add `linked_questions` as a formal register field — not just noted in the entry text but a machine-readable array that Task 1.3 can directly query to detect consolidation opportunities.
- Add `POTENTIAL-CONTRADICTION` as a WARNING-level flag to FC-2, with the rule: *"Contradictions that can only be confirmed with domain expertise are classified as WARNING with `contradiction_flag: true`. They are escalated to BLOCKER if confirmed during clarification."*


### Risks

- **Duplicate questions in Task 1.3:** Without `linked_questions`, Task 1.3 treats every BLOCKER entry as independent. For this brief, that produces two questions about the deployment target. The human answers one. Task 1.3 records a partial answer. The second question is asked and the human reasonably pushes back on the process quality.

***

## Subtask 4 — Classify Non-Mappable Statements

### What Is Happening

This subtask is new — not present in the current Step 1 policy. Every entry in the `non_mappable` array of `brief-inventory.yaml` is assessed for downstream consequence and classified. The classification test is simpler than for fields:

> Does this statement represent information with a downstream consequence in Steps 2–6?
> - YES, consequence is specific and named → **WARNING**
> - YES, consequence is plausible but indirect → **INFO**
> - NO → **INFO** (noted for completeness; no register entry required unless it represents a schema gap)

Applied to the case study non-mappable statements:


| Statement | Text | Classification | Reason |
| :-- | :-- | :-- | :-- |
| S-13 | "Cloudflare account active, DNS control available" | **WARNING** | Step 2 deployment section has a field for deployment infrastructure readiness. Without this recorded, Step 2 cannot confirm DNS configuration is self-managed — it may assume procurement is needed. Specific downstream consequence. |
| S-16 | "Handoff to a developer friend later" | **INFO** | No Step 2–6 schema field captures maintainability requirements. Downstream consequence is plausible (code quality standards) but too indirect to specify. Noted; candidate for a future `constraints` entry or schema addition. |
| S-17 | Design intent descriptors (typography, whitespace) | **INFO** | No manifest field captures design intent. Step 4 (Pattern Seeding) would benefit but the connection is indirect. Noted for completeness. |

### Skills Required to Do This to a High Standard

- **Schema gap recognition** — distinguishing between *"this information has no schema field"* (a schema gap, potentially requiring a future field addition) and *"this information doesn't belong in the schema"* (genuinely out of scope for the manifest). S-13 (infrastructure readiness) is a schema gap. S-17 (typography descriptors) is not — it belongs in a design brief, not a project manifest.
- **Downstream step awareness** — same as Subtask 1, this requires knowing what Steps 2–6 need. S-13 is only classifiable as WARNING if the executor knows Step 2 includes an infrastructure readiness field.


### Examples of Excellence

Classifying S-13 as WARNING with: *"No manifest field exists for existing infrastructure readiness. This information is relevant to Step 2's deployment section. Entering as WARNING to ensure it is reviewed at the human gate and manually considered when drafting the Step 2 contract. Schema gap: candidate field `existingInfrastructure`."* This produces a useful register entry AND a schema improvement signal.

### Examples of Poor Performance

Not performing this subtask at all — the most common failure mode when subtasks are not explicitly mandatory. All three non-mappable statements disappear from the process. S-13 reaches Step 2 unrecorded. The Step 2 executor either invents an assumption about DNS management or produces a contract with an unacknowledged gap.[^6_1]

### Opportunities to Improve the Policy

- Add Subtask 4 to the Task 1.2 policy definition explicitly — it is currently absent.
- Add a `schema_gap_flag: true` field to the register for WARNING entries that represent missing schema fields. This creates a feedback loop: schema gaps accumulate in the register across projects and inform manifest template evolution.

***

## Output: `open-questions-register.yaml`

Task 1.2 creates this file. It is not a summary or intermediate document — it IS the output. Applied to the case study, the initial register has nine entries:

```yaml
# open-questions-register.yaml
# Created: Step 1, Task 1.2
# Persists through: Steps 1–6

questions:

  - questionid: OQ-1-01
    field: techstack
    gap_type: AMBIGUOUS-INCOMPLETE
    gap: "AstroJS version not specified"
    impact: "Step 2 framework.version cannot be completed without a specific or minimum version"
    source_statements: [S-04]
    classification: BLOCKER
    raisedbystep: 1
    currentowner: 1
    resolutionstatus: OPEN

  - questionid: OQ-1-02
    field: techstack
    gap_type: AMBIGUOUS-INCOMPLETE
    gap: "React integration implied by Shadcn dependency but not explicitly declared as a stack element"
    impact: "Step 2 cannot enumerate all dependencies for install commands and config entries"
    source_statements: [S-04]
    classification: BLOCKER
    raisedbystep: 1
    currentowner: 1
    resolutionstatus: OPEN

  - questionid: OQ-1-03
    field: techstack
    gap_type: AMBIGUOUS-INCOMPLETE
    gap: "Package manager unconfirmed — npm stated as default, pnpm cited as acceptable alternative"
    impact: "Step 2 runtime.packagemanager and runtime.installcommand require a single confirmed value"
    source_statements: [S-09]
    classification: BLOCKER
    raisedbystep: 1
    currentowner: 1
    resolutionstatus: OPEN

  - questionid: OQ-1-04
    field: deploymenttarget
    gap_type: AMBIGUOUS-INCOMPLETE
    gap: "Cloudflare Workers named but technical target may be Cloudflare Pages given static constraint"
    impact: "Step 2 deployment section structure differs entirely between Workers and Pages"
    source_statements: [S-02]
    classification: BLOCKER
    linked_questions: [OQ-1-05]
    raisedbystep: 1
    currentowner: 1
    resolutionstatus: OPEN

  - questionid: OQ-1-05
    field: deploymenttarget
    gap_type: CONTRADICTION
    gap: "Cloudflare Workers implies edge compute adapter incompatible with AstroJS output:static; static constraint requires output:static"
    impact: "AstroJS output mode and adapter selection cannot be determined; entire Step 2 deployment and framework sections blocked"
    source_statements: [S-02, S-03]
    contradiction_ref: C-01
    classification: BLOCKER
    linked_questions: [OQ-1-04]
    raisedbystep: 1
    currentowner: 1
    resolutionstatus: OPEN

  - questionid: OQ-1-06
    field: devenvironment
    gap_type: AMBIGUOUS-INCOMPLETE
    gap: "Node.js runtime version unknown — human stated they do not know the exact version"
    impact: "Step 2 runtime.version requires an exact or minimum version; field cannot be completed"
    source_statements: [S-11]
    classification: BLOCKER
    raisedbystep: 1
    currentowner: 1
    resolutionstatus: OPEN

  - questionid: OQ-1-07
    field: appetite
    gap_type: AMBIGUOUS-FORMAT
    gap: "Appetite stated as 'within a week' — not a valid enum value (valid: small/medium/large)"
    impact: "REQUIRED field cannot be validly populated; manifest fails DoD 3"
    source_statements: [S-15]
    classification: BLOCKER
    raisedbystep: 1
    currentowner: 1
    resolutionstatus: OPEN

  - questionid: OQ-1-08
    field: integrationrequirements
    gap_type: AMBIGUOUS-INCOMPLETE
    gap: "Form handler provider tentative — Formspree mentioned but not confirmed"
    impact: "Step 2 services section conditionally required when form handler referenced; provider name and integration method cannot be specified"
    source_statements: [S-08]
    classification: WARNING
    raisedbystep: 1
    currentowner: 1
    resolutionstatus: OPEN

  - questionid: OQ-1-09
    field: null
    gap_type: SCHEMA-GAP
    gap: "Infrastructure readiness information present in brief but no manifest field exists"
    impact: "Step 2 deployment section may incorrectly assume DNS procurement is needed; self-managed DNS not formally recorded"
    source_statements: [S-13]
    classification: WARNING
    schema_gap_flag: true
    candidate_field: existingInfrastructure
    raisedbystep: 1
    currentowner: 1
    resolutionstatus: OPEN
```


***

## Done When

Task 1.2 is complete when:

1. Every `fields` entry in `brief-inventory.yaml` with coverage ABSENT or AMBIGUOUS has a corresponding register entry
2. Every `contradictions` entry has a BLOCKER register entry
3. Every `non_mappable` entry has been assessed and either has a register entry or has a documented reason for no entry
4. All BLOCKER entries involving the same field are linked via `linked_questions`
5. `open-questions-register.yaml` exists at the canonical path `.framework/open-questions-register.yaml`
6. All entries have `resolutionstatus: OPEN`

***

Ready to proceed to Task 1.3 (Clarification Resolution)?

<div align="center">⁂</div>

[^6_1]: i-am-making-progress-in-creati-fuGLU8hCRLyka3xtBTVglA.md


---

# Task 1.3 — Clarification Resolution: Full Subtask Analysis

**Task 1.3's question:** Can each BLOCKER gap be resolved by asking the human director directly?[^7_1]

**Conditional:** Runs only if BLOCKER entries exist in the open questions register. If Task 1.2 produces zero BLOCKERs (a complete, unambiguous brief), Task 1.3 is skipped and the process moves directly to Task 1.4.

**Input:** `open-questions-register.yaml` — specifically all entries with `classification: BLOCKER` and `resolutionstatus: OPEN`

**Outputs:**

- `clarification-exchange-CE-1-01.yaml` — the exchange record per FC-3[^7_1]
- Updated `open-questions-register.yaml` — each BLOCKER entry updated with resolution status and value

***

## Revised Subtask Structure

| \# | Subtask | Operation |
| :-- | :-- | :-- |
| 1 | Question Preparation | Query register for BLOCKERs; detect linked groups; formulate one question per independent gap or linked group |
| 2 | Exchange Conduct | Present questions to human director per FC-3 format; record exchange |
| 3 | Response Processing | Update each register entry with resolved value or CONFIRMED-UNKNOWN status |


***

## Subtask 1 — Question Preparation

### What Is Happening

The executor queries the register for all `classification: BLOCKER`, `resolutionstatus: OPEN` entries. Before formulating any question, it performs two operations:

**Step A — Linked group detection:** Any entries with `linked_questions` references are grouped. Linked entries share an underlying question; asking them separately would produce duplicate or contradictory questions. In our case study, OQ-1-04 and OQ-1-05 are linked — both concern the same `deploymenttarget` ambiguity from two angles (ambiguity and contradiction). They are consolidated into one question.

After consolidation, our seven BLOCKER entries collapse to six questions:


| Question | Register entries covered |
| :-- | :-- |
| Q1 — AstroJS version | OQ-1-01 |
| Q2 — React integration declaration | OQ-1-02 |
| Q3 — Package manager | OQ-1-03 |
| Q4 — Cloudflare Workers vs Pages *(consolidated)* | OQ-1-04 + OQ-1-05 |
| Q5 — Node.js version | OQ-1-06 |
| Q6 — Appetite enum value | OQ-1-07 |

**Step B — Question formulation:** Each question is formulated per FC-3 rules:[^7_1]

- One sentence, maximum 25 words
- Specific to a single field — not compound
- Named by field, not by domain
- Accompanied by a one-sentence impact statement

Questions grouped by domain for presentation:

```
Technical gaps (Questions 1–5):

Q1. Which version of AstroJS should this project use?
    Impact: Required before the environment contract can specify framework.version.

Q2. Should React be included as an explicit stack dependency for the Shadcn integration?
    Impact: Required to enumerate all install commands and config entries in the environment contract.

Q3. Which package manager should this project use — npm or pnpm?
    Impact: Required before install command entries can be written in the environment contract.

Q4. Are you deploying to Cloudflare Pages (static file hosting) or Cloudflare Workers (edge compute)?
    Impact: Determines the AstroJS output mode and adapter configuration; the entire deployment
    section of the environment contract depends on this.

Q5. What version of Node.js is installed in your development environment?
    Run `node --version` in your terminal to check.
    Impact: Required before the runtime section of the environment contract can be completed.

Scope gaps (Question 6):

Q6. Would you classify this project's appetite as small (days), medium (1–2 weeks), or large (multi-week)?
    Impact: The manifest requires one of these three values; freeform duration cannot be stored.
```


### Skills Required to Do This to a High Standard

- **Linked group detection** — reading `linked_questions` arrays and recognising when two separate register entries describe the same underlying question from different angles. Missing this produces duplicate questions that the human experiences as process failure.
- **Question scope discipline** — the FC-3 rule that each question is specific to a single field is hardest to apply when linked entries are consolidated. The consolidated Q4 covers `deploymenttarget` ambiguity AND a `deploymenttarget/constraints` contradiction. The question must remain one sentence addressing one field, even though two register entries are behind it.[^7_1]
- **Distinguishing resolution from decision** — FC-3 is explicit: the clarification protocol resolves *missing declared information*, not *undecided information*.  Q4 asks which Cloudflare product the human wants — if Alex has not decided, the answer is not a resolved value; it is a decision that must be made. These are different situations with different process paths, and the question formulation must not conflate them.[^7_1]
- **Impact statement precision** — the impact statement is not a threat or a justification; it is a single sentence naming the specific downstream field or DoD criterion that is blocked. Vague impact statements (*"needed for the next step"*) produce vague answers.


### Examples of Excellence

Q5 includes the specific terminal command `node --version`. This is not asking Alex to make a decision — it is providing the means to retrieve a specific fact. This is within FC-3's scope (resolving missing declared information) and eliminates a likely `CONFIRMED-UNKNOWN` outcome. The question is still one sentence with a verification method, not a compound instruction.

Q4 names the two options with brief parenthetical descriptions. This is not offering design choices — it is naming the two specific Cloudflare products so Alex can confirm which one they meant when they wrote "Cloudflare Workers." This is disambiguation, not decision-making.

### Examples of Poor Performance

- Formulating Q4 as: *"Can you clarify your deployment target and whether you need server-side rendering?"* — This is two questions in one sentence. FC-3 prohibits compound questions.  It also conflates the product question with the static/SSR question, making the answer harder to process in Subtask 3.[^7_1]
- Formulating Q2 as: *"Do you want to use React?"* — This sounds like a design preference question. FC-3 prohibits preference-gathering.  The correct framing establishes that React is *implied* by the brief and asks for explicit confirmation — it is resolving an implicit declaration, not soliciting a new decision.[^7_1]
- Formulating Q6 as: *"You said 'within a week' — does that mean small?"* — This is a leading question that proposes an answer. The human will say yes. If "within a week" is actually at the boundary between small and medium in their mind, the manifest captures the wrong value.


### Uncovered Questions / Gaps

**Q5 includes an instruction (`run node --version`) alongside a question.** FC-3's question formulation rules require *one sentence, maximum 25 words, specific to a single field.* A terminal command instruction technically violates the one-sentence rule. But asking for a Node.js version without providing the means to retrieve it is likely to produce `CONFIRMED-UNKNOWN` — the human already stated they don't know. The policy should address *instructional context* in question formulation: brief, parenthetical context that enables the human to answer is not a compound question. This is a gap in FC-3.

**What happens when a response is not a resolution?** If Alex responds to Q4 with *"I want Cloudflare Workers AND I want it fully static"* — this doesn't resolve the gap, it confirms the contradiction is real. The process needs a path for responses that surface design decisions rather than factual resolutions. The current policy has no such path.[^7_1]

**The register's `resolutionnote` field must hold the raw response value.** But Task 1.4 (Manifest Drafting) needs to translate that value into a valid manifest field entry. For Q6, the response might be *"I'd say small — it's just a few days of work"*. The resolutionnote records the raw response. Task 1.4 then maps *"small"* to the manifest enum value `small`. This mapping step is not described in the policy. If the raw response is ambiguous (*"it's a small-medium project"*), Task 1.4 cannot map it — creating a new gap that wasn't in the original register.

### Opportunities to Improve the Policy / FC-3

- Add a rule for *instructional context*: a question may include a parenthetical command or reference that enables the human to retrieve the information, provided it does not constitute a compound question or a decision prompt.
- Add a response classification step at the start of Subtask 3: before updating the register, each response is classified as `RESOLVED` (a specific, usable value), `CONFIRMED-UNKNOWN` (human cannot provide the information), or `DECISION-REQUIRED` (human has not decided; the gap cannot be resolved through clarification alone). The `DECISION-REQUIRED` path should flag the entry for human director action outside the clarification protocol.
- Add a note to Task 1.4 that `resolutionnote` values may require mapping to valid enum values, and that this mapping is a named derivation — not invention — and must be recorded in the traceability record.


### Risks

- **Duplicate questions reaching the human:** If linked group detection fails (OQ-1-04 and OQ-1-05 not consolidated), Alex receives two questions about the deployment target. They answer the first. When the second arrives, they may answer it inconsistently, or push back on the quality of the process. Either outcome is worse than one well-formulated question.
- **Appetite value ambiguity surviving into Task 1.4:** If Q6 is answered with a borderline response, the raw value stored in `resolutionnote` may not map cleanly to the valid enum. Task 1.4 may make an undocumented mapping decision — an invention by another name.

***

## Subtask 2 — Exchange Conduct

### What Is Happening

All questions are presented to the human director in a single exchange per FC-3 (batch approach).  The exchange is presented as a numbered list, grouped by domain, with each question followed immediately by its impact statement. The exchange is recorded in full before any response is processed.[^7_1]

The exchange record is created at the moment of sending — not after the response arrives:

```yaml
# clarification-exchange-CE-1-01.yaml

exchangeid: CE-1-01
step: 1
initiatedat: "2026-03-07T02:15:00+11:00"
questions:
  - questionid: Q-CE-1-01-01
    register_refs: [OQ-1-01]
    field: techstack
    questiontext: "Which version of AstroJS should this project use?"
    impactstatement: "Required before the environment contract can specify framework.version."

  - questionid: Q-CE-1-01-02
    register_refs: [OQ-1-02]
    field: techstack
    questiontext: "Should React be included as an explicit stack dependency for the Shadcn integration?"
    impactstatement: "Required to enumerate all install commands and config entries in the environment contract."

  - questionid: Q-CE-1-01-03
    register_refs: [OQ-1-03]
    field: techstack
    questiontext: "Which package manager should this project use — npm or pnpm?"
    impactstatement: "Required before install command entries can be written in the environment contract."

  - questionid: Q-CE-1-01-04
    register_refs: [OQ-1-04, OQ-1-05]
    field: deploymenttarget
    questiontext: "Are you deploying to Cloudflare Pages (static file hosting) or Cloudflare Workers (edge compute)?"
    impactstatement: "Determines the AstroJS output mode and adapter; the entire deployment section depends on this."

  - questionid: Q-CE-1-01-05
    register_refs: [OQ-1-06]
    field: devenvironment
    questiontext: "What version of Node.js is installed in your development environment? Run `node --version` to check."
    impactstatement: "Required before the runtime section of the environment contract can be completed."

  - questionid: Q-CE-1-01-06
    register_refs: [OQ-1-07]
    field: appetite
    questiontext: "Would you classify this appetite as small (days), medium (1–2 weeks), or large (multi-week)?"
    impactstatement: "The manifest requires one of these three values; freeform duration cannot be stored."

respondedat: null     # set when response arrives
responses: []         # populated in Subtask 3
```


### Skills Required to Do This to a High Standard

- **Record-before-send discipline** — the exchange record is created at `initiatedat` timestamp, before the human responds. This is not a detail; it is the evidence that the question was asked with a specific timestamp. An exchange record created after the response arrives could be backdated or misattributed.[^7_1]
- **Channel fidelity** — the questions are delivered exactly as formulated in Subtask 1. No paraphrasing, no added context, no conversational softening that changes the precision of the question.
- **Blocking correctly** — the process is blocked from proceeding to Subtask 3 until a response arrives. There is no timeout. There is no assumption.  If the human does not respond, the process waits.[^7_1]


### Examples of Excellence

The exchange is presented to the human as a clean, numbered list. No preamble beyond a one-line context statement. No explanatory paragraphs. Six questions, six impact statements. The exchange record is filed at the canonical path before the human sees the questions.

### Examples of Poor Performance

- Adding conversational framing: *"I've reviewed your brief and it's great — I just have a few quick questions before we get started!"* This wastes the human's attention and softens questions that are precise for a reason.
- Sending questions sequentially as they are formulated — one at a time — rather than batching. This produces multiple exchanges where one would suffice and tests the human's patience with the process.
- Not creating the exchange record until after the response arrives, backdating `initiatedat` to match the send time. This is an audit integrity failure.


### Uncovered Questions / Gaps

**The exchange presentation medium is not specified.** FC-3 defines the record format and question formulation rules but says nothing about *how* the exchange is presented to the human. In a chat interface, this is a single message. In a document-based workflow, it might be a review file. In an automated system, it could be an email or a form. The medium affects whether the response is structured (a form with per-question fields) or unstructured (a free-text reply). Unstructured responses make Subtask 3 harder. The policy should specify the expected response format.[^7_1]

### Opportunities to Improve the Policy / FC-3

- Specify the response format: the human is asked to respond per-question, referencing the question number. This is not a constraint on how the human writes — it is guidance on what makes a response processable in Subtask 3 without ambiguity.

***

## Subtask 3 — Response Processing

### What Is Happening

Each response is classified, the register is updated, and the exchange record is completed. Applying the response classification step proposed in Subtask 1:

Hypothetical responses from Alex:


| Question | Alex's response | Classification |
| :-- | :-- | :-- |
| Q1 — AstroJS version | "Latest stable is fine — I don't have a specific version preference" | `RESOLVED` — "latest stable" is a usable value with a documented derivation note |
| Q2 — React integration | "Yes, include React — Shadcn needs it" | `RESOLVED` — explicit confirmation |
| Q3 — Package manager | "Let's use pnpm" | `RESOLVED` |
| Q4 — Cloudflare deployment | "Cloudflare Pages — I got confused between the two products" | `RESOLVED` — contradiction also resolved |
| Q5 — Node.js version | "22.11.0 — just checked" | `RESOLVED` |
| Q6 — Appetite | "Small — a few days of focused work" | `RESOLVED` |

All six resolve cleanly in this hypothetical. The register is updated:

```yaml
# Updated register entries (showing OQ-1-01 and OQ-1-04 as examples)

- questionid: OQ-1-01
  field: techstack
  gap: "AstroJS version not specified"
  classification: BLOCKER
  resolutionstatus: RESOLVED
  resolutionnote: "Latest stable version acceptable — Alex confirmed no specific version preference (Q-CE-1-01-01)"
  resolvedbystep: 1
  resolvedatexchange: CE-1-01

- questionid: OQ-1-04
  field: deploymenttarget
  gap: "Cloudflare Workers named but technical target may be Cloudflare Pages"
  classification: BLOCKER
  resolutionstatus: RESOLVED
  resolutionnote: "Cloudflare Pages confirmed — Alex stated confusion between products (Q-CE-1-01-04)"
  resolvedbystep: 1
  resolvedatexchange: CE-1-01

- questionid: OQ-1-05
  field: deploymenttarget
  gap_type: CONTRADICTION
  gap: "Cloudflare Workers implies edge compute adapter incompatible with AstroJS output:static"
  classification: BLOCKER
  resolutionstatus: RESOLVED
  resolutionnote: "Contradiction resolved — correct target is Cloudflare Pages (static hosting); static constraint and deployment target are now consistent (Q-CE-1-01-04)"
  resolvedbystep: 1
  resolvedatexchange: CE-1-01
```

The exchange record is completed:

```yaml
# clarification-exchange-CE-1-01.yaml (completed)

respondedat: "2026-03-07T02:47:00+11:00"
responses:
  - questionid: Q-CE-1-01-01
    responsetext: "Latest stable is fine — I don't have a specific version preference"
    resolution: RESOLVED

  - questionid: Q-CE-1-01-04
    responsetext: "Cloudflare Pages — I got confused between the two products"
    resolution: RESOLVED

  # ... remaining responses
```


### Skills Required to Do This to a High Standard

- **Response classification before register update** — classifying each response as RESOLVED, CONFIRMED-UNKNOWN, or DECISION-REQUIRED before writing any register update. This prevents a partially processed response being written as RESOLVED when it is actually DECISION-REQUIRED.
- **Linked entry propagation** — when Q4 resolves OQ-1-04, the executor must also update OQ-1-05 (the linked contradiction entry). A single response can resolve multiple register entries. The executor must query `linked_questions` for each resolved entry and cascade the update.
- **"Latest stable" as a named derivation, not a value** — Alex's Q1 response is not a specific version. "Latest stable AstroJS" is a derivation rule: at manifest drafting time, Task 1.4 must resolve "latest stable" to an actual version number and record it as a derivation in the traceability record. This is not invention — it is a documented derivation. But it must be recorded as such, not silently treated as a value.[^7_1]
- **CONFIRMED-UNKNOWN cascade** — if any response is CONFIRMED-UNKNOWN, the register entry is updated and the gap is formally downgraded to a WARNING openquestion. This entry persists in the register and is carried into Step 2, where it may be reclassified as BLOCKER in Step 2's context. The FC-8 carry-forward mechanism handles this.[^7_1]


### Examples of Excellence

After processing Q4's response, the executor queries the register for all entries with `OQ-1-04` in their `linked_questions` array — finds OQ-1-05 — and updates both in the same operation. The resolutionnote for OQ-1-05 explicitly states that the contradiction is resolved, why it is resolved, and which exchange question provides the evidence. A verifier can independently confirm the resolution by reading the exchange record.

The Q1 "latest stable" response is marked RESOLVED but the `resolutionnote` explicitly flags: *"Value requires derivation at Task 1.4 — 'latest stable AstroJS' must be resolved to a specific version number at time of manifest drafting."* This note ensures Task 1.4 does not treat "latest stable" as a valid `techstack` entry.[^7_1]

### Examples of Poor Performance

- Updating OQ-1-04 as RESOLVED but not checking for linked entries — OQ-1-05 remains `OPEN`. Task 1.4 reads the register, finds OQ-1-05 still OPEN, and either blocks or escalates. The contradiction has been resolved in the exchange but the register doesn't reflect it.
- Treating "latest stable" as a RESOLVED value and writing `techstack: AstroJS (latest stable)` in the traceability note. "Latest stable" is not a version number. It is a derivation instruction. If Task 1.4 uses it as-is, the manifest violates the `techstack` field's format rule: *"Named technologies only — AstroJS 5.x is valid, modern frontend stack is not."*[^7_1]
- Processing all responses in a single pass without classifying each one first — a DECISION-REQUIRED response treated as RESOLVED because it contains an answer-shaped string.


### Uncovered Questions / Gaps

**"Latest stable" creates a version resolution dependency that doesn't exist in the policy.** The policy assumes clarification produces a specific value. Alex's Q1 response is technically a deferred decision — *"I'll take whatever the current version is."* This is common and reasonable behaviour for a new project. But it means the manifest's `techstack` field cannot be populated with a specific version at Task 1.4 time without an additional lookup step (check the current AstroJS release). That lookup is a new operation that belongs in Task 1.4 — but it requires the executor to know that current stable version lookups are permitted derivations. The policy should describe this case explicitly.[^7_1]

**The DECISION-REQUIRED path is still undefined.** If Alex had responded to Q4 with *"I want both — I want it on Workers but fully static,"* there is no process path. FC-3 says the clarification protocol handles *missing declared information*, not *undecided information*. A DECISION-REQUIRED response signals that the human has a conflicting intent — not missing information. This requires escalation to a human decision point, but the policy has no mechanism for mid-step escalation to a decision gate. This is a gap that should be flagged for framework-level resolution.[^7_1]

### Opportunities to Improve the Policy

- Add `DECISION-REQUIRED` as a formal response classification in FC-3, with a defined path: the entry remains BLOCKER, a decision-request record is created, and the step enters a `AWAITING-DECISION` state until the human resolves the conflict.
- Add a note to Task 1.3 that "latest stable" and equivalent deferred version references are valid RESOLVED responses but require a version-resolution derivation at Task 1.4. The `resolutionnote` must flag this explicitly.
- Add linked entry propagation as an explicit step in Subtask 3: *"For each RESOLVED entry, query the register for all entries referencing this entry's `questionid` in their `linked_questions` field and apply the same resolution."*


### Risks

- **OQ-1-05 left OPEN despite resolution:** The most mechanically likely failure. OQ-1-04 and OQ-1-05 are linked. If only OQ-1-04 is updated, Task 1.4 reads OQ-1-05 as still OPEN, treats `deploymenttarget` as having an unresolved contradiction, and either blocks or escalates. The error is in the register, not in the actual brief state.
- **"Latest stable" written as a manifest value:** If the `resolutionnote` for OQ-1-01 doesn't flag the derivation requirement, Task 1.4 may write `AstroJS (latest stable)` into the `techstack` field. This violates the field's format rule. The manifest fails its own schema validation.

***

## Done When

Task 1.3 is complete when:

1. `clarification-exchange-CE-1-01.yaml` exists at `.framework/clarifications/` with `respondedat` populated
2. Every BLOCKER entry in the register has `resolutionstatus` of either `RESOLVED` or `CONFIRMED-UNKNOWN`
3. All `RESOLVED` entries have a `resolutionnote` specific enough to populate the relevant manifest field (or flag a named derivation)
4. All `CONFIRMED-UNKNOWN` entries have their classification updated per FC-2 downgrade rules[^7_1]
5. All linked entries have been updated consistently — no linked pair with mismatched resolution statuses
6. No remaining `OPEN` BLOCKER entries exist in the register

***

Ready to proceed to Task 1.4 — Manifest Drafting?

<div align="center">⁂</div>

[^7_1]: i-am-making-progress-in-creati-fuGLU8hCRLyka3xtBTVglA.md


---

# Task 1.4 — Manifest Drafting: Full Subtask Analysis

**Task 1.4's question:** Can all confirmed values be structured into a valid, traceable manifest?[^8_1]

**Input:** `brief-inventory.yaml`, `open-questions-register.yaml` (all BLOCKERs resolved), `clarification-exchange-CE-1-01.yaml`, manifest schema

**Outputs:**

- `project-manifest.yaml` — primary output, DRAFT status, human-reviewed at Task 1.5
- `project-manifest.traceability.yaml` — FC-5 companion record, built field-by-field alongside the manifest[^8_1]

**Standing constraint for all subtasks:** The traceability record is written field-by-field *during* drafting, not after. A field value that cannot be given a traceability entry at the time of writing must not be written into the manifest yet. This is the operational enforcement of FC-1.[^8_1]

***

## Revised Subtask Structure

The policy's current subtask list is a flat sequence of instructions rather than discrete, verifiable units. Restructured:


| \# | Subtask | Purpose |
| :-- | :-- | :-- |
| 1 | Pre-Drafting Derivation Resolution | Resolve all pending derivations flagged in register before any field is written |
| 2 | Required Field Population | Populate all required fields with confirmed values; write traceability entry per field |
| 3 | Optional Field Population | Populate all optional fields; write traceability entry per field |
| 4 | Open Questions Population | Write register's unresolved WARNING/INFO/CONFIRMED-UNKNOWN entries into manifest `openquestions` |
| 5 | Self-Check | Validate manifest completeness against schema rules and DoD criteria before declaring DRAFT |


***

## Subtask 1 — Pre-Drafting Derivation Resolution

### What Is Happening

Before a single manifest field is written, the executor reads the register for any `resolutionnote` entries flagging pending derivations. These must be resolved first — writing a manifest field from an unresolved derivation produces an invalid value.[^8_1]

From Task 1.3's register, two derivations require resolution:

**Derivation 1 — AstroJS version**
The register entry for OQ-1-01 was marked RESOLVED with `resolutionnote`: *"Latest stable version acceptable — requires version resolution at Task 1.4."* The executor must determine the current AstroJS stable version before populating `techstack`. In an agent-automated context, this is a tool call (npm registry or GitHub releases lookup). The result is recorded in the traceability record as `sourcetype: derivationrule`, `sourcereference: latestStableVersionLookup-AstroJS-2026-03-07`.

**Derivation 2 — `projectid` from `projectname`**
`projectid` is derived from `projectname` via the kebab-case transformation rule. This is a known permitted derivation documented in FC-1.  No lookup required — the rule is deterministic.[^8_1]

**A gap surfaces here:** The clarification exchange asked about AstroJS version but not Shadcn version. Shadcn was also unversioned in the brief (S-04). During pre-drafting, when the executor attempts to resolve `techstack` entries, it finds no valid source for a Shadcn version number. This is an FC-1 violation waiting to happen: if a Shadcn version is written without a source, it is invented.

The correct handling: create a new WARNING entry in the open questions register (`OQ-1-10`) and proceed with `shadcn/ui (latest at project init)` as a named derivation — same treatment as AstroJS. This is a significant finding: **Task 1.2 failed to generate a BLOCKER for Shadcn version**, just as it was caught not generating a BLOCKER for `appetite`. The pre-drafting check functions as a quality gate that catches Task 1.2 omissions.

### Skills Required to Do This to a High Standard

- **Derivation rule knowledge** — distinguishing a permitted derivation (kebab-case from projectname, latest-stable from confirmed acceptance) from an invention (silently assuming AstroJS 5.6.2 without a source)
- **Register reading discipline** — scanning every RESOLVED entry's `resolutionnote` for derivation flags before beginning field population; not trusting that Task 1.3 will have flagged everything
- **Gap surfacing during drafting** — recognising when a field has no valid source mid-drafting and treating it as a new open question rather than proceeding with assumption


### Examples of Excellence

The executor identifies both the AstroJS and Shadcn version gaps before writing a single field. AstroJS is resolved via a version lookup and recorded as a named derivation. Shadcn is also resolved via the same mechanism. A new `OQ-1-10` entry is added to the register for Shadcn version, marked RESOLVED with the derivation note. The traceability record contains entries for both with specific `sourcereference` values including the lookup date.

### Examples of Poor Performance

- Proceeding directly to field population without checking for unresolved derivations — the AstroJS "latest stable" flag goes unnoticed, and `techstack` is populated with `AstroJS (latest stable)` as a literal string. This violates the schema rule that `techstack` must contain named technologies with version numbers.[^8_1]
- Catching the AstroJS derivation but not noticing Shadcn — because Shadcn wasn't explicitly flagged in the register. The executor writes `shadcn/ui` without a version, which either violates the format rule or creates a silent ambiguity.


### Uncovered Questions / Gaps

**Version lookup is a tool call that requires external access.** The framework currently has no specified tool for querying package registries or release APIs. If the agent cannot make this call, "latest stable" cannot be resolved to a specific version. The policy should specify how version resolution is handled when external lookup is unavailable — either as a CONFIRMED-UNKNOWN (no version, documented gap) or as a permitted shorthand (`AstroJS 5.x` using the major version only).[^8_1]

### Risks

- **Shadcn version omission from register:** If Subtask 1 doesn't catch the Shadcn gap, it surfaces even later — either at the self-check (Subtask 5) if the executor is thorough, or at Task 1.5 human review, or worst case at Step 2 when the environment contract cannot be written without it.

***

## Subtask 2 — Required Field Population

### What Is Happening

Each required field is populated in schema order. For every field, the sequence is:

1. Identify the source from the register, exchange record, or brief statement ID
2. Write the field value
3. Immediately write the traceability entry

The source identification step is not optional — it enforces FC-1 structurally.[^8_1]

Applied to the case study, abbreviated:

```yaml
# project-manifest.yaml (required fields)

projectid: meridian-consulting-launch-landing-page
projectname: "Meridian Consulting — Launch Landing Page"
description: >
  A single-page marketing website for Meridian Consulting. The page includes
  sections for hero introduction, services overview, an about section, and a
  contact form routing to email. Visual style: clean, minimal, credible.
techstack:
  - "AstroJS 5.3.0"       # version resolved by derivation: latest stable at 2026-03-07
  - "Shadcn/ui 2.4.0"     # version resolved by derivation: latest stable at 2026-03-07
  - "React 19.x"          # confirmed via clarification Q-CE-1-01-02
  - "@astrojs/react"      # confirmed via clarification Q-CE-1-01-02
  - "pnpm"                # confirmed via clarification Q-CE-1-01-03
deploymenttarget: "Cloudflare Pages — meridianconsulting.com.au"
devenvironment:
  os: "macOS Sonoma"
  editor: "VS Code"
  runtime: "Node.js 22.11.0"
  packagemanager: "pnpm"
humanactors:
  - name: "Alex Chen"
    role: humandirector
appetite: small

status: DRAFT
created: "2026-03-07T02:55:00+11:00"
```

Corresponding traceability entries (abbreviated):

```yaml
# project-manifest.traceability.yaml

- outputfield: projectid
  valuesummary: "meridian-consulting-l"
  sourcetype: derivationrule
  sourcereference: "kebab-case-transformation from projectname"

- outputfield: projectname
  valuesummary: "Meridian Consulting —"
  sourcetype: brief
  sourcereference: "brief S-01, first sentence"

- outputfield: techstack[^8_0]
  valuesummary: "AstroJS 5.3.0"
  sourcetype: derivationrule
  sourcereference: "latestStableVersionLookup-AstroJS-2026-03-07; acceptance confirmed by clarification Q-CE-1-01-01"

- outputfield: techstack[^8_2]
  valuesummary: "React 19.x"
  sourcetype: clarificationanswer
  sourcereference: "CE-1-01, Q-CE-1-01-02, response: 'Yes, include React — Shadcn needs it'"

- outputfield: deploymenttarget
  valuesummary: "Cloudflare Pages — m"
  sourcetype: clarificationanswer
  sourcereference: "CE-1-01, Q-CE-1-01-04, response: 'Cloudflare Pages — I got confused between the two products'"

- outputfield: appetite
  valuesummary: "small"
  sourcetype: clarificationanswer
  sourcereference: "CE-1-01, Q-CE-1-01-06, response: 'Small — a few days of focused work'; mapped from freeform to valid enum value 'small'"
```


### Skills Required to Do This to a High Standard

- **Schema-order discipline** — populating fields in schema order, not in the order they appear in the brief or the register. Schema order is not arbitrary; it mirrors the dependency structure of the manifest. `projectid` depends on `projectname`, which must be written first.
- **Description assembly without invention** — the `description` field requires 2–4 sentences drawn from the brief *without addition*. The executor must assemble from brief statements (S-01, S-06, S-07) without rephrasing, elaborating, or improving. If the brief's language is imprecise, the description is imprecise. This is a fidelity requirement, not a quality requirement.
- **Enum mapping as named derivation** — `appetite: small` is derived from Alex's freeform response *"Small — a few days of focused work."* Mapping "small" to the enum value `small` is a trivial derivation, but it must be recorded as such.  The traceability entry shows the raw response and the mapping rule.[^8_1]
- **Simultaneous traceability writing** — writing the manifest field and the traceability entry in the same operation, not queuing traceability updates for after the manifest is complete. If the executor writes the full manifest first and the traceability record second, there is a window in which the manifest exists without provenance — during which an interruption would produce an untraceable document.


### Examples of Excellence

The `description` field uses Alex's words from the brief without normalisation. If Alex wrote *"I need a single-page marketing website"*, the description begins *"A single-page marketing website"* — not *"This project delivers a single-page marketing website."* The executor's voice does not appear in the manifest.[^8_1]

The `techstack` entries include exact version numbers (not major-version shorthands) with traceability entries that identify the specific lookup date and the clarification that authorised the derivation.

### Examples of Poor Performance

- Rewriting the `description` field in cleaner, more formal language than Alex used. The manifest is a faithful restatement, not an edited version. Any wording not in Alex's brief or clarification responses is an invention.[^8_1]
- Writing `appetite: small` without a traceability entry documenting the mapping from freeform language. The mapping is auditable — but without the traceability entry, the verifier at Task 1.5 cannot confirm whether *"small"* came from Alex or was assumed by the executor.
- Deferring traceability entry writing to after all fields are populated — risking that the connection between value and source is reconstructed from memory rather than recorded at point of entry.


### Uncovered Questions / Gaps

**The `description` field's assembly instruction ("drawn from the brief without addition") is not a mechanical rule.** The brief contains many statements; the description field holds 2–4 sentences. Selecting which statements to include is an editorial judgment — and any selection is implicitly also a de-selection. The policy should specify the selection criteria: which aspects of the brief belong in `description` vs. `constraints` vs. `outofscope`. Without this, two executors may produce different descriptions from the same brief, both technically compliant.

**The `techstack` field format rule specifies "Named technologies only — AstroJS 5.x is valid."** But our manifest lists five stack entries (AstroJS, Shadcn/ui, React, @astrojs/react, pnpm). Should `pnpm` be in `techstack` or in `devenvironment.packagemanager`? It appears in both our manifest above. This is a schema ambiguity — package managers occupy a boundary between stack and environment. The manifest template should clarify whether package managers belong in `techstack`, `devenvironment`, or both.

### Opportunities to Improve the Policy

- Add selection criteria for the `description` field assembly: *"Include: project type, primary purpose, and key deliverable. Exclude: constraints, deployment details, and named actors — these have dedicated fields."*
- Clarify whether `pnpm`/`npm`/package managers belong in `techstack`, `devenvironment`, or both, and whether their presence in one field precludes the other.


### Risks

- **Traceability written after the fact:** If the executor drafts the full manifest and then writes traceability entries, the entries are reconstructions. For fields with clear, single sources, reconstruction is accurate. For fields assembled from multiple statements (like `description`), reconstruction introduces uncertainty about which statement contributed which phrase. The FC-5 requirement to write field-by-field exists precisely to prevent this.[^8_1]

***

## Subtask 3 — Optional Field Population

### What Is Happening

Optional fields follow the same field-then-traceability pattern. Fields with content from the brief are populated; fields with no brief content are explicitly recorded as `[]` or `none stated` — never omitted.  Omitting an optional field is structurally different from recording it as absent: omission creates ambiguity about whether the field was considered; explicit empty recording confirms it was assessed and found absent.[^8_1]

```yaml
# project-manifest.yaml (optional fields continued)

constraints:
  - "No dedicated backend — contact form must use third-party handler"
  - "Fully static site — no server-side rendering"
  - "Lighthouse Performance score 90 or above"
  - "Minimal dependency footprint — avoid unnecessary packages"

outofscope:
  - "CMS or content management capability"
  - "Blog or additional pages beyond the landing page"
  - "Analytics integration"
  - "Server-side logic beyond Cloudflare edge capabilities"

existingassets: []

referenceexamples:
  - "Linear.app — clean typography, bold headings, whitespace-heavy layout"
  - "Stripe marketing pages — professional, minimal, credible aesthetic"

integrationrequirements:
  - provider: "TBD"
    type: "third-party form handler"
    note: "Formspree mentioned tentatively; provider unconfirmed — see OQ-1-08"
```

The `integrationrequirements` entry deserves attention. The field is present but AMBIGUOUS — Formspree was mentioned tentatively, not confirmed. The manifest records what was said (`Formspree mentioned tentatively`) and references the open question register entry. It does not default to Formspree as the confirmed provider, and it does not leave the field empty as if nothing was said. This is the correct handling of AMBIGUOUS optional content: record the ambiguity faithfully with a register cross-reference.[^8_1]

### Skills Required to Do This to a High Standard

- **Faithful transcription of constraints and out-of-scope** — these fields must use Alex's language, not normalized or tidied versions. *"No dedicated backend"* is Alex's phrase; the manifest uses it. The executor may not interpret *"no dedicated backend"* as *"serverless architecture only"* — that is editorial expansion.
- **Empty field discipline** — recording `existingassets: []` rather than omitting the field. This seems trivial but is operationally important: a downstream agent checking whether existing assets were considered gets a definitive answer from `[]`; it gets no answer from an absent field.
- **Ambiguous optional field handling** — the `integrationrequirements` case. The executor must resist two failure modes: (a) treating AMBIGUOUS as ABSENT and leaving the field empty, losing the Formspree signal; (b) treating the tentative mention as a confirmed declaration and writing `provider: Formspree`.


### Examples of Excellence

The `referenceexamples` field includes Alex's design intent descriptors (*"clean typography, bold headings, whitespace-heavy"*) even though these exceed the field's typical scope. They were in the brief. They are recorded. A separate traceability note flags them as exceeding standard field scope and references the non-mappable list from Task 1.1 — the register trail is complete.

### Examples of Poor Performance

- Writing `constraints: ["no backend", "static", "90+ Lighthouse", "minimal deps"]` — normalised language that discards Alex's exact phrasing. If Alex's constraint *"avoid unnecessary packages"* is written as *"minimal deps"*, the constraint becomes ambiguous: what counts as unnecessary? Alex's words carry the intended scope; the executor's shorthand does not.
- Omitting `existingassets` entirely rather than recording `[]`.


### Uncovered Questions / Gaps

**The `referenceexamples` field has no defined scope boundary in the schema.** It currently accepts names of reference projects. Alex provided names plus qualitative descriptors. The schema rule doesn't specify whether descriptors are valid entries or overflow. The traceability record can document the judgment call, but the schema should be explicit.[^8_1]

***

## Subtask 4 — Open Questions Population

### What Is Happening

The manifest's `openquestions` field is populated from the register's remaining UNRESOLVED entries — those with `resolutionstatus: OPEN` and classification `WARNING` or `INFO`, plus any `CONFIRMED-UNKNOWN` entries from Task 1.3. In our case study, these are:

```yaml
openquestions:
  - questionid: OQ-1-08
    field: integrationrequirements
    gap: "Form handler provider tentative — Formspree mentioned but not confirmed"
    impact: "Step 2 services section cannot specify integration details until provider is confirmed"
    classification: WARNING
    resolutionstatus: OPEN

  - questionid: OQ-1-09
    field: null
    gap: "Cloudflare account active and DNS control available — no manifest field exists for this"
    impact: "Step 2 deployment section may not reflect self-managed DNS; schema gap candidate"
    classification: WARNING
    schema_gap_flag: true
    resolutionstatus: OPEN

  - questionid: OQ-1-10
    field: techstack
    gap: "Shadcn/ui version resolved via derivation — not confirmed by human director"
    impact: "If latest stable derivation is incorrect, environment contract version entries will be wrong"
    classification: WARNING
    resolutionstatus: OPEN
```


### Skills Required to Do This to a High Standard

- **Register completeness check** — querying the register for ALL non-RESOLVED entries, not just the ones the executor remembers from Task 1.2. New entries created during Task 1.4 (like OQ-1-10 for Shadcn) must also appear here.
- **Impact statement currency** — some register entries were written in Task 1.2 with Step 2 impacts. By Task 1.4, some impacts may be more specific. The executor may update `impact` to reflect the actual manifest state — but may not change `gap`, `questionid`, or `raisedbystep` (immutable per FC-8).[^8_1]


### Risks

- **OQ-1-10 absent from manifest:** If the Shadcn derivation was handled silently in Subtask 1 without a register entry, it also won't appear in the manifest's `openquestions`. Step 2 then receives a manifest with a version-derived `techstack` entry and no signal that the version was derived rather than confirmed. If the derivation turns out to be wrong (e.g., the project requires an older Shadcn version for compatibility), there is no record that it was ever flagged.

***

## Subtask 5 — Self-Check

### What Is Happening

Before setting `status: DRAFT`, the executor runs a deterministic checklist against the manifest. This is not a judgment review — each item is a binary pass/fail test.[^8_1]

```
Self-check checklist:

□ All required fields are present and non-empty
□ techstack has at least one versioned entry
□ humanactors has at least one entry with role: humandirector
□ appetite value is exactly one of: small / medium / large
□ status is DRAFT (not APPROVED — never self-approved)
□ created is set to current ISO 8601 datetime with timezone
□ approvedat is absent
□ approvedby is absent
□ Every required field has a corresponding traceability entry
□ Every RESOLVED BLOCKER register entry has a corresponding field value
□ Every UNRESOLVED register entry appears in openquestions
□ No field contains a value with no traceable source
□ No field uses language not found in the brief or clarification record
```

Any failed item is corrected before `status: DRAFT` is set. The self-check is not a separate review — it is the executor checking its own work. The formal review happens at Task 1.5 by a separate party.[^8_1]

### Skills Required to Do This to a High Standard

- **Checklist adherence without shortcuts** — running every item, not skipping items that "clearly pass." The most commonly skipped items are the last three, which require cross-referencing two documents.
- **Recognising that self-check failure is the correct outcome** — finding a self-check failure is not a process problem; it is the self-check working. The failure should be corrected and the item re-checked, not rationalised.


### Examples of Poor Performance

Setting `status: DRAFT` and then running the self-check — treating it as a review after the fact. The self-check gate must be passed *before* status is set, not after. Status DRAFT is the signal to Task 1.5 that the executor asserts completeness; setting it before the check undermines that assertion.

***

## Format Decision: `.md` vs `.yaml`

The policy specifies `project-manifest.md`.  But the manifest is structured data with a human gate — it is read by both the Task 1.5 executor and the human director. Two considerations:[^8_1]

- `.yaml` is both machine-readable and human-readable at this level of complexity. Alex can read a YAML manifest.
- `.md` implies prose sections that this manifest does not have. The manifest is entirely structured fields.

**Recommendation:** Change the manifest format to `.yaml` and the traceability record to `.yaml` (already proposed). At Task 1.5, if the human review interface requires prose, a rendered summary can be generated from the YAML — but the canonical artefact is the structured file. This should be flagged as an improvement to the Step 1 policy.

***

## Done When

Task 1.4 is complete when:

1. `project-manifest.yaml` exists at `.framework/project-manifest.yaml` with `status: DRAFT`
2. `project-manifest.traceability.yaml` exists at `.framework/traceability/project-manifest.traceability.yaml`
3. All required fields are non-empty
4. Every non-empty field has a corresponding traceability entry
5. Every RESOLVED BLOCKER register entry corresponds to a populated field value
6. Every UNRESOLVED register entry appears in `openquestions`
7. Self-check passed all items
8. `approvedat` and `approvedby` are absent
9. No field value is present without a traceable source

***

Ready to proceed to Task 1.5 — Human Review?

<div align="center">⁂</div>

[^8_1]: i-am-making-progress-in-creati-fuGLU8hCRLyka3xtBTVglA.md


---

# Task 1.5 — Human Review: Full Subtask Analysis

**Task 1.5's question:** Does the human director confirm that the manifest accurately represents their intent?[^9_1]

**This task is structurally different from all previous tasks.** Tasks 1.1–1.4 are agent-executed operations on structured data. Task 1.5 is a human gate. The agent's role shifts from producer to presenter and recorder. The human director is the only party who can close this task.

**Input:** `project-manifest.yaml` in DRAFT status from Task 1.4, `open-questions-register.yaml`

**Outputs:**

- `project-manifest.yaml` in APPROVED status
- Updated `project-manifest.traceability.yaml` (if corrections applied)
- Audit log entry per FC-4 Tier 1[^9_1]
- Updated `open-questions-register.yaml` (if corrections introduce new entries)

***

## Revised Subtask Structure

| \# | Subtask | Nature |
| :-- | :-- | :-- |
| 1 | Presentation Preparation | Agent — generate human-navigable review package |
| 2 | Presentation and Blocking | Agent → Human — deliver; block until response |
| 3 | Response Classification | Agent — classify response as APPROVED or RETURNED |
| 4 | Correction Application *(conditional, loops)* | Agent — apply corrections; update traceability; re-check |
| 5 | Approval Recording | Agent — record FC-4 Tier 1 approval action |


***

## Subtask 1 — Presentation Preparation

### What Is Happening

The canonical artefact is `project-manifest.yaml`. The human director confirmed they are comfortable with the project — but they did not agree to review raw YAML. Before presenting, the executor must determine whether the human can navigate the manifest directly or whether a rendered summary is required.

This surfaces a structural design question the policy does not answer: **what is the human actually reviewing?**

Two distinct things require review:

**A — Field accuracy:** Does each field value accurately represent what the human said? Alex can confirm this by reading the manifest. Most fields are direct transcriptions of their own words.

**B — Open questions acknowledgement:** The manifest contains open questions (OQ-1-08, OQ-1-09, OQ-1-10) that will carry into Step 2 unresolved. The human director must be informed of these and acknowledge them before approval — not because they need to resolve them here, but because approving a manifest with undisclosed gaps is not informed consent.[^9_1]

The presentation package therefore has two components:

```
review-package-CE-1-02.yaml       # not an exchange — a presentation record

manifestpath: .framework/project-manifest.yaml
manifestversion: DRAFT
presentedat: "2026-03-07T03:10:00+11:00"
presentedto: "Alex Chen"

summary:                          # human-readable rendering of key fields
  projectname: "Meridian Consulting — Launch Landing Page"
  techstack: ["AstroJS 5.3.0", "Shadcn/ui 2.4.0", "React 19.x", "@astrojs/react", "pnpm"]
  deploymenttarget: "Cloudflare Pages — meridianconsulting.com.au"
  appetite: small
  constraints:
    - "No dedicated backend — contact form uses third-party handler"
    - "Fully static — no server-side rendering"
    - "Lighthouse Performance 90+"
    - "Minimal dependency footprint"
  outofscope:
    - "CMS, blog, analytics, server-side logic"

open_questions_for_acknowledgement:
  - questionid: OQ-1-08
    summary: "Form handler provider not confirmed — Formspree mentioned tentatively"
    impact: "Step 2 services section will be incomplete until provider is confirmed"
  - questionid: OQ-1-09
    summary: "Cloudflare account readiness noted but no manifest field exists for it"
    impact: "Step 2 will need to address DNS configuration separately"
  - questionid: OQ-1-10
    summary: "Shadcn/ui version resolved by latest-stable derivation, not confirmed directly"
    impact: "If version is incorrect, environment contract version entries will need revision"

review_instruction: >
  Please confirm: (1) the fields above accurately represent your intent,
  and (2) you have noted the open questions listed. If any field is wrong
  or missing, identify the specific field and the correct value.
  To approve, respond with an explicit approval statement.
```

The summary is a rendered view — not the canonical document. The canonical document is the YAML. The summary is generated deterministically from the YAML fields; it does not editorially add or remove content. If the summary misrepresents the YAML, the summary is wrong, not the manifest.

### Skills Required to Do This to a High Standard

- **Presentation scope discipline** — the summary must render what is in the manifest, nothing more. Adding context (*"we asked about the deployment target because there was some confusion"*) introduces editorial content that the human may treat as part of the record.
- **Open questions presentation** — every WARNING and CONFIRMED-UNKNOWN register entry must appear in the review package. Presenting only BLOCKER-class items and omitting WARNINGs would allow the human to approve a manifest without knowing that, for example, the form handler provider is unresolved.
- **Distinguishing field accuracy from technical correctness** — the human director is not being asked whether AstroJS 5.3.0 is the right version for this project. They are being asked whether the record accurately captures what they said. The review instruction must not prompt a technical review — that is not within Alex's role at this step.


### Examples of Excellence

The review instruction contains exactly two questions: (1) are the fields accurate? (2) have you noted the open questions? It does not ask for technical sign-off, design approval, or strategic confirmation. It does not apologise for the process or over-explain why the open questions exist.

### Examples of Poor Performance

- Presenting the raw YAML without a summary, assuming Alex can navigate it. This is accurate but creates unnecessary friction. More importantly, the open questions section of the YAML is buried in a list of all register entries — the human may miss them or not understand their significance.
- Presenting a summary that omits `referenceexamples` or `constraints` because "Alex wrote those, they obviously know them." Every field is presented. The human must have the opportunity to correct any field, including fields they authored.
- Adding a review note: *"The tech stack was quite complex — we had to ask several clarifying questions. You may want to review those sections carefully."* This is editorial framing that primes the human to focus on specific areas, potentially causing them to overlook errors elsewhere.


### Uncovered Questions / Gaps

**The summary is generated from the manifest — but the manifest is the thing being reviewed.** If the summary contains an error (a rendering bug, a truncated value), the human may approve a summary that doesn't match the canonical YAML. The presentation preparation step needs an explicit validation: every summary field value must match the corresponding manifest field value exactly. This is a testable check, not a judgment call.

**The review instruction says "respond with an explicit approval statement" — but what counts as explicit?** In a chat interface, *"looks good"*, *"approved"*, *"yes"*, and *"APPROVED"* all express approval but with different levels of formality. The FC-4 Tier 1 approval record requires the action to be explicit and attributed.  The policy should define the minimum threshold for an explicit approval: at minimum, the response must contain the field name (`project-manifest`) and the word "approved" (case-insensitive). Freeform affirmation is not sufficient.[^9_1]

### Opportunities to Improve the Policy

- Add a summary generation step with a deterministic rendering rule and a summary-vs-manifest validation check.
- Define the minimum explicit approval statement format in FC-4: the response must name the document and state approval. *"Approved"* alone is insufficient — it may refer to something else in a conversation.

***

## Subtask 2 — Presentation and Blocking

### What Is Happening

The review package is delivered to the human director and the process blocks. No further work proceeds until a response is received. There is no timeout. There is no fallback that allows the process to self-approve or proceed on assumption.[^9_1]

The presentation timestamp (`presentedat`) is recorded before delivery — the same discipline as the clarification exchange in Task 1.3.

### Skills Required to Do This to a High Standard

- **Hard blocking** — the executor must not perform any further Task 1 work while awaiting response. No optimistic pre-loading of Task 1.5 correction logic, no pre-populating the approval record with expected values. The process is genuinely suspended.
- **Single delivery** — the review package is delivered once. If the human asks a question about the review package before responding, that question is answered but the review request is not re-sent. The original `presentedat` timestamp remains. Re-sending resets the clock in a way that could obscure the actual review duration.


### Uncovered Questions / Gaps

**The presentation medium is unspecified.** This is the same gap identified in Task 1.3 Subtask 2. In a chat interface, the review package is a message. In a document workflow, it may be a PR review request or a shared file. The medium affects what *"respond with an explicit approval statement"* looks like in practice. The policy should specify, or delegate to a platform-specific configuration.

**What constitutes a non-response?** If Alex doesn't respond, the step waits indefinitely. The FC-9 bootstrap state machine enters `AWAITING-DECISION` state.  The policy correctly defers the response-time SLA to framework level (F28), but for a human running this process interactively, there should be guidance on what to do after a reasonable wait period — even if that guidance is only *"the step remains blocked until a response is received; no autonomous action is taken."*[^9_1]

***

## Subtask 3 — Response Classification

### What Is Happening

The response is classified before any action is taken. Three possible classifications:


| Classification | Condition | Path |
| :-- | :-- | :-- |
| `APPROVED` | Response contains an explicit approval statement for the manifest | → Subtask 5 |
| `RETURNED` | Response identifies one or more specific corrections | → Subtask 4 |
| `UNCLEAR` | Response is ambiguous — neither a clear approval nor specific corrections | → Re-present with clarification request |

The `UNCLEAR` path is not in the current policy. It must be added because freeform human responses frequently fall between the two defined outcomes. *"Looks mostly right but I'm not sure about the appetite field"* is neither an approval nor a returned correction — it is an expression of uncertainty.[^9_1]

The correct handling of `UNCLEAR`: the executor identifies what specific question would resolve the ambiguity and re-presents a single targeted question. This is not a new clarification exchange (FC-3 is for brief gaps, not review responses) — it is a follow-up on the same review. The `presentedat` timestamp does not change; a `followuprequestedat` timestamp is added to the review record.

### Skills Required to Do This to a High Standard

- **Classification before action** — the executor must classify the response before deciding what to do. An executor that acts while classifying may simultaneously begin correction processing and approval recording if the response is ambiguous.
- **Specific correction identification** — a RETURNED response must identify specific fields. *"Something feels off about the tech stack"* is not a specific correction — it is an expression of unease. The executor must ask: *"Which field in the tech stack section needs to change, and what should it say?"* This is a follow-up, making the response `UNCLEAR`, not `RETURNED`.


### Examples of Excellence

Alex responds: *"Approved — but just to note, the appetite should probably be 'medium' since I said 1–2 weeks."*

This is both an approval statement AND a correction notice in one response. Classification: `RETURNED` — because the human has identified a specific field that needs changing. The approval statement is noted but does not take effect until the correction is applied and re-reviewed. An `APPROVED` response with an embedded correction is still `RETURNED`.[^9_1]

### Examples of Poor Performance

Classifying *"Looks good to me"* as `APPROVED`. This is `UNCLEAR` — it does not name the document and does not contain the word "approved." Processing it as an approval means the audit log has no defensible evidence of an explicit human decision.[^9_1]

***

## Subtask 4 — Correction Application *(Conditional, Loops)*

### What Is Happening

Each returned correction is applied to the manifest. This subtask loops: after corrections are applied, the review package is re-presented. The loop exits only when the response is `APPROVED`.[^9_1]

Corrections introduce new source material — the correction itself is a new input, attributed to the human director. Per FC-1, every field changed by a correction requires a new traceability entry.  The old traceability entry is not deleted — it remains as the record of the previous value. A new entry is added with `sourcetype: correction`.[^9_1]

**Correction record:**

```yaml
# correction-record-CR-1-01.yaml

correctionid: CR-1-01
step: 1
task: "1.5"
receivedat: "2026-03-07T03:28:00+11:00"
providedby: "Alex Chen"
corrections:
  - field: appetite
    previousvalue: small
    correctedvalue: medium
    basis: "Alex stated: 'Should probably be medium since I said 1-2 weeks'"
```

New traceability entry:

```yaml
- outputfield: appetite
  valuesummary: "medium"
  sourcetype: correction
  sourcereference: "CR-1-01, field: appetite, receivedat: 2026-03-07T03:28:00+11:00"
  supersedes: "previous entry for appetite (sourcetype: clarificationanswer, CE-1-01)"
```

After correction, the self-check from Task 1.4 Subtask 5 is re-run against the changed fields only. Re-running the full self-check is not required unless the correction changes a structurally significant field (e.g., a correction to `techstack` may invalidate other fields that depend on it).

### Skills Required to Do This to a High Standard

- **Correction scope containment** — applying exactly what was corrected, nothing more. If Alex says *"appetite should be medium"*, only `appetite` changes. Adjacent fields that the executor might judge should also change are not touched unless explicitly corrected.
- **New gap detection** — a correction might introduce a new gap. If Alex corrects `appetite` from `small` to `medium` but then adds *"actually, I think I might need a second page later"* — this is new scope information that may affect `outofscope`. The executor must assess whether the correction introduces any new BLOCKER entries and, if so, invoke Task 1.3 before re-presenting.
- **Traceability chain integrity** — the correction is a new source; the previous traceability entry is retained as history. Overwriting old entries breaks the audit trail.


### Examples of Excellence

Alex's correction response is processed as a formal correction record (`CR-1-01`). The manifest is updated. The traceability record has two entries for `appetite` — the original clarification-sourced entry and the correction-sourced entry, with the second explicitly noting it supersedes the first. The re-presented review package shows the corrected value and flags *"appetite updated from 'small' to 'medium' based on your correction"* so Alex can confirm the correction was applied correctly.

### Examples of Poor Performance

- Applying the correction and re-presenting without flagging what changed. Alex sees the same review package layout and may not notice the correction was applied, leading to a second approval that the executor cannot verify was informed.
- Deleting the old traceability entry for `appetite` and replacing it with the correction entry. This destroys the audit trail showing that `appetite: small` was the value at DRAFT time and why.
- Treating *"I might need a second page later"* as out-of-scope editorial commentary rather than potential new scope information. If the statement changes anything that should be in `constraints` or `outofscope`, it must be assessed as new input.


### Uncovered Questions / Gaps

**The loop has no defined exit condition for pathological cases.** The policy says there is no maximum number of correction cycles.  In practice, repeated corrections that keep changing the same field suggest either the human director is uncertain about their own intent, or the manifest presentation is confusing them. After a second correction to the same field, the executor should flag this as a potential `DECISION-REQUIRED` situation — the human director may need to make a decision rather than recall a fact.[^9_1]

**Corrections that add new required information are not addressed.** If Alex's correction adds a new constraint that implies a new `techstack` entry — for example, *"I also want to use Tailwind for utility classes"* — this is not a correction to an existing field; it is new content. New `techstack` entries require the same Task 1.1–1.3 processing as the original brief. The policy has no path for mid-review scope additions.

### Opportunities to Improve the Policy

- Define a correction loop health check: if the same field is corrected twice, the executor flags it as `UNSTABLE-FIELD` and requests the human director make a single definitive statement before re-presenting.
- Add a scope addition path: corrections that introduce new content (not corrections to existing values) are separated from corrections to existing fields and processed via a lightweight Task 1.1–1.3 mini-cycle before the manifest is updated.

***

## Subtask 5 — Approval Recording

### What Is Happening

The approval response has been classified as `APPROVED`. The executor must now execute the approval record per FC-4 Tier 1 — specifically:[^9_1]

1. Set `status: APPROVED` in the manifest
2. Set `approvedat` to the datetime of Alex's approval response
3. Set `approvedby` to `"Alex Chen"` — exactly as recorded in `humanactors`
4. Write the audit log entry
```yaml
# project-manifest.yaml (approval fields added)

status: APPROVED
approvedat: "2026-03-07T03:31:00+11:00"
approvedby: "Alex Chen"
```

```yaml
# audit log entry (FC-4 Tier 1)

actiontype: documentapproved
document: .framework/project-manifest.yaml
actor: "Alex Chen"
timestamp: "2026-03-07T03:31:00+11:00"
documentversion: DRAFT→APPROVED
approvalstatement: "Approved — appetite corrected to medium, rest is accurate"
```

The `approvalstatement` field records Alex's actual words — not a template phrase. This is evidence that the approval was deliberate, not automatic.[^9_1]

**Critical constraint:** `approvedat` is set to the timestamp of Alex's response — not the timestamp of the executor processing that response. These may differ. If there is a lag between response receipt and processing, the `approvedat` must reflect when Alex acted, not when the executor recorded it.

**The manifest is now sealed.** No further edits to field values are permitted after `status: APPROVED`. If an error is discovered after approval, the only valid path is to return the manifest to DRAFT and re-run Task 1.5 — not to apply a silent correction to an approved document.[^9_1]

### Skills Required to Do This to a High Standard

- **`approvedby` validation** — confirming that the name in `approvedby` matches exactly a `humandirector` entry in `humanactors`. A response from *"Alex"* (first name only) must be traced to *"Alex Chen"* in `humanactors` — not assumed. If the name doesn't match exactly, the approval is not valid.
- **Approval timestamp accuracy** — recording when Alex approved, not when the executor processed the approval. In synchronous interactions these are the same. In asynchronous workflows (email, document review) they may differ significantly.
- **Post-approval immutability enforcement** — after `status: APPROVED`, the executor must not write any further fields to the manifest. The approval is the terminal state. Any change, however minor, invalidates the approval.


### Examples of Excellence

The audit log entry contains Alex's actual approval statement verbatim. An independent reviewer reading the audit log can confirm that Alex explicitly approved the manifest, at a specific time, using words that constitute a deliberate decision rather than a passive acknowledgement.

### Examples of Poor Performance

- Recording `approvedat` as the timestamp of the executor's processing operation rather than Alex's response timestamp. In an automated system where responses are queued, this may be minutes or hours later. The FC-4 record must reflect when the human acted.
- Writing `approvedby: "humandirector"` (role title) rather than `"Alex Chen"` (named person). FC-4 requires attribution to a named human.  A role title is not attribution — it does not survive personnel changes and is not independently verifiable.[^9_1]
- Treating the approval as implicit from a positive clarification response earlier in the process. *"Great, Cloudflare Pages sounds right"* from Task 1.3 is not an approval of the manifest. The approval must be a deliberate response to a specific presentation of the DRAFT manifest.


### Uncovered Questions / Gaps

**The audit log is referenced but not defined in the Step 1 policy.** FC-4 requires an audit log entry, but the audit log itself — its location, format, and write mechanism — is defined elsewhere in the framework (the Nexus MCP server).  The Step 1 policy should reference the audit log specification rather than describing the entry format inline — otherwise the entry format may drift from the canonical audit log schema.[^9_1]

**The `approvalstatement` field is proposed here but not in the current FC-4 Tier 1 schema.** FC-4's required fields are `status`, `approvedby`, and `approvedat`. The approval statement — Alex's actual words — is mentioned as a concept but not a formal field. For a Tier 1 approval, the statement is evidence of intent. For a Tier 2 one-way decision, it is required.  Given that the Tier 1 approval is still consequential (it gates Step 2), requiring the statement as a Tier 1 field too would strengthen the evidence quality without adding significant burden.[^9_1]

### Opportunities to Improve the Policy

- Add `approvalstatement` as a required field in FC-4 Tier 1 — the actual words used, minimum 5 words, verbatim. This is a lightweight addition that substantially improves auditability.
- Add explicit guidance that `approvedat` records the human's action timestamp, not the executor's processing timestamp — and that in asynchronous workflows, these must be distinguished.

***

## The Correction Loop in Context

The most important structural property of Task 1.5 is that it may loop. Each loop cycle is a complete Subtask 2–4 pass. The loop is healthy when:

- Each cycle produces a smaller correction set
- Corrections address specific fields
- The human's responses are increasingly confident

The loop is unhealthy when:

- The same field is corrected repeatedly
- Corrections add new scope rather than fixing existing fields
- The human's responses become vaguer rather than more specific

Healthy loops close in one or two cycles. The policy's *"no maximum number of cycles"* is correct as a rule but should be accompanied by an escalation trigger: after three cycles without approval, the executor flags the loop as potentially pathological and surfaces the pattern to the human director explicitly.

***

## Done When

Task 1.5 is complete when all nine conditions are simultaneously true — the Step 1 DoD:[^9_1]

1. `project-manifest.yaml` exists at `.framework/project-manifest.yaml`
2. `status: APPROVED`
3. All required fields non-empty
4. Every field value traceable to a source in the brief or a recorded clarification or correction
5. No invented values
6. Every gap in `openquestions` with its classification
7. All contradictions resolved and recorded before drafting
8. `APPROVED` status set by Alex's explicit action — not by the executor
9. `approvedat` and `approvedby` present, consistent with `humanactors`

***

## Step 1 Complete

With Task 1.5 done, Step 1's output — `project-manifest.yaml` in APPROVED status — is the valid input to Step 2. The open questions register carries forward with its three unresolved entries (OQ-1-08, OQ-1-09, OQ-1-10). Step 2 reads the register at its start and reclassifies any entries whose severity changes in Step 2's context per FC-8.[^9_1]

***

**That completes the full Task 1.1 through 1.5 analysis for Step 1.** Would you like to compile the findings — gaps, policy improvements, and risks — into a consolidated list before moving on? Or proceed to the next phase of the work?

<div align="center">⁂</div>

[^9_1]: i-am-making-progress-in-creati-fuGLU8hCRLyka3xtBTVglA.md


---

# Step 1 Analysis — Consolidated Findings

Organised into five categories: decisions made, policy improvements, schema improvements, risks, and unresolved questions. Each finding is tagged with the task where it surfaced.

***

## 1. Decisions Made

Structural changes already agreed during this session. These are implemented — not recommendations.


| \# | Decision | Replaces | Source |
| :-- | :-- | :-- | :-- |
| D-01 | Task 1.1 output is `brief-inventory.yaml` — a single structured YAML document with four arrays (`statements`, `fields`, `non_mappable`, `contradictions`) | Separate intermediate documents per subtask | Task 1.1 |
| D-02 | Task 1.1 has four subtasks, each building one array of the output document; all subtasks carry a standing read-in-full precondition | Original five subtasks with separate outputs | Task 1.1 |
| D-03 | Gap severity vocabulary: `BLOCKER / WARNING / INFO` | `BLOCKING / WARNING / LOWRISK` | Task 1.2 |
| D-04 | Terminal states: `BLOCKER:RESOLVED` and `BLOCKER:CONFIRMED-UNKNOWN` | `BLOCKINGRESOLVED` / `BLOCKINGCONFIRMEDUNKNOWN` | Task 1.2 |
| D-05 | Task 1.2 has four subtasks — required fields, optional fields, contradictions, and non-mappable statements | Three subtasks (no non-mappable path) | Task 1.2 |
| D-06 | Task 1.2 creates the open questions register (`open-questions-register.yaml`) — this IS Task 1.2's output, not a separate intermediate "gap list" | Policy referred to a "two-tier gap list" without naming it as the register | Task 1.2 |
| D-07 | Manifest artefact format: `project-manifest.yaml` and `project-manifest.traceability.yaml` | `project-manifest.md` | Task 1.4 |
| D-08 | FC-2 Gate 3 addition: a REQUIRED schema field that cannot be validly populated from the current brief is BLOCKER regardless of downstream step dependency | Gate 3 did not exist | Task 1.2 |


***

## 2. Step 1 Policy Improvements

Recommended changes to the Step 1 policy document, by task.

### Task 1.1

- **P-01** Add a `gap_type` field to the `fields` array in `brief-inventory.yaml`: `ABSENT`, `AMBIGUOUS-INCOMPLETE` (partial information), `AMBIGUOUS-FORMAT` (information present but wrong form). This distinction propagates to Task 1.3 question formulation — absent fields require *"what is your X?"*; format-ambiguous fields require *"you said X — which valid value best matches?"*
- **P-02** Specify that contradiction detection must scan across all sections of the brief, not only between required fields — contradictions can span required and optional sections.
- **P-03** Add a `POTENTIAL-CONTRADICTION` classification for contradictions that can only be confirmed with domain expertise. Classified as WARNING with a `contradiction_flag: true` annotation. Escalated to BLOCKER if confirmed during clarification. (See also FC-2 improvement below.)


### Task 1.2

- **P-04** Add explicit instruction that Gate 1 requires the executor to have loaded Step 2 and Step 3 policy documents as reference material. Without this, Gate 1 is guesswork. State this as a required input to Task 1.2.
- **P-05** Add `linked_questions` as a required field in the open questions register schema — a machine-readable array, not just a text note. Task 1.3 queries this field directly to detect consolidation opportunities.
- **P-06** Add `schema_gap_flag: true` as an optional field in the register for WARNING entries that represent missing manifest schema fields. Creates a feedback loop for manifest template evolution.
- **P-07** Add Subtask 4 (non-mappable classification) explicitly to the Task 1.2 policy definition. Currently absent — non-mappable statements have no classification path and silently disappear.


### Task 1.3

- **P-08** Add response classification as the first operation of Subtask 3 — before updating any register entry, classify each response as `RESOLVED`, `CONFIRMED-UNKNOWN`, or `DECISION-REQUIRED`. Define `DECISION-REQUIRED` path: entry remains BLOCKER, a decision-request record is created, step enters `AWAITING-DECISION` state.
- **P-09** Add instructional context rule to question formulation: a question may include a parenthetical command or reference that enables the human to retrieve the information (e.g., `run node --version`), provided it does not constitute a compound question or decision prompt.
- **P-10** Add linked entry propagation as an explicit step in Subtask 3: *"For each RESOLVED entry, query the register for all entries referencing this entry's `questionid` in their `linked_questions` field and apply the same resolution."*
- **P-11** Add a note that `resolutionnote` values may require mapping to valid enum values. This mapping is a named derivation — not invention — and must be recorded in the traceability record. Specifically: *"latest stable"* and equivalent deferred version references are valid RESOLVED responses but require a version-resolution derivation step at Task 1.4; the `resolutionnote` must flag this explicitly.
- **P-12** Specify the expected response format for the clarification exchange: human is asked to respond per-question, referencing the question number. This is guidance for processability, not a constraint on how the human writes.


### Task 1.4

- **P-13** Add Subtask 1 (Pre-Drafting Derivation Resolution) as the first explicit subtask: before any field is written, the executor reads all register entries for `resolutionnote` derivation flags and resolves them. Version lookups happen here, not during field population.
- **P-14** Add new gap detection during pre-drafting as an explicit instruction: if a field has no valid source during derivation resolution, a new register entry is created before drafting begins. Task 1.4 is a quality gate that catches Task 1.2 omissions.
- **P-15** Add selection criteria for `description` field assembly: *"Include project type, primary purpose, and key deliverable. Exclude constraints, deployment details, and named actors — these have dedicated fields."* Without this, two executors produce different descriptions from the same brief.
- **P-16** Clarify that the self-check runs before `status: DRAFT` is set — not after. Status DRAFT is the executor's assertion of completeness; setting it before the check inverts the purpose of the check.
- **P-17** Add re-check scope rule for the correction loop in Task 1.5: after a correction, the self-check re-runs against changed fields and any fields that depend on them — not the full check unless a structurally significant field changed.


### Task 1.5

- **P-18** Add summary generation with a deterministic rendering rule and a summary-vs-manifest validation check: every summary field value must match the corresponding manifest field exactly.
- **P-19** Add `UNCLEAR` as a third response classification alongside `APPROVED` and `RETURNED`. Define handling: identify the specific question that resolves the ambiguity; re-present with that question; `presentedat` timestamp does not change.
- **P-20** Define minimum explicit approval statement: the response must name the document and contain the word "approved" (case-insensitive). Freeform affirmation alone is insufficient.
- **P-21** Add a scope addition path for the correction loop: corrections that introduce new content (not corrections to existing values) are separated from value corrections and processed via a lightweight Task 1.1–1.3 mini-cycle before the manifest is updated.
- **P-22** Add a correction loop health check: if the same field is corrected twice, the executor flags it as `UNSTABLE-FIELD` and requests the human director make a single definitive statement before re-presenting.
- **P-23** Add a loop escalation trigger: after three cycles without approval, the executor explicitly surfaces the loop pattern to the human director rather than continuing silently.
- **P-24** Reference the audit log specification by path rather than defining the entry format inline — prevents the Task 1.5 entry format drifting from the canonical audit log schema.

***

## 3. Cross-Cutting Policy Improvements

Recommended changes to FC-1 through FC-9.


| \# | Policy | Improvement |
| :-- | :-- | :-- |
| CC-01 | FC-2 | Add Gate 3 to the classification rule (already D-08 — formalise in the FC-2 document) |
| CC-02 | FC-2 | Add `POTENTIAL-CONTRADICTION` as a WARNING-level flag: contradictions requiring domain expertise to confirm are WARNING with `contradiction_flag: true`; escalated to BLOCKER if confirmed during clarification |
| CC-03 | FC-2 | Add `gap_type` as a required field in the open questions register schema: `ABSENT`, `AMBIGUOUS-INCOMPLETE`, `AMBIGUOUS-FORMAT`, `CONTRADICTION`, `SCHEMA-GAP` |
| CC-04 | FC-2 | Add `linked_questions` as a required field in the register schema (machine-readable array) |
| CC-05 | FC-2 | Add `schema_gap_flag` as an optional boolean field in the register schema, with optional `candidate_field` |
| CC-06 | FC-3 | Add instructional context rule — parenthetical retrieval instructions are permitted in questions provided they are not compound questions or decision prompts |
| CC-07 | FC-3 | Add `DECISION-REQUIRED` as a formal third response classification alongside `RESOLVED` and `CONFIRMED-UNKNOWN`. Define path: entry remains BLOCKER; decision-request record created; step enters `AWAITING-DECISION` |
| CC-08 | FC-3 | Add response format guidance: human is asked to respond per-question, referencing the question number |
| CC-09 | FC-4 | Add `approvalstatement` as a required field in Tier 1 — the human's actual words, verbatim, minimum 5 words |
| CC-10 | FC-4 | Add explicit guidance that `approvedat` records the human's action timestamp, not the executor's processing timestamp; in asynchronous workflows these must be explicitly distinguished |


***

## 4. Manifest Schema Improvements

Recommended changes to the manifest template.


| \# | Improvement | Reason |
| :-- | :-- | :-- |
| S-01 | Add optional field `existingInfrastructure` (or `existingSetup`) | Infrastructure readiness (registered domain, existing hosting accounts, DNS control) has direct Step 2 consequences but no current schema field. Surfaced by S-13 in the case study |
| S-02 | Add optional field `successCriteria` | The human director's explicit success definition (*"live on domain, 90+ Lighthouse, contact form works, handoff-ready"*) has no schema field. Currently either lost or squeezed into `constraints` |
| S-03 | Clarify `techstack` vs `devenvironment` boundary for package managers | pnpm appeared in both `techstack` and `devenvironment` in the case study. The schema should specify whether package managers belong in one, the other, or both — and whether duplication is permitted |
| S-04 | Add scope definition for `referenceexamples` | Currently accepts named examples. The case study brief included names plus qualitative descriptors. The schema should specify whether descriptors are valid entries or overflow to non-mappable |
| S-05 | Add conditional sections table to the manifest template metadata | A lookup table mapping tech stack patterns to triggered optional sections (e.g., form handler reference → services section conditionally required; measurable performance target → performance_targets section required). Makes Subtask 2 of Task 1.2 a table lookup rather than a judgment call |
| S-06 | Change manifest format from `.md` to `.yaml` | Already D-07 — confirm in the manifest template definition |
| S-07 | Change `appetite` enum vocabulary to align with the schema documentation | The enum values (`small`, `medium`, `large`) should include their associated time range in the schema documentation to reduce the AMBIGUOUS-FORMAT gap category for this field |


***

## 5. Risks

Ordered by propagation distance — how far downstream does the failure travel before it surfaces.

### Silent failures (surface in Step 2 or later)

- **R-01** Technical contradiction (Workers vs Pages) resolved by domain knowledge rather than surfaced for human confirmation. The manifest records a deployment target that does not match the human's actual intent. Step 2's environment contract is built on a false premise. *(Task 1.1 / 1.2)*
- **R-02** `techstack` version gaps not classified as BLOCKER (Gate 1 applied without Step 2 knowledge). Step 2 either invents versions (FC-1 violation) or produces an incomplete contract. *(Task 1.2)*
- **R-03** Shadcn version not identified as a gap during Task 1.2 or 1.3. During Task 1.4 pre-drafting, the gap surfaces but is resolved by derivation with no register entry. Step 2 receives a version-derived stack entry with no provenance signal. *(Task 1.4)*
- **R-04** Non-mappable statement S-13 (Cloudflare account, DNS control) not classified in Task 1.2. Step 2 cannot confirm self-managed DNS readiness; may assume procurement is needed. *(Task 1.2)*
- **R-05** `integrationrequirements` (Formspree) classified as INFO rather than WARNING. Step 2 produces an incomplete services section with no signal that it is expected. Surfaces at Step 3 or implementation. *(Task 1.2)*


### Process integrity failures

- **R-06** Linked entries OQ-1-04 and OQ-1-05 not consolidated. Task 1.3 asks two questions about the same deployment target. Human answers inconsistently or pushes back. *(Task 1.3)*
- **R-07** OQ-1-05 (contradiction entry) not updated when OQ-1-04 is resolved. Register shows an unresolved BLOCKER contradiction despite the underlying issue being resolved. Task 1.4 reads it as still OPEN and blocks or escalates incorrectly. *(Task 1.3)*
- **R-08** `"latest stable"` written as a literal manifest value rather than flagged as a derivation requiring version resolution. Manifest violates the `techstack` format rule. *(Task 1.3 / 1.4)*
- **R-09** Traceability record written after the manifest is complete rather than field-by-field. Entries for multi-source fields (like `description`) are reconstructed from memory. FC-1 provenance cannot be independently verified. *(Task 1.4)*
- **R-10** `"looks good to me"` accepted as an explicit approval. Audit log has no defensible evidence of a deliberate human decision. FC-4 Tier 1 requirements not met. *(Task 1.5)*
- **R-11** `approvedat` recorded as executor processing timestamp rather than human response timestamp. In asynchronous workflows, this may misrepresent the timeline by hours. *(Task 1.5)*
- **R-12** Silent correction applied to an APPROVED manifest. The audit trail shows an approved document and a subsequent edit with no re-approval record — an integrity failure. *(Task 1.5)*


### Schema and quality failures

- **R-13** `appetite` field classified as non-BLOCKER (Gate 3 not applied). Task 1.3 is never triggered for it. Task 1.4 populates by inference — FC-1 violation. Manifest fails DoD 3. *(Task 1.2)*
- **R-14** Compound BLOCKER entry for `techstack` (versions, React, package manager combined). Task 1.3 asks one compound question. Human provides a paragraph answer. Task 1.4 must decompose it — reintroducing ambiguity that Task 1.1 had already resolved. *(Task 1.2)*
- **R-15** `description` field rewritten in cleaner language than the brief. The manifest is no longer a faithful restatement. Subtle editorial changes may alter scope in ways that surface as disputes during delivery. *(Task 1.4)*

***

## 6. Unresolved Questions

Items surfaced but not resolved in this session. Each is a candidate for a future policy decision or framework-level resolution.


| \# | Question | Source | Where it belongs |
| :-- | :-- | :-- | :-- |
| UQ-01 | How are multi-part briefs handled? (email thread + separate notes file — which is canonical; how are conflicts between sources treated?) | Task 1.1 | Step 0 or Step 1 policy |
| UQ-02 | How is external version lookup (npm registry, GitHub releases) handled when the agent cannot make external API calls? Options: `CONFIRMED-UNKNOWN`; major-version shorthand; block until human provides. | Task 1.4 | Step 1 policy / framework tool specification |
| UQ-03 | What is the `DECISION-REQUIRED` path in full? A mid-step escalation to a human decision gate is structurally different from the clarification protocol. It implies a `AWAITING-DECISION` step state not currently in the FC-9 state machine. | Task 1.3 | FC-3 / FC-9 |
| UQ-04 | What presentation medium does the clarification exchange and the Task 1.5 review use? The medium determines what "respond with an explicit approval" looks like in practice. | Task 1.3 / 1.5 | Platform configuration or Step 1 policy |
| UQ-05 | Should correction additions (new scope introduced during the Task 1.5 correction loop) trigger a full mini Task 1.1–1.3 cycle, or a lighter-weight path? The full cycle is correct in principle but may feel disproportionate for a single added constraint. | Task 1.5 | Step 1 policy |
| UQ-06 | Does the open questions register need a terminal `ACCEPTED-AS-KNOWN-GAP` state for gaps the human director explicitly acknowledges at Step 6 but accepts without resolving? This was referenced in FC-8 but not confirmed in the register schema. | FC-8 | Open questions register schema |
| UQ-07 | Should `approvalstatement` be added to FC-4 Tier 1 as well as Tier 2? Currently Tier 2 (one-way decisions) requires it; Tier 1 (accuracy confirmations) does not. The case for adding it to Tier 1 is auditability; the case against is proportionality. | Task 1.5 | FC-4 |
| UQ-08 | The `description` field selection criteria ("include project type, primary purpose, key deliverable") were proposed here but not formally decided. Should this be codified in the manifest template or left as a skill-file instruction for the executing agent? | Task 1.4 | Manifest template or Step 1 skill file |


***

## Summary Counts

| Category | Count |
| :-- | :-- |
| Decisions made (D) | 8 |
| Step 1 policy improvements (P) | 24 |
| Cross-cutting policy improvements (CC) | 10 |
| Manifest schema improvements (S) | 7 |
| Risks identified (R) | 15 |
| Unresolved questions (UQ) | 8 |
| **Total findings** | **72** |


---

# Session Retrospective


***

## What This Session Accomplished

Before identifying learnings, it's worth being precise about what was produced. This session:

- Wrote a realistic example brief with intentional, realistic gaps
- Fully analysed Tasks 1.1 through 1.5 of Step 1
- Made 8 structural decisions
- Produced 72 findings (24 policy improvements, 10 cross-cutting policy improvements, 7 schema improvements, 15 risks, 8 unresolved questions)
- Redesigned two artefact formats (`brief-inventory.yaml`, `project-manifest.yaml`)
- Added one entirely new task structure (Task 1.2 Subtask 4 — non-mappable classification)
- Added Gate 3 to FC-2
- Identified the open questions register as the canonical output of Task 1.2

That is a substantial output for a single session. The depth was appropriate — but it comes with a cost noted below.

***

## What Worked Well

**The case study brief was the right anchor.**
Every abstract policy question that could have been debated theoretically was instead grounded by a concrete example. The Workers/Pages contradiction, the Shadcn version gap, the Formspree ambiguity, the appetite enum mismatch — none of these would have surfaced with the same clarity from abstract analysis. The brief paid dividends through all five tasks.

**The "decisions before proceeding" gate worked.**
Pausing before Task 1.2 to ask *"are there decisions needed before we continue?"* caught two decisions (subtask structure and vocabulary) that would have undermined the Task 1.2 analysis if left unresolved. This gate should be applied at the start of every task in future sessions — not just between tasks.

**The standing output-quality challenge improved the work.**
Your challenge to the Subtask A "mental note" output was the most important intervention of the session. The resulting principle — *if there is no concrete output, there is no way to verify the subtask was done or measure how well it was done* — is now a design invariant for every subsequent subtask across all steps. Apply it proactively.

**The "single document with arrays" resolution for Task 1.1 was clean.**
Once the question shifted from "what does each subtask produce?" to "what does the consuming task need?", the YAML array structure became obvious. The consumer-first framing resolved a structural debate that had been circling.

**Deferring without losing.**
Several findings were genuinely out of scope (UQ-01 through UQ-08) but were captured rather than either prematurely resolved or dropped. The consolidated findings list is a clean handoff document for future sessions.

***

## What Didn't Work as Well

**Subtask analysis began before output format was settled.**
The initial Task 1.1 analysis produced a five-subtask structure with separate outputs before the output format question was asked. This required partial rework. Roughly a third of the Task 1.1 analysis was redone after the structural decisions were made. The cost was modest here; on more complex tasks it would be higher.

**Vocabulary was decided mid-session rather than first.**
`BLOCKING` was used extensively in the Task 1.1 analysis before the vocabulary decision (BLOCKER/WARNING/INFO) was made in the Task 1.2 discussion. This created a small inconsistency in the analysis record — the Task 1.1 section uses the old vocabulary, Tasks 1.2–1.5 use the new. In a policy document, this would require a cleanup pass.

**The agent/multi-agent question was raised but not fully resolved.**
The question of whether each subtask would be executed by a separate agent surfaced during Task 1.1 and was addressed (single agent for Task 1.1, with reasoning). But the question applies to Tasks 1.2 through 1.5 as well, and was not revisited. The agent roster question will surface again — it should be resolved systematically, not task by task.

**Findings accumulated without a running tally.**
The 72-finding compilation at the end was valuable, but there was no running record during the session. Several findings from Task 1.1 had to be reconstructed. A lightweight running log during analysis would make the final compilation faster and reduce reconstruction risk.

***

## Learnings for Future Sessions

These are the actionable changes to how we run the next sessions.

### On session structure

**L-01 — Start each task with three questions before any analysis:**

1. What is this task's output artefact? (name, format, location)
2. Which task or agent consumes it?
3. What does the consumer need from it?

These three questions resolve most structural debates before they arise. We arrived at them organically this session — next session, ask them first.

**L-02 — Make decisions explicit before analysis, not mid-analysis.**
Identify all decisions that would change the analysis if made differently. Make them. Then analyse. The "decisions before proceeding" gate worked well as a between-task check — apply it within tasks too, at the start of subtask design.

**L-03 — Maintain a running decisions log during the session.**
Format:

```
D-xx | Decision | Task | Replaces
```

Write to it each time a decision is made. The final compilation then verifies the log rather than reconstructing it.

**L-04 — Scope the session to a fixed number of tasks.**
This session covered five tasks (1.1–1.5) and produced 72 findings. That is at the upper limit of what can be compiled cleanly in one session. Future sessions should scope to 3–4 tasks with a compilation step at the end. Depth over breadth — a shallow analysis of six tasks is less valuable than a thorough analysis of four.

### On case study use

**L-05 — Carry the Meridian Consulting brief forward.**
The brief and its artefacts are now established:

- `brief-inventory.yaml` (conceptual)
- `open-questions-register.yaml` with nine entries (OQ-1-01 through OQ-1-09)
- `clarification-exchange-CE-1-01.yaml` (conceptual)
- `project-manifest.yaml` in APPROVED status

Step 2's analysis should use these as input — not start fresh. The carry-forward will surface Step 2 gaps that would be invisible with a clean-slate brief.

**L-06 — Introduce deliberate edge cases.**
The Meridian brief was a good first case study but all its gaps resolved cleanly in Task 1.3. Future analysis should introduce at least one `CONFIRMED-UNKNOWN` outcome and one `DECISION-REQUIRED` outcome — these paths exist in the policy but were never exercised in this session. The untested paths are where the real policy gaps hide.

### On design principles

**L-07 — Apply the no-unverifiable-output invariant proactively.**
*If there is no concrete output, there is no way to verify the subtask was done or measure how well it was done.* Before finalising any subtask definition, ask: what is the output? Is it a named artefact or a named section of a named artefact? If the answer is "a mental note" or "an internal assessment," the subtask needs redesign.

**L-08 — Ask "who reads this?" for every artefact.**
The answer determines format, structure, and level of detail. `brief-inventory.yaml` → agent only → flat arrays with IDs. `project-manifest.yaml` → agent + human → structured YAML with rendered summary at human gate. This question resolves format debates in seconds.

**L-09 — The consumer-first principle applies to questions too.**
FC-3's question formulation rules were designed from the sender's perspective (one question, 25 words, named by field). The session surfaced that questions also need to be designed from the receiver's perspective: what format of response does this question produce, and can Task 1.3 process that response format? Design questions and their expected responses together.

### On framework alignment

**L-10 — Check each design decision against the framework principles explicitly.**
Several findings in this session (R-01, R-02, R-13) are violations of FC-1 or P3 that an agent following the policy could commit. The policy improvements are designed to prevent them — but the right test for each improvement is: *does this make the violation structurally impossible, or does it only make it less likely?* P3 says safety is built in, not hoped for. Preference structural prevention (FC-7's approach) over policy-stated rules wherever possible.

**L-11 — The "is this a policy rule or a skill-file instruction?" distinction matters.**
Several proposed improvements in this session (description field selection criteria, question formulation guidance) could live in the policy document or in the executing agent's skill file. The distinction: policy rules are invariants that any implementation must satisfy; skill-file instructions are the "how" of satisfying them. Keep policy documents lean — put the "how" in skill files.

***

## Forward State

What the next session inherits:


| Item | State |
| :-- | :-- |
| Step 1 policy analysis | Complete — 72 findings documented |
| Case study brief | Established — Meridian Consulting |
| Case study artefacts | Conceptually complete through Step 1 |
| Open questions register | 3 unresolved entries (OQ-1-08, OQ-1-09, OQ-1-10) carrying into Step 2 |
| Decisions D-01 through D-08 | Made — should be written into policy before Step 2 analysis begins |
| Unresolved questions UQ-01 through UQ-08 | Deferred — review at start of next session to confirm correct deferral destination |

**Recommended next session sequence:**

1. Review UQ-01 through UQ-08 — confirm deferral destinations, close any that can be decided quickly
2. Confirm D-01 through D-08 are reflected in the policy documents (or note them as pending policy updates)
3. Apply L-01 through L-03 as session operating rules
4. Begin Step 2 analysis using the Meridian case study artefacts as input

---

# Let's continue on with Task 1.2

Are their questions we need to answer/decisions to be made first?
What is our plan for analysing the subtasks?

Yes, there are a few things to lock in first, and we should tighten the plan for how we’ll walk Task 1.2 this time.

***

## Decisions / Questions to Settle Before Continuing

These are small but important; each one changes how we talk about the subtasks.

1. **Terminology for gap classes**
    - The policy doc still says: `BLOCKING / WARNING / LOWRISK` and “two-tier gap list (BLOCKING vs OPENQUESTIONS)”.[^12_1]
    - In our last session we converged on:
        - Severity: **BLOCKER / WARNING / INFO** (3 tiers).
        - Blocking status: BLOCKER vs non-blocking (WARNING/INFO) instead of “OPENQUESTION” as a separate type.
    - **Decision to confirm now:**
        - Use `BLOCKER / WARNING / INFO` as the vocabulary.
        - Treat “OPENQUESTION” as a *status/role* (non-blocking and carried in the register), not a separate severity label.
2. **What exactly is the output of Task 1.2?**
    - Policy says: “Output: a two-tier gap list” but FC-8 defines a shared open-questions register file at `.framework/open-questions-register.md`.[^12_1]
    - We implicitly decided last time that:
        - Task 1.2 **creates and populates** the shared open questions register.
    - **Decision to confirm now:**
        - Task 1.2’s output is `open-questions-register` (we’ll treat it as YAML), not a separate ad-hoc “gap list”.
3. **What does Task 1.2 consume as input?**
    - Policy: “Input: Classified inventory from Task 1.1.”[^12_1]
    - We redefined Task 1.1’s output as `brief-inventory.yaml` with:
        - `statements[]`
        - `fields[]` (field, required, coverage, supporting_statements)
        - `non_mappable[]`
        - `contradictions[]`
    - **Decision to confirm now:**
        - Task 1.2 input is exactly that structure; all classification work is expressed as queries over those arrays.
4. **Do we treat non-mappable statements in Task 1.2?**
    - Policy originally only mentioned: required, optional, contradictions.[^12_1]
    - We saw non-mappable items can have real downstream impact (e.g. infrastructure readiness) and must not disappear.
    - **Decision to confirm now:**
        - Add a fourth subtask to Task 1.2 for `non_mappable` classification, and have it create register entries (usually WARNING/INFO, possibly with `schema_gap_flag`).

If you’re happy with those four, we can treat them as fixed and proceed.

***

## Plan for Analysing Task 1.2 Subtasks (This Session)

We’ll reuse the structure that worked well for 1.1, but be stricter about sequencing and outputs.

### Step 0 — Restate Task 1.2 in our own words

- From policy: “Which gaps are blocking and which can be surfaced as open questions?”[^12_1]
- We’ll restate that as:
    - **“Given `brief-inventory`, produce a first version of `open-questions-register` with one entry per gap, each with classification and impact, ready for Task 1.3 to convert into questions.”**

We’ll sanity-check that framing against the policy text before we move on.

***

### Step 1 — Nail the artefacts for Task 1.2

We’ll define these concretely before touching subtasks:

- **Input artefact:** `brief-inventory.yaml`
    - Confirm its shape (statements/fields/non_mappable/contradictions).
- **Output artefact:** `open-questions-register.yaml`
    - Based on the FC-8 schema, we’ll adapt fields to our decisions:
        - `questionid`
        - `field`
        - `gap`
        - `gap_type` (ABSENT, AMBIGUOUS-INCOMPLETE, AMBIGUOUS-FORMAT, CONTRADICTION, SCHEMA-GAP)
        - `impact`
        - `raisedbystep`
        - `currentowner`
        - `classification` (BLOCKER/WARNING/INFO)
        - `resolutionstatus` (initially OPEN/UNRESOLVED)
        - timestamps and any flags (`schema_gap_flag`, `linked_questions`, etc.)[^12_1]

We’ll check FC-8 to align with its base schema and only extend, not break it.[^12_1]

***

### Step 2 — Analyse each subtask in turn

For each of the four subtasks, we’ll apply a consistent pattern:

1. **Define the subtask cleanly**
    - What question it answers.
    - Which slice of `brief-inventory` it operates on.
    - What it writes to `open-questions-register`.
2. **Walk through with the Meridian example**
    - Apply it concretely to our case brief:
        - Required fields with ABSENT/AMBIGUOUS coverage.
        - Optional fields with ABSENT/AMBIGUOUS coverage.
        - Contradictions list.
        - Non-mappable statements.
    - Because we already did an informal pass, this time we’ll:
        - Re-check any assumptions that changed with your new understanding.
        - Adjust the example entries to reflect the vocabulary and schema decisions above.
3. **Extract “skills required” and “failure modes”**
    - For each subtask:
        - What the executor needs to know (e.g. Step 2 requirements to apply “would Step 2 fail?”).
        - Typical mistakes (e.g. merging multiple gaps into one register entry).
4. **Note any cross-cutting policy implications**
    - If a subtask leans on FC-2/FC-3/FC-8 in a way they don’t currently specify, we capture that as a policy improvement (not re-argue the whole thing, just note it).

Concretely, the four subtasks we’ll walk:

1. **Subtask 1 — Required fields**
    - Input: `fields[]` where `required: true` and `coverage ∈ {ABSENT, AMBIGUOUS-*}`.
    - Operation: apply Gate 1 and Gate 3 of FC-2:
        - Gate 1: would Step 2/3 fail or be materially wrong? → BLOCKER.
        - Gate 3: REQUIRED and no valid value possible from brief → BLOCKER.
        - Else: WARNING/INFO depending on quality impact.
    - Output: one register entry per gap.
2. **Subtask 2 — Optional fields**
    - Input: `fields[]` where `required: false` and `coverage ∈ {ABSENT, AMBIGUOUS-*}`.
    - Operation:
        - Use conditional requirement rules (e.g. tech stack implies services section).
        - Apply FC-2 Gates 2/3 for WARNING vs INFO.
    - Output: register entries for optional-field gaps.
3. **Subtask 3 — Contradictions**
    - Input: `contradictions[]`.
    - Operation:
        - Each contradiction becomes BLOCKER (no downgrade).
        - If it references a field that already has an entry from Subtask 1/2, set up `linked_questions`.
    - Output: contradiction entries, plus linkages.
4. **Subtask 4 — Non-mappable statements**
    - Input: `non_mappable[]`.
    - Operation:
        - Decide whether each item has a *specific* downstream consequence.
        - Classify as WARNING/INFO and optionally flag `schema_gap_flag`.
    - Output: register entries for information with downstream impact or schema gaps.

***

### Step 3 — Sanity-check Task 1.2 as a whole

After we’ve done the four subtasks:

- Verify that:
    - Every ABSENT/AMBIGUOUS field in `brief-inventory.fields` is represented in the register.
    - Every `contradictions[]` item has a BLOCKER entry.
    - Every `non_mappable[]` item is either in the register or explicitly deemed to have no downstream consequence.
- Check that `open-questions-register.yaml` is in a shape Task 1.3 can use directly (no extra transformation layer).
- Identify any remaining design questions specifically about Task 1.2 (as opposed to FC-2/FC-8).

***

If you’re good with:

- the four decisions at the top, and
- this three-step plan for Task 1.2,

then next message I’ll treat those as fixed and start with Step 0 (restating Task 1.2) and Step 1 (pinning down the input/output artefacts more crisply).

<div align="center">⁂</div>

[^12_1]: i-am-making-progress-in-creati-fuGLU8hCRLyka3xtBTVglA.md


---

## Step 0 — Task 1.2 Restated

The policy asks: *"Which gaps are blocking and which can be surfaced as open questions?"*[^13_1]

That framing is deceptively narrow. The real job is:

> **Given `brief-inventory.yaml`, produce `open-questions-register.yaml` — one entry per gap, classified by severity, impact-described, and structured precisely for Task 1.3 to convert into clarification questions or carry forward as known gaps.**

Three things distinguish this from the policy's description:

- "gap list" is the register — not a separate intermediate document
- The register is created here and persists through all six steps per FC-8[^13_1]
- The question is not just BLOCKER vs non-BLOCKER — it is a three-tier classification with specific entry structure

***

## Step 1 — Artefacts

### Input: `brief-inventory.yaml`

Confirmed shape from Task 1.1:

```yaml
statements:        # atomic declarative statements from the brief
  - id: S-xx
    text: "..."
    clarity: CLEAR | AMBIGUOUS
    candidate_fields: [field_name, ...]

fields:            # one entry per manifest schema field
  - field: fieldname
    required: true | false
    coverage: PRESENT | ABSENT | AMBIGUOUS-INCOMPLETE | AMBIGUOUS-FORMAT
    supporting_statements: [S-xx, ...]

non_mappable:      # statements with no schema field association
  - statement_id: S-xx
    downstream_note: "..."

contradictions:    # conflicting statement pairs
  - id: C-xx
    statement_ids: [S-xx, S-xx]
    description: "..."
    affected_fields: [fieldname, ...]
```

Task 1.2 queries each array. No transformation is needed — the arrays map directly to the four subtasks.

***

### Output: `open-questions-register.yaml`

Filed at: `.framework/open-questions-register.yaml`

Created by Task 1.2. Owned by the bootstrap process through Step 6.

FC-8 defines the base schema.  We extend it with the fields confirmed in our session decisions:[^13_1]

```yaml
# open-questions-register.yaml
# Created: Step 1, Task 1.2
# Last modified by step: 1
# Persists through: Steps 1–6

questions:
  - questionid: OQ-{step}-{seq}    # e.g. OQ-1-01 — immutable once set
    field: fieldname | null         # null for non-mappable/schema-gap entries
    gap_type:                       # ABSENT | AMBIGUOUS-INCOMPLETE |
                                    # AMBIGUOUS-FORMAT | CONTRADICTION | SCHEMA-GAP
    gap: "one sentence"             # immutable once set
    impact: "one sentence"          # names the specific downstream field or DoD criterion
    source_statements: [S-xx]       # from brief-inventory.statements
    contradiction_ref: C-xx         # only for gap_type: CONTRADICTION
    classification: BLOCKER | WARNING | INFO
    linked_questions: [OQ-x-xx]     # machine-readable; populated when two entries share
                                    # an underlying question
    schema_gap_flag: true | false   # true when no manifest field exists for this information
    candidate_field: fieldname      # when schema_gap_flag: true
    raisedbystep: 1                 # immutable once set
    lastupdatedbystep: 1
    currentowner: 1                 # step currently responsible for resolution
    resolutionstatus: OPEN          # OPEN | RESOLVED | CONFIRMED-UNKNOWN |
                                    # DECISION-REQUIRED | ACCEPTED-AS-KNOWN-GAP
    resolutionnote: null            # populated at resolution
    resolvedbystep: null
    resolvedatexchange: null
```

Two fields from FC-8 warrant explicit confirmation:[^13_1]

- `raisedbystep` and `gap` are **immutable** — never changed after creation
- `classification` and `currentowner` are **mutable** — any subsequent step can reclassify upward or downward per FC-8 carry-forward rules

***

## Step 2 — Subtask Analysis

### Subtask 1 — Required Field Classification

**Slice:** `fields[]` where `required: true` and `coverage ∈ {ABSENT, AMBIGUOUS-INCOMPLETE, AMBIGUOUS-FORMAT}`

**Operation:** Apply FC-2 gates in order:

> **Gate 1:** Would proceeding without this, or getting it wrong, cause Step 2 or Step 3 to fail or produce a materially incorrect output? → **BLOCKER**
>
> **Gate 2:** Does absence have a known, specific downstream quality impact? → **WARNING**. Otherwise → **INFO**
>
> **Gate 3:** Is this a REQUIRED schema field that cannot be validly populated from the current brief? → **BLOCKER** regardless of Gates 1 and 2

Gate 3 is the safety net for fields where the downstream-failure test returns no — but the manifest would still be structurally invalid without them.

**Applied to the Meridian brief:**


| Field | Coverage | Gap type | Gate reached | Classification | Why |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `techstack` — AstroJS version | AMBIGUOUS-INCOMPLETE | AMBIGUOUS-INCOMPLETE | Gate 1 YES | **BLOCKER** | Step 2 `framework.version` requires a specific value; inventing it violates FC-1 |
| `techstack` — Shadcn version | AMBIGUOUS-INCOMPLETE | AMBIGUOUS-INCOMPLETE | Gate 1 YES | **BLOCKER** | Same: Step 2 cannot specify a version that was never declared |
| `techstack` — React integration | AMBIGUOUS-INCOMPLETE | AMBIGUOUS-INCOMPLETE | Gate 1 YES | **BLOCKER** | Step 2 install commands and config entries cannot be enumerated for an undeclared dependency |
| `techstack` — package manager | AMBIGUOUS-INCOMPLETE | AMBIGUOUS-INCOMPLETE | Gate 1 YES | **BLOCKER** | Step 2 `runtime.packagemanager` and `runtime.installcommand` require a single confirmed value |
| `deploymenttarget` | AMBIGUOUS-INCOMPLETE | AMBIGUOUS-INCOMPLETE | Gate 1 YES | **BLOCKER** | Step 2 deployment section structure differs entirely between Workers and Pages |
| `devenvironment.runtime.version` | AMBIGUOUS-INCOMPLETE | AMBIGUOUS-INCOMPLETE | Gate 1 YES | **BLOCKER** | Step 2 `runtime.version` requires an exact or minimum version |
| `appetite` | AMBIGUOUS-FORMAT | AMBIGUOUS-FORMAT | Gate 3 YES | **BLOCKER** | REQUIRED field; "within a week" is not a valid enum value; manifest fails DoD 3 without a valid entry; Step 2 does not consume `appetite` so Gate 1 returns NO — Gate 3 catches it |

**Each gap is a separate entry.** The three `techstack` gaps are distinct gaps with distinct impacts, distinct source statements, and distinct clarification questions. Collapsing them into one entry degrades every task downstream.

**Register entries produced by Subtask 1:**

```yaml
- questionid: OQ-1-01
  field: techstack
  gap_type: AMBIGUOUS-INCOMPLETE
  gap: "AstroJS version not specified in brief"
  impact: "Step 2 framework.version cannot be completed; populating from assumed current-stable violates FC-1"
  source_statements: [S-04]
  classification: BLOCKER
  linked_questions: []
  schema_gap_flag: false
  raisedbystep: 1
  lastupdatedbystep: 1
  currentowner: 1
  resolutionstatus: OPEN

- questionid: OQ-1-02
  field: techstack
  gap_type: AMBIGUOUS-INCOMPLETE
  gap: "Shadcn/ui version not specified in brief"
  impact: "Step 2 cannot specify a component library version without a declared or confirmed value"
  source_statements: [S-04]
  classification: BLOCKER
  linked_questions: []
  schema_gap_flag: false
  raisedbystep: 1
  lastupdatedbystep: 1
  currentowner: 1
  resolutionstatus: OPEN

- questionid: OQ-1-03
  field: techstack
  gap_type: AMBIGUOUS-INCOMPLETE
  gap: "React integration implied by Shadcn dependency but not declared as an explicit stack entry"
  impact: "Step 2 install commands and config entries cannot be written for an undeclared dependency"
  source_statements: [S-04]
  classification: BLOCKER
  linked_questions: []
  schema_gap_flag: false
  raisedbystep: 1
  lastupdatedbystep: 1
  currentowner: 1
  resolutionstatus: OPEN

- questionid: OQ-1-04
  field: techstack
  gap_type: AMBIGUOUS-INCOMPLETE
  gap: "Package manager unconfirmed — npm stated as current default, pnpm mentioned as acceptable alternative"
  impact: "Step 2 runtime.packagemanager and runtime.installcommand require a single confirmed value"
  source_statements: [S-09]
  classification: BLOCKER
  linked_questions: []
  schema_gap_flag: false
  raisedbystep: 1
  lastupdatedbystep: 1
  currentowner: 1
  resolutionstatus: OPEN

- questionid: OQ-1-05
  field: deploymenttarget
  gap_type: AMBIGUOUS-INCOMPLETE
  gap: "Cloudflare Workers named but target may be Cloudflare Pages given static constraint"
  impact: "Step 2 deployment section structure and AstroJS output mode depend entirely on which Cloudflare product is intended"
  source_statements: [S-02]
  classification: BLOCKER
  linked_questions: [OQ-1-06]   # contradiction entry for same field — populated after Subtask 3
  schema_gap_flag: false
  raisedbystep: 1
  lastupdatedbystep: 1
  currentowner: 1
  resolutionstatus: OPEN

- questionid: OQ-1-06
  field: devenvironment
  gap_type: AMBIGUOUS-INCOMPLETE
  gap: "Node.js runtime version unknown — human stated they do not know the exact version"
  impact: "Step 2 runtime.version requires an exact or minimum version; cannot be written without it"
  source_statements: [S-11]
  classification: BLOCKER
  linked_questions: []
  schema_gap_flag: false
  raisedbystep: 1
  lastupdatedbystep: 1
  currentowner: 1
  resolutionstatus: OPEN

- questionid: OQ-1-07
  field: appetite
  gap_type: AMBIGUOUS-FORMAT
  gap: "Appetite stated as 'within a week' — not a valid enum value (valid: small / medium / large)"
  impact: "REQUIRED field cannot be validly populated; manifest fails DoD 3 regardless of Step 2 dependency"
  source_statements: [S-15]
  classification: BLOCKER
  linked_questions: []
  schema_gap_flag: false
  raisedbystep: 1
  lastupdatedbystep: 1
  currentowner: 1
  resolutionstatus: OPEN
```

**Seven BLOCKER entries. Subtask 1 is the most consequential subtask — mistakes here propagate directly into whether Task 1.3 asks the right questions.**

***

#### Skills Required

- **Step 2 and Step 3 schema knowledge as a loaded prerequisite.** Gate 1 cannot be applied accurately without knowing what Step 2 and Step 3 need field by field. This must be explicit in the executor's context card or skill file — the policy should not assume this knowledge is implicit.[^13_1]
- **One gap, one entry discipline.** Three separate `techstack` gaps produce three entries. The test: if two gaps would produce different clarification questions, they are different entries.
- **Gate 3 awareness.** Required field validity is an independent classification criterion — not covered by the downstream-failure test alone. An executor applying only Gates 1 and 2 misses `appetite`.
- **No resolution during classification.** Classifying AstroJS version as BLOCKER and simultaneously noting "AstroJS latest stable is 5.x" is two acts merged into one. Only the classification belongs here.


#### Failure Modes

- Single `techstack` entry: *"Tech stack versions and configuration are ambiguous."* One entry covers all four gaps. Task 1.3 asks one compound question. Human provides a paragraph answer. Task 1.4 must decompose it — re-establishing structure that should have been created here.
- `appetite` classified non-BLOCKER because Step 2 doesn't use it. Gate 3 not applied. Task 1.3 never asks about it. Task 1.4 invents a value. Manifest fails DoD 5.
- Shadcn version not identified as a distinct gap because "it'll be covered when we ask about AstroJS." Two questions are needed; one is asked; one gap reaches Task 1.4 unresolved and requires a derivation with no register backing.
- `deploymenttarget` classified PRESENT because "Cloudflare Workers" is explicitly stated. The ambiguity — that Workers may be the wrong product — requires domain knowledge to detect. An executor without it won't generate OQ-1-05.


#### Policy Improvements Flagged

- **P-04 (confirmed):** The policy must state explicitly that Gate 1 requires the executor to have loaded Step 2 and Step 3 policy documents as reference material. Without this, Gate 1 is guesswork.
- **P-01 (confirmed):** `gap_type` as a register field — distinguishes AMBIGUOUS-INCOMPLETE from AMBIGUOUS-FORMAT upstream, shaping question formulation in Task 1.3 without re-derivation.

***

### Subtask 2 — Optional Field Classification

**Slice:** `fields[]` where `required: false` and `coverage ∈ {ABSENT, AMBIGUOUS-INCOMPLETE, AMBIGUOUS-FORMAT}`

**Operation:** Apply Gates 2 and 3 only — Gate 1 is not applicable; optional fields are legally absent. The additional rule: **conditional requirement detection** — when the tech stack declaration implies an optional section, that section's fields become WARNING automatically regardless of Gate 2.

**Applied to the Meridian brief:**


| Field | Coverage | Conditional? | Classification | Reason |
| :-- | :-- | :-- | :-- | :-- |
| `integrationrequirements` | AMBIGUOUS-INCOMPLETE | YES — form handler referenced in S-08 | **WARNING** | Step 2 `services` section is conditionally required once a form handler is referenced; provider and method cannot be specified without confirmation |
| `existingassets` | ABSENT | NO | **INFO** | No bootstrap step uses existing assets; absence has no quality impact |
| `referenceexamples` — descriptors | PRESENT (field) but descriptors non-mappable | NO | Handled in Subtask 4 | Field is PRESENT; the overflow content lives in `non_mappable[]` |

**Register entries produced by Subtask 2:**

```yaml
- questionid: OQ-1-08
  field: integrationrequirements
  gap_type: AMBIGUOUS-INCOMPLETE
  gap: "Form handler provider tentative — Formspree mentioned but not confirmed"
  impact: "Step 2 services section conditionally required when form handler referenced; provider name and integration method cannot be specified until confirmed"
  source_statements: [S-08]
  classification: WARNING
  linked_questions: []
  schema_gap_flag: false
  raisedbystep: 1
  lastupdatedbystep: 1
  currentowner: 1
  resolutionstatus: OPEN

- questionid: OQ-1-09
  field: existingassets
  gap_type: ABSENT
  gap: "No existing assets declared in brief"
  impact: "No downstream bootstrap step requires existing assets; noted for completeness"
  source_statements: []
  classification: INFO
  linked_questions: []
  schema_gap_flag: false
  raisedbystep: 1
  lastupdatedbystep: 1
  currentowner: 1
  resolutionstatus: OPEN
```

**The conditional requirement rule is the critical skill for this subtask.** Without it, `integrationrequirements` is classified INFO because "it's an optional field." With it, it becomes WARNING because the brief's content has triggered a downstream obligation.

#### Skills Required

- **Conditional requirement detection.** Knowing which optional manifest sections become functionally required given a specific tech stack. For this brief: a form handler reference triggers the services section. This is domain knowledge that should be codified in the manifest template's metadata — a lookup table, not a judgment call.
- **INFO ≠ ignorable.** INFO entries enter the register, travel through all six steps, and are presented at Step 6. They receive the same structural rigour as BLOCKER entries. The only difference is they don't block drafting.
- **PRESENT field with non-mappable overflow.** `referenceexamples` is PRESENT at the field level — no entry needed here. The overflow design descriptors live in `non_mappable[]` and are picked up in Subtask 4. The executor must not try to handle both concerns in Subtask 2.


#### Failure Modes

- Classifying `integrationrequirements` as INFO because "it's optional." The conditional requirement rule is missed. Formspree ambiguity reaches Step 2 unclassified. Step 2 produces an incomplete services section with no signal that one was expected.
- Generating no INFO entry for `existingassets`. Subtask 2's Done condition requires every optional field to have a register entry or an explicit "no entry needed" decision. Silently skipping ABSENT optional fields breaks the completeness check at Task 1.2's DoD.


#### Policy Improvements Flagged

- **S-05 (confirmed):** Add conditional sections table to the manifest template metadata. Maps tech stack patterns to triggered optional sections. Makes Subtask 2 a table lookup.
- **New — P-Subtask2-01:** The Done condition for Subtask 2 must require explicit confirmation that every optional field was assessed — not just that entries were created for the ones that triggered classification. An executor that silently skips ABSENT optional fields with "no impact" produces a register that appears complete but is not.

***

### Subtask 3 — Contradiction Classification

**Slice:** `contradictions[]`

**Operation:** Every entry becomes BLOCKER — no test, no gate, no downgrade.  Then: deduplication linking — if a contradiction involves a field that already has an entry from Subtasks 1 or 2, the entries are linked via `linked_questions`.[^13_1]

**Applied to the Meridian brief:**

The `contradictions` array has one entry:

```yaml
contradictions:
  - id: C-01
    statement_ids: [S-02, S-03]
    description: "Cloudflare Workers implies edge compute adapter (incompatible with AstroJS output:static);
                  static constraint requires output:static"
    affected_fields: [deploymenttarget, constraints]
```

`deploymenttarget` already has OQ-1-05. The contradiction entry becomes OQ-1-08 *(renumbered — the Shadcn entry now takes OQ-1-02 and the sequence shifts; for clarity let's use the next available ID)*. More precisely:

```yaml
- questionid: OQ-1-10
  field: deploymenttarget
  gap_type: CONTRADICTION
  gap: "Cloudflare Workers implies edge compute adapter incompatible with AstroJS output:static;
        static constraint requires output:static — both cannot be satisfied simultaneously"
  impact: "AstroJS output mode and adapter cannot be determined; Step 2 deployment section and
           framework section both blocked until resolved"
  source_statements: [S-02, S-03]
  contradiction_ref: C-01
  classification: BLOCKER
  linked_questions: [OQ-1-05]
  schema_gap_flag: false
  raisedbystep: 1
  lastupdatedbystep: 1
  currentowner: 1
  resolutionstatus: OPEN
```

And OQ-1-05 is updated:

```yaml
# OQ-1-05 updated after Subtask 3:
  linked_questions: [OQ-1-10]   # bidirectional
```

**The linkage is bidirectional.** OQ-1-05 references OQ-1-10 and OQ-1-10 references OQ-1-05. Task 1.3 queries `linked_questions` on every BLOCKER entry before formulating questions — finding this pair, it consolidates them into a single question rather than two.

#### Impact statement discipline for contradictions

A contradiction BLOCKER must name both competing interpretations and their downstream consequences — without choosing between them:

> *"If Cloudflare Workers: requires `@astrojs/cloudflare` adapter, AstroJS `output: server` or `hybrid` mode — incompatible with static constraint. If Cloudflare Pages: AstroJS `output: static`, no adapter required — consistent with static constraint."*

This is what Task 1.3 translates into a precise question. A vague impact statement (*"deployment target unclear"*) produces a vague question, which produces a vague answer, which produces an ambiguous manifest field.

#### Skills Required

- **No-downgrade discipline.** The most important skill. The executor may know that Cloudflare Pages is the right answer. That knowledge must not enter the classification or the impact statement.[^13_1]
- **Deduplication detection.** After creating OQ-1-10, the executor must check every `affected_field` against existing register entries and set `linked_questions` bidirectionally. This is a mechanical query, but only if the executor knows to perform it.
- **Two-interpretation impact statements.** The impact statement names both sides without choosing — giving Task 1.3 the raw material to formulate a question that produces a definitive answer.


#### Failure Modes

- Creating OQ-1-10 but not updating OQ-1-05's `linked_questions`. The linkage is unidirectional. Task 1.3 processes OQ-1-05 and formulates question Q-A. Then independently processes OQ-1-10 and formulates question Q-B. Alex receives two questions about the same underlying issue.
- Detecting the Workers/static contradiction but classifying it as WARNING rather than BLOCKER. The no-downgrade rule is the protection against this. If the executor applies domain knowledge (*"it's probably just a terminology confusion — likely not a real constraint conflict"*), the contradiction is downgraded and never reaches the human.[^13_1]
- Writing the impact statement from one perspective only: *"The static constraint cannot be met on Cloudflare Workers."* This presupposes that "static" is correct and Workers is wrong — the human hasn't confirmed this. The executor has silently resolved the contradiction.


#### Policy Improvements Flagged

- **P-03 (confirmed):** Add `POTENTIAL-CONTRADICTION` as a WARNING-level flag for contradictions that require domain expertise to confirm — enters the register with `contradiction_flag: true`, escalated to BLOCKER if confirmed during clarification.
- **New — P-Subtask3-01:** Make deduplication linking an explicit named step in the Subtask 3 procedure, not an implied consequence. *"For each contradiction entry, query the register for existing entries whose `field` appears in the contradiction's `affected_fields`. Set `linked_questions` bidirectionally."*

***

### Subtask 4 — Non-Mappable Statement Classification

**Slice:** `non_mappable[]`

**Operation:** Each non-mappable statement is assessed for downstream consequence and classified. Unlike Subtasks 1–3, this subtask may produce zero entries — some non-mappable statements are genuinely out of scope for the manifest and carry no downstream consequence. But the assessment must still be performed and recorded; an executor that skips non-mappable statements and produces zero entries without evidence of assessment has not completed this subtask.

**Classification test:**

> Does this statement represent information with a specific, named downstream consequence in Steps 2–6?
> - YES, consequence is specific and nameable → **WARNING**
> - YES, consequence is plausible but indirect → **INFO**
> - NO, and it represents a schema gap → **INFO** with `schema_gap_flag: true`
> - NO downstream consequence and no schema gap → No register entry; record explicit "no entry" decision

**Applied to the Meridian brief:**


| Statement | Text | Classification | Reason |
| :-- | :-- | :-- | :-- |
| S-13 | "Cloudflare account active, DNS control available" | **WARNING** | Step 2 deployment section cannot confirm self-managed DNS unless this is recorded; executor may assume DNS procurement is needed |
| S-16 | "Handoff to a developer friend later" | **INFO + schema_gap_flag** | Maintainability requirement; no manifest field exists; plausible downstream impact on Step 3 role configuration (code quality standards); candidate field `successCriteria` |
| S-17 | Design intent descriptors (typography, whitespace) | **INFO + schema_gap_flag** | No manifest field; indirect impact on Step 4 pattern seeding; candidate field `designIntent` or extension to `referenceexamples` |

**Register entries produced by Subtask 4:**

```yaml
- questionid: OQ-1-11
  field: null
  gap_type: SCHEMA-GAP
  gap: "Infrastructure readiness present in brief — Cloudflare account active, DNS control confirmed — but no manifest field exists"
  impact: "Step 2 deployment section may incorrectly assume DNS procurement is needed; self-managed DNS readiness not formally recorded"
  source_statements: [S-13]
  classification: WARNING
  linked_questions: []
  schema_gap_flag: true
  candidate_field: existingInfrastructure
  raisedbystep: 1
  lastupdatedbystep: 1
  currentowner: 1
  resolutionstatus: OPEN

- questionid: OQ-1-12
  field: null
  gap_type: SCHEMA-GAP
  gap: "Maintainability requirement present in brief ('handoff to a developer friend') but no manifest field exists"
  impact: "Step 3 role configuration cannot scope code quality standards without a recorded requirement; indirect downstream impact"
  source_statements: [S-16]
  classification: INFO
  linked_questions: []
  schema_gap_flag: true
  candidate_field: successCriteria
  raisedbystep: 1
  lastupdatedbystep: 1
  currentowner: 1
  resolutionstatus: OPEN

- questionid: OQ-1-13
  field: null
  gap_type: SCHEMA-GAP
  gap: "Design intent descriptors present in brief (typography, whitespace) but exceed referenceexamples field schema"
  impact: "Step 4 pattern seeding would benefit from explicit design intent; current schema has no field for it"
  source_statements: [S-17]
  classification: INFO
  linked_questions: []
  schema_gap_flag: true
  candidate_field: designIntent
  raisedbystep: 1
  lastupdatedbystep: 1
  currentowner: 1
  resolutionstatus: OPEN
```


#### Skills Required

- **Schema gap recognition.** Distinguishing *"this information has no current schema field"* (a schema gap worth recording) from *"this information doesn't belong in the manifest at all"* (genuinely out of scope, no entry needed). S-13 is a schema gap. S-17 is also a schema gap but less urgent. Pure pleasantries or conversational filler in a brief would be genuinely out of scope.
- **Downstream step awareness.** S-13 is WARNING only if the executor knows Step 2 has a deployment section that references DNS readiness. Without that knowledge, it would be classified INFO or skipped entirely.
- **Completeness over selectivity.** The executor must not selectively pick "important-looking" non-mappable statements. Every entry in `non_mappable[]` gets an assessment. Entries with no register output have an explicit no-entry decision recorded — even if that record is only in the executor's worklog.


#### Failure Modes

- Skipping this subtask entirely. The most common failure mode — it is the newest subtask, it produces no manifest field values, and it feels like optional tidying. But S-13 has a concrete Step 2 consequence. If it disappears here, it surfaces at Step 2 as an unrecorded assumption.[^13_1]
- Classifying S-13 as INFO because "account readiness isn't a gap in the brief." The question is not whether the brief is missing something — it is whether information in the brief has a downstream consequence that no schema field captures. S-13 provides information that Step 2 needs but cannot retrieve from the manifest.
- Creating INFO entries for S-16 and S-17 without `schema_gap_flag: true`. The flag is what creates a feedback loop for schema improvement. Without it, the information is in the register but there's no signal to the manifest template maintainer that these entries represent addressable schema gaps.


#### Policy Improvements Flagged

- **P-07 (confirmed):** Add Subtask 4 explicitly to the Task 1.2 policy.
- **New — P-Subtask4-01:** The Done condition for Subtask 4 must require the executor to confirm explicitly that every entry in `non_mappable[]` was assessed — either producing a register entry or recording a documented no-entry decision. Silent skipping is not detectable without this requirement.
- **CC-05 (confirmed):** `schema_gap_flag` and `candidate_field` as optional register fields, creating a structured feedback loop for manifest template evolution.

***

## Step 3 — Sanity Check

### Completeness check against `brief-inventory.yaml`

| Source array | Entries in brief-inventory | Register entries produced | All accounted for? |
| :-- | :-- | :-- | :-- |
| `fields[]` — required, non-PRESENT | 7 gaps across 5 fields | OQ-1-01 through OQ-1-07 (7 entries) | ✓ |
| `fields[]` — optional, non-PRESENT | 2 gaps | OQ-1-08 (WARNING), OQ-1-09 (INFO) | ✓ |
| `contradictions[]` | 1 entry (C-01) | OQ-1-10 (BLOCKER, linked to OQ-1-05) | ✓ |
| `non_mappable[]` | 3 entries | OQ-1-11 (WARNING), OQ-1-12 (INFO), OQ-1-13 (INFO) | ✓ |

**Total register entries: 13.** Every source entry is accounted for.

### Task 1.3 readiness check

Task 1.3 needs to:

1. Query all BLOCKER, OPEN entries → can do: filter `classification: BLOCKER`, `resolutionstatus: OPEN`
2. Detect linked groups → can do: query `linked_questions` on each BLOCKER entry
3. Formulate questions shaped by gap type → can do: `gap_type` field drives question format
4. Know the impact of each gap → present in `impact` field per entry
5. Know which brief statement supports each gap → `source_statements` per entry

The register is directly consumable by Task 1.3. No intermediate transformation needed.

### Design questions specific to Task 1.2

Three remain:

**DQ-01 — When does the `linked_questions` field get populated for Subtask 1 entries?**
OQ-1-05 needs `linked_questions: [OQ-1-10]` — but OQ-1-10 doesn't exist until Subtask 3 runs. This means `linked_questions` on Subtask 1 entries is only fully populated *after* Subtask 3 completes. Two options:

- Option A: Subtask 3 explicitly updates prior entries' `linked_questions` as part of its deduplication step.
- Option B: `linked_questions` is populated bidirectionally at the end of Subtask 3 in a single pass over all entries created so far.

Option B is cleaner — a single linking pass after all entries exist, rather than retroactive updates during Subtask 3. This should be added as a named step at the end of Subtask 3.

**DQ-02 — Is INFO entry OQ-1-09 (`existingassets: ABSENT`) worth creating?**
The argument for: completeness — every optional field was assessed. The argument against: it adds register noise with no actionable consequence. INFO entries with genuinely zero downstream impact create entries that every subsequent step must skip. The Done condition requiring all optional fields to be assessed could be satisfied by a worklog note rather than a register entry. This is a policy clarity question — does the register hold only actionable findings, or does it hold the complete assessment record?

**DQ-03 — The register currently has 13 entries from a fairly simple brief. How does this scale?**
A more complex brief with ten tech stack entries and multiple integration requirements could produce 30+ entries. Task 1.3 batching logic becomes more important at that scale. This is not a problem to solve now, but it should be noted as a future policy concern — specifically whether there is a maximum batch size for FC-3's clarification exchange, and whether BLOCKER entries can be prioritised before WARNING entries.

***

## Done When — Task 1.2

Task 1.2 is complete when all six conditions are simultaneously true:

1. `open-questions-register.yaml` exists at `.framework/open-questions-register.yaml`
2. Every `fields[]` entry with coverage ABSENT or AMBIGUOUS has a corresponding register entry
3. Every `contradictions[]` entry has a BLOCKER register entry
4. Every `non_mappable[]` entry has either a register entry or a documented no-entry decision in the executor's worklog
5. All register entries where `linked_questions` should be populated have been updated — specifically after Subtask 3's linking pass
6. All entries have `resolutionstatus: OPEN` and `currentowner: 1`

***

**DQ-01 has a clear answer (Option B) and should be decided before we proceed to Task 1.3. DQ-02 and DQ-03 can be deferred. Shall I make that call on DQ-01 and proceed to Task 1.3?**

<div align="center">⁂</div>

[^13_1]: i-am-making-progress-in-creati-fuGLU8hCRLyka3xtBTVglA.md


---

## Step 0 — Task 1.3 Restated

The policy asks: *"Can each blocking gap be resolved by asking humandirector directly?"*[^14_1]

More precisely:

> **Given `open-questions-register.yaml` containing BLOCKER entries, produce a clarification exchange record and update the register — so that every BLOCKER entry exits this task with either a specific, usable value or a `CONFIRMED-UNKNOWN` status. Task 1.4 must be able to populate every required manifest field from the register alone after this task completes.**

The policy's framing is correct but incomplete. "Can it be resolved?" is the question. "A complete, usable value per BLOCKER field, evidenced by a timestamped exchange record" is the output.

***

## Step 1 — Artefacts

### Input: `open-questions-register.yaml`

Task 1.3 reads only the BLOCKER slice:

```yaml
# Filter applied at start of Task 1.3:
classification: BLOCKER
resolutionstatus: OPEN
```

From our Meridian register, that is seven entries: OQ-1-01 through OQ-1-07, plus OQ-1-10 (the contradiction entry). OQ-1-05 and OQ-1-10 are linked — this is the first thing Task 1.3 must detect.

***

### Outputs

**Output 1 — `clarification-exchange-CE-1-01.yaml`**

Filed at: `.framework/clarifications/CE-1-01.yaml`

The exchange record per FC-3.  Created at the moment of sending — not after the response arrives.[^14_1]

```yaml
exchangeid: CE-1-01
step: 1
initiatedat: "..."      # set at moment of delivery
questions: [...]        # populated in Subtask 1
respondedat: null       # set when response arrives
responses: [...]        # populated in Subtask 3
```

**Output 2 — `open-questions-register.yaml` (updated)**

Every BLOCKER entry exits this task with one of:

- `resolutionstatus: RESOLVED` + `resolutionnote` containing the raw response value
- `resolutionstatus: CONFIRMED-UNKNOWN` + `resolutionnote` recording what Alex said
- `resolutionstatus: DECISION-REQUIRED` + note recording that Alex has a conflict, not missing information

The register is the canonical record. The exchange record is the evidence. Task 1.4 reads the register.

***

## Step 2 — Subtask Analysis

### Subtask 1 — Question Preparation

**What is happening:**

The executor queries the register for all `classification: BLOCKER`, `resolutionstatus: OPEN` entries and performs two operations before writing any question.

**Operation A — Linked group detection**

For each BLOCKER entry, check `linked_questions`. Any pair sharing a link is consolidated — they share an underlying issue and must produce one question, not two.

From the Meridian register:

- OQ-1-05 (`deploymenttarget` — ambiguity) `linked_questions: [OQ-1-10]`
- OQ-1-10 (`deploymenttarget` — contradiction) `linked_questions: [OQ-1-05]`

These collapse into one question covering both the product ambiguity and the static constraint contradiction. Eight BLOCKER entries become **seven questions**.

**Operation B — Question formulation**

Each question is formulated per FC-3 rules:[^14_1]

- One sentence, maximum 25 words
- Specific to a single field — not compound
- Named by field, not by domain
- Accompanied by a one-sentence impact statement
- Question type shaped by `gap_type`:
    - `AMBIGUOUS-INCOMPLETE` → *"What is your X?"* — retrieving a missing value
    - `AMBIGUOUS-FORMAT` → *"You said X — which of these valid values best matches?"* — mapping to a valid form
    - `CONTRADICTION` → *"Which of these two options reflects your intent?"* — disambiguating conflict

Applied to the Meridian BLOCKER entries:

```
Technical gaps:

Q1. [OQ-1-01 | gap_type: AMBIGUOUS-INCOMPLETE]
    "Which version of AstroJS should this project use?"
    Impact: Required before the environment contract can specify framework.version.

Q2. [OQ-1-02 | gap_type: AMBIGUOUS-INCOMPLETE]
    "Which version of Shadcn/ui should this project use?"
    Impact: Required to specify the component library version in the environment contract.

Q3. [OQ-1-03 | gap_type: AMBIGUOUS-INCOMPLETE]
    "Should React be included as an explicit stack dependency for the Shadcn integration?"
    Impact: Required to enumerate all install commands and config entries in the environment contract.

Q4. [OQ-1-04 | gap_type: AMBIGUOUS-INCOMPLETE]
    "Which package manager should this project use — npm or pnpm?"
    Impact: Required before install command entries can be written in the environment contract.

Q5. [OQ-1-05 + OQ-1-10 | gap_type: AMBIGUOUS-INCOMPLETE + CONTRADICTION — consolidated]
    "Are you deploying to Cloudflare Pages (static file hosting) or Cloudflare Workers
    (edge compute)?"
    Impact: Determines the AstroJS output mode and adapter; the entire deployment section
    of the environment contract depends on this.

Q6. [OQ-1-06 | gap_type: AMBIGUOUS-INCOMPLETE]
    "What version of Node.js is installed in your development environment?
    Run `node --version` in your terminal to check."
    Impact: Required before the runtime section of the environment contract can be completed.

Scope gap:

Q7. [OQ-1-07 | gap_type: AMBIGUOUS-FORMAT]
    "Would you classify this project's appetite as small (days), medium (1–2 weeks),
    or large (multi-week)?"
    Impact: The manifest requires one of these three values; 'within a week' cannot be
    stored as-is.
```

**Note on Q5:** The consolidated question absorbs both entries. The impact statement does not attempt to explain the contradiction — it names the downstream consequence cleanly. The complexity of the contradiction (Workers vs static) is visible in the question's parenthetical descriptions; the human can infer the tension without the question spelling it out.

**Note on Q6:** Includes a terminal command as instructional context. FC-3 question formulation requires one sentence, max 25 words.  This technically runs to two sentences. The policy improvement flagged in our previous session stands: a parenthetical retrieval instruction is not a compound question and should be permitted. Without it, Q6 is likely to produce `CONFIRMED-UNKNOWN` — Alex already said they don't know the version.[^14_1]

**Note on Q7:** Shaped by `AMBIGUOUS-FORMAT` — Alex provided a value, but in the wrong form. The question presents the valid enum options explicitly, making it trivially answerable without interpretation.

**Exchange record shell created before delivery:**

```yaml
exchangeid: CE-1-01
step: 1
initiatedat: null       # set at moment of delivery — not yet
questions:
  - questionid: Q-CE-1-01-01
    register_refs: [OQ-1-01]
    field: techstack
    gap_type: AMBIGUOUS-INCOMPLETE
    questiontext: "Which version of AstroJS should this project use?"
    impactstatement: "Required before the environment contract can specify framework.version."

  - questionid: Q-CE-1-01-02
    register_refs: [OQ-1-02]
    field: techstack
    gap_type: AMBIGUOUS-INCOMPLETE
    questiontext: "Which version of Shadcn/ui should this project use?"
    impactstatement: "Required to specify the component library version in the environment contract."

  - questionid: Q-CE-1-01-03
    register_refs: [OQ-1-03]
    field: techstack
    gap_type: AMBIGUOUS-INCOMPLETE
    questiontext: "Should React be included as an explicit stack dependency for the Shadcn integration?"
    impactstatement: "Required to enumerate all install commands and config entries in the environment contract."

  - questionid: Q-CE-1-01-04
    register_refs: [OQ-1-04]
    field: techstack
    gap_type: AMBIGUOUS-INCOMPLETE
    questiontext: "Which package manager should this project use — npm or pnpm?"
    impactstatement: "Required before install command entries can be written in the environment contract."

  - questionid: Q-CE-1-01-05
    register_refs: [OQ-1-05, OQ-1-10]
    field: deploymenttarget
    gap_type: CONTRADICTION
    questiontext: "Are you deploying to Cloudflare Pages (static file hosting) or Cloudflare Workers (edge compute)?"
    impactstatement: "Determines AstroJS output mode and adapter; the entire deployment section depends on this."

  - questionid: Q-CE-1-01-06
    register_refs: [OQ-1-06]
    field: devenvironment
    gap_type: AMBIGUOUS-INCOMPLETE
    questiontext: "What version of Node.js is installed in your development environment? Run `node --version` to check."
    impactstatement: "Required before the runtime section of the environment contract can be completed."

  - questionid: Q-CE-1-01-07
    register_refs: [OQ-1-07]
    field: appetite
    gap_type: AMBIGUOUS-FORMAT
    questiontext: "Would you classify this project's appetite as small (days), medium (1–2 weeks), or large (multi-week)?"
    impactstatement: "The manifest requires one of these three values; 'within a week' cannot be stored as-is."

respondedat: null
responses: []
```


#### Skills Required

- **Linked group detection before formulation.** The linkage check is the first operation — not an afterthought. An executor that formulates all questions first and then checks for links will have already written two separate questions for OQ-1-05 and OQ-1-10. Rewriting them after the fact risks losing precision from the original formulations.
- **`gap_type` → question type mapping.** The `gap_type` field from the register directly shapes the question form. `AMBIGUOUS-FORMAT` entries get a choice-based question; `AMBIGUOUS-INCOMPLETE` entries get a value-retrieval question; `CONTRADICTION` entries get a disambiguation question. An executor without this mapping produces question forms that don't match the gap structure — valid AMBIGUOUS-FORMAT entries asking *"What is your appetite?"* rather than *"Which of these three values best matches?"*
- **FC-3 compound question discipline.**  The hardest constraint to apply for `techstack` entries. OQ-1-01 through OQ-1-04 are all `techstack` gaps. It is tempting to combine them: *"What versions of AstroJS and Shadcn are you using, and which package manager?"* This is three questions in one sentence. FC-3 prohibits it. Each gap is a separate question.[^14_1]
- **Distinguishing resolution from decision.** FC-3 is explicit: the clarification protocol resolves *missing declared information*, not *undecided information*.  Q5 asks Alex to confirm which Cloudflare product they intend — this is disambiguation of a stated intent, not a request for a new decision. If Alex has not decided, the response is `DECISION-REQUIRED`, not `CONFIRMED-UNKNOWN`. The question form must not inadvertently prompt a new decision.[^14_1]


#### Failure Modes

- **Formulating Q5 as a compound question:** *"Are you using Cloudflare Pages or Workers, and do you want SSR?"* Two questions. The second asks about SSR — a design choice, not a clarification of declared intent. FC-3 prohibits both the compound form and the design preference question.[^14_1]
- **Merging OQ-1-01 through OQ-1-04 into one `techstack` question.** Produces one answer paragraph. Task 1.3 Subtask 3 then has to decompose the paragraph back into four field values — reintroducing the ambiguity Task 1.1 already resolved.
- **Formulating Q7 without presenting the valid enum options.** *"What is your appetite for this project?"* Alex will answer *"fairly small"* or *"a few days"* — not a valid enum value. The question produces another AMBIGUOUS-FORMAT response, requiring another exchange. The enum options must be in the question.
- **Creating the exchange record shell after delivery, not before.** If the executor sends the questions and then creates the record, the `initiatedat` timestamp is backdated. The record is a reconstruction, not a contemporaneous log.[^14_1]


#### Policy Improvements Flagged

- **P-09 (confirmed):** Instructional context rule for question formulation — parenthetical retrieval instructions permitted provided they are not compound questions or decision prompts.
- **New — P-Subtask1-01:** The question type mapping should be formalised in the Task 1.3 policy: `gap_type` values map to question forms. This makes question formulation deterministic rather than a judgment call.
- **New — P-Subtask1-02:** The exchange record shell must be created before delivery — `initiatedat` is set at the moment of sending, not at the moment of record creation. The policy should state these are the same moment and that any gap between them is an audit integrity issue.

***

### Subtask 2 — Exchange Conduct

**What is happening:**

All seven questions are delivered to Alex in a single batch per FC-3's batch approach.  The questions are grouped by domain:[^14_1]

```
Technical gaps (Q1–Q6):
  Q1. Which version of AstroJS should this project use?
      → Required before the environment contract can specify framework.version.

  Q2. Which version of Shadcn/ui should this project use?
      → Required to specify the component library version in the environment contract.

  Q3. Should React be included as an explicit stack dependency for the Shadcn integration?
      → Required to enumerate all install commands and config entries in the environment contract.

  Q4. Which package manager should this project use — npm or pnpm?
      → Required before install command entries can be written in the environment contract.

  Q5. Are you deploying to Cloudflare Pages (static file hosting) or Cloudflare Workers (edge compute)?
      → Determines AstroJS output mode and adapter; the entire deployment section depends on this.

  Q6. What version of Node.js is installed in your development environment?
      Run `node --version` in your terminal to check.
      → Required before the runtime section of the environment contract can be completed.

Scope gap (Q7):
  Q7. Would you classify this project's appetite as small (days), medium (1–2 weeks), or large (multi-week)?
      → The manifest requires one of these three values; 'within a week' cannot be stored as-is.
```

`initiatedat` is set. The exchange record is filed. The process blocks until Alex responds. No further work proceeds.[^14_1]

**One design tension to surface:** The policy says *"one question per item, not a consolidated list."*  FC-3 says batch all in one exchange. These are not contradictory — *"one question per item"* means each gap gets its own question (no merging), and *"batch"* means all questions are delivered together. The policy's wording is ambiguous and should be clarified: *"One question per gap — each gap produces exactly one question — all questions delivered in a single batch exchange."*[^14_1]

#### Skills Required

- **Hard blocking.** The executor must not begin Subtask 3 until `respondedat` is populated. No pre-loading of response processing logic, no optimistic assumptions about what Alex will say.[^14_1]
- **Exact delivery.** The questions are delivered exactly as formulated in Subtask 1. No conversational softening, no added context, no rephrasing that changes precision. *"Before we dive in, I just need a few quick answers!"* is not a question — it is preamble that primes the human's expectations and reduces the precision of their answers.
- **Single delivery.** The exchange is sent once. If Alex asks a clarifying question about one of the questions before responding, that question is answered but the exchange is not re-sent. The `initiatedat` timestamp reflects when the exchange was delivered, not when the follow-up was resolved.


#### Failure Modes

- **Sending questions sequentially** — one at a time as they are formulated. This produces up to seven separate exchanges where one would suffice. Each exchange is a human interruption. By question four, Alex is fatigued and answers with decreasing precision.[^14_1]
- **Adding conversational context:** *"I've reviewed your brief and I think it's a great project — just a few small gaps to fill in before we can get started."* This is factually harmless but sets the wrong frame. Alex may interpret "small gaps" as permission to answer casually. The questions are precise for a reason.
- **Sending questions before filing the exchange record.** The record must exist before Alex sees the questions. An exchange record created after the response arrives cannot be verified as contemporaneous.[^14_1]

***

### Subtask 3 — Response Processing

**What is happening:**

Alex's response arrives. Before updating any register entry, each response is classified. Classification before action is the invariant — an executor that acts while classifying may simultaneously begin writing RESOLVED entries and DECISION-REQUIRED entries without realising the conflict.

**Response classification taxonomy:**


| Status | Condition | Action |
| :-- | :-- | :-- |
| `RESOLVED` | Response provides a specific, usable value for the field | Update register entry; populate `resolutionnote` with raw response |
| `CONFIRMED-UNKNOWN` | Alex states they cannot provide this information | Update register; reclassify to WARNING; note confirmed-unknown status |
| `DECISION-REQUIRED` | Alex has not decided, or response surfaces a conflict rather than resolving one | Register entry remains BLOCKER; create decision-request note; step enters `AWAITING-DECISION` |
| `UNCLEAR` | Response is ambiguous — neither a usable value nor a clear unknown | Identify specific follow-up question; request clarification; do not update register until resolved |

**Applied to hypothetical Meridian responses:**


| Question | Alex's response | Classification | Notes |
| :-- | :-- | :-- | :-- |
| Q1 — AstroJS version | "Latest stable is fine" | `RESOLVED` | Valid — but requires derivation flag in `resolutionnote`; "latest stable" is not a version number |
| Q2 — Shadcn/ui version | "Whatever the latest is" | `RESOLVED` | Same derivation flag required |
| Q3 — React integration | "Yes, React is needed for Shadcn" | `RESOLVED` | Explicit confirmation |
| Q4 — Package manager | "Let's go with pnpm" | `RESOLVED` | Specific value |
| Q5 — Cloudflare product | "Cloudflare Pages — I got confused between the two" | `RESOLVED` | Resolves both OQ-1-05 and OQ-1-10; linked cascade required |
| Q6 — Node.js version | "22.11.0 — just checked" | `RESOLVED` | Specific value |
| Q7 — Appetite | "Small — a few days of focused work" | `RESOLVED` | Requires enum mapping note: "small" maps to valid enum `small` |

All seven resolve cleanly in this hypothetical. Three require additional handling noted below.

**Register updates:**

```yaml
# OQ-1-01 updated:
resolutionstatus: RESOLVED
resolutionnote: "Alex: 'Latest stable is fine' (Q-CE-1-01-01). Value requires derivation
                 at Task 1.4 — 'latest stable AstroJS' must be resolved to a specific
                 version number at time of manifest drafting."
resolvedbystep: 1
resolvedatexchange: CE-1-01

# OQ-1-05 updated:
resolutionstatus: RESOLVED
resolutionnote: "Alex: 'Cloudflare Pages — I got confused between the two' (Q-CE-1-01-05).
                 Deployment target confirmed: Cloudflare Pages. Static constraint consistent."
resolvedbystep: 1
resolvedatexchange: CE-1-01

# OQ-1-10 updated (cascade from OQ-1-05 resolution):
resolutionstatus: RESOLVED
resolutionnote: "Contradiction resolved — correct target is Cloudflare Pages (static hosting).
                 Static constraint and deployment target now consistent. Resolution via
                 Q-CE-1-01-05, which covered both OQ-1-05 and OQ-1-10 (linked entries)."
resolvedbystep: 1
resolvedatexchange: CE-1-01

# OQ-1-07 updated:
resolutionstatus: RESOLVED
resolutionnote: "Alex: 'Small — a few days of focused work' (Q-CE-1-01-07).
                 Mapped from freeform to valid enum value 'small'. Mapping is a named
                 derivation — not invention."
resolvedbystep: 1
resolvedatexchange: CE-1-01
```

**Linked entry cascade — the critical mechanical step:**

When Q5 resolves OQ-1-05, the executor must:

1. Update OQ-1-05 as RESOLVED
2. Query the register for all entries with `OQ-1-05` in their `linked_questions` array
3. Find OQ-1-10
4. Update OQ-1-10 as RESOLVED, with `resolutionnote` explicitly naming Q-CE-1-01-05 as the source

This is a mechanical query, but it must be an explicit named step — not an implied consequence. Without it, OQ-1-10 remains OPEN despite the contradiction being resolved.

**Exchange record completed:**

```yaml
respondedat: "2026-03-07T13:45:00+11:00"
responses:
  - questionid: Q-CE-1-01-01
    responsetext: "Latest stable is fine"
    resolution: RESOLVED
    derivation_flag: true

  - questionid: Q-CE-1-01-02
    responsetext: "Whatever the latest is"
    resolution: RESOLVED
    derivation_flag: true

  - questionid: Q-CE-1-01-03
    responsetext: "Yes, React is needed for Shadcn"
    resolution: RESOLVED

  - questionid: Q-CE-1-01-04
    responsetext: "Let's go with pnpm"
    resolution: RESOLVED

  - questionid: Q-CE-1-01-05
    responsetext: "Cloudflare Pages — I got confused between the two"
    resolution: RESOLVED
    linked_cascade: [OQ-1-10]

  - questionid: Q-CE-1-01-06
    responsetext: "22.11.0 — just checked"
    resolution: RESOLVED

  - questionid: Q-CE-1-01-07
    responsetext: "Small — a few days of focused work"
    resolution: RESOLVED
    enum_mapping: "small"
```


#### Skills Required

- **Classify before act.** Every response gets a classification before any register write. An executor that processes responses while classifying may write partial updates — particularly dangerous when a response that looks RESOLVED is actually DECISION-REQUIRED on second read.
- **"Latest stable" as a derivation flag, not a value.**  Alex's responses to Q1 and Q2 are not version numbers. They are acceptance of whatever the current version is. The `resolutionnote` must explicitly flag this: *"Value requires derivation at Task 1.4 — 'latest stable' must be resolved to a specific version at time of manifest drafting."* If this flag is absent, Task 1.4 may write `AstroJS (latest stable)` as a literal manifest value, which violates the `techstack` field format rule.[^14_1]
- **Linked cascade execution.** After resolving OQ-1-05, the executor must query `linked_questions` and apply the cascade. The cascade is not optional — it is the mechanism that prevents a register state where a resolved gap has an unresolved linked entry.
- **Enum mapping as named derivation.** `appetite: small` is derived from *"Small — a few days of focused work."* Writing `small` to the register is correct, but the `resolutionnote` must show the derivation: raw response → mapped value → mapping rule. This is not invention — it is a documented transformation.[^14_1]
- **CONFIRMED-UNKNOWN cascade.** If any response is `CONFIRMED-UNKNOWN`, the register entry is reclassified to WARNING and `resolutionstatus: CONFIRMED-UNKNOWN`. The entry carries forward to Task 1.4, which writes it into the manifest's `openquestions` field. The entry then persists in the register and is reclassified by Step 2 if its severity changes in that context per FC-8.[^14_1]


#### Failure Modes

- **OQ-1-10 left OPEN.** The cascade is not executed. OQ-1-05 is RESOLVED. OQ-1-10 remains OPEN. Task 1.4 reads the register, finds an unresolved BLOCKER contradiction for `deploymenttarget`, and either blocks or incorrectly escalates. The underlying issue is resolved — the register is wrong.
- **"Latest stable" written as a manifest value without a derivation flag.** Task 1.4 inherits `AstroJS (latest stable)` as a `resolutionnote` value, treats it as usable, and writes it directly to the manifest. The manifest's `techstack` field fails its format rule. The traceability record has no version resolution event.
- **`UNCLEAR` treated as `RESOLVED`.** If Alex responds to Q7 with *"probably small, maybe medium — hard to say,"* this is `UNCLEAR`, not `RESOLVED`. Processing it as `RESOLVED` and writing `small` to `resolutionnote` is an inference by the executor. The answer doesn't confirm `small` — it hedges between two values. A follow-up question is required: *"For the manifest we need one of the three values — can you confirm small or medium?"*
- **DECISION-REQUIRED not recognised.** If Alex responds to Q5 with *"I definitely want Workers AND I want it fully static — both are important to me,"* this is `DECISION-REQUIRED`. The contradiction is confirmed real, not a terminology confusion. The executor must not write this as RESOLVED — Alex has not resolved the tension; they have stated both sides of the contradiction as requirements. The entry remains BLOCKER and the step enters `AWAITING-DECISION`.


#### Policy Improvements Flagged

- **P-08 (confirmed):** Response classification (`RESOLVED` / `CONFIRMED-UNKNOWN` / `DECISION-REQUIRED` / `UNCLEAR`) as a formal first step of Subtask 3 — before any register update.
- **P-10 (confirmed):** Linked entry propagation as an explicit named step: *"For each RESOLVED entry, query the register for all entries referencing this entry's `questionid` in their `linked_questions` field and apply the same resolution."*
- **P-11 (confirmed):** "Latest stable" and equivalent deferred version references are valid RESOLVED responses but require a `derivation_flag` in the exchange record and a derivation note in `resolutionnote`. Task 1.4 must not treat these as final values.
- **New — P-Subtask3-01:** Define `UNCLEAR` handling: identify the single follow-up question that resolves the ambiguity; re-present to Alex; `initiatedat` timestamp of the original exchange does not change; a `followuprequestedat` timestamp is added.
- **New — P-Subtask3-02:** Define `DECISION-REQUIRED` handling in full — entry remains BLOCKER, step enters `AWAITING-DECISION`, a decision-request note is created. This is not a clarification exchange (FC-3 does not cover undecided information) — it is a human decision point that requires explicit framework support. Flag as unresolved question UQ-03 from the consolidated findings.

***

## Step 3 — Sanity Check

### Task 1.3 output check

After Subtask 3 completes, every BLOCKER entry in the register has one of:

- `resolutionstatus: RESOLVED` with a `resolutionnote` containing a usable value or a named derivation flag
- `resolutionstatus: CONFIRMED-UNKNOWN` with a `resolutionnote` recording what Alex said
- `resolutionstatus: DECISION-REQUIRED` with a note — step is `AWAITING-DECISION`

In the Meridian hypothetical: all eight BLOCKER entries (OQ-1-01 through OQ-1-07, OQ-1-10) are RESOLVED. The register is ready for Task 1.4.

### Task 1.4 readiness check

Task 1.4 needs to:

1. For each required manifest field, find the resolved value → `resolutionnote` per BLOCKER entry provides this
2. Know which values require further derivation → `derivation_flag: true` entries in the exchange record
3. Have an evidence chain for each field → `resolvedatexchange` + `questionid` per entry provides this
4. Know what remains unresolved → WARNING and INFO entries with `resolutionstatus: OPEN` provide this

The register is directly consumable by Task 1.4 after this task. No intermediate transformation needed.

### One remaining design question

**DQ-04 — Does the exchange record need a `derivation_flag` field, or is the `resolutionnote` sufficient?**

The `derivation_flag: true` on Q1 and Q2 responses signals to Task 1.4 that a version resolution step is needed before those values can be used. This flag could alternatively be embedded in the `resolutionnote` text — *"Requires version resolution at Task 1.4"* — which is what we did in the `resolutionnote` field. The flag in the exchange record is redundant if the `resolutionnote` is reliably read.

The case for the flag: it is machine-queryable. Task 1.4 can query `derivation_flag: true` entries directly and know before it starts which fields need pre-drafting resolution — this is the Subtask 1 pre-drafting step we defined in Task 1.4. The case against: it adds a field that duplicates information in `resolutionnote`.

**Recommendation:** Keep the `derivation_flag` in the exchange record as a machine-queryable signal for Task 1.4's pre-drafting step. The redundancy with `resolutionnote` is intentional — one is for human reading, one is for agent querying.

This is a small decision — call it now or carry forward?

***

## Done When — Task 1.3

Task 1.3 is complete when all six conditions are simultaneously true:

1. `CE-1-01.yaml` exists at `.framework/clarifications/` with `respondedat` populated
2. Every question in the exchange record has a corresponding response entry
3. Every BLOCKER register entry has `resolutionstatus` of `RESOLVED`, `CONFIRMED-UNKNOWN`, or `DECISION-REQUIRED` — no remaining `OPEN` BLOCKER entries
4. All `RESOLVED` entries have a `resolutionnote` specific enough to populate the relevant manifest field, or flagged as a named derivation
5. All linked entry cascades have been applied — no pair of linked entries with mismatched resolution statuses
6. `CONFIRMED-UNKNOWN` entries have been reclassified to WARNING per FC-2 downgrade rules[^14_1]

***

**DQ-04 needs a decision before we proceed to Task 1.4. Everything else in Task 1.3 is settled. What's your call on the `derivation_flag`?**

<div align="center">⁂</div>

[^14_1]: i-am-making-progress-in-creati-fuGLU8hCRLyka3xtBTVglA.md


---

## Step 0 — Task 1.4 Restated

The policy asks: *"Can all confirmed values be structured into a valid, traceable manifest?"*[^15_1]

More precisely:

> **Given `brief-inventory.yaml`, `open-questions-register.yaml` (all BLOCKERs resolved), and `CE-1-01.yaml`, produce `project-manifest.yaml` in DRAFT status with a field-by-field companion traceability record — such that every value has a named source, every unresolved gap is recorded in `openquestions`, and no value was invented.**

The policy's framing is accurate — but the critical word is *traceable*. Producing a valid manifest is necessary but not sufficient. The traceability record is equally an output, not a byproduct.

***

## Step 1 — Artefacts

### Inputs

| Artefact | Consumed for |
| :-- | :-- |
| `brief-inventory.yaml` | Statement IDs as source references for fields populated directly from the brief |
| `open-questions-register.yaml` | Resolved values from `resolutionnote`; unresolved WARNING/INFO entries for `openquestions` field |
| `CE-1-01.yaml` | Exchange IDs and question IDs as source references for clarification-sourced values; `derivation_flag` entries signalling pre-drafting work |
| Manifest schema | Field names, types, required/optional classification, format rules |

### Outputs

**Output 1 — `project-manifest.yaml`**

Filed at: `.framework/project-manifest.yaml`

Status: DRAFT on creation. APPROVED only by Alex's explicit action in Task 1.5.[^15_1]

**Output 2 — `project-manifest.traceability.yaml`**

Filed at: `.framework/traceability/project-manifest.traceability.yaml`

Companion record per FC-5.  Written field-by-field during drafting — not after. This is the operational enforcement of FC-1: if a field cannot be given a traceability entry at the time of writing, it must not be written yet.[^15_1]

**The standing constraint for all subtasks:** traceability entry written at the same moment as the field value. One operation, two writes.

***

## Step 2 — Subtask Analysis

### Subtask 1 — Pre-Drafting Derivation Resolution

**What is happening:**

Before a single manifest field is written, the executor queries `CE-1-01.yaml` for all responses with `derivation_flag: true`. These are responses that provided acceptance of a derivation rather than a specific value. They must be resolved to actual values before drafting begins — writing a manifest field from an unresolved derivation produces an invalid value that appears valid.

From the Meridian exchange, two derivation flags:


| Question | Response | Derivation required |
| :-- | :-- | :-- |
| Q-CE-1-01-01 (AstroJS version) | "Latest stable is fine" | Resolve to a specific AstroJS version number at time of drafting |
| Q-CE-1-01-02 (Shadcn/ui version) | "Whatever the latest is" | Resolve to a specific Shadcn/ui version number at time of drafting |

**Resolution method:** The executor performs a version lookup — npm registry, GitHub releases, or official documentation. The resolved values are recorded before the first manifest field is written:

```yaml
# Pre-drafting derivation log (internal worklog — not a formal artefact)

derivation-01:
  field: techstack[AstroJS]
  derivationrule: latestStableVersion
  resolvedvalue: "5.3.0"
  lookupdate: "2026-03-07"
  lookupsource: "npmjs.com/package/astro — latest dist-tag"
  authorisedby: "CE-1-01, Q-CE-1-01-01"

derivation-02:
  field: techstack[Shadcn/ui]
  derivationrule: latestStableVersion
  resolvedvalue: "2.4.0"
  lookupdate: "2026-03-07"
  lookupsource: "npmjs.com/package/shadcn-ui — latest dist-tag"
  authorisedby: "CE-1-01, Q-CE-1-01-02"
```

**Gap detection during pre-drafting:** While preparing derivations, the executor attempts to account for every `techstack` entry that will appear in the manifest. This is where a Task 1.2 omission surfaces: the `@astrojs/react` integration adapter has no register entry — it was not explicitly mentioned in the brief and was not asked about in Task 1.3. It is implied by the React confirmation (Q-CE-1-01-03) but was not explicitly declared.

The correct handling:

1. Create a new register entry `OQ-1-14` — WARNING, `gap_type: AMBIGUOUS-INCOMPLETE`, field: `techstack`, gap: *"@astrojs/react integration adapter implied by React confirmation but not explicitly declared"*
2. Resolve via named derivation: *"React integration confirmed in CE-1-01, Q-CE-1-01-03; @astrojs/react adapter is the standard integration mechanism — derivation documented"*
3. Proceed with the value

This is Task 1.4 functioning as a quality gate on Task 1.2. Pre-drafting is where omissions surface — better here than at Step 2.

#### Skills Required

- **`derivation_flag` query as the first act.** Not optional. The executor must check the exchange record for derivation flags before writing field one.
- **Version lookup as a tool call.** The executor needs external access to resolve "latest stable" to a version number. If external access is unavailable, the correct path is `CONFIRMED-UNKNOWN` with `resolutionnote: "Version lookup unavailable; value unresolvable at this time"` — not a guess.[^15_1]
- **Implicit dependency detection.** Recognising that confirming React implies `@astrojs/react` is domain knowledge. An executor without AstroJS knowledge may miss it. This is exactly the class of gap that belongs in the conditional sections table we proposed for the manifest template (S-05 from the consolidated findings) — but since that table doesn't exist yet, it requires domain knowledge here.
- **New register entry discipline when new gaps surface.** The executor creates a register entry before using the derived value — not after. The register entry is the evidence that the derivation was authorised, not invented.


#### Failure Modes

- **Proceeding without checking derivation flags.** AstroJS and Shadcn/ui versions are written to the manifest as `AstroJS (latest stable)` and `Shadcn/ui (latest)`. Both violate the `techstack` format rule: *"Named technologies only — AstroJS 5.x is valid, modern frontend stack is not."*[^15_1]
- **Resolving versions without recording the lookup.** The manifest contains `AstroJS 5.3.0` but the traceability record has no entry explaining how `5.3.0` was arrived at. A verifier reading the manifest cannot confirm the value traces to Alex's acceptance plus a specific lookup — it appears invented.
- **Missing `@astrojs/react`.** The manifest's `techstack` array omits the integration adapter. Step 2 cannot write the `framework.integrations` section without it. The omission is silent — no error, just an incomplete manifest.


#### Policy Improvements Flagged

- **P-13 (confirmed):** Pre-drafting derivation resolution as an explicit Subtask 1 — check `derivation_flag` entries, resolve to specific values, record in worklog before drafting begins.
- **New — P-Subtask1-PreDraft-01:** The policy must specify the handling when version lookup is unavailable: the value becomes `CONFIRMED-UNKNOWN`, the register entry is updated, and the field is written as empty with an `openquestions` entry — not guessed.

***

### Subtask 2 — Required Field Population

**What is happening:**

Each required field is populated in schema order. For each field, the sequence is fixed:

1. Identify the source — register `resolutionnote`, brief statement ID, or derivation log
2. Write the field value
3. Immediately write the traceability entry

Schema order for required fields: `projectid` → `projectname` → `description` → `techstack` → `deploymenttarget` → `devenvironment` → `humanactors` → `appetite`

**`projectid` — derived from `projectname`:**

```yaml
# Manifest:
projectid: meridian-consulting-launch-landing-page

# Traceability:
- outputfield: projectid
  valuesummary: "meridian-consulting-l"
  sourcetype: derivationrule
  sourcereference: "kebab-case-transformation from projectname; rule defined in manifest schema"
```

`projectid` is the only field where invention is structurally impossible — the derivation rule is deterministic and documented.[^15_1]

**`projectname` — from brief statement S-01:**

```yaml
# Manifest:
projectname: "Meridian Consulting — Launch Landing Page"

# Traceability:
- outputfield: projectname
  valuesummary: "Meridian Consulting —"
  sourcetype: brief
  sourcereference: "brief S-01: 'I need a single-page marketing website for my consulting practice, Meridian Consulting'"
```

The format rule: *"use humandirector's words exactly — do not normalise, correct capitalisation, or rewrite."*  The name `Meridian Consulting` is in the brief. `Launch Landing Page` is derived from the project description. The traceability entry must show both source references if the name is assembled from multiple statements.[^15_1]

**`description` — assembled from S-01, S-06, S-07:**

```yaml
# Manifest:
description: >
  A single-page marketing website for Meridian Consulting. The page includes
  sections for hero introduction, services overview, an about section, and a
  contact form routing to email via a third-party handler. Visual style is
  clean, minimal, and professional.

# Traceability:
- outputfield: description
  valuesummary: "A single-page marketing"
  sourcetype: brief
  sourcereference: "brief S-01 (project type and name), S-06 (page sections), S-07 (visual style)"
```

The assembly rule (P-15 from our consolidated findings): include project type, primary purpose, and key deliverable. Exclude constraints, deployment details, and named actors — these have dedicated fields.  Every sentence must trace to a brief statement. The executor's voice does not appear.[^15_1]

**`techstack` — assembled from brief, clarification, and derivation:**

```yaml
# Manifest:
techstack:
  - "AstroJS 5.3.0"
  - "Shadcn/ui 2.4.0"
  - "React 19.x"
  - "@astrojs/react"
  - "pnpm 9.x"

# Traceability:
- outputfield: "techstack[^15_0]: AstroJS 5.3.0"
  valuesummary: "AstroJS 5.3.0"
  sourcetype: derivationrule
  sourcereference: "latestStableVersion lookup 2026-03-07 (npmjs.com/package/astro); acceptance confirmed CE-1-01 Q-CE-1-01-01"

- outputfield: "techstack[^15_1]: Shadcn/ui 2.4.0"
  valuesummary: "Shadcn/ui 2.4.0"
  sourcetype: derivationrule
  sourcereference: "latestStableVersion lookup 2026-03-07 (npmjs.com/package/shadcn-ui); acceptance confirmed CE-1-01 Q-CE-1-01-02"

- outputfield: "techstack[^15_2]: React 19.x"
  valuesummary: "React 19.x"
  sourcetype: clarificationanswer
  sourcereference: "CE-1-01 Q-CE-1-01-03: 'Yes, React is needed for Shadcn'"

- outputfield: "techstack[^15_3]: @astrojs/react"
  valuesummary: "@astrojs/react"
  sourcetype: derivationrule
  sourcereference: "standard AstroJS React integration adapter; derivation authorised by React confirmation CE-1-01 Q-CE-1-01-03; register entry OQ-1-14"

- outputfield: "techstack[^15_4]: pnpm 9.x"
  valuesummary: "pnpm 9.x"
  sourcetype: clarificationanswer
  sourcereference: "CE-1-01 Q-CE-1-01-04: 'Let's go with pnpm'"
```

**Note on `pnpm` version:** Alex confirmed pnpm as the package manager but did not provide a version. The executor must decide: derive from latest stable (same pattern as AstroJS), or record without version. The manifest format rule for `techstack` is *"Named technologies only — AstroJS 5.x is valid."* Major version only is acceptable. This is another pre-drafting derivation — it was not caught in Subtask 1 because pnpm was not in the exchange with a derivation flag. A new `OQ-1-15` entry is created for pnpm version, resolved via latest-stable derivation, and recorded.

**`appetite` — from clarification with enum mapping:**

```yaml
# Manifest:
appetite: small

# Traceability:
- outputfield: appetite
  valuesummary: "small"
  sourcetype: clarificationanswer
  sourcereference: "CE-1-01 Q-CE-1-01-07: 'Small — a few days of focused work'; mapped from freeform to valid enum value 'small' — mapping is a named derivation, not invention"
```

The mapping is documented in the traceability entry. A verifier can confirm the mapping rule was applied correctly.[^15_1]

#### Skills Required

- **Schema-order population.** `projectid` depends on `projectname` — `projectname` must be written first. Any field that is derived from another must come after its source field in the drafting sequence.
- **Description assembly without editorial addition.** Every sentence in `description` must trace to a brief statement. If the brief's language is imprecise, the description is imprecise — fidelity over quality. The executor's instinct to improve the description is the most common source of FC-1 violations in this field.[^15_1]
- **Simultaneous traceability writing.** Field value and traceability entry in one operation. An executor who writes the full manifest first and traceability second is reconstructing, not recording. Reconstruction introduces uncertainty for assembled fields like `description`.
- **New gap detection mid-field.** When populating `techstack`, the executor discovers `@astrojs/react` and pnpm version were not resolved pre-drafting. The correct response is to pause, create register entries, resolve via derivation, and then write — not to proceed and fill in traceability later.


#### Failure Modes

- **`description` field written in cleaner language.** Alex wrote *"I need a single-page marketing website."* The manifest says *"This project delivers a single-page marketing website."* The executor's phrasing is not in the brief. It is an invention — small, harmless-seeming, and still an FC-1 violation.[^15_1]
- **`techstack` entries without version numbers.** Writing `AstroJS` without a version violates the format rule. Writing `AstroJS (latest stable)` uses the pre-derivation placeholder rather than the resolved value. Both indicate that Subtask 1 did not complete successfully.
- **Traceability entry written after all fields.** The manifest is complete. The executor now writes traceability entries by reading back through the manifest and identifying sources from memory. For `description`, assembled from three statements, the executor may misattribute or conflate sources. The FC-5 requirement is field-by-field for exactly this reason.[^15_1]
- **`appetite` mapping undocumented.** The traceability entry says `sourcetype: clarificationanswer` but does not record the mapping from *"Small — a few days"* to enum value `small`. A verifier cannot confirm whether `small` came from Alex's word choice or from the executor's judgment. The mapping rule must be explicit in `sourcereference`.


#### Policy Improvements Flagged

- **P-15 (confirmed):** Selection criteria for `description` assembly in the policy: include project type, primary purpose, key deliverable; exclude constraints, deployment details, named actors.
- **New — P-Subtask2-01:** The policy must specify that version-less `techstack` entries discovered during field population are treated the same as pre-drafting derivations: pause, create register entry, resolve, then write.
- **S-03 (confirmed):** Clarify whether package managers belong in `techstack`, `devenvironment`, or both. In our manifest, `pnpm` appears in `techstack` (as a versioned tool) and will appear in `devenvironment.packagemanager` (as a configuration value). The schema should specify whether this duplication is intentional.

***

### Subtask 3 — Optional Field Population

**What is happening:**

Optional fields follow the same field-then-traceability pattern. Fields with content from the brief or register are populated. Fields with no content are explicitly recorded as `[]` or `null` — never omitted. Omitting an optional field is structurally different from recording it as absent: omission creates ambiguity about whether the field was considered.[^15_1]

**Handling AMBIGUOUS optional content:**

`integrationrequirements` is AMBIGUOUS-INCOMPLETE (OQ-1-08, WARNING, OPEN). The field is not absent — Formspree was mentioned. The field is not confirmed — it was tentative. The correct handling: record what was said, reference the open question, do not default to Formspree as confirmed.

```yaml
# Manifest (selected optional fields):
constraints:
  - "No dedicated backend — contact form must use third-party handler"
  - "Fully static site — no server-side rendering"
  - "Lighthouse Performance score 90 or above"
  - "Minimal dependency footprint — avoid unnecessary packages"

outofscope:
  - "CMS or content management capability"
  - "Blog or additional pages beyond the landing page"
  - "Analytics integration"
  - "Server-side logic"

existingassets: []

referenceexamples:
  - "Linear.app — clean typography, bold headings, whitespace-heavy layout"
  - "Stripe marketing pages — professional, minimal, credible aesthetic"

integrationrequirements:
  - provider: "TBD"
    type: "third-party form handler"
    note: "Formspree mentioned tentatively in brief (S-08); unconfirmed — see OQ-1-08"

# Traceability (selected entries):
- outputfield: "constraints[^15_0]"
  valuesummary: "No dedicated backend"
  sourcetype: brief
  sourcereference: "brief S-05: 'no dedicated backend — contact form to use a third-party service'"

- outputfield: existingassets
  valuesummary: "[] (empty)"
  sourcetype: notpresentininput
  sourcereference: "brief contained no mention of existing assets; ABSENT in brief-inventory fields array"

- outputfield: "integrationrequirements[^15_0]"
  valuesummary: "TBD — third-party form"
  sourcetype: brief
  sourcereference: "brief S-08: 'maybe Formspree for the contact form' — tentative; open question OQ-1-08"
```

**Three discipline points surface here:**

1. **`constraints` uses Alex's exact phrasing.** *"No dedicated backend"* is Alex's phrase. The manifest uses it. The executor must not normalise to *"serverless architecture only"* — that is editorial expansion of scope.[^15_1]
2. **`existingassets: []` is recorded, not omitted.** The traceability entry confirms it was assessed and found absent. A downstream agent checking whether existing assets were considered gets a definitive `[]` — not a missing field that could mean either "absent" or "not assessed."[^15_1]
3. **`integrationrequirements` records the ambiguity faithfully.** Provider is `TBD`. The note references the brief statement and the open question ID. Task 1.5 and Step 2 both have visibility into this ambiguity without needing to re-derive it.

#### Skills Required

- **Faithful transcription.** Constraints and out-of-scope entries use Alex's language. The executor's role is transcription, not editing. If Alex's constraint is imprecise, the manifest constraint is imprecise — and that imprecision is visible to Alex at Task 1.5 review.
- **Empty field discipline.** `existingassets: []` is a positive statement: *"This field was assessed; nothing was found."* This is not the same as the field being absent. Every optional field receives an entry, even if empty.
- **AMBIGUOUS optional handling.** The `integrationrequirements` case is the hardest optional field case. The failure modes are: (a) treating AMBIGUOUS as ABSENT and leaving the field empty — losing the Formspree signal; (b) treating the tentative mention as confirmed — inventing a value. The correct path records the ambiguity with a register cross-reference.[^15_1]


#### Failure Modes

- **Constraints normalised.** *"Avoid unnecessary packages"* becomes *"minimal dependencies."* The normalisation is harmless in isolation but compounds across a project — by Step 2, every normalised constraint has drifted slightly from Alex's intent, and the cumulative drift is invisible because no single change looks significant.
- **`existingassets` omitted.** Downstream agents cannot distinguish *"absent"* from *"not assessed."* A Step 2 agent checking whether existing assets need to be accounted for gets no signal.
- **`integrationrequirements` populated with `provider: Formspree`.** Formspree is confirmed nowhere. Brief S-08 says *"maybe Formspree."* Writing `provider: Formspree` is an invention. Step 2 builds an integration section around a provider that was never confirmed. Alex may not use Formspree at all.


#### Policy Improvements Flagged

- **New — P-Subtask3-01:** Add an explicit rule that AMBIGUOUS optional fields are recorded with the ambiguity and a register cross-reference — not as confirmed values, not as empty fields.

***

### Subtask 4 — Open Questions Population

**What is happening:**

The manifest's `openquestions` field is populated from the register's remaining unresolved entries — all entries with `resolutionstatus: OPEN` and classification `WARNING` or `INFO`, plus any `CONFIRMED-UNKNOWN` entries from Task 1.3.

This subtask has one additional responsibility: ensuring that new register entries created during Tasks 1.4 Subtasks 1–3 (OQ-1-14 for `@astrojs/react`, OQ-1-15 for pnpm version) are included if they have an OPEN status.

From the Meridian register, unresolved entries after Task 1.3:

```yaml
openquestions:
  - questionid: OQ-1-08
    field: integrationrequirements
    gap: "Form handler provider tentative — Formspree mentioned but not confirmed"
    impact: "Step 2 services section conditionally required; provider and method cannot be specified until confirmed"
    classification: WARNING
    resolutionstatus: OPEN

  - questionid: OQ-1-09
    field: existingassets
    gap: "No existing assets declared in brief"
    impact: "No downstream bootstrap step requires existing assets; noted for completeness"
    classification: INFO
    resolutionstatus: OPEN

  - questionid: OQ-1-11
    field: null
    gap: "Infrastructure readiness present in brief but no manifest field exists"
    impact: "Step 2 deployment section may assume DNS procurement is needed; self-managed DNS not formally recorded"
    classification: WARNING
    schema_gap_flag: true
    resolutionstatus: OPEN

  - questionid: OQ-1-12
    field: null
    gap: "Maintainability requirement present in brief but no manifest field exists"
    impact: "Indirect downstream impact on Step 3 role configuration; no current schema field"
    classification: INFO
    schema_gap_flag: true
    resolutionstatus: OPEN

  - questionid: OQ-1-13
    field: null
    gap: "Design intent descriptors exceed referenceexamples field schema"
    impact: "Step 4 pattern seeding would benefit from explicit design intent"
    classification: INFO
    schema_gap_flag: true
    resolutionstatus: OPEN
```

*Note: OQ-1-14 and OQ-1-15 were created and resolved during Subtask 1/2 of this task. They are RESOLVED, not carried into `openquestions`.*

#### Skills Required

- **Register completeness query.** The executor queries the entire register for `resolutionstatus: OPEN` — not just entries from Task 1.2. Entries created during Task 1.4 (new discoveries) must also be checked.
- **Impact statement currency.** Some Task 1.2 impact statements were written in general terms. By Task 1.4, the actual manifest state is known. The impact for OQ-1-08 can now be more specific: *"Step 2 services section is conditionally required given form handler reference in S-08; provider and integration method cannot be specified until confirmed."* The `gap` field is immutable; `impact` can be updated to reflect current context.[^15_1]


#### Failure Modes

- **New Task 1.4 entries not included.** OQ-1-14 (resolved) and OQ-1-15 (resolved) are RESOLVED — they do not appear. But if a new gap surfaced during Subtask 3 and was left OPEN (e.g., a constraint entry with ambiguous source), it must appear here. Missing it means the manifest's `openquestions` is incomplete — Task 1.5 review and Step 2 have no visibility into it.
- **INFO entries omitted.** An executor who considers INFO entries as not worth recording produces a manifest `openquestions` section that looks cleaner but is less complete. Alex at Task 1.5 should see OQ-1-09 (`existingassets` absent) — even as INFO — because it confirms the field was assessed.

***

### Subtask 5 — Self-Check

**What is happening:**

Before setting `status: DRAFT`, the executor runs a deterministic checklist. Binary pass/fail. Every item checked. Any failure corrected before status is set — setting status DRAFT before the check inverts its purpose.[^15_1]

```
Self-check checklist:

□ 1. All required fields are present and non-empty
□ 2. techstack has at least one versioned entry with a specific version number
□ 3. humanactors has at least one entry with role: humandirector
□ 4. appetite is exactly one of: small / medium / large
□ 5. status is DRAFT (not APPROVED — never self-approved)
□ 6. created is set to current ISO 8601 datetime with timezone
□ 7. approvedat is absent
□ 8. approvedby is absent
□ 9. Every required field has a corresponding traceability entry
□ 10. Every non-empty optional field has a corresponding traceability entry
□ 11. Every RESOLVED BLOCKER register entry corresponds to a populated field value
□ 12. Every OPEN register entry (WARNING/INFO) appears in openquestions
□ 13. No field contains language not found in the brief, clarification record, or a documented derivation
□ 14. No techstack entry contains a placeholder (e.g., "latest stable", "TBD", "x.x")
□ 15. The traceability record file exists at the canonical path
```

Item 14 is new — it specifically catches the failure mode where pre-drafting derivation resolution was skipped or incomplete. A `techstack` entry reading `AstroJS (latest stable)` fails item 14 and must be corrected before DRAFT status is set.

Items 13 and 14 are the most commonly skipped because they require cross-referencing the manifest against source documents rather than just checking field presence. They are also the items most likely to catch FC-1 violations.

#### Skills Required

- **Checklist-before-status discipline.** Status DRAFT is the executor's assertion of completeness. Running the checklist after setting status means the assertion was made before evidence was confirmed.[^15_1]
- **Item 13 cross-reference.** For each field, the executor must confirm that every sentence, phrase, or value can be located in the brief, a clarification answer, or a derivation log entry. This is time-consuming for assembled fields like `description` and `constraints`. It is not optional.
- **Failure as correct behaviour.** Finding a self-check failure is not a process problem — it is the self-check working. The failure is corrected. The item is re-checked. Status DRAFT is not set until all 15 items pass.


#### Failure Modes

- **Status set before checklist.** *"I'll do the self-check now that it's in DRAFT."* The DRAFT state signals Task 1.5 readiness. If Task 1.5 is triggered before the self-check completes, the human reviews an unverified document.
- **Items 13–14 skipped as "obvious."** The executor knows what they wrote and considers the cross-check unnecessary. An AstroJS version placeholder that was missed in Subtask 1 survives into DRAFT status. Task 1.5 review catches it — but only if Alex knows to look at version numbers, which is unlikely. The failure reaches Step 2 undetected.

***

## Step 3 — Sanity Check

### Output completeness

| Manifest section | Source | Complete? |
| :-- | :-- | :-- |
| All required fields | Brief + clarification + derivation | ✓ |
| All optional fields — populated | Brief statements | ✓ |
| All optional fields — absent | Recorded as `[]` or `null` | ✓ |
| `openquestions` | Register OPEN entries (WARNING/INFO) | ✓ — 5 entries |
| `status: DRAFT` | Self-check passed | ✓ |
| Traceability — every field | Written field-by-field | ✓ |

### Task 1.5 readiness check

Task 1.5 needs to:

1. Present the manifest to Alex for review → manifest is structured and human-readable in YAML
2. Present open questions for acknowledgement → `openquestions` field contains all WARNING/INFO entries
3. Accept corrections and apply them → traceability record supports adding correction entries
4. Record approval with timestamp and attribution → `status`, `approvedat`, `approvedby` fields are present and empty

The manifest is directly ready for Task 1.5. No intermediate transformation needed.

### Two remaining design questions

**DQ-05 — The pre-drafting worklog: formal artefact or internal only?**

The derivation log produced in Subtask 1 records version lookups and their sources. It is currently described as an *internal worklog — not a formal artefact.* But the traceability record's `sourcereference` fields point back to it: *"latestStableVersion lookup 2026-03-07 (npmjs.com/package/astro)."* If the worklog is not retained, the traceability entry's `sourcereference` is a reference to nothing — it cannot be verified.

**Options:**

- **Option A:** The worklog is a formal artefact, filed at `.framework/traceability/drafting-worklog-step-1.yaml`. The traceability entries reference it by path.
- **Option B:** The worklog entries are folded into the traceability record itself as additional entries with `sourcetype: derivationrule` — the lookup details appear in `sourcereference` inline.

Option B is simpler and keeps all provenance in one file. Option A is more structured but adds a third artefact to Step 1. **Recommendation: Option B** — fold derivation worklog entries into the traceability record. The traceability record already exists for this purpose.

**DQ-06 — Should `pnpm` appear in both `techstack` and `devenvironment.packagemanager`?**

In our manifest it appears in both. The schema ambiguity (S-03 from consolidated findings) is real. **Decision needed now** — it affects what we write into the manifest.

- `techstack` captures *what was used to build* — pnpm as a versioned tool the project depends on
- `devenvironment.packagemanager` captures *how the environment is configured* — pnpm as a runtime configuration value

These are different representations of the same choice. Duplication is not wrong if each field is serving a different downstream consumer. Step 2's environment contract will read `devenvironment.packagemanager` to configure the runtime section. Pattern seeding in Step 4 will read `techstack` to identify applicable patterns.

**Recommendation: allow duplication with an explicit note in the manifest schema.** `pnpm` appears in both fields. The traceability record has a single source (`CE-1-01 Q-CE-1-01-04`) referenced by both entries.

***

These two decisions can be made now or carried as DQ items. DQ-05 has a clear answer (Option B). DQ-06 has a recommendation. **Shall I take both as decided and proceed to Task 1.5?**

<div align="center">⁂</div>

[^15_1]: i-am-making-progress-in-creati-fuGLU8hCRLyka3xtBTVglA.md


---

## Step 0 — Task 1.5 Restated

The policy asks: *"Does humandirector confirm that the manifest accurately represents their intent?"*[^16_1]

More precisely:

> **Given `project-manifest.yaml` in DRAFT status, obtain Alex's explicit, informed approval — ensuring they have seen every field value and been notified of every unresolved open question — and record that approval in a form that satisfies FC-4 Tier 1. The manifest exits this task in APPROVED status, sealed against further edits.**

Three words matter in that restatement:

- **explicit** — not inferred from prior positive responses
- **informed** — Alex has seen the open questions, not just the field values
- **sealed** — APPROVED is a terminal state; any post-approval change requires a full re-run of Task 1.5[^16_1]

***

## Step 1 — Artefacts

### Input

`project-manifest.yaml` in DRAFT status — self-check passed, all 15 items confirmed.

### Outputs

| Artefact | Nature |
| :-- | :-- |
| `project-manifest.yaml` in APPROVED status | Primary output — status field updated, `approvedat` and `approvedby` set |
| Audit log entry (FC-4 Tier 1) | Approval record independent of the manifest field [^16_1] |
| `correction-record-CR-1-xx.yaml` *(conditional)* | Created if Alex returns corrections; filed at `.framework/corrections/` |
| Updated `project-manifest.traceability.yaml` *(conditional)* | New entries added for any corrected fields |
| Updated `open-questions-register.yaml` *(conditional)* | New entries if corrections introduce new gaps |


***

## Step 2 — Subtask Analysis

### Subtask 1 — Presentation Preparation

**What is happening:**

The executor prepares a review package. Before preparing anything, two questions must be answered:

**Question A — What is Alex actually being asked to confirm?**

Two distinct things require review and they must not be conflated:

- **Field accuracy:** Does each value correctly represent what Alex said?
- **Open question acknowledgement:** Alex must be informed of the five unresolved entries before approving — approving a manifest without knowing its gaps is not informed consent

**Question B — Can Alex navigate `project-manifest.yaml` directly?**

YAML is human-readable at this complexity level. Alex can read it. The question is whether reading it unaided is sufficient for a *meaningful* review. The risk: Alex skims the field values (which are their own words) and misses the `openquestions` section entirely.

The review package therefore has a structured two-part presentation — not a separate document, but a framed delivery:

```
Part 1 — Field values for your confirmation:

projectname:       Meridian Consulting — Launch Landing Page
description:       A single-page marketing website for Meridian Consulting. The page
                   includes sections for hero introduction, services overview, an about
                   section, and a contact form routing to email via a third-party handler.
                   Visual style is clean, minimal, and professional.
techstack:         AstroJS 5.3.0 / Shadcn/ui 2.4.0 / React 19.x / @astrojs/react / pnpm 9.x
deploymenttarget:  Cloudflare Pages — meridianconsulting.com.au
devenvironment:    macOS Sonoma / VS Code / Node.js 22.11.0 / pnpm
appetite:          small
constraints:       No dedicated backend — contact form uses third-party handler /
                   Fully static — no server-side rendering /
                   Lighthouse Performance 90+ /
                   Minimal dependency footprint
outofscope:        CMS, blog, analytics, server-side logic
referenceexamples: Linear.app, Stripe marketing pages

Part 2 — Open questions you are approving with knowledge of:

OQ-1-08 [WARNING] Form handler provider not yet confirmed — Formspree mentioned
                   tentatively. Impact: Step 2 services section incomplete until confirmed.
OQ-1-11 [WARNING] Infrastructure readiness (Cloudflare account, DNS control) noted in
                   brief but no manifest field exists. Impact: Step 2 deployment section
                   will need to address this separately.
OQ-1-09 [INFO]    No existing assets declared. Noted for completeness.
OQ-1-12 [INFO]    Maintainability requirement (handoff to developer) noted but no
                   manifest field exists.
OQ-1-13 [INFO]    Design intent descriptors exceed referenceexamples field scope.
                   Noted for Step 4.

To approve: confirm the field values above accurately represent your intent and that
you have noted the open questions. If any field is wrong, identify the field and the
correct value.
```

**The summary is generated deterministically from the manifest.** Every value in Part 1 maps to an exact field in `project-manifest.yaml`. The executor must validate this before delivery: each summary value matches its corresponding manifest field exactly. A rendering error here means Alex approves a summary that doesn't match the canonical document.[^16_1]

**The approval instruction is precise.** Two things are asked: confirm accuracy, acknowledge open questions. The instruction does not ask for technical sign-off, design approval, or strategic confirmation. It does not prompt Alex to re-review areas the executor considers uncertain.

#### Skills Required

- **Summary fidelity validation.** Before delivery, every summary value is checked against the manifest. Not asserted — checked. A `techstack` summary showing `AstroJS 5.3.0` when the manifest contains `AstroJS 5.30.0` (a typo) means Alex approves the wrong version.
- **Open question completeness.** All five OPEN register entries appear in Part 2. The executor must not filter by "likely to matter to Alex" — all unresolved gaps are presented. WARNING entries are distinguished from INFO entries so Alex understands which carry downstream consequences.
- **Instruction precision.** The review instruction names exactly what constitutes an approval and what constitutes a returned correction. Alex cannot accidentally approve by saying *"looks mostly fine."*


#### Failure Modes

- **Part 2 omitted or truncated.** Alex sees only field values. They approve without knowing about OQ-1-08 (form handler unconfirmed). Step 2 receives a manifest whose `openquestions` contains a WARNING the human director was never informed about — the approval was not informed consent.
- **Summary adds context not in the manifest.** *"The tech stack includes AstroJS and its ecosystem dependencies."* The word *"ecosystem"* is not in the manifest. It's an editorial framing. It primes Alex to approve a characterisation that may not match how they think about the stack.
- **Approval instruction is a leading question.** *"Does this look right?"* invites *"yes"* as a reflex. *"Confirm the field values above accurately represent your intent"* invites deliberate reading.


#### Policy Improvements Flagged

- **P-18 (confirmed):** Summary generation with a deterministic rendering rule and a summary-vs-manifest validation check before delivery.
- **P-20 (confirmed):** Define minimum explicit approval statement — the response must name the document and contain the word "approved" (case-insensitive). Freeform affirmation insufficient.
- **New — P-Subtask1-1.5-01:** The review instruction must explicitly name what a returned correction looks like: *"identify the specific field and the correct value."* Without this, Alex may return a correction as a vague statement (*"something feels off about the tech stack"*) that Task 1.5 Subtask 3 cannot classify as `RETURNED` without a follow-up.

***

### Subtask 2 — Presentation and Blocking

**What is happening:**

The review package is delivered to Alex. `presentedat` timestamp is recorded immediately — before Alex reads it, not after they respond. The process blocks.[^16_1]

The exchange record for this presentation:

```yaml
# review-record-RR-1-01.yaml
# Filed at: .framework/reviews/RR-1-01.yaml

reviewid: RR-1-01
step: 1
document: .framework/project-manifest.yaml
documentstatus: DRAFT
presentedto: "Alex Chen"
presentedat: "2026-03-07T13:55:00+11:00"
summaryvalidated: true       # summary-vs-manifest check passed before delivery
openquestionsincluded: [OQ-1-08, OQ-1-09, OQ-1-11, OQ-1-12, OQ-1-13]
respondedat: null            # set when response arrives
responseclassification: null # APPROVED | RETURNED | UNCLEAR
response: null               # raw response text
```

**The blocking state is genuine.** No further Task 1 work proceeds until `respondedat` is populated. There is no timeout that allows the process to self-approve or proceed on assumption. There is no "optimistic pre-loading" of correction logic.[^16_1]

**One structural note:** The review record is a new artefact — `RR-1-01.yaml` — not part of the clarification exchange series. The clarification exchange (CE) records are FC-3 artefacts for resolving BLOCKER gaps. The review record is an FC-4 artefact for recording human approval. They have different purposes, different schemas, and must not be conflated. This distinction should be explicit in the policy.

#### Skills Required

- **Record-before-deliver discipline.** `presentedat` is set at the moment of delivery. Not when the response arrives. Not when the executor decides to send. At the moment the package is delivered to Alex. An executor who creates the record after the response arrives cannot set an accurate `presentedat`.[^16_1]
- **Hard blocking.** The executor must not begin Subtask 3 processing logic, pre-load correction workflows, or assume an approval outcome. The process is suspended.


#### Failure Modes

- **`presentedat` backdated.** The executor creates the review record after receiving Alex's response and sets `presentedat` to an estimated send time. The audit trail shows an approval that preceded the review by minutes or hours. This is an integrity failure even if the intent was innocent.[^16_1]
- **Review record not filed before delivery.** Same consequence as backdating — the record is a reconstruction rather than a contemporaneous log.

***

### Subtask 3 — Response Classification

**What is happening:**

Alex's response arrives. Before any action, it is classified. Classification is a gate, not a side note.

**Three primary classifications:**


| Classification | Condition | Path |
| :-- | :-- | :-- |
| `APPROVED` | Response contains an explicit approval of the manifest, naming the document | → Subtask 5 |
| `RETURNED` | Response identifies one or more specific field corrections | → Subtask 4 |
| `UNCLEAR` | Response is neither a clear approval nor specific corrections | → Follow-up question |

**The `UNCLEAR` path in detail:**

`UNCLEAR` is not a failure — it is a common outcome when Alex responds informally. Examples:

- *"Looks good to me"* — positive but not explicit; does not name the document
- *"Mostly right but I'm not sure about the tech stack section"* — neither approval nor specific correction
- *"Fine, proceed"* — ambiguous; could be approval or dismissal

For each `UNCLEAR` response, the executor identifies the single follow-up question that resolves the ambiguity:

- *"Looks good to me"* → *"To confirm approval of the project manifest: do the field values above accurately represent your intent?"*
- *"Not sure about the tech stack"* → *"Which specific entry in the tech stack section needs to change, and what should it say?"*

The follow-up is recorded in the review record (`followuprequestedat` timestamp added). The `presentedat` timestamp of the original delivery does not change.

**The embedded correction case:**

Alex responds: *"Approved — but appetite should probably be medium since I said 1–2 weeks."*

This response contains both an approval statement and a specific correction. Classification: **`RETURNED`**. The approval statement is noted but does not take effect until the correction is applied and re-reviewed. An approval with an embedded correction is still `RETURNED` — the manifest does not reflect Alex's intent as stated in this response.[^16_1]

**The `DECISION-REQUIRED` case:**

Alex responds to Part 2 about OQ-1-08: *"Actually I haven't decided on Formspree yet — I might go with a different service."*

This is not a new correction — OQ-1-08 was already OPEN in the manifest. Alex is confirming an existing open question remains open. Classification: **`APPROVED`** for the field accuracy review. The open question status is unchanged.

But if Alex says: *"Wait — I don't want static anymore. I think I want server-side rendering for the contact form logic."* This is a new scope statement that contradicts a confirmed constraint. Classification: **`RETURNED`** with a scope change flag — this is not a simple field correction; it is a change that invalidates the Workers/Pages resolution and potentially re-opens OQ-1-10.

#### Skills Required

- **Classification before action.** The executor reads the full response before classifying. A response that starts with *"Approved"* and ends with *"but change the appetite"* is `RETURNED`, not `APPROVED`. Reading to the end before classifying prevents partial processing.[^16_1]
- **Explicit approval threshold.** The minimum approval statement: names the document (or is unambiguously in the context of this review), contains the word "approved" or an equivalent deliberate affirmation (*"confirmed"*, *"yes, that's correct"* — not *"fine"* or *"sure"*). This threshold is a policy definition, not a judgment call — the threshold must be stated in the policy.
- **Scope change detection.** A correction that changes a constraint or out-of-scope entry may invalidate prior resolutions. The executor must not treat these as simple field edits — they may require re-running Task 1.2 classification for the affected field.


#### Failure Modes

- **"Looks good to me" classified as `APPROVED`.** The audit log records this as the approval statement. A verifier reading the record cannot confirm a deliberate decision was made. FC-4 Tier 1 requires the approval to be explicit and attributed. *"Looks good"* is neither explicit nor specific to the document.[^16_1]
- **Embedded correction ignored.** Alex says *"Approved — but appetite should be medium."* The executor records `APPROVED` and sets the status. The manifest now has `appetite: small` in an APPROVED document, contradicting Alex's last statement. The correction was never applied.
- **Scope change treated as a simple correction.** Alex says *"Change the static constraint — I want SSR."* The executor updates `constraints` to remove the static entry and re-presents. But removing the static constraint reopens the Workers/Pages question (previously resolved as Pages because static was confirmed). The scope change has downstream consequences that a simple field edit does not capture.


#### Policy Improvements Flagged

- **P-20 (confirmed):** Define minimum explicit approval statement in FC-4 Tier 1.
- **P-19 (confirmed):** Add `UNCLEAR` as a formal third classification with defined follow-up path.
- **New — P-Subtask3-1.5-01:** Add scope change detection to the `RETURNED` classification: if a correction modifies a field whose value was used to resolve a prior BLOCKER entry, the executor must check whether the correction invalidates that resolution before applying it. This is not a new Task 1.2 run — it is a targeted check against the register.

***

### Subtask 4 — Correction Application *(conditional, loops)*

**What is happening:**

Each returned correction is applied. The loop: apply → re-present → re-classify → exit on `APPROVED`. Every pass through the loop is a complete Subtask 2–4 cycle.

**Two types of corrections:**


| Type | Example | Handling |
| :-- | :-- | :-- |
| **Value correction** | *"appetite should be medium, not small"* | Update field value; add correction traceability entry; re-check affected self-check items |
| **Scope addition** | *"I also want to add Tailwind for utility classes"* | Not a value correction — new content; lightweight Task 1.1–1.3 mini-cycle before manifest update |

Value corrections are processed directly. Scope additions require a mini-cycle because they introduce new information that must be classified, potentially clarified, and traced before entering the manifest.

**Value correction processing:**

```yaml
# correction-record-CR-1-01.yaml

correctionid: CR-1-01
step: 1
task: "1.5"
receivedat: "2026-03-07T14:12:00+11:00"
providedby: "Alex Chen"
corrections:
  - field: appetite
    previousvalue: small
    correctedvalue: medium
    basis: "Alex: 'appetite should probably be medium since I said 1–2 weeks'"
```

```yaml
# New traceability entry added (not replacing the old one):
- outputfield: appetite
  valuesummary: "medium"
  sourcetype: correction
  sourcereference: "CR-1-01, field: appetite, receivedat: 2026-03-07T14:12:00+11:00"
  supersedes: "previous entry: sourcetype clarificationanswer, CE-1-01 Q-CE-1-01-07"
```

**The old traceability entry is retained.** The audit trail shows: Task 1.3 produced `small` from *"a few days of focused work."* Task 1.5 received a correction to `medium` from *"I said 1–2 weeks."* Both entries exist. A verifier can reconstruct the complete history of this field.[^16_1]

**The `appetite` correction case is instructive:** Alex's clarification response (*"small — a few days"*) and the correction (*"medium — 1–2 weeks"*) are both Alex's words. They contradict each other. The correction is dated later and attributed to Alex. It takes precedence. The traceability record shows the contradiction was not a process error — it was a human change of mind, recorded and traceable.

**Re-presentation after correction:**

The review package is re-presented with a change summary — not the full package in neutral form:

```
Correction applied:
  appetite: updated from 'small' to 'medium' based on your correction.

The updated manifest is ready for your approval. Please confirm the correction
is accurate and that all other field values remain as previously presented.
```

This confirms to Alex that the correction was applied correctly, and resets their review scope to the changed field — they do not need to re-read every field unchanged from the prior presentation.

#### Skills Required

- **Correction scope containment.** Only the corrected field changes. Adjacent fields that the executor might judge should also change are not touched unless explicitly corrected. If Alex corrects `appetite` to `medium`, the `description` field is not changed — even if the executor judges that the description now sounds too "small."[^16_1]
- **Traceability chain integrity.** The old entry is retained; the new entry is added with `supersedes` referencing the old. Two entries for one field in the traceability record is correct — it is the audit trail. Replacing the old entry loses the history.
- **Loop health monitoring.** After each correction cycle, the executor assesses whether the loop is healthy:
    - Same field corrected twice → `UNSTABLE-FIELD` flag; request definitive statement before re-presenting
    - Three cycles without approval → surface the loop pattern explicitly to Alex; ask what is preventing approval


#### Failure Modes

- **Old traceability entry deleted.** The manifest now shows `appetite: medium` with one traceability entry sourced to the correction. The original `small` entry from Task 1.3 is gone. A verifier cannot confirm that the value changed — it looks as if `medium` was always the value, sourced to a correction record for a correction that apparently changed nothing.
- **Correction applied silently without change summary.** Alex receives the review package again with no indication of what changed. They re-read everything. They may or may not notice the `appetite` change. If they don't, they approve a manifest where the correction may or may not have been applied correctly — they cannot verify.[^16_1]
- **Scope addition treated as value correction.** Alex says *"add Tailwind to the stack."* The executor adds `Tailwind CSS 3.x` to `techstack` and re-presents. But Tailwind was not in `brief-inventory.yaml`, not in any register entry, not in any clarification exchange. Its addition has no traceability source. The traceability entry would need to say `sourcetype: correction, sourcereference: CR-1-01` — which is a valid source. The problem is not the traceability; it is that adding Tailwind may trigger Step 2 consequences (new build tooling, new config entries) that should be classified before being accepted. The distinction between a value correction and a scope addition is consequential, not administrative.


#### Policy Improvements Flagged

- **P-21 (confirmed):** Add scope addition path — corrections introducing new content are separated from value corrections and processed via a lightweight Task 1.1–1.3 mini-cycle.
- **P-22 (confirmed):** `UNSTABLE-FIELD` flag after second correction to the same field.
- **P-23 (confirmed):** Loop escalation trigger after three cycles without approval.
- **New — P-Subtask4-1.5-01:** Change summary is a required element of every re-presentation after correction — not optional. The human must be able to confirm the correction was applied correctly without re-reading unchanged content.

***

### Subtask 5 — Approval Recording

**What is happening:**

The response has been classified as `APPROVED`. Three operations in strict sequence:

**Operation 1 — Validate approver identity**

`approvedby` must match exactly a `humandirector` entry in `humanactors`. Alex's response may come from *"Alex"* (first name only). This must be traced to *"Alex Chen"* in `humanactors` — not assumed. If the name doesn't match exactly, the approval is not valid per FC-4.[^16_1]

**Operation 2 — Update the manifest**

```yaml
# project-manifest.yaml additions:
status: APPROVED
approvedat: "2026-03-07T14:15:00+11:00"    # Alex's response timestamp — not executor processing time
approvedby: "Alex Chen"
```

`approvedat` is the timestamp of Alex's response — not the timestamp of the executor writing these fields. In synchronous interactions these are the same. In asynchronous workflows (document review, email) they may differ significantly. The policy must be explicit: record when the human acted.[^16_1]

**Operation 3 — Write the audit log entry**

```yaml
# FC-4 Tier 1 audit log entry:

actiontype: documentapproved
document: .framework/project-manifest.yaml
actor: "Alex Chen"
timestamp: "2026-03-07T14:15:00+11:00"
documentversion: "DRAFT→APPROVED"
approvalstatement: "Approved — appetite updated to medium, everything else looks right"
reviewrecord: RR-1-01
```

The `approvalstatement` field records Alex's actual words verbatim. This is evidence of a deliberate decision, not a status transition. A verifier reading this entry can confirm that a specific named person explicitly approved a specific document at a specific time using words that constitute deliberate affirmation.[^16_1]

The audit log entry is independent of the manifest field. The manifest field (`status: APPROVED`) is the state indicator. The audit log entry is the proof. Both must exist.[^16_1]

**The manifest is now sealed.** Status APPROVED is a terminal state. Any subsequent edit — however minor — invalidates the approval. If an error is discovered after approval, the only valid path is to return the manifest to DRAFT and re-run Task 1.5 from Subtask 1. There is no *"minor correction"* exception.[^16_1]

**Completing the review record:**

```yaml
# RR-1-01.yaml completed:
respondedat: "2026-03-07T14:15:00+11:00"
responseclassification: APPROVED
response: "Approved — appetite updated to medium, everything else looks right"
correctionapplied: CR-1-01
auditlogentry: "documentapproved-2026-03-07T14:15:00"
```


#### Skills Required

- **`approvedby` exact-match validation.** Not *"close enough."* The value must match the `humanactors` entry exactly. A discrepancy must be resolved before the approval is recorded — not after.
- **`approvedat` as human action timestamp.** The executor's clock at the time of processing is not the evidence. Alex's response timestamp is. In any system where responses are queued, batched, or delayed in transit, the two timestamps may differ. The policy must require the human's action timestamp, not the processing timestamp.[^16_1]
- **Post-approval immutability.** After writing `status: APPROVED`, the executor must not write any further field values to the manifest — not even the traceability record, which was already complete at DRAFT time. Any change to the manifest after APPROVED status invalidates the approval. If a traceability correction is needed post-approval, it goes into a separate correction record, not into the sealed document.


#### Failure Modes

- **`approvedat` set to executor processing time.** In a synchronous chat, this may be seconds off — inconsequential. In an asynchronous workflow where Alex emails an approval and the executor processes it hours later, the `approvedat` may be off by hours. The audit trail then misrepresents the timeline of the approval.[^16_1]
- **`approvedby: "humandirector"`** — role title rather than named person. FC-4 requires attribution to a named human. A role title does not survive personnel changes; it is not independently verifiable. *"Alex Chen"* is verifiable. *"humandirector"* is not.[^16_1]
- **Traceability update after APPROVED.** The executor notices a traceability entry is incomplete and updates `project-manifest.traceability.yaml` after setting `status: APPROVED`. The manifest document is unchanged — but the companion record, which together with the manifest constitutes the verified output, has been modified post-approval. The approved state is no longer fully sealed.


#### Policy Improvements Flagged

- **CC-09 (confirmed):** Add `approvalstatement` as a required FC-4 Tier 1 field — verbatim, minimum 5 words.
- **CC-10 (confirmed):** Explicit guidance that `approvedat` records the human's action timestamp, not the executor's processing timestamp. In asynchronous workflows, these must be explicitly distinguished.
- **New — P-Subtask5-1.5-01:** Extend the post-approval immutability rule to the traceability companion record: once `status: APPROVED` is set, neither the manifest nor its companion traceability record may be modified. Any post-approval correction requires re-opening to DRAFT and completing a full Task 1.5 re-run.

***

## Step 3 — Sanity Check

### Step 1 DoD — All nine conditions checked against the completed artefacts[^16_1]

| DoD | Condition | Met? |
| :-- | :-- | :-- |
| 1 | `project-manifest.yaml` exists at `.framework/project-manifest.yaml` | ✓ |
| 2 | `status: APPROVED` | ✓ — set at Task 1.5 Subtask 5 |
| 3 | All required fields non-empty | ✓ — self-check item 1 passed |
| 4 | Every field value traceable to a source | ✓ — companion traceability record covers all fields |
| 5 | No value was invented | ✓ — all values trace to brief, clarification, or documented derivation |
| 6 | Every gap in `openquestions` with classification | ✓ — 5 entries (2 WARNING, 3 INFO) |
| 7 | All contradictions resolved before drafting | ✓ — C-01 resolved via CE-1-01 Q-CE-1-01-05 |
| 8 | APPROVED set by Alex's explicit action, not by the process | ✓ — audit log entry independent of manifest field |
| 9 | `approvedat` and `approvedby` present and consistent with `humanactors` | ✓ |

All nine pass. Step 1 is complete.

***

## Done When — Task 1.5

Task 1.5 is complete when all eight conditions are simultaneously true:

1. `project-manifest.yaml` exists with `status: APPROVED`
2. `approvedat` contains the datetime of Alex's approval response — not executor processing time
3. `approvedby` exactly matches a `humandirector` entry in `humanactors`
4. An audit log entry exists for this approval, independent of the manifest field, with `approvalstatement` containing Alex's verbatim words
5. `RR-1-01.yaml` exists at `.framework/reviews/` with `respondedat` and `responseclassification: APPROVED` populated
6. Any corrections applied have a corresponding `CR-1-xx.yaml` correction record and new traceability entries with `sourcetype: correction`
7. No manifest field or companion traceability record has been modified after `status: APPROVED` was set
8. The review record references the audit log entry and any correction records applied during the review loop

***

## Task 1.2 Through 1.5 — What This Session Added

Compared to the previous session's analysis of the same tasks, this session produced materially tighter outputs across four dimensions:

**Artefact precision.** Every artefact now has a canonical path, a defined schema, and a clear consumer. The distinction between CE (clarification exchange), RR (review record), and CR (correction record) as separate artefact types with different schemas and purposes was not present in the previous session's analysis.

**Subtask sequencing.** Pre-drafting derivation resolution (Task 1.4 Subtask 1) emerged cleanly because the `derivation_flag` field was decided before analysis began. The session structure — decisions first, analysis second — directly produced a cleaner result.

**The case study grounded every design decision.** The `@astrojs/react` implicit dependency surfaced because we were populating actual `techstack` entries, not describing them abstractly. The `pnpm` duplication question surfaced because we were writing both `techstack` and `devenvironment` in sequence.

**New findings this session:** DQ-05 (derivation worklog folded into traceability record), DQ-06 (pnpm duplication allowed with explicit note), and seven new policy improvements (P-Subtask1-PreDraft-01, P-Subtask2-01, P-Subtask3-01, P-Subtask1-1.5-01, P-Subtask3-1.5-01, P-Subtask4-1.5-01, P-Subtask5-1.5-01) not in the previous session's consolidated findings.

***

Ready to compile the full findings for this session, or proceed directly to the retro?

<div align="center">⁂</div>

[^16_1]: i-am-making-progress-in-creati-fuGLU8hCRLyka3xtBTVglA.md


---

# Compile the findings, templates, schema, policy improvements, open questions, other questions etc

This will be a comprehensive compilation. Let me organise it into discrete sections covering everything produced across Tasks 1.2–1.5.

***

# Session Findings — Step 1, Tasks 1.2–1.5

**Session scope:** Task 1.2 Gap Classification → Task 1.3 Clarification Resolution → Task 1.4 Manifest Drafting → Task 1.5 Human Review
**Session date:** 7 March 2026
**Status:** Draft — pending review

***

## Part 1 — Decisions Confirmed This Session

These were confirmed at the start and treated as fixed throughout the analysis.


| ID | Decision | Effect |
| :-- | :-- | :-- |
| **D-01** | Vocabulary: `BLOCKER / WARNING / INFO` (three tiers) | Replaces policy's `BLOCKING / OPENQUESTION / WARNING / LOWRISK` across all Task 1.x analysis |
| **D-02** | "OPENQUESTION" is a role/status, not a severity label | Non-blocking entries are `WARNING` or `INFO`; they carry forward in the register |
| **D-03** | Task 1.2 output is `open-questions-register.yaml` — not a separate ad-hoc gap list | Register created in Task 1.2 and persists through all six steps per FC-8 |
| **D-04** | Task 1.2 input is `brief-inventory.yaml` exactly as shaped in Task 1.1 | All classification work is expressed as queries over its four arrays |
| **D-05** | Task 1.2 has four subtasks — required fields, optional fields, contradictions, non-mappable | Non-mappable classification is an explicit fourth subtask, not implied |
| **DQ-01** | `linked_questions` populated in a single bidirectional pass at end of Subtask 3 — not retroactively during subtask execution | Prevents orphaned linkages and retroactive record updates |
| **DQ-04** | `derivation_flag` retained in exchange record as machine-queryable signal | Redundancy with `resolutionnote` is intentional — one for human reading, one for agent querying |
| **DQ-05** | Derivation worklog folded into traceability record (Option B) | No separate worklog artefact; derivation entries use `sourcetype: derivationrule` in the traceability record |
| **DQ-06** | `pnpm` (and any package manager) may appear in both `techstack` and `devenvironment.packagemanager` | Each field serves a different downstream consumer; duplication is intentional with a single shared source reference |


***

## Part 2 — Artefact Schemas

### 2.1 `brief-inventory.yaml` *(confirmed shape from Task 1.1)*

Filed at: `.framework/brief-inventory.yaml`

```yaml
statements:
  - id: S-xx
    text: "..."
    clarity: CLEAR | AMBIGUOUS
    candidate_fields: [field_name, ...]

fields:
  - field: fieldname
    required: true | false
    coverage: PRESENT | ABSENT | AMBIGUOUS-INCOMPLETE | AMBIGUOUS-FORMAT
    supporting_statements: [S-xx, ...]

non_mappable:
  - statement_id: S-xx
    downstream_note: "..."

contradictions:
  - id: C-xx
    statement_ids: [S-xx, S-xx]
    description: "..."
    affected_fields: [fieldname, ...]
```


***

### 2.2 `open-questions-register.yaml` *(created Task 1.2)*

Filed at: `.framework/open-questions-register.yaml`

```yaml
# Created: Step 1, Task 1.2
# Last modified by step: 1
# Persists through: Steps 1–6

questions:
  - questionid: OQ-{step}-{seq}         # e.g. OQ-1-01 — IMMUTABLE once set
    field: fieldname | null              # null for non-mappable/schema-gap entries
    gap_type: ABSENT
                | AMBIGUOUS-INCOMPLETE
                | AMBIGUOUS-FORMAT
                | CONTRADICTION
                | SCHEMA-GAP
    gap: "one sentence"                  # IMMUTABLE once set
    impact: "one sentence"               # names specific downstream field or DoD criterion
    source_statements: [S-xx]            # from brief-inventory.statements
    contradiction_ref: C-xx              # only for gap_type: CONTRADICTION
    classification: BLOCKER | WARNING | INFO
    linked_questions: [OQ-x-xx]          # bidirectional; populated in linking pass after Subtask 3
    schema_gap_flag: true | false        # true when no manifest field exists for this information
    candidate_field: fieldname           # when schema_gap_flag: true
    raisedbystep: 1                      # IMMUTABLE once set
    lastupdatedbystep: 1                 # mutable — updated by any step that reclassifies
    currentowner: 1                      # step currently responsible for resolution
    resolutionstatus: OPEN
                    | RESOLVED
                    | CONFIRMED-UNKNOWN
                    | DECISION-REQUIRED
                    | ACCEPTED-AS-KNOWN-GAP
    resolutionnote: null                 # populated at resolution; includes raw response and derivation notes
    resolvedbystep: null
    resolvedatexchange: null             # CE-x-xx reference
```

**Immutability rules:**

- `questionid`, `gap`, `raisedbystep` — never modified after creation
- `classification`, `currentowner`, `impact`, `lastupdatedbystep` — mutable by any subsequent step per FC-8

***

### 2.3 `CE-1-xx.yaml` — Clarification Exchange Record *(created Task 1.3)*

Filed at: `.framework/clarifications/CE-1-01.yaml`

```yaml
exchangeid: CE-{step}-{seq}              # e.g. CE-1-01
step: 1
initiatedat: "ISO 8601"                  # set at moment of delivery — NOT post-response
questions:
  - questionid: Q-CE-1-01-{seq}
    register_refs: [OQ-x-xx]            # all register entries this question covers
    field: fieldname
    gap_type: AMBIGUOUS-INCOMPLETE | AMBIGUOUS-FORMAT | CONTRADICTION
    questiontext: "..."                  # max 25 words; one sentence
    impactstatement: "..."               # one sentence
    derivation_flag: false               # true when response authorises a derivation, not a specific value
respondedat: null                        # set when Alex responds
responses:
  - questionid: Q-CE-1-01-{seq}
    responsetext: "..."                  # verbatim
    resolution: RESOLVED | CONFIRMED-UNKNOWN | DECISION-REQUIRED | UNCLEAR
    derivation_flag: true | false
    enum_mapping: value                  # when gap_type AMBIGUOUS-FORMAT
    linked_cascade: [OQ-x-xx]           # entries updated as part of linked resolution
```


***

### 2.4 `RR-1-xx.yaml` — Review Record *(created Task 1.5, new this session)*

Filed at: `.framework/reviews/RR-1-01.yaml`

Distinct from CE records — FC-4 Tier 1 artefact for human approval, not FC-3 clarification.

```yaml
reviewid: RR-{step}-{seq}
step: 1
document: .framework/project-manifest.yaml
documentstatus: DRAFT
presentedto: "Alex Chen"
presentedat: "ISO 8601"                  # set at moment of delivery
summaryvalidated: true | false           # summary-vs-manifest check passed before delivery
openquestionsincluded: [OQ-x-xx]        # all OPEN entries included in Part 2 of review package
respondedat: null
responseclassification: APPROVED | RETURNED | UNCLEAR
response: null                           # verbatim
followuprequestedat: null                # set if UNCLEAR requires follow-up
correctionapplied: null                  # CR-x-xx reference if RETURNED
auditlogentry: "actiontype-timestamp"    # reference to FC-4 audit log entry
```


***

### 2.5 `CR-1-xx.yaml` — Correction Record *(created Task 1.5, new this session)*

Filed at: `.framework/corrections/CR-1-01.yaml`

```yaml
correctionid: CR-{step}-{seq}
step: 1
task: "1.5"
receivedat: "ISO 8601"
providedby: "Alex Chen"
correctiontype: VALUE-CORRECTION | SCOPE-ADDITION
corrections:
  - field: fieldname
    previousvalue: "..."
    correctedvalue: "..."
    basis: "verbatim from Alex's response"
scopeaddition:                           # only for correctiontype: SCOPE-ADDITION
  description: "..."
  requires_mini_cycle: true | false
  mini_cycle_tasks: [1.1, 1.2, 1.3]
```


***

### 2.6 `project-manifest.traceability.yaml` *(FC-5, confirmed and extended)*

Filed at: `.framework/traceability/project-manifest.traceability.yaml`

```yaml
# Written field-by-field during drafting — NOT after
# Retained permanently after approval
# Extended sourcetypes this session:

entries:
  - outputfield: "exact field name | techstack[^17_0] | corrections[n]"
    valuesummary: "first 30 chars of value"
    sourcetype: brief
              | clarificationanswer
              | manifestfield
              | contractfield
              | seedingresource
              | derivationrule
              | correction          # NEW — for corrections applied in Task 1.5
              | notpresentininput
    sourcereference: "specific locator"
    supersedes: "prior entry reference"  # NEW — when a correction replaces a prior value
```

**New `sourcetype` values confirmed this session:** `correction`, plus `supersedes` field for correction chains.

***

### 2.7 FC-4 Tier 1 Audit Log Entry *(confirmed and extended)*

```yaml
actiontype: documentapproved
document: .framework/project-manifest.yaml
actor: "Alex Chen"                       # named person — NOT role title
timestamp: "ISO 8601"                    # human's action timestamp — NOT executor processing time
documentversion: "DRAFT→APPROVED"
approvalstatement: "verbatim words"      # NEW — minimum 5 words, required
reviewrecord: RR-1-01
```


***

## Part 3 — Policy Improvements

Organised by task. Each entry includes: ID, description, classification (NEW vs CONFIRMED from prior sessions), and which policy document it affects.

***

### Task 1.2 — Gap Classification

| ID | Description | Type | Affects |
| :-- | :-- | :-- | :-- |
| **P-04** | Task 1.2 policy must explicitly state the executor must have loaded Step 2 and Step 3 policy documents as reference material before applying Gate 1. Gate 1 is not guesswork — it requires knowledge of what each downstream step needs per field. | CONFIRMED | Task 1.2 policy |
| **P-01** | Add `gap_type` as a required field in the open-questions register schema. Values: `ABSENT`, `AMBIGUOUS-INCOMPLETE`, `AMBIGUOUS-FORMAT`, `CONTRADICTION`, `SCHEMA-GAP`. Distinguishes gap character upstream, shapes question formulation in Task 1.3 without re-derivation. | CONFIRMED | Register schema, FC-8 |
| **S-05** | Add a conditional sections table to the manifest template metadata. Maps tech stack patterns to triggered optional manifest sections (e.g. form handler reference → `integrationrequirements` conditionally required). Makes Subtask 2 a table lookup, not a judgment call. | CONFIRMED | Manifest template |
| **P-Subtask2-01** | The Done condition for Task 1.2 Subtask 2 must require explicit confirmation that every optional field was assessed — not just that entries were created for the ones that triggered classification. Silent skipping of ABSENT optional fields with "no impact" produces a register that appears complete but is not. | NEW | Task 1.2 policy, DoD |
| **P-07** | Add Subtask 4 (non-mappable statement classification) explicitly to the Task 1.2 policy. Currently absent. Non-mappable statements with downstream consequences must not disappear after Task 1.1. | CONFIRMED | Task 1.2 policy |
| **P-Subtask4-01** | The Done condition for Task 1.2 Subtask 4 must require the executor to confirm explicitly that every entry in `non_mappable[]` was assessed — either producing a register entry or recording a documented no-entry decision. Silent skipping is not detectable without this requirement. | NEW | Task 1.2 policy, DoD |
| **CC-05** | Add `schema_gap_flag` (boolean) and `candidate_field` (string) as optional register fields. `schema_gap_flag: true` creates a structured feedback loop for manifest template evolution. Without the flag, schema gaps are in the register but produce no signal for template improvement. | CONFIRMED | Register schema, FC-8 |
| **P-Linking-01** | The bidirectional `linked_questions` linking pass must be an explicit named step at the end of Task 1.2 Subtask 3 (not implied). Procedure: for each register entry, query all entries referencing its `questionid` in their `linked_questions` field; set linkages bidirectionally. | NEW | Task 1.2 policy, Subtask 3 |
| **P-03** | Add `POTENTIAL-CONTRADICTION` as a WARNING-level flag for contradictions that require domain expertise to confirm. Enters the register with `contradiction_flag: true`, escalated to BLOCKER if confirmed during clarification. Prevents domain-knowledge-dependent contradictions from being silently missed. | CONFIRMED | FC-2, Register schema |


***

### Task 1.3 — Clarification Resolution

| ID | Description | Type | Affects |
| :-- | :-- | :-- | :-- |
| **P-09** | Instructional context rule for question formulation: parenthetical retrieval instructions are permitted in questions (e.g. "Run `node --version` to check") provided they are not compound questions or decision prompts. Without this rule, Q6 for Node.js version is almost certain to produce `CONFIRMED-UNKNOWN` from a human who could find the answer with one command. | CONFIRMED | FC-3, Task 1.3 policy |
| **P-Subtask1-01** | Formalise the `gap_type` → question type mapping in Task 1.3 policy. `AMBIGUOUS-INCOMPLETE` → value-retrieval question; `AMBIGUOUS-FORMAT` → choice-based question presenting valid options; `CONTRADICTION` → disambiguation question naming both interpretations. Makes question formulation deterministic rather than a judgment call. | NEW | Task 1.3 policy, FC-3 |
| **P-Subtask1-02** | The exchange record shell must be created and filed before delivery. `initiatedat` is set at the moment of sending — these are the same moment. Any gap between record creation and delivery is an audit integrity issue. The policy must state this explicitly. | NEW | Task 1.3 policy, FC-3 |
| **P-Subtask1-03** | Clarify the apparent tension in the policy between "one question per item, not a consolidated list" and "all blocking gaps in one batch exchange." These are not contradictory. Correct statement: *"One question per gap — each gap produces exactly one question — all questions delivered in a single batch exchange."* Current wording allows misreading. | NEW | Task 1.3 policy, FC-3 |
| **P-08** | Response classification (`RESOLVED` / `CONFIRMED-UNKNOWN` / `DECISION-REQUIRED` / `UNCLEAR`) must be a formal, named first step of Task 1.3 Subtask 3 — before any register update. Classify before act is the invariant. | CONFIRMED | Task 1.3 policy |
| **P-10** | Linked entry propagation must be an explicit named step in Task 1.3 Subtask 3: "For each RESOLVED entry, query the register for all entries with this entry's `questionid` in their `linked_questions` field and apply the same resolution, citing the same exchange reference." Without this, a resolved contradiction leaves its linked ambiguity entry in OPEN status. | CONFIRMED | Task 1.3 policy |
| **P-11** | "Latest stable" and equivalent deferred version references are valid `RESOLVED` responses but require `derivation_flag: true` in the exchange record and an explicit derivation note in `resolutionnote`. Task 1.4 must not treat these as final values — they require version resolution before field population. | CONFIRMED | Task 1.3 policy, Task 1.4 policy |
| **P-Subtask3-01** | Define `UNCLEAR` response handling: identify the single follow-up question that resolves the ambiguity; re-present to Alex; `initiatedat` timestamp of the original exchange does not change; a `followuprequestedat` timestamp is added to the exchange record. | NEW | Task 1.3 policy |
| **P-Subtask3-02** | Define `DECISION-REQUIRED` response handling in full: entry remains BLOCKER, process enters `AWAITING-DECISION` state, a decision-request note is created. This is not a clarification exchange — FC-3 does not cover undecided information. Undecided technical choices require explicit framework support outside FC-3. Flag as UQ-03. | NEW | Task 1.3 policy, FC-3 |


***

### Task 1.4 — Manifest Drafting

| ID | Description | Type | Affects |
| :-- | :-- | :-- | :-- |
| **P-13** | Add pre-drafting derivation resolution as an explicit Subtask 1 in Task 1.4. Before any manifest field is written: query `CE-1-xx.yaml` for `derivation_flag: true` entries; resolve each to a specific value; record in the traceability record with `sourcetype: derivationrule`. Only then begin field population. | CONFIRMED | Task 1.4 policy |
| **P-Subtask1-PreDraft-01** | The policy must specify handling when version lookup is unavailable during pre-drafting resolution: the value becomes `CONFIRMED-UNKNOWN`, the register entry is updated to reflect this, and the field is written as empty with an `openquestions` entry. Guessing a version number is not a fallback. | NEW | Task 1.4 policy |
| **P-15** | Add selection criteria for `description` field assembly to the policy: include project type, primary purpose, key deliverable. Exclude constraints, deployment details, and named actors — these have dedicated fields. Every sentence must trace to a brief statement. The executor's voice does not appear. | CONFIRMED | Task 1.4 policy |
| **P-Subtask2-01** | Version-less `techstack` entries discovered during field population (e.g. `pnpm` version not confirmed) are treated the same as pre-drafting derivations: pause field population, create a register entry, resolve via derivation, then write. The pre-drafting step may not have caught every derivation-dependent field. | NEW | Task 1.4 policy |
| **S-03** | Clarify in the manifest schema whether package managers belong in `techstack`, `devenvironment.packagemanager`, or both. Confirmed decision (DQ-06): duplication is permitted and intentional. The schema should document this explicitly so it is not interpreted as an error by a verifier. | CONFIRMED | Manifest schema |
| **P-Subtask3-01** | Add an explicit rule that AMBIGUOUS optional fields are recorded with the ambiguity and a register cross-reference — not as confirmed values and not as empty fields. The `integrationrequirements` case (tentative Formspree) is the model: record what was said, note it is tentative, reference the open question ID. | NEW | Task 1.4 policy |


***

### Task 1.5 — Human Review

| ID | Description | Type | Affects |
| :-- | :-- | :-- | :-- |
| **P-18** | Summary generation rule: the review package summary is generated deterministically from the manifest. Before delivery, every summary value is validated against its corresponding manifest field. A rendering error means Alex approves a summary that doesn't match the canonical document. Validation is a required step. | CONFIRMED | Task 1.5 policy |
| **P-Subtask1-1.5-01** | The review instruction must explicitly name what a returned correction looks like: *"identify the specific field and the correct value."* Without this, Alex may return a correction as a vague statement that cannot be classified as `RETURNED` without a follow-up. | NEW | Task 1.5 policy |
| **P-19** | Add `UNCLEAR` as a formal third response classification in Task 1.5 Subtask 3, with a defined follow-up path. Matches the pattern established in Task 1.3. Examples of `UNCLEAR`: *"Looks good to me"*, *"Mostly right but not sure about the tech stack."* | CONFIRMED | Task 1.5 policy |
| **P-20** | Define minimum explicit approval statement for FC-4 Tier 1. The response must: name the document (or be unambiguously in the context of the review), and contain a deliberate affirmation — "approved," "confirmed," "yes, that's correct" are valid. "Fine," "sure," "looks good" are not sufficient. This is a policy definition, not a judgment call. | CONFIRMED | Task 1.5 policy, FC-4 |
| **P-Subtask3-1.5-01** | Add scope change detection to the `RETURNED` classification. If a correction modifies a field whose value was used to resolve a prior BLOCKER register entry, the executor must check whether the correction invalidates that resolution before applying it. Example: removing the static constraint re-opens the Workers/Pages question (OQ-1-10). This is a targeted register check, not a full Task 1.2 re-run. | NEW | Task 1.5 policy |
| **P-21** | Add a scope addition path for Task 1.5 corrections. Corrections that introduce new content (not a value change to an existing field) are separated from value corrections and processed via a lightweight Task 1.1–1.3 mini-cycle before the manifest is updated. | CONFIRMED | Task 1.5 policy |
| **P-22** | Add `UNSTABLE-FIELD` flag after the same field is returned for correction twice in the same Task 1.5 loop. When triggered: request a definitive statement from Alex on that specific field before re-presenting the full manifest. | CONFIRMED | Task 1.5 policy |
| **P-23** | Add loop escalation trigger after three Task 1.5 correction cycles without approval. When triggered: surface the loop pattern explicitly to Alex; ask what is preventing approval. Do not continue silent cycling. | CONFIRMED | Task 1.5 policy |
| **P-Subtask4-1.5-01** | Change summary is a required element of every re-presentation after a correction — not optional. Format: names the field, the previous value, and the corrected value. Allows Alex to confirm the correction was applied correctly without re-reading unchanged content. | NEW | Task 1.5 policy |
| **CC-09** | Add `approvalstatement` as a required field in FC-4 Tier 1 audit log entries. Contains Alex's verbatim approval words. Minimum 5 words. This is the evidence of a deliberate decision — a status field alone is a state indicator, not proof. | CONFIRMED | FC-4 |
| **CC-10** | `approvedat` must record the human's action timestamp — the datetime of Alex's response — not the executor's processing timestamp. In asynchronous workflows these may differ significantly. The policy must make this distinction explicit and require the human's timestamp. | CONFIRMED | FC-4, Task 1.5 policy |
| **P-Subtask5-1.5-01** | Extend the post-approval immutability rule to the companion traceability record. Once `status: APPROVED` is set, neither `project-manifest.yaml` nor `project-manifest.traceability.yaml` may be modified. Any post-approval correction requires returning to DRAFT and completing a full Task 1.5 re-run. | NEW | Task 1.5 policy, FC-1, FC-5 |


***

## Part 4 — New Artefact Types Confirmed This Session

Two artefact types not previously defined:


| Artefact | Series | Purpose | Distinct from |
| :-- | :-- | :-- | :-- |
| Review Record | `RR-{step}-{seq}` | FC-4 Tier 1 approval record — documents the human review exchange: what was presented, when, what the response was, and what audit log entry it produced | CE records (those are FC-3 gap resolution, not approval) |
| Correction Record | `CR-{step}-{seq}` | Documents each RETURNED correction: field, previous value, corrected value, basis, and whether it is a value correction or scope addition | Not embedded in the review record — separate artefact so corrections are independently queryable |

The distinction between CE, RR, and CR series must be made explicit in the framework's document taxonomy (FC-8 / context tree).

***

## Part 5 — Skill Requirements by Task

Compiled from all subtask analyses. These are the loaded prerequisites an executor must have before beginning each task.

### Task 1.2

- Step 2 and Step 3 policy documents loaded as reference — Gate 1 cannot be applied without them
- FC-2 three-tier classification and Gate sequence
- Manifest schema — required vs optional field distinction, conditional requirement rules
- One-gap-one-entry discipline — if two gaps produce different clarification questions, they are different entries
- Domain knowledge of the declared tech stack — to detect domain-level contradictions


### Task 1.3

- `gap_type` → question type mapping (AMBIGUOUS-INCOMPLETE → value-retrieval; AMBIGUOUS-FORMAT → choice; CONTRADICTION → disambiguation)
- FC-3 compound question prohibition — one sentence, max 25 words, one gap per question
- FC-3 batch delivery rule — all questions in one exchange
- Linked group detection procedure — check `linked_questions` before formulating any question
- Response classification taxonomy before any register write
- Linked cascade execution after each `RESOLVED` response


### Task 1.4

- Pre-drafting derivation resolution — derivation_flag query before field one
- Version lookup capability or defined fallback when unavailable
- Step 2 schema knowledge — to detect implicit dependencies (e.g. `@astrojs/react`) during population
- Traceability-alongside-field discipline — one operation, two writes
- Description assembly rule — fidelity to brief language, no editorial voice
- Conditional sections table (S-05) — or equivalent domain knowledge


### Task 1.5

- Summary fidelity validation — deterministic rendering, value-by-value check before delivery
- Minimum explicit approval threshold — must be a loaded definition, not a judgment call
- Scope change detection — must know which register entries were used to resolve prior BLOCKERs
- Post-approval immutability — no writes to manifest or traceability record after APPROVED

***

## Part 6 — Failure Mode Catalogue

The most consequential failure modes across all four tasks:


| Task | Subtask | Failure Mode | Downstream consequence |
| :-- | :-- | :-- | :-- |
| 1.2 | Subtask 1 | Multiple `techstack` gaps collapsed into one entry | Task 1.3 asks one compound question; answer is a paragraph; downstream decomposition re-does Task 1.2 work |
| 1.2 | Subtask 1 | `appetite` classified non-BLOCKER because Step 2 doesn't use it | Gate 3 not applied; question never asked; Task 1.4 invents enum value; manifest fails DoD 3 |
| 1.2 | Subtask 1 | `deploymenttarget` classified PRESENT because "Cloudflare Workers" is explicit | Ambiguity between Workers and Pages undetected; wrong adapter used in Step 2 |
| 1.2 | Subtask 3 | Contradiction downgraded to WARNING using domain knowledge | Contradiction never reaches human; one side of an unresolved conflict enters the manifest |
| 1.2 | Subtask 3 | OQ-1-05/OQ-1-10 linkage not set bidirectionally | Task 1.3 asks two questions about the same issue; human receives duplicate questions |
| 1.2 | Subtask 4 | Non-mappable subtask skipped entirely | S-13 (Cloudflare account readiness) disappears; Step 2 incorrectly assumes DNS procurement needed |
| 1.3 | Subtask 1 | Compound question for `deploymenttarget` + SSR | FC-3 violation; design preference embedded in clarification question |
| 1.3 | Subtask 3 | OQ-1-10 not cascade-updated after OQ-1-05 RESOLVED | Manifest exits with one resolved and one unresolved entry for the same underlying issue |
| 1.3 | Subtask 3 | "Latest stable" treated as a final value | Task 1.4 writes placeholder into manifest; format rule violated; Step 2 receives non-specific version |
| 1.3 | Subtask 3 | `UNCLEAR` treated as `RESOLVED` | Hedged answer produces incorrect register value; error propagates into manifest |
| 1.4 | Subtask 1 | Pre-drafting step skipped | AstroJS and Shadcn version placeholders survive into DRAFT manifest |
| 1.4 | Subtask 2 | `@astrojs/react` not detected as implicit dependency | `techstack` incomplete; Step 2 `framework.integrations` section cannot be written |
| 1.4 | Subtask 2 | Traceability written after manifest rather than alongside | `description` source attribution unreliable; assembled field provenance becomes reconstruction |
| 1.4 | Subtask 3 | `integrationrequirements` populated with `provider: Formspree` | Unconfirmed provider becomes a manifest value; Step 2 builds integration section around an invented choice |
| 1.4 | Subtask 5 | Self-check run after `status: DRAFT` is set | DRAFT signals readiness; unverified manifest reaches Task 1.5 review |
| 1.5 | Subtask 1 | Part 2 (open questions) omitted from review package | Alex approves without knowing about WARNING-level gaps; approval not informed consent |
| 1.5 | Subtask 3 | "Looks good to me" classified as `APPROVED` | FC-4 audit record lacks explicit deliberate affirmation; approval is not independently verifiable |
| 1.5 | Subtask 3 | Embedded correction ignored | APPROVED set; manifest contains value Alex explicitly said was wrong in their approval response |
| 1.5 | Subtask 4 | Old traceability entry deleted when correction applied | History of field change lost; verifier cannot confirm the value changed rather than always being the corrected value |
| 1.5 | Subtask 5 | `approvedat` set to executor processing time | Audit trail misrepresents the timeline; particularly significant in asynchronous workflows |
| 1.5 | Subtask 5 | `approvedby: "humandirector"` (role title) | FC-4 requires named person attribution; role title is not independently verifiable |
| 1.5 | Post-approval | Traceability record updated after `status: APPROVED` | Companion record modified post-seal; approved state no longer fully intact |


***

## Part 7 — Done When Conditions

### Task 1.2

1. `open-questions-register.yaml` exists at `.framework/open-questions-register.yaml`
2. Every `fields[]` entry with coverage `ABSENT` or `AMBIGUOUS-*` has a corresponding register entry
3. Every `contradictions[]` entry has a `BLOCKER` register entry
4. Every `non_mappable[]` entry has either a register entry or a documented no-entry decision in the executor's worklog
5. All `linked_questions` fields are bidirectionally populated — completed in the linking pass at end of Subtask 3
6. All entries have `resolutionstatus: OPEN` and `currentowner: 1`

### Task 1.3

1. `CE-1-01.yaml` exists at `.framework/clarifications/` with `respondedat` populated
2. Every question in the exchange record has a corresponding response entry
3. Every BLOCKER register entry has `resolutionstatus` of `RESOLVED`, `CONFIRMED-UNKNOWN`, or `DECISION-REQUIRED` — no remaining `OPEN` BLOCKER entries
4. All `RESOLVED` entries have a `resolutionnote` specific enough to populate the manifest field, or flagged as a named derivation with `derivation_flag: true`
5. All linked entry cascades have been applied — no linked pair with mismatched resolution statuses
6. `CONFIRMED-UNKNOWN` entries have been reclassified from BLOCKER to WARNING per FC-2 downgrade rules

### Task 1.4

1. `project-manifest.yaml` exists at `.framework/project-manifest.yaml` with `status: DRAFT`
2. All required fields are non-empty
3. No `techstack` entry contains a placeholder value (`latest stable`, `TBD`, `x.x`)
4. All optional fields are present — populated with confirmed values, or explicitly recorded as `[]` / `null`
5. All `OPEN` register entries with classification `WARNING` or `INFO` appear in the manifest's `openquestions` field
6. `project-manifest.traceability.yaml` exists and covers every non-empty field
7. All 15 self-check items passed before `status: DRAFT` was set
8. `approvedat` and `approvedby` are absent

### Task 1.5

1. `project-manifest.yaml` exists with `status: APPROVED`
2. `approvedat` contains the datetime of Alex's approval response — not executor processing time
3. `approvedby` exactly matches a `humandirector` entry in `humanactors`
4. An FC-4 audit log entry exists for this approval, independent of the manifest field, with `approvalstatement` containing Alex's verbatim words (minimum 5 words)
5. `RR-1-01.yaml` exists at `.framework/reviews/` with `respondedat` and `responseclassification: APPROVED` populated
6. Any corrections applied have a corresponding `CR-1-xx.yaml` and new traceability entries with `sourcetype: correction` and `supersedes` referencing the prior entry
7. No manifest field or traceability companion record was modified after `status: APPROVED` was set
8. The review record references the audit log entry and any correction records applied during the loop

***

## Part 8 — Open Questions / Unresolved Items

### Unresolved Design Questions (carried forward)

| ID | Question | Stakes | Deferred to |
| :-- | :-- | :-- | :-- |
| **DQ-02** | Is an INFO entry for `existingassets: ABSENT` worth creating — register noise vs completeness record? | Low | Framework-level decision on register scope: actionable findings only vs complete assessment record |
| **DQ-03** | The Meridian register has 13 entries from a simple brief. A complex brief could produce 30+. Is there a maximum batch size for FC-3 exchanges? Should BLOCKERs be prioritised before WARNINGs? | Medium | FC-3 policy extension |
| **UQ-03** | `DECISION-REQUIRED` handling: when Alex has not decided (not missing declared information), FC-3 does not apply. What framework mechanism handles undecided technical choices? Step blocks until a decision is made — but no protocol is defined for what happens next. | High — blocks Task 1.3 in this scenario | Framework-level; flag for FC-3 extension |

### Questions Confirmed Settled This Session

| ID | Question | Settlement |
| :-- | :-- | :-- |
| **DQ-01** | When does `linked_questions` get populated for Subtask 1 entries created before Subtask 3 runs? | Option B: single bidirectional linking pass at end of Subtask 3 |
| **DQ-04** | Retain `derivation_flag` in exchange record? | Yes — machine-queryable signal for Task 1.4 pre-drafting step |
| **DQ-05** | Derivation worklog as formal artefact or internal only? | Option B: fold into traceability record as `sourcetype: derivationrule` entries |
| **DQ-06** | Should `pnpm` appear in both `techstack` and `devenvironment.packagemanager`? | Yes — duplication intentional, documented in schema, single shared source reference |


***

## Part 9 — Cross-Cutting Policy Implications

Items that surfaced during Task 1.2–1.5 analysis which affect FC policies, not just step policies.


| FC Policy | Implication | Session evidence |
| :-- | :-- | :-- |
| **FC-2** | Gate 3 (required field validity) must be documented as a separate, independent gate alongside Gates 1 and 2. The `appetite` case demonstrates that a required field can fail Gate 3 while returning NO on Gate 1 — Gate 2-only classification misses it. | Task 1.2 Subtask 1, `appetite` entry |
| **FC-2** | `POTENTIAL-CONTRADICTION` as a WARNING-level pre-flag for domain-knowledge-dependent contradictions. Not all contradictions are detectable without domain expertise. | Task 1.2 Subtask 3, Workers/static case |
| **FC-3** | Parenthetical retrieval instructions permitted — not compound questions. Max 25-word rule should explicitly carve out single-sentence retrieval instructions. | Task 1.3 Subtask 1, Q6 Node.js case |
| **FC-3** | `DECISION-REQUIRED` is not covered by FC-3. FC-3 resolves *missing declared information*. A human who has not decided what they want cannot be clarified — they must decide. This is a gap in the framework's coverage between FC-3 and whatever decision-support mechanism exists. | Task 1.3 Subtask 3 |
| **FC-3** | "One question per item, not a consolidated list" must be clarified to mean: "one question per gap; all questions delivered in one batch." Current wording is ambiguous. | Task 1.3 Subtask 2 |
| **FC-4** | Review record (`RR-xx`) must be defined as a distinct FC-4 Tier 1 artefact, separate from the clarification exchange record series (`CE-xx`). The document taxonomy must contain both series with distinct schemas. | Task 1.5 Subtask 2 |
| **FC-4** | `approvalstatement` (verbatim, minimum 5 words) must be a required field in the Tier 1 audit log entry. Currently the specification does not require this. | Task 1.5 Subtask 5 |
| **FC-4** | `approvedat` = human action timestamp, not executor processing timestamp. Asynchronous workflows make this distinction non-trivial. Must be stated explicitly. | Task 1.5 Subtask 5 |
| **FC-5** | Two new `sourcetype` values needed: `correction` (for Task 1.5 correction-sourced values) and an implicit `supersedes` link field (for correction chains). FC-5's current sourcetype list does not include these. | Task 1.5 Subtask 4 |
| **FC-5** | Post-approval immutability must explicitly extend to the companion traceability record, not just the primary document. Modifying the traceability record post-approval is functionally equivalent to modifying the manifest. | Task 1.5 Subtask 5 |
| **FC-8** | The document taxonomy must distinguish CE, RR, and CR artefact series. Currently FC-8 focuses on the register but does not define the full set of clarification/review/correction artefacts that Steps 1–6 produce. | Task 1.3, Task 1.5 |


***

## Part 10 — Meridian Example Register (Final State After Task 1.3)

Thirteen entries. All BLOCKERs resolved. Five non-blocking entries carried to Task 1.4 `openquestions`.


| ID | Field | Gap type | Class | Resolution status | Notes |
| :-- | :-- | :-- | :-- | :-- | :-- |
| OQ-1-01 | `techstack` | AMBIGUOUS-INCOMPLETE | BLOCKER | RESOLVED | AstroJS 5.3.0 — derivation from "latest stable" acceptance |
| OQ-1-02 | `techstack` | AMBIGUOUS-INCOMPLETE | BLOCKER | RESOLVED | Shadcn/ui 2.4.0 — derivation from "latest stable" acceptance |
| OQ-1-03 | `techstack` | AMBIGUOUS-INCOMPLETE | BLOCKER | RESOLVED | React confirmed explicit |
| OQ-1-04 | `techstack` | AMBIGUOUS-INCOMPLETE | BLOCKER | RESOLVED | pnpm confirmed explicit |
| OQ-1-05 | `deploymenttarget` | AMBIGUOUS-INCOMPLETE | BLOCKER | RESOLVED | Cloudflare Pages confirmed; linked to OQ-1-10 |
| OQ-1-06 | `devenvironment` | AMBIGUOUS-INCOMPLETE | BLOCKER | RESOLVED | Node.js 22.11.0 confirmed |
| OQ-1-07 | `appetite` | AMBIGUOUS-FORMAT | BLOCKER | RESOLVED | "Small — a few days" → enum `small` (later corrected to `medium` in Task 1.5) |
| OQ-1-08 | `integrationrequirements` | AMBIGUOUS-INCOMPLETE | WARNING | OPEN | Formspree tentative — carried to `openquestions` |
| OQ-1-09 | `existingassets` | ABSENT | INFO | OPEN | No assets in brief — carried to `openquestions` |
| OQ-1-10 | `deploymenttarget` | CONTRADICTION | BLOCKER | RESOLVED | Workers/static contradiction resolved via Q5 cascade from OQ-1-05 |
| OQ-1-11 | `null` | SCHEMA-GAP | WARNING | OPEN | Cloudflare account readiness — `schema_gap_flag: true` |
| OQ-1-12 | `null` | SCHEMA-GAP | INFO | OPEN | Maintainability/handoff requirement — `schema_gap_flag: true` |
| OQ-1-13 | `null` | SCHEMA-GAP | INFO | OPEN | Design intent descriptors — `schema_gap_flag: true` |
| OQ-1-14 | `techstack` | AMBIGUOUS-INCOMPLETE | BLOCKER | RESOLVED | `@astrojs/react` implicit dependency — created and resolved in Task 1.4 Subtask 1 |
| OQ-1-15 | `techstack` | AMBIGUOUS-INCOMPLETE | BLOCKER | RESOLVED | pnpm version — created and resolved in Task 1.4 Subtask 2 |


***

## Part 11 — Session Output Summary

| Output | Count | Notes |
| :-- | :-- | :-- |
| Decisions confirmed | 9 (D-01 to D-06, DQ-01, DQ-04–06) | All fixed before analysis |
| Artefact schemas defined | 6 | Register, exchange, review record, correction record, traceability, audit log entry |
| New artefact types | 2 | RR series, CR series |
| Policy improvements — confirmed from prior sessions | 16 | P-01, P-03, P-04, P-07–P-15, P-18–P-23, CC-05, CC-09–10, S-03, S-05 |
| Policy improvements — new this session | 13 | P-Linking-01, P-Subtask2-01, P-Subtask4-01, P-Subtask1-01 through P-Subtask5-1.5-01 |
| Done When conditions | 4 sets (Tasks 1.2–1.5) | Fully specified |
| Failure modes catalogued | 23 | Across all four tasks |
| Open questions carried forward | 3 | DQ-02, DQ-03, UQ-03 |
| Cross-cutting policy implications | 10 | Across FC-2, FC-3, FC-4, FC-5, FC-8 |
| Meridian register entries | 15 | 13 from Tasks 1.2–1.3; 2 discovered during Task 1.4 |

<span style="display:none">[^17_1]</span>

<div align="center">⁂</div>

[^17_1]: i-am-making-progress-in-creati-fuGLU8hCRLyka3xtBTVglA.md


---

## Session Retrospective — Step 1, Tasks 1.2–1.5

**Session date:** 7 March 2026
**Scope:** Task 1.2 Gap Classification → Task 1.3 Clarification Resolution → Task 1.4 Manifest Drafting → Task 1.5 Human Review

***

## What Was Produced

The honest accounting before evaluation:

- Four task analyses — each with a restated question, artefact definitions, subtask-by-subtask breakdown, skills required, failure modes, and Done When conditions
- 6 artefact schemas defined or extended (register, exchange record, review record, correction record, traceability record, audit log entry)
- 2 new artefact types formalised (RR and CR series) not previously defined in the framework
- 29 policy improvements — 16 confirmed from prior sessions, 13 net-new this session
- 23 failure modes catalogued across all four tasks
- 15 register entries for the Meridian example, with full resolution lifecycle through Task 1.5
- 10 cross-cutting FC policy implications identified
- A comprehensive findings document covering all of the above

***

## What Went Well

**Decisions-before-analysis held the whole session.** Confirming D-01 through D-06 at the start — before touching Task 1.2 — meant every subtask analysis was written against a stable vocabulary and stable artefact shapes. The previous session's pattern of settling decisions mid-analysis (which produced retroactive adjustments) did not occur once.[^18_1]

**The case study was load-bearing, not decorative.** The `@astrojs/react` implicit dependency and the `pnpm` version gap were not invented examples — they emerged naturally from populating actual `techstack` entries in Task 1.4 Subtask 2. Both produced real policy improvements (P-Subtask2-01) and a real register entry (OQ-1-14). Grounding every analysis in the Meridian brief produced findings that abstract analysis would have missed.

**The DQ process worked cleanly.** Four design questions surfaced across the session. Each was explicitly named, held, and resolved at a natural boundary rather than mid-subtask. The session never stalled on an undecided question, and no decision was reversed after being made.

**The FC policy implications section earned its place.** Cross-cutting implications identified this session (FC-4 `approvalstatement`, FC-5 `correction` sourcetype, FC-3 `DECISION-REQUIRED` gap) are materially more specific than the F-series flags from the prior session. They name the exact field or rule that needs changing, which means they can be actioned directly rather than studied further.[^18_1]

**Failure modes are now a catalogue, not incidental observations.** 23 failure modes across four tasks, each with a downstream consequence. That structure transforms them from analytical commentary into something that can be used to write verification criteria for the eventual executor and reviewer agents.

***

## What Could Improve

**The self-check checklist (Task 1.4 Subtask 5) was designed in one pass without stress-testing.** Fifteen items is a confident number. But items 13 and 14 (FC-1 cross-reference and placeholder detection) are significantly more cognitively expensive than items 1–12. An agent running this checklist sequentially may be less thorough on the expensive items. The checklist design — specifically the ordering and whether the expensive items should be gated differently — was not interrogated. That is a design gap.

**Task 1.5 got thinner as the session progressed.** Task 1.2 has four fully developed subtasks with deep failure mode analysis. Task 1.5 has five subtasks but the correction application path (Subtask 4) and approval recording (Subtask 5) were covered faster. This is partly appropriate — those subtasks are more mechanical — but the scope addition path (P-21) and `UNSTABLE-FIELD` flag (P-22) were confirmed without being worked through concretely against a Meridian example. They may surface gaps when implemented.

**The session had no stated Definition of Done.**  We applied L6 rigorously within each task analysis but not to the session itself. The session ended at "compile findings" rather than at a pre-stated exit condition. This made the pacing reasonable but also meant there was no explicit moment where we checked whether all four tasks were analysed to the same depth. Task 1.2 and Task 1.4 are more deeply worked than Tasks 1.3 and 1.5 and it is not clear whether that asymmetry was a deliberate choice or a consequence of momentum.[^18_1]

**UQ-03 (`DECISION-REQUIRED` handling) is a structural gap with no resolution path.** FC-3 does not cover undecided information. We flagged it and moved on. But this gap will block the Task 1.3 executor agent in any project where Alex genuinely hasn't decided something. It is not a deferred design question — it is a missing framework mechanism. It is more urgent than its current UQ classification implies.

**The policy improvements list is now large across two sessions.** 29 improvements this session alone, on top of prior session findings. There is no prioritisation, no grouping by urgency, and no mechanism for distinguishing "must be resolved before agent design" from "can be adjusted during agent design." The same Tier 1/2/3 classification that was applied to the F-series flags should be applied to the policy improvements.[^18_1]

***

## Key Decisions on Record This Session

| Decision | Rationale |
| :-- | :-- |
| Decisions-before-analysis as session structure | Prevents retroactive adjustments; consistent with L6 |
| `linked_questions` populated in a single linking pass (DQ-01) | Prevents orphaned linkages from subtask sequencing |
| `derivation_flag` retained as machine-queryable field (DQ-04) | Redundancy with `resolutionnote` is intentional — different consumers |
| Derivation worklog folded into traceability record (DQ-05) | Keeps provenance in one file; no third artefact |
| Package manager in both `techstack` and `devenvironment` (DQ-06) | Different downstream consumers; single source reference |
| RR and CR as distinct artefact series from CE | FC-3 and FC-4 are different events; conflating them loses the distinction |
| Post-approval immutability extends to traceability companion | Sealing the manifest without sealing its companion is not a seal |


***

## Learnings to Carry Forward

- **The task restatement step is worth keeping.** Restating the policy's question in operational terms before defining artefacts consistently produced a sharper analysis. It is the L5 equivalent for task-level analysis — understand the problem before designing the solution.[^18_1]
- **Failure modes are more useful than skills required as a verification design input.** The skills required section answers *"what must the executor know?"* The failure modes section answers *"what must the verifier check for?"* The latter is directly usable in reviewer agent design. Future sessions should consider writing failure modes first and deriving skills from them.
- **Pre-drafting resolution as a subtask pattern is reusable.** Task 1.4 Subtask 1 exists because some clarification responses (derivation flags) cannot be directly used as field values. The same pattern — resolve deferred values before populating fields — will recur in Step 2 (environment contract) when version numbers from the manifest need to be resolved against dependency compatibility matrices. The pattern should be named and reusable, not re-invented per task.
- **The case study should be run all the way through before declaring any policy stable.** Two gaps (OQ-1-14, OQ-1-15) were only discovered by populating actual manifest fields. Policies that have not been walked against a real case are policies with undiscovered gaps.

***

## Recommendations — What to Do Next

There are four realistic paths. They are not equal.

***

### Option A — Apply policy improvement triage, then start agent design for Step 1

**What this involves:**

- Take the full policy improvements list (both sessions) and apply Tier 1/2/3 classification — the same approach used for the F-series flags[^18_1]
- Tier 1: must be resolved before writing the Step 1 executor and reviewer agent definitions
- Tier 2: resolve during agent design when first encountered
- Tier 3: defer
- Then begin the `ProjectRegistrar` executor agent class definition — the Step 1 executor — using the step policies and FC policies as the stable contracts

**Why this is attractive:**
The FC policies are already written.  The step policies for all six steps are written. The detailed task analysis (Tasks 1.1–1.5) is now complete for Step 1. There is more design surface for Step 1 than for any other step. The agent design work is ready to begin.[^18_1]

**The risk:**
The same risk that existed before the FC policies were written exists again at a smaller scale: 29 policy improvements from this session alone, some of which affect FC schemas, are not yet incorporated. Starting agent design before the FC schemas stabilise means some agent definitions may need revision when the schemas are updated.

***

### Option B — Incorporate this session's policy improvements into the FC documents first

**What this involves:**

- Work through the 10 FC implications from Part 9 of the findings
- Update FC-2 (Gate 3), FC-3 (`DECISION-REQUIRED` gap, batch clarification wording), FC-4 (`approvalstatement`, `approvedat` timing, RR schema), FC-5 (new sourcetypes, post-approval immutability), FC-8 (RR/CR artefact types)
- Confirm the updated FC schemas are consistent with Tasks 1.2–1.5 analysis
- Then proceed to agent design

**Why this is attractive:**
The FC policies are explicitly marked as v0.1, pending review.  Agent class definitions reference FC policies directly. Writing agent definitions against v0.1 FC policies that are known to need updating creates the same rework risk the prior session's modified Option A was designed to prevent.[^18_1]

**The risk:**
This is a writing task, not a design task. The decisions are already made — the FC implications just need to be incorporated. It should take one focused session, not an analytical one. The risk of delay is low if scoped tightly.

***

### Option C — Resolve UQ-03 (`DECISION-REQUIRED`) as a standalone framework mechanism design

**What this involves:**

- UQ-03 is a genuine structural gap: FC-3 covers *missing declared information* but not *undecided information*. When Alex hasn't decided something, the process currently has no defined path.[^18_1]
- Design the mechanism: what triggers it, what the human sees, how it differs from a clarification exchange, how the register is updated, and how the process resumes
- This is a focused design question, not a session-length topic. It could be resolved in an hour

**Why this is attractive:**
UQ-03 will block the Task 1.3 executor agent the first time it encounters a genuinely undecided human. That is not a rare case — a significant proportion of real briefs contain undecided technical choices. Leaving it unresolved means the first live run of Task 1.3 will surface this gap mid-execution.

**The risk:**
None — this is a small, well-scoped design question. The risk is not doing it.

***

### Option D — Step 2 task analysis before agent design

**What this involves:**

- Apply the same Tasks 1.1–1.5 analysis approach to Step 2 (Environment Contract)
- Step 2 consumes the approved manifest and produces `environment-contract.yaml` — a richer, more technical artefact
- The Step 2 executor (`EnvironmentContractAuthor`) will need the same task-level clarity that Step 1 now has

**Why this is attractive:**
The prior session's retrospective noted that *"some DoD sections became very prescriptive before implementation evidence exists."*  Step 2 has similarly elaborate policy. Walking it against a real case (what does the Meridian environment contract actually look like?) would surface the same class of gaps that Tasks 1.2–1.5 surfaced for Step 1. It would also validate that the register carry-forward from Step 1 works correctly — the five OPEN entries (OQ-1-08 through OQ-1-13) all get reclassified in Step 2.[^18_1]

**The risk:**
This delays agent design further. The same risk that existed before is still present — but with better grounds for sequencing it.

***

### Recommendation

**Do B, then C, then A — in that order, in the same session if possible.**

The reasoning:

**B first** because it is a writing task with no design uncertainty. The decisions are made. The FC documents just need to reflect them. Doing this before agent design means the agent definitions are written against stable, v0.2 FC policies rather than known-incomplete v0.1 ones. It protects the agent design work from the most likely source of rework.

**C next** because it is small, scoped, and high-consequence. UQ-03 is the only item in the open questions list that will cause an active process failure rather than a quality degradation. It takes an hour to resolve. Leaving it open is the one decision in this list that carries genuine execution risk.

**A after** — once B and C are done, the policy surface is stable and UQ-03 is resolved. Agent design for Step 1 (`ProjectRegistrar` executor) begins with:

- Stable FC policies (post-B)
- No structural gaps in the clarification path (post-C)
- A policy improvements list with Tier classification applied
- The most thoroughly analysed step policy in the system
- A failure mode catalogue that is directly usable as reviewer verification criteria

**Option D is the right fourth step** — after Step 1 agent design produces the first real executor, applying the same task analysis to Step 2 is the natural continuation. It also validates the register carry-forward, which is the most consequential cross-step mechanism in the bootstrap phase and has not yet been tested against a live case.

<div align="center">⁂</div>

[^18_1]: i-am-making-progress-in-creati-fuGLU8hCRLyka3xtBTVglA.md


---

## UQ-03 Resolution Recommendation

**The problem stated precisely:**

FC-3 governs clarification — it resolves missing declared information. Its explicit scope statement: *"the clarification protocol resolves missing declared information, not undecided information."*  When a Task 1.3 clarification response returns `DECISION-REQUIRED`, the executor has no defined path. The process blocks with no mechanism to unblock it.[^19_1]

This is a structural gap, not an edge case. Any project where Alex hasn't yet decided a technically consequential choice — form handler provider, deployment tier, authentication approach — will hit this gap on the first BLOCKER clarification.

***

## The Core Distinction

Before designing the mechanism, the distinction must be precise:


|  | FC-3 Clarification | UQ-03 (DECISION-REQUIRED) |
| :-- | :-- | :-- |
| **Cause** | Alex has the information but didn't include it | Alex doesn't yet have an answer — the choice is unmade |
| **Example** | "What Node version are you running?" | "Have you decided between Formspree and a custom handler?" |
| **Executor's role** | Retrieve existing knowledge | Support a decision the human must make |
| **Block reason** | Missing data | Unmade decision |
| **Unblock condition** | Alex provides the value | Alex makes and states the decision |

These are different events. Extending FC-3 to cover the second case would directly contradict FC-3's own scope statement and conflate two distinct executor behaviours. The correct solution is a new, separate mechanism.[^19_1]

***

## Decision Options

### Option A — Downgrade to WARNING and proceed

When Alex says *"I haven't decided yet,"* reclassify the gap from BLOCKER to WARNING, document in `openquestions`, and continue drafting.

**Problem:** If a gap was classified BLOCKER, it is because a downstream step will produce an invalid output without the value.  Downgrading doesn't remove the downstream dependency — it defers it. The manifest reaches Task 1.5 review as APPROVED with a known unresolved BLOCKER relabelled as WARNING. That is false resolution, not a design decision.[^19_1]

**Not recommended.**

***

### Option B — Treat as CONFIRMED-UNKNOWN

When Alex says *"I haven't decided yet,"* treat it identically to `CONFIRMED-UNKNOWN`. Reclassify from BLOCKER to WARNING and proceed with an empty field.

**Problem:** `CONFIRMED-UNKNOWN` means Alex genuinely cannot provide information — they don't know their Node version, they haven't set up the domain yet. `DECISION-REQUIRED` means Alex has agency over the answer and needs to exercise it.  These have different downstream implications:[^19_1]

- `CONFIRMED-UNKNOWN` → human needs to *find out* (investigation)
- `DECISION-REQUIRED` → human needs to *choose* (judgment)

Conflating them loses a signal that is operationally meaningful. A Step 2 executor receiving a `CONFIRMED-UNKNOWN` entry will handle it very differently from a `DECISION-REQUIRED` entry. Both deserves distinction.

**Not recommended.**

***

### Option C — Hard block with no further action

When Alex returns `DECISION-REQUIRED`, the process suspends. No presentation, no support, no artefact — just a status note in the register that the process is blocked awaiting a decision.

**Problem:** Alex is left without the context to make the decision efficiently. They may not remember which field is blocked, why it matters, or what the options are. The block has no exit path defined — Alex must somehow know to return with a decision, in the right form, to the right process. This is L1 violation territory: the process has surfaced an issue but not given the human what they need to resolve it.[^19_1]

**Not recommended as a standalone mechanism.**

***

### Option D — New Human Decision Support Protocol (FC-9)

A separate, named protocol governing how the executor responds to `DECISION-REQUIRED` gaps. Distinct from FC-3 in purpose, artefact type, and executor behaviour. When triggered:

1. The executor creates a Decision Request record (DR series)
2. The record presents structured decision support — options and their implications — without making the choice
3. The step enters formal `AWAITING-DECISION` state
4. The step blocks — no timeout, no downgrade
5. When Alex responds with a decision, the DR record is closed and the register entry is updated to `RESOLVED`

**Recommended.**

***

## Recommendation — Option D: FC-9 Human Decision Support Protocol

### Why FC-9 and not FC-3 extended

FC-3's explicit scope exclusion is not incidental phrasing — it is the policy's integrity boundary.  Extending FC-3 to include decisions would require removing that boundary, after which FC-3 would need to specify when to clarify versus when to support — which recreates the same design problem inside FC-3. A new protocol is cleaner and consistent with how FC-4 (approval) was kept separate from FC-3 (clarification) despite both being human interactions.[^19_1]

***

## FC-9 — Human Decision Support Protocol

**Version:** 0.1 Draft
**Scope:** Bootstrap phase. Applies wherever a BLOCKER register entry returns `resolutionstatus: DECISION-REQUIRED` from a clarification response.

***

### Context

When a BLOCKER gap is presented via FC-3 and Alex responds that the information does not yet exist because a decision is unmade, FC-3's resolution loop cannot close. FC-3 resolves *missing declared information.* An unmade decision is not missing information — it is an unexercised judgment. The executor's role shifts: from retrieval to support.

***

### What FC-9 does

FC-9 governs the executor's behaviour when a BLOCKER register entry has `resolutionstatus: DECISION-REQUIRED`. It defines:

- What the executor presents to Alex to support the decision
- The artefact produced (Decision Request record)
- The process state entered
- The unblock condition and return path
- What the executor must not do

***

### What the executor presents

When `DECISION-REQUIRED` is confirmed, the executor produces a structured decision support package containing four elements — no more, no fewer:

**1. Field and impact statement** — names the manifest field and why it is blocked:

> *"`integrationrequirements.provider` — the form handler provider must be confirmed before the Step 2 integration contract can be written. Without it, the Step 2 executor cannot specify the submission endpoint, the CORS configuration, or the environment variable schema."*

**2. Options** — the available choices, drawn only from the executor's knowledge base or information already in the brief. No invented options. Each option includes a one-sentence description and a one-sentence implication:

> *"Option A: Formspree — hosted form handler; requires a Formspree account and a POST endpoint in the form's action attribute. Implication: no server-side logic required; the integration is a single configuration value.*
> Option B: Custom server-side handler — requires a server-rendered route or a serverless function. Implication: contradicts the `fullyStatic` constraint declared in the manifest; would require constraint revision.*
> Option C: Defer this decision — proceed with the form handler entry marked CONFIRMED-UNKNOWN. Implication: the Step 2 integration section cannot be drafted; the decision must be made before Step 2 begins."*

**3. Decision instruction** — names exactly what response constitutes a usable decision:

> *"To unblock this: state which option you are selecting, or provide a different option not listed above. If you choose to defer (Option C), confirm explicitly — the field will be left empty and flagged as CONFIRMED-UNKNOWN."*

**4. No recommendation** — the executor does not recommend an option. This is the boundary between decision support and scope-setting. Providing a recommendation is a scope-setting act — it introduces executor preference into a human-owner judgment call.[^19_1]

***

### The Decision Request record

A new artefact type — DR series. Distinct from CE (clarification exchange) and RR (review record).

Filed at: `.framework/decisions/DR-{step}-{seq}.yaml`

```yaml
decisionrequestid: DR-1-01
step: 1
register_ref: OQ-1-08
field: integrationrequirements.provider
decisionrequired: >
  Which form handler provider will be used?
options:
  - optionid: A
    description: "Formspree — hosted form handler"
    implication: "No server-side logic required; single configuration value"
  - optionid: B
    description: "Custom server-side handler"
    implication: "Contradicts fullyStatic constraint; requires constraint revision"
  - optionid: C
    description: "Defer — proceed with CONFIRMED-UNKNOWN"
    implication: "Step 2 integration section cannot be drafted; decision required before Step 2"
requestedat: "ISO 8601"
respondedAt: null
selecteddecision: null          # Alex's chosen option ID or free-text description
decisionstatement: null         # verbatim from Alex's response
resolvedvalue: null             # the field value this decision produces
resolvedoption: null            # A | B | C | OTHER
resolutionstatus: AWAITING-DECISION
```


***

### Process state

When a DR record is created:

- The register entry for the affected BLOCKER gap is updated: `resolutionstatus: AWAITING-DECISION`
- The step enters `AWAITING-DECISION` state for this entry
- No other BLOCKER gaps are blocked by this state — other entries continue through FC-3 in parallel
- The step's final blocking condition (no remaining OPEN BLOCKER entries) cannot be satisfied while any entry is in `AWAITING-DECISION`

The process **does not** downgrade the entry, proceed past it, or set a timeout.  L2 applies: the step was blocked by an unmade decision that belongs to Alex. The human must cross this threshold consciously.[^19_1]

***

### Unblock condition

Alex responds with a decision. The response is classified identically to a FC-3 response — one of three outcomes:


| Response | Classification | Action |
| :-- | :-- | :-- |
| Alex names an option or provides a specific value | `DECISION-MADE` | DR record closed; register entry updated to `RESOLVED` with `resolvedvalue` populated; FC-3 resumes for this entry |
| Alex explicitly defers (selects Option C or equivalent) | `DEFERRED` | DR record closed; register entry updated to `CONFIRMED-UNKNOWN`; gap downgraded from BLOCKER per FC-2 downgrade rules; Step proceeds without the value |
| Alex's response is ambiguous | `UNCLEAR` | Follow-up question per P-Subtask3-01; DR record `respondedAt` not set until a classifiable response arrives |

Note on `DEFERRED`: explicit deferral by Alex is materially different from an unresolved DECISION-REQUIRED. When Alex says *"I'll decide later,"* that is a conscious choice to proceed with a gap — which satisfies L2.  The gap becomes `CONFIRMED-UNKNOWN` with Alex's explicit attribution. A process that never received a response is still blocked.[^19_1]

***

### What FC-9 does not govern

- **Design preferences** — FC-9 presents options to support a decision; it does not gather preferences about things Alex has already decided
- **Scope additions** — if Alex's decision reveals new scope not in the brief (e.g. *"I want SSR now"*), that is a scope change, not a decision. It requires a correction path, not an FC-9 resolution
- **Multi-step deferral** — if Alex defers a decision at Step 1, FC-9 does not guarantee the decision will be re-requested at Step 2. The carry-forward protocol (FC-8) governs re-classification at each step; if the gap is still BLOCKER in Step 2's context, FC-9 is invoked again at Step 2

***

### The executor boundary — what it must not do

- Must not recommend an option. Presenting options is support; recommending is scope-setting.
- Must not invent options not grounded in the knowledge base or the brief.
- Must not proceed past a `AWAITING-DECISION` entry by treating silence as implicit deferral.
- Must not create a DR record for a gap that FC-3 could resolve — if Alex simply hasn't provided a value they clearly know, FC-3 is the correct mechanism. FC-9 is only triggered when Alex has explicitly stated the decision is unmade.

***

### Trigger condition — FC-9 vs FC-3

The boundary must be explicit. One test, one question:

> *"Does Alex have this information available right now, and would stating it resolve the gap?"*

- **YES → FC-3.** The gap is missing declared information. Ask.
- **NO → FC-9.** The gap is an unmade decision. Support.

The trigger is Alex's own response, not the executor's prior classification. FC-3 runs first. If the FC-3 response indicates `DECISION-REQUIRED`, FC-9 is then invoked. FC-9 is never invoked before FC-3 is attempted.

***

### Policy improvements produced

| ID | Description | Affects |
| :-- | :-- | :-- |
| **FC-9 (new)** | Human Decision Support Protocol — governing the DECISION-REQUIRED path | FC-3, FC-8, Task 1.3 policy |
| **FC-3 update** | Add a cross-reference to FC-9 at the DECISION-REQUIRED classification point. The current FC-3 statement *"does not cover undecided information"* should become: *"when undecided information is identified, FC-9 Human Decision Support Protocol is invoked."* [^19_1] | FC-3 |
| **FC-2 update** | Add `AWAITING-DECISION` as a valid intermediate `resolutionstatus` for BLOCKER entries — distinct from `OPEN`, `RESOLVED`, `CONFIRMED-UNKNOWN`, and `ACCEPTED-AS-KNOWN-GAP`. | FC-2, register schema |
| **FC-8 update** | Carry-forward rules must handle `AWAITING-DECISION` explicitly: an entry in this state at Step 1 handoff is carried to Step 2 with status preserved; Step 2 must assess whether it is still BLOCKER in its own context before deciding whether to invoke FC-9 again or reclassify. | FC-8 |
| **Register schema update** | Add `decisionrequestref: DR-x-xx` as an optional field — populated when `resolutionstatus: AWAITING-DECISION`. Links the register entry to its DR record without embedding DR content in the register. | Register schema |


***

## Done When — UQ-03 is resolved

UQ-03 is closed when all five conditions are simultaneously true:

1. FC-9 exists as a named, versioned policy document with a stated scope, trigger condition, and executor boundary
2. FC-3 contains an explicit cross-reference to FC-9 at the `DECISION-REQUIRED` classification point
3. FC-2 includes `AWAITING-DECISION` as a valid intermediate `resolutionstatus` with a defined transition rule
4. The register schema includes `decisionrequestref` as an optional field
5. The DR artefact schema is defined with all required fields

<div align="center">⁂</div>

[^19_1]: i-am-making-progress-in-creati-fuGLU8hCRLyka3xtBTVglA.md


---

# list the skills required for each of the subtasks in Task 1.1

Task 1.1 has not yet been given the same subtask-level skills analysis as Tasks 1.2–1.5. The policy defines five actions for Task 1.1, but they map onto six distinct subtasks when the output schema is used as the frame. What follows applies the same analytical approach used this session, grounded in the `brief-inventory.yaml` schema confirmed in Task 1.2.[^20_1]

***

## Task 1.1 — Brief Inventory: Skills by Subtask

**The question Task 1.1 answers:** *What is in the brief, and does it map to the required schema?*

**Output structure:** `brief-inventory.yaml` — four arrays: `statements[]`, `fields[]`, `non_mappable[]`, `contradictions[]`

**The subtask sequence is dependency-ordered.** Subtask 1 (full read) must complete before any other subtask begins. Subtask 2 (statement extraction) before Subtask 3 (required fields) — because field coverage is assessed against extracted statements, not against the raw brief directly. Subtasks 5 and 6 (non-mappable and contradictions) run after Subtask 4 (optional fields) — both require a complete field coverage picture before they can be assessed reliably.

***

### Subtask 1 — Full Brief Read

**Question:** What does this brief contain as a whole?

**No classification happens in this subtask.** The executor reads the entire brief before writing a single entry. This is not administrative — it is the operational application of L5.[^20_1]

#### Skills Required

- **Read-before-classify discipline.** The executor must not begin populating `statements[]` during the read. The risk of classifying mid-read is anchoring: an early statement that appears unambiguous may only reveal its ambiguity in light of a later statement. If Subtask 2 begins before the full brief is read, the executor may classify S-01 as CLEAR and miss that S-08 contradicts it.
- **Tension flagging without resolution.** During the read, the executor notes apparent tensions, contradictions, and non-mappable content for later subtasks — without resolving them. Resolution is Subtask 6's job. A read that produces internal resolutions (*"these two things seem inconsistent but probably mean X"*) silently eliminates the evidence that Subtask 6 needs to produce a `contradictions[]` entry.
- **Brief completeness assessment.** Before Subtask 2 begins, the executor forms a structural picture: does the brief appear to contain tech stack information at all? Does it mention deployment? This prevents a Subtask 3 failure mode where a field is classified ABSENT because the executor stopped reading too early and missed a late-brief statement.


#### Failure Modes

- **Premature classification.** The executor begins writing `statements[]` during the read. An ambiguity discovered at S-10 cannot retroactively change the clarity classification assigned to S-02 if the subtask boundary has already been crossed.
- **Tension resolved during read.** The executor reads S-04 (*"Cloudflare Workers"*) and S-11 (*"fully static"*), internally resolves the tension using domain knowledge, and does not flag it for Subtask 6. The `contradictions[]` array is empty where it should contain `C-01`.

***

### Subtask 2 — Statement Extraction and Clarity Classification

**Question:** What are the discrete statements in the brief, and is each one unambiguous?

**Output:** `statements[]` — each entry: `id`, `text`, `clarity` (CLEAR | AMBIGUOUS), `candidate_fields[]`

#### Skills Required

- **Statement atomisation.** A brief sentence may contain two statements. *"I need a static site deployed to Cloudflare using AstroJS"* contains three statements: (1) static output mode, (2) Cloudflare deployment, (3) AstroJS tech stack. Each requires its own `statements[]` entry. An executor who records this as a single S-01 with three candidate fields produces a register downstream that cannot independently trace each value to a specific statement — it can only trace to *"a sentence that mentioned all three."*
- **Clarity classification precision.** `AMBIGUOUS` does not mean *"I am uncertain."* It means *"this statement could be interpreted to produce different field values depending on interpretation, and both interpretations are plausible from the brief alone."* The executor must be able to name at least two competing interpretations before assigning AMBIGUOUS. A statement is CLEAR if a single reading produces the field value unambiguously.
- **Candidate field assignment from schema knowledge.** `candidate_fields[]` entries must be real manifest field names — not descriptions, not paraphrases. *"The tech stack"* is not a valid `candidate_fields` entry. *"techstack"* is. This requires the executor to have the manifest schema loaded before Subtask 2 begins. A statement assigned `candidate_fields: []` is a non-mappable statement — it should be left for Subtask 5, not recorded as an entry with an empty array.
- **Implicit statement recognition.** Some brief statements make implicit claims. *"Shadcn/ui requires React"* is a statement about tech stack (explicit: Shadcn/ui; implicit: React). The implicit claim must produce its own statement entry — not be absorbed into the explicit one — because its `clarity` classification may differ from the parent statement. The `@astrojs/react` case from Task 1.4 demonstrates the cost of missing this at Subtask 2: the implicit dependency was not surfaced until manifest drafting.[^20_1]
- **Verbatim extraction discipline.** `text` is the statement as it appears in the brief — not paraphrased, not normalised. The executor's editorial voice must not appear in the `statements[]` array. If the brief says *"I want it to feel clean and minimal"*, `text` is that sentence. It is not *"visual style preference: clean, minimal."*


#### Failure Modes

- **Compound statement recorded as one.** S-01 says *"AstroJS with Shadcn/ui and React for component interactivity."* Recorded as one entry with `candidate_fields: [techstack]`. Task 1.2 Subtask 1 later struggles to create separate register entries for AstroJS, Shadcn/ui, and React because they share a single source statement — the source reference for each field is identical rather than specific.
- **AMBIGUOUS assigned without naming two interpretations.** The executor marks *"Cloudflare Workers or Pages"* as AMBIGUOUS — correct. But assigns it a single `candidate_field: deploymenttarget`. Task 1.2 cannot determine from this entry whether the ambiguity is format-based (two names for the same thing) or content-based (two genuinely different products). The `gap_type` in the register (AMBIGUOUS-FORMAT vs AMBIGUOUS-INCOMPLETE) is not derivable from the `brief-inventory.yaml` entry alone.
- **Implicit statement missed.** React confirmed via *"Shadcn/ui requires React"* but no separate `statements[]` entry created for React. Task 1.2 Subtask 1 sees no explicit statement for React → classifies `techstack` as ABSENT for React → creates OQ-1-03 as ABSENT rather than AMBIGUOUS-INCOMPLETE. The question asked is *"Is React required?"* rather than *"The brief implies React — please confirm."* Two different questions producing two different register entries.[^20_1]

***

### Subtask 3 — Required Field Coverage Mapping

**Question:** Does the brief contain sufficient information to populate each required manifest field?

**Output:** `fields[]` entries for required fields — each: `field`, `required: true`, `coverage` (PRESENT | ABSENT | AMBIGUOUS-INCOMPLETE | AMBIGUOUS-FORMAT), `supporting_statements[]`

#### Skills Required

- **Coverage classification precision — PRESENT means sufficient to populate, not merely mentioned.** A brief that says *"we'll be using the latest AstroJS"* mentions AstroJS but does not provide sufficient information to populate `techstack` per its format rule (*"named technologies only — AstroJS 5.x is valid, modern frontend stack is not"*). The field is AMBIGUOUS-INCOMPLETE, not PRESENT. The executor must test coverage against format rules, not just against field names.[^20_1]
- **Format rule knowledge per field.** The manifest schema's format rules are not all identical. `appetite` has valid enum values; `techstack` has a named-technology rule; `deploymenttarget` requires a named provider. Each field's coverage classification must be tested against its own format rule, not a generic "does information exist" test. An executor without format rule knowledge produces PRESENT classifications that Task 1.4 later rejects at the self-check step.
- **Multi-statement assembly detection.** A required field may have PRESENT coverage only when two or more statements are combined. `description` often draws from three or four brief statements. The executor must recognise when PRESENT coverage is assembled rather than stated directly — because assembled fields have a different traceability shape: `supporting_statements: [S-01, S-06, S-07]` rather than `supporting_statements: [S-01]`. This distinction directly informs Task 1.4's description assembly rule.[^20_1]
- **`humanactors` completeness check.** This field has a structural requirement: at least one `humandirector` entry must exist. PRESENT coverage means both *"a human actor is mentioned"* and *"their role is identifiable as humandirector."* A brief that names Alex as the project contact but never makes the humandirector role unambiguous is AMBIGUOUS-INCOMPLETE for `humanactors` — not PRESENT.
- **`appetite` enum awareness.** The `appetite` field has three valid values: `small`, `medium`, `large`. A brief that says *"I want this done quickly"* is ABSENT — no mappable value. A brief that says *"a couple of weeks"* is AMBIGUOUS-FORMAT — a duration is present but not in enum form. The executor must know the enum before classifying this field.
- **Step 2 and Step 3 downstream awareness.** The executor does not apply Gate 1 in Task 1.1 — that is Task 1.2's job. But awareness of what downstream steps require per field shapes the precision of PRESENT vs AMBIGUOUS-INCOMPLETE classification. A field that Task 1.2 will almost certainly classify BLOCKER deserves a more precise coverage assessment than a field unlikely to have BLOCKER consequences. This is not a formal requirement — it is a quality-of-output competency.


#### Failure Modes

- **PRESENT assigned for mentioned-but-insufficient values.** `techstack` classified PRESENT because the brief mentions *"AstroJS, the latest version."* Task 1.2 passes over it. Task 1.4 pre-drafting step discovers `derivation_flag` is needed and creates OQ-1-01 retroactively. The register entry should have been created in Task 1.2 from a Task 1.1 AMBIGUOUS-INCOMPLETE classification.[^20_1]
- **`appetite` classified ABSENT when it is AMBIGUOUS-FORMAT.** *"A few days of focused work"* is not ABSENT — it is a duration that requires mapping to a valid enum value. If classified ABSENT, Task 1.2 creates a register entry asking *"what is the project appetite?"* — a question Alex already partially answered. The correct question (and question type) is different: *"Your timeline of a few days maps to 'small' — can you confirm?"*
- **Multi-statement PRESENT not recorded.** `description` is classified PRESENT with `supporting_statements: [S-01]`. But S-01 only provides the project type and name. S-06 provides the page sections. S-07 provides the visual style. Task 1.4's description assembly produces a value with a traceability entry citing only S-01 — and a verifier checking the assembled description against the stated source cannot find the sections or visual style referenced in S-01 alone. FC-1 fails.

***

### Subtask 4 — Optional Field Coverage Mapping

**Question:** Does the brief contain information relevant to each optional manifest field?

**Output:** `fields[]` entries for optional fields — each: `field`, `required: false`, `coverage`, `supporting_statements[]`

#### Skills Required

- **Restraint — ABSENT is a valid, complete classification.** Optional fields absent from the brief are recorded as ABSENT and left empty. The executor must not populate them with reasonable assumptions. *"No existing assets mentioned — probably doesn't have any"* is not a basis for a PRESENT classification. ABSENT is the complete, correct entry. The assumption temptation is stronger for optional fields than required ones, precisely because the stakes feel lower.[^20_1]
- **Distinguishing ABSENT from information that would belong in a different field.** A brief that says *"I'll need to hand this off to a developer later"* is not providing `existingassets` information. It may be providing `constraints` information, or non-mappable content. The executor must resist the urge to re-map statements from Subtask 2 to optional fields they don't quite fit. The candidate field assignment from Subtask 2 is the canonical mapping — optional field coverage mapping tests against it, not against a fresh reading.
- **`constraints` and `outofscope` specificity requirement.** These fields have explicit format rules: *"only constraints explicitly stated by humandirector — do not infer from the tech stack"* and *"only what humandirector explicitly excluded — absence of mention ≠ out of scope."*  An executor who marks `constraints` as PRESENT because the tech stack implies certain limitations produces a field value in Task 1.4 that violates the format rule. The coverage classification must test against the format rule: is there an explicit statement of a constraint, or is the constraint inferred?[^20_1]
- **`referenceexamples` recognition.** This optional field is easy to miss because reference examples in briefs are rarely labelled as such. *"I like how Linear.app looks"* is a `referenceexamples` statement. An executor without schema awareness of this field's existence will classify this as non-mappable in Subtask 5. The field must be in the executor's schema vocabulary before Subtask 4 begins.
- **Conditional requirement awareness.** Some optional fields become effectively required in certain contexts. `integrationrequirements` is optional by schema but becomes a WARNING-level gap (not INFO) when a contact form is declared in the brief — because the form handler is a downstream dependency. The executor does not classify severity in Task 1.1, but identifying that *"optional"* doesn't mean *"low stakes"* improves the coverage classification precision.


#### Failure Modes

- **Inferred constraint recorded as PRESENT.** The brief declares AstroJS. The executor infers *"no server-side rendering"* as a constraint of AstroJS's default static output mode and records `constraints` as PRESENT. Task 1.4 populates `constraints` with inferred content. FC-1 fails — the traceability entry cites no brief statement because Alex never stated the constraint.[^20_1]
- **`referenceexamples` not recognised.** *"I want it to feel like Linear.app"* is classified as non-mappable style preference in Subtask 5. Task 1.2 does not create a register entry for `referenceexamples` because the field shows ABSENT. Task 1.4 produces a manifest with an empty `referenceexamples` field. Alex reviews and says *"I mentioned Linear.app — why isn't that in there?"* The gap traces to a missed classification in Subtask 4.
- **`outofscope` populated from absence.** Alex never mentions a CMS. The executor records `outofscope: [CMS]` because it is a common exclusion. Task 1.4 writes *"CMS"* into the `outofscope` field. FC-1 fails — Alex never said CMS was out of scope; the executor invented an exclusion from an absence of mention, which the format rule explicitly prohibits.[^20_1]

***

### Subtask 5 — Non-Mappable Statement Identification

**Question:** Which brief statements don't map to any manifest field, and do they carry downstream consequences?

**Output:** `non_mappable[]` — each: `statement_id`, `downstream_note`

#### Skills Required

- **Schema exhaustion check.** After Subtasks 3 and 4, every statement in `statements[]` that has at least one entry in `supporting_statements[]` across the `fields[]` array is accounted for. Non-mappable statements are those that appear in no `supporting_statements[]` reference. The executor must run this check explicitly — not rely on memory of which statements felt relevant during Subtasks 3 and 4.
- **Downstream consequence assessment.** Not all non-mappable statements are inconsequential. A statement like *"I already have a Cloudflare account set up"* maps to no manifest field but carries a Step 2 infrastructure consequence. The `downstream_note` must identify this consequence specifically — not record *"no manifest field."* The note *"Infrastructure readiness — no manifest field exists; Step 2 deployment section may assume account procurement is required if this is not surfaced"* is a complete entry. *"Does not map to schema"* is not.
- **Distinguishing truly non-mappable from missed-field-mapping.** Before recording a statement as non-mappable, the executor must confirm it does not map to a field that was missed in Subtasks 3 or 4. A statement that maps to an existing optional field the executor didn't consider is not non-mappable — it is an ABSENT classification that should be corrected. Non-mappable is reserved for statements where no manifest field exists for the content type.
- **`schema_gap_flag` awareness.** Non-mappable statements that carry genuine downstream consequences are candidates for `schema_gap_flag: true` in the Task 1.2 register. The executor does not set this flag in Task 1.1 — that is Task 1.2 Subtask 4's work — but the `downstream_note` quality directly determines whether Task 1.2 can make that classification correctly. A vague note produces a vague register entry. A specific note produces a specific register entry.


#### Failure Modes

- **Schema exhaustion check not run.** The executor identifies non-mappable statements during the read (Subtask 1) and relies on that memory. Two statements that felt irrelevant during reading are not recorded. Task 1.2 Subtask 4 receives a `non_mappable[]` array that is incomplete — no entry for the Cloudflare account statement. OQ-1-11 is never created.[^20_1]
- **`downstream_note` is generic.** Every non-mappable entry reads *"No corresponding manifest field."* Task 1.2 Subtask 4 processes each entry and cannot determine which ones warrant register entries versus which are genuinely inconsequential. The executor either creates register entries for all of them (register noise) or none of them (missed gaps). Both outcomes stem from a `downstream_note` that provided no signal.
- **Non-mappable confused with optional-field-absent.** *"I have a Cloudflare account"* is recorded as non-mappable. In fact, `deploymenttarget` has a `supporting_statements` entry and the account statement was simply not considered during Subtask 3. The non-mappable entry creates a duplicate path: Task 1.2 Subtask 1 creates a register entry for `deploymenttarget` from the AMBIGUOUS-INCOMPLETE classification, and Task 1.2 Subtask 4 creates a second register entry from the non-mappable note — both about the same underlying information.

***

### Subtask 6 — Contradiction Detection

**Question:** Do any brief statements contradict each other, directly or by implication?

**Output:** `contradictions[]` — each: `id`, `statement_ids[]`, `description`, `affected_fields[]`

#### Skills Required

- **Domain knowledge of the declared tech stack.** Some contradictions are only visible to an executor who knows the technology. *"Cloudflare Workers"* and *"fully static output"* are not lexically contradictory — Cloudflare Workers is a server runtime, and static output means no server-side rendering. Without knowing that, the executor sees two statements about Cloudflare and does not flag a contradiction.  Domain knowledge is a prerequisite skill for this subtask — it cannot be replaced by policy compliance alone.[^20_1]
- **Implicit contradiction detection.** Contradictions are not always stated directly. *"No server-side rendering"* (explicit constraint) and *"contact form with server validation"* (implied requirement) contradict each other without using contradictory words. The executor must read for what each statement *implies* about the architecture, not just what it explicitly states.
- **Cross-statement reading discipline.** Contradictions require at least two statements to be read simultaneously. Single-statement reading — the default mode during Subtask 2 — will not surface them. The executor must make a dedicated pass over the full `statements[]` array specifically looking for cross-statement tensions, after Subtask 2 has made all implicit content explicit.
- **Non-resolution discipline.** The executor must record the contradiction without resolving it. This is the hardest skill in this subtask. An executor with domain knowledge will often have a strong intuition about which side of a contradiction is correct. That intuition must not produce a silent resolution — it must produce a `contradictions[]` entry with a specific `description` that names both sides. Task 1.3 is where the resolution happens, with Alex's input.[^20_1]
- **Multi-field impact enumeration.** A single contradiction may affect more than one manifest field. The Workers/Pages contradiction affects `deploymenttarget` (which product?) and potentially `constraints` (is the static constraint still valid?). `affected_fields[]` must enumerate all fields the contradiction touches — not just the most obvious one. An incomplete `affected_fields[]` means Task 1.2 creates register entries for some affected fields but not others.


#### Failure Modes

- **Domain-knowledge-dependent contradiction silently resolved.** The executor sees *"Cloudflare Workers"* and *"fully static"*, knows Workers is a server runtime, concludes the human probably meant Cloudflare Pages, and records `deploymenttarget` as AMBIGUOUS-INCOMPLETE (not PRESENT) without a `contradictions[]` entry. Task 1.2 treats this as a single gap — asks *"Which Cloudflare product?"* — and Alex confirms Pages. The static constraint contradiction is never explicitly surfaced. The constraint stays in the manifest unchallenged.[^20_1]
- **Implicit contradiction missed.** No statement says *"no server-side rendering"* explicitly, but the tech stack (AstroJS, static output) implies it. The contact form handler requirement implies a POST endpoint. The executor, finding no explicit constraint statement, misses the implicit tension. Task 1.3 never asks about it. Task 1.4 records `constraints: [fullyStatic]` from the AstroJS inference and `integrationrequirements: [formHandler]` — and no one has confirmed these are compatible in Alex's understanding.
- **`affected_fields[]` incomplete.** The Workers/Pages contradiction is recorded with `affected_fields: [deploymenttarget]`. Task 1.2 creates OQ-1-05 for `deploymenttarget`. The static constraint (`constraints`) is not listed. OQ-1-10 is created in Task 1.2 Subtask 1 from the `constraints` field coverage analysis — but its link to OQ-1-05 is not established because the `contradictions[]` entry didn't connect them. The bidirectional linking pass in Task 1.2 must reconstruct a connection that Task 1.1 should have made explicit.

***

## Summary — Skills Compendium for Task 1.1

| Subtask | Critical skill | Most consequential failure |
| :-- | :-- | :-- |
| 1 — Full read | Read-before-classify discipline | Implicit contradiction silently resolved during read |
| 2 — Statement extraction | Statement atomisation; implicit statement recognition | Compound statements collapsed; implicit dependency missed |
| 3 — Required field coverage | Format-rule knowledge per field; multi-statement assembly detection | PRESENT assigned for format-non-compliant values |
| 4 — Optional field coverage | Restraint (ABSENT is complete); `constraints`/`outofscope` format rule knowledge | Inferred constraints recorded as PRESENT |
| 5 — Non-mappable identification | Schema exhaustion check; downstream consequence assessment | Non-mappable array incomplete; vague `downstream_note` |
| 6 — Contradiction detection | Domain knowledge; non-resolution discipline; multi-field impact enumeration | Domain-knowledge contradiction silently resolved |

**One skill appears across all six subtasks and is the most foundational prerequisite for Task 1.1:** full manifest schema knowledge — required field names, optional field names, format rules per field, and valid enum values. An executor without this loaded before Subtask 2 begins cannot reliably classify coverage, identify candidate fields, or detect format-based ambiguities. It is the single skill whose absence degrades every other subtask output.

<div align="center">⁂</div>

[^20_1]: i-am-making-progress-in-creati-fuGLU8hCRLyka3xtBTVglA.md


---

# do the same for tasks 1.2 - 1.5

This is a synthesis task drawing entirely from this session's analysis. No search needed.

***

## Task 1.2 — Gap Classification: Skills by Subtask

**The question Task 1.2 answers:** *Which gaps in the brief inventory are blocking, and which can be carried as open questions?*

**Output:** `open-questions-register.yaml` — four subtasks, each populating the register from a different input array in `brief-inventory.yaml`

***

### Subtask 1 — Required Field Gap Classification

**Question:** For each required field with non-PRESENT coverage, would proceeding without it cause a downstream step to fail?

**Output:** Register entries for all required fields with classification BLOCKER | WARNING | INFO

#### Skills Required

- **Step 2 and Step 3 policy documents loaded before starting.** Gate 1 — *"would getting this wrong cause Step 2 or Step 3 to fail?"* — cannot be answered from Step 1's policy alone. The executor must know what each required field is consumed for downstream. `appetite` is not consumed by Step 2 or Step 3 directly, but it is required by the manifest schema — Gate 3 catches it. Without Step 2/3 policy knowledge, Gate 1 produces false negatives.[^21_1]
- **Three-gate classification sequence, applied in order.** Gate 1: downstream failure test. Gate 2: output validity test (can the manifest DoD be met without this value?). Gate 3: required field format rule test (is the value present but in an invalid form?). An executor who applies only Gate 1 misses fields that fail Gate 3 only — like `appetite` with a valid duration statement that doesn't map to a valid enum. The sequence is non-negotiable: Gates 1 and 2 test for impact; Gate 3 tests for form.[^21_1]
- **Format rule knowledge per required field.** Gate 3 is only executable if the executor knows each field's format rule. `techstack` must contain named technologies with versions. `appetite` must be `small | medium | large`. `approvedby` must match a `humanactors` entry. An executor running Gate 3 without format rule knowledge approves values that Task 1.4's self-check later rejects.
- **`gap_type` precision — four distinct values, each with a different consequence.** `ABSENT` → the brief contains no information for this field. `AMBIGUOUS-INCOMPLETE` → information exists but is insufficient to populate the field. `AMBIGUOUS-FORMAT` → information exists and is complete but not in the required format. `CONTRADICTION` → two statements provide conflicting values. Each `gap_type` determines the question type in Task 1.3. An executor who conflates AMBIGUOUS-INCOMPLETE with AMBIGUOUS-FORMAT formulates the wrong question: the first requires a value-retrieval question; the second requires a choice-based question presenting valid options.[^21_1]
- **One-gap-one-entry discipline.** If `techstack` has three gaps (AstroJS version, Shadcn/ui version, React unconfirmed), three entries are created. Not one entry for `techstack`. Task 1.3 will produce one question per entry — a compound question for a compound entry violates FC-3. The downstream consequence is real: a single `techstack` entry with three gaps produces one question whose answer is a paragraph that cannot be cleanly parsed into three discrete `resolutionnote` values.[^21_1]
- **BLOCKER downgrade constraint for `CONFIRMED-UNKNOWN`.** An entry becomes BLOCKER when classified. It can be downgraded to WARNING only if Alex confirms the information genuinely does not exist (`CONFIRMED-UNKNOWN`). It cannot be downgraded by the executor's judgment that *"we can probably proceed anyway."* This constraint must be a loaded rule, not a policy the executor follows when convenient.


#### Failure Modes

- **Step 2/3 policy not loaded.** `appetite` classified as INFO because no downstream step consumes it directly. Gate 3 not applied. Task 1.4 writes a non-enum value into the manifest. Self-check fails at item 6.
- **Three `techstack` gaps collapsed into one entry.** Task 1.3 formulates one question. Alex responds with a paragraph. Response classification (Subtask 3) is unclear. A follow-up is needed — which recreates the three-entry structure that should have been the starting point.
- **`AMBIGUOUS-FORMAT` classified as `AMBIGUOUS-INCOMPLETE`.** `appetite: "a few days of focused work"` becomes a value-retrieval question: *"What is your project appetite?"* Alex answers *"small — a few days."* But the question implied Alex hadn't answered at all — which isn't true. The correct question was a confirmation: *"Your timeline of a few days maps to 'small' — can you confirm?"* The wrong `gap_type` produced the wrong question.

***

### Subtask 2 — Optional Field Gap Classification

**Question:** For each optional field with non-PRESENT coverage, what is the downstream impact?

**Output:** Register entries for optional fields with classification WARNING | INFO (never BLOCKER by definition)

#### Skills Required

- **Explicit absence confirmation discipline.** Every optional field must be assessed — not just those that seem relevant. The Done condition requires confirming every optional field was visited, not just that entries were created for the ones that triggered classification. Silent skipping of an ABSENT optional field with "no downstream impact" produces a register that appears complete but is not.[^21_1]
- **WARNING vs INFO threshold — impact-based, not intuition-based.** WARNING means a specific, named downstream step will produce a degraded output. INFO means the gap is noted for completeness with no identifiable downstream consequence. The threshold is not *"how important does this feel?"* — it is *"which downstream output degrades and by how much?"* An executor applying intuition rather than impact analysis produces inconsistent classifications across the register.
- **Conditional requirement recognition.** Some optional fields become effectively WARNING-level when other fields are populated in specific ways. `integrationrequirements` is optional by schema but becomes WARNING when `techstack` includes a form handler or when the brief mentions a contact form. This conditionality requires reading optional field classification against confirmed required field values — not in isolation.[^21_1]
- **`schema_gap_flag` awareness for fields that don't exist.** Some brief content has clear downstream value but no manifest field to map to. Infrastructure readiness, maintainability requirements, design intent beyond reference examples — these are not ABSENT optional fields, they are ABSENT *from the schema itself*. The executor must distinguish between *"this optional field has no value"* and *"this information has no field"* — the second produces a register entry with `schema_gap_flag: true`.[^21_1]


#### Failure Modes

- **Implicit conditional requirement missed.** `integrationrequirements` classified INFO because it is optional. A contact form is in the brief. The downstream consequence — Step 2's integration section cannot be drafted without a provider — is not assessed. OQ-1-08 is created with classification INFO rather than WARNING. Task 1.5 review presents it as an INFO item. Alex approves without understanding the Step 2 consequence.
- **Infrastructure readiness classified as ABSENT for `deploymenttarget`.** The statement *"I already have a Cloudflare account"* is not absence of deployment information — it is deployment-adjacent information with no manifest field. Classifying `deploymenttarget` as ABSENT misses this; classifying it correctly as AMBIGUOUS-INCOMPLETE doesn't capture the infrastructure readiness signal either. Only `schema_gap_flag: true` on a non-mappable-derived entry (OQ-1-11) preserves it.[^21_1]

***

### Subtask 3 — Contradiction Classification and Linking

**Question:** Which contradictions require clarification before drafting, and how do they relate to other register entries?

**Output:** Register entries for contradictions; bidirectional `linked_questions` population for all related entries

#### Skills Required

- **Contradiction classification is always BLOCKER — no exceptions.** This is a loaded invariant, not a judgment call. A contradiction in the brief means the manifest cannot contain both values and cannot safely choose one without human confirmation. Downgrading a contradiction to WARNING requires the executor to be confident enough in the correct resolution to proceed without asking — which is a domain knowledge substitution for a human decision. Per L2, one-way decisions belong to humans.[^21_1]
- **Linking pass as a distinct, named step.** After all register entries are created, a separate linking pass identifies all entry pairs that share an underlying cause. The linking is bidirectional: if OQ-1-05 is linked to OQ-1-10, OQ-1-10 must also be linked to OQ-1-05. This pass runs once, after Subtask 3 completes — not incrementally during subtask execution. Incremental linking produces orphaned linkages when earlier entries reference later entries that don't exist yet.[^21_1]
- **Linked group identification — finding the underlying cause.** Two register entries are linked when resolving one resolution note contains information that resolves the other. The Workers/Pages contradiction (OQ-1-05) and the static/SSR ambiguity (OQ-1-10) are linked because confirming Cloudflare Pages resolves both. An executor who does not identify the underlying cause cannot identify the linked group. Domain knowledge is required here: understanding that Pages = static and Workers = server is the basis for the link.
- **Impact field specificity.** Each entry's `impact` field must name a specific downstream failure — not a general concern. *"Step 2 cannot be drafted"* is insufficient. *"Step 2 deployment section cannot specify the build output configuration without knowing whether Workers or Pages is the target"* is specific. The `impact` field is the primary signal Task 1.3 uses to formulate an impact statement in the clarification question. Vague impact → vague question → vague response.


#### Failure Modes

- **Contradiction downgraded to WARNING using domain knowledge.** The executor knows that AstroJS defaults to static output and that *"Cloudflare Workers"* was probably a naming mistake — Alex meant Pages. The contradiction is recorded as WARNING. Task 1.3 never asks about it. Task 1.4 writes `deploymenttarget: Cloudflare Pages` with `sourcetype: derivationrule` — but the derivation is a domain-knowledge substitution, not a documented rule. FC-1 fails.[^21_1]
- **Linking pass skipped.** OQ-1-05 and OQ-1-10 are both created but `linked_questions: []` on both. Task 1.3 formulates two separate questions for the same underlying issue. Alex receives a question about the Cloudflare product and a separate question about the static constraint. One response resolves both; the executor only resolves OQ-1-05. OQ-1-10 remains OPEN. Task 1.4 begins with one OPEN BLOCKER — which the executor must either skip (invalid) or loop back through Task 1.3 to resolve.

***

### Subtask 4 — Non-Mappable Statement Classification

**Question:** Which non-mappable brief statements carry downstream consequences requiring a register entry?

**Output:** Register entries for consequential non-mappable statements (with `schema_gap_flag: true`); documented no-entry decisions for inconsequential ones

#### Skills Required

- **Downstream consequence assessment for non-schema content.** The executor must assess each `non_mappable[]` entry from `brief-inventory.yaml` against Steps 2–6 — not just Step 1. A statement that has no Step 1 consequence may have a Step 2 consequence. Infrastructure readiness affects Step 2's deployment section. Maintainability requirements may affect Step 3's roster. Design intent descriptors affect Step 4's pattern selection. The executor needs a working model of what each downstream step consumes.
- **Explicit no-entry documentation.** For every `non_mappable[]` entry that does not produce a register entry, the executor must record a no-entry decision. The Done condition for Subtask 4 requires explicit confirmation that every non-mappable entry was assessed — not just that entries were created for the ones that mattered. A register that appears complete may simply be one where non-consequential items were silently skipped.[^21_1]
- **`schema_gap_flag` implications for framework feedback.** Entries with `schema_gap_flag: true` are not just register entries — they are signals to the framework that the manifest schema has a gap. An executor who understands this creates entries whose `candidate_field` suggestions are actionable: *"maintainability: string — records developer handoff requirement"* is more useful than *"some field for handoff requirements."* This skill is not required for Task 1.2 to complete correctly, but it determines whether the schema gap signal is usable by the framework.


#### Failure Modes

- **Subtask 4 skipped entirely.** The most common failure. The `non_mappable[]` array is processed in Task 1.1 with `downstream_note` values, but Task 1.2 treats it as already handled. OQ-1-11 (Cloudflare account readiness), OQ-1-12 (maintainability), and OQ-1-13 (design intent) are never created. All three appear in the session's Meridian register precisely because Subtask 4 ran. Their absence would produce a manifest whose `openquestions` section is missing three entries the human director should know about at Task 1.5 review.[^21_1]
- **No-entry decisions not documented.** Three entries from `non_mappable[]` are inconsequential (vague expressions of enthusiasm, scheduling notes). The executor creates no register entries for them — correctly. But without documented no-entry decisions, a verifier cannot distinguish *"assessed and found inconsequential"* from *"never assessed."* The Done condition for Subtask 4 cannot be confirmed.

***

## Task 1.3 — Clarification Resolution: Skills by Subtask

**The question Task 1.3 answers:** *Can each blocking gap be resolved by asking Alex directly?*

**Output:** `CE-1-01.yaml` with all BLOCKER entries resolved, reclassified, or formally noted as `CONFIRMED-UNKNOWN` or `DECISION-REQUIRED`

***

### Subtask 1 — Question Formulation and Exchange Record Creation

**Question:** What is the precisely correct question to ask for each BLOCKER register entry?

**Output:** Exchange record shell created; one question per BLOCKER entry

#### Skills Required

- **`gap_type` → question type mapping, applied mechanically.** Each `gap_type` has a corresponding question structure that must be applied without deviation:[^21_1]
    - `ABSENT` → value-retrieval question: *"What is X?"*
    - `AMBIGUOUS-INCOMPLETE` → value-retrieval question with context: *"You mentioned Y — what specifically is Z?"*
    - `AMBIGUOUS-FORMAT` → choice question presenting valid options: *"You mentioned [duration] — which of [small / medium / large] best fits?"*
    - `CONTRADICTION` → disambiguation question naming both interpretations: *"The brief mentions both A and B, which appear to conflict — which is correct?"*

An executor applying judgment rather than this mapping produces questions that mix types — asking for a choice when a value is needed, or asking for disambiguation when a format mapping would close the gap.
- **FC-3 compound question prohibition — 25-word maximum, one gap per question.** The character limit is a proxy for the structural rule: one question resolves one gap. A question that requires two pieces of information to answer is a compound question by definition, regardless of word count. The executor must test every formulated question: *"Can this be fully answered by addressing one register entry?"* If no, it is compound.[^21_1]
- **Parenthetical retrieval instructions — permitted, not compound.** *"Run `node --version` in your terminal and paste the result"* added to a question about Node.js version is a retrieval instruction, not a second question. It does not ask for two pieces of information — it helps Alex retrieve the one piece being asked for. The policy must permit these; an executor who strips them out produces questions that return `CONFIRMED-UNKNOWN` from a human who could have answered with a 10-second terminal check.[^21_1]
- **Linked group detection — ask once, not twice.** Before formulating a question for any entry, the executor checks `linked_questions[]` for that entry. If two entries are linked, one question covers both — and the question is formulated against both entries' `gap` fields. An executor who formulates separate questions for linked entries violates the efficiency principle of FC-3 and confuses Alex with duplicate questions about the same underlying issue.
- **Impact statement precision.** Every question includes a one-sentence impact statement — not to explain to Alex why the executor is asking, but to help Alex understand the stakes so they provide a usable answer. *"This affects whether Step 2 can specify the deployment configuration"* is specific. *"This is needed to complete the project record"* is not. The impact statement is drawn from the register entry's `impact` field — not rewritten by the executor.[^21_1]
- **Exchange record shell created before delivery, not after.** `initiatedat` is set at the moment of sending. The shell must exist before the questions are delivered. An executor who creates the record after Alex's response cannot set an accurate `initiatedat` — this is an audit integrity issue, not an administrative detail.[^21_1]


#### Failure Modes

- **Compound question for linked entries.** OQ-1-05 and OQ-1-10 produce one question: *"The brief mentions both Cloudflare Workers and a fully static site — which is the correct deployment target, and does the static constraint still apply?"* This is compound: two questions, two answers required. Alex responds to the first. The executor records one `RESOLVED` and must create a follow-up for the second — which should have been the cascade update rule, not a second question.
- **`AMBIGUOUS-FORMAT` treated as `AMBIGUOUS-INCOMPLETE`.** OQ-1-07 (`appetite`) produces: *"What is the project appetite — small, medium, or large?"* — correct. If misclassified as AMBIGUOUS-INCOMPLETE: *"What is the project timeline?"* — Alex answers *"a couple of weeks"* and the executor is back where it started: AMBIGUOUS-FORMAT, requiring another exchange.
- **Exchange record created post-response.** The executor delivers questions to Alex, receives responses, then creates the exchange record with `initiatedat` estimated. In a synchronous session this is minutes off. In an asynchronous workflow it may be hours. The audit trail misrepresents when the questions were asked.[^21_1]

***

### Subtask 2 — Batch Delivery and Blocking

**Question:** Has the complete batch been delivered to Alex as a single exchange, and is the process correctly blocked?

**Output:** `initiatedat` timestamp set; process suspended

#### Skills Required

- **Batch vs sequential discipline — all questions delivered once.** All BLOCKER questions are batched into a single exchange. One delivery, one block, one response. An executor who delivers questions sequentially — waiting for each response before formulating the next — multiplies the number of round trips unnecessarily and risks asking questions that later questions make irrelevant. If Q1 is *"Which Cloudflare product?"* and Q2 is *"Does the static constraint apply?"* — receiving Q1's answer before asking Q2 means the executor might be able to derive Q2's answer from Q1's response. The batch approach handles this through cascade updates in Subtask 3.[^21_1]
- **Hard blocking — no optimistic pre-loading.** Once the exchange is delivered and `initiatedat` is set, the process blocks completely. The executor must not begin drafting the manifest, pre-populate fields where the answer seems obvious, or pre-load correction workflows. Any work done during the block that consumes unconfirmed values will need to be undone if Alex's responses differ from expectation. The block is genuine suspension, not an opportunity for parallel work.[^21_1]
- **Clarity of the question package as presented to Alex.** Each question must be self-contained — Alex should not need to refer to other questions to answer any one question. If two questions are linked, the linking is noted in the presentation (*"Your answer to Q1 may also address Q2"*) but each question still stands independently. An executor who presents questions assuming Alex will read all of them before answering any of them has no guarantee that is how Alex will read them.


#### Failure Modes

- **Sequential delivery.** The executor asks Q1, receives an answer, formulates Q2, delivers Q2. Three questions become three exchange cycles. The Meridian brief has 7 BLOCKER entries. Sequential delivery means seven round trips before Task 1.4 can begin — avoidable entirely with a single batch.
- **Partial batch.** The executor batches questions for the four tech stack entries but delivers the `appetite` and `deploymenttarget` questions separately because they feel different in character. Two exchange records are created for a single Task 1.3 run. The exchange record series is CE-1-01 and CE-1-02. The register entries for the second batch show a different `resolvedatexchange` reference than the first. FC-8 carry-forward must now reconcile two exchange references for a single step's resolution work. Unnecessary complexity with no benefit.[^21_1]

***

### Subtask 3 — Response Classification and Register Update

**Question:** Does each response constitute a resolution, and what does the register entry become?

**Output:** All BLOCKER entries reclassified; `resolutionnote` populated; `derivation_flag` set where applicable; cascade updates applied

#### Skills Required

- **Classification-before-action as a hard sequence rule.** The response is classified before any register entry is updated. The four classifications — `RESOLVED`, `CONFIRMED-UNKNOWN`, `DECISION-REQUIRED`, `UNCLEAR` — are mutually exclusive. An executor who begins updating the register mid-classification produces partial updates if the classification changes upon reading the full response. The most dangerous version: a response that starts with *"Yes, go with X"* and ends with *"but actually I'm not sure about Y"* — classifying on the first sentence produces `RESOLVED`; reading the full response produces `UNCLEAR`.[^21_1]
- **`derivation_flag` identification — acceptance of a rule, not a value.** When Alex says *"latest stable is fine"*, this is not a `RESOLVED` response with value *"latest stable."* It is an acceptance of a derivation rule: the executor is authorised to resolve *"latest stable"* to a specific version via lookup at the time of drafting. The `derivation_flag: true` in the exchange record is the machine-queryable signal that Task 1.4's pre-drafting step will query. An executor who records this as `RESOLVED` with `resolutionnote: "latest stable"` produces a manifest entry that violates the `techstack` format rule.[^21_1]
- **Linked cascade execution — a named step, not an implied side effect.** After each `RESOLVED` classification, the executor queries the register for all entries with `linked_questions` referencing the just-resolved entry's `questionid`. For each linked entry, the same resolution is applied, citing the same exchange reference. This is not optional — an unresolved linked entry after its parent entry is resolved is an inconsistent register. OQ-1-10 must be cascade-updated when OQ-1-05 is resolved; the manifest cannot have `deploymenttarget: Cloudflare Pages` and `constraints: fullyStatic` without both underlying entries being RESOLVED.[^21_1]
- **`UNCLEAR` handling — single follow-up, not re-presenting the full batch.** When a response is `UNCLEAR`, the executor identifies the single follow-up question that resolves the ambiguity — not the original question rephrased. *"You mentioned a timeframe — which of small, medium, or large best describes your appetite?"* is the follow-up for an UNCLEAR appetite response. The `initiatedat` timestamp of the original exchange is unchanged. A `followuprequestedat` timestamp is added.[^21_1]
- **`DECISION-REQUIRED` routing to FC-9.** When Alex's response indicates the information does not exist because a decision is unmade, the executor does not attempt further clarification. FC-3's scope ends here. FC-9 is invoked: a Decision Request record is created, the register entry is updated to `resolutionstatus: AWAITING-DECISION`, and the step enters a decision-specific block state. This routing is a loaded rule — an executor who attempts to resolve `DECISION-REQUIRED` through further clarification questions is working outside FC-3's scope.[^21_1]
- **Verbatim recording in `resolutionnote`.** Alex's response text is recorded verbatim — not summarised, not normalised. The traceability chain from field value back to human response depends on this verbatim record. A paraphrased `resolutionnote` cannot independently verify that the manifest value matches what Alex actually said.


#### Failure Modes

- **"Latest stable" recorded as a final value.** OQ-1-01 gets `resolutionnote: "AstroJS latest stable"`, `resolutionstatus: RESOLVED`, `derivation_flag: false`. Task 1.4's pre-drafting step has no `derivation_flag: true` entries to query. The manifest field is written as `AstroJS (latest stable)` — a format rule violation.[^21_1]
- **Cascade update missed.** OQ-1-05 resolved, OQ-1-10 not cascade-updated. Task 1.4 begins with OQ-1-10 still OPEN. The executor discovers this during required field population — the `constraints` field has an OPEN BLOCKER reference. Task 1.4 cannot proceed without re-engaging Task 1.3. The cascade update that should have happened in Subtask 3 becomes a Task 1.4 blocker.
- **`UNCLEAR` response upgraded to `RESOLVED`.** Alex says *"I think React is probably needed."* The executor records `RESOLVED: React confirmed.` The word *"probably"* signals uncertainty — this is UNCLEAR, requiring a follow-up. *"React 19.x"* in the manifest traces to an uncertain confirmation. A Step 2 executor who pulls React from the manifest has an unclear basis for it.[^21_1]

***

## Task 1.4 — Manifest Drafting: Skills by Subtask

**The question Task 1.4 answers:** *Can all confirmed values be structured into a valid, traceable manifest?*

**Output:** `project-manifest.yaml` in DRAFT status; `project-manifest.traceability.yaml` covering every non-empty field

***

### Subtask 1 — Pre-Drafting Derivation Resolution

**Question:** For every `derivation_flag: true` entry in the exchange record, what is the specific resolved value?

**Output:** Derivation entries in the traceability record; new register entries for any gaps discovered

#### Skills Required

- **Exchange record query as the first act of Task 1.4 — before field one.** The executor queries `CE-1-01.yaml` for all responses with `derivation_flag: true`. This is not optional and not a preliminary check — it is the first action of the task. An executor who begins populating fields before querying derivation flags will encounter the gap mid-population and must either retroactively update already-written entries or proceed with invalid placeholder values.[^21_1]
- **Version lookup capability or defined fallback.** Resolving *"latest stable"* to `AstroJS 5.3.0` requires external access to a package registry or release page. The executor must either perform the lookup or apply the defined fallback: `CONFIRMED-UNKNOWN`, register entry updated, field left empty. Guessing a version number is not a fallback — it produces an invented value with no source reference, which fails FC-1.[^21_1]
- **Implicit dependency detection during pre-drafting.** While resolving explicit derivations, the executor checks whether any resolved tech stack entry implies an unlisted dependency. React confirmed → `@astrojs/react` implied. This requires domain knowledge of the declared stack. The implication must produce a new register entry (OQ-1-14) before the value is written — the register entry is the evidence that the derivation was authorised, not invented.[^21_1]
- **Traceability entry format for derivation-resolved values.** Derivation-sourced values use `sourcetype: derivationrule` with a `sourcereference` that names the rule (`latestStableVersion`), the lookup date, the lookup source, and the authorising exchange reference. This is a more complex traceability entry than a `brief` or `clarificationanswer` type — the executor must know the format before writing it.


#### Failure Modes

- **Pre-drafting step skipped.** The executor begins populating `techstack` from the register's `resolutionnote` values. OQ-1-01 has `resolutionnote: "latest stable is fine"` and `derivation_flag: true`. The executor writes `techstack[^21_0]: AstroJS (latest stable)`. Format rule violation. `@astrojs/react` is never detected. The manifest's `techstack` is incomplete at DRAFT time.
- **Version guessed without lookup.** The executor cannot access npm. Rather than recording `CONFIRMED-UNKNOWN`, writes `AstroJS 5.x`. The traceability entry says `sourcetype: derivationrule` — but there is no lookup date, no lookup source, and no specific version. A verifier cannot confirm where `5.x` came from. FC-1 fails.[^21_1]

***

### Subtask 2 — Required Field Population

**Question:** Can each required field be populated with a specific, traced, format-conformant value?

**Output:** All required fields populated in `project-manifest.yaml`; corresponding traceability entries in companion record

#### Skills Required

- **Traceability-alongside-field as one operation, two writes.** Field value written → traceability entry written immediately — before moving to the next field. Not after all fields are written. Not in a separate pass. The two writes are simultaneous because the source reference is unambiguous at the moment of writing; reconstructing it later introduces risk of misattribution. An executor who writes the full manifest and then produces the traceability record is reconstructing provenance rather than recording it.[^21_1]
- **Description assembly rule — brief language without editorial voice.** The `description` field is assembled from multiple brief statements. Every sentence must trace to a named statement ID. No sentence from the executor's own voice may appear. The assembly rule: include project type, primary purpose, and key deliverable; exclude constraints, deployment details, and named actors — those have dedicated fields.  An executor who adds a sentence not sourced to the brief has introduced an invented value into a required field.[^21_1]
- **`techstack` format rule enforcement during population.** Entries must be named technologies with versions. An entry that passes the pre-drafting step (derivation resolved) but is written without a version number (e.g. `pnpm` version not confirmed during Task 1.3) must be caught here. The correct action: create a new register entry, resolve via derivation, then write. The pre-drafting step catches planned derivations; this subtask catches unplanned ones discovered during population.
- **`humanactors` entry structure.** The field requires at least one entry with `role: humandirector`, with `name` matching exactly the name that will be used in `approvedby` at Task 1.5. An executor who writes `name: Alex` rather than `name: Alex Chen` creates a mismatch that Task 1.5 Subtask 5's `approvedby` validation will reject.
- **`appetite` enum mapping from resolution note.** The `resolutionnote` for OQ-1-07 contains Alex's verbatim words (*"small — a few days of focused work"*). The manifest field value is the enum: `small`. The traceability entry cites the `resolutionnote`. An executor who writes `appetite: "small — a few days"` fails the format rule. The enum value and the verbatim quote are different things serving different purposes.


#### Failure Modes

- **Traceability written after all fields.** The executor writes all required fields, then produces the traceability record from memory of what was used for each field. `description` sources are reconstructed as S-01 only — the executor no longer recalls which other statements contributed. The FC-1 verifier checks `description` against S-01 and finds the sections and visual style content not present in S-01. FC-1 fails.[^21_1]
- **`pnpm` in `techstack` without version.** The executor writes `pnpm` — confirmed via CE-1-01 Q-CE-1-01-04, but no version was asked or answered. The format rule requires a version. The field is written without one because pre-drafting only caught the flagged derivations. No new register entry is created. Task 1.4 self-check item 3 (no placeholders in `techstack`) is later supposed to catch this — but `pnpm` without a version is not a placeholder in the traditional sense; it may pass a naive self-check.

***

### Subtask 3 — Optional Field Population

**Question:** For each optional field, should it be populated, left empty, or recorded as tentative with an open question reference?

**Output:** All optional fields either populated with traced values, explicitly empty, or recorded with register cross-references

#### Skills Required

- **Restraint on empty fields — empty is a valid, complete state.** An optional field absent from the brief is left empty (`[]` or `null` depending on type) with a traceability entry of `sourcetype: notpresentininput`. The executor must not populate it with a reasonable default. `existingassets: []` with `sourcetype: notpresentininput` is a complete, correct entry. `existingassets: ["none stated"]` is an invented value.[^21_1]
- **Tentative value handling for AMBIGUOUS optional fields.** A field with an ambiguous optional value — like `integrationrequirements` where Formspree was mentioned tentatively — must not be recorded as confirmed. The correct approach: record what was said, note it is tentative, reference the open question ID. `provider: Formspree (tentative — see OQ-1-08)` with `sourcetype: clarificationanswer, sourcereference: "CE-1-01 Q-CE-1-01-08: tentative mention only"` is a complete entry. A confirmed-sounding entry without the tentative notation will mislead Step 2.[^21_1]
- **`constraints` and `outofscope` format rule — stated, not inferred.** These fields have explicit prohibitions against inference. The executor must source every entry to a brief statement or clarification answer. An entry with no source reference is an invented constraint. Domain-knowledge-inferred constraints (*"AstroJS implies no SSR"*) are not valid entries — unless Alex explicitly stated the constraint in a form the executor can cite.[^21_1]
- **`referenceexamples` verbatim extraction.** If Alex named specific design references, they enter this field verbatim. The executor must not normalise (*"minimalist SaaS landing pages"* in place of *"Linear.app, Stripe marketing pages"*) or editorially describe. The reference names are the values.


#### Failure Modes

- **`integrationrequirements.provider` written as `Formspree` without tentative notation.** Step 2's integration section is drafted around Formspree. Alex later selects a different provider. Step 2 must be partially redrafted because a tentative brief mention was treated as a confirmed value.
- **`constraints` populated with inferred AstroJS static output constraint.** No brief statement says *"fully static."* The AstroJS default behaviour implies it. The executor writes `constraints: [fullyStatic: true, noServerRendering: true]`. FC-1 fails — no brief statement or clarification answer supports these entries.[^21_1]

***

### Subtask 4 — Open Questions Field Population

**Question:** Which register entries belong in the manifest's `openquestions` field?

**Output:** `openquestions[]` populated with all WARNING and INFO entries

#### Skills Required

- **Completeness test — all non-RESOLVED register entries must appear.** Every register entry with `resolutionstatus: OPEN` and classification `WARNING` or `INFO` must appear in `openquestions`. The executor cannot filter by *"likely to matter to Alex."* The manifest's `openquestions` field is the human-readable presentation of the register's non-blocking content. If it is incomplete, Task 1.5 presents an incomplete picture — Alex approves without knowing about gaps the process knows about.
- **`openquestions` entry format — field, gap, impact, classification.** Each entry maps to its register source: `field` is the register entry's `field` value, `gap` is the register entry's `gap` (verbatim — not paraphrased), `impact` is the register entry's `impact`, `classification` is WARNING or INFO. The executor must not rewrite these fields — they come from the register. Rewriting loses the traceability link between the manifest entry and its register source.[^21_1]
- **`CONFIRMED-UNKNOWN` entries included as WARNING.** Entries reclassified from BLOCKER to WARNING via `CONFIRMED-UNKNOWN` carry into `openquestions` with their current classification. They are not omitted because they were once BLOCKER — they are included because they remain unresolved and carry downstream impact. An executor who omits them because *"the BLOCKER was resolved"* misunderstands the distinction between *"the blocking condition is resolved"* and *"the gap is filled."*


#### Failure Modes

- **OQ-1-11 (schema_gap_flag) omitted.** The executor only includes entries with a named manifest `field`. OQ-1-11 has `field: null` (no manifest field exists). It is omitted. Alex reviews the manifest and approves without knowing that Cloudflare account readiness was noted but has no place in the manifest. Step 2's deployment section will either assume Alex needs to procure a Cloudflare account, or will ask again — re-raising a gap that Step 1 already knew about.
- **`openquestions` entries rewritten editorially.** OQ-1-08's `gap` field reads: *"Form handler provider not confirmed — Formspree mentioned tentatively."* The executor rewrites: *"The contact form configuration is still to be determined."* The rewrite loses the Formspree mention, loses the tentative qualifier, and loses the specificity. Task 1.5's review package presents the rewritten version to Alex. Alex approves without knowing Formspree was the tentative option.

***

### Subtask 5 — Self-Check

**Question:** Does the DRAFT manifest satisfy all correctness conditions before Task 1.5 review?

**Output:** 15-item self-check passed; `status: DRAFT` set only after all items pass

#### Skills Required

- **Self-check before `status: DRAFT` — not after.** `DRAFT` signals readiness for human review. Setting it before the self-check means a manifest with known defects reaches Alex. The self-check is the executor's quality gate — the reviewer in Task 1.5 is the human's quality gate. Both must exist; neither substitutes for the other.[^21_1]
- **Placeholder detection for `techstack` entries.** Self-check item 3 tests that no `techstack` entry contains a placeholder value (`latest stable`, `TBD`, `x.x`, or any non-specific version indicator). This requires the executor to know what a placeholder looks like. `AstroJS 5.3.0` is not a placeholder. `AstroJS 5.x` is. `AstroJS (latest)` is. An executor who cannot distinguish specific versions from version patterns will pass a manifest with invalid `techstack` entries.
- **FC-1 cross-reference test — every field has a traceability entry.** Self-check item 13 (or equivalent) requires the executor to confirm that the traceability companion record has an entry for every non-empty manifest field. This is not a count check — it is a field-by-field correspondence check. A companion record with 12 entries for a manifest with 14 non-empty fields passes a count check of *"entries exist"* but fails a field-by-field check.[^21_1]
- **`humanactors` structural check — at least one `humandirector` entry.** The executor confirms that `humanactors` contains at least one entry with `role: humandirector` and a `name` value that will match `approvedby` at Task 1.5. This cross-checks two fields against each other — not just each field in isolation.
- **`approvedat` and `approvedby` absence check.** These fields must not be present at DRAFT time — their presence would indicate they were set by the executor, not by Alex's action. An executor who pre-populates these fields in anticipation of Alex's approval has violated FC-4 Tier 1's requirement that approval is set by a human action.[^21_1]


#### Failure Modes

- **Self-check run after `status: DRAFT` is set.** The executor sets `DRAFT` to signal completion, then runs the self-check. A failure at self-check means the manifest has been presented to the system as ready when it is not. Depending on workflow design, Alex may receive the unverified manifest before the self-check failure is caught.
- **FC-1 check done by count rather than by field.** The traceability record has 11 entries. The manifest has 11 non-empty fields. Count matches — self-check passes. But `openquestions` has no traceability entry (it was populated from the register, not from the brief or clarification). The count coincidence masks the missing entry. A verifier later finds `openquestions` has no source reference. FC-1 fails post-approval.[^21_1]

***

## Task 1.5 — Human Review: Skills by Subtask

**The question Task 1.5 answers:** *Does Alex confirm that the manifest accurately represents their intent?*

**Output:** `project-manifest.yaml` in APPROVED status; FC-4 audit log entry; `RR-1-01.yaml`

***

### Subtask 1 — Presentation Preparation

**Question:** What exactly is Alex being asked to confirm, and is the review package accurate?

**Output:** Review package with Part 1 (field values) and Part 2 (open questions); `summaryvalidated: true` confirmed before delivery

#### Skills Required

- **Two-part structure distinction — field values and open questions are separate asks.** Alex is being asked to confirm two distinct things: (1) that field values accurately represent their intent, and (2) that they are aware of the unresolved gaps before approving. Conflating these into a single presentation produces responses that mix confirmation of values with reactions to gaps — which are harder to classify. A response to a mixed presentation may say *"yes but about that Formspree thing..."* — which is partly approval and partly a gap reaction. The two-part structure separates these.[^21_1]
- **Summary fidelity validation — every summary value checked against the manifest before delivery.** The review package summary is generated from the manifest — not from memory, not from the traceability record. Before delivery, every summary value is checked against its source manifest field. A rendering error in the summary means Alex approves a description of the manifest that doesn't match the canonical document. The executor cannot assume the summary is correct — it must be verified.[^21_1]
- **All open questions presented — no filtering by "likely relevance."** Part 2 must include all five OPEN register entries, classified by severity (WARNING before INFO). The executor must not filter by *"this one probably won't matter to Alex"* — that judgment is Alex's to make, not the executor's.[^21_1]
- **Approval instruction precision.** The instruction to Alex must name exactly what constitutes an approval and what constitutes a returned correction. *"Confirm the field values above accurately represent your intent, and that you have noted the open questions"* is specific. *"Does this look right?"* is not — it invites reflexive affirmation rather than deliberate review.


#### Failure Modes

- **Part 2 omitted.** Alex sees only field values. Approves. OQ-1-08 (Formspree unconfirmed, WARNING) was never presented. The approval is not informed consent. Task 1.5 is technically completed but the approval does not satisfy FC-4's requirement for an informed approval.[^21_1]
- **Summary not validated before delivery.** The `description` summary reads *"A single-page marketing website for Meridian Consulting with CMS support"* — a rendering error included a phrase from a prior draft. Alex reads the summary and approves. The canonical manifest contains no CMS reference. The approval is for a summary that does not match the document it purports to summarise.

***

### Subtask 2 — Presentation and Blocking

**Question:** Has the review package been delivered with an accurate timestamp and is the process genuinely blocked?

**Output:** `presentedat` set at moment of delivery; process suspended; `RR-1-01.yaml` filed

#### Skills Required

- **Record-before-deliver discipline — `presentedat` set at the moment of delivery.** Not when the executor decides to send. Not when Alex responds. At the moment the package reaches Alex. In a synchronous session these may be simultaneous. In any asynchronous workflow they are distinct events. The record must be created and `presentedat` set before delivery completes — otherwise the timestamp is a reconstruction.[^21_1]
- **Hard blocking without exception.** No further Task 1 work proceeds until Alex responds. No partial pre-loading of correction workflows. No drafting of anticipated correction outcomes. The block is genuine process suspension. An executor who performs preparatory work during the block has introduced assumptions about Alex's response that may not hold — and those assumptions may persist if the executor does not carefully undo them when the actual response arrives.
- **Review record as an FC-4 artefact — distinct from CE records.** `RR-1-01.yaml` is filed in `.framework/reviews/`, not in `.framework/clarifications/`. The distinction is not administrative — CE records document FC-3 clarification exchanges; RR records document FC-4 approval events. Conflating them loses the framework's ability to independently query approval events versus clarification events.[^21_1]


#### Failure Modes

- **`presentedat` set at response receipt time.** In an asynchronous workflow, Alex reviews the manifest two hours after delivery and responds. The executor creates the record when the response arrives and sets `presentedat` to the current time. The record shows Alex approved a manifest two hours before they received it. Audit trail integrity fails.[^21_1]

***

### Subtask 3 — Response Classification

**Question:** Is Alex's response an approval, a correction, or something that requires follow-up?

**Output:** `responseclassification: APPROVED | RETURNED | UNCLEAR`; appropriate path initiated

#### Skills Required

- **Read the full response before classifying.** The response is classified as a whole, not sentence by sentence. A response that begins *"Approved"* and ends with *"but appetite should be medium"* is `RETURNED`. Reading to the end before classifying is the single most important skill in this subtask — the most consequential misclassification (embedded correction treated as clean approval) results from classifying on the opening word.[^21_1]
- **Minimum explicit approval threshold — loaded definition, not judgment.** The threshold is: the response names the document (or is unambiguously in the context of the review) and contains a deliberate affirmation. Valid: *"approved"*, *"confirmed"*, *"yes, that's correct."* Invalid: *"fine"*, *"sure"*, *"looks good"*, *"ok."* This is a policy definition. The executor applies it mechanically — it is not a case where *"looks good sounds like an approval to me"* is a valid substitution.[^21_1]
- **Scope change detection for `RETURNED` responses.** When a correction modifies a field whose value was used to resolve a prior BLOCKER register entry, the executor must check whether the correction invalidates that resolution before applying it. Removing the `fullyStatic` constraint is not a simple field edit — it reopens OQ-1-10 (Workers/static contradiction). The executor must know which register entries were used to resolve which fields. This requires having the register open during classification.[^21_1]
- **`UNCLEAR` follow-up precision — one question, resolving one ambiguity.** When the response is `UNCLEAR`, the executor identifies the single follow-up question that resolves the ambiguity. Not the original question rephrased. Not a request to re-read the manifest. One question targeted at the specific ambiguity in the response.


#### Failure Modes

- **"Looks good to me" classified as `APPROVED`.** The audit log records this as the approval statement. A verifier reading the record cannot confirm a deliberate decision was made — *"looks good"* is not an explicit affirmation. FC-4 Tier 1 requires an explicit, deliberate approval statement. The approval is not FC-4 compliant.[^21_1]
- **Embedded correction ignored.** Response: *"Approved — but appetite should probably be medium since I said 1–2 weeks."* Classified as `APPROVED`. `status: APPROVED` set. Manifest contains `appetite: small` in an APPROVED document, directly contradicting Alex's last statement. The word "approved" led the executor to classify on the opening word, never reaching the correction at the end.[^21_1]

***

### Subtask 4 — Correction Application *(conditional)*

**Question:** Has the correction been applied correctly, and does the result need re-review?

**Output:** Corrected field value; new traceability entry with `sourcetype: correction`; old traceability entry retained with `supersedes` reference; `CR-1-xx.yaml`; change summary for re-presentation

#### Skills Required

- **Correction scope containment — only the corrected field changes.** The correction names a field and a value. Only that field is updated. Adjacent fields that the executor might judge should also change — because the correction implies something about them — are not touched unless explicitly corrected. If Alex corrects `appetite` to `medium`, `description` is not touched. Scope containment is not a courtesy — it is a discipline that prevents the executor from making scope decisions that belong to Alex.[^21_1]
- **Traceability chain integrity — retain old entry, add new entry with `supersedes`.** The correction produces a new traceability entry. The old entry is retained. Two entries for one field is correct — it is the audit trail of the field's history. An executor who replaces the old entry loses the record that the value changed. A verifier reading the manifest cannot confirm the correction occurred — the field looks as though `medium` was always the value.[^21_1]
- **Value correction vs scope addition classification.** A correction that changes an existing field's value is applied directly. A correction that introduces new content (a new `techstack` entry, a new constraint) is a scope addition — it requires a lightweight Task 1.1–1.3 mini-cycle before entering the manifest. The executor must classify the correction before applying it. Applying a scope addition as a value correction produces an untraced field value with `sourcetype: correction` but no underlying brief statement or clarification answer supporting the added content.[^21_1]
- **Change summary for re-presentation.** Every re-presentation after a correction includes a change summary naming the field, the previous value, and the corrected value. Alex is asked to confirm the correction was applied correctly, not to re-read the full manifest. An executor who re-presents the full manifest without a change summary forces Alex to find the changed field — which they may or may not succeed at.
- **`UNSTABLE-FIELD` flag — triggered on second correction to the same field.** If the same field is returned for correction a second time, the executor flags it as `UNSTABLE-FIELD` and requests a definitive statement from Alex before re-presenting. This prevents the correction loop from cycling indefinitely on a field the human cannot seem to settle.[^21_1]


#### Failure Modes

- **Old traceability entry deleted.** `appetite` traceability record is updated in-place from `small` (CE-1-01 source) to `medium` (CR-1-01 source). The record now shows one entry with `sourcetype: correction`. A verifier reading this entry sees *"the appetite was corrected to medium"* but has no record of what it was corrected from. The correction event loses its evidential value — it looks like a field whose value was medium from the start, not one that changed.[^21_1]
- **Scope addition treated as value correction.** Alex says *"add Tailwind to the stack."* The executor adds `Tailwind CSS 3.x` to `techstack` with `sourcetype: correction, sourcereference: CR-1-01`. Tailwind was not in the brief, not in any register entry, not in any clarification exchange. Its addition implies new build tooling, new config entries, and potentially conflicts with Shadcn/ui's styling approach. None of these consequences are assessed. The manifest is re-presented with Tailwind in the tech stack as if it were a simple value change.[^21_1]

***

### Subtask 5 — Approval Recording

**Question:** Has the approval been recorded in a form that satisfies FC-4 Tier 1 with full attribution and accurate timestamps?

**Output:** `status: APPROVED`; `approvedat`; `approvedby`; FC-4 Tier 1 audit log entry; `RR-1-01.yaml` completed

#### Skills Required

- **`approvedby` exact-match validation against `humanactors`.** Before setting `status: APPROVED`, the executor confirms that the name in Alex's response — which may be *"Alex"*, *"Alex C"*, or *"Alex Chen"* — maps to exactly the `name` value in the `humanactors` entry. The manifest `approvedby` field must contain the exact value from `humanactors`. *"Alex"* as `approvedby` when `humanactors` contains *"Alex Chen"* is a mismatch that FC-4 rejects. The resolution: use the `humanactors` entry's `name` value, not the name as signed in the response, provided the identity is unambiguous.[^21_1]
- **`approvedat` as human action timestamp — not executor processing timestamp.** `approvedat` records when Alex approved — the datetime of Alex's response, not when the executor processed it. In synchronous sessions the gap is seconds. In asynchronous workflows it may be hours. The policy is explicit: record when the human acted. An executor who sets `approvedat` to the current datetime at the time of processing has misrepresented the approval timeline.[^21_1]
- **`approvalstatement` — verbatim, minimum 5 words, required.** The FC-4 audit log entry's `approvalstatement` field contains Alex's actual words. Not a paraphrase. Not a template statement (*"humandirector approved the manifest."*). Alex's verbatim words are the evidence of deliberate decision-making. A template statement is a status record — which already exists in the `status` field. The audit log entry is evidence, not a status mirror.[^21_1]
- **Post-approval immutability — no writes after `status: APPROVED`.** Once `status: APPROVED` is set, neither the manifest nor the companion traceability record may be modified. Any post-approval correction — however minor — requires returning the manifest to DRAFT and re-running Task 1.5 from Subtask 1. An executor who notices a traceability entry is incomplete after APPROVED is set must create a correction record rather than editing the companion file.[^21_1]
- **Audit log entry as independent evidence.** The audit log entry exists independently of the manifest field. The `status: APPROVED` field is a state indicator. The audit log entry is proof. Both must exist. An executor who considers the `status` field sufficient has not satisfied FC-4 Tier 1's requirement for an independent approval record.[^21_1]


#### Failure Modes

- **`approvedat` set to executor processing time in an asynchronous workflow.** Alex emailed approval at 11:00. The executor processes the email at 14:00. `approvedat: 14:00`. The audit trail shows the manifest was approved three hours after Alex actually acted. For a delivery with a strict timeline, this misrepresents the project history.[^21_1]
- **`approvedby: "humandirector"` — role title instead of name.** FC-4 requires attribution to a named human. A role title is not independently verifiable — it does not survive personnel changes, and it cannot be confirmed against the `humanactors` entry because `humanactors` contains names, not role identifiers as primary keys.[^21_1]
- **Traceability companion record updated post-approval.** The executor notices OQ-1-09's traceability entry is missing a `sourcereference`. Updates `project-manifest.traceability.yaml`. The manifest itself is unchanged — but the companion record, which together with the manifest constitutes the verified output set, has been modified after the seal was set. The APPROVED state is no longer fully intact. Any verifier whose check includes *"has the traceability record been modified post-approval?"* will produce a finding.[^21_1]

***

## Summary — Skills Compendium, Tasks 1.2–1.5

| Task | Subtask | Critical skill | Most consequential failure |
| :-- | :-- | :-- | :-- |
| 1.2 | ST1 Required fields | Three-gate sequence with Step 2/3 policy loaded; gap_type precision | Gate 3 not applied; format-invalid value passes as PRESENT |
| 1.2 | ST2 Optional fields | Conditional requirement recognition; `schema_gap_flag` awareness | Conditional WARNING misclassified as INFO |
| 1.2 | ST3 Contradictions | Contradiction always BLOCKER; linked pass as named step | Contradiction downgraded via domain knowledge; linking skipped |
| 1.2 | ST4 Non-mappable | Schema exhaustion check; no-entry documentation | Subtask skipped entirely; OQ-1-11/12/13 never created |
| 1.3 | ST1 |  |  |

<div align="center">⁂</div>

[^21_1]: i-am-making-progress-in-creati-fuGLU8hCRLyka3xtBTVglA.md

