<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# now what data structure would be needed if I wanted users to be able to view, add and manage details rather than enter and edit big blocks of formatted text?

Great question — this is the shift from a *document editor* to a *structured data application*. Instead of one big markdown blob per section, you decompose each section into discrete, typed fields that can be rendered, edited, and queried independently.

Here's how each section of the business plan maps to a structured data model:

***

## Core Design Principle

Each business plan **section becomes its own table/entity**, linked back to a parent `BusinessPlan` record. Fields are typed (string, number, date, enum, boolean) rather than freeform text — with the exception of a few intentionally narrative fields like `rationale` or `description`.

***

## Revised Data Model

### `BusinessPlan` *(parent record)*

```
BusinessPlan {
  id: uuid
  name: string               // "Futures Edge Business Plan v1"
  status: enum [draft, active, archived]
  version: integer
  createdAt: timestamp
  updatedAt: timestamp
}
```

Everything else hangs off this via `businessPlanId`.

***

### `CompanyProfile` *(1:1 with BusinessPlan)*

Replaces the freeform company description section.

```
CompanyProfile {
  id: uuid
  businessPlanId: uuid
  legalName: string
  tradingName: string
  legalStructure: enum [sole_trader, pty_ltd, partnership, trust, social_enterprise, ngo]
  abn: string | null
  foundedDate: date | null
  headquartersCity: string
  headquartersState: string
  website: string | null
  mission: text
  vision: text
  tagline: string | null
  socialEnterpriseStatus: boolean
}
```


***

### `Founder[]` *(many per BusinessPlan)*

```
Founder {
  id: uuid
  businessPlanId: uuid
  fullName: string
  title: string
  bio: text
  linkedInUrl: string | null
  strengths: string[]        // e.g. ["Futuristic", "Strategic", "Activator"]
  primaryRole: string        // "Vision & Communication" / "Systems & Implementation"
  photoUrl: string | null
}
```


***

### `Value[]` *(many per BusinessPlan)*

Simple but important — renders as a scannable list, not a paragraph.

```
Value {
  id: uuid
  businessPlanId: uuid
  title: string              // "Human flourishing first"
  description: text
  displayOrder: integer
}
```


***

### `ProductService[]` *(many per BusinessPlan)*

Replaces the service architecture prose.

```
ProductService {
  id: uuid
  businessPlanId: uuid
  name: string               // "AI with Confidence"
  stream: enum [training, consulting, community, job_board, other]
  description: text
  format: string             // "Online cohort, 6 weeks"
  deliveryMode: enum [onsite, online, hybrid]
  targetSegment: string[]    // FK refs to Segment[] or just labels
  priceMin: number | null
  priceMax: number | null
  currency: string           // "AUD"
  pricingModel: enum [fixed, per_person, retainer, subscription, listing_fee]
  status: enum [concept, piloting, active, retired]
  isProprietaryIP: boolean
}
```


***

### `MarketSegment[]` *(many per BusinessPlan)*

Each of the four customer groups becomes a discrete record.

```
MarketSegment {
  id: uuid
  businessPlanId: uuid
  name: string               // "Career Professionals"
  personaName: string        // "Capable Claire"
  personaTagline: text
  problemStatement: text
  goal: text
  triggers: string[]         // bullet list of triggers
  rootCauses: string[]
  impacts: string[]
  currentWorkarounds: string[]
  ageRange: string | null
  incomeRangeMin: number | null
  incomeRangeMax: number | null
  geographicScope: string[]
  priorityRank: integer      // 1 = highest priority
}
```


***

### `Competitor[]` *(many per BusinessPlan)*

```
Competitor {
  id: uuid
  businessPlanId: uuid
  name: string
  type: enum [big_firm, online_platform, influencer, specialist_consultant, other]
  theirStrength: text
  theirWeakness: text
  ourAdvantage: text
  threatLevel: enum [low, medium, high, critical]
}
```


***

### `SwotItem[]` *(many per BusinessPlan)*

Rather than one SWOT table, each item is a discrete record — queryable, taggable, and usable in the TOWS matrix.

```
SwotItem {
  id: uuid
  businessPlanId: uuid
  quadrant: enum [strength, weakness, opportunity, threat]
  dimension: enum [internal, external]
  title: string
  description: text
  severity: enum [low, medium, high]    // for W/T; magnitude for S/O
  isMitigated: boolean                  // for W/T
  relatedStrategyIds: uuid[]            // FK → Strategy[]
  tags: string[]
}
```


