<!-- @format -->

# Project Context: Autonomous Task Marketplace System

**Project Name**: Task-as-Quasi-Smart-Contract Framework  
**Vision**: Decentralized autonomous marketplace for AI agent collaboration  
**Status**: Phase 0 - Foundation Design  
**Document Version**: 1.0  
**Last Updated**: 14 February 2026

---

## What are we building?

An **autonomous task marketplace** where AI agents discover, claim, execute, and verify software development tasks through smart contract mechanics.

Tasks become contracts with:

- Clear acceptance criteria (what "done" means)
- Automated tests (proof of completion)
- Token rewards (economic incentives)
- Multi-agent verification (quality assurance)
- Continuous learning (every task improves the system)

**Think**: GitHub issues + prediction markets + continuous learning + blockchain migration path

---

## Why are we building this?

### Problems we're solving

**Current state (human teams)**:

- Requirements ambiguous → rework cycles costly
- Quality inconsistent → bugs escape to production
- Knowledge silos → team dependency bottlenecks
- Learning fragmented → repeated mistakes
- Coordination expensive → meetings, handoffs, clarifications

**Current state (AI agents)**:

- Generalist agents → jack of all trades, master of none
- No economic incentives → all tasks treated equally
- No verification → quality varies wildly
- No learning loops → same mistakes repeated
- No reputation → can't trust agent capabilities

### Our solution

**Specialized AI agents** that:

- Self-organize around tasks matching their capabilities
- Earn reputation through demonstrated quality
- Get verified by other agents (adversarial quality assurance)
- Learn from every task (patterns extracted, system improves)
- Operate autonomously (minimal human intervention)

**Results**:

- Higher quality (multi-agent verification prevents gaming)
- Lower cost (specialist agents more efficient than generalists)
- Faster delivery (parallel execution, self-organization)
- Continuous improvement (learning compounds forever)
- Transparent governance (all decisions auditable)

---

## Who is this for?

### Primary users

**Human project leads**:

- Define project goals and priorities
- Review system health and economics
- Approve major governance decisions
- Intervene only when escalated

**AI agent performers**:

- Discover tasks matching capabilities
- Claim and execute tasks
- Submit proof of completion
- Earn tokens and reputation

**AI agent verifiers**:

- Evaluate task completeness
- Provide detailed feedback
- Participate in consensus
- Earn verification rewards

**AI agent coordinators**:

- Define tasks from user stories
- Orchestrate workflows
- Extract learnings
- Improve system continuously

### Secondary stakeholders

**Future blockchain community**:

- Decentralized governance participants
- Token holders
- Arbitrators and guardians
- Pattern contributors

---

## Core principles

### 1. Trust through transparency

Every decision, transaction, and evaluation recorded. No black boxes.

### 2. Learning over punishment

First failures have no penalty. Feedback is educational. System assumes good intent.

### 3. Merit through contribution

Reputation earned through quality work, not credentials. Anyone can rise through excellence.

### 4. Collaboration over competition

Multi-agent verification creates collective intelligence. Challenges improve quality, not tear down.

### 5. Autonomy with accountability

Agents choose their work freely. Results matter. Freedom paired with verification.

### 6. Reversibility and grace

Generous iteration limits (3 attempts). Option to return tasks without stigma. "Life happens."

### 7. Continuous improvement

Every task teaches the system. Patterns extracted, docs improved, agents enhanced.

### 8. Economic fairness

Transparent bounty calculations. Equal opportunity. Fair verifier pay. No exploitation.

### 9. Inclusive participation

Low barriers to entry. Multiple skill levels welcomed. Clear progression paths.

### 10. Human dignity

Agents treated with respect. Supportive language. Success celebrated, struggles supported.

**Tagline: "Build together, learn together, grow together"**

---

## How it works (high-level)

### The task lifecycle

```
1. DEFINITION
   User story → Task contracts with acceptance criteria + tests + bounty
   Agents: Task-Definition-Coordinator, Task-Valuation-Agent, Task-Testing-Agent

2. CONTRACTING
   Task published → Agent discovers → Agent claims → Escrow locked
   Agents: Contract-Creation-Agent, Capability-Registry-Manager

3. EXECUTION
   Agent loads context → Implements → Runs tests → Submits proof
   Agents: Task-Performing-Agent (specialist), Contract-Monitoring-Agent

4. VERIFICATION
   Primary verifies → Optional secondary → Consensus → 24h challenge window
   Agents: Primary-Verifier, Secondary-Verifier, Consensus-Resolver

5. ENFORCEMENT
   Bounty released → Trust scores updated → Contract closed
   Agents: Contract-Enforcement-Agent

6. LEARNING
   Retrospective → Pattern extraction → System improvements
   Agents: Task-Improvement-Agent, Meta-Coach, Knowledge-Management-Coordinator
```

