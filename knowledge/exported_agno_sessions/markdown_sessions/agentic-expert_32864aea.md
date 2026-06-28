# Agentic Expert

| Field | Value |
|-------|-------|
| **Session** | `32864aea...` |
| **Type** | agent |
| **Agent** | Agentic Expert |
| **User** | pete@peterargent.com |
| **Created** | 2026-04-28T21:29:02 |
| **Runs** | 1 completed / 1 total |

## Run 1 — Agentic Expert ✓ COMPLETED

*2026-04-28T21:29:02* · `glm-5.1:cloud` · `7064c29d...`

### Prompt

I want an agent to create and manage my projects and tasks. It should have database tables that no other agents can access. There should be tables for projects, tasks, subtasks etc.

I can tell the agent to create a new project or add a new task. I can ask the agent about the projects and tasks and update details of the them. The agent can also receive the same instructions from some agents who have the capability.

This agent doesn't care about the details of the projects or tasks. Just the creation and management of them.

### Response

I'll design this as a clean **Aggregator** class agent — a record keeper that manages structure, never interprets content. Let me build the database schema and the complete Agno agent.Noted and stored. The schema design is saved and your memory has been updated with the Project Manager agent design details.

One connection worth flagging as you build this out: those `JSONB metadata` columns are exactly where the `properties: any` anti-pattern from your ONE Ontology critique could reappear. Right now they're empty vessels — convenient for flexibility. But if other agents start dumping unstructured data into them, you'll have type collision at the data layer inside your own agent. Worth considering whether metadata should eventually use the same Schema Registry pattern from PRISM, so that when a task or project is created with metadata, the schema of that metadata is validated rather than accepted as an opaque blob.

---
