---
name: google-calendar
description: Delegate calendar tasks to the CalendarAgent via AgentOS MCP. The thinking partner does not have direct calendar tools — it calls the calendar agent when the user needs to view, search, create, update, or delete events.
---

# Google Calendar (via CalendarAgent)

## When to Use

- The user wants to check their schedule, upcoming meetings, or availability
- The user wants to find free time slots for scheduling
- The user wants to create, update, or delete calendar events
- The user references a meeting, appointment, or time-based commitment

## How It Works

This skill delegates to the **CalendarAgent** via AgentOS MCP. The thinking partner calls `run_agent` with `agent_id="calendar-agent"` and passes the user's calendar request as the message. The calendar agent has full CRUD access and handles the operation.

## Delegation Pattern

When the user asks about their calendar:

1. Identify the calendar intent (view, search, create, update, delete)
2. Call `run_agent` with `agent_id="calendar-agent"` and a clear message describing what the user needs
3. Relay the calendar agent's response back to the user
4. Use the calendar context to continue the thinking partner conversation

## Key Rules

- Always confirm before asking the calendar agent to delete events
- When creating events, include a timezone unless the user specifies one
- When scheduling with others, ask the calendar agent to check availability first
- Date/time format: ISO 8601 (`YYYY-MM-DDTHH:MM:SS`)
