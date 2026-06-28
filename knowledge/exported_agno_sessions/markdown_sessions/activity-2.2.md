# Activity 2.2 — Evaluation and Validation: Knowing When to Trust AI

***

### The capability most training skips

Most introductions to AI at work focus on how to use it: how to write prompts, which tools to try, what tasks to start with. That's useful as far as it goes. But there's a more consequential skill that receives far less attention, and it's the one that separates professionals who use AI well from those who use it dangerously.

That skill is evaluation: the ability to look at an AI-generated output and make a sound, informed judgement about whether it is accurate, appropriate, and safe to act on.

This matters because AI outputs are not self-evidently reliable or unreliable. The same tool that produces a genuinely useful first draft in one situation can produce a fluent, confidently worded, completely wrong response in the next. The output looks the same in both cases. The difference is only visible to someone who knows what to look for.

This activity builds that capability. It covers why AI fails in the specific ways it does, how to recognise the warning signs, how to identify bias, how to verify efficiently, and what professional accountability requires of you regardless of how output was produced.

***

## Task 2.2.1 — Why AI Gets Things Wrong

***

### Starting with the mental model

In Task 1.1.2, you built a mental model of how generative AI works: a pattern-completion system trained on vast amounts of human text, optimised to produce plausible output rather than verified truth. That model is the foundation for everything in this activity.

If AI were optimising for accuracy, its failures would be random and easy to spot. The output would simply be incoherent when it was wrong. But because AI is optimising for plausibility, its failures are coherent. They look like correct answers. They use the right vocabulary, the right structure, the right level of confidence. This is what makes them professionally dangerous.

Understanding the specific ways AI fails gives you a much better chance of catching those failures before they cause a problem.

***

### Failure mode 1: Hallucination

Hallucination is the term used when an AI model generates content that is factually incorrect but presented as if it were accurate. The model isn't lying. It has no concept of truth or falsehood. It's producing text that statistically fits the pattern of a correct answer, even when no correct answer is available in its training data.

Hallucinations are most common in:

- Specific facts: statistics, dates, names, figures, percentages
- Citations and references: the model may generate a plausible-looking citation for a paper, study, or article that does not exist
- Recent events: anything that occurred after the model's training cutoff
- Niche or specialist topics: areas where the model has less training data and less pattern density to draw from

Hallucinations are particularly dangerous because they are often embedded in otherwise accurate, well-structured text. A document that is 90 per cent correct can cause significant problems if the 10 per cent that's wrong contains a figure used to make a decision or a reference presented to a client.

***

### Failure mode 2: Bias

AI models learn from human-generated data, and human-generated data contains the full range of human biases: cultural, demographic, linguistic, historical, and professional. The model learns from what exists, not from what is balanced or representative.

Bias in AI outputs is often subtle. It may show up as:

- A tendency to frame issues from a particular cultural or geographic perspective
- Default assumptions about who holds certain roles or occupies certain positions
- A preference for majority-represented viewpoints when presenting "balanced" perspectives
- Outputs that reflect historical norms rather than current best practice in areas like language, inclusion, and professional standards

Bias is particularly difficult to catch because it doesn't look like an error. The output is fluent and internally consistent. The problem is not what the model said, but what it assumed without saying it.

***

### Failure mode 3: Brittleness

AI models can perform impressively on typical cases and fail unpredictably on edge cases. This is called brittleness: reliable performance within the range of situations well-represented in training data, with unreliable performance outside it.

In practice, brittleness shows up when:

- A task involves a context, industry, or use case that is less common in the training data
- The prompt is slightly outside the pattern the model has strong examples for
- The required output format is unusual or highly specific
- Local, regional, or organisational specifics are involved that the model has limited exposure to

Brittleness is particularly relevant for Australian workplaces, because much of the content AI models are trained on reflects US legal frameworks, business conventions, and cultural norms. Outputs on topics with jurisdiction-specific dimensions, including employment law, privacy obligations, tax treatment, and regulatory compliance, should be treated with additional caution.

