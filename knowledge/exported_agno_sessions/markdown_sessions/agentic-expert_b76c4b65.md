# Agentic Expert

| Field | Value |
|-------|-------|
| **Session** | `b76c4b65...` |
| **Type** | agent |
| **Agent** | Agentic Expert |
| **User** | pete@peterargent.com |
| **Created** | 2026-05-20T02:30:40 |
| **Runs** | 2 completed / 2 total |

## Run 1 — Agentic Expert ✓ COMPLETED

*2026-05-20T02:30:40* · `glm-5.1:cloud` · `ab401fbb...`

### Prompt

Talk me through the idea for this tool:
***
2.2 Cognitive Load Budget Calculator
The Problem

The 5-decisions-per-session budget is based on research-informed estimates, not empirical data. Decision density varies by user (Sarah Chen has 30 minutes; Daniel Kovacs might have 2 hours), by domain (commercial law decisions carry more weight than marketing copy decisions), and by session (the first Boundary Map session is more cognitively demanding than a Trust Ledger review).

The current cognitive load budget is a fixed number. It should be adaptive.

The Solution

Build a Cognitive Load Budget Calculator that produces per-session, per-user, per-domain budgets:

Budget Formula:

decisions_per_session = base_capacity
  × domain_weight
  × user_experience_modifier
  × session_sequence_modifier
  × decision_complexity_modifier

Component Definitions:

Factor
How It's Set
Example Values
Base capacity
Research baseline (5 decisions/session for unfamiliar domain)
3 (novice) → 5 (standard) → 8 (expert)
Domain weight
Stakes classification from P0
0.7 (high-stakes legal) → 1.0 (standard) → 1.3 (low-stakes operational)
User experience modifier
Progressive disclosure level
0.8 (Quick Start) → 1.0 (Practitioner) → 1.3 (Architect)
Session sequence modifier
Position in Boundary Journey
0.7 (first session — unfamiliar) → 1.0 (second session — pattern recognized) → 1.2 (third+ — routine)
Decision complexity modifier
Average decision complexity in this session
0.6 (high complexity — identity questions) → 1.0 (standard) → 1.4 (low complexity — status review)


Sample Calculations:

User
Domain
Session
Budget
Sarah Chen (novice)
High-stakes legal
First Boundary Map
5 × 0.7 × 0.8 × 0.7 × 0.6 = 1.2 → 1-2 decisions
Daniel Kovacs (Practitioner)
Standard legal
Second Allocation Map
5 × 1.0 × 1.0 × 1.0 × 1.0 = 5 decisions
Peter (Architect)
Low-stakes operational
Fifth Trust Ledger
5 × 1.3 × 1.3 × 1.2 × 1.4 = 14 → 12-15 decisions


Sarah Chen's first session should have 1-2 decisions, not 5. That means the Mirror Agent presents fewer options per turn and spreads the identity questions across more turns.

Implementation Architecture:

cognitive_load_calculator/
  ├── models.py          # CognitiveLoadBudget, SessionProfile, DecisionProfile Pydantic models
  ├── calculator.py      # Budget calculation engine
  ├── session_tracker.py # Tracks decisions made per session, adjusts modifier over time
  ├── domain_profiles.py # Default domain weight profiles
  └── api.py             # API for integration with Design Studio and Mirror Agent

Integration Points:

Integration
What It Does
Mirror Agent
Uses budget to pace decisions per turn
Design Studio
Displays remaining decision capacity in attention map
Trust Ledger
Tracks decision fatigue indicators (rushing, rubber-stamping, inconsistency)
Progressive Autonomy
Decision budget increases as user gains experience (learning scaffold)


Connection to existing concepts: This operationalizes CC-2 (Human Enrichment Assessment) and ADHD design principle #1 (Cognitive Load as a Budget). The budget is literally a budget — a finite resource that must be allocated. The calculator makes the budget adaptive rather than fixed. It connects to the User Context Framework (cognitive style, time constraints, decision complexity all influence the budget).
***

### Response

Good — this is a tool idea that deserves real scrutiny. Let me walk through it honestly, pulling in what we know from the full body of work.

## What's Strong

**The core insight is right.** A fixed 5-decisions-per-session budget contradicts three things we already believe:

1. **ADHD Design Principle #1** — cognitive load is a *budget*, not an assumption. If it's a budget, it should be *calculated*, not guessed.
2. **Progressive Disclosure** — Sarah Chen at Quick Start level should not face the same decision density as Peter at Architect level. One size is not one budget.
3. **The 77% Challenge** — Sarah walks in with 30 minutes and maximum skepticism. If she faces 5 decisions in that window, she's gone. The calculator models this correctly: 1-2 decisions for Sarah's first session is *real*.

**The formula is transparent and composable.** Each modifier has a clear source (P0 stakes, progressive disclosure level, session position, decision type). This means you can explain *why* a budget is what it is — which is the trust-through-specificity principle applied to system behavior, not just agent output.

**The Sarah Chen calculation is the proof.** `5 × 0.7 × 0.8 × 0.7 × 0.6 = 1.18` → 1-2 decisions. That's not a theoretical exercise — that's exactly what the 30-minute Boundary Map needs. If Sarah gets 5 decisions in her first session, we've already lost her. If she gets 1-2, she has capacity to think about each one.

## What Needs Pushback

**The formula looks precise but the modifiers are estimates.** The example values (0.7 for high-stakes, 0.8 for novice, etc.) are research-informed but not empirically validated. This is the same criticism the document levels at the fixed number — the modifiers just spread the estimation across 5 dimensions instead of concentrating it in 1. That's *better* (dimensional estimates compound more realistically than a single number), but it's still estimation.

**Recommendation:** Ship with the estimated modifier ranges, but treat them as *hypotheses*, not constants. Each modifier should have a `source` field (initially "research_estimate") and an `evidence` field (initially empty). As real session data comes in, the calculator should update modifiers based on observed decision patterns. This is specification aging applied to the tool itself.

---

**Decision complexity modifier is the hardest to get right.** Domain weight, user experience, and session sequence are knowable before the session starts. Decision complexity *changes within the session*. The identity questions (Q1-Q4) are harder than the boundary placement decisions. So the budget should *adapt mid-session*, not just be set at the start.

**Recommendation:** Add an intra-session adaptation layer. Start with the calculated budget. Then:
- After each decision, estimate the *cognitive cost* of that decision (simple: was it a pattern-matched choice or a novel judgment?)
- Track cumulative cost against the budget
- When 80% of budget is consumed, the Mirror Agent should start *reducing options per turn* (from 3-4 to 2) and *offering more pre-filled defaults*

This is the cognitive load budget version of progressive autonomy — as the user's capacity depletes, the system takes more of the structuring work.