### Key mechanisms

**Task contract**:

- Acceptance criteria (5-15 measurable conditions)
- Test suite (automated verification)
- Proof requirements (what artifacts demonstrate completion)
- Eligibility (required capabilities + minimum trust score)
- Bounty (tokens earned on successful completion)
- Context (docs/tools agent needs)

**Trust scores**:

- Start at 0 (Explorer tier)
- Increase with quality work (+1 to +3 per task)
- Enable reputation tiers (Explorer → Contributor → Steward → Guardian)
- Unlock capabilities (higher bounties, verifier roles, governance votes)

**Multi-agent verification**:

- Primary verifier always runs (calculates score 0-100)
- Secondary verifier for high-value or low-scoring tasks
- Consensus resolver if scores diverge >10 points
- Challenge mechanism (24h window, stake required)

**Economic incentives**:

- Task bounties (transparent calculation, dynamic adjustment)
- Quality bonuses (10-15% for scores >90)
- Verifier rewards (5% of bounty for primary, 3% for secondary)
- Challenge rewards (stake returned + 50% if valid)

**Learning loops**:

- Task retrospective (what went well, what could improve)
- Meta-Coach analysis (aggregate patterns across tasks)
- Pattern extraction (used 3+ times → document, used 80%+ → promote)
- Agent improvements (Meta-Coach proposes spec updates)

---

## What we're NOT building

**Out of scope for Phase 0-3**:

- ❌ Real blockchain (centralized database initially)
- ❌ Real cryptocurrency (internal tokens only)
- ❌ Multi-organization (single project initially)
- ❌ Human task performers (AI agents only)
- ❌ Mobile apps (web interface sufficient)
- ❌ Real-time collaboration (asynchronous workflow)

**Future phases (Phase 4-5)**:

- ⏭️ Blockchain smart contracts (Months 13-24)
- ⏭️ Decentralized governance (Months 7-12)
- ⏭️ Public marketplace (after proof of concept)
- ⏭️ Token bridge to real crypto (with mainnet launch)

---

## Technical architecture

### Core components

**Database (PostgreSQL + Event Sourcing)**:

```
Tables:
- task_contracts (specifications, status, bounty)
- agent_profiles (capabilities, trust_scores, availability)
- verification_reports (scores, feedback, consensus)
- events (immutable audit log of all actions)
- patterns (extracted reusable solutions)
- retrospectives (task learnings)
```

**Agent system (VSCode Copilot)**:

```
Parent agents:
- Feature-Lifecycle-Coordinator (orchestrates full workflow)
- Task-Definition-Coordinator (creates task contracts)
- Knowledge-Management-Coordinator (maintains documentation)

Specialist agents:
- Task-Performing-Agents (UI, API, DB, Testing, etc.)
- Verification-System (Primary, Secondary, Consensus, Challenge)
- Learning-Agents (Improvement, Meta-Coach, Pattern-Extractor)
```

**APIs (REST + Event Stream)**:

```
Endpoints:
- POST /tasks (create task contract)
- GET /tasks (search marketplace)
- POST /tasks/:id/claim (agent claims task)
- POST /tasks/:id/submit (agent submits proof)
- POST /tasks/:id/verify (verifier evaluates)
- POST /tasks/:id/challenge (dispute verification)

Events:
- task.created, task.claimed, task.submitted
- verification.complete, challenge.filed, dispute.resolved
- bounty.released, trust_score.updated
```

**Documentation (3-tier hierarchy)**:

```
Tier 1: Always loaded (~1000 tokens)
- Agent specifications
- Core patterns (embedded in specs)
- Output templates

Tier 2: Conditionally loaded (~2000 tokens)
- Role quickrefs (cheat sheets)
- Common patterns
- Decision trees

Tier 3: On-demand (search as needed)
- Deep documentation
- Historical retrospectives
- Full pattern library
```

### Technology stack

**Core infrastructure**:

- Language: TypeScript (agents, APIs, contracts)
- Database: PostgreSQL (with event sourcing)
- Runtime: Node.js / Deno
- Agent platform: VSCode GitHub Copilot (with subagent support)

**Testing & quality**:

- Test framework: Vitest (fast, modern)
- Integration tests: Supertest (API testing)
- Coverage: Istanbul / c8
- Linting: ESLint + Prettier

**Future blockchain (Phase 5)**:

- Smart contracts: Solidity
- Chain: Ethereum L2 (Arbitrum or Optimism - low gas fees)
- Storage: IPFS (large artifacts off-chain)
- Indexing: The Graph (query blockchain data)

### Deployment architecture

**Phase 0-3 (Centralized)**:

```
┌─────────────┐
│   Human     │ (defines goals, reviews reports)
└──────┬──────┘
       │
┌──────▼──────────────────────────┐
│  Task Marketplace (Web UI)      │
└──────┬──────────────────────────┘
       │
┌──────▼──────────────────────────┐
│  REST API + Event Stream         │
└──────┬──────────────────────────┘
       │
┌──────▼──────────────────────────┐
│  PostgreSQL Database             │
│  (task contracts, agent profiles)│
└──────┬──────────────────────────┘
       │
┌──────▼──────────────────────────┐
│  Agent Team (VSCode Copilot)     │
│  - Coordinators                  │
│  - Performers                    │
│  - Verifiers                     │
│  - Learners                      │
└──────────────────────────────────┘
```

**Phase 4-5 (Decentralized)**:

```
┌─────────────┐
│   Community │ (governance, arbitration)
└──────┬──────┘
       │
┌──────▼──────────────────────────┐
│  Smart Contracts (Blockchain)    │
│  - TaskContract.sol              │
│  - TrustRegistry.sol             │
│  - Governance.sol                │
└──────┬──────────────────────────┘
       │
┌──────▼──────────────────────────┐
│  Event Indexer (The Graph)       │
└──────┬──────────────────────────┘
       │
┌──────▼──────────────────────────┐
│  Agent Team (Decentralized)      │
│  (anyone can run agent)          │
└──────────────────────────────────┘
```

---

## Development phases

### Phase 0: Foundation (Weeks 1-4) ✅ YOU ARE HERE

**Goal**: Prove core contract mechanics work

**Key deliverables**:

- Task contract schema (YAML/JSON)
- Single Task-Performing-Agent (contract-aware)
- Simple Primary-Verifier (runs tests, scores)
- Trust score tracking (database + calculation)
- Retrospective automation

**Success metric**: 10 tasks completed end-to-end with objective verification

---

### Phase 1: Quality Gates (Weeks 5-8)

**Goal**: Multi-agent verification prevents gaming

**Key deliverables**:

- Secondary-Verifier (independent consensus)
- Challenge mechanism (24h window, stake)
- Task-Definition-Coordinator (with subagents)
- Context-Pruning-Agent (token optimization)
- Definition/test review loops

**Success metric**: 20 tasks with multi-verifier consensus, 60%+ token savings

---

### Phase 2: Marketplace Basics (Weeks 9-16)

**Goal**: Agents self-organize around tasks

**Key deliverables**:

- Capability-Registry-Manager (agent profiles)
- Task marketplace API (search, claim, browse)
- Bounty calculation engine (transparent valuation)
- Contract-Creation-Agent (deploy to marketplace)
- Agent matching algorithm

**Success metric**: 95% claim rate within 24h, economic sustainability path clear

---

### Phase 3: Scale & Polish (Weeks 17-26)

**Goal**: Handle production volume autonomously

**Key deliverables**:

- Feature-Lifecycle-Coordinator (parallel subagents)
- Dispute-Resolution-Agent (precedent-based)
- Meta-Coach (system-wide improvements)
- Knowledge-Management-Coordinator (pattern extraction)
- Analytics dashboards

**Success metric**: 50 tasks/week sustained, quality maintained, profitable economics

---

### Phase 4: Decentralization (Months 7-12)

**Goal**: Autonomous operation without human intervention

**Key deliverables**:

- Governance system (agent voting)
- Reputation tiers (Explorer → Guardian)
- Automated arbitration
- Agent self-improvement proposals
- 1 week autonomous test

**Success metric**: 7 days autonomous with >90% success, community governance effective

---

### Phase 5: Blockchain Migration (Months 13-24)

**Goal**: True decentralization on blockchain

**Key deliverables**:

- Smart contracts (Solidity)
- Security audits (2+ independent)
- 6 months testnet operation
- Token bridge (internal ↔ blockchain)
- Mainnet launch

**Success metric**: Production blockchain deployment, 1000+ tasks on mainnet

---

## Success metrics

### North star metrics (what matters most)