***

### Failure mode 4: Overconfidence

AI models do not express uncertainty the way humans do. A human subject matter expert will hedge, qualify, and flag their confidence level when they're on uncertain ground. An AI model will often produce equally fluent, equally confident-sounding text whether it's drawing on strong training data or filling a gap with plausible-sounding invention.

This means that the confidence of an AI output is not a reliable signal of its accuracy. An output that sounds definitive may be less reliable than one that includes caveats. And an output that includes appropriate-sounding caveats may still contain errors in the substantive claims those caveats are attached to.

The practical implication: treat all AI outputs as provisional, regardless of how authoritative they sound. The verification burden doesn't decrease because the output sounds certain.

***

### Failure mode 5: Compounding errors

In multi-step reasoning tasks, errors in early steps flow through to later ones. The model doesn't flag that an earlier conclusion was shaky; it builds on it as if it were solid.

This is most relevant when you ask AI to perform analysis, draw inferences, or make recommendations based on reasoning rather than simple retrieval. A plausible-sounding first-step error can produce a logically consistent but entirely wrong final output.

The implication is that verification needs to include not just the conclusions but the reasoning that produced them.

***

### What these failure modes have in common

All five failure modes share a structural cause: the model is optimised for producing plausible, well-formed text, and plausibility is not the same as accuracy. Each failure mode is a different expression of that same underlying property.

Knowing this doesn't make AI less useful. It makes you more capable of using it well, because you know what to look for.

***

### Asset note: AI failure modes explainer

*A one-page reference document covering the five failure modes with a plain-language explanation of each, a brief description of what it looks like in practice, and a workplace example illustrating the professional implications.*

***

## Task 2.2.2 — Five Red Flags in AI Output

***

### Evaluation needs a framework, not just instinct

Telling someone to "read AI output critically" is not enough. Critical reading is a skill, and like any skill it benefits from a structured approach that reduces the chance of missing something important.

The five red flags below are a practical evaluation framework. They don't require technical knowledge to apply. They require attention, professional judgement, and the willingness to slow down before using an output.

Not every output will trigger every flag. Some outputs are excellent and need minimal review. But having a consistent framework ensures that the review you do is reliable, not dependent on how much time you have or how confident the output sounds.

***

### Red flag 1: Vagueness

Vague outputs use general, non-specific language to create the impression of substance without providing it. They sound informative but don't actually commit to anything that could be checked or acted on.

**What it looks like:**

- Claims like "research shows that..." or "studies suggest..." with no specific sources
- "Many organisations have found that..." without naming any
- Generalisations presented as conclusions: "This approach has been shown to improve outcomes"
- Percentages or figures presented without a source: "Productivity increased by 23 per cent"

**Why it happens:** The model produces statistically likely phrasing for a topic. In professional writing, general claims with vague attribution are common, so the model produces them.

**What to do:** If a claim matters enough to include, it matters enough to verify. Either find the source for the specific claim or remove it. Do not pass on vague claims as if they are substantiated facts.

***

### Red flag 2: Implausibility

An implausible output doesn't match what you know about the subject, the context, or the organisation. It might be internally consistent but contradict something you know from direct experience, professional knowledge, or the material you provided.

**What it looks like:**

- A figure or statistic that seems much higher or lower than you'd expect
- A recommendation that contradicts well-established practice in your field
- A description of a process, role, or regulation that doesn't match your experience
- A conclusion that doesn't follow logically from the information provided

**Why it happens:** The model is drawing on its training data, which may not accurately reflect your specific industry, jurisdiction, or organisation. It has no way of knowing when its output contradicts your context.

**What to do:** Trust your professional knowledge. If something seems wrong, investigate before using it. The fact that the model stated it confidently is not a reason to accept it.

***

### Red flag 3: Internal inconsistency

Internally inconsistent outputs contain contradictions within the same response. The model may state something clearly in one section and contradict it in another, particularly in longer outputs.