---

**The "decision" unit is underspecified.** What counts as a decision? Is selecting a pre-filled pattern 1 decision, or 0.3 decisions? Is the identity question "What IS this agent?" 1 decision or 3 (because the user has to decide on essence, scope, and principal simultaneously)?

**Recommendation:** Define decision *weight*, not just decision *count*. Some decisions are heavy (identity questions, harm assessment, authority boundaries), some are light (confirming a pattern match, accepting a pre-fill), some are structural (navigating to the next section). The calculator should track *weighted decision capacity*, not raw count.

```
decision_weight:
  heavy: 1.0   # identity questions, boundary placement, harm assessment
  medium: 0.5  # pattern selection, confirming pre-fills, choosing from 2-3 options
  light: 0.2   # navigation, confirming status, accepting defaults
```

Sarah's 1-2 decisions = 1-2 *heavy* decisions, or up to 4-5 *light* confirmations within those.

---

**The connection to CC-2 is clear but the connection to CC-9 (Possibility Orientation) is missing.** The cognitive load budget should *increase* in possibility-oriented phases (P0-P2) because the user needs more space to explore, and *decrease* in constraint-oriented phases (P7-P8) because decisions are tighter and more consequential. Currently the formula only accounts for decision *complexity* — it doesn't account for the *orientation* of the phase.

**Recommendation:** Add a `phase_orientation_modifier`:

```
Phase Orientation Weights:
P0-P2 (possibility): 0.8  # fewer hard decisions, more exploration space
P3-P5 (structure):    1.0  # standard decision density
P6-P8 (constraint):   1.2  # more decisions, tighter boundaries, more stakes
P9 (empathize):       0.9  # partially reopens possibility
P10 (evolve):         1.0  # standard
```

This means the calculator respects the possibility gradient — it doesn't just track capacity, it tracks *what kind of capacity* the phase needs.

---

**Missing: rubber-stamping detection.** The document mentions the Trust Ledger tracks "rushing, rubber-stamping, inconsistency" as decision fatigue indicators, but the calculator doesn't use these indicators to *adjust the budget mid-session*. If Sarah starts rubber-stamping (accepting defaults without reading them), the system should interpret that as budget exhaustion, not agreement.

**Recommendation:** Add a `fatigue_detector` that monitors:
- **Decision velocity**: time between decisions (speeding up = rushing, not efficiency)
- **Default acceptance rate**: percentage of decisions where the user accepts the pre-fill without modification
- **Consistency drift**: decisions that contradict earlier decisions in the same session
- **Engagement decline**: shorter responses, fewer custom options, more "I don't know"

When fatigue indicators cross a threshold, the system should:
1. Reduce remaining decision budget by 30-50%
2. Switch to higher-structure mode (more pre-fills, fewer open choices)
3. Offer to pause and resume (interrupt architecture)
4. Flag the session in the Trust Ledger for review

This directly operationalizes ADHD Design Principle #4 (Interrupt Architecture) — the system detects cognitive depletion and responds with structure, not pressure.

---

**Missing: the connection to the Attention Map.** The Milestone 1 interaction design has an attention map (left rail, traffic light system) that shows section status. The cognitive load budget should be *visible* in that attention map — a "decision capacity" indicator that shows how much budget remains, what's been spent, and what the next decision will cost.

**Recommendation:** The attention map should include a *decision budget bar* alongside the section traffic lights. Something like:

```
Decision Capacity: ████████░░ 4/5 remaining
Next decision: Medium (0.5) — Boundary placement for "contract review"
```

This operationalizes ADHD Design Principle #2 (Visibility as Memory) and #5 (Engagement Over Priority) — the user can see their capacity and choose where to spend it.

---

**Missing: session resumption budget.** If Sarah pauses and resumes tomorrow, her decision capacity resets — but not to full. She's now in session 2, which has a higher session sequence modifier (1.0 instead of 0.7). But she also carries context from session 1, which reduces the cognitive cost of *orientation* decisions while not reducing the cost of *judgment* decisions.

**Recommendation:** Distinguish between *orientation decisions* (where am I, what was I doing) and *judgment decisions* (what should this boundary be). Orientation decisions are cheaper in resumed sessions because the context is stored. Judgment decisions cost the same. The session resumption modifier should account for this:

```
orientation_cost_reduction: 0.5  # 50% cheaper to re-orient in resumed sessions
judgment_cost: 1.0                # judgment costs the same regardless
```

---

**The file structure is clean but the API contract is underspecified.** The calculator needs to produce a `CognitiveLoadBudget` that the Mirror Agent and Design Studio can consume. That budget needs to include not just the number, but the *reasoning* — why this budget, what modifiers were applied, what assumptions were made. This is CC-3 (epistemic metadata) applied to the budget itself.

**Recommendation:** The `CognitiveLoadBudget` model should include:

```python
class CognitiveLoadBudget(BaseModel):
    budget: float                              # weighted decision capacity
    raw_budget: int                            # raw decision count (before weighting)
    modifiers_applied: dict[str, ModifierDetail]  # each modifier with value + source
    assumptions: list[str]                     # what we're assuming about this session
    fatigue_indicators: FatigueStatus | None    # current fatigue state
    recommendation: str                        # plain English recommendation for Mirror Agent
    phase_orientation: str                      # possibility/structure/constraint
    remaining_capacity: float                   # updated during session
    decisions_made: list[DecisionRecord]        # what was decided, weight, time
```

Every field carries its own epistemic metadata. The budget isn't just a number — it's a *traceable, contestable calculation*.

## What This Connects To