***

### `StrategicInitiative[]` *(many per BusinessPlan — replaces TOWS strategies)*

```
StrategicInitiative {
  id: uuid
  businessPlanId: uuid
  title: string
  description: text
  towsQuadrant: enum [SO, WO, ST, WT]  // which TOWS cell it came from
  horizon: enum [short, medium, long]
  status: enum [proposed, active, paused, complete, abandoned]
  relatedSwotIds: uuid[]               // which SWOT items it addresses
  owner: string | null
  targetDate: date | null
}
```


***

### `RevenueStream[]` *(many per BusinessPlan)*

```
RevenueStream {
  id: uuid
  businessPlanId: uuid
  productServiceId: uuid | null       // FK → ProductService
  label: string                       // "NFP Cohort Training"
  year: integer                       // 1, 2, 3
  projectedVolume: number
  unitValue: number
  currency: string
  projectedRevenue: number            // computed: volume × unitValue
  notes: text | null
}
```


***

### `CostItem[]` *(many per BusinessPlan)*

```
CostItem {
  id: uuid
  businessPlanId: uuid
  category: enum [infrastructure, marketing, legal, staffing, travel, software, other]
  label: string
  year: integer
  amount: number
  currency: string
  isRecurring: boolean
  frequency: enum [one_off, monthly, quarterly, annual] | null
  notes: text | null
}
```


***

### `TeamMember[]` *(planned hires — many per BusinessPlan)*

```
TeamMember {
  id: uuid
  businessPlanId: uuid
  role: string                        // "Part-time Operations/BD"
  employmentType: enum [full_time, part_time, contractor, advisor]
  plannedStartMonth: integer          // months from launch
  rationale: text
  annualCostEstimate: number | null
  isHired: boolean
}
```


***

### `Milestone[]` *(many per BusinessPlan)*

```
Milestone {
  id: uuid
  businessPlanId: uuid
  title: string
  description: text | null
  horizon: enum [short, medium, long]  // 0-12m, 1-3y, 3-5y
  targetDate: date | null
  status: enum [not_started, in_progress, complete, at_risk, deferred]
  isUrgent: boolean
  relatedInitiativeId: uuid | null
}
```


***

### `PlanGap[]` *(transparency layer — unique to your use case)*

Based on your ideation doc, this tracks known unknowns explicitly — rather than embedding caveats in prose.

```
PlanGap {
  id: uuid
  businessPlanId: uuid
  section: string              // "Pricing", "Legal Structure", "Funding"
  description: text            // what is missing
  filledByAI: boolean          // true = AI estimate, needs validation
  aiEstimate: text | null      // what the AI guessed
  resolvedAt: date | null
  resolvedNote: text | null
}
```


***

## Entity Map

```
BusinessPlan (1)
 ├── CompanyProfile (1:1)
 ├── Founder[] (1:many)
 ├── Value[] (1:many)
 ├── ProductService[] (1:many)
 │    └── RevenueStream[] (references ProductService)
 ├── MarketSegment[] (1:many)
 ├── Competitor[] (1:many)
 ├── SwotItem[] (1:many)
 │    └── StrategicInitiative[] (references SwotItem[])
 ├── RevenueStream[] (1:many)
 ├── CostItem[] (1:many)
 ├── TeamMember[] (1:many)
 ├── Milestone[] (1:many)
 │    └── ActionItem[] (from previous model)
 └── PlanGap[] (1:many)
```

The `Goal`, `ProgressUpdate`, `DecisionLog`, and `ActionItem` models from the earlier conversation sit **above** the plan layer — they reference the plan but belong to the broader dashboard, not just the plan document.

***

## What This Unlocks in the UI

- **Segment cards** — each persona is a swipeable card, not a wall of text
- **SWOT board** — drag-and-drop quadrant view, each item editable in a drawer
- **Revenue calculator** — live total updates as you change volume/unit values
- **Competitor table** — sortable by threat level, filterable by type
- **Milestone tracker** — timeline/kanban view, status chips, urgency flags
- **Gap register** — a living list of known unknowns with AI-filled vs. validated status

Want to start building the UI from here, or refine any of these models further first?