**What it looks like:**

- A recommended approach in one paragraph that conflicts with guidance in another
- A figure stated as one value in an introduction and a different value later in the same document
- A conclusion that doesn't logically follow from the reasoning that preceded it
- A list of recommendations that includes items pointing in opposite directions

**Why it happens:** The model generates text sequentially. It doesn't maintain a coherent internal model of what it has already said, particularly in long outputs, the way a human writer would.

**What to do:** Read the whole output before using any of it. Check for contradictions between sections. If you find them, either resolve them yourself or prompt the model to clarify which position it intends to take and why.

***

### Red flag 4: Overconfidence

This red flag is the detectable surface of Failure Mode 4 from Task 2.2.1, where overconfidence is a property of how the model generates text. Here it becomes something you can spot and act on in the output itself.

Overconfident outputs make absolute or unqualified claims in areas where genuine uncertainty, complexity, or professional debate exists. They present contested questions as settled, and nuanced situations as straightforward.

**What it looks like:**

- "You should always..." or "You must never..." in contexts where the correct answer depends on circumstances
- Regulatory or legal statements presented as definitive without jurisdiction-specific qualification
- Medical, financial, or professional advice presented without appropriate caveats
- Confident recommendations in situations that clearly depend on organisational context the model doesn't have

**Why it happens:** Confident, direct language is statistically common in authoritative professional writing. The model produces the linguistic patterns of authority whether or not its underlying information supports them.

**What to do:** Add appropriate qualifications where they're missing, verify claims in regulated domains with a qualified professional, and be especially careful about sharing overconfident AI output with audiences who may not be in a position to evaluate it themselves.

***

### Red flag 5: Incompleteness

Incomplete outputs address part of what you asked while omitting something material. The output may be accurate as far as it goes, but if it's missing a significant element, acting on it could lead to poor decisions.

**What it looks like:**

- A list of options that omits a significant category or consideration
- An analysis that addresses the upside without the risks, or vice versa
- A summary of a document that captures some sections thoroughly but skips others without flagging the gap
- A recommendation that addresses the immediate question but not the downstream implications

**Why it happens:** The model responds to what you asked, not to what you needed. If your prompt didn't specify "include risks as well as benefits," the model may not include them.

**What to do:** Before accepting an output as complete, ask: what's missing? Is there a perspective, a risk, a counterargument, or a downstream consequence that should be here? If so, prompt the model to address it, or add it yourself.

***

### Using the five red flags as a review checklist

Before submitting or acting on any AI output that matters professionally, run this check:

- [ ] Are specific claims substantiated, or does the output rely on vague attribution? (Vagueness)
- [ ] Does anything conflict with what I know from professional experience or the materials I provided? (Implausibility)
- [ ] Are there any contradictions within the output itself? (Internal inconsistency)
- [ ] Are there claims that are more confident or absolute than the subject warrants? (Overconfidence)
- [ ] Is anything material missing that should be here? (Incompleteness)

This check takes two to three minutes on a typical output. It is the most practical single habit you can build for professional AI use.

***

### Asset note: Interactive output review task

*An in-platform activity presenting three AI-generated workplace outputs, each containing one or more red flags. Learners identify the specific flags present, explain why each is a problem in this professional context, and describe what they would do before using the output. Feedback explains the flags in detail and models the reasoning behind each.*

***

## Task 2.2.3 — Recognising Bias in AI Outputs

***

### Bias doesn't look like an error

Of the five failure modes covered in Task 2.2.1, bias is the hardest to catch. Hallucinations can be checked against sources. Internal inconsistencies can be spotted by careful reading. Overconfidence is visible in the language. But bias often doesn't announce itself. The output is fluent, internally consistent, and plausible. The problem is in what it assumes, excludes, or takes for granted.

Developing the ability to recognise bias in AI outputs is a distinct skill. It requires you to look not just at what the model said, but at what perspective it was speaking from.

***

### How training data shapes what AI "knows"

