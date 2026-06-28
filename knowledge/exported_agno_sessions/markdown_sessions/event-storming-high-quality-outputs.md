<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# List the outputs of an event storming session for agentic workflow design when the exercise has been completed at a very high standard. What are the characteristics of the outputs that make it high quality?

A high-standard Event Storming session for agentic workflow design produces outputs that are both **complete** (nothing missing) and **actionable** (directly usable by architects and engineers without further interpretation). Here's the full picture:

## Outputs of the Session

### Agentic Event Model

- Complete, chronologically ordered **domain event timeline** covering every meaningful state change an agent triggers or observes[^1]
- Every event named as a **past-tense verb phrase** ("TaskDecomposed", "ToolCallFailed", "HumanApprovalGranted") — unambiguous and implementation-ready[^2]
- **Event flows between agents/bounded contexts** drawn as directed arrows, making inter-agent communication explicit[^3]


### Task \& Dependency Artefacts

- **Full task decomposition tree** — every top-level goal broken into atomic, delegable subtasks[^4]
- **Dependency graph (DAG)** — explicit sequencing of tasks showing which are parallel-safe, strictly sequential, or conditionally dependent[^5]
- **Aggregate ownership map** — which agent or service owns which state, preventing conflicting writes[^1]
- **Tool call catalogue** — every external tool, API, and sub-agent invocation listed as a named command with its triggering condition[^6]


### Human-in-the-Loop Design

- **Escalation point register** — every identified step requiring human approval, review, or decision, with the reason categorised (irreversibility, risk, regulatory, low confidence)[^7]
- **Read models at decision gates** — the exact data a human reviewer needs to see before approving each gate[^4]
- **Policy definitions** — the explicit rules governing automated vs. human-handled paths[^1]


### System \& Architecture Outputs

- **Bounded context map** — agent responsibilities cleanly separated, with named interfaces at each boundary[^3]
- **Rollback and compensation flows** — what events are emitted and what actions are taken when a task fails mid-execution[^8]
- **Observability hooks catalogue** — every event identified as a logging or tracing point[^9]
- **Hotspot register** — unresolved questions, contested boundaries, and known risk areas, each with an owner[^3]

***

## Characteristics of High-Quality Outputs

### Completeness

- **No orphaned events** — every event has a command that caused it and a policy or agent that reacts to it[^2]
- **No orphaned commands** — every command has an actor (agent, user, or policy) and produces at least one event[^1]
- **All hotspots resolved or explicitly deferred** — none left ambiguous; each has a decision recorded[^2]
- **End-to-end coverage** — the model traces from the initial trigger all the way to the terminal state with no gaps[^4]


### Precision \& Naming

- **Ubiquitous language enforced throughout** — every term means exactly one thing; synonyms have been debated and resolved[^6]
- **Events are atomic** — each captures a single state change, not a bundle of changes ("OrderItemReserved" not "OrderProcessed")[^2]
- **Commands are imperative and specific** — "ValidateCustomerIdentity" not "Do Identity Check"[^1]


### Boundary Quality

- **Bounded contexts have a single, named responsibility** — no context does two unrelated things[^3]
- **Inter-context interfaces are minimal and explicit** — the only coupling between agents is through well-defined published events[^9]
- **No implicit shared state** — every data dependency is surfaced as a read model or event payload, not assumed[^4]


### Human Gate Design

- **Each gate specifies the triggering condition, the reviewer role, the read model, and the timeout behaviour** — not just "a human reviews this"[^10][^7]
- **Irreversible steps are clearly marked and always gated** — no irreversible action is on an autonomous path without explicit design sign-off[^7]


### Actionability

- **Every output maps directly to a backlog item, agent spec, or architecture decision record** — nothing is left as a vague diagram[^11]
- **The dependency graph is machine-readable or directly transcribable** — e.g., it can be rendered as a DAG in code without further interpretation[^5]
- **Rollback paths are as detailed as happy paths** — failure is a first-class citizen in the model[^8]
<span style="display:none">[^12][^13][^14][^15][^16][^17][^18][^19]</span>

<div align="center">⁂</div>

[^1]: https://contextmapper.org/docs/event-storming/

[^2]: https://xebia.com/blog/eventstorming-cheat-sheet/

[^3]: https://github.com/wwerner/event-storming-cheatsheet

[^4]: https://openpracticelibrary.com/practice/event-storming/

[^5]: https://www.gocodeo.com/post/dependency-graphs-orchestration-and-control-flows-in-ai-agent-frameworks

[^6]: https://tyk.io/blog/delivering-high-value-apis-using-eventstorming/

[^7]: https://www.elementum.ai/blog/human-in-the-loop-agentic-ai

[^8]: https://dev.to/danielbutlerirl/designing-agentic-workflows-the-core-loop-166d

[^9]: https://www.confluent.io/blog/the-future-of-ai-agents-is-event-driven/

[^10]: https://developers.cloudflare.com/agents/guides/human-in-the-loop/

[^11]: https://www.ssw.com.au/rules/event-storming

[^12]: https://arxiv.org/html/2512.08769v1

[^13]: https://www.linkedin.com/posts/andrewyng_new-short-course-event-driven-agentic-document-activity-7303155272661798913-gHuf

[^14]: https://www.crazehq.com/ai-agent/ai-agentic-workflows

[^15]: https://www.youtube.com/watch?v=C3FZL7hXj0Y

[^16]: https://www.putitforward.com/agentic-ai/agentic-orchestration-design-patterns

[^17]: https://www.youtube.com/watch?v=Gr_sLZ28Klw

[^18]: https://www.reddit.com/r/LLMDevs/comments/1qwd728/do_agentic_systems_need_eventdriven_architecture/

[^19]: https://www.boldare.com/blog/event-storming-guide/

