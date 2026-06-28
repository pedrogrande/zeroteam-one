# Claude Code Instructions — Clause-Level Contract MVP

## Purpose

Build a minimal prototype to test one hypothesis:

> **Clause-level diffs + structured negotiation rounds reduce re-review time and increase trust compared to track changes in a Word document.**

This is a **validation prototype**, not a production app. Every decision should serve that test. Do not add features not listed here.

---

## Your behaviour rules for this project

- **Read relevant docs first** before writing any code.
- **Produce a written implementation plan** before touching any files.
- **Wait for explicit approval** on the plan before making changes.
- Ask one clarifying question at a time if anything is ambiguous.
- Do not design solutions until you understand the problem from multiple angles.
- Do not execute any step until the definition of done for that step is agreed.

---

## Hypothesis and definition of done

The prototype is complete enough to test when:

- A contractor can enter a contract as atomic clauses.
- A reviewer can see exactly which clauses changed between two rounds.
- Both sides can comment on individual clauses.
- The "changes only" view is the default — full contract is secondary.
- Two hardcoded personas work in two browser tabs with no login required.
- A real user can complete a review session without needing instructions from the builder.

**Stop before the prototype reaches that bar. Do not add features beyond it.**

---

## Stack

- **Backend:** Node.js with Express (or Fastify)
- **Database:** PostgreSQL
- **Deployment target:** Railway-compatible (standard Postgres + Node service)
- **Frontend:** Server-rendered HTML with minimal JS, or a simple React SPA — choose whichever is fastest to iterate
- **Auth:** None. Two hardcoded personas: `contractor` and `reviewer`. Persona is selected by a simple toggle or URL param (`?as=contractor` / `?as=reviewer`).

Do not introduce auth, sessions, or user management.

---

## What to build

### Data model

Implement these tables only. No others.

```
Contract
  contract_id       UUID PK
  title             TEXT
  status            TEXT  -- draft | negotiating | complete
  created_at        TIMESTAMPTZ

Section
  section_id        UUID PK
  contract_id       UUID FK → Contract
  parent_section_id UUID FK → Section (nullable)
  title             TEXT
  order_index       INT

Clause
  clause_id         UUID PK
  contract_id       UUID FK → Contract
  section_id        UUID FK → Section
  stable_key        TEXT        -- e.g. C-2.1.3-CMS
  current_version_id UUID FK → ClauseVersion (nullable, set after first version)
  status            TEXT        -- active | deleted
  created_at        TIMESTAMPTZ

ClauseVersion
  clause_version_id UUID PK
  clause_id         UUID FK → Clause
  version_number    INT
  author_persona    TEXT        -- 'contractor' | 'reviewer'
  text              TEXT
  created_at        TIMESTAMPTZ

NegotiationRound
  round_id          UUID PK
  contract_id       UUID FK → Contract
  number            INT
  locked_by_persona TEXT        -- 'contractor' | 'reviewer'
  locked_at         TIMESTAMPTZ (nullable — null = draft)
  status            TEXT        -- draft | locked

RoundClauseSnapshot
  snapshot_id       UUID PK
  round_id          UUID FK → NegotiationRound
  clause_id         UUID FK → Clause
  clause_version_id UUID FK → ClauseVersion
  diff_status       TEXT        -- unchanged | added | modified | deleted

ClauseComment
  comment_id        UUID PK
  clause_id         UUID FK → Clause
  author_persona    TEXT
  text              TEXT
  created_at        TIMESTAMPTZ
```

No integrity/hash tables. No blockchain tables. No user/party tables. No playbook tables.

### Application features

Build these screens and flows only.

**Contractor view**

1. **Contract list** — list of contracts. Button to create new.
2. **Contract editor** — clause tree on the left, detail panel on the right.
   - Add / edit / delete clauses within sections.
   - Each edit creates a new `ClauseVersion`.
   - Show a badge on each clause: "modified" if it differs from v1, "new" if added after initial creation.
3. **Pre-lock summary screen** — before locking a round, show:
   - Count of clauses: unchanged / modified / added / deleted vs last locked round.
   - List of which clauses changed.
4. **Lock and send** — locks the current round by setting `locked_at` and writing `RoundClauseSnapshot` rows.
   - After locking, show a copyable "reviewer link" (`?as=reviewer&contract=<id>`).

**Reviewer view**

1. **Default view: changes only** — on opening a contract, show only clauses with `diff_status` of `added | modified | deleted` since the last locked round.
   - Clearly labelled: added (green), modified (amber), deleted (red/strikethrough).
   - For modified clauses: show previous text and new text side by side or as a diff highlight.
   - Button to "View full contract" as a secondary option.