AI models learn from the data they're trained on. That data is a representation of human knowledge and communication up to a certain point in time, filtered through whatever sources were included in the training corpus.

The implications are significant:

- If a topic is discussed more from one cultural or geographic perspective, the model will tend to reflect that perspective
- If historical data contains demographic patterns that no longer reflect current norms, the model may reproduce those patterns
- If a professional field's literature is dominated by a particular viewpoint, the model will tend to produce outputs consistent with that viewpoint
- If a topic is simply underrepresented in the training data, the model's outputs on that topic will be less reliable

None of this is the result of a deliberate decision. It is a structural property of how large language models are built. But the professional consequences are real, and the responsibility for catching and correcting bias in outputs rests with you.

***

### How question framing shapes the answer you get

Bias doesn't only enter outputs through training data. It can also enter through the framing of your prompt.

The model responds to the assumptions embedded in your question, often without flagging them. If you ask "What are the advantages of implementing a four-day work week?", you are more likely to receive a list of advantages than a balanced analysis, even if you wanted the latter. The framing of the question shaped the framing of the answer.

This is important for two reasons. First, it means some apparent bias in an output is actually a reflection of how the question was asked. Second, it gives you a practical tool for testing outputs: change the framing of the prompt and see whether the answer changes in ways that reveal hidden assumptions.

**Prompt framing test:**
If you suspect an output may be framed in a particular direction, try an alternative prompt that frames the same question differently:

- "What are the arguments for and against...?"
- "What would critics of this approach say?"
- "What factors might make this approach inappropriate or ineffective?"

If the output changes significantly when you reframe the question, that tells you something about what assumptions the original framing was activating.

***

### Hidden assumptions: when defaults don't match your context

AI models have defaults. When your prompt doesn't specify certain things, the model fills them in based on what's most statistically common in its training data. These defaults are often invisible, and they often reflect the dominant context in the training data rather than your context.

Examples of hidden assumptions worth watching for:

**Geographic and legal defaults:** Outputs on employment law, privacy obligations, tax treatment, and regulatory requirements often default to US frameworks. In an Australian professional context, this is a specific and consequential gap.

**Organisational defaults:** The model has no knowledge of your organisation's culture, history, priorities, or constraints. When you ask for a recommendation, the model applies generic best practice, which may not be appropriate for your context.

**Audience defaults:** If you don't specify the audience, the model will produce output for whoever it assumes the typical reader of this kind of content is. That assumption may be wrong.

**Professional and disciplinary defaults:** In fields with established conventions, the model may default to one school of thought or one set of professional standards without flagging that alternatives exist.

The practical response to hidden assumptions is to make them explicit. State your context clearly in the prompt, and when reviewing the output, ask: what did this model assume about my situation that I didn't tell it?

***

### Demographic, cultural, and linguistic bias

Outputs involving people, roles, or groups can reflect demographic biases embedded in training data. These biases are often subtle but can have meaningful professional consequences.

Things to watch for:

- Default gender assumptions in descriptions of professional roles
- Cultural assumptions about communication style, family structure, or social norms embedded in examples or advice
- Language that reflects majority-culture perspectives when the context requires a more inclusive frame
- Descriptions of leadership, expertise, or authority that implicitly centre particular demographic groups

This is particularly relevant in communications and HR contexts, where outputs may be used to write job descriptions, performance frameworks, or staff-facing policies.

***

### Bias in analysis and recommendations

Bias in analytical outputs is different from bias in descriptive or narrative content. In analysis, bias shows up as a tendency to reproduce existing patterns rather than challenge them, or to frame options and recommendations in ways that favour the status quo.

This matters in strategic or advisory contexts, where the value of the analysis lies partly in its ability to surface possibilities or challenges that aren't already obvious. If the model's output simply reflects the most common approach in its training data, it may not be telling you anything you didn't already know, and may be reinforcing choices that deserve scrutiny.