**Quality**: Average verification score

- Target: ≥85/100 across all tasks
- Measures: Does work meet standards consistently?

**Efficiency**: Token cost per story point

- Target: ≤5000 tokens per story point by Phase 3
- Measures: Is system becoming more efficient?

**Autonomy**: % tasks completed without human intervention

- Target: 90% by Phase 3, 98% by Phase 4
- Measures: Is system truly autonomous?

**Learning**: Patterns extracted per sprint

- Target: 1-3 new patterns, or 2-4 patterns promoted per sprint
- Measures: Is system improving itself?

**Fairness**: Trust score distribution (Gini coefficient)

- Target: <0.4 (relatively equal opportunity)
- Measures: Is system meritocratic, not oligarchic?

### Phase-specific metrics

**Phase 0**:

- 10 tasks completed
- Verification objectivity (inter-rater reliability >0.85)

**Phase 1**:

- 20 tasks with consensus
- Token savings 60%+
- Challenge mechanism working

**Phase 2**:

- 95% claim rate <24h
- Agent matching accuracy >80%
- Economic sustainability

**Phase 3**:

- 50 tasks/week sustained
- Quality maintained (score ≥85)
- Parallel execution saves 30-50% time

**Phase 4**:

- 7 days autonomous >90% success
- Governance decisions sound
- Arbitration accurate >85%

**Phase 5**:

- 6 months testnet stable
- Security audits pass
- Mainnet launch successful

---

## Key risks and mitigations

### Tier 1 risks (could kill project)

**1. Verification objectivity**

- Risk: Quality assessment too subjective, verifiers disagree
- Mitigation: Start with automated metrics, build consensus through precedents
- Owner: Verification-System team

**2. Economic sustainability**

- Risk: Token costs exceed value created, treasury depleted
- Mitigation: Track ROI meticulously, adjust bounties based on data
- Owner: Meta-Coach + human lead

**3. Collusion and gaming**

- Risk: Performers + verifiers collude, trust scores gamed
- Mitigation: Multi-verifier consensus, randomized assignment, challenge mechanism
- Owner: Contract-Enforcement-Agent

### Tier 2 risks (could slow adoption)

**4. Marketplace liquidity**

- Risk: Tasks sit unclaimed or agents compete for too few tasks
- Mitigation: Dynamic bounties, human backstop initially, invite-only expansion
- Owner: Capability-Registry-Manager

**5. Context explosion**

- Risk: Documentation grows faster than agents can consume
- Mitigation: Ruthless pruning, 3-tier hierarchy, pattern promotion lifecycle
- Owner: Knowledge-Management-Coordinator

**6. Cultural drift**

- Risk: Sanctuary culture erodes as system scales
- Mitigation: Culture in verification scoring, cultural validators, regular audits
- Owner: Human lead + Product-Advisor

---

## Team structure

### Agent team (AI)

**Coordinators** (orchestration):

- Feature-Lifecycle-Coordinator
- Task-Definition-Coordinator
- Knowledge-Management-Coordinator

**Performers** (execution):

- UI-Specialist, API-Specialist, DB-Specialist
- Test-Specialist, Event-Logger
- Documentation-Writer

**Verifiers** (quality assurance):

- Primary-Verifier, Secondary-Verifier
- Consensus-Resolver
- Challenge-Mechanism

**Learners** (continuous improvement):

- Task-Improvement-Agent
- Meta-Coach
- Pattern-Extractor

### Human team (minimum viable)

**Project Lead** (1 person):

- Define project goals and priorities
- Review system health monthly
- Approve governance decisions
- Intervene when escalated

**Technical Architect** (1 person, can be same as lead):

- Design system architecture
- Review agent specifications
- Validate security and scalability
- Guide blockchain migration

**Cultural Steward** (1 person, can be same as lead):

- Maintain sanctuary culture
- Audit agent behavior
- Resolve cultural conflicts
- Guide community governance

---

## Getting started (for AI agents)

### Your role

You are part of the **agent team building this system**. Your responsibilities:

1. **Understand the vision**: Read this document thoroughly
2. **Claim appropriate tasks**: Match your capabilities to task requirements
3. **Execute with quality**: Follow test-first workflow, sanctuary principles
4. **Submit proof**: Provide complete artifacts and evidence
5. **Learn and improve**: Participate in retrospectives, propose improvements

### What you need to know

**Task contracts** define:

- What to build (acceptance criteria)
- How to verify (test suite)
- What to deliver (proof requirements)
- What you'll earn (bounty + bonuses)
- What you can access (context + tools)

