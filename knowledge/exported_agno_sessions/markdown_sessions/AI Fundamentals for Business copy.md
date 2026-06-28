# AI Fundamentals for Business

# Activity 1.1.0

## Task 1.1.1

What Is AI? (And What Isn't It?)

---

### The word "AI" is doing a lot of work

Artificial intelligence gets applied to everything from spam filters to self-driving cars to the chatbot that wrote a colleague's performance review. That range is part of why the term is so confusing, it covers genuinely different things that behave very differently.

This task gives you a clear, working definition of AI and its key variants, so you can think and talk about it accurately at work.

---

### Artificial Intelligence, the working definition

**Artificial Intelligence (AI)** is a broad term for computer systems designed to perform tasks that would typically require human-like cognitive abilities, things like recognising patterns, generating text, making predictions, or interpreting images.

The key word is *designed*. AI systems don't think, feel, or understand. They process inputs and produce outputs according to what they've been trained to do. How they're trained, and what they're trained on, varies enormously.

---

### Machine Learning, how most modern AI actually works

Most AI you'll encounter in a business context is built on **Machine Learning (ML)**.

Rather than following rules a programmer explicitly wrote, a machine learning system learns from examples. Feed it enough data, emails, images, transactions, text, and it identifies patterns that let it make predictions or decisions on new inputs.

- A spam filter that learns what spam looks like from millions of flagged emails → machine learning  
- A payroll system that calculates tax according to programmed rules → **not** machine learning, just software

This distinction matters. ML systems improve with more data, but they also inherit the biases and gaps in that data.

---

### Generative AI, the type you're most likely using

**Generative AI** is a specific type of machine learning that produces new content, text, images, audio, code, rather than just classifying or predicting.

Tools like ChatGPT, Microsoft Copilot, Google Gemini, and Anthropic's Claude are generative AI. When you type a question and get a written response, you're seeing generative AI at work.

What makes generative AI different:

- It doesn't retrieve pre-written answers, it *generates* a response each time  
- It can produce fluent, confident-sounding output even when it's wrong  
- It doesn't have a fixed list of correct answers, it produces what's statistically likely given its training

---

### Narrow AI vs. General AI

Every AI system you will use at work is **narrow AI**, a system built and trained to do specific things well. A tool that writes text brilliantly cannot drive a car. A tool that recognises faces cannot explain a legal clause.

**General AI**, a system that could reason flexibly across any task the way a human can, does not currently exist. You may have seen it discussed in the news or in AI company announcements; treat those claims with healthy scepticism.

|  | Narrow AI | General AI |
| :---- | :---- | :---- |
| **Exists today?** | Yes | No |
| **Examples** | ChatGPT, image recognition, recommendation engines | Hypothetical |
| **Scope** | Designed task only | Any cognitive task |
| **Business relevance** | High, this is what you'll use | Low, not a current workplace reality |

---

### Common misconceptions worth correcting now

| Misconception | Reality |
| :---- | :---- |
| "AI understands what I mean" | AI predicts likely responses based on patterns, it has no understanding |
| "AI is always accurate" | AI can produce plausible-sounding errors confidently, this is a known failure mode |
| "AI is just a smarter search engine" | Search retrieves existing content; generative AI creates new text |
| "AI will replace my job entirely" | AI changes how work is done; most roles will shift, not disappear |
| "AI is neutral and objective" | AI reflects biases in its training data, it is never fully neutral |

---

### Asset note: AI Landscape Map infographic

*This task is accompanied by a one-page visual showing how AI, Machine Learning, Deep Learning, and Generative AI nest inside each other, with common business examples at each level.*

---

---

## Task 1.1.2

How Generative AI Works (Without the Jargon)

---

### Why this matters for you

You don't need to know how to build an AI system to use one well. But you do need a basic mental model of how it works, because that model explains almost everything puzzling or frustrating about AI behaviour.

Why does it sometimes sound so confident and still be wrong? Why does the same question sometimes produce different answers? Why does it "hallucinate" facts? The answer to all of these lies in what's actually happening when you send a prompt.

---

### It was trained, not programmed

Most software follows rules a programmer wrote. If X, then Y. A calculator follows rules. A payroll system follows rules.

Generative AI is different. It was **trained**, exposed to enormous amounts of text (books, websites, articles, code, conversations) and allowed to learn statistical patterns in that text. No one wrote rules for what it should say. It learned what words and ideas tend to follow other words and ideas, across billions of examples.

The result is a system that can produce fluent, coherent text on almost any topic, because it has seen fluent, coherent text on almost every topic.

---

### It's predicting, not thinking

When you type a prompt, the model doesn't "look up" an answer. It doesn't consult a database of facts. It generates a response **word by word** (technically, token by token), each time predicting: *given everything I've been trained on and everything in this conversation so far, what is the most likely next word?*

Think of it like a very sophisticated autocomplete, one trained on so much text that its predictions are often remarkably useful.

This has a critical implication: **the model is optimising for plausibility, not accuracy.** It will produce text that reads like a correct answer whether or not it is one.

---

### Why AI sounds confident even when it's wrong

This is the most important thing to understand about generative AI in a professional context.

Because the model is predicting likely text rather than retrieving verified facts, it can:

- Generate a plausible-sounding statistic that doesn't exist  
- Cite a real author but invent a paper they never wrote  
- Give a confident legal or medical answer that is technically incorrect  
- Fill in gaps in its knowledge with what *sounds* right

This isn't dishonesty, the model has no concept of truth or falsehood. It's producing what statistically fits. This is what's called a **hallucination**: an output that is fluent and confident but factually wrong.

Knowing this doesn't mean you can't trust AI, it means you know *when* to check.

---

### Why the same prompt gives different answers

Generative AI models include a degree of randomness in how they sample from possible next words. This is partly by design, it makes outputs more varied and natural rather than robotic.

The practical result is that identical prompts can produce different outputs at different times. This isn't a bug. It's useful when you want creative options, and something to be aware of when you need consistent results.

---

### What it doesn't have access to (unless told otherwise)

A standard generative AI model has a **knowledge cutoff**, a point in time after which it wasn't trained on new data. It doesn't know what happened last week. It doesn't know your company's internal documents. It doesn't know what your colleague said in a meeting.

Some tools are connected to the internet or to your organisation's systems, but that's an additional capability, not the default. Always check what your tool has access to before assuming it knows something current or internal.

---

### The mental model in one sentence

*Generative AI is a pattern-completion engine trained on vast amounts of human text, optimised to produce plausible output, not verified truth.*

Hold that model in mind throughout this course, and most AI behaviour will start to make sense.

---

### Asset note: Explainer animation / scroll-based visual

*This task could be accompanied by a short animation or scroll-based visual walking through the journey from prompt → tokenisation → prediction → output, using a simple workplace example.*

---

---

## Task 1.1.3

What AI Can and Can't Do

---

### Calibrating your expectations

AI can do some things remarkably well. It can also fail in ways that are easy to miss, because the failures often look just like the successes. Building an accurate picture of capability, not over-inflated by hype, not dismissed out of hand, is one of the most practical things you can do as a professional.

---

### The four core capability types

| Capability type | What it means | Workplace examples |
| :---- | :---- | :---- |
| **Language** | Generate, summarise, translate, edit, classify text | Drafting emails, summarising reports, translating documents |
| **Vision** | Interpret and describe images, documents, diagrams | Reading invoices, analysing charts, extracting data from scanned forms |
| **Prediction** | Forecast outcomes based on patterns in data | Customer churn modelling, demand forecasting, risk scoring |
| **Generation** | Create new content (text, images, code, audio) | Writing copy, generating code, creating slide content |

Most tools you'll use day-to-day combine language and generation. Vision and prediction capabilities are more often built into specialist platforms or enterprise software.

---

### Where AI genuinely adds value at work

AI performs well when:

- The task involves **high volumes of text or data** that would take a human much longer  
- A **good first draft** is more valuable than starting from scratch  
- You need to **summarise or extract** key information from long documents  
- The task is **low-stakes enough** that an imperfect output is a useful starting point  
- You need to **generate options**, ideas, phrasings, variations, for a human to evaluate

---

### Where AI falls short or fails

AI performs poorly, or dangerously, when:

- **Accuracy is critical** and outputs won't be independently verified (legal, medical, financial advice)  
- The task requires **live or real-world data** the model doesn't have access to  
- **Context is everything** and the model lacks the organisational, relational, or cultural background to get it right  
- The task requires **genuine reasoning** rather than pattern completion (complex causal analysis, ethical judgement)  
- **Accountability matters**, AI cannot be held responsible; a human always is

---

### Hype vs. reality, three common claims

| The claim | The reality |
| :---- | :---- |
| "AI will automate entire job roles" | AI automates *tasks within roles*, not roles wholesale, especially where human judgement, relationship, or accountability is required |
| "AI is as good as a subject expert" | AI produces expert-*sounding* output; it doesn't have expert-*level* judgement, particularly in novel or high-stakes situations |
| "AI gets smarter the more you use it" | Standard AI tools don't learn from your individual conversations, each session typically starts fresh |

---

### Asset note: Interactive matching activity

*This task could be accompanied by a drag-and-drop activity where learners match a set of workplace task types to the AI capability category most relevant to each. Scenarios include both good matches and deliberate mismatches to test reasoning.*

---

---

## Task 1.1.4

AI Tools: A Landscape Overview

---

### Tool awareness without tool dependency

The AI tools landscape changes fast. New models are released frequently, interfaces update, features appear and disappear, and what's available varies by organisation and country. Rather than a tutorial on any one tool, this task gives you enough orientation to navigate the landscape, and a framework for evaluating any tool you encounter.

---

### General-purpose AI tools

These are the AI assistants most people encounter first. They accept natural language inputs and generate text, answer questions, help with drafting, summarising, coding, analysis, and much more.

| Tool | Made by | Where you might encounter it |
| :---- | :---- | :---- |
| **ChatGPT** | OpenAI | Direct via chatgpt.com; integrated in some business tools |
| **Microsoft Copilot** | Microsoft | Built into Microsoft 365 (Word, Outlook, Teams, Excel) |
| **Google Gemini** | Google | Built into Google Workspace (Docs, Gmail, Slides) |
| **Claude** | Anthropic | Direct via claude.ai; API integrations |

These tools share the same underlying architecture (large language models) and many of the same strengths and limitations. The differences, in tone, capability, privacy settings, data handling, matter less than the principles for using them well, which transfer across all of them.

---

### AI already built into your workplace software

You may already be using AI without thinking of it that way. Many tools your organisation uses daily have AI features embedded:

- **Email tools**, smart reply suggestions, draft assistance, email summarisation (Outlook, Gmail)  
- **Document tools**, writing suggestions, summarisation, content generation (Word, Google Docs)  
- **Communication platforms**, meeting summaries, transcription, action item extraction (Teams, Zoom)  
- **CRM and HR systems**, predictive scoring, automated reporting, candidate screening  
- **Search tools**, AI-generated answers layered over traditional search results

These embedded features are often enabled by default. It's worth knowing which ones are active in your organisation's tools and what data they process.

---

### A framework for any tool you encounter

When your organisation introduces a new AI tool, or you encounter one, apply this three-question check before using it for work purposes:

1. **What was it trained on?** Understanding the data source gives you a sense of its likely accuracy and blind spots.  
2. **What can it access?** Does it connect to the internet, your files, your email, your organisation's systems? What data are you sending to it?  
3. **Who is responsible for outputs?** What are the terms of service? What does your organisation's AI policy say about this tool?

If you can't answer these questions, that's useful information in itself, it means the tool warrants scrutiny before use.

---

### The tool-agnostic principle

The most durable AI skill isn't knowing how to use ChatGPT. It's developing the judgement to use *any* AI tool effectively, and the ability to evaluate tools critically when new ones appear.

The prompting principles, evaluation habits, and ethical awareness you build in this course apply whether your organisation uses today's leading tools or something that hasn't been released yet.

---

### Asset note: Tool overview sheet

*This task could be accompanied by a one-page reference card covering currently common tools, their primary use cases, data-handling considerations, and a blank row for your organisation's approved tools. The sheet is designed to be updated periodically.*

---

---

## Task 1.1.5

Reflection: A Mental Model That Transfers

---

### Why this matters more than any tip or trick

If you've spent any time looking up "how to use ChatGPT" online, you've probably come across lists of clever tricks, specific prompt templates, and step-by-step guides. Some of them are genuinely useful, for about six months, until the tool updates and the trick stops working.

AI tools change fast. Features are added and removed. New models behave differently from old ones. Interfaces shift. What works as a specific technique today may be irrelevant by the time your organisation's next AI tool arrives.

What doesn't change is the underlying logic of how to engage with AI well: the ability to construct a clear input, evaluate the output critically, and make a sound judgement about what to do with it.

---

### Three questions that always apply

Regardless of which tool you're using, these three questions should become second nature whenever you use AI for anything that matters at work:

**1\. Is this accurate?** Does this output reflect reality? Have I checked the specific claims, figures, or references that would cause a problem if they were wrong?

**2\. Is this appropriate?** Is this the right response for this situation, in tone, content, level of detail, and professional context? Would I be comfortable putting my name on this?

**3\. Am I accountable for this?** If this output is wrong, misleading, or causes a problem, who is responsible? (Spoiler: it's you, not the AI.)

These three questions don't replace careful prompting or critical evaluation, you'll build those skills in Module 2\. But they are the foundation. A professional who can reliably ask and answer these questions will use AI better than someone who knows a hundred tricks.

---

### What a durable mental model looks like

The mental model you've built in this activity is:

- AI is a **pattern-completion system**, not a reasoning or knowledge system  
- It produces **plausible output**, not verified truth  
- Its confidence is **not a reliable signal of accuracy**  
- It is a powerful **first-draft and augmentation tool**, not a replacement for judgement  
- You are always **responsible** for what you submit, regardless of how it was generated

This model will serve you across tools, roles, and the ongoing evolution of AI in your workplace.

---

### Reflection activity

Take 5–10 minutes to write a response to the following prompt. There's no word limit. Write in plain language, as if explaining your thinking to a colleague.

---

**Reflection prompt:**

*Look back at your responses to the AI Literacy Self-Diagnostic at the start of this activity.*

*Choose one belief, assumption, or expectation about AI that you held before working through this content, and describe how your thinking has shifted, or been confirmed, or become more nuanced.*

*Then answer: based on what you now understand, what is one thing you'll do differently (or more carefully) the next time you use an AI tool at work?*

---

*Your reflection is saved as a personal learning record. In the final module, you'll revisit it as part of your overall course reflection.*

---

### What's next

You now have a clear mental model of what AI is, how generative AI works, what it can and can't do, and how to evaluate tools critically.

**Activity 1.2** builds directly on this foundation, moving from understanding to practice. It focuses on getting the best out of AI in your day-to-day work: how to construct effective prompts, how to iterate, and how to make AI a genuinely useful part of how you work.

---

*End of Activity 1.1. Introducing AI in Business*