When using AI for analytical or advisory work, it's worth explicitly prompting for challenge as well as support: "What would a strong critic of this approach argue?" or "What risks does this analysis not adequately account for?"

***

### Asset note: Bias scenario case study

*A 500-word case study describing a realistic professional situation in which an AI-generated output contains subtle but consequential bias. Learners identify the source of the bias, what assumptions the model made, what the professional consequences could be, and how the prompt and review process should have been different.*

***

## Task 2.2.4 — Verification Strategies

***

### Verification is a skill, not a reflex

Most professionals understand that AI outputs should be checked before use. Fewer have a structured approach to verification that scales across different task types and risk levels.

Without a structure, verification tends to be inconsistent: thorough when time allows, cursory under pressure, and guided by instinct rather than a considered assessment of what actually needs checking. This creates a gap between the principle of human oversight and the practice of it.

This task gives you a practical, tiered approach to verification that is proportionate to the stakes of the task and the type of content being checked.

***

### The verification spectrum

Not every AI output requires the same level of verification. The appropriate level depends on two factors: how consequential an error would be, and what type of content is most likely to contain one.

**Full independent verification**
Applied to outputs where errors could cause significant professional, legal, financial, or reputational harm. Every substantive factual claim is checked against an independent source. The output is treated as a starting point for research, not a finished product.

Applies to: external-facing documents, regulatory or compliance content, financial analysis, any output involving legal or professional advice, content that will be published or formally submitted.

**Targeted spot-check**
Applied to outputs where the overall structure and direction are likely sound but specific elements carry meaningful risk. The human identifies the highest-risk elements (typically specific facts, figures, dates, named sources, or regulatory claims) and verifies those, while accepting the rest on the basis of professional judgement.

Applies to: internal documents used for decision-making, briefing notes and talking points, research summaries that will be cited or acted on.

**Reasonable trust with light review**
Applied to low-stakes outputs where errors are easily caught and the consequences of an imperfect draft are minor. The human reads for overall quality and fitness for purpose but does not independently verify every claim.

Applies to: first drafts for internal circulation, content that will be substantially edited before use, routine correspondence generated from structured inputs.

***

### What to check: the highest-risk content types

Regardless of the verification tier, certain types of content carry disproportionate risk and should be checked as a matter of course:

**Specific statistics and figures**
Numbers are among the most common hallucination sites. If a figure matters, verify it against its source before using it. If you can't find the source, remove the figure or replace it with a general observation.

**Named citations and references**
AI models frequently generate plausible-looking citations for papers, reports, or articles that do not exist, or that exist but say something different from what the model attributed to them. Any citation that will be presented as evidence should be checked directly.

**Dates and timelines**
Models can be wrong about when things happened, when regulations came into force, or when current standards were published. Date errors are easy to miss and can have significant consequences in compliance contexts.

**Legal, regulatory, and professional standards**
These are high-risk for two reasons: errors can have serious consequences, and the model's training data may reflect standards from a different jurisdiction, an earlier version of the regulation, or a context that doesn't match yours.

**Quoted or attributed statements**
The model may generate a plausible quote from a named individual or organisation that was never actually said. Any attributed statement used in a professional context should be verified against the original source.

***

### Using AI to critique AI

One practical and underused verification technique is to use AI to review its own output. This doesn't replace independent verification for high-stakes content, but it can surface problems quickly and efficiently for medium-stakes tasks.

Useful prompts for self-review:

> "Review the output you just produced. List any specific factual claims that you are uncertain about or that should be independently verified before use."

> "What assumptions did you make about the context or audience in producing this output? List three assumptions and indicate whether they are likely to be correct."

> "Identify any parts of this output that could be misleading or incomplete for a reader who is not already familiar with the subject."

This technique sits in apparent tension with the mental model you've built: if the model has no concept of truth, why would its self-assessment be useful?

The answer is that the model isn't checking its own logic; it's doing something more limited and more useful. It's statistically recognising patterns in its own output that resemble uncertain, contested, or under-specified content. The same way it recognises patterns in any text. That's a weaker form of self-awareness than genuine knowledge, but it's enough to surface regions of the output worth scrutinising.