2. **Clause detail panel** — clicking a clause shows:
   - Current text.
   - Previous version text (if modified).
   - Comment thread.
   - A text field to add a comment.
   - A button to "Propose edit" — opens the clause text for editing, creates a new draft `ClauseVersion` attributed to `reviewer`.
3. **Lock and return** — reviewer locks their round and gets a link to send back to contractor.

**Shared / both personas**

- Full contract view (secondary): all clauses in section order with diff badges visible.
- Round history: list of locked rounds with who locked and when.
- No notifications, emails, or invites. Links are copied manually.

---

## What to fake or leave out

Do not build these. If they come up, defer them explicitly.

| Item | How to handle |
|---|---|
| Auth / login | Hardcoded personas via URL param |
| Blockchain / hashing | Omit entirely |
| eSignature | Omit entirely |
| AI suggestions | Omit entirely |
| Cross-clause dependency tracking | Omit — note it as a known gap |
| Document import (Word / PDF) | Omit — seed data entered manually |
| Notifications / email | Omit — links copied manually |
| Multi-party (3+ parties) | Omit — contractor + reviewer only |
| Playbooks | Omit entirely |
| Mobile responsiveness | Best effort only, not a priority |

---

## Seed data

Pre-load one contract so the prototype is immediately testable. Use the web development services agreement below.

Seed two rounds:

- **Round 1 (locked, by contractor):** the clauses as originally drafted.
- **Round 2 (draft, by reviewer):** with the following changes already applied so the diff view has something to show:
  - Clause 2.1.1: page templates increased from 12 to 15.
  - Clause 4.2: payment schedule changed (30/40/30 → 50/25/25).
  - Clause 9.1: warranty period extended from 30 days to 60 days.
  - New clause 2.1.6: "The website will include a blog module with tagging and basic RSS feed."

**Contract: Web Development Services Agreement**

```
Section 1 — Parties and Summary
  1.1  Parties
  1.2  Project summary

Section 2 — Scope of Work
  2.1  Deliverables
    2.1.1  Page templates
    2.1.2  Responsive design
    2.1.3  Content management system
    2.1.4  Analytics
    2.1.5  Contact form
  2.2  Exclusions
  2.3  Technologies and platforms
  2.4  Assumptions
  2.5  Third-party services

Section 3 — Project Timeline and Milestones
  3.1  Milestones
  3.2  Delays

Section 4 — Fees and Payment
  4.1  Project fee
  4.2  Payment schedule
  4.3  Additional work

Section 5 — Client Responsibilities
  5.1  Approvals and feedback
  5.2  Content and assets

Section 6 — Change Requests
  6.1  Change process

Section 7 — Intellectual Property
  7.1  Ownership of final deliverables
  7.2  Developer tools

Section 8 — Confidentiality
  8.1  Confidential information

Section 9 — Warranties and Liability
  9.1  Limited warranty
  9.2  Disclaimer
  9.3  Limitation of liability

Section 10 — Term and Termination
  10.1  Term
  10.2  Termination for convenience

Section 11 — Acceptance and Testing
  11.1  Acceptance

Section 12 — General
  12.1  Governing law
  12.2  Entire agreement
```

Clause text for seed data is available separately — ask the user to provide the source document, or use short placeholder text per clause if needed.

---

## Implementation plan (required before coding)

Before writing any code, produce a written plan covering:

1. **Project structure** — directory layout, key files.
2. **Database setup** — migration approach, how seed data is applied.
3. **Route plan** — list every HTTP route with method, path, and what it does.
4. **Component / template plan** — list every screen and what data it needs.
5. **Build order** — which pieces you'll build first and why.
6. **Risks and open questions** — anything that needs a decision before proceeding.

Present the plan and wait for approval before writing any application code.

---

## Known gaps to document, not fix

When the prototype is running, add a `KNOWN_GAPS.md` file listing:

- Cross-clause dependency: changing a defined term does not flag downstream clauses.
- Parallel editing: no conflict resolution if both personas edit the same clause simultaneously.
- Acceptance state: "locked" ≠ "mutually agreed" — no per-clause acceptance tracking.
- Open comment threads are not resolved or carried forward between rounds.
- No document export (PDF / Word) of the final contract.

These are deliberate omissions. They are research questions for after the hypothesis test.

---

## Done signal

The prototype is ready to test when:

- [ ] Seed data loads and is visible on first run.
- [ ] Contractor can edit a clause, see the version increment, and lock a round.
- [ ] Reviewer opens the contract and sees only changed clauses by default.
- [ ] Reviewer can identify all 4 seeded changes without being told what they are.
- [ ] Reviewer can comment on a clause and propose an edit.
- [ ] Both personas can navigate the full contract as a secondary view.
- [ ] No instructions are needed to complete a review session.
