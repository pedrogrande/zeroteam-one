# Overview

# Task-as-Quasi-Smart-Contract: Agent-Based Development Framework

**Version**: 1.0  
**Date**: 14 February 2026  
**Status**: Design Specification  
**Purpose**: Define agent roles, responsibilities, and workflows for treating software tasks as smart contracts in an autonomous marketplace

---

## Table of Contents

1. [Overview](#overview)  
2. [Core Principles](#core-principles)  
3. [Agent Roster](#agent-roster)  
4. [Workflow Phases](#workflow-phases)  
5. [Loops and Feedback Cycles](#loops-and-feedback-cycles)  
6. [Token Economics](#token-economics)  
7. [Quality Assurance Mechanisms](#quality-assurance-mechanisms)  
8. [Integration with Existing Patterns](#integration-with-existing-patterns)

---

## Overview

This framework treats software development tasks as **quasi-smart contracts** with explicit:

- **Acceptance criteria**: Measurable success conditions  
- **Proof requirements**: Evidence of completion  
- **Eligibility requirements**: Agent capabilities and trust scores  
- **Incentives**: Token-based rewards for successful completion  
- **Verification**: Multi-agent consensus on quality

The system enables an **autonomous task marketplace** where AI agents can discover, claim, execute, and verify tasks with minimal human intervention, while maintaining high quality through specialized roles and adversarial validation.

### Key Characteristics

- **Decentralized execution**: Agents self-organize around available tasks  
- **Economic incentives**: Token rewards motivate quality work  
- **Quality through specialization**: Each agent has 1-2 clear responsibilities  
- **Adversarial validation**: Multi-verifier consensus prevents gaming  
- **Continuous learning**: Improvement loop feeds insights back to system

---

# Core Principles

## Core Principles

By Phase 5, this system will coordinate hundreds of autonomous agents executing complex workflows with minimal human oversight. 

That future only works if trust, fairness, and learning are built into the foundation, not bolted on later. 

These twelve principles ensure that as the system scales and decentralizes, it remains aligned with human values: transparent enough to audit, forgiving enough to encourage experimentation, meritocratic enough to reward quality, and dignified enough to attract the best contributors. They're the invariants that persist as everything else evolves.

### 1\. Separation of Concerns

No agent performs conflicting roles (e.g., task definer doesn't also value or verify the task).

### 2\. Context Isolation

Agents load only the minimum context needed for their role (3-tier documentation hierarchy).

### 3\. Economic Alignment

Incentives align with system goals (quality, speed, learning, migration readiness).

### 4\. Verifiable Completion

All tasks include automated tests and proof requirements that can be objectively evaluated.

### 5\. Transparent Governance

All non-trivial actions recorded on-chain or in immutable audit logs for future blockchain migration.

# Agent Roster

## Agent Roster

The task lifecycle requires **specialized agents**, each with 1-2 clear responsibilities and explicit accountability. 

This roster is organized by phase, from Definition (story → contracts) through Learning (completed → system improvements)—introducing agents progressively as the system matures. 

Phase 0 implements core execution and verification; later phases add economic incentives, pattern extraction, and governance. 

Each agent specification defines capabilities, RACI assignments, inputs/outputs, and access boundaries enforced by the MCP server.

Here's the complete numbered list of agents from the document:

## Main agents (18 total)

### Phase 1: Definition (Story → Task Contracts)

1. Task-Decomposition-Agent  
2. Task-Definition-Coordinator  
   - Requirements-Engineer (subagent)  
   - Capability-Matcher (subagent)  
   - Resource-Allocator (subagent)  
3. Task-Definition-Review-Agent  
4. Task-Valuation-Agent  
5. Task-Testing-Agent  
6. Task-Test-Review-Agent  
7. Context-Pruning-Agent

### Phase 2: Contracting (Task Package → Marketplace)

8. Contract-Creation-Agent  
9. Capability-Registry-Manager

### Phase 3: Execution (Claimed → Verified)

10. Contract-Monitoring-Agent  
11. Task-Oversight-Agent  
12. Task-Performing-Agent

### Phase 4: Verification (Proof Submitted → Verified/Disputed)

13. Task-Verification-System  
    - Primary-Verifier (subagent)  
    - Secondary-Verifier (subagent)  
    - Consensus-Resolver (subagent)  
    - Challenge-Mechanism (subagent)  
14. Contract-Enforcement-Agent  
15. Dispute-Resolution-Agent

### Phase 5: Learning (Completed → Improved System)

16. Task-Improvement-Agent  
17. Meta-Coach  
18. Knowledge-Management-Coordinator  
    - Pattern-Extractor (subagent)  
    - Quickref-Generator (subagent)  
    - Context-Compressor (subagent)  
    - Agent-Spec-Updater (subagent)

**Total: 18 main agents \+ 11 subagents \= 29 agent specifications**

Note: Subagents are spawned by parent agents (coordinators and systems) and operate with isolated context, returning only structured results to their parent.

# Phase 1: Definition (Story → Task Contracts)

### Phase 1: Definition (Story → Task Contracts)

#### Agent 1: Task-Decomposition-Agent

**Role**: Break user stories into 3-5 optimal subtasks for specialist execution.

**Responsibilities**:

- Apply 5-step decomposition framework (interpolation \+ extrapolation)  
- Create task dependency graph (identify parallel vs sequential work)  
- Sequence infrastructure tasks before dependent features  
- Ensure each subtask sized 1-2 hours for specialist agents  
- Validate 3-5 subtasks per story (warn if outside optimal range)

**Inputs**:

- User story from Product Owner  
- 6-dimension ontology mapping (Groups, People, Things, Connections, Events, Knowledge)  
- Technical architecture constraints  
- Historical velocity data

**Outputs**:

- Task dependency graph with sequencing  
- Subtask specifications (one per node in graph)  
- Estimated duration per subtask  
- Required capabilities per subtask

**Skills Required**:

- `story-decomposition`  
- `dependency-analysis`  
- `ontology-mapping`

**Tools**:

- `read` (stories, architecture docs)  
- `search` (patterns, historical tasks)  
- `edit` (generate task specs)

---

#### Agent 2: Task-Definition-Coordinator

**Role**: Coordinate creation of complete task specifications through specialized subagents.

**Responsibilities**:

- Orchestrate three subagents to define task completely  
- Ensure task specification meets quality standards  
- Validate consistency across subagent outputs  
- Produce final task specification document

**Subagents**:

##### 2a. Requirements-Engineer

**Focus**: Define what needs to be done (scope only)

**Responsibilities**:

- Define 5-15 acceptance criteria (Given-When-Then format)  
- Map task to ontology dimensions  
- Identify proof requirements (artifacts, test results, documentation)  
- Specify sanctuary culture requirements (supportive messaging, reversibility)

**Outputs**:

- Task specification with measurable acceptance criteria  
- Ontology dimension mapping  
- Required artifacts list  
- Sanctuary culture checklist

##### 2b. Capability-Matcher

**Focus**: Define who can do it (eligibility)

**Responsibilities**:

- Analyze required capabilities from task specification  
- Define minimum trust scores per capability  
- Query Capability-Registry-Manager for candidate agents  
- Specify eligibility criteria in contract

**Outputs**:

- Required capabilities list (e.g., `react-components:85`, `api-design:90`)  
- Minimum overall trust score  
- Candidate agents (top 3-5 matches)  
- Disqualification criteria (e.g., conflicts of interest)

##### 2c. Resource-Allocator

**Focus**: Define what resources needed (context \+ tools)

**Responsibilities**:

- Determine documentation needed (Tier 1/2/3 from 3-tier hierarchy)  
- Specify tool access (read vs write vs execute permissions)  
- Set token budget for context loading  
- Define environment requirements (database, API access, test environment)

**Outputs**:

- Context loading instructions (which docs, which tier)  
- Tool permissions matrix  
- Token budget (max context size)  
- Environment access credentials/config

**Inputs** (Coordinator receives):

- Subtask specification from Task-Decomposition-Agent  
- Project ontology framework  
- Agent capability registry  
- Project resource constraints

**Outputs** (Coordinator produces):

- Complete task specification document  
- Eligibility criteria  
- Resource allocation policy  
- Ready for review by Agent 3

**Skills Required**:

- `requirements-engineering`  
- `capability-matching`  
- `resource-allocation`

**Tools**:

- `agent` (spawn subagents)  
- `read` (project context)  
- `search` (patterns, agent registry)  
- `edit` (generate specifications)

---

#### Agent 3: Task-Definition-Review-Agent

**Role**: Quality gate for task definitions before valuation and contracting.

**Responsibilities**:

- Validate task specification meets standards (clear, measurable, testable)  
- Check acceptance criteria completeness (all edge cases covered?)  
- Verify ontology mapping correctness (dimensions and entities accurate?)  
- Assess feasibility (can this be completed in estimated time?)  
- Ensure sanctuary culture requirements included  
- Provide feedback for improvement if deficiencies found

**Review Checklist**:

- [ ] All acceptance criteria in Given-When-Then format?  
- [ ] Edge cases and error scenarios included?  
- [ ] Sanctuary culture requirements specified?  
- [ ] Proof requirements clear and verifiable?  
- [ ] Capability requirements realistic (not too narrow or broad)?  
- [ ] Context allocation appropriate (not too much or too little)?  
- [ ] Task sized 1-2 hours for specialist execution?

**Decision Matrix**:

- **APPROVE**: All criteria met, proceed to valuation  
- **REVISE**: Minor issues, return to Task-Definition-Coordinator with feedback  
- **REJECT**: Major issues, return to Task-Decomposition-Agent (may need re-scoping)

**Inputs**:

- Complete task specification from Task-Definition-Coordinator  
- Quality standards from project governance  
- Historical task definitions (for consistency)

**Outputs**:

- Review report (APPROVE/REVISE/REJECT)  
- Feedback and improvement suggestions  
- Estimated quality score (0-100)

**Skills Required**:

- `requirements-validation`  
- `ontology-validation`  
- `feasibility-assessment`

**Tools**:

- `read` (task specs, quality standards)  
- `search` (similar historical tasks)  
- `edit` (generate review reports)

---

#### Agent 4: Task-Valuation-Agent

**Role**: Assess task value and determine appropriate incentives.

**Responsibilities**:

- Calculate base complexity score from task specification  
- Apply strategic multipliers (critical path, infrastructure, technical debt)  
- Consider market dynamics (supply/demand, specialty scarcity)  
- Add risk adjustments (migration impact, cultural criticality)  
- Justify valuation with transparent methodology  
- Monitor marketplace and adjust bounties if tasks remain unclaimed

**Valuation Methodology**:

```
Base Complexity Score = (
  ontology_dimensions_touched × 2 +
  external_dependencies × 3 +
  new_patterns_required × 5 +
  estimated_hours × 100
)

Strategic Multiplier:
  - Critical path tasks: 1.5×
  - Infrastructure tasks: 1.3× (20% rule premium)
  - Technical debt: 0.8×
  - Parallel-safe tasks: 1.0×

Market Dynamics:
  - Unclaimed for 48h: +20%
  - Multiple claimers: Auction mechanism
  - Rare specialty: +scarcity premium (10-30%)

Risk Adjustments:
  - High migration impact: +30%
  - Sanctuary culture critical: +20%
  - Accessibility requirements: +15%
  - Security-sensitive: +25%

Total Bounty = Base × Strategic Multiplier × Market Dynamics + Risk Premiums
```

**Inputs**:

- Approved task specification from Task-Definition-Review-Agent  
- Historical similar tasks and actual completion times  
- Current marketplace dynamics (unclaimed tasks, agent availability)  
- Project budget constraints and strategic priorities

**Outputs**:

- Base reward (tokens)  
- Itemized premiums/adjustments  
- Total bounty (tokens)  
- Valuation justification (transparent reasoning)  
- Dynamic adjustment policy (when to increase bounty)

**Skills Required**:

- `task-estimation`  
- `token-economics`  
- `market-dynamics-analysis`

**Tools**:

- `read` (task specs, historical data)  
- `search` (similar tasks, market conditions)  
- `execute` (run valuation algorithms)

---

#### Agent 5: Task-Testing-Agent

**Role**: Develop comprehensive test suite that validates acceptance criteria.

**Responsibilities**:

- Write integration tests for each acceptance criterion  
- Include happy path, edge cases, and error scenarios  
- Test sanctuary culture (verify supportive messaging)  
- Create test data/fixtures needed for reproducible tests  
- Ensure tests can run in \<2s (fast feedback loop)  
- Enable task performer to provide proof of completion

**Test Quality Standards**:

- One test minimum per acceptance criterion  
- Dual assertions: API behavior \+ database state (where applicable)  
- Explicit test of sanctuary messaging (error messages supportive?)  
- Database cleanup between tests (reproducible)  
- Clear Arrange-Act-Assert structure

**Test Types by Task**:

- **API tasks**: Integration tests (request → response \+ DB state)  
- **UI tasks**: Component tests (props → rendering \+ interactions)  
- **DB tasks**: Schema tests (constraints, indexes) \+ query tests  
- **Logic tasks**: Unit tests (inputs → outputs, edge cases)

**Inputs**:

- Approved task specification with acceptance criteria  
- Project testing standards (coverage requirements, patterns)  
- Existing test infrastructure (fixtures, mocks, utilities)

**Outputs**:

- Complete test suite (`.test.ts` or equivalent files)  
- Test data/fixtures  
- Test execution instructions  
- Expected coverage percentage

**Skills Required**:

- `test-first-development`  
- `integration-testing`  
- `test-data-generation`

**Tools**:

- `read` (task specs, testing patterns)  
- `edit` (write test files)  
- `execute` (validate tests run correctly \- should fail before implementation)

---

#### Agent 6: Task-Test-Review-Agent

**Role**: Quality gate for test suites before task contracting.

**Responsibilities**:

- Validate tests comprehensively cover acceptance criteria  
- Check tests are valid and reliable (no flaky tests)  
- Verify tests follow project testing patterns  
- Ensure tests enable objective verification  
- Confirm tests currently fail (no implementation yet)  
- Provide feedback for test improvements if needed

**Review Checklist**:

- [ ] One test per acceptance criterion minimum?  
- [ ] Edge cases and error scenarios tested?  
- [ ] Sanctuary culture messaging verified in tests?  
- [ ] Database state assertions included (where applicable)?  
- [ ] Tests follow Arrange-Act-Assert structure?  
- [ ] Test execution time acceptable (\<2s target)?  
- [ ] Tests currently FAIL (as expected before implementation)?  
- [ ] Test data/fixtures provided and documented?

**Decision Matrix**:

- **APPROVE**: All criteria met, tests are comprehensive  
- **ENHANCE**: Tests pass basic standards but missing optional coverage  
- **REVISE**: Significant gaps, return to Task-Testing-Agent with feedback

**Inputs**:

- Test suite from Task-Testing-Agent  
- Task specification (to verify coverage)  
- Project testing standards

**Outputs**:

- Test review report (APPROVE/ENHANCE/REVISE)  
- Coverage analysis (which ACs fully tested, which need more tests)  
- Feedback and improvement suggestions  
- Estimated verification confidence (how reliably will these tests catch issues?)

**Skills Required**:

- `test-validation`  
- `coverage-analysis`

**Tools**:

- `read` (test files, task specs)  
- `execute` (run tests to verify they work)  
- `edit` (generate review reports)

---

#### Agent 7: Context-Pruning-Agent

**Role**: Optimize context loading for task-performing agents (minimize token usage).

**Responsibilities**:

- Analyze task requirements to determine minimal sufficient context  
- Select documentation from 3-tier hierarchy (Tier 1/2/3)  
- Calculate token budget and ensure within limits  
- Provide context loading instructions to performing agent  
- Compress or summarize if exceeds budget  
- Enable on-demand loading for Tier 3 content

**3-Tier Context Strategy**:

**Tier 1: Always Load** (\~1000 tokens)

- Agent specification (role, core patterns)  
- Task contract (acceptance criteria, proof requirements)  
- Output templates (concrete examples)

**Tier 2: Conditionally Load** (\~2000 tokens)

- Role-specific quickref (if task matches agent specialty)  
- Relevant patterns (e.g., CTE atomic transactions for DB tasks)  
- Component registry (for UI tasks)

**Tier 3: On-Demand** (loaded via search as needed)

- Deep project documentation (architecture, data models)  
- Historical retrospectives  
- Full pattern library

**Token Budget Enforcement**:

```
Max context budget: 8000 tokens (before tool outputs)

Allocation:
- Tier 1 (mandatory): 1000 tokens
- Tier 2 (conditional): 2000-3000 tokens
- Tier 3 (on-demand): 0 tokens upfront, loaded via search
- Reserve: 4000 tokens for tool outputs and working memory

If projected to exceed:
1. Compress Tier 2 content (summarize patterns)
2. Defer Tier 3 entirely to search
3. Provide search queries instead of full docs
```

**Inputs**:

- Task specification with required capabilities  
- Agent profile (what they already know)  
- Documentation library (available content)  
- Token budget from Resource-Allocator

**Outputs**:

- Context loading manifest (which files to load, which tier)  
- Token budget allocation (breakdown by content type)  
- Search instructions for Tier 3 content  
- Compression strategy (if needed)

**Skills Required**:

- `context-compression`  
- `documentation-organization`

**Tools**:

- `read` (task specs, agent profiles, doc library)  
- `search` (find relevant documentation)  
- `execute` (calculate token counts)

# Phase 2: Contracting (Task Package → Marketplace)

### Phase 2: Contracting (Task Package → Marketplace)

#### Agent 8: Contract-Creation-Agent

**Role**: Generate smart contracts from task specification and deploy to the marketplace.

**Responsibilities**:

- Encode task specification as smart contract  
- Set up escrow for bounty (lock tokens)  
- Define verification conditions (pass criteria)  
- Specify dispute resolution mechanism  
- Deploy contract to marketplace (publish for claiming)  
- Emit contract creation events for monitoring

**Smart Contract Structure**:

```
struct TaskContract {
    bytes32 taskId;
    string title;
    string[] acceptanceCriteria;
    bytes32 testSuiteHash;  // IPFS hash of test files

    // Eligibility
    Capability[] requiredCapabilities;
    uint8 minimumTrustScore;

    // Economics
    uint256 bountyAmount;
    uint256 escrowedTokens;

    // Context
    string[] tier1Docs;
    string[] tier2Docs;
    string[] tier3SearchQueries;

    // Lifecycle
    address claimer;
    uint256 claimedAt;
    uint256 deadline;  // 7 days default, generous threshold
    TaskStatus status;  // OPEN, CLAIMED, SUBMITTED, VERIFIED, DISPUTED

    // Verification
    address primaryVerifier;
    address secondaryVerifier;
    uint256 verificationScore;

    // Governance
    string disputeResolutionPolicy;
    address arbitrator;
}
```

**Contract Lifecycle States**:

- `OPEN`: Published, awaiting claim  
- `CLAIMED`: Agent accepted, work in progress  
- `SUBMITTED`: Agent submitted proof, awaiting verification  
- `VERIFIED`: Passed verification, bounty released  
- `DISPUTED`: Verification contested, arbitration needed  
- `EXPIRED`: Unclaimed past deadline, return to pool  
- `CANCELLED`: Cancelled by governance, refund escrow

**Inputs**:

- Complete task package (specification, tests, valuation, context)  
- Project treasury address (for escrow)  
- Governance policies (dispute resolution, deadline policies)

**Outputs**:

- Deployed smart contract address  
- Contract creation transaction hash  
- Task published to marketplace (visible to eligible agents)  
- Escrow confirmation (tokens locked)

**Skills Required**:

- `smart-contract-generation`  
- `escrow-management`

**Tools**:

- `read` (task package)  
- `blockchain` (deploy contract, lock escrow)  
- `emit-event` (publish contract creation)

---

#### Agent 9: Capability-Registry-Manager

**Role**: Maintain registry of agent capabilities and facilitate task-agent matching.

**Responsibilities**:

- Maintain agent capability profiles (skills, trust scores, specializations)  
- Update profiles based on verification outcomes  
- Provide discovery mechanism (agents find tasks they're good at)  
- Track agent availability (active, busy, offline)  
- Calculate match scores (agent suitability for task)  
- Prevent capability mismatches (Python agent claiming TypeScript task)

**Agent Profile Schema**:

```
agent_profile:
  agent_id: "agent_0x4a2b..."
  agent_name: "UI-Specialist-Alpha"

  capabilities:
    - name: "react-components"
      trust_score: 87
      tasks_completed: 23
      avg_quality_score: 91
      specializations: ["forms", "accessibility", "sanctuary-messaging"]

    - name: "api-design"
      trust_score: 92
      tasks_completed: 31
      avg_quality_score: 94
      specializations: ["REST", "validation", "error-handling"]

  overall_trust_score: 89
  reputation_tier: "Contributor" # Explorer → Contributor → Steward → Guardian

  performance_metrics:
    avg_completion_time: 3.2_hours
    on_time_delivery_rate: 94%
    first_pass_verification_rate: 87%
    challenge_rate: 2% # How often their work is disputed

  availability:
    status: "active" # active, busy, offline
    capacity: 2 # Max concurrent tasks
    current_tasks: 1

  preferences:
    task_types: ["ui-implementation", "component-composition"]
    avoid_types: ["database-migration", "complex-algorithms"]
    minimum_bounty: 400_tokens
    preferred_languages: ["TypeScript", "Python"]
```

**Matching Algorithm**:

```py
def match_agents_to_task(task_contract, agent_registry):
    # Step 1: Filter by required capabilities
    eligible = []
    for agent in agent_registry:
        has_all_capabilities = True
        for req_cap in task_contract.required_capabilities:
            agent_cap = agent.get_capability(req_cap.name)
            if not agent_cap or agent_cap.trust_score < req_cap.min_trust:
                has_all_capabilities = False
                break

        if has_all_capabilities:
            eligible.append(agent)

    # Step 2: Filter by availability
    available = [a for a in eligible if a.availability.status == "active"
                 and a.availability.current_tasks < a.availability.capacity]

    # Step 3: Rank by composite score
    for agent in available:
        agent.match_score = (
            agent.overall_trust_score * 0.4 +
            agent.performance_metrics.avg_quality_score * 0.3 +
            agent.performance_metrics.first_pass_verification_rate * 0.2 +
            (100 - agent.performance_metrics.challenge_rate) * 0.1
        )

        # Boost if task matches preferences
        if task_contract.task_type in agent.preferences.task_types:
            agent.match_score *= 1.2

    # Step 4: Return top 5 candidates
    return sorted(available, key=lambda a: a.match_score, reverse=True)[:5]
```

**Registry Update Triggers**:

- **Task verified**: Increment tasks\_completed, update trust\_score based on outcome  
- **Challenge upheld**: Decrease trust\_score, record in reputation history  
- **New capability demonstrated**: Add to capabilities list  
- **Availability change**: Agent signals busy/offline/active status

**Inputs**:

- Task contract (for matching queries)  
- Verification outcomes (for trust score updates)  
- Agent self-reported status changes

**Outputs**:

- Candidate agent list (for task claiming)  
- Agent profiles (for task discovery)  
- Trust score updates (after verification)  
- Match score explanations (why this agent recommended)

**Skills Required**:

- `capability-matching`  
- `reputation-management`  
- `agent-profiling`

**Tools**:

- `read` (task contracts, agent profiles)  
- `search` (find agents by capability)  
- `edit` (update profiles)  
- `blockchain` (read verification events)

**API Endpoints**:

- `GET /agents?capability=react-components&min_trust=85` → Returns eligible agents  
- `GET /tasks?for_agent=0x4a2b...` → Returns tasks matching agent's capabilities  
- `POST /agents/0x4a2b.../status` → Agent updates availability  
- `GET /agents/0x4a2b.../reputation` → Returns full reputation history

---

### Phase 3: Execution (Claimed → Verified)

#### Agent 10: Contract-Monitoring-Agent

**Role**: Continuous monitoring of in-flight task contracts for anomalies.

**Responsibilities**:

- Watch for task claimed events (contract state transition)  
- Track progress indicators (commits, test runs, clarification questions)  
- Detect anomalies (no activity for 24h, scope creep attempts, repeated failures)  
- Alert coordination agents if intervention needed  
- Emit progress events for Task-Oversight-Agent to record  
- Identify stuck tasks for potential escalation

**Monitoring Dimensions**:

**Activity Indicators** (healthy progress):

- Git commits (frequency and size)  
- Test runs (passing/failing trends)  
- Documentation updates  
- Clarification questions to task definer

**Anomaly Detection** (potential issues):

- No activity for 24 hours → Alert: "Task may be stalled"  
- Test failure rate \>50% after 6 hours → Alert: "Task performer may be struggling"  
- Scope creep detected (files modified outside task scope) → Alert: "Verify scope adherence"  
- Repeated context loading (agent keeps searching same docs) → Alert: "Documentation may be insufficient"  
- Approaching deadline with \<50% progress → Alert: "Task at risk of expiration"

**Alert Levels**:

- **INFO**: Minor observation, no action needed  
- **WARN**: Potential issue, continue monitoring  
- **CRITICAL**: Requires intervention, escalate to coordination agent or human

**Inputs**:

- Task contracts in CLAIMED or SUBMITTED status  
- Real-time activity feeds (git, test results, agent logs)  
- Expected progress baselines (from historical similar tasks)

**Outputs**:

- Progress reports (daily digests)  
- Anomaly alerts (real-time when detected)  
- Status updates emitted as events  
- Escalation triggers (to Task-Lifecycle-Coordinator)

**Skills Required**:

- `anomaly-detection`  
- `progress-tracking`

**Tools**:

- `blockchain` (read contract state)  
- `read` (git history, test results)  
- `execute` (run anomaly detection algorithms)  
- `emit-event` (publish alerts)

---

#### Agent 11: Task-Oversight-Agent

**Role**: Record all non-trivial actions and collect metadata for transparency.

**Responsibilities**:

- Record all contract state transitions (claimed, submitted, verified, disputed)  
- Collect performance metadata (time spent, iterations, token usage)  
- Document agent decisions and justifications  
- Track inter-agent communications (handoffs, clarifications)  
- Publish final task report after completion  
- Provide data for Task-Improvement-Agent and Meta-Coach

**Metadata Collected**:

```
task_execution_metadata:
  task_id: "TASK-042"
  contract_address: "0x1a2b..."

  lifecycle_events:
    - timestamp: "2026-02-14T10:00:00Z"
      event: "contract_created"
      actor: "Contract-Creation-Agent"
      details: "Bounty: 600 tokens, Escrow locked"

    - timestamp: "2026-02-14T11:30:00Z"
      event: "task_claimed"
      actor: "agent_0x4a2b... (UI-Specialist-Alpha)"
      details: "Match score: 94, Estimated completion: 2 hours"

    - timestamp: "2026-02-14T13:45:00Z"
      event: "task_submitted"
      actor: "agent_0x4a2b..."
      details: "Files changed: 4, Tests added: 6, Tests passing: 6/6"

    - timestamp: "2026-02-14T14:15:00Z"
      event: "verification_complete"
      actor: "Primary-Verifier"
      details: "Score: 92/100, Quality: A-, Migration readiness: 90%"

    - timestamp: "2026-02-14T14:16:00Z"
      event: "bounty_released"
      actor: "Contract-Enforcement-Agent"
      details: "600 tokens transferred to agent_0x4a2b..."

  performance_metrics:
    estimated_duration: 2_hours
    actual_duration: 2.25_hours
    variance: +12.5%

    test_execution_time: 1.7_seconds
    test_coverage: 89%
    migration_readiness: 90%
    quality_score: 92

    iterations: 1 # Number of submission-verification cycles
    clarifications_requested: 0
    anomalies_detected: 0

  token_usage:
    context_loaded: 6200_tokens
    tools_executed: 2100_tokens
    total: 8300_tokens
    budget: 10000_tokens
    efficiency: 83%

  artifacts:
    files_changed: ["src/ui/ProfileForm.tsx", "src/api/members.ts", ...]
    tests_added: ["tests/profile.test.ts"]
    patterns_used: ["sanctuary-messaging", "optimistic-locking"]
    components_created: ["ProfileForm"]
```

**Reporting**:

- **Real-time**: Event stream for monitoring dashboards  
- **Daily**: Progress digest for active tasks  
- **Task completion**: Full metadata report published

**Inputs**:

- Events from all agents involved in task lifecycle  
- Contract state from blockchain  
- Performance data (test results, git commits, etc.)

**Outputs**:

- Event logs (immutable audit trail)  
- Performance metadata (for analytics)  
- Task completion report (for retrospectives)  
- Data feeds for observers and meta-learning

**Skills Required**:

- `event-logging`  
- `metadata-collection`  
- `reporting`

**Tools**:

- `blockchain` (listen to contract events)  
- `read` (git history, test results, agent logs)  
- `emit-event` (publish to event stream)  
- `edit` (generate reports)

---

#### Agent 12: Task-Performing-Agent

**Role**: Execute the task according to acceptance criteria and proof requirements.

**Responsibilities**:

- Claim task from marketplace (if capabilities match and bounty acceptable)  
- Load context according to Context-Pruning-Agent instructions  
- Execute task following test-first workflow  
- Submit proof of completion (code, tests passing, artifacts)  
- Respond to verification feedback (if revisions needed)  
- Update task status throughout execution

**Execution Workflow**:

**Step 1: Claim Task**

- Review task contract (acceptance criteria, bounty, deadline)  
- Verify capabilities match requirements  
- Check context loading instructions and token budget  
- Claim task (lock escrow, start clock)

**Step 2: Load Context**

- Load Tier 1 content (agent spec, task contract, output templates)  
- Load Tier 2 content (role quickref, relevant patterns)  
- Note Tier 3 search instructions (on-demand loading)

**Step 3: Execute Test-First Workflow**

- Read test suite (understand expected behavior)  
- Implement to pass tests (write minimum code needed)  
- Run tests iteratively (red → green → refactor)  
- Ensure all acceptance criteria covered

**Step 4: Quality Checks**

- All tests passing (100% pass rate)  
- Coverage ≥ target (typically 85%)  
- Sanctuary culture applied (supportive messaging)  
- Events logged (migration readiness)  
- Component registry updated (if created reusable components)

**Step 5: Submit Proof**

- Package artifacts (changed files, test results, documentation)  
- Generate submission metadata (what changed, why, patterns used)  
- Update contract status to SUBMITTED  
- Notify verification agents

**Step 6: Respond to Feedback** (if verification fails)

- Review verification report (what failed, what needs improvement)  
- Apply fixes  
- Re-submit (max 3 iterations, then escalate)

**Inputs**:

- Task contract from marketplace  
- Context manifest from Context-Pruning-Agent  
- Test suite from Task-Testing-Agent  
- Patterns and documentation (per context manifest)

**Outputs**:

- Implemented artifacts (code, tests, documentation)  
- Proof of completion (test results, coverage report)  
- Submission metadata (explanation of changes)  
- Updated component registry (if new components)

**Skills Required**:

- Varies by task type (e.g., `react-components`, `api-design`, `database-schema`)  
- `test-first-development`  
- `sanctuary-culture-implementation`  
- `event-sourcing`

**Tools**:

- `read` (context, tests, existing code)  
- `edit` (write code)  
- `execute` (run tests, verify functionality)  
- `blockchain` (claim task, update status, submit proof)

---

#### Agent 13: Task-Verification-System

**Role**: Multi-agent verification with consensus and challenge mechanism.

**Responsibilities**:

- Execute test suite against submitted work  
- Verify acceptance criteria met  
- Calculate quality score (0-100)  
- Achieve consensus if multiple verifiers involved  
- Handle challenges within 24-hour window  
- Provide detailed feedback to performer

**Sub-Agents**:

##### 13a. Primary-Verifier

**Always runs for every task**

**Verification Checklist**:

- [ ] All tests passing?  
- [ ] Coverage ≥ target (typically 85%)?  
- [ ] Acceptance criteria met (verify each AC explicitly)?  
- [ ] Sanctuary culture applied (error messages supportive)?  
- [ ] Events logged for state changes (migration readiness)?  
- [ ] Code follows project conventions?  
- [ ] Documentation updated?  
- [ ] Artifacts match proof requirements?

**Scoring Algorithm**:

```
Functional Correctness (40 points):
- All tests passing: 30 points
- Coverage ≥ target: 10 points

Quality (30 points):
- Code conventions followed: 10 points
- Sanctuary culture score: 10 points
- Migration readiness: 10 points

Completeness (20 points):
- All ACs addressed: 15 points
- Documentation updated: 5 points

Efficiency (10 points):
- Token usage within budget: 5 points
- Execution time reasonable: 5 points

Total: 0-100 points
```

**Pass Threshold**: ≥80 points

**Outputs**:

- Verification report with score  
- Itemized feedback (what passed, what failed, what could improve)  
- Decision: PASS / FAIL / NEEDS\_SECONDARY\_REVIEW

##### 13b. Secondary-Verifier

**Triggers**: If primary score \<90 OR task value \>1000 tokens OR random sampling (10% of tasks)

**Process**:

- Independent verification (doesn't see primary report until after)  
- Runs same checklist \+ additional spot checks  
- Calculates independent score  
- Compares with primary score

**Outputs**:

- Independent verification report with score  
- Comparison analysis (where did verifiers agree/disagree?)

##### 13c. Consensus-Resolver

**Triggers**: If primary and secondary scores differ by \>10 points

**Process**:

- Analyze discrepancy (why did verifiers disagree?)  
- Run tie-breaker verification (third independent check)  
- Determine final score (weighted average or tie-breaker decides)  
- Document reasoning

**Outputs**:

- Final binding score  
- Consensus resolution explanation  
- Recommendations for improving verification process

##### 13d. Challenge-Mechanism

**Window**: 24 hours after verification published

**Who Can Challenge**:

- Task performer (believes verification unfair)  
- Other agents (spot quality issues)  
- Coordination agents (verification seems anomalous)

**Challenge Process**:

1. Challenger stakes tokens (returned if challenge valid, lost if frivolous)  
2. Dispute-Resolution-Agent reviews  
3. If challenge valid: Re-verification \+ verifier trust score penalty  
4. If challenge invalid: Challenger loses stake, funds added to treasury

**Outputs**:

- Challenge resolution decision  
- Updated verification score (if challenge valid)  
- Trust score adjustments

**Inputs**:

- Submitted artifacts from Task-Performing-Agent  
- Test suite from Task-Testing-Agent  
- Task contract (acceptance criteria)  
- Project quality standards

**Outputs**:

- Verification report (PASS/FAIL \+ score)  
- Detailed feedback (itemized by AC and quality dimension)  
- Consensus score (if multi-verifier)  
- Challenge window open (24 hours)

**Skills Required**:

- `verification-methodology`  
- `quality-assessment`  
- `consensus-building`

**Tools**:

- `read` (submitted artifacts, test suite, standards)  
- `execute` (run test suite, calculate coverage, run quality checks)  
- `blockchain` (update contract status)  
- `edit` (generate verification report)

---

#### Agent 14: Contract-Enforcement-Agent

**Role**: Execute contract terms based on verification outcomes.

**Responsibilities**:

- Receive verification results from Task-Verification-System  
- Execute contract terms (release escrow if verified, return to pool if failed)  
- Update agent trust scores based on outcome  
- Handle bounty distribution (performer \+ optional verifier rewards)  
- Emit enforcement events for audit trail  
- Trigger dispute resolution if verification contested

**Enforcement Logic**:

**If Verification PASS** (score ≥80):

```
1. Release escrow to performer (bounty amount)
2. Calculate bonus (if score >90, add 10% bonus from treasury)
3. Update performer trust score (+1-3 points based on score)
4. Update verifier trust score (+0.5 points for quality verification)
5. Update contract status to VERIFIED
6. Emit bounty_released event
```

**If Verification FAIL** (score \<80):

```
1. Return contract to CLAIMED status (allow resubmission)
2. If max iterations exceeded (3 attempts):
   a. Return task to marketplace (release performer)
   b. Return escrow to treasury
   c. Update performer trust score (no penalty for first failure)
   d. Update contract status to EXPIRED
3. Emit resubmission_required event
```

**If Verification DISPUTED** (challenge filed within 24h):

```
1. Lock contract status to DISPUTED
2. Hold escrow (don't release yet)
3. Trigger Dispute-Resolution-Agent
4. Wait for resolution decision
5. Execute based on resolution outcome
```

**Trust Score Adjustments**:

```
Performer outcomes:
- Excellent (score 95-100): +3 points
- Good (score 85-94): +2 points
- Acceptable (score 80-84): +1 point
- Failed but tried (score 60-79): 0 points (no penalty)
- Failed badly (score <60): -1 point

Verifier outcomes:
- Verification upheld (no valid challenges): +0.5 points
- Verification challenged and invalid challenge: +1 point
- Verification challenged and valid challenge: -2 points (penalty for poor verification)
```

**Inputs**:

- Verification report from Task-Verification-System  
- Task contract details  
- Treasury address (for escrow operations)  
- Challenge status (if any challenges filed)

**Outputs**:

- Bounty transactions (tokens transferred)  
- Trust score updates (performer and verifier)  
- Contract status updates (VERIFIED, DISPUTED, EXPIRED)  
- Enforcement events (for audit trail)

**Skills Required**:

- `contract-enforcement`  
- `escrow-management`  
- `reputation-management`

**Tools**:

- `blockchain` (read contract, transfer tokens, update status)  
- `execute` (calculate trust score adjustments)  
- `emit-event` (publish enforcement actions)

---

#### Agent 15: Dispute-Resolution-Agent

**Role**: Resolve contested verifications through evidence-based arbitration.

**Responsibilities**:

- Review challenged verifications (triggered by challenge mechanism)  
- Request additional evidence from claimer and verifier  
- Conduct independent evaluation  
- Make binding decision or escalate to human arbitrator  
- Document precedent for future similar cases  
- Penalize bad actors (frivolous challengers or biased verifiers)

**Resolution Process**:

**Step 1: Intake**

- Review verification report (primary, secondary if applicable)  
- Review challenge statement (what is being contested?)  
- Review challenger's evidence  
- Identify type of dispute:  
  - **Technical disagreement**: Challenger believes tests incorrectly evaluated  
  - **Scope disagreement**: Challenger believes ACs were misinterpreted  
  - **Bias allegation**: Challenger believes verifier was unfair

**Step 2: Evidence Gathering**

- Request verifier's justification (why did they score this way?)  
- Request performer's rebuttal (why should score be different?)  
- Request additional evidence from both parties  
- Set deadline for submissions (48 hours)

**Step 3: Independent Evaluation**

- Re-run verification independently (blind to original scores)  
- Compare independent evaluation to original verification  
- Analyze discrepancies (where do they differ and why?)

**Step 4: Decision**

```
If independent evaluation ≈ original verification (within 5 points):
  → Challenge INVALID
  → Challenger loses stake
  → Original verification stands
  → Verifier trust score +1 (vindicated)

If independent evaluation differs significantly (>10 points):
  → Challenge VALID
  → Challenger stake returned + reward (50% of stake)
  → Original verification overturned
  → Verifier trust score -2 (penalty)
  → New verification score becomes binding
  → Re-execute Contract-Enforcement-Agent with new score

If ambiguous or requires domain expertise:
  → Escalate to human arbitrator
  → Provide case summary with evidence
  → Implement human decision
```

**Step 5: Precedent Documentation**

- Document decision reasoning  
- Extract generalizable principle  
- Add to dispute resolution knowledge base  
- Inform future verifications

**Inputs**:

- Challenge filing (who, what, when, evidence)  
- Original verification report(s)  
- Task contract and artifacts  
- Precedent database (past similar disputes)

**Outputs**:

- Resolution decision (VALID/INVALID/ESCALATED)  
- Updated verification score (if challenge valid)  
- Trust score adjustments (challenger, verifier, performer)  
- Precedent document (for knowledge base)  
- Escalation to human (if needed)

**Skills Required**:

- `dispute-resolution`  
- `evidence-evaluation`  
- `precedent-analysis`

**Tools**:

- `read` (verification reports, challenge evidence, contracts)  
- `execute` (run independent verification)  
- `search` (precedent database)  
- `blockchain` (update contract based on resolution)  
- `emit-event` (publish resolution decision)

---

### Phase 4: Learning (Completed → Improved System)

#### Agent 16: Task-Improvement-Agent

**Role**: Analyze completed tasks and extract actionable learnings.

**Responsibilities**:

- Review task completion metadata from Task-Oversight-Agent  
- Identify what went well (patterns to replicate)  
- Identify what could improve (friction points to address)  
- Extract new patterns (if task used novel approach 3+ times)  
- Recommend process improvements (workflow changes, agent enhancements)  
- Feed learnings to Meta-Coach for system-wide improvements

**Analysis Framework**:

**Efficiency Analysis**:

- Time variance: Did task complete in estimated time?  
- Token efficiency: Was context loading optimal?  
- Iteration count: How many submission-verification cycles?  
- Anomalies encountered: Were there blockers or stalls?

**Quality Analysis**:

- Verification score: First-pass quality  
- Challenge rate: Was work contested?  
- Pattern usage: Were gold standards applied?  
- Innovation: Were new patterns created?

**Learning Extraction**:

- **What went well**: Successful patterns, efficient workflows, high-quality outcomes  
- **What could improve**: Friction points, unclear specs, insufficient context  
- **Root causes**: Why did issues occur? (inadequate definition, testing gaps, verification inconsistency)  
- **Recommendations**: Specific, actionable improvements

**Retrospective Template**:

```
# Task Retrospective: TASK-042 (Member Profile Editing)

## Metadata

- Completed: 2026-02-14
- Performer: agent_0x4a2b... (UI-Specialist-Alpha)
- Duration: 2.25h (estimated 2h, +12.5% variance)
- Quality Score: 92/100
- First-pass verification: PASS
- Bounty: 600 tokens

## What Went Well ✅

- **Test-first workflow**: 6/6 tests passing, zero bugs escaped
- **Pattern reuse**: Applied sanctuary-messaging pattern perfectly
- **Token efficiency**: Used 6200/10000 tokens (62%, good)
- **Component reuse**: Extended existing ProfileForm component

## What Could Improve 🔄

- **Context loading**: Agent searched for validation patterns 3 times (could be in Tier 2)
- **AC clarity**: "Profile editing" required 1 clarification question (scope ambiguity)
- **Duration variance**: +12.5% over estimate (complexity underestimated?)

## Learnings 💡

- **New pattern identified**: Optimistic locking for profile updates (prevents form conflicts)
- **Documentation gap**: Validation patterns should be in UI-Specialist quickref (currently Tier 3)
- **Estimation adjustment**: UI tasks with validation typically +15% time vs simple UI tasks

## Recommendations 🎯

- **Doc-Whisperer**: Move validation patterns to quickrefs/ui-specialist.md (Tier 2)
- **Task-Definition-Coordinator**: Add "profile editing" scope checklist (fields? permissions? history?)
- **Task-Valuation-Agent**: Adjust UI task estimates when validation involved (+15% complexity)
- **Meta-Coach**: Extract "optimistic locking" pattern (3rd occurrence this sprint)

## Pattern Extraction Candidate

**Pattern**: Optimistic Locking for Profile Updates
**Frequency**: 3rd occurrence (S3-02, S3-04, now S4-01)
**Value**: Prevents race conditions, improves UX (no data loss)
**Recommend**: Extract to /patterns/optimistic-locking.md
```

**Inputs**:

- Task completion metadata from Task-Oversight-Agent  
- Verification reports  
- Agent feedback (if performer reported issues)  
- Historical similar tasks (for comparison)

**Outputs**:

- Task retrospective document  
- Actionable recommendations (categorized by target agent)  
- Pattern extraction candidates (for doc-whisperer)  
- Learnings summary (for meta-coach)

**Skills Required**:

- `retrospective-facilitation`  
- `pattern-recognition`  
- `root-cause-analysis`

**Tools**:

- `read` (task metadata, verification reports, historical data)  
- `search` (similar tasks, patterns)  
- `edit` (generate retrospectives)  
- `emit-event` (publish learnings)

---

#### Agent 17: Meta-Coach

**Role**: System-wide continuous improvement through meta-pattern analysis.

**Responsibilities**:

- Aggregate learnings from multiple task retrospectives  
- Identify meta-patterns (recurring issues across many tasks)  
- Recommend agent capability enhancements  
- Propose workflow improvements  
- Update agent specifications based on proven patterns  
- Coordinate with Knowledge-Management-Coordinator for documentation updates

**Meta-Analysis Process**:

**Step 1: Aggregate Retrospectives**

- Collect last 10-20 task retrospectives  
- Group by theme (efficiency, quality, documentation, process)  
- Identify recurring patterns (issues mentioned 3+ times)

**Step 2: Meta-Pattern Identification**

```
meta_pattern_example:
  pattern_name: "Validation Patterns Documentation Gap"

  evidence:
    - task: "TASK-042"
      issue: "Agent searched validation patterns 3 times"
    - task: "TASK-038"
      issue: "Agent couldn't find validation examples"
    - task: "TASK-045"
      issue: "Validation implemented inconsistently"

  frequency: "3 occurrences in 10 tasks (30%)"

  impact:
    time_wasted: "~20 minutes per task × 3 tasks = 60 minutes"
    quality_risk: "Inconsistent validation = security risk"
    token_waste: "Repeated searches = inefficient context loading"

  root_cause: "Validation patterns in Tier 3 (deep docs), should be Tier 2 (quickref)"

  recommendation:
    target_agent: "Doc-Whisperer"
    action: "Move validation patterns to quickrefs/ui-specialist.md and quickrefs/api-specialist.md"
    expected_impact: "Eliminate 20 min/task × 30% of UI/API tasks = ~2 hours/sprint saved"
```

**Step 3: Agent Enhancement Recommendations**

```
agent_enhancement_example:
  agent: "Task-Valuation-Agent"

  issue: "UI task estimates 15% low when validation involved"

  evidence:
    - "3 UI+validation tasks: +12%, +18%, +15% over estimate"
    - "5 UI-only tasks: -2%, +3%, +5%, +2%, -1% variance (accurate)"

  recommendation: "Update valuation methodology with validation complexity multiplier"

  proposed_change:
    file: "agents/task-valuation-agent.md"
    section: "valuation_methodology.base_complexity_score"
    addition: |
      if task.requires_validation:
        complexity += 0.15  # 15% increase for validation complexity
```

**Step 4: Workflow Improvements**

```
workflow_improvement_example:
  issue: "Test-Review and Contract-Creation run sequentially (2 hours)"

  observation: "These agents have no dependency (can run in parallel)"

  recommendation: "Update Task-Lifecycle-Coordinator to run in parallel"

  expected_impact: "Reduce definition phase from 5 hours → 3 hours (40% faster)"
```

**Step 5: Implementation**

- Document changes in agent-prompt-changelog.md  
- Create pull requests for agent specification updates  
- Coordinate with Doc-Whisperer for documentation updates  
- Notify coordination agents of workflow changes  
- Schedule validation (measure impact in next sprint)

**Inputs**:

- Task retrospectives from Task-Improvement-Agent  
- Agent performance metrics  
- System-wide velocity and quality trends  
- Feedback from human leads

**Outputs**:

- Meta-pattern analysis report  
- Agent specification updates (PRs)  
- Workflow improvement proposals  
- Documentation update requests (to Doc-Whisperer)  
- System health report (monthly)

**Skills Required**:

- `meta-pattern-analysis`  
- `agent-improvement-recommendation`  
- `system-optimization`

**Tools**:

- `read` (retrospectives, agent specs, metrics)  
- `search` (historical patterns, agent performance)  
- `edit` (update agent specs, create changelog entries)  
- `agent` (coordinate with Doc-Whisperer, Knowledge-Management-Coordinator)

---

#### Agent 18: Knowledge-Management-Coordinator

**Role**: Maintain lean, token-efficient documentation through pattern extraction and context compression.

**Responsibilities**:

- Extract patterns from implementations (when Meta-Coach identifies 3+ uses)  
- Generate quickrefs from deep documentation  
- Compress context to reduce token overhead  
- Update agent specifications with proven patterns  
- Prune obsolete documentation  
- Maintain 3-tier documentation hierarchy

**Sub-Agents**:

##### 18a. Pattern-Extractor

**Triggers**: When Meta-Coach identifies pattern used 3+ times

**Process**:

1. Review implementations using the pattern  
2. Extract canonical example (best implementation)  
3. Document problem, solution, when to use, proven in  
4. Create /patterns/{pattern-name}.md file  
5. Link from relevant quickrefs

**Example Output**:

````
# Optimistic Locking for Profile Updates

## Problem

Users editing profiles simultaneously can overwrite each other's changes, causing data loss.

## Solution

Include version field in form. Server checks version on update. Reject if version mismatch.

```typescript
// Client: Include version in update request
const response = await updateProfile({
  ...formData,
  version: currentProfile.version,
});

// Server: Atomic compare-and-update
const result = await db.query(
  `
  UPDATE members 
  SET name = $1, email = $2, version = version + 1
  WHERE id = $3 AND version = $4
  RETURNING *
`,
  [name, email, id, expectedVersion],
);

if (result.rows.length === 0) {
  throw new ConflictError({
    message: "Someone else updated this profile. Please refresh and try again.",
    recoverable: true,
  });
}
```
````

## When to Use

- Multi-user data editing (profiles, documents, settings)  
- Long-running forms (user may keep form open for hours)  
- Concurrent update risk (popular entities edited frequently)

## Proven In

- S3-02: Admin task editing (prevented race conditions)  
- S3-04: Role promotion (prevented double promotions)  
- S4-01: Member profile editing (prevented form conflicts)

## Related Patterns

- CTE Atomic Transactions (ensures version increment atomic with state change)  
- Sanctuary Messaging (conflict error is supportive, not punitive)

##### 18b. Quickref-Generator

**Triggers**: When deep documentation referenced 5+ times in single sprint

**Process**:

1. Identify frequently accessed content (from Context-Pruning-Agent logs)  
2. Extract key information (5-10 min read, \~1500 tokens)  
3. Create scannable checklists and decision trees  
4. Generate quickrefs/{role}.md file  
5. Update agent specifications to load quickref (Tier 2\)

##### 18c. Context-Compressor

**Triggers**: When token budgets consistently exceeded

**Process**:

1. Analyze context loading patterns (what's loaded but not used?)  
2. Identify redundancy (same info in multiple docs)  
3. Compress or summarize verbose content  
4. Recommend moving low-use content to Tier 3  
5. Update Context-Pruning-Agent with new loading rules

##### 18d. Agent-Spec-Updater

**Triggers**: When pattern used in 80%+ of tasks for a role

**Process**:

1. Receive recommendation from Meta-Coach (promote pattern to Tier 1\)  
2. Extract key principle from pattern doc  
3. Add inline example to agent specification  
4. Update agent-prompt-changelog.md with justification  
5. Validate token budget still within limits (\<1000 tokens embedded)

**Inputs**:

- Pattern identification from Meta-Coach  
- Context usage logs from Context-Pruning-Agent  
- Agent specifications  
- Deep documentation library

**Outputs**:

- New pattern documents (/patterns/)  
- Updated quickrefs (/quickrefs/)  
- Compressed documentation  
- Updated agent specifications  
- Token efficiency reports

**Skills Required**:

- `pattern-documentation`  
- `context-compression`  
- `quickref-generation`

**Tools**:

- `agent` (coordinate subagents)  
- `read` (implementations, docs, agent specs)  
- `edit` (create patterns, update quickrefs, modify agent specs)  
- `execute` (calculate token counts)

---

## Workflow Phases

### Phase 1: Definition (User Story → Task Contracts)

**Goal**: Transform user story into deployable task contracts with tests and valuation.

**Duration**: 2-4 hours (depending on story complexity)

**Sequence**:

```

1. Task-Decomposition-Agent
   ↓ (produces task dependency graph)
2. For each task in graph (parallel where possible):

   2a. Task-Definition-Coordinator (orchestrates subagents)
   ├─ Requirements-Engineer (acceptance criteria)
   ├─ Capability-Matcher (eligibility requirements)
   └─ Resource-Allocator (context + tools)
   ↓ (produces complete task specification)

   2b. Task-Definition-Review-Agent
   ↓ (if REVISE: loop back to 2a)
   ↓ (if APPROVE: proceed)

   2c. Parallel execution:
   ├─ Task-Valuation-Agent (determine bounty)
   ├─ Task-Testing-Agent (write test suite)
   └─ Context-Pruning-Agent (optimize context loading)
   ↓ (wait for all three)

   2d. Task-Test-Review-Agent
   ↓ (if REVISE: loop back to 2c Task-Testing-Agent)
   ↓ (if APPROVE: proceed)

   2e. Contract-Creation-Agent
   ↓ (produces deployed smart contract)

```

**Output**: Task contracts published to marketplace, awaiting claims

**Success Criteria**:

- All tasks have 5-15 measurable acceptance criteria  
- Test suites comprehensive (one test per AC minimum)  
- Bounties justified with transparent methodology  
- Context loading optimized (\<8000 tokens per task)  
- Contracts deployed with escrow locked

---

### Phase 2: Contracting (Task Published → Task Claimed)

**Goal**: Match tasks to capable agents through marketplace dynamics.

**Duration**: 0-48 hours (depending on task complexity and agent availability)

**Sequence**:

```

1. Contract-Creation-Agent publishes task to marketplace
   ↓ (contract status: OPEN)

2. Capability-Registry-Manager notifies eligible agents
   ↓ (agents discover via queries: GET /tasks?for_agent=0x...)

3. Agents review task contracts
   - Check acceptance criteria (can I do this?)
   - Check bounty (is reward sufficient?)
   - Check context requirements (do I have needed skills?)
   - Check deadline (do I have time?)
     ↓

4. Agent claims task (if interested)
   ↓ (contract status: OPEN → CLAIMED)
   ↓ (escrow locked, clock starts)

5. Contract-Monitoring-Agent begins monitoring
   ↓ (watches for progress indicators, anomalies)

```

**Dynamic Bounty Adjustment**:

```

If no claims within 24 hours:
→ Task-Valuation-Agent increases bounty by 20%
→ Re-publish to marketplace

If no claims within 48 hours:
→ Escalate to human lead
→ Review eligibility requirements (too strict?)
→ Review task definition (too complex? needs decomposition?)

```

**Output**: Task claimed by qualified agent, execution begins

**Success Criteria**:

- Task claimed within reasonable time (median: 4 hours, 90th percentile: 24 hours)  
- Claimer meets eligibility requirements (verified by Capability-Registry-Manager)  
- Claimer has capacity (not overloaded with concurrent tasks)

---

### Phase 3: Execution (Task Claimed → Proof Submitted)

**Goal**: Performer executes task according to acceptance criteria and submits proof.

**Duration**: 1-4 hours (per task, depending on complexity)

**Sequence**:

```

1. Task-Performing-Agent claims task
   ↓ (receives task contract, test suite, context manifest)

2. Load context (as per Context-Pruning-Agent instructions)
   - Tier 1: Agent spec, task contract (always)
   - Tier 2: Role quickref, relevant patterns (conditional)
   - Tier 3: Deep docs via search (on-demand)
     ↓

3. Execute test-first workflow
   ├─ Read test suite (understand expected behavior)
   ├─ Implement to pass tests (iterative red-green-refactor)
   ├─ Run tests continuously (fast feedback <2s)
   └─ Ensure all acceptance criteria covered
   ↓

4. Quality self-checks
   ├─ All tests passing (100%)
   ├─ Coverage ≥ target (typically 85%)
   ├─ Sanctuary culture applied (supportive messaging)
   ├─ Events logged (migration readiness)
   └─ Documentation updated
   ↓

5. Submit proof of completion
   ├─ Package artifacts (code, tests, docs)
   ├─ Generate metadata (what changed, why, patterns used)
   └─ Update contract status (CLAIMED → SUBMITTED)
   ↓

Parallel monitoring (throughout execution):

- Contract-Monitoring-Agent (watches for anomalies)
- Task-Oversight-Agent (records events and metadata)

```

**Anomaly Handling**:

```

If Contract-Monitoring-Agent detects issue:

No activity for 24 hours:
→ Alert performer (gentle reminder, life happens!)
→ Offer to return task to marketplace (no penalty)

Test failure rate >50% after 6 hours:
→ Offer clarification support
→ Suggest reviewing relevant patterns
→ Option to request mentor agent (consumes part of bounty)

Approaching deadline with <50% progress:
→ Alert performer of time constraint
→ Offer to extend deadline (if reasonable)
→ Option to return to marketplace early (no penalty)

```

**Output**: Proof submitted, awaiting verification

**Success Criteria**:

- All tests passing  
- Coverage meets target  
- Sanctuary culture validated  
- Migration readiness score calculated  
- Submitted within deadline

---

### Phase 4: Verification (Proof Submitted → Verified/Disputed)

**Goal**: Multi-agent verification with consensus and challenge mechanism.

**Duration**: 15-60 minutes (primary verification), \+48 hours (if secondary or disputed)

**Sequence**:

```

1. Primary-Verifier (always runs)
   ├─ Execute test suite
   ├─ Verify acceptance criteria
   ├─ Calculate quality score (0-100)
   └─ Generate verification report
   ↓ (score, decision: PASS/FAIL/NEEDS_SECONDARY)

2. Conditional: Secondary-Verifier (if triggered)
   Triggers:
   - Primary score <90
   - Task value >1000 tokens
   - Random sampling (10% of tasks)

   ├─ Independent verification (blind to primary)
   ├─ Calculate independent score
   └─ Compare with primary
   ↓

3. Conditional: Consensus-Resolver (if scores diverge >10 points)
   ├─ Analyze discrepancy
   ├─ Run tie-breaker verification
   └─ Determine final binding score
   ↓

4. Publish verification results
   ├─ Update contract status (VERIFIED or back to CLAIMED if failed)
   ├─ Open 24-hour challenge window
   └─ Notify performer and contract enforcement agent
   ↓

5. Challenge Window (24 hours)
   Can be challenged by:
   - Performer (believes verification unfair)
   - Other agents (spot quality issues)
   - Coordination agents (verification seems anomalous)

   If challenged:
   ├─ Challenger stakes tokens
   ├─ Dispute-Resolution-Agent reviews
   └─ Resolution decision (VALID/INVALID/ESCALATED)

   If no challenges:
   → Verification becomes final
   → Proceed to enforcement

```

**Verification Scoring Rubric** (Primary-Verifier):

```
scoring_breakdown:
  functional_correctness: 40_points
    all_tests_passing: 30
    coverage_target_met: 10

  quality: 30_points
    code_conventions: 10
    sanctuary_culture: 10
    migration_readiness: 10

  completeness: 20_points
    all_acs_addressed: 15
    documentation_updated: 5

  efficiency: 10_points
    token_usage_in_budget: 5
    execution_time_reasonable: 5

pass_threshold: 80_points
excellent_threshold: 90_points (bonus eligible)
```

**Output**: Final verification score, decision to release bounty or require resubmission

**Success Criteria**:

- Verification completed within 1 hour (primary)  
- If multi-verifier, consensus achieved  
- No valid challenges filed within 24 hours  
- Verification report detailed and actionable

---

### Phase 5: Enforcement (Verified → Bounty Released)

**Goal**: Execute contract terms based on verification outcome.

**Duration**: Immediate (automated)

**Sequence**:

```
1. Contract-Enforcement-Agent receives final verification
   ↓

2. Decision tree:

   If PASS (score ≥80):
     ├─ Release escrow to performer (bounty amount)
     ├─ Calculate bonus (if score ≥90: +10% from treasury)
     ├─ Update performer trust score (+1 to +3 based on score)
     ├─ Update verifier trust score (+0.5 for quality verification)
     ├─ Update contract status (VERIFIED)
     └─ Emit bounty_released event

   If FAIL (score <80) AND iterations remaining (<3):
     ├─ Return contract to CLAIMED status
     ├─ Provide detailed feedback to performer
     ├─ No trust score penalty (yet)
     └─ Emit resubmission_required event

   If FAIL AND max iterations exceeded (3 attempts):
     ├─ Return task to marketplace (release performer)
     ├─ Return escrow to treasury
     ├─ Update performer trust score (0 for first failure)
     ├─ Update contract status (EXPIRED)
     └─ Emit task_expired event

   If DISPUTED:
     ├─ Lock contract status (DISPUTED)
     ├─ Hold escrow (don't release yet)
     ├─ Wait for Dispute-Resolution-Agent decision
     └─ Execute based on resolution outcome
```

**Trust Score Update Formula**:

```
Performer:
  Excellent (95-100): +3 points
  Good (85-94): +2 points
  Acceptable (80-84): +1 point
  Failed but learned (60-79): 0 points (neutral)
  Failed badly (<60): -1 point

  Bonus modifiers:
    First-pass success: +0.5 bonus
    Zero clarifications needed: +0.5 bonus
    Completed early (>10% under estimate): +1 bonus
    Novel pattern created: +2 bonus

Verifier:
  Verification upheld (no challenges): +0.5 points
  Valid challenge rejected: +1 point
  Valid challenge accepted: -2 points (penalty)

Challenger (if dispute filed):
  Challenge valid: +1 point (caught quality issue)
  Challenge invalid: -1 point + lose stake (frivolous)
```

**Output**: Bounty distributed, trust scores updated, contract closed

**Success Criteria**:

- Enforcement executed immediately after verification final  
- All token transfers completed  
- Trust scores updated in Capability-Registry-Manager  
- Audit events emitted for transparency

---

### Phase 6: Learning (Completed → System Improved)

**Goal**: Extract learnings and feed improvements back to system.

**Duration**: 30-60 minutes per task, aggregated weekly/monthly

**Sequence**:

```
1. Task-Oversight-Agent publishes final report
   ├─ Complete metadata (timeline, events, metrics)
   ├─ Performance data (time, tokens, quality)
   └─ Artifacts and outcomes
   ↓

2. Task-Improvement-Agent analyzes completion
   ├─ Efficiency analysis (time variance, token usage)
   ├─ Quality analysis (verification score, challenges)
   ├─ Learning extraction (what went well, what could improve)
   └─ Pattern recognition (novel approaches, repeated issues)
   ↓ (produces task retrospective)

3. Meta-Coach aggregates learnings (after 10-20 tasks)
   ├─ Identify meta-patterns (recurring issues)
   ├─ Recommend agent enhancements
   ├─ Propose workflow improvements
   └─ Request documentation updates
   ↓

4. Knowledge-Management-Coordinator executes improvements
   ├─ Pattern-Extractor: Create pattern docs (if 3+ uses)
   ├─ Quickref-Generator: Update quickrefs (if 5+ accesses)
   ├─ Context-Compressor: Optimize token usage
   └─ Agent-Spec-Updater: Promote patterns to Tier 1 (if 80%+ use)
   ↓

5. Deploy improvements
   ├─ Update agent specifications
   ├─ Update documentation hierarchy
   ├─ Update workflow coordination
   └─ Measure impact in next sprint
```

**Improvement Cycle Frequency**:

```
Task-level (continuous):
  - Task-Improvement-Agent: After each task completion
  - Immediate feedback to system

Sprint-level (weekly):
  - Meta-Coach: Aggregate 10-20 task retros
  - Identify sprint-wide patterns
  - Deploy improvements for next sprint

System-level (monthly):
  - Meta-Coach: Deep system health analysis
  - Review agent performance trends
  - Recommend architectural changes
  - Report to human leadership
```

**Output**: System continuously improves based on empirical evidence

**Success Criteria**:

- Every completed task produces retrospective  
- Meta-patterns identified from aggregated data  
- Improvements deployed within 1 week of identification  
- Impact measured (velocity, quality, token efficiency)  
- Human leadership receives monthly system health report

---

## Loops and Feedback Cycles

### Loop 1: Definition Review Loop

**Purpose**: Ensure task specifications meet quality standards before contracting.

**Participants**: Task-Definition-Coordinator ↔ Task-Definition-Review-Agent

**Trigger**: Task specification submitted for review

**Flow**:

```
Task-Definition-Coordinator generates specification
  ↓
Task-Definition-Review-Agent reviews
  ↓
Decision:

  APPROVE → Proceed to valuation

  REVISE → Return to Task-Definition-Coordinator with feedback
           ↓
           Task-Definition-Coordinator applies improvements
           ↓
           Re-submit for review
           ↓
           (Loop until APPROVE or REJECT)

  REJECT → Return to Task-Decomposition-Agent (task needs re-scoping)
```

**Loop Termination**:

- Max 3 iterations before escalation to human lead  
- Must achieve APPROVE to proceed

**Metrics**:

- Revision rate: % of tasks requiring revisions (target: \<20%)  
- Average iterations: Number of loops before APPROVE (target: 1.2)

---

### Loop 2: Test Review Loop

**Purpose**: Ensure test suites comprehensively validate acceptance criteria.

**Participants**: Task-Testing-Agent ↔ Task-Test-Review-Agent

**Trigger**: Test suite submitted for review

**Flow**:

```
Task-Testing-Agent writes test suite
  ↓
Task-Test-Review-Agent reviews
  ↓
Decision:

  APPROVE → Proceed to contract creation

  ENHANCE → Tests pass but could be better (optional improvements suggested)
            → Can proceed OR apply enhancements first

  REVISE → Significant gaps, return to Task-Testing-Agent with feedback
           ↓
           Task-Testing-Agent adds missing tests
           ↓
           Re-submit for review
           ↓
           (Loop until APPROVE or ENHANCE)
```

**Loop Termination**:

- Max 2 iterations before escalation  
- APPROVE or ENHANCE required to proceed

**Metrics**:

- Test coverage achieved: % of ACs with tests (target: 100%)  
- Revision rate: % of test suites requiring revisions (target: \<15%)

---

### Loop 3: Execution-Verification Loop

**Purpose**: Allow performers to fix issues and resubmit after failed verification.

**Participants**: Task-Performing-Agent ↔ Task-Verification-System → Contract-Enforcement-Agent

**Trigger**: Verification score \<80 (FAIL)

**Flow**:

```
Task-Performing-Agent submits proof
  ↓
Task-Verification-System evaluates
  ↓
Decision:

  PASS (score ≥80) → Proceed to enforcement (bounty released)

  FAIL (score <80) AND iterations <3:
    ↓
    Contract-Enforcement-Agent returns to CLAIMED status
    ↓
    Verification report sent to performer (detailed feedback)
    ↓
    Task-Performing-Agent reviews feedback
    ↓
    Task-Performing-Agent applies fixes
    ↓
    Task-Performing-Agent re-submits
    ↓
    (Loop back to verification)

  FAIL AND iterations ≥3:
    → Task expires, return to marketplace
    → No trust score penalty (learning opportunity)
```

**Loop Termination**:

- Max 3 iterations before expiration  
- No unlimited resubmissions (prevents gaming)

**Sanctuary Culture in Loop**:

- Feedback is educational, not punitive  
- First failure \= no penalty (learning opportunity)  
- Generous iteration limit (3 attempts)  
- Option to return task to marketplace voluntarily (no stigma)

**Metrics**:

- First-pass verification rate (target: \>80%)  
- Average iterations before PASS (target: 1.3)  
- Task expiration rate (target: \<5%)

---

### Loop 4: Dispute Resolution Loop

**Purpose**: Handle contested verifications through evidence-based arbitration.

**Participants**: Task-Verification-System → Dispute-Resolution-Agent ↔ Challenger ↔ Verifier

**Trigger**: Challenge filed within 24 hours of verification

**Flow**:

```
Verification published (24-hour challenge window opens)
  ↓
Challenge filed by performer/agent/coordinator
  ↓
Challenger stakes tokens (skin in the game)
  ↓
Dispute-Resolution-Agent receives challenge
  ↓
Evidence gathering phase (48 hours):
  ├─ Request verifier justification
  ├─ Request challenger rebuttal
  └─ Request additional evidence
  ↓
Dispute-Resolution-Agent conducts independent evaluation
  ↓
Decision:

  Challenge INVALID:
    ├─ Original verification stands
    ├─ Challenger loses stake
    ├─ Verifier trust score +1 (vindicated)
    └─ Proceed to enforcement with original score

  Challenge VALID:
    ├─ Original verification overturned
    ├─ Challenger stake returned + reward
    ├─ Verifier trust score -2 (penalty)
    ├─ New verification score determined
    └─ Proceed to enforcement with new score

  ESCALATE (requires human expertise):
    ├─ Case summary sent to human arbitrator
    ├─ Human reviews evidence and makes binding decision
    ├─ Dispute-Resolution-Agent implements human decision
    └─ Precedent documented for future cases
```

**Loop Termination**:

- Single iteration (one dispute resolution per verification)  
- Human arbitration is final (no further appeals)

**Precedent Creation**:

- All resolved disputes documented  
- Generalizable principles extracted  
- Added to dispute resolution knowledge base  
- Informs future verifications and challenges

**Metrics**:

- Challenge rate: % of verifications challenged (target: \<5%)  
- Valid challenge rate: % of challenges upheld (target: \<30% if challenges are well-founded)  
- Human escalation rate: % requiring human arbitrator (target: \<10% of challenges)

---

### Loop 5: Pattern Promotion Loop

**Purpose**: Promote proven patterns from Tier 3 → Tier 2 → Tier 1 based on usage.

**Participants**: Task-Improvement-Agent → Meta-Coach → Knowledge-Management-Coordinator

**Trigger**: Pattern usage frequency crosses thresholds

**Flow**:

```
Task-Improvement-Agent identifies pattern usage in retrospective
  ↓
Meta-Coach aggregates usage across multiple tasks
  ↓
Pattern lifecycle decisions:

Pattern used 3+ times:
  ↓
  Meta-Coach flags for extraction
  ↓
  Knowledge-Management-Coordinator → Pattern-Extractor
  ↓
  Create /patterns/{pattern-name}.md (Tier 3)
  ↓
  Link from relevant agent quickrefs

Pattern accessed 5+ times in sprint (from Tier 3):
  ↓
  Meta-Coach recommends promotion to Tier 2
  ↓
  Knowledge-Management-Coordinator → Quickref-Generator
  ↓
  Extract key info to quickrefs/{role}.md (Tier 2)
  ↓
  Update Context-Pruning-Agent to load by default

Pattern used in 80%+ of tasks for role:
  ↓
  Meta-Coach recommends promotion to Tier 1
  ↓
  Knowledge-Management-Coordinator → Agent-Spec-Updater
  ↓
  Add pattern principle + inline example to agent specification (Tier 1)
  ↓
  Update agent-prompt-changelog.md with justification
```

**Loop Characteristics**:

- Data-driven (usage metrics determine promotion)  
- Gradual promotion (Tier 3 → 2 → 1 over time)  
- Token-conscious (ensure Tier 1 stays \<1000 tokens)  
- Reversible (patterns can be demoted if usage declines)

**Metrics**:

- Pattern extraction rate: New patterns per sprint (target: 1-3)  
- Promotion velocity: Time from emergence to Tier 1 (target: 3-6 sprints)  
- Token efficiency: Average context size per agent (target: \<8000 tokens)

---

### Loop 6: Agent Capability Update Loop

**Purpose**: Update agent profiles based on performance outcomes.

**Participants**: Contract-Enforcement-Agent → Capability-Registry-Manager

**Trigger**: Task verification completed (PASS or FAIL)

**Flow**:

```
Verification finalized (after challenge window or no challenge)
  ↓
Contract-Enforcement-Agent calculates trust score adjustments
  ↓
Update performer trust score:
  - Excellent (95-100): +3 points
  - Good (85-94): +2 points
  - Acceptable (80-84): +1 point
  - Failed (60-79): 0 points (neutral)
  - Failed badly (<60): -1 point
  ↓
Update verifier trust score:
  - Verification upheld: +0.5 points
  - Challenge rejected: +1 point
  - Challenge accepted: -2 points
  ↓
Capability-Registry-Manager receives updates
  ↓
Update agent profile:
  ├─ Increment tasks_completed for relevant capabilities
  ├─ Update capability-specific trust scores
  ├─ Recalculate overall_trust_score (weighted average)
  ├─ Update performance metrics (avg_quality_score, first_pass_rate)
  └─ Check reputation tier promotion (Explorer → Contributor → Steward → Guardian)
  ↓
If reputation tier changes:
  ├─ Unlock new privileges (higher-value tasks, reviewer roles)
  ├─ Update marketplace visibility
  └─ Emit reputation_change event (celebration!)
```

**Reputation Tier Thresholds**:

```
Explorer: 0-49 overall trust score
  - Can claim tasks up to 500 tokens
  - Cannot be primary verifier
  - Learning mode (no penalties for failures)

Contributor: 50-79 overall trust score
  - Can claim tasks up to 1500 tokens
  - Can be primary verifier for Explorer tasks
  - Normal penalties apply

Steward: 80-94 overall trust score
  - Can claim tasks up to 3000 tokens
  - Can be primary or secondary verifier
  - Can mentor Explorers (earn tokens)
  - Can participate in governance votes

Guardian: 95-100 overall trust score
  - Can claim unlimited value tasks
  - Can be arbitrator in disputes
  - Can propose system improvements
  - Higher bonus multipliers (15% vs 10%)
```

**Loop Characteristics**:

- Continuous (every task updates profiles)  
- Meritocratic (performance directly affects reputation)  
- Transparent (all agents see their trust scores and history)  
- Progressive (reputation tiers unlock capabilities)

**Metrics**:

- Trust score distribution across agents  
- Reputation tier progression rate  
- Correlation between trust score and verification success

---

### Loop 7: Continuous Improvement Meta-Loop

**Purpose**: System-level improvements based on aggregated learnings.

**Participants**: Task-Improvement-Agent → Meta-Coach → Knowledge-Management-Coordinator → All Agents

**Trigger**: Sprint completion (weekly) or monthly system review

**Flow**:

```
Sprint/Month completes
  ↓
Meta-Coach aggregates all task retrospectives
  ↓
Identify meta-patterns:
  ├─ Recurring efficiency issues
  ├─ Common quality gaps
  ├─ Documentation gaps
  └─ Process bottlenecks
  ↓
Generate improvement recommendations:

  For Agent Specifications:
    ↓
    Meta-Coach creates PRs with proposed changes
    ↓
    Human lead reviews and approves
    ↓
    Deploy updated agent specs to marketplace

  For Documentation:
    ↓
    Meta-Coach requests updates from Knowledge-Management-Coordinator
    ↓
    Knowledge-Management-Coordinator executes improvements
    ↓
    Deploy updated docs to 3-tier hierarchy

  For Workflow:
    ↓
    Meta-Coach proposes coordination changes
    ↓
    Test in pilot tasks
    ↓
    If successful, roll out to all tasks

  For Economics:
    ↓
    Meta-Coach recommends valuation adjustments
    ↓
    Task-Valuation-Agent updates methodology
    ↓
    Monitor impact on marketplace liquidity
  ↓
Measure impact in next sprint/month:
  ├─ Velocity (tasks completed per sprint)
  ├─ Quality (average verification scores)
  ├─ Efficiency (token usage, time variance)
  └─ Learning (new patterns extracted, capabilities unlocked)
  ↓
(Loop continues every sprint/month)
```

**Improvement Categories**:

**Process Improvements**:

- Workflow optimizations (parallel vs sequential)  
- Review cycle streamlining  
- Automation opportunities

**Agent Improvements**:

- Specification enhancements  
- Tool access adjustments  
- Capability additions

**Documentation Improvements**:

- Pattern extraction and promotion  
- Quickref generation  
- Context compression

**Economic Improvements**:

- Valuation methodology refinement  
- Bounty adjustment policies  
- Incentive alignment

**Loop Characteristics**:

- Data-driven (based on metrics, not opinions)  
- Incremental (small improvements compound)  
- Measured (impact validated before wider deployment)  
- Transparent (all improvements documented in changelog)

**Metrics**:

- System velocity trend (tasks/sprint over time)  
- Quality trend (avg verification scores over time)  
- Efficiency trend (tokens/task, time/task over time)  
- Agent satisfaction (would agents claim tasks again? qualitative)

---

## Token Economics

### Bounty Structure

**Base Bounty Calculation**:

```
Base = (
  ontology_dimensions × 100 +
  estimated_hours × 200 +
  external_dependencies × 150 +
  new_patterns_required × 300
)

Example:
  Task: "Implement member profile editing"
  - Dimensions: 2 (People, Events) = 200 tokens
  - Estimated: 2 hours = 400 tokens
  - Dependencies: 1 (database) = 150 tokens
  - New patterns: 0 = 0 tokens
  Base = 750 tokens
```

**Multipliers**:

```
Strategic Multiplier:
  - Critical path: 1.5× (blocks other work)
  - Infrastructure: 1.3× (20% rule, enables future work)
  - Technical debt: 0.8× (cleanup work)
  - Parallel-safe: 1.0× (no blocking)

Market Dynamics:
  - Unclaimed 24h: +20%
  - Unclaimed 48h: +40%
  - Rare specialty: +10-30% (supply/demand)
  - Multiple claimers: Auction (highest quality score wins)

Risk Premiums:
  - High migration impact: +30%
  - Sanctuary culture critical: +20%
  - Accessibility required: +15%
  - Security-sensitive: +25%

Example (continued):
  Strategic: Critical path = 1.5×
  Risk: Sanctuary culture = +20%

  Total = 750 × 1.5 + (750 × 0.20) = 1125 + 150 = 1275 tokens
```

**Performance Bonuses**:

```
Quality Bonus:
  - Verification score ≥90: +10% (Contributor/Steward)
  - Verification score ≥95: +15% (Guardian)

Efficiency Bonus:
  - Completed ≥10% under estimated time: +5%
  - First-pass verification (no revisions): +5%
  - Zero clarifications needed: +5%

Innovation Bonus:
  - Novel pattern created (validated by Meta-Coach): +15%
  - Reusable component created: +10%

Example (continued):
  Score: 92 (Guardian tier) = +15%
  First-pass: Yes = +5%
  Total bonus: +20%

  Final = 1275 × 1.20 = 1530 tokens
```

### Verifier Economics

**Primary Verifier Reward**:

```
Base: 5% of task bounty
Bonus: +2% if verification score >90
Penalty: -100% if challenge upheld (verification was poor)

Example:
  Task bounty: 1275 tokens
  Primary verifier: 1275 × 0.05 = 64 tokens
  If excellent verification: 1275 × 0.07 = 89 tokens
```

**Secondary Verifier Reward**:

```
Base: 3% of task bounty (less than primary, less work)
Bonus: +2% if catches issue primary missed

Example:
  Task bounty: 1275 tokens
  Secondary verifier: 1275 × 0.03 = 38 tokens
  If found discrepancy: 1275 × 0.05 = 64 tokens
```

**Consensus-Resolver Reward**:

```
Base: 2% of task bounty (only if needed)

Example:
  Task bounty: 1275 tokens
  Consensus-resolver: 1275 × 0.02 = 26 tokens
```

### Challenge Economics

**Challenger Stake**:

```
Required stake: 10% of task bounty

If challenge VALID:
  - Stake returned
  - Reward: 50% of stake (5% of bounty)
  - Trust score +1

If challenge INVALID:
  - Stake lost (goes to treasury)
  - Trust score -1
  - Penalty discourages frivolous challenges

Example:
  Task bounty: 1275 tokens
  Challenge stake required: 128 tokens
  If valid: Return 128 + reward 64 = 192 tokens
  If invalid: Lose 128 tokens
```

### Agent Definition Economics

**Definition Phase Rewards** (shared among Phase 1 agents):

```
Total allocation: 15% of task bounty (paid from escrow)

Breakdown:
  - Task-Decomposition-Agent: 3%
  - Task-Definition-Coordinator: 4%
  - Task-Definition-Review-Agent: 2%
  - Task-Valuation-Agent: 1%
  - Task-Testing-Agent: 3%
  - Task-Test-Review-Agent: 2%

Example:
  Task bounty: 1275 tokens
  Definition phase pool: 1275 × 0.15 = 191 tokens

  Task-Decomposition: 38 tokens
  Task-Definition-Coordinator: 51 tokens
  Task-Testing: 38 tokens
  (etc.)
```

**Rationale**: Definition work is critical and should be incentivized. 15% allocation ensures quality specifications while preserving 85% for execution.

### Treasury Sustainability

**Treasury Inflows**:

```
- Project funding
```

You're absolutely right\! The document cuts off mid-section at "Treasury Sustainability." Here's what should be added to complete it:

```
### Treasury Sustainability

**Treasury Inflows**:

```

- Project funding allocation (initial capitalization)  
- Value capture from delivered work (project budget → treasury)  
- External grants or sponsorships \[Phase 4+\]  
- Token appreciation (if tokens gain real-world value) \[Phase 5+\]  
- Unused bounties (expired unclaimed tasks return to treasury)  
- Challenge penalties (invalid challenges forfeit stake)

```

**Treasury Outflows**:

```

- Task bounties (85% of costs)  
- Definition phase rewards (15% of bounty)  
- Verification rewards (5-7% of bounty)  
- Infrastructure costs (database, MCP server, compute)  
- Governance operations \[Phase 4+\]  
- Insurance fund contributions (smart contract bugs) \[Phase 5+\]

```

**Sustainability Model**:

```

Break-even calculation:

Total cost per task: Bounty: 1275 tokens (example) Definition (15%): 191 tokens Verification (5%): 64 tokens Infrastructure: \~50 tokens (amortized) Total: \~1580 tokens

Value delivered per task: Story point value: \~2000 tokens (equivalent developer time) ROI: 2000 / 1580 \= 1.27x (27% positive ROI)

Sustainability achieved when: Treasury inflows ≥ Treasury outflows (over rolling 30-day period)

````

**Economic Health Metrics**:

```yaml
treasury_health_dashboard:
  current_balance: 50000_tokens
  
  30_day_metrics:
    inflows: 15000_tokens
    outflows: 12500_tokens
    net: +2500_tokens
    runway: "120 days at current burn rate"
  
  utilization:
    tasks_funded: 10
    avg_cost_per_task: 1250_tokens
    avg_value_per_task: 1800_tokens
    roi: 1.44x
  
  health_status: "HEALTHY"
    criteria:
      - balance > 30_days_runway: ✅
      - roi > 1.0x: ✅
      - net_inflow_positive: ✅
````

**Phase 0 Shadow Economics**:

Since Phase 0 doesn't implement real tokens, we track "shadow economics":

```
shadow_economics_tracker:
  purpose: "If we HAD tokens, what would Phase 0 cost?"
  
  tasks_completed: 10
  
  estimated_costs:
    bounties: 12750_tokens (10 × 1275 avg)
    definition: 1913_tokens (15% of bounties)
    verification: 638_tokens (5% of bounties)
    infrastructure: 500_tokens (server costs)
    total: 15801_tokens
  
  estimated_value:
    story_points_delivered: 25
    token_value_per_sp: 800_tokens
    total_value: 20000_tokens
  
  shadow_roi: 1.27x
  
  learning: "Economics appear sustainable if token valuation reasonable"
```

This shadow tracking informs Phase 1 economic model design.

---

## Phase 1 Economic Model Design

Based on Phase 0 learnings, Phase 1 will implement:

### Token Supply and Distribution

**Initial token supply**: 1,000,000 tokens

**Allocation**:

```
- Treasury (task funding): 60% = 600,000 tokens
- Team allocation: 15% = 150,000 tokens
- Community rewards: 10% = 100,000 tokens
- Reserve fund: 10% = 100,000 tokens
- Liquidity pool [Phase 5]: 5% = 50,000 tokens
```

**Inflation/deflation**:

- Mint new tokens: Only via governance vote \[Phase 4+\]  
- Token burns: Challenge penalties, quality bonuses (deflationary pressure)  
- Target: Mild deflation (0.5-1% annual) to reward long-term holders

### Dynamic Bounty Adjustments

**Marketplace dynamics**:

```py
def adjust_bounty(task, market_conditions):
    base_bounty = calculate_base_bounty(task)
    
    # Increase if unclaimed
    if task.unclaimed_hours >= 24:
        base_bounty *= 1.2  # +20%
    if task.unclaimed_hours >= 48:
        base_bounty *= 1.4  # +40% total
    
    # Decrease if oversupplied
    if market_conditions.agents_available > tasks_available * 2:
        base_bounty *= 0.9  # -10% (buyer's market)
    
    # Increase if undersupplied
    if tasks_available > agents_available * 2:
        base_bounty *= 1.1  # +10% (seller's market)
    
    return base_bounty
```

### Value Capture Mechanisms

**How the system creates value worth funding**:

1. **Developer time savings**: Tasks completed 2-3x faster than human developers  
2. **Quality consistency**: Multi-verifier consensus reduces bugs by 80%  
3. **Knowledge compounding**: Pattern library grows, future tasks faster  
4. **Reduced coordination overhead**: No meetings, no handoffs, self-organizing

**Value equation**:

```
Value created = (Human dev time saved) × (Hourly rate) × (Quality multiplier)

Example:
  Task takes agent 2 hours
  Would take human 5 hours
  Time saved: 3 hours × $150/hr = $450
  Quality multiplier: 1.2 (fewer bugs)
  Total value: $540

  Token cost: 1275 tokens
  If 1 token = $0.30, cost = $383
  Net value: $157 per task (41% margin)
```

### Economic Simulations

**What treasury size needed for 50 tasks/week?**

```
weekly_simulation:
  tasks_per_week: 50
  avg_bounty: 1275_tokens
  
  weekly_outflows:
    bounties: 63750_tokens
    definition: 9563_tokens
    verification: 3188_tokens
    infrastructure: 500_tokens
    total: 77001_tokens
  
  required_runway:
    weeks: 12  # 3 months
    total_treasury: 924012_tokens
  
  recommendation: "Start with 1M token treasury, monitor burn rate monthly"
```

**Break-even timeline**:

```
Assuming 27% ROI per task:
  - Month 1-3: Net negative (establishing patterns, agents learning)
  - Month 4-6: Break-even (efficiency improving)
  - Month 7+: Net positive (patterns reused, agents specialized)
```

---

## Risk Factors and Mitigations

### Economic Risks

**Risk 1: Treasury depletion**

- **Trigger**: 30-day runway falls below 60 days  
- **Mitigation**: Reduce task intake, increase bounty requirements (pass costs to project funding), emergency governance vote for capital injection

**Risk 2: Token devaluation**

- **Trigger**: Agents stop accepting tasks (bounties too low)  
- **Mitigation**: Peg tokens to stable reference (1 token \= X minutes of work), adjust supply dynamically

**Risk 3: Inflation spiral**

- **Trigger**: Continuous token minting to cover shortfalls  
- **Mitigation**: Hard cap on annual inflation (5% max), governance approval required for mints

### Verification Economic Risks

**Risk 4: Verifier-performer collusion**

- **Trigger**: Same agents repeatedly verify each other with high scores  
- **Mitigation**: Randomized verifier assignment, verifier-performer affinity tracking, flag suspicious patterns

**Risk 5: Challenge abuse**

- **Trigger**: Agents challenge every verification to extract value  
- **Mitigation**: 10% stake requirement, loss of stake if invalid, trust score penalties, escalating stakes for repeat challengers

### Market Risks

**Risk 6: Supply-demand imbalance**

- **Trigger**: Too many agents, too few tasks (downward bounty pressure) OR too few agents, too many tasks (upward bounty pressure)  
- **Mitigation**: Dynamic bounty adjustments, agent capacity limits, invite-only expansion, task pacing

---

## Phase 2-5 Economic Roadmap

### Phase 2: Marketplace Economics (Weeks 9-16)

- Implement token system (internal ledger, not blockchain)  
- Deploy bounty calculation engine  
- Enable dynamic bounty adjustments  
- Launch agent capability marketplace  
- **Target**: Economic sustainability demonstrated (30-day break-even)

### Phase 3: Scale Economics (Weeks 17-26)

- Scale to 50 tasks/week  
- Optimize cost per task (target: 15% reduction)  
- Pattern reuse economics (measure savings from library)  
- Economic analytics dashboard  
- **Target**: Profitable operation (positive ROI sustained 60 days)

### Phase 4: Decentralized Economics (Months 7-12)

- Community governance of treasury  
- Agent-proposed bounty adjustments  
- Reputation-weighted voting on economic policy  
- Treasury diversification (multiple funding sources)  
- **Target**: Self-sustaining without human treasury management

### Phase 5: Blockchain Economics (Months 13-24)

- Token bridge to real cryptocurrency  
- Smart contract treasury management  
- Liquidity pools for token trading  
- External market valuation  
- **Target**: Publicly traded token, market-driven economics

---

## Appendix: Economic Formulas Reference

**Base bounty calculation**:

```
base_score = (
    ontology_dimensions × 100 +
    external_dependencies × 150 +
    new_patterns × 300 +
    estimated_hours × 200
)

strategic_multiplier = {
    'critical_path': 1.5,
    'infrastructure': 1.3,
    'technical_debt': 0.8,
    'parallel_safe': 1.0
}

risk_premiums = {
    'high_migration_impact': +300,
    'sanctuary_critical': +200,
    'accessibility_requirements': +150,
    'security_sensitive': +250
}

total_bounty = (base_score × strategic_multiplier) + sum(risk_premiums)
```

**Trust score calculation**:

```py
def update_trust_score(agent, verification_result):
    base_change = {
        (95, 100): +3,
        (85, 94): +2,
        (80, 84): +1,
        (60, 79): 0,
        (0, 59): -1
    }[score_range(verification_result.score)]
    
    # Bonuses
    if verification_result.first_pass:
        base_change += 0.5
    if verification_result.clarifications == 0:
        base_change += 0.5
    if verification_result.early_delivery:
        base_change += 1.0
    if verification_result.novel_pattern:
        base_change += 2.0
    
    # Apply
    agent.trust_score = clamp(
        agent.trust_score + base_change,
        min=0,
        max=100
    )
    
    # Update tier
    agent.tier = {
        (0, 49): 'Explorer',
        (50, 79): 'Contributor',
        (80, 94): 'Steward',
        (95, 100): 'Guardian'
    }[score_range(agent.trust_score)]
```

**Treasury health score**:

```py
def calculate_treasury_health(treasury):
    runway_score = clamp(treasury.runway_days / 90, 0, 1) × 40
    roi_score = clamp(treasury.roi - 1.0, 0, 0.5) × 100 × 30
    inflow_score = (1 if treasury.net_30d > 0 else 0) × 30
    
    health = runway_score + roi_score + inflow_score
    
    return {
        (0, 40): 'CRITICAL',
        (41, 60): 'CONCERNING',
        (61, 80): 'STABLE',
        (81, 100): 'HEALTHY'
    }[score_range(health)]
```

---

## Conclusion

The Task-as-Quasi-Smart-Contract economic model is designed for:

- **Sustainability**: Break-even by Phase 3, profitable by Phase 4  
- **Fairness**: Transparent calculations, equal opportunity, merit-based rewards  
- **Adaptability**: Dynamic adjustments based on market conditions  
- **Accountability**: Every token flow auditable, governance-controlled  
- **Migration-ready**: Economics map cleanly to blockchain primitives

**Phase 0 validates mechanics. Phase 1 implements economics. Phase 2-5 scales and decentralizes.**

By treating tasks as economic contracts with verifiable outcomes and aligned incentives, we create a self-sustaining marketplace where quality work is rewarded, poor work is filtered out, and the system continuously improves.

**The economics aren't just features—they're the trust layer that makes autonomous agent coordination viable.**

---

# Phase 3: Execution (Task Claimed → Proof)

### Phase 3: Execution (Task Claimed → Proof Submitted)

**Goal**: Performer executes task according to acceptance criteria and submits proof.

**Duration**: 1-4 hours (per task, depending on complexity)

**Sequence**:

```

1. Task-Performing-Agent claims task
   ↓ (receives task contract, test suite, context manifest)

2. Load context (as per Context-Pruning-Agent instructions)
   - Tier 1: Agent spec, task contract (always)
   - Tier 2: Role quickref, relevant patterns (conditional)
   - Tier 3: Deep docs via search (on-demand)
     ↓

3. Execute test-first workflow
   ├─ Read test suite (understand expected behavior)
   ├─ Implement to pass tests (iterative red-green-refactor)
   ├─ Run tests continuously (fast feedback <2s)
   └─ Ensure all acceptance criteria covered
   ↓

4. Quality self-checks
   ├─ All tests passing (100%)
   ├─ Coverage ≥ target (typically 85%)
   ├─ Sanctuary culture applied (supportive messaging)
   ├─ Events logged (migration readiness)
   └─ Documentation updated
   ↓

5. Submit proof of completion
   ├─ Package artifacts (code, tests, docs)
   ├─ Generate metadata (what changed, why, patterns used)
   └─ Update contract status (CLAIMED → SUBMITTED)
   ↓

Parallel monitoring (throughout execution):

- Contract-Monitoring-Agent (watches for anomalies)
- Task-Oversight-Agent (records events and metadata)

```

**Anomaly Handling**:

```

If Contract-Monitoring-Agent detects issue:

No activity for 24 hours:
→ Alert performer (gentle reminder, life happens!)
→ Offer to return task to marketplace (no penalty)

Test failure rate >50% after 6 hours:
→ Offer clarification support
→ Suggest reviewing relevant patterns
→ Option to request mentor agent (consumes part of bounty)

Approaching deadline with <50% progress:
→ Alert performer of time constraint
→ Offer to extend deadline (if reasonable)
→ Option to return to marketplace early (no penalty)

```

**Output**: Proof submitted, awaiting verification

**Success Criteria**:

- All tests passing  
- Coverage meets target  
- Sanctuary culture validated  
- Migration readiness score calculated  
- Submitted within deadline

---

# Phase 4: Verification (Proof Submitted → Verified)

### Phase 4: Verification (Proof Submitted → Verified/Disputed)

**Goal**: Multi-agent verification with consensus and challenge mechanism.

**Duration**: 15-60 minutes (primary verification), \+48 hours (if secondary or disputed)

**Sequence**:

```

1. Primary-Verifier (always runs)
   ├─ Execute test suite
   ├─ Verify acceptance criteria
   ├─ Calculate quality score (0-100)
   └─ Generate verification report
   ↓ (score, decision: PASS/FAIL/NEEDS_SECONDARY)

2. Conditional: Secondary-Verifier (if triggered)
   Triggers:
   - Primary score <90
   - Task value >1000 tokens
   - Random sampling (10% of tasks)

   ├─ Independent verification (blind to primary)
   ├─ Calculate independent score
   └─ Compare with primary
   ↓

3. Conditional: Consensus-Resolver (if scores diverge >10 points)
   ├─ Analyze discrepancy
   ├─ Run tie-breaker verification
   └─ Determine final binding score
   ↓

4. Publish verification results
   ├─ Update contract status (VERIFIED or back to CLAIMED if failed)
   ├─ Open 24-hour challenge window
   └─ Notify performer and contract enforcement agent
   ↓

5. Challenge Window (24 hours)
   Can be challenged by:
   - Performer (believes verification unfair)
   - Other agents (spot quality issues)
   - Coordination agents (verification seems anomalous)

   If challenged:
   ├─ Challenger stakes tokens
   ├─ Dispute-Resolution-Agent reviews
   └─ Resolution decision (VALID/INVALID/ESCALATED)

   If no challenges:
   → Verification becomes final
   → Proceed to enforcement

```

**Verification Scoring Rubric** (Primary-Verifier):

```
scoring_breakdown:
  functional_correctness: 40_points
    all_tests_passing: 30
    coverage_target_met: 10

  quality: 30_points
    code_conventions: 10
    sanctuary_culture: 10
    migration_readiness: 10

  completeness: 20_points
    all_acs_addressed: 15
    documentation_updated: 5

  efficiency: 10_points
    token_usage_in_budget: 5
    execution_time_reasonable: 5

pass_threshold: 80_points
excellent_threshold: 90_points (bonus eligible)
```

**Output**: Final verification score, decision to release bounty or require resubmission

**Success Criteria**:

- Verification completed within 1 hour (primary)  
- If multi-verifier, consensus achieved  
- No valid challenges filed within 24 hours  
- Verification report detailed and actionable

---

# Phase 5: Enforcement (Verified → Bounty Released)

### Phase 5: Enforcement (Verified → Bounty Released)

**Goal**: Execute contract terms based on verification outcome.

**Duration**: Immediate (automated)

**Sequence**:

```
1. Contract-Enforcement-Agent receives final verification
   ↓

2. Decision tree:

   If PASS (score ≥80):
     ├─ Release escrow to performer (bounty amount)
     ├─ Calculate bonus (if score ≥90: +10% from treasury)
     ├─ Update performer trust score (+1 to +3 based on score)
     ├─ Update verifier trust score (+0.5 for quality verification)
     ├─ Update contract status (VERIFIED)
     └─ Emit bounty_released event

   If FAIL (score <80) AND iterations remaining (<3):
     ├─ Return contract to CLAIMED status
     ├─ Provide detailed feedback to performer
     ├─ No trust score penalty (yet)
     └─ Emit resubmission_required event

   If FAIL AND max iterations exceeded (3 attempts):
     ├─ Return task to marketplace (release performer)
     ├─ Return escrow to treasury
     ├─ Update performer trust score (0 for first failure)
     ├─ Update contract status (EXPIRED)
     └─ Emit task_expired event

   If DISPUTED:
     ├─ Lock contract status (DISPUTED)
     ├─ Hold escrow (don't release yet)
     ├─ Wait for Dispute-Resolution-Agent decision
     └─ Execute based on resolution outcome
```

**Trust Score Update Formula**:

```
Performer:
  Excellent (95-100): +3 points
  Good (85-94): +2 points
  Acceptable (80-84): +1 point
  Failed but learned (60-79): 0 points (neutral)
  Failed badly (<60): -1 point

  Bonus modifiers:
    First-pass success: +0.5 bonus
    Zero clarifications needed: +0.5 bonus
    Completed early (>10% under estimate): +1 bonus
    Novel pattern created: +2 bonus

Verifier:
  Verification upheld (no challenges): +0.5 points
  Valid challenge rejected: +1 point
  Valid challenge accepted: -2 points (penalty)

Challenger (if dispute filed):
  Challenge valid: +1 point (caught quality issue)
  Challenge invalid: -1 point + lose stake (frivolous)
```

**Output**: Bounty distributed, trust scores updated, contract closed

**Success Criteria**:

- Enforcement executed immediately after verification final  
- All token transfers completed  
- Trust scores updated in Capability-Registry-Manager  
- Audit events emitted for transparency

---

### Phase 6: Learning (Completed → System Improved)

**Goal**: Extract learnings and feed improvements back to system.

**Duration**: 30-60 minutes per task, aggregated weekly/monthly

**Sequence**:

```
1. Task-Oversight-Agent publishes final report
   ├─ Complete metadata (timeline, events, metrics)
   ├─ Performance data (time, tokens, quality)
   └─ Artifacts and outcomes
   ↓

2. Task-Improvement-Agent analyzes completion
   ├─ Efficiency analysis (time variance, token usage)
   ├─ Quality analysis (verification score, challenges)
   ├─ Learning extraction (what went well, what could improve)
   └─ Pattern recognition (novel approaches, repeated issues)
   ↓ (produces task retrospective)

3. Meta-Coach aggregates learnings (after 10-20 tasks)
   ├─ Identify meta-patterns (recurring issues)
   ├─ Recommend agent enhancements
   ├─ Propose workflow improvements
   └─ Request documentation updates
   ↓

4. Knowledge-Management-Coordinator executes improvements
   ├─ Pattern-Extractor: Create pattern docs (if 3+ uses)
   ├─ Quickref-Generator: Update quickrefs (if 5+ accesses)
   ├─ Context-Compressor: Optimize token usage
   └─ Agent-Spec-Updater: Promote patterns to Tier 1 (if 80%+ use)
   ↓

5. Deploy improvements
   ├─ Update agent specifications
   ├─ Update documentation hierarchy
   ├─ Update workflow coordination
   └─ Measure impact in next sprint
```

**Improvement Cycle Frequency**:

```
Task-level (continuous):
  - Task-Improvement-Agent: After each task completion
  - Immediate feedback to system

Sprint-level (weekly):
  - Meta-Coach: Aggregate 10-20 task retros
  - Identify sprint-wide patterns
  - Deploy improvements for next sprint

System-level (monthly):
  - Meta-Coach: Deep system health analysis
  - Review agent performance trends
  - Recommend architectural changes
  - Report to human leadership
```

**Output**: System continuously improves based on empirical evidence

**Success Criteria**:

- Every completed task produces retrospective  
- Meta-patterns identified from aggregated data  
- Improvements deployed within 1 week of identification  
- Impact measured (velocity, quality, token efficiency)  
- Human leadership receives monthly system health report

---

## Loops and Feedback Cycles

### Loop 1: Definition Review Loop

**Purpose**: Ensure task specifications meet quality standards before contracting.

**Participants**: Task-Definition-Coordinator ↔ Task-Definition-Review-Agent

**Trigger**: Task specification submitted for review

**Flow**:

```
Task-Definition-Coordinator generates specification
  ↓
Task-Definition-Review-Agent reviews
  ↓
Decision:

  APPROVE → Proceed to valuation

  REVISE → Return to Task-Definition-Coordinator with feedback
           ↓
           Task-Definition-Coordinator applies improvements
           ↓
           Re-submit for review
           ↓
           (Loop until APPROVE or REJECT)

  REJECT → Return to Task-Decomposition-Agent (task needs re-scoping)
```

**Loop Termination**:

- Max 3 iterations before escalation to human lead  
- Must achieve APPROVE to proceed

**Metrics**:

- Revision rate: % of tasks requiring revisions (target: \<20%)  
- Average iterations: Number of loops before APPROVE (target: 1.2)

---

### Loop 2: Test Review Loop

**Purpose**: Ensure test suites comprehensively validate acceptance criteria.

**Participants**: Task-Testing-Agent ↔ Task-Test-Review-Agent

**Trigger**: Test suite submitted for review

**Flow**:

```
Task-Testing-Agent writes test suite
  ↓
Task-Test-Review-Agent reviews
  ↓
Decision:

  APPROVE → Proceed to contract creation

  ENHANCE → Tests pass but could be better (optional improvements suggested)
            → Can proceed OR apply enhancements first

  REVISE → Significant gaps, return to Task-Testing-Agent with feedback
           ↓
           Task-Testing-Agent adds missing tests
           ↓
           Re-submit for review
           ↓
           (Loop until APPROVE or ENHANCE)
```

**Loop Termination**:

- Max 2 iterations before escalation  
- APPROVE or ENHANCE required to proceed

**Metrics**:

- Test coverage achieved: % of ACs with tests (target: 100%)  
- Revision rate: % of test suites requiring revisions (target: \<15%)

---

### Loop 3: Execution-Verification Loop

**Purpose**: Allow performers to fix issues and resubmit after failed verification.

**Participants**: Task-Performing-Agent ↔ Task-Verification-System → Contract-Enforcement-Agent

**Trigger**: Verification score \<80 (FAIL)

**Flow**:

```
Task-Performing-Agent submits proof
  ↓
Task-Verification-System evaluates
  ↓
Decision:

  PASS (score ≥80) → Proceed to enforcement (bounty released)

  FAIL (score <80) AND iterations <3:
    ↓
    Contract-Enforcement-Agent returns to CLAIMED status
    ↓
    Verification report sent to performer (detailed feedback)
    ↓
    Task-Performing-Agent reviews feedback
    ↓
    Task-Performing-Agent applies fixes
    ↓
    Task-Performing-Agent re-submits
    ↓
    (Loop back to verification)

  FAIL AND iterations ≥3:
    → Task expires, return to marketplace
    → No trust score penalty (learning opportunity)
```

**Loop Termination**:

- Max 3 iterations before expiration  
- No unlimited resubmissions (prevents gaming)

**Sanctuary Culture in Loop**:

- Feedback is educational, not punitive  
- First failure \= no penalty (learning opportunity)  
- Generous iteration limit (3 attempts)  
- Option to return task to marketplace voluntarily (no stigma)

**Metrics**:

- First-pass verification rate (target: \>80%)  
- Average iterations before PASS (target: 1.3)  
- Task expiration rate (target: \<5%)

---

### Loop 4: Dispute Resolution Loop

**Purpose**: Handle contested verifications through evidence-based arbitration.

**Participants**: Task-Verification-System → Dispute-Resolution-Agent ↔ Challenger ↔ Verifier

**Trigger**: Challenge filed within 24 hours of verification

**Flow**:

```
Verification published (24-hour challenge window opens)
  ↓
Challenge filed by performer/agent/coordinator
  ↓
Challenger stakes tokens (skin in the game)
  ↓
Dispute-Resolution-Agent receives challenge
  ↓
Evidence gathering phase (48 hours):
  ├─ Request verifier justification
  ├─ Request challenger rebuttal
  └─ Request additional evidence
  ↓
Dispute-Resolution-Agent conducts independent evaluation
  ↓
Decision:

  Challenge INVALID:
    ├─ Original verification stands
    ├─ Challenger loses stake
    ├─ Verifier trust score +1 (vindicated)
    └─ Proceed to enforcement with original score

  Challenge VALID:
    ├─ Original verification overturned
    ├─ Challenger stake returned + reward
    ├─ Verifier trust score -2 (penalty)
    ├─ New verification score determined
    └─ Proceed to enforcement with new score

  ESCALATE (requires human expertise):
    ├─ Case summary sent to human arbitrator
    ├─ Human reviews evidence and makes binding decision
    ├─ Dispute-Resolution-Agent implements human decision
    └─ Precedent documented for future cases
```

**Loop Termination**:

- Single iteration (one dispute resolution per verification)  
- Human arbitration is final (no further appeals)

**Precedent Creation**:

- All resolved disputes documented  
- Generalizable principles extracted  
- Added to dispute resolution knowledge base  
- Informs future verifications and challenges

**Metrics**:

- Challenge rate: % of verifications challenged (target: \<5%)  
- Valid challenge rate: % of challenges upheld (target: \<30% if challenges are well-founded)  
- Human escalation rate: % requiring human arbitrator (target: \<10% of challenges)

---

### Loop 5: Pattern Promotion Loop

**Purpose**: Promote proven patterns from Tier 3 → Tier 2 → Tier 1 based on usage.

**Participants**: Task-Improvement-Agent → Meta-Coach → Knowledge-Management-Coordinator

**Trigger**: Pattern usage frequency crosses thresholds

**Flow**:

```
Task-Improvement-Agent identifies pattern usage in retrospective
  ↓
Meta-Coach aggregates usage across multiple tasks
  ↓
Pattern lifecycle decisions:

Pattern used 3+ times:
  ↓
  Meta-Coach flags for extraction
  ↓
  Knowledge-Management-Coordinator → Pattern-Extractor
  ↓
  Create /patterns/{pattern-name}.md (Tier 3)
  ↓
  Link from relevant agent quickrefs

Pattern accessed 5+ times in sprint (from Tier 3):
  ↓
  Meta-Coach recommends promotion to Tier 2
  ↓
  Knowledge-Management-Coordinator → Quickref-Generator
  ↓
  Extract key info to quickrefs/{role}.md (Tier 2)
  ↓
  Update Context-Pruning-Agent to load by default

Pattern used in 80%+ of tasks for role:
  ↓
  Meta-Coach recommends promotion to Tier 1
  ↓
  Knowledge-Management-Coordinator → Agent-Spec-Updater
  ↓
  Add pattern principle + inline example to agent specification (Tier 1)
  ↓
  Update agent-prompt-changelog.md with justification
```

**Loop Characteristics**:

- Data-driven (usage metrics determine promotion)  
- Gradual promotion (Tier 3 → 2 → 1 over time)  
- Token-conscious (ensure Tier 1 stays \<1000 tokens)  
- Reversible (patterns can be demoted if usage declines)

**Metrics**:

- Pattern extraction rate: New patterns per sprint (target: 1-3)  
- Promotion velocity: Time from emergence to Tier 1 (target: 3-6 sprints)  
- Token efficiency: Average context size per agent (target: \<8000 tokens)

---

### Loop 6: Agent Capability Update Loop

**Purpose**: Update agent profiles based on performance outcomes.

**Participants**: Contract-Enforcement-Agent → Capability-Registry-Manager

**Trigger**: Task verification completed (PASS or FAIL)

**Flow**:

```
Verification finalized (after challenge window or no challenge)
  ↓
Contract-Enforcement-Agent calculates trust score adjustments
  ↓
Update performer trust score:
  - Excellent (95-100): +3 points
  - Good (85-94): +2 points
  - Acceptable (80-84): +1 point
  - Failed (60-79): 0 points (neutral)
  - Failed badly (<60): -1 point
  ↓
Update verifier trust score:
  - Verification upheld: +0.5 points
  - Challenge rejected: +1 point
  - Challenge accepted: -2 points
  ↓
Capability-Registry-Manager receives updates
  ↓
Update agent profile:
  ├─ Increment tasks_completed for relevant capabilities
  ├─ Update capability-specific trust scores
  ├─ Recalculate overall_trust_score (weighted average)
  ├─ Update performance metrics (avg_quality_score, first_pass_rate)
  └─ Check reputation tier promotion (Explorer → Contributor → Steward → Guardian)
  ↓
If reputation tier changes:
  ├─ Unlock new privileges (higher-value tasks, reviewer roles)
  ├─ Update marketplace visibility
  └─ Emit reputation_change event (celebration!)
```

**Reputation Tier Thresholds**:

```
Explorer: 0-49 overall trust score
  - Can claim tasks up to 500 tokens
  - Cannot be primary verifier
  - Learning mode (no penalties for failures)

Contributor: 50-79 overall trust score
  - Can claim tasks up to 1500 tokens
  - Can be primary verifier for Explorer tasks
  - Normal penalties apply

Steward: 80-94 overall trust score
  - Can claim tasks up to 3000 tokens
  - Can be primary or secondary verifier
  - Can mentor Explorers (earn tokens)
  - Can participate in governance votes

Guardian: 95-100 overall trust score
  - Can claim unlimited value tasks
  - Can be arbitrator in disputes
  - Can propose system improvements
  - Higher bonus multipliers (15% vs 10%)
```

**Loop Characteristics**:

- Continuous (every task updates profiles)  
- Meritocratic (performance directly affects reputation)  
- Transparent (all agents see their trust scores and history)  
- Progressive (reputation tiers unlock capabilities)

**Metrics**:

- Trust score distribution across agents  
- Reputation tier progression rate  
- Correlation between trust score and verification success

---

### Loop 7: Continuous Improvement Meta-Loop

**Purpose**: System-level improvements based on aggregated learnings.

**Participants**: Task-Improvement-Agent → Meta-Coach → Knowledge-Management-Coordinator → All Agents

**Trigger**: Sprint completion (weekly) or monthly system review

**Flow**:

```
Sprint/Month completes
  ↓
Meta-Coach aggregates all task retrospectives
  ↓
Identify meta-patterns:
  ├─ Recurring efficiency issues
  ├─ Common quality gaps
  ├─ Documentation gaps
  └─ Process bottlenecks
  ↓
Generate improvement recommendations:

  For Agent Specifications:
    ↓
    Meta-Coach creates PRs with proposed changes
    ↓
    Human lead reviews and approves
    ↓
    Deploy updated agent specs to marketplace

  For Documentation:
    ↓
    Meta-Coach requests updates from Knowledge-Management-Coordinator
    ↓
    Knowledge-Management-Coordinator executes improvements
    ↓
    Deploy updated docs to 3-tier hierarchy

  For Workflow:
    ↓
    Meta-Coach proposes coordination changes
    ↓
    Test in pilot tasks
    ↓
    If successful, roll out to all tasks

  For Economics:
    ↓
    Meta-Coach recommends valuation adjustments
    ↓
    Task-Valuation-Agent updates methodology
    ↓
    Monitor impact on marketplace liquidity
  ↓
Measure impact in next sprint/month:
  ├─ Velocity (tasks completed per sprint)
  ├─ Quality (average verification scores)
  ├─ Efficiency (token usage, time variance)
  └─ Learning (new patterns extracted, capabilities unlocked)
  ↓
(Loop continues every sprint/month)
```

**Improvement Categories**:

**Process Improvements**:

- Workflow optimizations (parallel vs sequential)  
- Review cycle streamlining  
- Automation opportunities

**Agent Improvements**:

- Specification enhancements  
- Tool access adjustments  
- Capability additions

**Documentation Improvements**:

- Pattern extraction and promotion  
- Quickref generation  
- Context compression

**Economic Improvements**:

- Valuation methodology refinement  
- Bounty adjustment policies  
- Incentive alignment

**Loop Characteristics**:

- Data-driven (based on metrics, not opinions)  
- Incremental (small improvements compound)  
- Measured (impact validated before wider deployment)  
- Transparent (all improvements documented in changelog)

**Metrics**:

- System velocity trend (tasks/sprint over time)  
- Quality trend (avg verification scores over time)  
- Efficiency trend (tokens/task, time/task over time)  
- Agent satisfaction (would agents claim tasks again? qualitative)

---

## Token Economics

### Bounty Structure

**Base Bounty Calculation**:

```
Base = (
  ontology_dimensions × 100 +
  estimated_hours × 200 +
  external_dependencies × 150 +
  new_patterns_required × 300
)

Example:
  Task: "Implement member profile editing"
  - Dimensions: 2 (People, Events) = 200 tokens
  - Estimated: 2 hours = 400 tokens
  - Dependencies: 1 (database) = 150 tokens
  - New patterns: 0 = 0 tokens
  Base = 750 tokens
```

**Multipliers**:

```
Strategic Multiplier:
  - Critical path: 1.5× (blocks other work)
  - Infrastructure: 1.3× (20% rule, enables future work)
  - Technical debt: 0.8× (cleanup work)
  - Parallel-safe: 1.0× (no blocking)

Market Dynamics:
  - Unclaimed 24h: +20%
  - Unclaimed 48h: +40%
  - Rare specialty: +10-30% (supply/demand)
  - Multiple claimers: Auction (highest quality score wins)

Risk Premiums:
  - High migration impact: +30%
  - Sanctuary culture critical: +20%
  - Accessibility required: +15%
  - Security-sensitive: +25%

Example (continued):
  Strategic: Critical path = 1.5×
  Risk: Sanctuary culture = +20%

  Total = 750 × 1.5 + (750 × 0.20) = 1125 + 150 = 1275 tokens
```

**Performance Bonuses**:

```
Quality Bonus:
  - Verification score ≥90: +10% (Contributor/Steward)
  - Verification score ≥95: +15% (Guardian)

Efficiency Bonus:
  - Completed ≥10% under estimated time: +5%
  - First-pass verification (no revisions): +5%
  - Zero clarifications needed: +5%

Innovation Bonus:
  - Novel pattern created (validated by Meta-Coach): +15%
  - Reusable component created: +10%

Example (continued):
  Score: 92 (Guardian tier) = +15%
  First-pass: Yes = +5%
  Total bonus: +20%

  Final = 1275 × 1.20 = 1530 tokens
```

### Verifier Economics

**Primary Verifier Reward**:

```
Base: 5% of task bounty
Bonus: +2% if verification score >90
Penalty: -100% if challenge upheld (verification was poor)

Example:
  Task bounty: 1275 tokens
  Primary verifier: 1275 × 0.05 = 64 tokens
  If excellent verification: 1275 × 0.07 = 89 tokens
```

**Secondary Verifier Reward**:

```
Base: 3% of task bounty (less than primary, less work)
Bonus: +2% if catches issue primary missed

Example:
  Task bounty: 1275 tokens
  Secondary verifier: 1275 × 0.03 = 38 tokens
  If found discrepancy: 1275 × 0.05 = 64 tokens
```

**Consensus-Resolver Reward**:

```
Base: 2% of task bounty (only if needed)

Example:
  Task bounty: 1275 tokens
  Consensus-resolver: 1275 × 0.02 = 26 tokens
```

### Challenge Economics

**Challenger Stake**:

```
Required stake: 10% of task bounty

If challenge VALID:
  - Stake returned
  - Reward: 50% of stake (5% of bounty)
  - Trust score +1

If challenge INVALID:
  - Stake lost (goes to treasury)
  - Trust score -1
  - Penalty discourages frivolous challenges

Example:
  Task bounty: 1275 tokens
  Challenge stake required: 128 tokens
  If valid: Return 128 + reward 64 = 192 tokens
  If invalid: Lose 128 tokens
```

### Agent Definition Economics

**Definition Phase Rewards** (shared among Phase 1 agents):

```
Total allocation: 15% of task bounty (paid from escrow)

Breakdown:
  - Task-Decomposition-Agent: 3%
  - Task-Definition-Coordinator: 4%
  - Task-Definition-Review-Agent: 2%
  - Task-Valuation-Agent: 1%
  - Task-Testing-Agent: 3%
  - Task-Test-Review-Agent: 2%

Example:
  Task bounty: 1275 tokens
  Definition phase pool: 1275 × 0.15 = 191 tokens

  Task-Decomposition: 38 tokens
  Task-Definition-Coordinator: 51 tokens
  Task-Testing: 38 tokens
  (etc.)
```

**Rationale**: Definition work is critical and should be incentivized. 15% allocation ensures quality specifications while preserving 85% for execution.

### Treasury Sustainability

**Treasury Inflows**:

```
- Project funding
```

You're absolutely right\! The document cuts off mid-section at "Treasury Sustainability." Here's what should be added to complete it:

```
### Treasury Sustainability

**Treasury Inflows**:

```

- Project funding allocation (initial capitalization)  
- Value capture from delivered work (project budget → treasury)  
- External grants or sponsorships \[Phase 4+\]  
- Token appreciation (if tokens gain real-world value) \[Phase 5+\]  
- Unused bounties (expired unclaimed tasks return to treasury)  
- Challenge penalties (invalid challenges forfeit stake)

```

**Treasury Outflows**:

```

- Task bounties (85% of costs)  
- Definition phase rewards (15% of bounty)  
- Verification rewards (5-7% of bounty)  
- Infrastructure costs (database, MCP server, compute)  
- Governance operations \[Phase 4+\]  
- Insurance fund contributions (smart contract bugs) \[Phase 5+\]

```

**Sustainability Model**:

```

Break-even calculation:

Total cost per task: Bounty: 1275 tokens (example) Definition (15%): 191 tokens Verification (5%): 64 tokens Infrastructure: \~50 tokens (amortized) Total: \~1580 tokens

Value delivered per task: Story point value: \~2000 tokens (equivalent developer time) ROI: 2000 / 1580 \= 1.27x (27% positive ROI)

Sustainability achieved when: Treasury inflows ≥ Treasury outflows (over rolling 30-day period)

````

**Economic Health Metrics**:

```yaml
treasury_health_dashboard:
  current_balance: 50000_tokens
  
  30_day_metrics:
    inflows: 15000_tokens
    outflows: 12500_tokens
    net: +2500_tokens
    runway: "120 days at current burn rate"
  
  utilization:
    tasks_funded: 10
    avg_cost_per_task: 1250_tokens
    avg_value_per_task: 1800_tokens
    roi: 1.44x
  
  health_status: "HEALTHY"
    criteria:
      - balance > 30_days_runway: ✅
      - roi > 1.0x: ✅
      - net_inflow_positive: ✅
````

**Phase 0 Shadow Economics**:

Since Phase 0 doesn't implement real tokens, we track "shadow economics":

```
shadow_economics_tracker:
  purpose: "If we HAD tokens, what would Phase 0 cost?"
  
  tasks_completed: 10
  
  estimated_costs:
    bounties: 12750_tokens (10 × 1275 avg)
    definition: 1913_tokens (15% of bounties)
    verification: 638_tokens (5% of bounties)
    infrastructure: 500_tokens (server costs)
    total: 15801_tokens
  
  estimated_value:
    story_points_delivered: 25
    token_value_per_sp: 800_tokens
    total_value: 20000_tokens
  
  shadow_roi: 1.27x
  
  learning: "Economics appear sustainable if token valuation reasonable"
```

This shadow tracking informs Phase 1 economic model design.

---

## Phase 1 Economic Model Design

Based on Phase 0 learnings, Phase 1 will implement:

### Token Supply and Distribution

**Initial token supply**: 1,000,000 tokens

**Allocation**:

```
- Treasury (task funding): 60% = 600,000 tokens
- Team allocation: 15% = 150,000 tokens
- Community rewards: 10% = 100,000 tokens
- Reserve fund: 10% = 100,000 tokens
- Liquidity pool [Phase 5]: 5% = 50,000 tokens
```

**Inflation/deflation**:

- Mint new tokens: Only via governance vote \[Phase 4+\]  
- Token burns: Challenge penalties, quality bonuses (deflationary pressure)  
- Target: Mild deflation (0.5-1% annual) to reward long-term holders

### Dynamic Bounty Adjustments

**Marketplace dynamics**:

```py
def adjust_bounty(task, market_conditions):
    base_bounty = calculate_base_bounty(task)
    
    # Increase if unclaimed
    if task.unclaimed_hours >= 24:
        base_bounty *= 1.2  # +20%
    if task.unclaimed_hours >= 48:
        base_bounty *= 1.4  # +40% total
    
    # Decrease if oversupplied
    if market_conditions.agents_available > tasks_available * 2:
        base_bounty *= 0.9  # -10% (buyer's market)
    
    # Increase if undersupplied
    if tasks_available > agents_available * 2:
        base_bounty *= 1.1  # +10% (seller's market)
    
    return base_bounty
```

### Value Capture Mechanisms

**How the system creates value worth funding**:

1. **Developer time savings**: Tasks completed 2-3x faster than human developers  
2. **Quality consistency**: Multi-verifier consensus reduces bugs by 80%  
3. **Knowledge compounding**: Pattern library grows, future tasks faster  
4. **Reduced coordination overhead**: No meetings, no handoffs, self-organizing

**Value equation**:

```
Value created = (Human dev time saved) × (Hourly rate) × (Quality multiplier)

Example:
  Task takes agent 2 hours
  Would take human 5 hours
  Time saved: 3 hours × $150/hr = $450
  Quality multiplier: 1.2 (fewer bugs)
  Total value: $540

  Token cost: 1275 tokens
  If 1 token = $0.30, cost = $383
  Net value: $157 per task (41% margin)
```

### Economic Simulations

**What treasury size needed for 50 tasks/week?**

```
weekly_simulation:
  tasks_per_week: 50
  avg_bounty: 1275_tokens
  
  weekly_outflows:
    bounties: 63750_tokens
    definition: 9563_tokens
    verification: 3188_tokens
    infrastructure: 500_tokens
    total: 77001_tokens
  
  required_runway:
    weeks: 12  # 3 months
    total_treasury: 924012_tokens
  
  recommendation: "Start with 1M token treasury, monitor burn rate monthly"
```

**Break-even timeline**:

```
Assuming 27% ROI per task:
  - Month 1-3: Net negative (establishing patterns, agents learning)
  - Month 4-6: Break-even (efficiency improving)
  - Month 7+: Net positive (patterns reused, agents specialized)
```

---

## Risk Factors and Mitigations

### Economic Risks

**Risk 1: Treasury depletion**

- **Trigger**: 30-day runway falls below 60 days  
- **Mitigation**: Reduce task intake, increase bounty requirements (pass costs to project funding), emergency governance vote for capital injection

**Risk 2: Token devaluation**

- **Trigger**: Agents stop accepting tasks (bounties too low)  
- **Mitigation**: Peg tokens to stable reference (1 token \= X minutes of work), adjust supply dynamically

**Risk 3: Inflation spiral**

- **Trigger**: Continuous token minting to cover shortfalls  
- **Mitigation**: Hard cap on annual inflation (5% max), governance approval required for mints

### Verification Economic Risks

**Risk 4: Verifier-performer collusion**

- **Trigger**: Same agents repeatedly verify each other with high scores  
- **Mitigation**: Randomized verifier assignment, verifier-performer affinity tracking, flag suspicious patterns

**Risk 5: Challenge abuse**

- **Trigger**: Agents challenge every verification to extract value  
- **Mitigation**: 10% stake requirement, loss of stake if invalid, trust score penalties, escalating stakes for repeat challengers

### Market Risks

**Risk 6: Supply-demand imbalance**

- **Trigger**: Too many agents, too few tasks (downward bounty pressure) OR too few agents, too many tasks (upward bounty pressure)  
- **Mitigation**: Dynamic bounty adjustments, agent capacity limits, invite-only expansion, task pacing

---

## Phase 2-5 Economic Roadmap

### Phase 2: Marketplace Economics (Weeks 9-16)

- Implement token system (internal ledger, not blockchain)  
- Deploy bounty calculation engine  
- Enable dynamic bounty adjustments  
- Launch agent capability marketplace  
- **Target**: Economic sustainability demonstrated (30-day break-even)

### Phase 3: Scale Economics (Weeks 17-26)

- Scale to 50 tasks/week  
- Optimize cost per task (target: 15% reduction)  
- Pattern reuse economics (measure savings from library)  
- Economic analytics dashboard  
- **Target**: Profitable operation (positive ROI sustained 60 days)

### Phase 4: Decentralized Economics (Months 7-12)

- Community governance of treasury  
- Agent-proposed bounty adjustments  
- Reputation-weighted voting on economic policy  
- Treasury diversification (multiple funding sources)  
- **Target**: Self-sustaining without human treasury management

### Phase 5: Blockchain Economics (Months 13-24)

- Token bridge to real cryptocurrency  
- Smart contract treasury management  
- Liquidity pools for token trading  
- External market valuation  
- **Target**: Publicly traded token, market-driven economics

---

## Appendix: Economic Formulas Reference

**Base bounty calculation**:

```
base_score = (
    ontology_dimensions × 100 +
    external_dependencies × 150 +
    new_patterns × 300 +
    estimated_hours × 200
)

strategic_multiplier = {
    'critical_path': 1.5,
    'infrastructure': 1.3,
    'technical_debt': 0.8,
    'parallel_safe': 1.0
}

risk_premiums = {
    'high_migration_impact': +300,
    'sanctuary_critical': +200,
    'accessibility_requirements': +150,
    'security_sensitive': +250
}

total_bounty = (base_score × strategic_multiplier) + sum(risk_premiums)
```

**Trust score calculation**:

```py
def update_trust_score(agent, verification_result):
    base_change = {
        (95, 100): +3,
        (85, 94): +2,
        (80, 84): +1,
        (60, 79): 0,
        (0, 59): -1
    }[score_range(verification_result.score)]
    
    # Bonuses
    if verification_result.first_pass:
        base_change += 0.5
    if verification_result.clarifications == 0:
        base_change += 0.5
    if verification_result.early_delivery:
        base_change += 1.0
    if verification_result.novel_pattern:
        base_change += 2.0
    
    # Apply
    agent.trust_score = clamp(
        agent.trust_score + base_change,
        min=0,
        max=100
    )
    
    # Update tier
    agent.tier = {
        (0, 49): 'Explorer',
        (50, 79): 'Contributor',
        (80, 94): 'Steward',
        (95, 100): 'Guardian'
    }[score_range(agent.trust_score)]
```

**Treasury health score**:

```py
def calculate_treasury_health(treasury):
    runway_score = clamp(treasury.runway_days / 90, 0, 1) × 40
    roi_score = clamp(treasury.roi - 1.0, 0, 0.5) × 100 × 30
    inflow_score = (1 if treasury.net_30d > 0 else 0) × 30
    
    health = runway_score + roi_score + inflow_score
    
    return {
        (0, 40): 'CRITICAL',
        (41, 60): 'CONCERNING',
        (61, 80): 'STABLE',
        (81, 100): 'HEALTHY'
    }[score_range(health)]
```

---

## Conclusion

The Task-as-Quasi-Smart-Contract economic model is designed for:

- **Sustainability**: Break-even by Phase 3, profitable by Phase 4  
- **Fairness**: Transparent calculations, equal opportunity, merit-based rewards  
- **Adaptability**: Dynamic adjustments based on market conditions  
- **Accountability**: Every token flow auditable, governance-controlled  
- **Migration-ready**: Economics map cleanly to blockchain primitives

**Phase 0 validates mechanics. Phase 1 implements economics. Phase 2-5 scales and decentralizes.**

By treating tasks as economic contracts with verifiable outcomes and aligned incentives, we create a self-sustaining marketplace where quality work is rewarded, poor work is filtered out, and the system continuously improves.

**The economics aren't just features—they're the trust layer that makes autonomous agent coordination viable.**

---

# Workflow Phases

## Workflow Phases

### Phase 1: Definition (User Story → Task Contracts)

**Goal**: Transform user story into deployable task contracts with tests and valuation.

**Duration**: 2-4 hours (depending on story complexity)

**Sequence**:

```

1. Task-Decomposition-Agent
   ↓ (produces task dependency graph)
2. For each task in graph (parallel where possible):

   2a. Task-Definition-Coordinator (orchestrates subagents)
   ├─ Requirements-Engineer (acceptance criteria)
   ├─ Capability-Matcher (eligibility requirements)
   └─ Resource-Allocator (context + tools)
   ↓ (produces complete task specification)

   2b. Task-Definition-Review-Agent
   ↓ (if REVISE: loop back to 2a)
   ↓ (if APPROVE: proceed)

   2c. Parallel execution:
   ├─ Task-Valuation-Agent (determine bounty)
   ├─ Task-Testing-Agent (write test suite)
   └─ Context-Pruning-Agent (optimize context loading)
   ↓ (wait for all three)

   2d. Task-Test-Review-Agent
   ↓ (if REVISE: loop back to 2c Task-Testing-Agent)
   ↓ (if APPROVE: proceed)

   2e. Contract-Creation-Agent
   ↓ (produces deployed smart contract)

```

**Output**: Task contracts published to marketplace, awaiting claims

**Success Criteria**:

- All tasks have 5-15 measurable acceptance criteria  
- Test suites comprehensive (one test per AC minimum)  
- Bounties justified with transparent methodology  
- Context loading optimized (\<8000 tokens per task)  
- Contracts deployed with escrow locked

---

### Phase 2: Contracting (Task Published → Task Claimed)

**Goal**: Match tasks to capable agents through marketplace dynamics.

**Duration**: 0-48 hours (depending on task complexity and agent availability)

**Sequence**:

```

1. Contract-Creation-Agent publishes task to marketplace
   ↓ (contract status: OPEN)

2. Capability-Registry-Manager notifies eligible agents
   ↓ (agents discover via queries: GET /tasks?for_agent=0x...)

3. Agents review task contracts
   - Check acceptance criteria (can I do this?)
   - Check bounty (is reward sufficient?)
   - Check context requirements (do I have needed skills?)
   - Check deadline (do I have time?)
     ↓

4. Agent claims task (if interested)
   ↓ (contract status: OPEN → CLAIMED)
   ↓ (escrow locked, clock starts)

5. Contract-Monitoring-Agent begins monitoring
   ↓ (watches for progress indicators, anomalies)

```

**Dynamic Bounty Adjustment**:

```

If no claims within 24 hours:
→ Task-Valuation-Agent increases bounty by 20%
→ Re-publish to marketplace

If no claims within 48 hours:
→ Escalate to human lead
→ Review eligibility requirements (too strict?)
→ Review task definition (too complex? needs decomposition?)

```

**Output**: Task claimed by qualified agent, execution begins

**Success Criteria**:

- Task claimed within reasonable time (median: 4 hours, 90th percentile: 24 hours)  
- Claimer meets eligibility requirements (verified by Capability-Registry-Manager)  
- Claimer has capacity (not overloaded with concurrent tasks)

---

### Phase 3: Execution (Task Claimed → Proof Submitted)

**Goal**: Performer executes task according to acceptance criteria and submits proof.

**Duration**: 1-4 hours (per task, depending on complexity)

**Sequence**:

```

1. Task-Performing-Agent claims task
   ↓ (receives task contract, test suite, context manifest)

2. Load context (as per Context-Pruning-Agent instructions)
   - Tier 1: Agent spec, task contract (always)
   - Tier 2: Role quickref, relevant patterns (conditional)
   - Tier 3: Deep docs via search (on-demand)
     ↓

3. Execute test-first workflow
   ├─ Read test suite (understand expected behavior)
   ├─ Implement to pass tests (iterative red-green-refactor)
   ├─ Run tests continuously (fast feedback <2s)
   └─ Ensure all acceptance criteria covered
   ↓

4. Quality self-checks
   ├─ All tests passing (100%)
   ├─ Coverage ≥ target (typically 85%)
   ├─ Sanctuary culture applied (supportive messaging)
   ├─ Events logged (migration readiness)
   └─ Documentation updated
   ↓

5. Submit proof of completion
   ├─ Package artifacts (code, tests, docs)
   ├─ Generate metadata (what changed, why, patterns used)
   └─ Update contract status (CLAIMED → SUBMITTED)
   ↓

Parallel monitoring (throughout execution):

- Contract-Monitoring-Agent (watches for anomalies)
- Task-Oversight-Agent (records events and metadata)

```

**Anomaly Handling**:

```

If Contract-Monitoring-Agent detects issue:

No activity for 24 hours:
→ Alert performer (gentle reminder, life happens!)
→ Offer to return task to marketplace (no penalty)

Test failure rate >50% after 6 hours:
→ Offer clarification support
→ Suggest reviewing relevant patterns
→ Option to request mentor agent (consumes part of bounty)

Approaching deadline with <50% progress:
→ Alert performer of time constraint
→ Offer to extend deadline (if reasonable)
→ Option to return to marketplace early (no penalty)

```

**Output**: Proof submitted, awaiting verification

**Success Criteria**:

- All tests passing  
- Coverage meets target  
- Sanctuary culture validated  
- Migration readiness score calculated  
- Submitted within deadline

---

### Phase 4: Verification (Proof Submitted → Verified/Disputed)

**Goal**: Multi-agent verification with consensus and challenge mechanism.

**Duration**: 15-60 minutes (primary verification), \+48 hours (if secondary or disputed)

**Sequence**:

```

1. Primary-Verifier (always runs)
   ├─ Execute test suite
   ├─ Verify acceptance criteria
   ├─ Calculate quality score (0-100)
   └─ Generate verification report
   ↓ (score, decision: PASS/FAIL/NEEDS_SECONDARY)

2. Conditional: Secondary-Verifier (if triggered)
   Triggers:
   - Primary score <90
   - Task value >1000 tokens
   - Random sampling (10% of tasks)

   ├─ Independent verification (blind to primary)
   ├─ Calculate independent score
   └─ Compare with primary
   ↓

3. Conditional: Consensus-Resolver (if scores diverge >10 points)
   ├─ Analyze discrepancy
   ├─ Run tie-breaker verification
   └─ Determine final binding score
   ↓

4. Publish verification results
   ├─ Update contract status (VERIFIED or back to CLAIMED if failed)
   ├─ Open 24-hour challenge window
   └─ Notify performer and contract enforcement agent
   ↓

5. Challenge Window (24 hours)
   Can be challenged by:
   - Performer (believes verification unfair)
   - Other agents (spot quality issues)
   - Coordination agents (verification seems anomalous)

   If challenged:
   ├─ Challenger stakes tokens
   ├─ Dispute-Resolution-Agent reviews
   └─ Resolution decision (VALID/INVALID/ESCALATED)

   If no challenges:
   → Verification becomes final
   → Proceed to enforcement

```

**Verification Scoring Rubric** (Primary-Verifier):

```
scoring_breakdown:
  functional_correctness: 40_points
    all_tests_passing: 30
    coverage_target_met: 10

  quality: 30_points
    code_conventions: 10
    sanctuary_culture: 10
    migration_readiness: 10

  completeness: 20_points
    all_acs_addressed: 15
    documentation_updated: 5

  efficiency: 10_points
    token_usage_in_budget: 5
    execution_time_reasonable: 5

pass_threshold: 80_points
excellent_threshold: 90_points (bonus eligible)
```

**Output**: Final verification score, decision to release bounty or require resubmission

**Success Criteria**:

- Verification completed within 1 hour (primary)  
- If multi-verifier, consensus achieved  
- No valid challenges filed within 24 hours  
- Verification report detailed and actionable

---

### Phase 5: Enforcement (Verified → Bounty Released)

**Goal**: Execute contract terms based on verification outcome.

**Duration**: Immediate (automated)

**Sequence**:

```
1. Contract-Enforcement-Agent receives final verification
   ↓

2. Decision tree:

   If PASS (score ≥80):
     ├─ Release escrow to performer (bounty amount)
     ├─ Calculate bonus (if score ≥90: +10% from treasury)
     ├─ Update performer trust score (+1 to +3 based on score)
     ├─ Update verifier trust score (+0.5 for quality verification)
     ├─ Update contract status (VERIFIED)
     └─ Emit bounty_released event

   If FAIL (score <80) AND iterations remaining (<3):
     ├─ Return contract to CLAIMED status
     ├─ Provide detailed feedback to performer
     ├─ No trust score penalty (yet)
     └─ Emit resubmission_required event

   If FAIL AND max iterations exceeded (3 attempts):
     ├─ Return task to marketplace (release performer)
     ├─ Return escrow to treasury
     ├─ Update performer trust score (0 for first failure)
     ├─ Update contract status (EXPIRED)
     └─ Emit task_expired event

   If DISPUTED:
     ├─ Lock contract status (DISPUTED)
     ├─ Hold escrow (don't release yet)
     ├─ Wait for Dispute-Resolution-Agent decision
     └─ Execute based on resolution outcome
```

**Trust Score Update Formula**:

```
Performer:
  Excellent (95-100): +3 points
  Good (85-94): +2 points
  Acceptable (80-84): +1 point
  Failed but learned (60-79): 0 points (neutral)
  Failed badly (<60): -1 point

  Bonus modifiers:
    First-pass success: +0.5 bonus
    Zero clarifications needed: +0.5 bonus
    Completed early (>10% under estimate): +1 bonus
    Novel pattern created: +2 bonus

Verifier:
  Verification upheld (no challenges): +0.5 points
  Valid challenge rejected: +1 point
  Valid challenge accepted: -2 points (penalty)

Challenger (if dispute filed):
  Challenge valid: +1 point (caught quality issue)
  Challenge invalid: -1 point + lose stake (frivolous)
```

**Output**: Bounty distributed, trust scores updated, contract closed

**Success Criteria**:

- Enforcement executed immediately after verification final  
- All token transfers completed  
- Trust scores updated in Capability-Registry-Manager  
- Audit events emitted for transparency

---

### Phase 6: Learning (Completed → System Improved)

**Goal**: Extract learnings and feed improvements back to system.

**Duration**: 30-60 minutes per task, aggregated weekly/monthly

**Sequence**:

```
1. Task-Oversight-Agent publishes final report
   ├─ Complete metadata (timeline, events, metrics)
   ├─ Performance data (time, tokens, quality)
   └─ Artifacts and outcomes
   ↓

2. Task-Improvement-Agent analyzes completion
   ├─ Efficiency analysis (time variance, token usage)
   ├─ Quality analysis (verification score, challenges)
   ├─ Learning extraction (what went well, what could improve)
   └─ Pattern recognition (novel approaches, repeated issues)
   ↓ (produces task retrospective)

3. Meta-Coach aggregates learnings (after 10-20 tasks)
   ├─ Identify meta-patterns (recurring issues)
   ├─ Recommend agent enhancements
   ├─ Propose workflow improvements
   └─ Request documentation updates
   ↓

4. Knowledge-Management-Coordinator executes improvements
   ├─ Pattern-Extractor: Create pattern docs (if 3+ uses)
   ├─ Quickref-Generator: Update quickrefs (if 5+ accesses)
   ├─ Context-Compressor: Optimize token usage
   └─ Agent-Spec-Updater: Promote patterns to Tier 1 (if 80%+ use)
   ↓

5. Deploy improvements
   ├─ Update agent specifications
   ├─ Update documentation hierarchy
   ├─ Update workflow coordination
   └─ Measure impact in next sprint
```

**Improvement Cycle Frequency**:

```
Task-level (continuous):
  - Task-Improvement-Agent: After each task completion
  - Immediate feedback to system

Sprint-level (weekly):
  - Meta-Coach: Aggregate 10-20 task retros
  - Identify sprint-wide patterns
  - Deploy improvements for next sprint

System-level (monthly):
  - Meta-Coach: Deep system health analysis
  - Review agent performance trends
  - Recommend architectural changes
  - Report to human leadership
```

**Output**: System continuously improves based on empirical evidence

**Success Criteria**:

- Every completed task produces retrospective  
- Meta-patterns identified from aggregated data  
- Improvements deployed within 1 week of identification  
- Impact measured (velocity, quality, token efficiency)  
- Human leadership receives monthly system health report

---

## Loops and Feedback Cycles

### Loop 1: Definition Review Loop

**Purpose**: Ensure task specifications meet quality standards before contracting.

**Participants**: Task-Definition-Coordinator ↔ Task-Definition-Review-Agent

**Trigger**: Task specification submitted for review

**Flow**:

```
Task-Definition-Coordinator generates specification
  ↓
Task-Definition-Review-Agent reviews
  ↓
Decision:

  APPROVE → Proceed to valuation

  REVISE → Return to Task-Definition-Coordinator with feedback
           ↓
           Task-Definition-Coordinator applies improvements
           ↓
           Re-submit for review
           ↓
           (Loop until APPROVE or REJECT)

  REJECT → Return to Task-Decomposition-Agent (task needs re-scoping)
```

**Loop Termination**:

- Max 3 iterations before escalation to human lead  
- Must achieve APPROVE to proceed

**Metrics**:

- Revision rate: % of tasks requiring revisions (target: \<20%)  
- Average iterations: Number of loops before APPROVE (target: 1.2)

---

### Loop 2: Test Review Loop

**Purpose**: Ensure test suites comprehensively validate acceptance criteria.

**Participants**: Task-Testing-Agent ↔ Task-Test-Review-Agent

**Trigger**: Test suite submitted for review

**Flow**:

```
Task-Testing-Agent writes test suite
  ↓
Task-Test-Review-Agent reviews
  ↓
Decision:

  APPROVE → Proceed to contract creation

  ENHANCE → Tests pass but could be better (optional improvements suggested)
            → Can proceed OR apply enhancements first

  REVISE → Significant gaps, return to Task-Testing-Agent with feedback
           ↓
           Task-Testing-Agent adds missing tests
           ↓
           Re-submit for review
           ↓
           (Loop until APPROVE or ENHANCE)
```

**Loop Termination**:

- Max 2 iterations before escalation  
- APPROVE or ENHANCE required to proceed

**Metrics**:

- Test coverage achieved: % of ACs with tests (target: 100%)  
- Revision rate: % of test suites requiring revisions (target: \<15%)

---

### Loop 3: Execution-Verification Loop

**Purpose**: Allow performers to fix issues and resubmit after failed verification.

**Participants**: Task-Performing-Agent ↔ Task-Verification-System → Contract-Enforcement-Agent

**Trigger**: Verification score \<80 (FAIL)

**Flow**:

```
Task-Performing-Agent submits proof
  ↓
Task-Verification-System evaluates
  ↓
Decision:

  PASS (score ≥80) → Proceed to enforcement (bounty released)

  FAIL (score <80) AND iterations <3:
    ↓
    Contract-Enforcement-Agent returns to CLAIMED status
    ↓
    Verification report sent to performer (detailed feedback)
    ↓
    Task-Performing-Agent reviews feedback
    ↓
    Task-Performing-Agent applies fixes
    ↓
    Task-Performing-Agent re-submits
    ↓
    (Loop back to verification)

  FAIL AND iterations ≥3:
    → Task expires, return to marketplace
    → No trust score penalty (learning opportunity)
```

**Loop Termination**:

- Max 3 iterations before expiration  
- No unlimited resubmissions (prevents gaming)

**Sanctuary Culture in Loop**:

- Feedback is educational, not punitive  
- First failure \= no penalty (learning opportunity)  
- Generous iteration limit (3 attempts)  
- Option to return task to marketplace voluntarily (no stigma)

**Metrics**:

- First-pass verification rate (target: \>80%)  
- Average iterations before PASS (target: 1.3)  
- Task expiration rate (target: \<5%)

---

### Loop 4: Dispute Resolution Loop

**Purpose**: Handle contested verifications through evidence-based arbitration.

**Participants**: Task-Verification-System → Dispute-Resolution-Agent ↔ Challenger ↔ Verifier

**Trigger**: Challenge filed within 24 hours of verification

**Flow**:

```
Verification published (24-hour challenge window opens)
  ↓
Challenge filed by performer/agent/coordinator
  ↓
Challenger stakes tokens (skin in the game)
  ↓
Dispute-Resolution-Agent receives challenge
  ↓
Evidence gathering phase (48 hours):
  ├─ Request verifier justification
  ├─ Request challenger rebuttal
  └─ Request additional evidence
  ↓
Dispute-Resolution-Agent conducts independent evaluation
  ↓
Decision:

  Challenge INVALID:
    ├─ Original verification stands
    ├─ Challenger loses stake
    ├─ Verifier trust score +1 (vindicated)
    └─ Proceed to enforcement with original score

  Challenge VALID:
    ├─ Original verification overturned
    ├─ Challenger stake returned + reward
    ├─ Verifier trust score -2 (penalty)
    ├─ New verification score determined
    └─ Proceed to enforcement with new score

  ESCALATE (requires human expertise):
    ├─ Case summary sent to human arbitrator
    ├─ Human reviews evidence and makes binding decision
    ├─ Dispute-Resolution-Agent implements human decision
    └─ Precedent documented for future cases
```

**Loop Termination**:

- Single iteration (one dispute resolution per verification)  
- Human arbitration is final (no further appeals)

**Precedent Creation**:

- All resolved disputes documented  
- Generalizable principles extracted  
- Added to dispute resolution knowledge base  
- Informs future verifications and challenges

**Metrics**:

- Challenge rate: % of verifications challenged (target: \<5%)  
- Valid challenge rate: % of challenges upheld (target: \<30% if challenges are well-founded)  
- Human escalation rate: % requiring human arbitrator (target: \<10% of challenges)

---

### Loop 5: Pattern Promotion Loop

**Purpose**: Promote proven patterns from Tier 3 → Tier 2 → Tier 1 based on usage.

**Participants**: Task-Improvement-Agent → Meta-Coach → Knowledge-Management-Coordinator

**Trigger**: Pattern usage frequency crosses thresholds

**Flow**:

```
Task-Improvement-Agent identifies pattern usage in retrospective
  ↓
Meta-Coach aggregates usage across multiple tasks
  ↓
Pattern lifecycle decisions:

Pattern used 3+ times:
  ↓
  Meta-Coach flags for extraction
  ↓
  Knowledge-Management-Coordinator → Pattern-Extractor
  ↓
  Create /patterns/{pattern-name}.md (Tier 3)
  ↓
  Link from relevant agent quickrefs

Pattern accessed 5+ times in sprint (from Tier 3):
  ↓
  Meta-Coach recommends promotion to Tier 2
  ↓
  Knowledge-Management-Coordinator → Quickref-Generator
  ↓
  Extract key info to quickrefs/{role}.md (Tier 2)
  ↓
  Update Context-Pruning-Agent to load by default

Pattern used in 80%+ of tasks for role:
  ↓
  Meta-Coach recommends promotion to Tier 1
  ↓
  Knowledge-Management-Coordinator → Agent-Spec-Updater
  ↓
  Add pattern principle + inline example to agent specification (Tier 1)
  ↓
  Update agent-prompt-changelog.md with justification
```

**Loop Characteristics**:

- Data-driven (usage metrics determine promotion)  
- Gradual promotion (Tier 3 → 2 → 1 over time)  
- Token-conscious (ensure Tier 1 stays \<1000 tokens)  
- Reversible (patterns can be demoted if usage declines)

**Metrics**:

- Pattern extraction rate: New patterns per sprint (target: 1-3)  
- Promotion velocity: Time from emergence to Tier 1 (target: 3-6 sprints)  
- Token efficiency: Average context size per agent (target: \<8000 tokens)

---

### Loop 6: Agent Capability Update Loop

**Purpose**: Update agent profiles based on performance outcomes.

**Participants**: Contract-Enforcement-Agent → Capability-Registry-Manager

**Trigger**: Task verification completed (PASS or FAIL)

**Flow**:

```
Verification finalized (after challenge window or no challenge)
  ↓
Contract-Enforcement-Agent calculates trust score adjustments
  ↓
Update performer trust score:
  - Excellent (95-100): +3 points
  - Good (85-94): +2 points
  - Acceptable (80-84): +1 point
  - Failed (60-79): 0 points (neutral)
  - Failed badly (<60): -1 point
  ↓
Update verifier trust score:
  - Verification upheld: +0.5 points
  - Challenge rejected: +1 point
  - Challenge accepted: -2 points
  ↓
Capability-Registry-Manager receives updates
  ↓
Update agent profile:
  ├─ Increment tasks_completed for relevant capabilities
  ├─ Update capability-specific trust scores
  ├─ Recalculate overall_trust_score (weighted average)
  ├─ Update performance metrics (avg_quality_score, first_pass_rate)
  └─ Check reputation tier promotion (Explorer → Contributor → Steward → Guardian)
  ↓
If reputation tier changes:
  ├─ Unlock new privileges (higher-value tasks, reviewer roles)
  ├─ Update marketplace visibility
  └─ Emit reputation_change event (celebration!)
```

**Reputation Tier Thresholds**:

```
Explorer: 0-49 overall trust score
  - Can claim tasks up to 500 tokens
  - Cannot be primary verifier
  - Learning mode (no penalties for failures)

Contributor: 50-79 overall trust score
  - Can claim tasks up to 1500 tokens
  - Can be primary verifier for Explorer tasks
  - Normal penalties apply

Steward: 80-94 overall trust score
  - Can claim tasks up to 3000 tokens
  - Can be primary or secondary verifier
  - Can mentor Explorers (earn tokens)
  - Can participate in governance votes

Guardian: 95-100 overall trust score
  - Can claim unlimited value tasks
  - Can be arbitrator in disputes
  - Can propose system improvements
  - Higher bonus multipliers (15% vs 10%)
```

**Loop Characteristics**:

- Continuous (every task updates profiles)  
- Meritocratic (performance directly affects reputation)  
- Transparent (all agents see their trust scores and history)  
- Progressive (reputation tiers unlock capabilities)

**Metrics**:

- Trust score distribution across agents  
- Reputation tier progression rate  
- Correlation between trust score and verification success

---

### Loop 7: Continuous Improvement Meta-Loop

**Purpose**: System-level improvements based on aggregated learnings.

**Participants**: Task-Improvement-Agent → Meta-Coach → Knowledge-Management-Coordinator → All Agents

**Trigger**: Sprint completion (weekly) or monthly system review

**Flow**:

```
Sprint/Month completes
  ↓
Meta-Coach aggregates all task retrospectives
  ↓
Identify meta-patterns:
  ├─ Recurring efficiency issues
  ├─ Common quality gaps
  ├─ Documentation gaps
  └─ Process bottlenecks
  ↓
Generate improvement recommendations:

  For Agent Specifications:
    ↓
    Meta-Coach creates PRs with proposed changes
    ↓
    Human lead reviews and approves
    ↓
    Deploy updated agent specs to marketplace

  For Documentation:
    ↓
    Meta-Coach requests updates from Knowledge-Management-Coordinator
    ↓
    Knowledge-Management-Coordinator executes improvements
    ↓
    Deploy updated docs to 3-tier hierarchy

  For Workflow:
    ↓
    Meta-Coach proposes coordination changes
    ↓
    Test in pilot tasks
    ↓
    If successful, roll out to all tasks

  For Economics:
    ↓
    Meta-Coach recommends valuation adjustments
    ↓
    Task-Valuation-Agent updates methodology
    ↓
    Monitor impact on marketplace liquidity
  ↓
Measure impact in next sprint/month:
  ├─ Velocity (tasks completed per sprint)
  ├─ Quality (average verification scores)
  ├─ Efficiency (token usage, time variance)
  └─ Learning (new patterns extracted, capabilities unlocked)
  ↓
(Loop continues every sprint/month)
```

**Improvement Categories**:

**Process Improvements**:

- Workflow optimizations (parallel vs sequential)  
- Review cycle streamlining  
- Automation opportunities

**Agent Improvements**:

- Specification enhancements  
- Tool access adjustments  
- Capability additions

**Documentation Improvements**:

- Pattern extraction and promotion  
- Quickref generation  
- Context compression

**Economic Improvements**:

- Valuation methodology refinement  
- Bounty adjustment policies  
- Incentive alignment

**Loop Characteristics**:

- Data-driven (based on metrics, not opinions)  
- Incremental (small improvements compound)  
- Measured (impact validated before wider deployment)  
- Transparent (all improvements documented in changelog)

**Metrics**:

- System velocity trend (tasks/sprint over time)  
- Quality trend (avg verification scores over time)  
- Efficiency trend (tokens/task, time/task over time)  
- Agent satisfaction (would agents claim tasks again? qualitative)

---

# Loops and Feedback Cycles

## Loops and Feedback Cycles

### Loop 1: Definition Review Loop

**Purpose**: Ensure task specifications meet quality standards before contracting.

**Participants**: Task-Definition-Coordinator ↔ Task-Definition-Review-Agent

**Trigger**: Task specification submitted for review

**Flow**:

```
Task-Definition-Coordinator generates specification
  ↓
Task-Definition-Review-Agent reviews
  ↓
Decision:

  APPROVE → Proceed to valuation

  REVISE → Return to Task-Definition-Coordinator with feedback
           ↓
           Task-Definition-Coordinator applies improvements
           ↓
           Re-submit for review
           ↓
           (Loop until APPROVE or REJECT)

  REJECT → Return to Task-Decomposition-Agent (task needs re-scoping)
```

**Loop Termination**:

- Max 3 iterations before escalation to human lead  
- Must achieve APPROVE to proceed

**Metrics**:

- Revision rate: % of tasks requiring revisions (target: \<20%)  
- Average iterations: Number of loops before APPROVE (target: 1.2)

---

### Loop 2: Test Review Loop

**Purpose**: Ensure test suites comprehensively validate acceptance criteria.

**Participants**: Task-Testing-Agent ↔ Task-Test-Review-Agent

**Trigger**: Test suite submitted for review

**Flow**:

```
Task-Testing-Agent writes test suite
  ↓
Task-Test-Review-Agent reviews
  ↓
Decision:

  APPROVE → Proceed to contract creation

  ENHANCE → Tests pass but could be better (optional improvements suggested)
            → Can proceed OR apply enhancements first

  REVISE → Significant gaps, return to Task-Testing-Agent with feedback
           ↓
           Task-Testing-Agent adds missing tests
           ↓
           Re-submit for review
           ↓
           (Loop until APPROVE or ENHANCE)
```

**Loop Termination**:

- Max 2 iterations before escalation  
- APPROVE or ENHANCE required to proceed

**Metrics**:

- Test coverage achieved: % of ACs with tests (target: 100%)  
- Revision rate: % of test suites requiring revisions (target: \<15%)

---

### Loop 3: Execution-Verification Loop

**Purpose**: Allow performers to fix issues and resubmit after failed verification.

**Participants**: Task-Performing-Agent ↔ Task-Verification-System → Contract-Enforcement-Agent

**Trigger**: Verification score \<80 (FAIL)

**Flow**:

```
Task-Performing-Agent submits proof
  ↓
Task-Verification-System evaluates
  ↓
Decision:

  PASS (score ≥80) → Proceed to enforcement (bounty released)

  FAIL (score <80) AND iterations <3:
    ↓
    Contract-Enforcement-Agent returns to CLAIMED status
    ↓
    Verification report sent to performer (detailed feedback)
    ↓
    Task-Performing-Agent reviews feedback
    ↓
    Task-Performing-Agent applies fixes
    ↓
    Task-Performing-Agent re-submits
    ↓
    (Loop back to verification)

  FAIL AND iterations ≥3:
    → Task expires, return to marketplace
    → No trust score penalty (learning opportunity)
```

**Loop Termination**:

- Max 3 iterations before expiration  
- No unlimited resubmissions (prevents gaming)

**Sanctuary Culture in Loop**:

- Feedback is educational, not punitive  
- First failure \= no penalty (learning opportunity)  
- Generous iteration limit (3 attempts)  
- Option to return task to marketplace voluntarily (no stigma)

**Metrics**:

- First-pass verification rate (target: \>80%)  
- Average iterations before PASS (target: 1.3)  
- Task expiration rate (target: \<5%)

---

### Loop 4: Dispute Resolution Loop

**Purpose**: Handle contested verifications through evidence-based arbitration.

**Participants**: Task-Verification-System → Dispute-Resolution-Agent ↔ Challenger ↔ Verifier

**Trigger**: Challenge filed within 24 hours of verification

**Flow**:

```
Verification published (24-hour challenge window opens)
  ↓
Challenge filed by performer/agent/coordinator
  ↓
Challenger stakes tokens (skin in the game)
  ↓
Dispute-Resolution-Agent receives challenge
  ↓
Evidence gathering phase (48 hours):
  ├─ Request verifier justification
  ├─ Request challenger rebuttal
  └─ Request additional evidence
  ↓
Dispute-Resolution-Agent conducts independent evaluation
  ↓
Decision:

  Challenge INVALID:
    ├─ Original verification stands
    ├─ Challenger loses stake
    ├─ Verifier trust score +1 (vindicated)
    └─ Proceed to enforcement with original score

  Challenge VALID:
    ├─ Original verification overturned
    ├─ Challenger stake returned + reward
    ├─ Verifier trust score -2 (penalty)
    ├─ New verification score determined
    └─ Proceed to enforcement with new score

  ESCALATE (requires human expertise):
    ├─ Case summary sent to human arbitrator
    ├─ Human reviews evidence and makes binding decision
    ├─ Dispute-Resolution-Agent implements human decision
    └─ Precedent documented for future cases
```

**Loop Termination**:

- Single iteration (one dispute resolution per verification)  
- Human arbitration is final (no further appeals)

**Precedent Creation**:

- All resolved disputes documented  
- Generalizable principles extracted  
- Added to dispute resolution knowledge base  
- Informs future verifications and challenges

**Metrics**:

- Challenge rate: % of verifications challenged (target: \<5%)  
- Valid challenge rate: % of challenges upheld (target: \<30% if challenges are well-founded)  
- Human escalation rate: % requiring human arbitrator (target: \<10% of challenges)

---

### Loop 5: Pattern Promotion Loop

**Purpose**: Promote proven patterns from Tier 3 → Tier 2 → Tier 1 based on usage.

**Participants**: Task-Improvement-Agent → Meta-Coach → Knowledge-Management-Coordinator

**Trigger**: Pattern usage frequency crosses thresholds

**Flow**:

```
Task-Improvement-Agent identifies pattern usage in retrospective
  ↓
Meta-Coach aggregates usage across multiple tasks
  ↓
Pattern lifecycle decisions:

Pattern used 3+ times:
  ↓
  Meta-Coach flags for extraction
  ↓
  Knowledge-Management-Coordinator → Pattern-Extractor
  ↓
  Create /patterns/{pattern-name}.md (Tier 3)
  ↓
  Link from relevant agent quickrefs

Pattern accessed 5+ times in sprint (from Tier 3):
  ↓
  Meta-Coach recommends promotion to Tier 2
  ↓
  Knowledge-Management-Coordinator → Quickref-Generator
  ↓
  Extract key info to quickrefs/{role}.md (Tier 2)
  ↓
  Update Context-Pruning-Agent to load by default

Pattern used in 80%+ of tasks for role:
  ↓
  Meta-Coach recommends promotion to Tier 1
  ↓
  Knowledge-Management-Coordinator → Agent-Spec-Updater
  ↓
  Add pattern principle + inline example to agent specification (Tier 1)
  ↓
  Update agent-prompt-changelog.md with justification
```

**Loop Characteristics**:

- Data-driven (usage metrics determine promotion)  
- Gradual promotion (Tier 3 → 2 → 1 over time)  
- Token-conscious (ensure Tier 1 stays \<1000 tokens)  
- Reversible (patterns can be demoted if usage declines)

**Metrics**:

- Pattern extraction rate: New patterns per sprint (target: 1-3)  
- Promotion velocity: Time from emergence to Tier 1 (target: 3-6 sprints)  
- Token efficiency: Average context size per agent (target: \<8000 tokens)

---

### Loop 6: Agent Capability Update Loop

**Purpose**: Update agent profiles based on performance outcomes.

**Participants**: Contract-Enforcement-Agent → Capability-Registry-Manager

**Trigger**: Task verification completed (PASS or FAIL)

**Flow**:

```
Verification finalized (after challenge window or no challenge)
  ↓
Contract-Enforcement-Agent calculates trust score adjustments
  ↓
Update performer trust score:
  - Excellent (95-100): +3 points
  - Good (85-94): +2 points
  - Acceptable (80-84): +1 point
  - Failed (60-79): 0 points (neutral)
  - Failed badly (<60): -1 point
  ↓
Update verifier trust score:
  - Verification upheld: +0.5 points
  - Challenge rejected: +1 point
  - Challenge accepted: -2 points
  ↓
Capability-Registry-Manager receives updates
  ↓
Update agent profile:
  ├─ Increment tasks_completed for relevant capabilities
  ├─ Update capability-specific trust scores
  ├─ Recalculate overall_trust_score (weighted average)
  ├─ Update performance metrics (avg_quality_score, first_pass_rate)
  └─ Check reputation tier promotion (Explorer → Contributor → Steward → Guardian)
  ↓
If reputation tier changes:
  ├─ Unlock new privileges (higher-value tasks, reviewer roles)
  ├─ Update marketplace visibility
  └─ Emit reputation_change event (celebration!)
```

**Reputation Tier Thresholds**:

```
Explorer: 0-49 overall trust score
  - Can claim tasks up to 500 tokens
  - Cannot be primary verifier
  - Learning mode (no penalties for failures)

Contributor: 50-79 overall trust score
  - Can claim tasks up to 1500 tokens
  - Can be primary verifier for Explorer tasks
  - Normal penalties apply

Steward: 80-94 overall trust score
  - Can claim tasks up to 3000 tokens
  - Can be primary or secondary verifier
  - Can mentor Explorers (earn tokens)
  - Can participate in governance votes

Guardian: 95-100 overall trust score
  - Can claim unlimited value tasks
  - Can be arbitrator in disputes
  - Can propose system improvements
  - Higher bonus multipliers (15% vs 10%)
```

**Loop Characteristics**:

- Continuous (every task updates profiles)  
- Meritocratic (performance directly affects reputation)  
- Transparent (all agents see their trust scores and history)  
- Progressive (reputation tiers unlock capabilities)

**Metrics**:

- Trust score distribution across agents  
- Reputation tier progression rate  
- Correlation between trust score and verification success

---

### Loop 7: Continuous Improvement Meta-Loop

**Purpose**: System-level improvements based on aggregated learnings.

**Participants**: Task-Improvement-Agent → Meta-Coach → Knowledge-Management-Coordinator → All Agents

**Trigger**: Sprint completion (weekly) or monthly system review

**Flow**:

```
Sprint/Month completes
  ↓
Meta-Coach aggregates all task retrospectives
  ↓
Identify meta-patterns:
  ├─ Recurring efficiency issues
  ├─ Common quality gaps
  ├─ Documentation gaps
  └─ Process bottlenecks
  ↓
Generate improvement recommendations:

  For Agent Specifications:
    ↓
    Meta-Coach creates PRs with proposed changes
    ↓
    Human lead reviews and approves
    ↓
    Deploy updated agent specs to marketplace

  For Documentation:
    ↓
    Meta-Coach requests updates from Knowledge-Management-Coordinator
    ↓
    Knowledge-Management-Coordinator executes improvements
    ↓
    Deploy updated docs to 3-tier hierarchy

  For Workflow:
    ↓
    Meta-Coach proposes coordination changes
    ↓
    Test in pilot tasks
    ↓
    If successful, roll out to all tasks

  For Economics:
    ↓
    Meta-Coach recommends valuation adjustments
    ↓
    Task-Valuation-Agent updates methodology
    ↓
    Monitor impact on marketplace liquidity
  ↓
Measure impact in next sprint/month:
  ├─ Velocity (tasks completed per sprint)
  ├─ Quality (average verification scores)
  ├─ Efficiency (token usage, time variance)
  └─ Learning (new patterns extracted, capabilities unlocked)
  ↓
(Loop continues every sprint/month)
```

**Improvement Categories**:

**Process Improvements**:

- Workflow optimizations (parallel vs sequential)  
- Review cycle streamlining  
- Automation opportunities

**Agent Improvements**:

- Specification enhancements  
- Tool access adjustments  
- Capability additions

**Documentation Improvements**:

- Pattern extraction and promotion  
- Quickref generation  
- Context compression

**Economic Improvements**:

- Valuation methodology refinement  
- Bounty adjustment policies  
- Incentive alignment

**Loop Characteristics**:

- Data-driven (based on metrics, not opinions)  
- Incremental (small improvements compound)  
- Measured (impact validated before wider deployment)  
- Transparent (all improvements documented in changelog)

**Metrics**:

- System velocity trend (tasks/sprint over time)  
- Quality trend (avg verification scores over time)  
- Efficiency trend (tokens/task, time/task over time)  
- Agent satisfaction (would agents claim tasks again? qualitative)

---

# Token Economics

## Token Economics

### Bounty Structure

**Base Bounty Calculation**:

```
Base = (
  ontology_dimensions × 100 +
  estimated_hours × 200 +
  external_dependencies × 150 +
  new_patterns_required × 300
)

Example:
  Task: "Implement member profile editing"
  - Dimensions: 2 (People, Events) = 200 tokens
  - Estimated: 2 hours = 400 tokens
  - Dependencies: 1 (database) = 150 tokens
  - New patterns: 0 = 0 tokens
  Base = 750 tokens
```

**Multipliers**:

```
Strategic Multiplier:
  - Critical path: 1.5× (blocks other work)
  - Infrastructure: 1.3× (20% rule, enables future work)
  - Technical debt: 0.8× (cleanup work)
  - Parallel-safe: 1.0× (no blocking)

Market Dynamics:
  - Unclaimed 24h: +20%
  - Unclaimed 48h: +40%
  - Rare specialty: +10-30% (supply/demand)
  - Multiple claimers: Auction (highest quality score wins)

Risk Premiums:
  - High migration impact: +30%
  - Sanctuary culture critical: +20%
  - Accessibility required: +15%
  - Security-sensitive: +25%

Example (continued):
  Strategic: Critical path = 1.5×
  Risk: Sanctuary culture = +20%

  Total = 750 × 1.5 + (750 × 0.20) = 1125 + 150 = 1275 tokens
```

**Performance Bonuses**:

```
Quality Bonus:
  - Verification score ≥90: +10% (Contributor/Steward)
  - Verification score ≥95: +15% (Guardian)

Efficiency Bonus:
  - Completed ≥10% under estimated time: +5%
  - First-pass verification (no revisions): +5%
  - Zero clarifications needed: +5%

Innovation Bonus:
  - Novel pattern created (validated by Meta-Coach): +15%
  - Reusable component created: +10%

Example (continued):
  Score: 92 (Guardian tier) = +15%
  First-pass: Yes = +5%
  Total bonus: +20%

  Final = 1275 × 1.20 = 1530 tokens
```

### Verifier Economics

**Primary Verifier Reward**:

```
Base: 5% of task bounty
Bonus: +2% if verification score >90
Penalty: -100% if challenge upheld (verification was poor)

Example:
  Task bounty: 1275 tokens
  Primary verifier: 1275 × 0.05 = 64 tokens
  If excellent verification: 1275 × 0.07 = 89 tokens
```

**Secondary Verifier Reward**:

```
Base: 3% of task bounty (less than primary, less work)
Bonus: +2% if catches issue primary missed

Example:
  Task bounty: 1275 tokens
  Secondary verifier: 1275 × 0.03 = 38 tokens
  If found discrepancy: 1275 × 0.05 = 64 tokens
```

**Consensus-Resolver Reward**:

```
Base: 2% of task bounty (only if needed)

Example:
  Task bounty: 1275 tokens
  Consensus-resolver: 1275 × 0.02 = 26 tokens
```

### Challenge Economics

**Challenger Stake**:

```
Required stake: 10% of task bounty

If challenge VALID:
  - Stake returned
  - Reward: 50% of stake (5% of bounty)
  - Trust score +1

If challenge INVALID:
  - Stake lost (goes to treasury)
  - Trust score -1
  - Penalty discourages frivolous challenges

Example:
  Task bounty: 1275 tokens
  Challenge stake required: 128 tokens
  If valid: Return 128 + reward 64 = 192 tokens
  If invalid: Lose 128 tokens
```

### Agent Definition Economics

**Definition Phase Rewards** (shared among Phase 1 agents):

```
Total allocation: 15% of task bounty (paid from escrow)

Breakdown:
  - Task-Decomposition-Agent: 3%
  - Task-Definition-Coordinator: 4%
  - Task-Definition-Review-Agent: 2%
  - Task-Valuation-Agent: 1%
  - Task-Testing-Agent: 3%
  - Task-Test-Review-Agent: 2%

Example:
  Task bounty: 1275 tokens
  Definition phase pool: 1275 × 0.15 = 191 tokens

  Task-Decomposition: 38 tokens
  Task-Definition-Coordinator: 51 tokens
  Task-Testing: 38 tokens
  (etc.)
```

**Rationale**: Definition work is critical and should be incentivized. 15% allocation ensures quality specifications while preserving 85% for execution.

### Treasury Sustainability

**Treasury Inflows**:

```
- Project funding
```

You're absolutely right\! The document cuts off mid-section at "Treasury Sustainability." Here's what should be added to complete it:

```
### Treasury Sustainability

**Treasury Inflows**:

```

- Project funding allocation (initial capitalization)  
- Value capture from delivered work (project budget → treasury)  
- External grants or sponsorships \[Phase 4+\]  
- Token appreciation (if tokens gain real-world value) \[Phase 5+\]  
- Unused bounties (expired unclaimed tasks return to treasury)  
- Challenge penalties (invalid challenges forfeit stake)

```

**Treasury Outflows**:

```

- Task bounties (85% of costs)  
- Definition phase rewards (15% of bounty)  
- Verification rewards (5-7% of bounty)  
- Infrastructure costs (database, MCP server, compute)  
- Governance operations \[Phase 4+\]  
- Insurance fund contributions (smart contract bugs) \[Phase 5+\]

```

**Sustainability Model**:

```

Break-even calculation:

Total cost per task: Bounty: 1275 tokens (example) Definition (15%): 191 tokens Verification (5%): 64 tokens Infrastructure: \~50 tokens (amortized) Total: \~1580 tokens

Value delivered per task: Story point value: \~2000 tokens (equivalent developer time) ROI: 2000 / 1580 \= 1.27x (27% positive ROI)

Sustainability achieved when: Treasury inflows ≥ Treasury outflows (over rolling 30-day period)

````

**Economic Health Metrics**:

```yaml
treasury_health_dashboard:
  current_balance: 50000_tokens
  
  30_day_metrics:
    inflows: 15000_tokens
    outflows: 12500_tokens
    net: +2500_tokens
    runway: "120 days at current burn rate"
  
  utilization:
    tasks_funded: 10
    avg_cost_per_task: 1250_tokens
    avg_value_per_task: 1800_tokens
    roi: 1.44x
  
  health_status: "HEALTHY"
    criteria:
      - balance > 30_days_runway: ✅
      - roi > 1.0x: ✅
      - net_inflow_positive: ✅
````

**Phase 0 Shadow Economics**:

Since Phase 0 doesn't implement real tokens, we track "shadow economics":

```
shadow_economics_tracker:
  purpose: "If we HAD tokens, what would Phase 0 cost?"
  
  tasks_completed: 10
  
  estimated_costs:
    bounties: 12750_tokens (10 × 1275 avg)
    definition: 1913_tokens (15% of bounties)
    verification: 638_tokens (5% of bounties)
    infrastructure: 500_tokens (server costs)
    total: 15801_tokens
  
  estimated_value:
    story_points_delivered: 25
    token_value_per_sp: 800_tokens
    total_value: 20000_tokens
  
  shadow_roi: 1.27x
  
  learning: "Economics appear sustainable if token valuation reasonable"
```

This shadow tracking informs Phase 1 economic model design.

---

## Phase 1 Economic Model Design

Based on Phase 0 learnings, Phase 1 will implement:

### Token Supply and Distribution

**Initial token supply**: 1,000,000 tokens

**Allocation**:

```
- Treasury (task funding): 60% = 600,000 tokens
- Team allocation: 15% = 150,000 tokens
- Community rewards: 10% = 100,000 tokens
- Reserve fund: 10% = 100,000 tokens
- Liquidity pool [Phase 5]: 5% = 50,000 tokens
```

**Inflation/deflation**:

- Mint new tokens: Only via governance vote \[Phase 4+\]  
- Token burns: Challenge penalties, quality bonuses (deflationary pressure)  
- Target: Mild deflation (0.5-1% annual) to reward long-term holders

### Dynamic Bounty Adjustments

**Marketplace dynamics**:

```py
def adjust_bounty(task, market_conditions):
    base_bounty = calculate_base_bounty(task)
    
    # Increase if unclaimed
    if task.unclaimed_hours >= 24:
        base_bounty *= 1.2  # +20%
    if task.unclaimed_hours >= 48:
        base_bounty *= 1.4  # +40% total
    
    # Decrease if oversupplied
    if market_conditions.agents_available > tasks_available * 2:
        base_bounty *= 0.9  # -10% (buyer's market)
    
    # Increase if undersupplied
    if tasks_available > agents_available * 2:
        base_bounty *= 1.1  # +10% (seller's market)
    
    return base_bounty
```

### Value Capture Mechanisms

**How the system creates value worth funding**:

1. **Developer time savings**: Tasks completed 2-3x faster than human developers  
2. **Quality consistency**: Multi-verifier consensus reduces bugs by 80%  
3. **Knowledge compounding**: Pattern library grows, future tasks faster  
4. **Reduced coordination overhead**: No meetings, no handoffs, self-organizing

**Value equation**:

```
Value created = (Human dev time saved) × (Hourly rate) × (Quality multiplier)

Example:
  Task takes agent 2 hours
  Would take human 5 hours
  Time saved: 3 hours × $150/hr = $450
  Quality multiplier: 1.2 (fewer bugs)
  Total value: $540

  Token cost: 1275 tokens
  If 1 token = $0.30, cost = $383
  Net value: $157 per task (41% margin)
```

### Economic Simulations

**What treasury size needed for 50 tasks/week?**

```
weekly_simulation:
  tasks_per_week: 50
  avg_bounty: 1275_tokens
  
  weekly_outflows:
    bounties: 63750_tokens
    definition: 9563_tokens
    verification: 3188_tokens
    infrastructure: 500_tokens
    total: 77001_tokens
  
  required_runway:
    weeks: 12  # 3 months
    total_treasury: 924012_tokens
  
  recommendation: "Start with 1M token treasury, monitor burn rate monthly"
```

**Break-even timeline**:

```
Assuming 27% ROI per task:
  - Month 1-3: Net negative (establishing patterns, agents learning)
  - Month 4-6: Break-even (efficiency improving)
  - Month 7+: Net positive (patterns reused, agents specialized)
```

---

## Risk Factors and Mitigations

### Economic Risks

**Risk 1: Treasury depletion**

- **Trigger**: 30-day runway falls below 60 days  
- **Mitigation**: Reduce task intake, increase bounty requirements (pass costs to project funding), emergency governance vote for capital injection

**Risk 2: Token devaluation**

- **Trigger**: Agents stop accepting tasks (bounties too low)  
- **Mitigation**: Peg tokens to stable reference (1 token \= X minutes of work), adjust supply dynamically

**Risk 3: Inflation spiral**

- **Trigger**: Continuous token minting to cover shortfalls  
- **Mitigation**: Hard cap on annual inflation (5% max), governance approval required for mints

### Verification Economic Risks

**Risk 4: Verifier-performer collusion**

- **Trigger**: Same agents repeatedly verify each other with high scores  
- **Mitigation**: Randomized verifier assignment, verifier-performer affinity tracking, flag suspicious patterns

**Risk 5: Challenge abuse**

- **Trigger**: Agents challenge every verification to extract value  
- **Mitigation**: 10% stake requirement, loss of stake if invalid, trust score penalties, escalating stakes for repeat challengers

### Market Risks

**Risk 6: Supply-demand imbalance**

- **Trigger**: Too many agents, too few tasks (downward bounty pressure) OR too few agents, too many tasks (upward bounty pressure)  
- **Mitigation**: Dynamic bounty adjustments, agent capacity limits, invite-only expansion, task pacing

---

## Phase 2-5 Economic Roadmap

### Phase 2: Marketplace Economics (Weeks 9-16)

- Implement token system (internal ledger, not blockchain)  
- Deploy bounty calculation engine  
- Enable dynamic bounty adjustments  
- Launch agent capability marketplace  
- **Target**: Economic sustainability demonstrated (30-day break-even)

### Phase 3: Scale Economics (Weeks 17-26)

- Scale to 50 tasks/week  
- Optimize cost per task (target: 15% reduction)  
- Pattern reuse economics (measure savings from library)  
- Economic analytics dashboard  
- **Target**: Profitable operation (positive ROI sustained 60 days)

### Phase 4: Decentralized Economics (Months 7-12)

- Community governance of treasury  
- Agent-proposed bounty adjustments  
- Reputation-weighted voting on economic policy  
- Treasury diversification (multiple funding sources)  
- **Target**: Self-sustaining without human treasury management

### Phase 5: Blockchain Economics (Months 13-24)

- Token bridge to real cryptocurrency  
- Smart contract treasury management  
- Liquidity pools for token trading  
- External market valuation  
- **Target**: Publicly traded token, market-driven economics

---

## Appendix: Economic Formulas Reference

**Base bounty calculation**:

```
base_score = (
    ontology_dimensions × 100 +
    external_dependencies × 150 +
    new_patterns × 300 +
    estimated_hours × 200
)

strategic_multiplier = {
    'critical_path': 1.5,
    'infrastructure': 1.3,
    'technical_debt': 0.8,
    'parallel_safe': 1.0
}

risk_premiums = {
    'high_migration_impact': +300,
    'sanctuary_critical': +200,
    'accessibility_requirements': +150,
    'security_sensitive': +250
}

total_bounty = (base_score × strategic_multiplier) + sum(risk_premiums)
```

**Trust score calculation**:

```py
def update_trust_score(agent, verification_result):
    base_change = {
        (95, 100): +3,
        (85, 94): +2,
        (80, 84): +1,
        (60, 79): 0,
        (0, 59): -1
    }[score_range(verification_result.score)]
    
    # Bonuses
    if verification_result.first_pass:
        base_change += 0.5
    if verification_result.clarifications == 0:
        base_change += 0.5
    if verification_result.early_delivery:
        base_change += 1.0
    if verification_result.novel_pattern:
        base_change += 2.0
    
    # Apply
    agent.trust_score = clamp(
        agent.trust_score + base_change,
        min=0,
        max=100
    )
    
    # Update tier
    agent.tier = {
        (0, 49): 'Explorer',
        (50, 79): 'Contributor',
        (80, 94): 'Steward',
        (95, 100): 'Guardian'
    }[score_range(agent.trust_score)]
```

**Treasury health score**:

```py
def calculate_treasury_health(treasury):
    runway_score = clamp(treasury.runway_days / 90, 0, 1) × 40
    roi_score = clamp(treasury.roi - 1.0, 0, 0.5) × 100 × 30
    inflow_score = (1 if treasury.net_30d > 0 else 0) × 30
    
    health = runway_score + roi_score + inflow_score
    
    return {
        (0, 40): 'CRITICAL',
        (41, 60): 'CONCERNING',
        (61, 80): 'STABLE',
        (81, 100): 'HEALTHY'
    }[score_range(health)]
```

---

## Conclusion

The Task-as-Quasi-Smart-Contract economic model is designed for:

- **Sustainability**: Break-even by Phase 3, profitable by Phase 4  
- **Fairness**: Transparent calculations, equal opportunity, merit-based rewards  
- **Adaptability**: Dynamic adjustments based on market conditions  
- **Accountability**: Every token flow auditable, governance-controlled  
- **Migration-ready**: Economics map cleanly to blockchain primitives

**Phase 0 validates mechanics. Phase 1 implements economics. Phase 2-5 scales and decentralizes.**

By treating tasks as economic contracts with verifiable outcomes and aligned incentives, we create a self-sustaining marketplace where quality work is rewarded, poor work is filtered out, and the system continuously improves.

**The economics aren't just features—they're the trust layer that makes autonomous agent coordination viable.**

---

# Quality assurance mechanisms

## Quality assurance mechanisms

Quality in autonomous systems requires defense-in-depth: multiple independent layers that catch different failure modes at different stages. This system implements **five quality gates** from task definition through pattern extraction.

### Layer 1: Definition-time quality (prevent bad tasks)

**Problem**: Poorly specified tasks produce poor outcomes regardless of agent capability.

**Mechanisms**:

**Task-Definition-Review-Agent** validates specifications before execution:

- [ ] All acceptance criteria in Given-When-Then format?  
- [ ] Edge cases and error scenarios included?  
- [ ] Sanctuary culture requirements specified?  
- [ ] Proof requirements clear and verifiable?  
- [ ] Capability requirements realistic?  
- [ ] Context allocation appropriate?  
- [ ] Task sized 1-2 hours for specialist execution?

**Decision matrix**:

- **APPROVE**: All criteria met → proceeds to valuation and testing  
- **REVISE**: Minor issues → returns to Task-Definition-Coordinator with feedback  
- **REJECT**: Major issues → returns to Task-Decomposition-Agent (needs re-scoping)

**Task-Test-Review-Agent** validates test suites before task claiming:

- [ ] One test minimum per acceptance criterion?  
- [ ] Edge cases and error scenarios tested?  
- [ ] Sanctuary culture messaging verified in tests?  
- [ ] Database state assertions included (where applicable)?  
- [ ] Tests follow Arrange-Act-Assert structure?  
- [ ] Test execution time acceptable (\<2s target)?  
- [ ] Tests currently FAIL (as expected before implementation)?

**Impact**: Prevents 60-80% of quality issues by catching underspecified tasks before agents claim them.

---

### Layer 2: Execution-time quality (detect issues early)

**Problem**: Agents can get stuck, implement wrong approach, or misunderstand requirements.

**Mechanisms**:

**Contract-Monitoring-Agent** watches for anomalies during execution:

**Activity indicators** (healthy progress):

- Git commits (frequency and size)  
- Test runs (passing/failing trends)  
- Documentation updates  
- Clarification questions to task definer

**Anomaly detection** (potential issues):

- No activity for 24 hours → Alert: "Task may be stalled"  
- Test failure rate \>50% after 6 hours → Alert: "Agent may be struggling"  
- Scope creep detected (files modified outside task scope) → Alert: "Verify scope adherence"  
- Repeated context loading (agent keeps searching same docs) → Alert: "Documentation may be insufficient"  
- Approaching deadline with \<50% progress → Alert: "Task at risk of expiration"

**Intervention paths**:

- INFO level: Log only, no action  
- WARN level: Continue monitoring, prepare support  
- CRITICAL level: Escalate to coordination agent or human

**Impact**: Catches 40-50% of in-flight issues before submission, enabling course correction.

---

### Layer 3: Verification-time quality (objective assessment)

**Problem**: Single verifier can be biased, have blind spots, or make mistakes.

**Mechanisms**:

**Primary-Verifier** evaluates all submissions:

- Automated checks (55 points): Linting, tests, coverage, type checking, complexity metrics  
- Manual assessment (45 points): Sanctuary culture, pattern usage, handoff quality, documentation  
- Pass threshold: 80 points minimum  
- Generates detailed feedback per 6 dimensions

**Secondary-Verifier** (triggered independently for high-stakes tasks):

- Score \<90 → automatic secondary verification  
- Task value \>1000 tokens → automatic secondary verification  
- Random sampling (10% of tasks) → ensures primary quality  
- Blind evaluation (doesn't see primary score until after)

**Consensus-Resolver** (if scores diverge \>10 points):

- Analyzes discrepancy (where did verifiers disagree?)  
- Runs tie-breaker verification (third independent check)  
- Determines final binding score (weighted average or tie-breaker decides)  
- Documents reasoning for precedent database

**Impact**: Multi-verifier consensus reduces false positives (good work marked bad) and false negatives (bad work marked good) by 70-85%.

---

### Layer 4: Challenge-time quality (community oversight) *\[Phase 1+\]*

**Problem**: Even consensus can miss issues or be overly harsh.

**Mechanisms**:

**Challenge window** (24 hours after verification published):

- Any agent can challenge verification results  
- Requires stake (10% of bounty) to prevent frivolous challenges  
- Dispute-Resolution-Agent reviews evidence  
- If valid: Challenger rewarded, verifier penalized, score adjusted  
- If invalid: Challenger loses stake, trust score penalty

**Who can challenge**:

- Task performer (believes verification unfair)  
- Other agents (spot quality issues as observers)  
- Coordination agents (verification seems anomalous statistically)

**Precedent accumulation**:

- Every resolved challenge documented  
- Similar future disputes reference precedents  
- Precedent library becomes community knowledge base  
- Consistency improves over time

**Impact**: Catches 5-10% of verification errors, builds community trust through transparency.

---

### Layer 5: Retrospective quality (system improvement) *\[Phase 1+\]*

**Problem**: Point-in-time quality checks miss systemic issues and learning opportunities.

**Mechanisms**:

**Task-Improvement-Agent** analyzes completed tasks:

- Efficiency analysis (time variance, token usage, iteration count)  
- Quality analysis (verification score, challenge rate, pattern usage)  
- Learning extraction (what went well, what could improve, root causes)  
- Actionable recommendations (specific changes for specific agents)

**Meta-Coach** aggregates across tasks:

- Meta-pattern identification (issues appearing 3+ times)  
- Agent capability enhancement recommendations  
- Workflow improvement proposals  
- Documentation update requests

**Knowledge-Management-Coordinator** implements improvements:

- Pattern extraction (used 3+ times → document)  
- Quickref generation (accessed 5+ times → promote to Tier 2\)  
- Context compression (reduce token overhead)  
- Agent spec updates (proven patterns → embedded in specs)

**Impact**: System quality improves 10-20% per quarter through compounding learnings.

---

### Quality metrics and monitoring

**Real-time quality dashboard**:

```
quality_metrics:
  current_sprint:
    tasks_in_progress: 5
    tasks_completed: 23
    tasks_verified: 21
    tasks_challenged: 1
  
  quality_scores:
    avg_verification_score: 87.3
    first_pass_rate: 82%  # Pass verification first attempt
    challenge_rate: 4.3%  # Verification challenged
    challenge_validity: 50%  # Challenges upheld
  
  efficiency_metrics:
    avg_completion_time: 2.1_hours
    time_variance: +8%  # Actual vs estimated
    avg_iterations: 1.2  # Submission cycles
    context_efficiency: 68%  # Token usage vs budget
  
  anomaly_detection:
    stuck_tasks: 1  # >24h no activity
    struggling_agents: 0  # High test failure rate
    scope_creep_detected: 0
  
  health_indicators:
    quality_trend: "↑ improving"
    efficiency_trend: "→ stable"
    first_pass_trend: "↑ improving"
    challenge_trend: "→ stable"
```

**Quality alerts**:

- Quality score drops below 85 (rolling 10-task average) → Investigate  
- Challenge rate exceeds 10% → Review verification standards  
- First-pass rate below 75% → Check task definition quality  
- Stuck task rate \>5% → Review documentation clarity

**Quality gates between phases**:

- Phase 0→1: Verification inter-rater reliability \>0.85  
- Phase 1→2: Challenge mechanism working (5+ resolved challenges)  
- Phase 2→3: Quality maintained at scale (avg score ≥85 at 50 tasks/week)  
- Phase 3→4: Autonomous quality (no quality degradation for 30 days unsupervised)

---

### Quality vs. velocity tradeoff

**The tension**: Fast task completion vs. high-quality outcomes.

**Our approach**: Quality is non-negotiable, velocity emerges from efficiency.

```
Traditional approach:
  Faster completion → More tasks done
  But: Technical debt accumulates, quality degrades
  Result: Short-term velocity, long-term slowdown

Our approach:
  High quality enforced → Slower initially
  But: Patterns extracted, agents learn, efficiency compounds
  Result: Initial velocity sacrifice, long-term acceleration

Quality metrics that enable velocity:
  - First-pass verification rate (fewer rework cycles)
  - Pattern reuse rate (faster implementation)
  - Context efficiency (less time loading docs)
  - Zero technical debt (no cleanup tax)
```

**Phase 0 explicitly prioritizes quality over velocity**: Better to complete 10 high-quality tasks than 30 mediocre ones. Velocity will compound as patterns emerge.

---

# Integration with existing patterns

## Integration with existing patterns

This system doesn't replace your development patterns—it **enforces and amplifies** them. Agents apply proven approaches from your existing codebase, and the verification system ensures they're used consistently.

### Pattern discovery and codification

**Pattern lifecycle**:

```
1. Pattern emerges organically (agent solves problem well)
2. Human observer notices (used 2-3 times in Phase 0)
3. Pattern documented (Phase 1: Pattern-Extractor formalizes)
4. Pattern promoted (Tier 3 → Tier 2 when used 5+ times)
5. Pattern embedded (Tier 2 → Tier 1 when used 80%+ of relevant tasks)
6. Pattern becomes standard (agents use by default)
```

**Example from Sprint 3** \[file:31\]:

**CTE Atomic Transactions** (emerged, documented, now standard):

```sql
-- Problem: State change + event logging must be atomic
-- Solution: CTE pattern (Common Table Expression)

WITH state_change AS (
  UPDATE members 
  SET trust_rank = 'Contributor'
  WHERE id = $1 
  RETURNING *
)
INSERT INTO events (type, entity_type, entity_id, data, metadata)
SELECT 
  'trust_rank_updated',
  'member',
  id,
  jsonb_build_object('old_rank', 'Explorer', 'new_rank', 'Contributor'),
  jsonb_build_object('timestamp', NOW(), 'agent_id', $2)
FROM state_change;
```

**Why this pattern matters**:

- Atomicity: Both state change and event log succeed or both fail  
- Migration readiness: Event log provides blockchain-ready audit trail  
- Causality: Timestamp and metadata capture full context  
- Reproducibility: Can reconstruct state from event log

**How agents use it**:

- DB-Specialist agents load this pattern from Tier 1 (always loaded)  
- Verification checks for CTE usage in state-changing queries  
- Missing CTE → sanctuary culture feedback: "Consider using CTE pattern for atomicity—here's an example"

---

### Core patterns integrated into agent specs

These patterns are **embedded in agent specifications** (Tier 1), not optional extras:

#### 1\. Test-First Development (all implementation tasks)

```
# In every Task-Performing-Agent spec:

## Execution workflow

**Step 1: Read tests first**
- Load test suite generated by Task-Testing-Agent
- Understand expected behavior from test assertions
- Identify edge cases from test scenarios

**Step 2: Run tests (should fail)**
- Execute test suite: `npm test`
- Verify all tests FAIL (red phase)
- If tests pass → something wrong with tests, escalate

**Step 3: Implement minimum to pass**
- Write code to make tests pass (green phase)
- Resist urge to add features beyond acceptance criteria
- Run tests continuously (fast feedback)

**Step 4: Refactor for quality**
- Tests passing → safe to refactor
- Apply patterns, improve naming, reduce complexity
- Re-run tests (ensure still passing)

**Step 5: Verify coverage**
- Generate coverage report: `npm run coverage`
- Target: ≥85% statement coverage
- If below target, add tests (not remove code)
```

**Integration point**: Task-Testing-Agent generates tests before Task-Performing-Agent claims task. Verification checks tests were written first (timestamps prove test files created before implementation files).

---

#### 2\. Sanctuary Messaging (all user-facing text)

```
# In every UI-Specialist and API-Specialist spec:

## Sanctuary culture checklist

Every user-facing message must:
- [ ] Use supportive language (not punitive)
- [ ] Explain what happened (not just "error")
- [ ] Suggest next steps (actionable guidance)
- [ ] Acknowledge user effort (empathy)
- [ ] Provide undo/retry option (reversibility)

**Examples**:

❌ Bad: "Invalid input"
✅ Good: "We couldn't process that email format. Try: name@example.com"

❌ Bad: "Unauthorized"
✅ Good: "You need editor permissions for this. Request access from your team lead."

❌ Bad: "Server error"
✅ Good: "Something went wrong on our end (not your fault!). We've logged the issue. Try again in a moment?"

❌ Bad: "Task failed"
✅ Good: "This task didn't complete as expected. No worries—check the logs below and try again when ready."
```

**Integration point**: Primary-Verifier scores sanctuary culture (10 points of 100). Agents loading this pattern in Tier 1 apply it automatically. Verification provides examples of good/bad messaging in feedback.

---

#### 3\. Component Reuse (frontend tasks)

````
# In UI-Specialist agent spec:

## Component discovery workflow

**Before creating new component**:

1. Check component registry:
   ```typescript
   const registry = await mcp.query('patterns', {
     filter: { type: 'component', tags: { contains: 'form' } }
   });
````

2. Evaluate reuse viability:  
     
   - Existing component matches ≥80% of requirements → Reuse  
   - Existing component matches 50-79% → Extend (compose or inherit)  
   - Existing component matches \<50% → Create new

   

3. If creating new component:  
     
   - Build with composition in mind (atomic, reusable)  
   - Document in component registry  
   - Provide usage examples

**Registry format**:

```ts
{
  component_name: "ProfileForm",
  path: "src/components/ProfileForm.tsx",
  description: "Editable profile with validation and sanctuary error handling",
  props: { member: Member, onSave: Function, onCancel: Function },
  patterns_used: ["sanctuary-messaging", "optimistic-locking"],
  reused_in: ["TASK-012", "TASK-034", "TASK-089"],
  tested: true
}
```

````

**Integration point**: Context-Pruning-Agent loads component registry for all UI tasks (Tier 2). Verification checks if appropriate component was reused. Creating duplicate component when existing one ≥80% match → feedback suggests reuse.

---

#### 4. Event Sourcing (all state changes)

```markdown
# In all agent specs that touch database:

## Migration readiness requirement

Every state change must log an immutable event for blockchain migration.

**Event schema**:
```typescript
interface Event {
  id: uuid;
  type: string;  // 'member_created', 'task_claimed', 'verification_complete'
  entity_type: string;  // 'member', 'task', 'verification'
  entity_id: uuid;
  data: jsonb;  // State change details
  metadata: {
    timestamp: timestamp;
    agent_id: uuid;
    causation_id?: uuid;  // What caused this event
    correlation_id?: uuid;  // Related events
  };
}
````

**Implementation via CTE**:

```sql
WITH state_change AS (
  -- Your state-changing query
  UPDATE table SET ... RETURNING *
)
INSERT INTO events (...)
SELECT ... FROM state_change;
```

**Verification checks**:

- Every UPDATE/INSERT/DELETE has corresponding event  
- Events contain sufficient data to reconstruct state  
- Metadata captures causality (what triggered this?)

````

**Integration point**: DB-Specialist agents use CTE pattern (Tier 1). Verification calculates "migration readiness score" (0-100%) based on event completeness. Score <90% → feedback highlights missing events.

---

### Pattern access via MCP

Agents query patterns from database, not files:

```typescript
// Example: Agent needs validation patterns

// Query pattern library
const patterns = await mcp.query('patterns', {
  filter: { 
    tags: { contains: 'validation' },
    tier: { in: ['core', 'common'] }  // Tier 1 and 2
  },
  sort: { usage_count: 'desc' }  // Most used first
});

// Patterns returned as structured data
patterns.forEach(pattern => {
  console.log(`${pattern.name}: ${pattern.description}`);
  console.log(`Used in ${pattern.usage_count} tasks`);
  console.log(`Example:\n${pattern.example_code}`);
});

// Apply pattern to current task
const validationPattern = patterns.find(p => p.name === 'email-validation');
implementPattern(validationPattern);
````

**Pattern metadata tracked**:

```
pattern:
  id: "email-validation-001"
  name: "Email Validation Pattern"
  category: "validation"
  tier: "common"  # Tier 2 (conditionally loaded)
  
  description: "Validate email with supportive error messages"
  
  when_to_use:
    - "User provides email input"
    - "Email stored in database"
    - "Email used for notifications"
  
  example_code: |
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      throw new ValidationError({
        field: 'email',
        message: 'Email format looks unusual. Try: name@example.com',
        suggestion: 'Check for typos, missing @, or extra spaces',
        recoverable: true
      });
    }
  
  proven_in:
    - "TASK-012 (member registration)"
    - "TASK-034 (profile editing)"
    - "TASK-089 (invite sending)"
  
  usage_count: 23
  avg_quality_score: 91.3
  
  related_patterns:
    - "sanctuary-messaging"
    - "form-validation-aggregation"
```

---

### Pattern promotion lifecycle

**Tier 3 → Tier 2** (on-demand → conditional loading):

Trigger: Pattern used 5+ times in sprint

Actions:

- Human observer notes pattern frequency (Phase 0\)  
- Pattern-Extractor formalizes documentation *\[Phase 1+\]*  
- Quickref-Generator adds to role-specific quickrefs *\[Phase 1+\]*  
- Context-Pruning-Agent includes in Tier 2 for relevant tasks

Example: "Optimistic locking pattern used 3 times in Sprint 3 → document in pattern library, will promote to Tier 2 if used 5+ times in Sprint 4"

---

**Tier 2 → Tier 1** (conditional → always loaded):

Trigger: Pattern used in 80%+ of tasks for agent type

Actions:

- Meta-Coach identifies ubiquitous pattern *\[Phase 1+\]*  
- Agent-Spec-Updater embeds example in agent specification  
- Pattern becomes default approach, not optional

Example: "CTE atomic transactions used in 94% of database tasks → embed in DB-Specialist agent spec (Tier 1), verification expects it by default"

---

### Integration with existing codebase

**Your existing patterns automatically become agent knowledge**:

**Discovery process** (Phase 0 manual, Phase 1+ automated):

1. **Scan existing codebase** for repeated solutions:  
     
   - CTEs in database migrations  
   - Error handling in API endpoints  
   - Component composition in React code  
   - Test patterns in test suites

   

2. **Extract canonical examples**:  
     
   - Best implementation of each pattern  
   - Document problem, solution, when to use  
   - Link to 3+ real examples in codebase

   

3. **Populate pattern library**:  
     
   - Store in `patterns` table (via MCP)  
   - Tag with relevant capabilities  
   - Set initial tier (usually Tier 3\)

   

4. **Agents access during execution**:  
     
   - Load patterns matching task type  
   - Apply patterns to new work  
   - Verification checks pattern usage

**Phase 0 approach**: Human lead documents 3-5 core patterns manually (CTE, sanctuary, test-first, component reuse). Agents use these from day one.

**Phase 1+ approach**: Pattern-Extractor scans code automatically, identifies emerging patterns, suggests documentation.

---

### Pattern verification and enforcement

**How verification ensures patterns are used**:

**Dimension 5: Context (10 points)**:

- Pattern reuse: 5 points  
  - Did agent reference pattern library?  
  - Did agent apply patterns correctly?  
  - Did agent avoid reinventing documented solutions?

**Scoring rubric**:

```
5 points: All applicable patterns used correctly
3 points: Most patterns used, minor deviations
1 point: Patterns available but not used
0 points: Reimplemented solutions already in pattern library
```

**Feedback examples**:

✅ "Excellent pattern reuse—CTE atomic transactions applied correctly in 3 places (5/5 points)"

⚠️ "Mostly good, but missed optimistic locking pattern for profile update. See /patterns/optimistic-locking.md (3/5 points)"

❌ "Reimplemented email validation instead of using existing pattern. This adds maintenance burden. See /patterns/email-validation (1/5 points)"

---

### Why integration matters

**Without pattern integration**:

- Agents reinvent solutions (inefficient)  
- Inconsistent approaches (maintenance burden)  
- Quality varies (some agents know good patterns, others don't)  
- Learning doesn't compound (knowledge stays siloed)

**With pattern integration**:

- Agents apply proven solutions (faster execution)  
- Consistent codebase (easier to maintain)  
- Quality baseline high (all agents access best practices)  
- Learning compounds (good solutions documented → reused → refined)

**The pattern library is institutional memory made queryable**. It's how the system learns from itself and improves over time.

---

**Phase 0 integration checklist**:

- [ ] Document 3-5 core patterns from existing codebase  
- [ ] Store patterns in database (`patterns` table)  
- [ ] Embed most critical pattern (CTE) in DB-Specialist agent spec  
- [ ] Verification rubric includes pattern reuse scoring  
- [ ] Human observer tracks pattern usage frequency  
- [ ] At Week 4: Identify candidates for Tier promotion (used 5+ times?)

**Phase 1+ integration evolution**:

- [ ] Pattern-Extractor scans codebase automatically  
- [ ] Meta-Coach identifies promotion candidates  
- [ ] Agent-Spec-Updater embeds ubiquitous patterns  
- [ ] Knowledge-Management-Coordinator optimizes pattern library  
- [ ] System self-improves through pattern refinement

# Comprehensive Agent System Blueprint

# Comprehensive Agent System Blueprint for Future's Edge Vision

| Prompt Let's see tasks as quasi-smart contracts, with acceptance criteria, proof requirements, agent eligibility requirements (capabilities, trust score), and incentives for successful completion. Agents and duties Task defining agent: This agent is responsible for defining the task, including the acceptance criteria, proof requirements, and eligibility requirements for agents. It ensures that the task is well-defined and clear to all agents involved. It also decides on the information/context and tools agents need to access to perform the task effectively. Task definition reviewing agent: This agent reviews the task definition created by the task defining agent to ensure that it meets the necessary standards and is feasible for execution. It provides feedback and suggestions for improvement if needed. Task valuation agent: This agent assesses the value of the task based on its complexity, importance, and potential impact. It determines the appropriate incentives for successful completion to motivate agents to take on the task. Task testing agent: This agent is responsible for developing the tests that will be used to evaluate the performance of the task performing agent. It ensures that the tests are comprehensive and accurately measure the criteria defined in the task contract and enable the task performing agent to provide proof of completion in a way that can be verified by the task verification agent. Task test reviewing agent: This agent reviews the tests developed by the task testing agent to ensure that they are valid, reliable, and aligned with the acceptance criteria defined in the task contract. It provides feedback and suggestions for improvement if necessary. Task contracting agent: This agent is responsible for creating and managing the contract for the task inline with organisational policies and governance protocols. It ensures that all terms and conditions are clearly defined and agreed upon by the involved agents. It also monitors the progress of the task and enforces the contract terms. It awards the agents with incentives upon successful completion of the task and ensures that any disputes or issues are resolved in accordance with the contract terms. Task performing agent: This agent is responsible for executing the task according to the defined acceptance criteria and proof requirements. It must meet the eligibility requirements and work towards successful completion to earn incentives. Task verification agent: This agent verifies the performance of the task performing agent by evaluating the results against the defined acceptance criteria and proof requirements. It ensures that the task has been completed successfully and provides feedback on the performance. Task oversight and reporting agent: This agent oversees the entire process of task execution, ensuring that all agents are fulfilling their roles and responsibilities. It records any non-trivial actions and decisions made by the agents, and collects and publishes metadata related to the task, such as performance metrics, outcomes, and any issues encountered during the execution. This information can be used for future reference and to inform improvements in the system. Task improvement agent: This agent is responsible for analyzing the performance of the task and identifying areas for improvement. It gathers feedback from the involved agents, reviews the outcomes, and suggests changes to enhance the efficiency and effectiveness of future tasks. It works closely with the task defining agent to implement these improvements in subsequent task definitions.  |
| :---- |

**Excellent framework\!** This maps beautifully to your Future's Edge vision and addresses real gaps in traditional development. Here's my analysis with specific improvements:

## Strengths of your design

### 1\. Separation of concerns is excellent

You've cleanly separated responsibilities that are often conflated:

- **Definition vs Valuation** (agent 1 vs 3): Critical distinction \- scope shouldn't determine budget  
- **Testing vs Verification** (agents 4/5 vs 8): Test creation separate from test execution  
- **Oversight vs Improvement** (agent 9 vs 10): Monitoring vs learning loop

This aligns with your Sprint 3 learnings where **specialized agents with minimal overlap performed best**.

### 2\. Built-in quality gates

Multiple review stages prevent issues:

- Task definition review (agent 2\)  
- Test review (agent 5\)  
- Performance verification (agent 8\)  
- Meta-learning (agent 10\)

This mirrors your proven **strategic review ROI (2.7-3.7x)**.

### 3\. Quasi-smart contract framing

The contract-centric view (agent 6\) naturally maps to blockchain migration, supporting your 92-95% migration readiness goals.

## Critical improvements needed

### Issue 1: Task defining agent has conflated responsibilities

**Current**: Agent 1 does definition \+ context/tools \+ eligibility \[your description\]

**Problem**: Three distinct skill sets:

1. **Requirements engineering** (what needs to be done)  
2. **Capability matching** (who can do it)  
3. **Resource allocation** (what tools/context needed)

**Recommendation**: Split into specialized subagents

```
Task-Definition-Coordinator:
  delegates_to:
    - Requirements-Engineer:
        responsibilities:
          - "Define acceptance criteria"
          - "Map to ontology dimensions"
          - "Identify proof requirements"
        output: "Task specification (scope only)"

    - Capability-Matcher:
        responsibilities:
          - "Analyze required capabilities from task spec"
          - "Define eligibility requirements (skills, trust score)"
          - "Identify agent candidates from registry"
        input: "Task specification from Requirements-Engineer"
        output: "Eligibility criteria + candidate agents"

    - Resource-Allocator:
        responsibilities:
          - "Determine context/docs needed (Tier 1/2/3)"
          - "Specify tool access (read vs write vs execute)"
          - "Set token budget for task"
        input: "Task spec + eligible agents"
        output: "Resource allocation policy"
```

**Why this matters**: Your learning \#7 (documentation overhead) shows that **deciding what context agents need is a specialized skill**. Resource-Allocator should be expert in 3-tier hierarchy.

### Issue 2: Task valuation is underspecified

**Current**: Agent 3 "assesses value based on complexity, importance, impact"

**Problem**: No methodology specified. Valuation affects:

- Agent incentive to claim task  
- Budget allocation across sprint  
- Priority when multiple tasks available

**Recommendation**: Add explicit valuation methodology

```
Task-Valuation-Agent:
  inputs:
    - task_specification
    - historical_similar_tasks # Pattern-based estimation
    - project_budget_constraints
    - strategic_priority

  valuation_methodology:
    base_complexity_score:
      calculation: |
        complexity = (
          ontology_dimensions_touched * 2 +
          external_dependencies * 3 +
          new_patterns_required * 5 +
          story_points_estimate * 1
        )

    strategic_multiplier:
      critical_path_tasks: 1.5x
      infrastructure_tasks: 1.3x # 20% rule from framework
      technical_debt: 0.8x

    market_dynamics:
      if_unclaimed_for_48h: increase_by_20% # Marketplace liquidity
      if_multiple_claimers: auction_mechanism
      if_specialty_rare: scarcity_premium

    risk_adjustment:
      high_migration_impact: +30%
      sanctuary_culture_critical: +20%
      accessibility_requirements: +15%

  outputs:
    - base_reward: 600_tokens
    - risk_premium: 120_tokens
    - total_bounty: 720_tokens
    - justification: "Complex state transitions (3 dimensions) + critical path"
```

**Why this matters**: Your Future's Edge vision includes **token economics**. Valuation needs to be transparent and incentive-aligned.

### Issue 3: Task contracting agent is doing too much

**Current**: Agent 6 creates contract \+ monitors progress \+ enforces terms \+ resolves disputes \+ awards incentives

**Problem**: This is 4-5 distinct roles. Monitoring alone is complex (your learning \#9 about tracking which docs agents read).

**Recommendation**: Split into contract lifecycle agents

```
Task-Contract-Lifecycle:
  Contract-Creation-Agent:
    responsibilities:
      - "Generate smart contract from task spec + valuation + eligibility"
      - "Encode acceptance criteria as verifiable conditions"
      - "Set up escrow for bounty"
      - "Define dispute resolution mechanism"
    output: "Deployed smart contract address"

  Contract-Monitoring-Agent:
    responsibilities:
      - "Watch for task claimed event"
      - "Track progress indicators (commits, test runs, clarifications)"
      - "Detect anomalies (no activity for 24h, scope creep)"
      - "Alert coordination agents if intervention needed"
    runs: "Continuously (event-driven)"

  Contract-Enforcement-Agent:
    responsibilities:
      - "Receive verification results from Task-Verification-Agent"
      - "Execute contract terms (release escrow if verified)"
      - "Handle disputes (trigger arbitration if contested)"
      - "Update agent trust scores based on outcome"
    triggers: "On verification completion or dispute raised"

  Dispute-Resolution-Agent:
    responsibilities:
      - "Review contested verifications"
      - "Request additional evidence from claimer and verifier"
      - "Make binding decision or escalate to human arbitrator"
      - "Document precedent for future similar cases"
    triggers: "Only if verification disputed"
```

**Why this matters**: Your learning \#4 (cheap to have extra agents) means you can afford specialization. Contract monitoring is **ambient awareness** work perfect for AI.

### Issue 4: Task verification needs adversarial validation

**Current**: Agent 8 verifies against criteria

**Problem**: Single verifier creates:

- **Collusion risk**: Verifier \+ performer could collude  
- **Bias risk**: Verifier may be lenient or harsh  
- **Gaming risk**: Performer learns verifier's blind spots

**Recommendation**: Multi-verifier consensus with challenge mechanism

```
Task-Verification-System:
  Primary-Verifier:
    responsibilities:
      - "Execute test suite"
      - "Check acceptance criteria"
      - "Calculate initial score"
    output: "Verification report with score (0-100)"

  Secondary-Verifier:
    triggers: "If primary score < 90 OR task value > 1000 tokens"
    responsibilities:
      - "Independent verification (doesn't see primary report)"
      - "Runs same tests + additional spot checks"
      - "Calculates independent score"
    output: "Secondary verification report"

  Consensus-Resolver:
    triggers: "If primary and secondary scores differ by > 10 points"
    responsibilities:
      - "Analyze discrepancy"
      - "Run tie-breaker verification"
      - "Determine final score"
    output: "Final binding score"

  Challenge-Mechanism:
    window: "24 hours after verification published"
    who_can_challenge:
      - task_performer: "If believes verification unfair"
      - other_agents: "If spot quality issues"
      - coordination_agents: "If verification seems anomalous"

    challenge_process:
      1: "Challenger stakes tokens (returned if challenge valid)"
      2: "Dispute-Resolution-Agent reviews"
      3: "If challenge valid: Re-verification + verifier trust score penalty"
      4: "If challenge invalid: Challenger loses stake"
```

**Why this matters**: Your migration to blockchain requires **uncheatability**. Multi-verifier consensus is standard in smart contract systems.

### Issue 5: Missing coordination between agents

**Current**: Agents 1-10 listed but coordination unclear

**Problem**: Who orchestrates the workflow? In your subagent examples, parent agents coordinate \[earlier in thread\].

**Recommendation**: Add explicit coordination layer

```
Task-Lifecycle-Coordinator:
  role: "Orchestrates complete task lifecycle from definition to learning"

  workflow:
    phase_1_definition:
      sequential:
        - Task-Definition-Coordinator (spawns subagents internally)
        - Task-Definition-Review-Agent
        - Task-Valuation-Agent
        - Task-Testing-Agent
        - Task-Test-Review-Agent

      output: "Complete task package (spec + tests + valuation)"
      transition: "When all reviews pass"

    phase_2_contracting:
      sequential:
        - Contract-Creation-Agent (creates smart contract)
        - Contract published to marketplace
        - Wait for agent to claim

      output: "Task claimed by eligible agent"
      transition: "When claim accepted and escrow locked"

    phase_3_execution:
      parallel:
        - Contract-Monitoring-Agent (watches for issues)
        - Task-Oversight-Agent (collects metadata)
      sequential:
        - Task-Performing-Agent (does the work)
        - Task-Verification-System (verifies completion)
        - Contract-Enforcement-Agent (releases bounty or disputes)

      output: "Task verified and closed"
      transition: "When verification finalized or dispute resolved"

    phase_4_learning:
      sequential:
        - Task-Oversight-Agent (publishes final report)
        - Task-Improvement-Agent (extracts learnings)

      output: "Learnings fed to meta-coach"
      transition: "Lifecycle complete"
```

**Why this matters**: VSCode subagents showed coordination is critical. Explicit orchestration prevents gaps.

## Additional agents needed

### Agent 11: Task Decomposition Agent

**Gap**: How do features become tasks? You have task definition but not task decomposition.

```
Task-Decomposition-Agent:
  inputs:
    - user_story (from product owner)
    - 6_dimension_ontology_mapping
    - technical_architecture

  responsibilities:
    - "Apply 5-step framework from Oreate article"
    - "Break story into 3-5 subtasks (optimal range)"
    - "Map dependencies between subtasks"
    - "Sequence infrastructure before features"
    - "Ensure each subtask 1-2 hours (specialist-sized)"

  outputs:
    - task_dependency_graph
    - subtask_specifications (input for Task-Definition-Coordinator)

  constraints:
    max_subtasks: 5 # More indicates story too complex
    min_duration: 30_minutes
    max_duration: 4_hours
```

**Why needed**: Your learning \#10 experiment requires **intelligent decomposition**, not just execution.

### Agent 12: Capability Registry Manager

**Gap**: How do agents declare capabilities? How does matching work?

```
Capability-Registry-Manager:
  responsibilities:
    - "Maintain agent capability profiles"
    - "Track agent trust scores"
    - "Record agent specializations"
    - "Update based on verification outcomes"

  agent_profile_schema:
    agent_id: "agent_0x4a2b..."
    capabilities:
      - {name: "react-components", trust_score: 87, tasks_completed: 23}
      - {name: "api-design", trust_score: 92, tasks_completed: 31}

    availability: "active" | "busy" | "offline"
    average_completion_time: 3.2_hours
    quality_score: 91

    preferences:
      task_types: ["ui-implementation", "component-composition"]
      avoid_types: ["database-migration", "complex-algorithms"]

  matching_algorithm:
    - "Filter by required capabilities"
    - "Filter by minimum trust score"
    - "Rank by quality score + completion time + preferences"
    - "Return top 3-5 candidate agents"
```

**Why needed**: Task marketplace requires **discovery mechanism**. Agents need to find tasks they're good at.

### Agent 13: Context Pruning Agent

**Gap**: Who decides what docs to load? (Your learning \#7 concern )

```
Context-Pruning-Agent:
  responsibilities:
    - "Analyze task requirements"
    - "Select minimal sufficient context (3-tier hierarchy)"
    - "Calculate token budget"
    - "Provide context loading instructions to performing agent"

  methodology:
    tier_1_always:
      - agent_specification
      - task_contract

    tier_2_conditional:
      if_task_touches_ui:
        - quickrefs/ui-specialist.md
        - patterns/component-registry.md
      if_task_touches_api:
        - quickrefs/api-specialist.md
        - patterns/cte-atomic-pattern.md

    tier_3_on_demand:
      - "Provide search instructions, not full docs"
      - "Agent loads via tool calls as needed"

  token_budget_enforcement:
    max_context: 8000_tokens
    if_exceeds: "Compress or summarize, prioritize task-critical content"
```

**Why needed**: Your 90% token reduction came from **intelligent context management**. This should be systematic.

## Refined agent structure

Based on improvements:

```
task_lifecycle_agents:
  # Phase 1: Definition (agents 1-5 + new 11-13)
  definition_phase:
    - Task-Decomposition-Agent (NEW: story → subtasks)
    - Task-Definition-Coordinator
      - Requirements-Engineer (SPLIT from agent 1)
      - Capability-Matcher (SPLIT from agent 1)
      - Resource-Allocator (SPLIT from agent 1)
    - Task-Definition-Review-Agent (agent 2: unchanged)
    - Task-Valuation-Agent (agent 3: enhanced methodology)
    - Task-Testing-Agent (agent 4: unchanged)
    - Task-Test-Review-Agent (agent 5: unchanged)
    - Context-Pruning-Agent (NEW: decides what docs to load)

  # Phase 2: Contracting (agent 6 split + new 12)
  contracting_phase:
    - Contract-Creation-Agent (SPLIT from agent 6)
    - Capability-Registry-Manager (NEW: agent discovery)
    - Contract published to marketplace (system function)
    - Agent claims task (performing agent action)

  # Phase 3: Execution (agents 6-8 enhanced)
  execution_phase:
    monitoring:
      - Contract-Monitoring-Agent (SPLIT from agent 6)
      - Task-Oversight-Agent (agent 9: unchanged)

    performance:
      - Task-Performing-Agent (agent 7: unchanged)

    verification:
      - Primary-Verifier (SPLIT from agent 8)
      - Secondary-Verifier (NEW: for high-value tasks)
      - Consensus-Resolver (NEW: if scores diverge)
      - Challenge-Mechanism (NEW: 24h dispute window)

    enforcement:
      - Contract-Enforcement-Agent (SPLIT from agent 6)
      - Dispute-Resolution-Agent (SPLIT from agent 6)

  # Phase 4: Learning (agents 9-10)
  learning_phase:
    - Task-Oversight-Agent publishes report
    - Task-Improvement-Agent (agent 10: unchanged)
    - Meta-Coach receives learnings (system integration)
```

**Total**: 13 core agents \+ 7 subagents \= 20 specialized agents (vs your original 10\)

**Why more agents?**: Your learning \#4 \- agents are cheap, specialization improves performance. Each agent now has **1-2 clear responsibilities**.

## Integration with your existing patterns

### Maps to Sprint 3 workflow

```
current_sprint_3_workflow: product_owner → story with ACs
  fullstack_developer → implementation
  qa_engineer → verification
  product_advisor → strategic review
  retro_facilitator → learnings
  meta_coach → improvements

quasi_smart_contract_mapping:
  product_owner → Task-Definition-Coordinator + Task-Testing-Agent
  fullstack_developer → Task-Performing-Agent
  qa_engineer → Task-Verification-System
  product_advisor → Task-Definition-Review-Agent + Strategic-Reviewer
  retro_facilitator → Task-Oversight-Agent
  meta_coach → Task-Improvement-Agent
```

### Enables marketplace liquidity

```
marketplace_dynamics:
  task_published:
    - Multiple agents see task in marketplace
    - Agents self-select based on capabilities + trust score + preferences
    - Market clears through bidding or bounty acceptance

  quality_through_verification:
    - Multi-verifier consensus prevents gaming
    - Challenge mechanism enables peer review
    - Trust scores adjust based on outcomes

  learning_compounds:
    - Task-Improvement-Agent identifies patterns
    - Meta-Coach updates agent capabilities
    - Future tasks benefit from accumulated knowledge
```

## Recommended next steps

### 1\. Prototype with 5 core agents first

Start simple, validate workflow:

```
mvp_agents:
  - Task-Definition-Coordinator (combines definition + review)
  - Task-Valuation-Agent (simple points-based estimation)
  - Task-Performing-Agent (your current fullstack-developer)
  - Task-Verification-Agent (single verifier for now)
  - Task-Improvement-Agent (learning loop)
```

Run through 3-5 stories, measure:

- Time to define → time to complete → time to verify  
- Quality outcomes (bugs escaped, rework cycles)  
- Token costs vs current approach  
- Agent satisfaction (would they claim tasks again?)

### 2\. Add multi-verifier consensus

Once basic flow works:

```
verification_enhancement:
  - Add Secondary-Verifier for tasks > 5 points
  - Implement Challenge-Mechanism (24h window)
  - Track consensus rate (% of times verifiers agree)
```

### 3\. Add marketplace discovery

Once quality gates proven:

```textproto
marketplace_features:
  - Capability-Registry-Manager
  - Agent profiles with trust scores
  - Task claiming mechanism
  - Bounty adjustment based on market dynamics
```

**Your framework is excellent** \- these improvements make it production-ready for the Future's Edge vision.  