Think of the technique as a first-pass filter, not a final authority. The model won't catch everything, and it may not be aware of its deepest errors. But it reliably surfaces the uncertainty it can detect, and a human reviewer acting on those signals will do a more targeted and efficient job than one reviewing blind.

***

### Building verification into your workflow

Verification is most reliable when it's built into the workflow rather than added at the end. Three practices that help:

**Set the expectation in the prompt.** Include a line in complex prompts such as "Flag any specific claims you are uncertain about" or "Note where you've made assumptions about the context." This primes the model to surface uncertainty rather than paper over it.

**Identify your verification points before you start.** Before using AI on a task, decide in advance what you will verify and how. This prevents the situation where time pressure leads to skipping verification steps that were always intended.

**Keep a record.** For outputs that are formally submitted or acted on, note that they were AI-assisted and what verification was performed. This is good professional practice and, in some organisational contexts, a compliance requirement.

***

### Asset note: Verification checklist

*A one-page reference tool listing the most common verification failure points in AI outputs, with a tiered approach based on stakes and content type. Includes a brief guidance note on when each tier applies and a reminder of the key content types that require checking regardless of tier.*

***

## Task 2.2.5 — Appropriateness and Professional Accountability

***

### Accuracy is necessary but not sufficient

Everything in Activity 2.2 so far has focused on accuracy: catching what's wrong in AI outputs before it causes a problem. But there is a second, distinct dimension of output quality that is equally important in professional contexts, and it can't be assessed by fact-checking alone.

That dimension is appropriateness: whether an output is suitable for this audience, this situation, this professional context, and this moment, regardless of whether the information it contains is factually correct.

An output can be accurate and still be professionally wrong. A response that is technically correct but delivered in the wrong tone can damage a client relationship. An analysis that is factually sound but framed insensitively can cause significant internal harm. A communication that gets all the facts right but misreads the organisational moment can create exactly the problem it was meant to address.

Appropriateness is a judgement that requires human context. It is one of the reasons that human oversight is not just a procedural requirement, but a genuine professional contribution.

***

### What appropriateness means in practice

Appropriateness has several dimensions that are worth checking explicitly:

**Tone and register**
Is the tone appropriate for this audience and relationship? AI defaults tend toward a professional but generic register. In practice, the right tone for a message to a long-standing client is different from the tone appropriate for a new regulatory contact, which is different again from internal team communication. These distinctions require human judgement about relationship context that the model doesn't have.

**Timing and situational sensitivity**
An output that would be entirely appropriate in one situation can be wrong in another, based on context the model doesn't know. A summary of a cost-reduction initiative that is technically accurate but sent to a team that has just been through redundancies requires different handling than the same summary sent to a finance executive. The model produces the content; the human must assess the moment.

**Organisational and professional norms**
Every organisation has conventions about how communication should be framed, what language is appropriate, what level of formality is expected, and what topics require particular care. These norms are often unwritten and deeply contextual. They are invisible to the model and must be applied by the human reviewer.

**Audience assumptions**
An output calibrated for one audience can be inappropriate for another. Content written for specialists may be inaccessible or condescending when shared with a general audience. Content written for a general audience may oversimplify in ways that mislead specialists. The model produces an output calibrated for its best guess at the audience; the human must confirm that guess is correct.

***

### When technically correct output is professionally wrong

Consider the following scenario.

A manager uses AI to draft a response to a team member who has raised a concern about workload. The AI produces a clear, professional response that acknowledges the concern, references the organisation's wellbeing policies, and outlines the formal support options available.

The output is accurate. The policies it references are real. The support options are correct. But the response is impersonal, formal, and reads like a policy document rather than a response from a manager who knows this person. Sending it without significant revision would communicate the opposite of what was intended.