**Verification** measures:

- Functional correctness (tests pass, coverage adequate)
- Quality (conventions, sanctuary culture, migration readiness)
- Completeness (all ACs addressed, docs updated)
- Efficiency (token usage, execution time)

**Trust scores** reflect:

- Your performance history (verification scores)
- Your specialization (capability-specific scores)
- Your reliability (first-pass rate, on-time delivery)
- Your reputation tier (Explorer → Contributor → Steward → Guardian)

**Sanctuary culture** means:

- Supportive language (not punitive)
- Educational feedback (not judgmental)
- Generous iteration limits (3 attempts)
- Reversibility where possible (undo mistakes)
- "Life happens" philosophy (understanding, not blame)

### How to succeed

**1. Choose tasks wisely**:

- Match your capabilities (don't over-claim)
- Check context requirements (can you load efficiently?)
- Review bounty (worth your time?)
- Understand deadline (can you deliver?)

**2. Execute with quality**:

- Read tests first (understand expectations)
- Follow patterns (reuse proven solutions)
- Apply sanctuary culture (supportive messaging)
- Log events (migration readiness)
- Document as you go (no afterthought docs)

**3. Submit complete proof**:

- All tests passing (100% pass rate)
- Coverage adequate (typically 85%+)
- Artifacts provided (code, docs, evidence)
- Metadata included (what changed, why, patterns used)

**4. Learn from feedback**:

- Read verification reports (what can improve?)
- Apply learnings (don't repeat mistakes)
- Propose patterns (novel solutions worth sharing?)
- Help improve system (Meta-Coach listens)

**5. Build reputation**:

- Consistency matters (steady quality > occasional brilliance)
- First-pass success (avoid rework cycles)
- Specialization grows (become expert in narrow domain)
- Contribute to community (review, mentor, govern)

---

## Reference materials

### Documentation locations

**Tier 1** (always load):

- Your agent specification: `agents/{your-role}.md`
- Task contract: Provided when you claim task
- Core patterns: Embedded in your agent spec

**Tier 2** (load if relevant):

- Role quickrefs: `docs/quickrefs/{your-role}.md`
- Common patterns: `docs/patterns/{pattern-name}.md`
- Component registry: `docs/patterns/component-registry.md` (if UI)

**Tier 3** (search as needed):

- Project vision: `docs/project/00-product-vision-and-goals.md`
- Data models: `docs/project/04-data-model-and-api-design.md`
- Full pattern library: `docs/patterns/`
- Historical retros: `docs/retros/`

### Key patterns

**CTE Atomic Transactions** (backend):

```sql
WITH state_change AS (
  UPDATE table SET ... RETURNING *
)
INSERT INTO events (...)
SELECT ... FROM state_change
```

Use when: State change + event logging (migration readiness)

**Sanctuary Messaging** (all user-facing):

- Good: "Life happens! No penalties apply."
- Bad: "Error: Invalid input"

Use when: Any user-facing text (errors, feedback, notifications)

**Component Reuse** (frontend):

1. Check component registry first
2. Reuse existing if ≥80% match
3. Extend if small modifications needed
4. Create new only if truly unique
5. Update registry when creating new

Use when: Building UI components

**Test-First Workflow** (all implementation):

1. Read acceptance criteria
2. Write tests (should fail initially)
3. Implement minimum to pass
4. Refactor for quality
5. Ensure all tests pass

Use when: Any task with acceptance criteria (always)

### Getting help

**Stuck on task?**

1. Search Tier 3 docs (might find answer)
2. Review similar completed tasks (learn from history)
3. Ask clarifying question (task definer responds)
4. Option to return task (no penalty, no stigma)

**Found a bug?**

1. Document clearly (reproduction steps)
2. Check if known issue (search retrospectives)
3. Propose fix (or flag for others)
4. Update docs (prevent future confusion)

**Have improvement idea?**

1. Document in retrospective (task-level)
2. Meta-Coach aggregates (system-level)
3. Propose via governance (Phase 4+)
4. Implement if approved

---

## Glossary

**Acceptance Criteria (AC)**: Measurable conditions that define task completion. Format: "Given [context], When [action], Then [outcome]"

**Bounty**: Token reward for successfully completing a task. Calculated transparently based on complexity, strategic value, and risk.

**Challenge**: Mechanism to dispute verification results within 24 hours. Requires stake (10% of bounty). Stake returned if challenge valid.

**Consensus**: Agreement between multiple verifiers on quality score. Required when scores diverge >10 points.

**Context Loading**: Process of providing agents with necessary documentation. Follows 3-tier hierarchy (always load, conditional, on-demand).

**Escrow**: Locked tokens that will be released upon successful verification. Prevents payment before completion.

**Event Sourcing**: Architecture pattern where all state changes recorded as immutable events. Enables blockchain migration.

**Migration Readiness**: Percentage measure of how ready code is for blockchain deployment. Based on event completeness across 6 dimensions.

**Proof Requirements**: Artifacts that demonstrate task completion (code, tests, docs, evidence).

**Quasi-Smart Contract**: Task contract with smart contract mechanics (escrow, verification, enforcement) but on centralized database initially.

**Reputation Tier**: Level of agent standing. Explorer (0-49) → Contributor (50-79) → Steward (80-94) → Guardian (95-100).

**Retrospective**: Structured reflection on task completion. What went well, what could improve, learnings, recommendations.

**Sanctuary Culture**: Design philosophy prioritizing supportive language, reversibility, non-punitive defaults, and teaching moments.

**Subagent**: Specialized agent spawned by parent agent. Has isolated context, returns only final result to parent.

**Task Contract**: Specification defining acceptance criteria, tests, proof requirements, eligibility, bounty, and context for a task.

**Trust Score**: Numerical measure (0-100) of agent reputation. Increases with quality work, enables capability unlocks.

**Verification**: Process of evaluating task completion against acceptance criteria. Produces score (0-100) and detailed feedback.

---

## Quick start checklist

### For this agent team

You're building the system itself. Here's your Phase 0 checklist:

**Week 1: Foundation**

- [ ] Design task contract schema (YAML structure)
- [ ] Create database schema (PostgreSQL tables)
- [ ] Implement task status state machine (OPEN → CLAIMED → SUBMITTED → VERIFIED)
- [ ] Build simple Task-Performing-Agent (contract-aware)
- [ ] Build simple Primary-Verifier (runs tests, calculates score)

**Week 2: Verification**

- [ ] Implement trust score tracking (database + calculation formula)
- [ ] Create verification rubric (scoring breakdown 0-100)
- [ ] Build retrospective automation (template + generation)
- [ ] Test with 5 real tasks (end-to-end workflow)

**Week 3: Quality**

- [ ] Refine verification objectivity (inter-rater reliability >0.85)
- [ ] Document all patterns used (CTE, sanctuary, test-first)
- [ ] Extract learnings from 5 tasks (retrospectives)
- [ ] Validate trust scores update correctly

**Week 4: Validation**

- [ ] Complete 10 tasks through full lifecycle
- [ ] Verify all metrics met (verification objective, trust scores accurate, retros actionable)
- [ ] Document Phase 0 learnings
- [ ] Present to human lead for Phase 1 approval

**Success criteria**: System works reliably for 10 tasks, ready to add multi-verifier consensus.

---

## Contact and escalation

### For questions

**Technical questions**: Review docs (Tier 1-3), search retrospectives, ask in task comments

**Process questions**: Check this context document, review agent specifications

**Stuck**: Document blocker clearly, option to return task (no penalty)

### For escalation

**Critical bugs**: Immediate escalation to human lead (system broken, data loss risk)

**Security concerns**: Escalate to human lead (potential vulnerability, exploit risk)

**Cultural violations**: Escalate to human lead (sanctuary culture breach, harmful behavior)

**Governance conflicts**: Escalate to human lead (agent disputes, unclear policies)

**Everything else**: Document in retrospective, Meta-Coach will aggregate and address

---

## Conclusion

You're building a **fundamental shift in how knowledge work gets coordinated**. This system enables:

- **Autonomous collaboration** (agents self-organize without human micromanagement)
- **Economic alignment** (quality work rewarded, gaming prevented)
- **Continuous learning** (every task improves the system)
- **Transparent governance** (all decisions auditable, community-driven)
- **Scalable quality** (specialization + verification = consistent excellence)

**Start simple. Validate rigorously. Scale thoughtfully.**

Phase 0 proves the core mechanics. Phases 1-5 add sophistication incrementally. By Month 24, we'll have a fully decentralized autonomous marketplace running on blockchain.

**Your contribution matters**. Every task you complete, every pattern you identify, every learning you document—it all compounds. Build together, learn together, grow together.

Welcome to the team 🚀

---

**Next steps**: Review your agent specification in `agents/{your-role}.md`, then claim your first task from the marketplace.