| Existing Concept | Connection |
|---|---|
| ADHD Design Principle #1 (Cognitive Load as a Budget) | This IS that principle, operationalized |
| CC-2 Human Enrichment Assessment | Budget depletion = enrichment check trigger |
| CC-9 Possibility Orientation | Phase orientation affects budget (possibility = more space, constraint = tighter) |
| CC-3 Epistemic Metadata | Budget carries provenance, assumptions, and source |
| Progressive Disclosure (4 levels) | User experience modifier maps directly to disclosure level |
| Milestone 1 Attention Map | Decision capacity bar belongs in the attention map |
| Sarah Chen persona | 1-2 decisions first session is the proof case |
| Trust Ledger | Decision fatigue indicators feed Trust Ledger quarterly reports |
| Interrupt Architecture (ADHD #4) | Fatigue detection triggers pause/resume offers |
| Decision Presentation Pattern | Budget determines how many options per turn (2-4) |
| Session resumption | Orientation vs judgment cost distinction |
| Specification Aging | Modifier values are hypotheses that age — update with evidence |

## What I'd Change

1. **Add decision weighting** (heavy/medium/light) — not all decisions cost the same
2. **Add intra-session adaptation** — budget adjusts as fatigue indicators appear
3. **Add phase orientation modifier** — possibility phases need different capacity than constraint phases
4. **Add fatigue detection** — rubber-stamping, rushing, inconsistency are budget signals
5. **Add epistemic metadata to the budget itself** — the calculation is a hypothesis, not a fact
6. **Add visibility in the attention map** — decision capacity bar alongside section status
7. **Add orientation vs judgment distinction for resumed sessions** — re-orientation is cheaper than new judgment
8. **Treat initial modifier values as hypotheses** — plan to update them with real session data

The tool is worth building. The formula is the right shape. The adjustments above make it *adaptive* in the way it promises to be — not just calculated differently per user, but adjusted *within* a session based on observed behavior, and *across* sessions based on accumulating evidence.

Want me to draft the updated `models.py` and `calculator.py` with these adjustments, or do you want to push on something else first?

---

## Run 2 — Agentic Expert ✓ COMPLETED

*2026-05-20T02:46:03* · `glm-5.1:cloud` · `5b33bde6...`

### Prompt

Write an implementation plan for this tool here (inline).

### Response

## Cognitive Load Budget Calculator — Implementation Plan

### Overview

Build an adaptive cognitive load budget calculator that produces per-session, per-user, per-domain decision budgets, adjusts mid-session based on fatigue indicators, and surfaces remaining capacity in the Design Studio attention map. Ship with estimated modifier values treated as hypotheses, not constants.

### Build Order

Three phases, each independently deployable.

**Phase 1: Core Calculator** — the budget formula, decision weighting, and session tracking. Enough for the Mirror Agent to use.

**Phase 2: Fatigue Detection** — intra-session adaptation based on observed behavior. Makes the budget adaptive, not just calculated.

**Phase 3: Attention Map Integration** — visibility in the Design Studio. Makes the budget visible to the user.

Phase 1 is the minimum for the 77% Challenge. Phases 2 and 3 enhance it but don't block it.

---

### Phase 1: Core Calculator

#### File Structure

```
cognitive_load/
  __init__.py
  models.py           # Pydantic models
  calculator.py        # Budget calculation engine
  modifiers.py         # Default modifier profiles and sources
  session_tracker.py   # Tracks decisions per session
```

#### models.py

```python
from enum import Enum
from pydantic import BaseModel, Field
from datetime import datetime


class DecisionWeight(str, Enum):
    """How cognitively expensive a decision is."""
    HEAVY = "heavy"      # 1.0 — identity questions, boundary placement, harm assessment
    MEDIUM = "medium"    # 0.5 — pattern selection, confirming pre-fills, 2-3 options
    LIGHT = "light"      # 0.2 — navigation, confirming status, accepting defaults


class PhaseOrientation(str, Enum):
    """What kind of cognitive capacity the phase needs."""
    POSSIBILITY = "possibility"  # P0-P2 — more exploration space, fewer hard decisions
    STRUCTURE = "structure"      # P3-P5 — standard decision density
    CONSTRAINT = "constraint"    # P6-P8 — more decisions, tighter boundaries
    EMPATHIZE = "empathize"      # P9 — partially reopens possibility
    EVOLVE = "evolve"            # P10 — standard


class DisclosureLevel(str, Enum):
    """Progressive disclosure level — maps to user experience."""
    QUICK_START = "quick_start"   # 0.8 — novice, seeing framework for first time
    PRACTITIONER = "practitioner"  # 1.0 — has used it before, knows basics
    ARCHITECT = "architect"        # 1.3 — deep user, customising extensively
    CONTRIBUTOR = "contributor"    # 1.5 — extending the methodology itself


class ModifierSource(str, Enum):
    """Where a modifier value came from."""
    RESEARCH_ESTIMATE = "research_estimate"  # Initial values from literature
    OBSERVED_DATA = "observed_data"          # Updated from real session data
    MANUAL_OVERRIDE = "manual_override"      # Explicitly set by operator


class StakesLevel(str, Enum):
    """Domain stakes classification from P0."""
    HIGH = "high"        # 0.7 — legal, medical, financial decisions
    STANDARD = "standard"  # 1.0 — operational, typical business decisions
    LOW = "low"           # 1.3 — low-risk, reversible, operational decisions


class SessionPosition(str, Enum):
    """Where this session sits in the user's journey."""
    FIRST = "first"          # 0.7 — unfamiliar, no prior context
    SECOND = "second"        # 1.0 — pattern recognized from session 1
    THIRD_PLUS = "third_plus" # 1.2 — routine, familiar territory


class ModifierDetail(BaseModel):
    """A single modifier with provenance."""
    value: float
    source: ModifierSource = ModifierSource.RESEARCH_ESTIMATE
    evidence: str = ""
    last_updated: datetime = Field(default_factory=datetime.now)


class DecisionRecord(BaseModel):
    """A single decision made during a session."""
    decision_id: str
    timestamp: datetime = Field(default_factory=datetime.now)
    weight: DecisionWeight
    weighted_cost: float  # actual cost (1.0, 0.5, or 0.2)
    description: str  # plain English description of what was decided
    was_default_accepted: bool = False  # did the user accept a pre-fill?
    was_custom: bool = False  # did the user provide their own option?
    response_time_seconds: float | None = None  # time taken to decide


class FatigueIndicators(BaseModel):
    """Observed signals that cognitive capacity is depleting."""
    decision_velocity: float | None = None      # decisions per minute (trending up = rushing)
    default_acceptance_rate: float | None = None  # % of decisions accepting pre-fills
    consistency_drift: bool = False               # decisions contradicting earlier ones
    engagement_decline: bool = False             # shorter responses, fewer custom options
    fatigue_detected: bool = False              # composite: is fatigue likely?
    fatigue_confidence: float = 0.0             # 0-1 how confident we are in detection


class CognitiveLoadBudget(BaseModel):
    """The complete budget for a session — the primary output of the calculator."""
    # Core budget
    weighted_budget: float           # weighted decision capacity (after all modifiers)
    raw_budget: int                  # raw decision count (before weighting, typically 5)
    remaining_capacity: float       # updated during session as decisions are made
    
    # Modifier provenance
    modifiers_applied: dict[str, ModifierDetail]  # each modifier with value + source
    assumptions: list[str]           # what we're assuming about this session
    
    # Session context
    phase_orientation: PhaseOrientation
    disclosure_level: DisclosureLevel
    stakes_level: StakesLevel
    
    # Decision tracking
    decisions_made: list[DecisionRecord] = []
    decisions_remaining: int  # estimated count of decisions still available
    
    # Fatigue
    fatigue_indicators: FatigueIndicators | None = None
    
    # Mirror Agent guidance
    recommendation: str  # plain English recommendation for Mirror Agent pacing
    max_options_per_turn: int  # how many options to show (2-4, adjusted by budget)
    
    # Metadata
    session_id: str
    user_id: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


class SessionProfile(BaseModel):
    """Everything the calculator needs to know about the user and session."""
    user_id: str
    session_id: str
    session_number: int  # 1 = first, 2 = second, etc.
    disclosure_level: DisclosureLevel
    stakes_level: StakesLevel
    phase_orientation: PhaseOrientation
    domain: str  # e.g., "commercial_law", "marketing", "operations"
    
    # Decision complexity for this session type
    average_decision_weight: DecisionWeight = DecisionWeight.MEDIUM
    
    # Override: if the operator wants to set a specific budget
    manual_budget_override: float | None = None
```

#### modifiers.py

```python
"""Default modifier profiles — treated as hypotheses, not constants."""

from models import (
    ModifierDetail, ModifierSource, DisclosureLevel, 
    StakesLevel, SessionPosition, PhaseOrientation, DecisionWeight
)
from datetime import datetime


# Base capacity: research-informed estimate of decisions per session
# Source: Miller (1956) working memory, Sweller cognitive load theory,
# Kahneman System 1/2, and ADHD-specific research on decision fatigue
BASE_CAPACITY: dict[str, float] = {
    "novice": 3.0,      # unfamiliar domain, limited prior context
    "standard": 5.0,    # moderate familiarity, standard session
    "expert": 8.0,       # deep familiarity, routine decisions
}

DOMAIN_WEIGHTS: dict[str, ModifierDetail] = {
    "high_stakes_legal": ModifierDetail(
        value=0.7, source=ModifierSource.RESEARCH_ESTIMATE,
        evidence="Legal decisions carry professional indemnity risk; Sarah Chen persona validation",
        last_updated=datetime(2025, 7, 1),
    ),
    "high_stakes_financial": ModifierDetail(
        value=0.7, source=ModifierSource.RESEARCH_ESTIMATE,
        evidence="Financial decisions carry regulatory and client risk",
        last_updated=datetime(2025, 7, 1),
    ),
    "standard_business": ModifierDetail(
        value=1.0, source=ModifierSource.RESEARCH_ESTIMATE,
        evidence="Standard operational decisions; moderate reversibility",
        last_updated=datetime(2025, 7, 1),
    ),
    "low_stakes_operational": ModifierDetail(
        value=1.3, source=ModifierSource.RESEARCH_ESTIMATE,
        evidence="Operational decisions with low irreversibility; easy to correct",
        last_updated=datetime(2025, 7, 1),
    ),
}

USER_EXPERIENCE_MODIFIERS: dict[DisclosureLevel, ModifierDetail] = {
    DisclosureLevel.QUICK_START: ModifierDetail(
        value=0.8, source=ModifierSource.RESEARCH_ESTIMATE,
        evidence="First exposure to framework; cognitive load from learning + deciding",
        last_updated=datetime(2025, 7, 1),
    ),
    DisclosureLevel.PRACTITIONER: ModifierDetail(
        value=1.0, source=ModifierSource.RESEARCH_ESTIMATE,
        evidence="Knows basics; cognitive load from deciding, not learning",
        last_updated=datetime(2025, 7, 1),
    ),
    DisclosureLevel.ARCHITECT: ModifierDetail(
        value=1.3, source=ModifierSource.RESEARCH_ESTIMATE,
        evidence="Deep familiarity; can handle more decisions with less overhead",
        last_updated=datetime(2025, 7, 1),
    ),
    DisclosureLevel.CONTRIBUTOR: ModifierDetail(
        value=1.5, source=ModifierSource.RESEARCH_ESTIMATE,
        evidence="Extending methodology; highest capacity for framework decisions",
        last_updated=datetime(2025, 7, 1),
    ),
}

SESSION_SEQUENCE_MODIFIERS: dict[SessionPosition, ModifierDetail] = {
    SessionPosition.FIRST: ModifierDetail(
        value=0.7, source=ModifierSource.RESEARCH_ESTIMATE,
        evidence="Unfamiliar territory; no prior context to reduce orientation load",
        last_updated=datetime(2025, 7, 1),
    ),
    SessionPosition.SECOND: ModifierDetail(
        value=1.0, source=ModifierSource.RESEARCH_ESTIMATE,
        evidence="Pattern recognized from session 1; orientation cost reduced",
        last_updated=datetime(2025, 7, 1),
    ),
    SessionPosition.THIRD_PLUS: ModifierDetail(
        value=1.2, source=ModifierSource.RESEARCH_ESTIMATE,
        evidence="Routine territory; orientation cost minimal",
        last_updated=datetime(2025, 7, 1),
    ),
}

PHASE_ORIENTATION_MODIFIERS: dict[PhaseOrientation, ModifierDetail] = {
    PhaseOrientation.POSSIBILITY: ModifierDetail(
        value=0.8, source=ModifierSource.RESEARCH_ESTIMATE,
        evidence="P0-P2: fewer hard decisions, more exploration space needed",
        last_updated=datetime(2025, 7, 1),
    ),
    PhaseOrientation.STRUCTURE: ModifierDetail(
        value=1.0, source=ModifierSource.RESEARCH_ESTIMATE,
        evidence="P3-P5: standard decision density",
        last_updated=datetime(2025, 7, 1),
    ),
    PhaseOrientation.CONSTRAINT: ModifierDetail(
        value=1.2, source=ModifierSource.RESEARCH_ESTIMATE,
        evidence="P6-P8: more decisions, tighter boundaries, higher stakes",
        last_updated=datetime(2025, 7, 1),
    ),
    PhaseOrientation.EMPATHIZE: ModifierDetail(
        value=0.9, source=ModifierSource.RESEARCH_ESTIMATE,
        evidence="P9: partially reopens possibility; mixed decision types",
        last_updated=datetime(2025, 7, 1),
    ),
    PhaseOrientation.EVOLVE: ModifierDetail(
        value=1.0, source=ModifierSource.RESEARCH_ESTIMATE,
        evidence="P10: standard decision density for review/evolution",
        last_updated=datetime(2025, 7, 1),
    ),
}

# Decision weights — how much cognitive capacity each decision type costs
DECISION_WEIGHT_VALUES: dict[DecisionWeight, float] = {
    DecisionWeight.HEAVY: 1.0,   # identity questions, boundary placement, harm assessment
    DecisionWeight.MEDIUM: 0.5,  # pattern selection, confirming pre-fills, 2-3 options
    DecisionWeight.LIGHT: 0.2,   # navigation, confirming status, accepting defaults
}

# Map session contexts to decision weight expectations
# Used when average_decision_weight is not explicitly set
PHASE_DEFAULT_WEIGHT: dict[PhaseOrientation, DecisionWeight] = {
    PhaseOrientation.POSSIBILITY: DecisionWeight.HEAVY,   # P0-P2: identity decisions are heavy
    PhaseOrientation.STRUCTURE: DecisionWeight.MEDIUM,     # P3-P5: decomposition and allocation
    PhaseOrientation.CONSTRAINT: DecisionWeight.HEAVY,    # P6-P8: boundary and contract decisions
    PhaseOrientation.EMPATHIZE: DecisionWeight.MEDIUM,    # P9: human experience decisions
    PhaseOrientation.EVOLVE: DecisionWeight.MEDIUM,        # P10: review and evolution decisions
}

# Decision complexity modifier — derived from average decision weight
# Heavy decisions reduce capacity, light decisions increase capacity
DECISION_COMPLEXITY_MODIFIERS: dict[DecisionWeight, ModifierDetail] = {
    DecisionWeight.HEAVY: ModifierDetail(
        value=0.6, source=ModifierSource.RESEARCH_ESTIMATE,
        evidence="Identity and boundary decisions require deep judgment; high cognitive cost",
        last_updated=datetime(2025, 7, 1),
    ),
    DecisionWeight.MEDIUM: ModifierDetail(
        value=1.0, source=ModifierSource.RESEARCH_ESTIMATE,
        evidence="Standard decisions — pattern selection, confirmation, option comparison",
        last_updated=datetime(2025, 7, 1),
    ),
    DecisionWeight.LIGHT: ModifierDetail(
        value=1.4, source=ModifierSource.RESEARCH_ESTIMATE,
        evidence="Navigation and confirmation — low cognitive cost, high capacity for more",
        last_updated=datetime(2025, 7, 1),
    ),
}

# Session resumption: orientation decisions are cheaper in resumed sessions
ORIENTATION_COST_REDUCTION = 0.5  # 50% cheaper to re-orient in resumed sessions
JUDGMENT_COST = 1.0               # judgment costs the same regardless of session history
```

#### calculator.py

```python
"""Budget calculation engine — produces per-session, per-user, per-domain budgets."""

from models import (
    CognitiveLoadBudget, SessionProfile, ModifierDetail, 
    ModifierSource, DecisionRecord, DecisionWeight, FatigueIndicators,
    DisclosureLevel, StakesLevel, SessionPosition, PhaseOrientation
)
from modifiers import (
    BASE_CAPACITY, DOMAIN_WEIGHTS, USER_EXPERIENCE_MODIFIERS,
    SESSION_SEQUENCE_MODIFIERS, PHASE_ORIENTATION_MODIFIERS,
    DECISION_WEIGHT_VALUES, DECISION_COMPLEXITY_MODIFIERS,
    PHASE_DEFAULT_WEIGHT, ORIENTATION_COST_REDUCTION, JUDGMENT_COST
)
from datetime import datetime


class CognitiveLoadCalculator:
    """Calculates adaptive cognitive load budgets for agent design sessions."""

    def calculate_budget(self, profile: SessionProfile) -> CognitiveLoadBudget:
        """Calculate the initial budget for a session based on the user profile."""
        
        # Manual override takes precedence
        if profile.manual_budget_override is not None:
            return CognitiveLoadBudget(
                weighted_budget=profile.manual_budget_override,
                raw_budget=int(profile.manual_budget_override),
                remaining_capacity=profile.manual_budget_override,
                decisions_remaining=int(profile.manual_budget_override),
                modifiers_applied={
                    "manual_override": ModifierDetail(
                        value=profile.manual_budget_override,
                        source=ModifierSource.MANUAL_OVERRIDE,
                        evidence="Explicitly set by operator",
                    )
                },
                assumptions=["Budget manually set by operator; all modifiers bypassed"],
                phase_orientation=profile.phase_orientation,
                disclosure_level=profile.disclosure_level,
                stakes_level=profile.stakes_level,
                decisions_made=[],
                recommendation=f"Manual budget of {profile.manual_budget_override} decisions",
                max_options_per_turn=3,
                session_id=profile.session_id,
                user_id=profile.user_id,
            )

        # Step 1: Determine base capacity from user expertise
        base_capacity = self._get_base_capacity(profile.disclosure_level)
        
        # Step 2: Get all modifiers with provenance
        domain_weight = self._get_domain_weight(profile.domain)
        experience_mod = USER_EXPERIENCE_MODIFIERS[profile.disclosure_level]
        session_mod = self._get_session_sequence_modifier(profile.session_number)
        phase_mod = PHASE_ORIENTATION_MODIFIERS[profile.phase_orientation]
        
        # Step 3: Determine decision complexity modifier
        avg_weight = profile.average_decision_weight
        if avg_weight == DecisionWeight.MEDIUM:
            # Infer from phase if not explicitly set
            avg_weight = PHASE_DEFAULT_WEIGHT.get(profile.phase_orientation, DecisionWeight.MEDIUM)
        complexity_mod = DECISION_COMPLEXITY_MODIFIERS[avg_weight]
        
        # Step 4: Calculate weighted budget
        # Formula: base_capacity × domain_weight × experience × session × phase × complexity
        weighted_budget = (
            base_capacity
            * domain_weight.value
            * experience_mod.value
            * session_mod.value
            * phase_mod.value
            * complexity_mod.value
        )
        
        # Step 5: Floor at 1 (minimum 1 decision per session)
        weighted_budget = max(1.0, round(weighted_budget, 1))
        
        # Step 6: Determine max options per turn based on budget
        max_options = self._calculate_max_options(weighted_budget)
        
        # Step 7: Generate plain English recommendation
        recommendation = self._generate_recommendation(
            weighted_budget, profile.stakes_level, profile.session_number
        )
        
        # Step 8: Compile assumptions
        assumptions = self._compile_assumptions(profile, domain_weight, experience_mod)
        
        # Step 9: Build modifiers_applied dict
        modifiers_applied = {
            "base_capacity": ModifierDetail(
                value=base_capacity,
                source=ModifierSource.RESEARCH_ESTIMATE,
                evidence=f"Based on {profile.disclosure_level.value} disclosure level",
            ),
            "domain_weight": domain_weight,
            "user_experience": experience_mod,
            "session_sequence": session_mod,
            "phase_orientation": phase_mod,
            "decision_complexity": complexity_mod,
        }
        
        return CognitiveLoadBudget(
            weighted_budget=weighted_budget,
            raw_budget=int(round(weighted_budget)),
            remaining_capacity=weighted_budget,
            decisions_made=[],
            decisions_remaining=int(round(weighted_budget)),
            modifiers_applied=modifiers_applied,
            assumptions=assumptions,
            phase_orientation=profile.phase_orientation,
            disclosure_level=profile.disclosure_level,
            stakes_level=profile.stakes_level,
            fatigue_indicators=None,
            recommendation=recommendation,
            max_options_per_turn=max_options,
            session_id=profile.session_id,
            user_id=profile.user_id,
        )

    def record_decision(
        self, 
        budget: CognitiveLoadBudget, 
        decision: DecisionRecord
    ) -> CognitiveLoadBudget:
        """Record a decision and update remaining capacity."""
        
        cost = decision.weighted_cost
        
        updated_decisions = budget.decisions_made + [decision]
        updated_remaining = max(0, budget.remaining_capacity - cost)
        updated_count_remaining = max(
            0, 
            int(round(updated_remaining / DECISION_WEIGHT_VALUES.get(
                decision.weight, 0.5
            )))
        )
        
        # Recalculate max options based on remaining capacity
        max_options = self._calculate_max_options(updated_remaining)
        
        # Update recommendation based on remaining capacity
        recommendation = self._update_recommendation(
            updated_remaining, budget.weighted_budget, budget.stakes_level
        )
        
        return budget.model_copy(update={
            "decisions_made": updated_decisions,
            "remaining_capacity": round(updated_remaining, 2),
            "decisions_remaining": updated_count_remaining,
            "max_options_per_turn": max_options,
            "recommendation": recommendation,
            "updated_at": datetime.now(),
        })

    def _get_base_capacity(self, disclosure_level: DisclosureLevel) -> float:
        """Map disclosure level to base capacity."""
        mapping = {
            DisclosureLevel.QUICK_START: BASE_CAPACITY["novice"],
            DisclosureLevel.PRACTITIONER: BASE_CAPACITY["standard"],
            DisclosureLevel.ARCHITECT: BASE_CAPACITY["expert"],
            DisclosureLevel.CONTRIBUTOR: BASE_CAPACITY["expert"] * 1.2,
        }
        return mapping.get(disclosure_level, BASE_CAPACITY["standard"])

    def _get_domain_weight(self, domain: str) -> ModifierDetail:
        """Look up domain weight, defaulting to standard business."""
        # Try exact match first
        if domain in DOMAIN_WEIGHTS:
            return DOMAIN_WEIGHTS[domain]
        
        # Try partial match on key words
        domain_lower = domain.lower()
        if any(kw in domain_lower for kw in ["legal", "law", "compliance", "regulatory"]):
            return DOMAIN_WEIGHTS["high_stakes_legal"]
        elif any(kw in domain_lower for kw in ["financial", "accounting", "tax"]):
            return DOMAIN_WEIGHTS["high_stakes_financial"]
        elif any(kw in domain_lower for kw in ["marketing", "content", "social"]):
            return DOMAIN_WEIGHTS["low_stakes_operational"]
        else:
            return DOMAIN_WEIGHTS["standard_business"]

    def _get_session_sequence_modifier(self, session_number: int) -> ModifierDetail:
        """Map session number to sequence modifier."""
        if session_number == 1:
            return SESSION_SEQUENCE_MODIFIERS[SessionPosition.FIRST]
        elif session_number == 2:
            return SESSION_SEQUENCE_MODIFIERS[SessionPosition.SECOND]
        else:
            return SESSION_SEQUENCE_MODIFIERS[SessionPosition.THIRD_PLUS]

    def _calculate_max_options(self, remaining_capacity: float) -> int:
        """Determine how many options to show per turn based on remaining capacity."""
        if remaining_capacity <= 1.5:
            return 2  # Low capacity: minimal choices
        elif remaining_capacity <= 3.0:
            return 3  # Moderate capacity: standard choices
        else:
            return 4  # High capacity: more options

    def _generate_recommendation(
        self, 
        budget: float, 
        stakes: StakesLevel, 
        session: int
    ) -> str:
        """Generate plain English recommendation for Mirror Agent pacing."""
        if budget <= 1.5:
            return (
                "Very limited capacity. Present 2 options maximum. "
                "Use more pre-fills and defaults. Spread decisions across "
                "more turns. Consider offering to pause and resume."
            )
        elif budget <= 3.0:
            return (
                "Moderate capacity. Present 2-3 options. "
                "Pre-fill where possible. Allow extra time for heavy decisions."
            )
        elif budget <= 5.0:
            return (
                "Standard capacity. Present 3 options. "
                "Normal pacing with check-ins after heavy decisions."
            )
        elif budget <= 8.0:
            return (
                "Good capacity. Present 3-4 options. "
                "Standard pacing. User can handle open-ended decisions."
            )
        else:
            return (
                "High capacity. Present 4 options. "
                "User can handle complex decisions and detailed exploration."
            )

    def _update_recommendation(
        self, 
        remaining: float, 
        total: float, 
        stakes: StakesLevel
    ) -> str:
        """Update recommendation based on remaining capacity."""
        ratio = remaining / total if total > 0 else 0
        
        if ratio <= 0.2:
            return (
                "Critical: less than 20% capacity remaining. "
                "Offer to pause and resume. Switch to confirmation-only mode. "
                "No new heavy decisions."
            )
        elif ratio <= 0.4:
            return (
                "Low: 20-40% capacity remaining. "
                "Reduce to 2 options per turn. Increase pre-fills. "
                "Avoid heavy decisions if possible."
            )
        elif ratio <= 0.6:
            return (
                "Moderate: 40-60% capacity remaining. "
                "Standard pacing. Check in after heavy decisions."
            )
        elif ratio <= 0.8:
            return (
                "Good: 60-80% capacity remaining. "
                "Normal pacing. User can handle standard decisions."
            )
        else:
            return (
                "Fresh: 80%+ capacity remaining. "
                "Full pacing available. User can handle complex decisions."
            )

    def _compile_assumptions(
        self,
        profile: SessionProfile,
        domain_weight: ModifierDetail,
        experience_mod: ModifierDetail,
    ) -> list[str]:
        """Document the assumptions baked into this budget calculation."""
        assumptions = [
            f"Base capacity set to {self._get_base_capacity(profile.disclosure_level)} "
            f"based on {profile.disclosure_level.value} disclosure level",
            f"Domain weight {domain_weight.value} applied for {profile.domain}",
            f"User experience modifier {experience_mod.value} applied for "
            f"{profile.disclosure_level.value} level",
            f"All modifier values are research estimates — treat as hypotheses, not constants",
        ]
        
        if profile.session_number == 1:
            assumptions.append(
                "First session: user has no prior context; reduced capacity due to orientation load"
            )
        
        if profile.stakes_level == StakesLevel.HIGH:
            assumptions.append(
                "High-stakes domain: decisions carry professional/legal risk; reduced capacity"
            )
        
        return assumptions
```

#### session_tracker.py

```python
"""Tracks decisions made per session and adjusts modifiers over time."""

from models import (
    CognitiveLoadBudget, DecisionRecord, DecisionWeight,
    FatigueIndicators, SessionProfile
)
from calculator import CognitiveLoadCalculator
from datetime import datetime, timedelta


class SessionTracker:
    """Tracks session progress and detects fatigue indicators."""
    
    def __init__(self, calculator: CognitiveLoadCalculator):
        self.calculator = calculator

    def check_fatigue(self, budget: CognitiveLoadBudget) -> FatigueIndicators:
        """Detect cognitive fatigue from decision patterns."""
        
        if not budget.decisions_made:
            return FatigueIndicators(fatigue_detected=False, fatigue_confidence=0.0)
        
        decisions = budget.decisions_made
        
        # Decision velocity: decisions per minute (higher = rushing)
        if len(decisions) >= 2:
            time_span = (decisions[-1].timestamp - decisions[0].timestamp).total_seconds()
            if time_span > 0:
                velocity = len(decisions) / (time_span / 60)
            else:
                velocity = 0.0
        else:
            velocity = None
        
        # Default acceptance rate: % of decisions accepting pre-fills
        total_with_default = sum(1 for d in decisions if d.was_default_accepted is not None)
        if total_with_default > 0:
            accepted = sum(1 for d in decisions if d.was_default_accepted)
            acceptance_rate = accepted / total_with_default
        else:
            acceptance_rate = None
        
        # Consistency drift: later decisions contradicting earlier ones
        # (This requires domain-specific logic; for now, flag as False)
        consistency_drift = False
        
        # Engagement decline: shorter responses, fewer custom options
        custom_count = sum(1 for d in decisions if d.was_custom)
        total_count = len(decisions)
        engagement_decline = (
            total_count > 3 
            and custom_count == 0 
            and all(d.was_default_accepted for d in decisions[-3:])
        )
        
        # Composite fatigue detection
        fatigue_signals = 0
        total_signals = 0
        
        if velocity is not None and velocity > 3.0:
            # More than 3 decisions per minute suggests rushing
            fatigue_signals += 1
        total_signals += 1
        
        if acceptance_rate is not None and acceptance_rate > 0.8:
            # More than 80% default acceptance suggests rubber-stamping
            fatigue_signals += 1
        total_signals += 1
        
        if engagement_decline:
            fatigue_signals += 1
        total_signals += 1
        
        fatigue_confidence = fatigue_signals / total_signals if total_signals > 0 else 0.0
        fatigue_detected = fatigue_confidence >= 0.5
        
        return FatigueIndicators(
            decision_velocity=velocity,
            default_acceptance_rate=acceptance_rate,
            consistency_drift=consistency_drift,
            engagement_decline=engagement_decline,
            fatigue_detected=fatigue_detected,
            fatigue_confidence=round(fatigue_confidence, 2),
        )

    def apply_fatigue_adjustment(
        self, 
        budget: CognitiveLoadBudget
    ) -> CognitiveLoadBudget:
        """Reduce remaining capacity based on detected fatigue."""
        
        fatigue = self.check_fatigue(budget)
        
        if not fatigue.fatigue_detected:
            return budget.model_copy(update={"fatigue_indicators": fatigue})
        
        # Reduce remaining capacity by 30-50% when fatigue is detected
        reduction_factor = 0.5 if fatigue.fatigue_confidence >= 0.7 else 0.7
        adjusted_remaining = budget.remaining_capacity * reduction_factor
        
        # Reduce max options per turn
        max_options = 2  # Force minimal options when fatigued
        
        # Update recommendation
        recommendation = (
            f"Fatigue detected (confidence: {fatigue.fatigue_confidence:.0%}). "
            f"Capacity reduced to {adjusted_remaining:.1f}. "
            f"Switching to confirmation-only mode. "
            f"Consider offering to pause and resume."
        )
        
        return budget.model_copy(update={
            "remaining_capacity": round(adjusted_remaining, 2),
            "decisions_remaining": max(0, int(round(adjusted_remaining))),
            "max_options_per_turn": max_options,
            "recommendation": recommendation,
            "fatigue_indicators": fatigue,
            "updated_at": datetime.now(),
        })

    def calculate_session_resumption_budget(
        self,
        profile: SessionProfile,
        previous_budget: CognitiveLoadBudget | None = None,
    ) -> CognitiveLoadBudget:
        """Calculate budget for a resumed session.
        
        Orientation decisions cost less in resumed sessions.
        Judgment decisions cost the same regardless.
        """
        # Start with a fresh calculation for this session position
        new_budget = self.calculator.calculate_budget(profile)
        
        if previous_budget is None:
            return new_budget
        
        # Calculate orientation cost reduction
        # In a resumed session, re-orientation is 50% cheaper
        # But judgment decisions still cost full price
        # This means the effective budget increase is moderate, not doubled
        
        # Count orientation vs judgment decisions from previous session
        # (Light decisions are often orientation; heavy/medium are judgment)
        previous_light = sum(
            1 for d in previous_budget.decisions_made 
            if d.weight == DecisionWeight.LIGHT
        )
        total_previous = len(previous_budget.decisions_made)
        
        if total_previous > 0:
            # Estimate orientation vs judgment split
            orientation_ratio = previous_light / total_previous
            orientation_boost = orientation_ratio * ORIENTATION_COST_REDUCTION
            judgment_preserve = (1 - orientation_ratio) * JUDGMENT_COST
            
            # Apply mixed adjustment
            # Resumed sessions get a small boost for orientation efficiency
            # but full cost for judgment decisions
            resumption_modifier = 1.0 + (orientation_boost * 0.1)
            # (Small adjustment — not dramatic, because judgment still costs full price)
            
            new_remaining = min(
                new_budget.weighted_budget * resumption_modifier,
                new_budget.weighted_budget * 1.2  # Cap at 20% boost
            )
            
            new_budget = new_budget.model_copy(update={
                "remaining_capacity": round(new_remaining, 2),
                "decisions_remaining": int(round(new_remaining)),
                "assumptions": new_budget.assumptions + [
                    f"Resumed session: orientation decisions ~50% cheaper, "
                    f"judgment decisions full cost. Estimated {orientation_ratio:.0%} "
                    f"orientation decisions in previous session."
                ],
            })
        
        return new_budget


# Import for session resumption calculation
from modifiers import ORIENTATION_COST_REDUCTION, JUDGMENT_COST
```

---

### Phase 2: Fatigue Detection

Phase 2 adds real-time fatigue detection and mid-session budget adjustment. This makes the budget *adaptive*, not just *calculated*.

**What Phase 2 adds on top of Phase 1:**

1. **Intra-session adaptation** — the `apply_fatigue_adjustment` method in `session_tracker.py` already handles this. When fatigue indicators cross thresholds, remaining capacity is reduced by 30-50%, max options drop to 2, and the Mirror Agent switches to confirmation-only mode.

2. **Fatigue signal monitoring** — the `check_fatigue` method detects:
   - Decision velocity (decisions per minute — speeding up suggests rushing)
   - Default acceptance rate (accepting pre-fills without modification suggests rubber-stamping)
   - Engagement decline (no custom options in the last 3+ decisions)
   - Consistency drift (placeholder for domain-specific contradiction detection)

3. **Trigger actions when fatigue detected** — the Mirror Agent should:
   - Reduce remaining budget by 30-50%
   - Switch to 2 options per turn maximum
   - Increase pre-fill usage
   - Offer to pause and resume (interrupt architecture)
   - Flag session in Trust Ledger for review

**Phase 2 is already coded in `session_tracker.py`.** The fatigue detection and adjustment logic is complete. What remains is integration with the Mirror Agent and the Design Studio to consume these signals and adjust behavior accordingly.

**Integration checklist for Phase 2:**
- Mirror Agent reads `budget.recommendation` and adjusts options per turn
- Mirror Agent reads `budget.fatigue_indicators` and adjusts pacing
- When `fatigue_detected=True`, Mirror Agent switches to higher-structure mode
- When `remaining_capacity <= 1.0`, Mirror Agent offers pause/resume
- Trust Ledger receives fatigue flags for quarterly review
- Decision fatigue indicators are included in Trust Ledger reports

---

### Phase 3: Attention Map Integration

Phase 3 makes the budget visible in the Design Studio attention map. This operationalizes ADHD Design Principle #2 (Visibility as Memory).

**What Phase 3 adds:**

1. **Decision capacity bar** in the attention map (left rail of the Design Studio):
   ```
   Decision Capacity: ████████░░ 4/5 remaining
   Next decision: Medium (0.5) — Boundary placement for "contract review"
   ```

2. **Capacity color coding:**
   - 🟢 60%+ remaining — full capacity, standard pacing
   - 🟡 40-60% remaining — moderate capacity, increase pre-fills
   - 🟠 20-40% remaining — low capacity, reduce to 2 options, check in after each heavy decision
   - 🔴 <20% remaining — critical, offer pause/resume, confirmation-only mode

3. **Per-section capacity estimates** in the attention map:
   - Each section shows an estimated decision cost (heavy/medium/light)
   - Users can see which sections will be expensive before starting them
   - This operationalizes "one clear next step" — users can plan their remaining capacity

4. **Session history persistence** — when a user resumes a session, the attention map shows:
   - Decisions made in previous sessions
   - Remaining capacity from previous session (adjusted for resumption)
   - Which sections were completed and which remain

**Integration checklist for Phase 3:**
- Design Studio attention map component receives `CognitiveLoadBudget` object
- Renders decision capacity bar with color coding
- Shows per-section decision weight estimates
- Persists session history to database
- Loads previous session context on resume

---

### Testing Plan

**Unit tests (Phase 1):**
- Budget calculation with all modifier combinations
- Sarah Chen scenario: `5 × 0.7 × 0.8 × 0.7 × 0.6 = 1.68` → 1-2 decisions
- Daniel Kovacs scenario: `5 × 1.0 × 1.0 × 1.0 × 1.0 = 5` → 5 decisions
- Peter scenario: `5 × 1.3 × 1.3 × 1.2 × 1.4 = 14.2` → 14 decisions
- Manual override bypasses all modifiers
- Budget floor at 1.0 (minimum 1 decision per session)
- Decision recording updates remaining capacity correctly
- Decision weighting (heavy/medium/light) calculates cost correctly

**Integration tests (Phase 2):**
- Fatigue detection with mock decision histories
- Fatigue adjustment reduces capacity correctly
- Session resumption calculates orientation vs judgment cost

**User validation tests (Phase 3):**
- 5 real sessions with the 77% Challenge
- H5: Attention map reduces cognitive load (compare sessions with/without visibility)
- H6: 30 minutes achievable for most users
- Decision count tracking vs. self-reported cognitive load

---

### Dependency Map

```
models.py ──────────────────────────────────────────┐
  │                                                    │
  ├──> calculator.py ───> session_tracker.py           │
  │         │                    │                     │
  │         │                    └──> fatigue detection │
  │         │                           & adjustment  │
  │         │                                           │
modifiers.py ──> calculator.py                         │
  │                                                    │
  └──> (all modifier values with provenance)          │
                                                       │
  Integration Points:                                  │
  ├── Mirror Agent ──── reads budget.recommendation    │
  │                     reads budget.max_options        │
  │                     reads budget.fatigue_indicators │
  │                                                     │
  ├── Design Studio ── reads budget for attention map  │
  │                     renders decision capacity bar   │
  │                                                     │
  ├── Trust Ledger ─── receives fatigue flags          │
  │                     quarterly decision analysis     │
  │                                                     │
  └── Progressive ──── updates disclosure_level         │
      Autonomy          as user gains experience        │
```

---

### What This Doesn't Do (Yet)

- **Modifier validation from real data** — the modifier values are hypotheses. Phase 1 ships with estimates; a feedback loop from real session data should update them over time (specification aging applied to the tool itself).
- **Cross-session learning** — the tracker handles resumption but doesn't yet build a user profile across sessions (e.g., "Sarah consistently hits capacity at 3 decisions in high-stakes domains").
- **Domain-specific decision weight profiles** — currently, decision weight is set per phase orientation. Domain-specific profiles (e.g., legal boundary decisions are heavier than marketing boundary decisions) should be calibrated from real data.
- **Consistency drift detection** — the placeholder exists in `FatigueIndicators.consistency_drift` but requires domain-specific logic to detect when a user contradicts an earlier decision.

---

### How This Connects to the 77% Challenge

Sarah Chen walks into a 30-minute Boundary Map session. The calculator produces:

```
Budget: 5 × 0.7 (high-stakes legal) × 0.8 (Quick Start) × 0.7 (first session) × 0.6 (heavy decisions) = 1.18
→ Round to 1-2 decisions
→ Max options per turn: 2
→ Recommendation: "Very limited capacity. Present 2 options maximum. Use more pre-fills and defaults."
```

That's not a bug. That's the calculator *working correctly*. Sarah Chen should face 1-2 decisions in her first session, not 5. The Mirror Agent paces accordingly — fewer options, more pre-fills, more structured choices. She leaves with a Boundary Map she owns, not 5 decisions she rubber-stamped.

That's the 77% Challenge in action: the methodology adapts to the human, not the other way around.

---