This is not an AI failure in the usual sense. It's a fit-for-purpose failure. The output was not wrong; it was not right for this situation. Catching this requires a human who understands the relationship, the history, and the professional context in a way the model never can.

***

### The accountability principle

Regardless of how an output was produced, the person who submits or acts on it is professionally responsible for it.

This is not a new principle applied specifically to AI. It reflects how professional responsibility has always worked: the person who signs off on a document, submits a report, sends a communication, or advises a client is accountable for that work, regardless of who or what contributed to its production.

AI does not change this. What AI changes is the ease with which professional outputs can be generated, and therefore the ease with which this principle can be inadvertently bypassed.

Practically, this means:

- Submitting AI-generated content without adequate review is not a risk-neutral act. If the content is wrong, inappropriate, or causes harm, the professional consequences attach to you.
- "The AI produced it" is not a defence in most professional, regulatory, or employment contexts. The question that matters is whether you, as the responsible professional, adequately reviewed and approved the output before it left your hands.
- This accountability does not diminish as AI tools become more capable. If anything, as tools become more fluent and outputs become harder to distinguish from human-produced work, the responsibility to review carefully becomes more important, not less.

***

### What professional frameworks say

Across professional domains, the principle that the practitioner is responsible for their output is embedded in codes of conduct, regulatory frameworks, and employment obligations.

In legal practice, a lawyer who submits AI-generated research containing errors is responsible for those errors. In financial advice, an adviser who relies on AI-generated analysis without adequate verification has not met their professional obligation. In healthcare administration, a practitioner who passes on AI-generated guidance without clinical review has not discharged their duty of care.

These obligations exist independently of what tool was used to produce the content. They are not suspended because AI was involved. In some jurisdictions and professions, using AI without appropriate oversight and verification may itself constitute a breach of professional standards.

If your role involves regulated professional obligations, the specific standards that apply to AI-assisted work in your field should be understood and followed. Your organisation's compliance or legal function is the appropriate starting point if you are unsure what those obligations are.

***

### Building the final judgement habit

The practice that ties all of Activity 2.2 together is this: before any AI-assisted output leaves your hands, apply a final human judgement.

This is not an additional burden on top of the verification and red-flag review you've already done. It's a brief, deliberate pause that asks three questions drawn from the mental model you built in Module 1:

**Is this accurate?**
Have I checked the specific claims that would cause a problem if wrong? Are there any red flags I haven't resolved?

**Is this appropriate?**
Is this the right response for this audience, this relationship, this moment? Would I be comfortable if the recipient saw both this output and the prompt I used to generate it?

**Am I accountable for this?**
If this output causes a problem, is my review process one I could defend? Would I be comfortable explaining how I used AI in producing this, and what oversight I applied?

If the answer to all three is yes, the output is ready. If the answer to any of them is no, it is not.

***

### Asset note: Appropriateness scenario

*A workplace case study presenting an AI output that is factually accurate but contextually and professionally inappropriate for the situation described. Learners identify the specific appropriateness failures, explain what human context the model lacked, and describe what a proper review process would have required. The case study is designed to make the distinction between accuracy and appropriateness concrete and professionally relevant.*

***

### Closing Activity 2.2

The five tasks in this activity have built a layered capability: understanding why AI fails in the ways it does, recognising the warning signs in outputs, identifying bias and hidden assumptions, applying verification proportionate to the stakes, and maintaining the professional accountability that no tool can substitute for.

These skills are the other side of the prompting skills you built in Activity 1.2. Effective AI use requires both: the ability to construct good inputs, and the ability to evaluate what comes back with genuine professional judgement.

Together, they constitute what it means to use AI well at work.

***

*Module 2 closes here. Module 3 applies everything built in the first two modules to your specific industry, organisation, and professional context: the AI use cases most relevant to your sector, your organisation's strategic direction and approved tools, the regulatory and ethical obligations that govern AI use in your field, and the practical steps for integrating AI into your team's everyday workflows.*

*Module 3 follows: AI in My Industry: Adoption, Ethics and Oversight.*
