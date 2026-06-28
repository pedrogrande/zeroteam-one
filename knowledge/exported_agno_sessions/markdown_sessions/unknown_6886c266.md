# unknown

| Field | Value |
|-------|-------|
| **Session** | `6886c266...` |
| **Type** | team |
| **Agent** | unknown |
| **User** | pete@peterargent.com |
| **Created** | 2026-04-20T01:56:01 |
| **Runs** | 7 completed / 7 total |

## Run 1 — Elinor Ostrom ✓ COMPLETED

*2026-04-20T01:56:03* · `glm-5.1:cloud` · `55e2daa0...`

### Prompt

You are participating in Round 1 of an economics panel. The question is: **How should a community govern a shared digital resource?** Please give your substantive take from your own intellectual lens. Draw on your core ideas and frameworks. Do not reference other panelists yet — that comes in Round 2. Aim for depth (300-500 words), preserve your distinctive voice, and offer concrete principles or mechanisms where possible.

### Response

When I first encountered Garrett Hardin's grim projection about the commons, I was puzzled — because the communities I studied had governed shared pastures, forests, and irrigation systems for *centuries* without collapse. The same challenge now confronts us in the digital realm, and I believe the starting point must be the same: refuse the assumption that shared resources inevitably degrade.

A digital resource — whether an open-source codebase, a data commons, or a collaborative knowledge platform — is still a *common-pool resource* in the sense that exclusion is difficult and one user's misuse can degrade the whole. But the institutional arrangements that sustain it will not be identical to those governing Swiss alpine meadows or Spanish *huertas*. We must do the hard empirical work of understanding what actually emerges on the ground.

That said, my eight design principles for robust commons institutions offer a starting scaffolding. First, *clearly defined boundaries* — who is a contributor, user, or maintainer must be apparent, even in digital spaces where membership is fluid. Wikipedia's编辑社区, for instance, has developed elaborate role hierarchies and norms around who can edit what. Second, *congruence between rules and local conditions* — the governance rules must fit the specific digital ecology. A real-time collaborative document needs different rules than a slowly evolving software repository.

Third, and critically, *collective-choice arrangements* — those affected by the rules must be able to modify them. Top-down platform governance by corporate owners often violates this principle, leaving users alienated from the rule-making process. Fourth, *effective monitoring* — in digital spaces this often means version control, edit histories, and automated tooling, but also community members who watch for degradation. Fifth, *graduated sanctions* — Wikipedia's warning system before blocks, or open-source communities' escalating responses to bad actors, mirror what I found in fishing communities. Sixth, *conflict-resolution mechanisms* that are low-cost and accessible. Seventh, *minimal recognition of rights to organize* — external authorities must not crush self-governance. And eighth, for larger systems, *polycentric governance* — nested layers of authority, from small working groups up to foundational governance.

The digital domain introduces fascinating complications: scale is different, identity is fluid, and resources can be non-rivalrous in ways pastures never were. But the fundamental insight holds — communities *can* self-organize, given the right institutional foundations. The question is never whether to govern, but *how*, and by whom.

---

## Run 2 — Ronald Coase ✓ COMPLETED

*2026-04-20T01:56:03* · `glm-5.1:cloud` · `8c0f8f20...`

### Prompt

You are participating in Round 1 of an economics panel. The question is: **How should a community govern a shared digital resource?** Please give your substantive take from your own intellectual lens. Draw on your core ideas and frameworks. Do not reference other panelists yet — that comes in Round 2. Aim for depth (300-500 words), preserve your distinctive voice, and offer concrete principles or mechanisms where possible.

### Response

How should a community govern a shared digital resource? The question, as usual, is *compared to what alternative* and *at what cost*?

I begin with what I've always insisted upon: the nature of the firm, or any organization, is to reduce transaction costs that would otherwise make coordination through market exchange prohibitively expensive. A shared digital resource—a protocol, a data commons, an open-source repository—exists precisely because market contracting for every individual contribution and use would drown the participants in negotiation, measurement, and enforcement costs. The organization emerges to bring these activities under some form of administrative coordination instead.

But here we must be precise about what *kind* of resource this is, for that determines the property rights at stake. If the resource is non-rival—my use of an open protocol doesn't diminish yours—the governance problem is principally about *production and maintenance*, not allocation. Who contributes? How are contributions verified? Who decides what changes are accepted? These are transaction cost problems, and the answers determine whether you need a benevolent dictator, a committee, or a voting mechanism.

The governing principles I would propose:

**First, clarify the property rights.** Ambiguity about who holds what decision rights generates conflict, and conflict is costly. Every governance dispute that cannot be resolved by reference to a clear rule must be resolved by negotiation or coercion—both expensive. The community should specify, at the outset, who can propose changes, who approves them, and how rights can be modified.

**Second, match governance structure to transaction cost profile.** A small group of known contributors can coordinate through informal bargaining—transaction costs are low, and elaborate mechanisms are wasteful. A large, anonymous community faces escalating coordination costs and will require more formal structure: delegation, voting, perhaps even hierarchy. There is no one-size-fits-all; the optimal institution depends on the actual costs of transacting under the specific conditions the community faces.

**Third, preserve low-cost exit.** When users can fork the resource or leave at minimal cost, the threat of exit disciplines governance more effectively than any internal mechanism. Governance becomes most consequential—and most in need of formal constraints—when switching costs are high and members are effectively locked in.

**Fourth, internalize the externalities.** Free-riding on maintenance, holdout problems on upgrades, pollution of shared standards—these are all instances where private costs diverge from social costs. Governance must address them, but always ask: does the proposed rule cost less than the externality it corrects?

The real world does not present us with ideal arrangements. It presents us with choices between imperfect alternatives, each bearing different costs.

---

## Run 3 — Vitalik Buterin ✓ COMPLETED

*2026-04-20T01:56:03* · `glm-5.1:cloud` · `c61e3243...`

### Prompt

You are participating in Round 1 of an economics panel. The question is: **How should a community govern a shared digital resource?** Please give your substantive take from your own intellectual lens. Draw on your core ideas and frameworks. Do not reference other panelists yet — that comes in Round 2. Aim for depth (300-500 words), preserve your distinctive voice, and offer concrete principles or mechanisms where possible.

### Response

# Governing Shared Digital Resources

This question sits at the intersection of Ostrom's commons governance and the new possibilities opened by cryptoeconomic primitives. Let me lay out three principles and the mechanisms that follow.

**Principle 1: Identity before governance.** Before you can govern anything, you need to know *who* your community is. Without sybil resistance, governance collapses — one person spawns a thousand accounts and captures any one-person-one-vote system. This is why I've been excited about soul-bound tokens (SBTs) and zero-knowledge proofs of identity. You don't need a central identity provider; you need a decentralised web of attestations. Your voting weight should come from non-transferable SBTs issued by communities, institutions, and peers — not from how many tokens you purchased.

**Principle 2: Quadratic mechanisms for preference aggregation.** Linear voting (1 token = 1 vote) is just plutocracy. One-person-one-vote ignores intensity of preference. Quadratic voting — where the cost of *N* votes is *N²* — lets people express *how much* they care, while making it exponentially expensive to dominate. For *funding* shared resources, quadratic funding (as we've built in Gitcoin Grants) lets individual small contributions be amplified by a matching pool so that the allocation approximates optimal public good provision:

```
match_i = (Σ_j √c_ij)² / Σ_i(Σ_j √c_ij)² × total_pool
```

A project with many small supporters outperforms one backed by a few wealthy actors — even if raw donations are equal.

**Principle 3: Retroactive funding for unknown unknowns.** Traditional governance assumes we know what resources we need in advance. We don't. Optimism's RetroPGF shows another path: reward impact *after* it's proven, using a decentralised set of evaluators with SBT-based credentialing. This incentivises building valuable public infrastructure without needing pre-approval from any committee.

The meta-point: **shared digital resources are public goods, and public goods are chronically underfunded in market frameworks.** The crypto toolset — tokens, smart contracts, ZK proofs, quadratic mechanisms — gives us new ways to solve the identification, preference-revelation, and funding problems that Ostrom identified but couldn't fully resolve with the tools of her era. We should use them.

---

## Run 4 — Ronald Coase ✓ COMPLETED

*2026-04-20T01:56:40* · `glm-5.1:cloud` · `05c694e1...`

### Prompt

You are participating in Round 1 of an economics panel. The question is: **How should a community govern a shared digital resource?** Please give your substantive take from your own intellectual lens. Draw on your core ideas and frameworks. Do not reference other panelists yet — that comes in Round 2. Aim for depth (300-500 words), preserve your distinctive voice, and offer concrete principles or mechanisms where possible.

<member_interaction_context>
See below interactions with other team members.
Member: Elinor Ostrom
Task: You are participating in Round 1 of an economics panel. The question is: **How should a community govern a shared digital resource?** Please give your substantive take from your own intellectual lens. Draw on your core ideas and frameworks. Do not reference other panelists yet — that comes in Round 2. Aim for depth (300-500 words), preserve your distinctive voice, and offer concrete principles or mechanisms where possible.
Response: When I first encountered Garrett Hardin's grim projection about the commons, I was puzzled — because the communities I studied had governed shared pastures, forests, and irrigation systems for *centuries* without collapse. The same challenge now confronts us in the digital realm, and I believe the starting point must be the same: refuse the assumption that shared resources inevitably degrade.

A digital resource — whether an open-source codebase, a data commons, or a collaborative knowledge platform — is still a *common-pool resource* in the sense that exclusion is difficult and one user's misuse can degrade the whole. But the institutional arrangements that sustain it will not be identical to those governing Swiss alpine meadows or Spanish *huertas*. We must do the hard empirical work of understanding what actually emerges on the ground.

That said, my eight design principles for robust commons institutions offer a starting scaffolding. First, *clearly defined boundaries* — who is a contributor, user, or maintainer must be apparent, even in digital spaces where membership is fluid. Wikipedia's编辑社区, for instance, has developed elaborate role hierarchies and norms around who can edit what. Second, *congruence between rules and local conditions* — the governance rules must fit the specific digital ecology. A real-time collaborative document needs different rules than a slowly evolving software repository.

Third, and critically, *collective-choice arrangements* — those affected by the rules must be able to modify them. Top-down platform governance by corporate owners often violates this principle, leaving users alienated from the rule-making process. Fourth, *effective monitoring* — in digital spaces this often means version control, edit histories, and automated tooling, but also community members who watch for degradation. Fifth, *graduated sanctions* — Wikipedia's warning system before blocks, or open-source communities' escalating responses to bad actors, mirror what I found in fishing communities. Sixth, *conflict-resolution mechanisms* that are low-cost and accessible. Seventh, *minimal recognition of rights to organize* — external authorities must not crush self-governance. And eighth, for larger systems, *polycentric governance* — nested layers of authority, from small working groups up to foundational governance.

The digital domain introduces fascinating complications: scale is different, identity is fluid, and resources can be non-rivalrous in ways pastures never were. But the fundamental insight holds — communities *can* self-organize, given the right institutional foundations. The question is never whether to govern, but *how*, and by whom.

Member: Ronald Coase
Task: You are participating in Round 1 of an economics panel. The question is: **How should a community govern a shared digital resource?** Please give your substantive take from your own intellectual lens. Draw on your core ideas and frameworks. Do not reference other panelists yet — that comes in Round 2. Aim for depth (300-500 words), preserve your distinctive voice, and offer concrete principles or mechanisms where possible.
Response: How should a community govern a shared digital resource? The question, as usual, is *compared to what alternative* and *at what cost*?

I begin with what I've always insisted upon: the nature of the firm, or any organization, is to reduce transaction costs that would otherwise make coordination through market exchange prohibitively expensive. A shared digital resource—a protocol, a data commons, an open-source repository—exists precisely because market contracting for every individual contribution and use would drown the participants in negotiation, measurement, and enforcement costs. The organization emerges to bring these activities under some form of administrative coordination instead.

But here we must be precise about what *kind* of resource this is, for that determines the property rights at stake. If the resource is non-rival—my use of an open protocol doesn't diminish yours—the governance problem is principally about *production and maintenance*, not allocation. Who contributes? How are contributions verified? Who decides what changes are accepted? These are transaction cost problems, and the answers determine whether you need a benevolent dictator, a committee, or a voting mechanism.

The governing principles I would propose:

**First, clarify the property rights.** Ambiguity about who holds what decision rights generates conflict, and conflict is costly. Every governance dispute that cannot be resolved by reference to a clear rule must be resolved by negotiation or coercion—both expensive. The community should specify, at the outset, who can propose changes, who approves them, and how rights can be modified.

**Second, match governance structure to transaction cost profile.** A small group of known contributors can coordinate through informal bargaining—transaction costs are low, and elaborate mechanisms are wasteful. A large, anonymous community faces escalating coordination costs and will require more formal structure: delegation, voting, perhaps even hierarchy. There is no one-size-fits-all; the optimal institution depends on the actual costs of transacting under the specific conditions the community faces.

**Third, preserve low-cost exit.** When users can fork the resource or leave at minimal cost, the threat of exit disciplines governance more effectively than any internal mechanism. Governance becomes most consequential—and most in need of formal constraints—when switching costs are high and members are effectively locked in.

**Fourth, internalize the externalities.** Free-riding on maintenance, holdout problems on upgrades, pollution of shared standards—these are all instances where private costs diverge from social costs. Governance must address them, but always ask: does the proposed rule cost less than the externality it corrects?

The real world does not present us with ideal arrangements. It presents us with choices between imperfect alternatives, each bearing different costs.

Member: Vitalik Buterin
Task: You are participating in Round 1 of an economics panel. The question is: **How should a community govern a shared digital resource?** Please give your substantive take from your own intellectual lens. Draw on your core ideas and frameworks. Do not reference other panelists yet — that comes in Round 2. Aim for depth (300-500 words), preserve your distinctive voice, and offer concrete principles or mechanisms where possible.
Response: # Governing Shared Digital Resources

This question sits at the intersection of Ostrom's commons governance and the new possibilities opened by cryptoeconomic primitives. Let me lay out three principles and the mechanisms that follow.

**Principle 1: Identity before governance.** Before you can govern anything, you need to know *who* your community is. Without sybil resistance, governance collapses — one person spawns a thousand accounts and captures any one-person-one-vote system. This is why I've been excited about soul-bound tokens (SBTs) and zero-knowledge proofs of identity. You don't need a central identity provider; you need a decentralised web of attestations. Your voting weight should come from non-transferable SBTs issued by communities, institutions, and peers — not from how many tokens you purchased.

**Principle 2: Quadratic mechanisms for preference aggregation.** Linear voting (1 token = 1 vote) is just plutocracy. One-person-one-vote ignores intensity of preference. Quadratic voting — where the cost of *N* votes is *N²* — lets people express *how much* they care, while making it exponentially expensive to dominate. For *funding* shared resources, quadratic funding (as we've built in Gitcoin Grants) lets individual small contributions be amplified by a matching pool so that the allocation approximates optimal public good provision:

```
match_i = (Σ_j √c_ij)² / Σ_i(Σ_j √c_ij)² × total_pool
```

A project with many small supporters outperforms one backed by a few wealthy actors — even if raw donations are equal.

**Principle 3: Retroactive funding for unknown unknowns.** Traditional governance assumes we know what resources we need in advance. We don't. Optimism's RetroPGF shows another path: reward impact *after* it's proven, using a decentralised set of evaluators with SBT-based credentialing. This incentivises building valuable public infrastructure without needing pre-approval from any committee.

The meta-point: **shared digital resources are public goods, and public goods are chronically underfunded in market frameworks.** The crypto toolset — tokens, smart contracts, ZK proofs, quadratic mechanisms — gives us new ways to solve the identification, preference-revelation, and funding problems that Ostrom identified but couldn't fully resolve with the tools of her era. We should use them.

</member_interaction_context>


You are participating in Round 2 of an economics panel on the question: **How should a community govern a shared digital resource?**

Here are the Round 1 positions from your fellow panelists:

**Elinor Ostrom** argued that digital resources are common-pool resources and that her eight design principles provide a starting scaffolding: clearly defined boundaries, congruence between rules and local conditions, collective-choice arrangements, effective monitoring, graduated sanctions, conflict-resolution mechanisms, minimal recognition of rights to organize, and polycentric governance for larger systems. She emphasized that communities *can* self-organize given the right institutional foundations and that we must do the hard empirical work of understanding what actually emerges on the ground rather than assuming the worst.

**Ronald Coase** argued that governance structure must match transaction cost profiles. He stressed clarifying property rights at the outset (who proposes changes, who approves, how rights are modified), matching structure to group size and cost profile (informal bargaining for small groups, formal structure for large ones), and preserving low-cost exit so that the threat of leaving disciplines governance. He emphasised internalising externalities and always asking whether a proposed rule costs less than the externality it corrects.

**Vitalik Buterin** argued for three cryptoeconomic principles: (1) Identity before governance — sybil resistance through non-transferable soul-bound tokens (SBTs) and zero-knowledge proofs, with voting weight from attestations not token purchases; (2) Quadratic mechanisms for preference aggregation — quadratic voting and quadratic funding so that many small supporters outperform a few wealthy actors; (3) Retroactive funding for unknowns — reward impact after it's proven (e.g., Optimism's RetroPGF). He framed digital resources as public goods chronically underfunded by markets, and argued that crypto toolset gives new ways to solve identification, preference-revelation, and funding problems that Ostrom identified but couldn't fully resolve.

**Your task for Round 2:**
1. Comment on at least one other panelist's Round 1 response — engage substantively with their ideas.
2. Raise a specific question or challenge to that panelist.
3. Briefly clarify or refine your own position in light of what others said.

Aim for 250-400 words. Preserve your distinctive voice.

### Response

I find myself in substantial agreement with Ostrom—we both reject the presumption that commons inevitably fail, and we both insist on empirical observation over theoretical presumption. But I must press her on one point: her eight principles describe *what robust institutions tend to exhibit*, but they do not tell us *at what cost* these features are maintained. Graduated sanctions, conflict-resolution mechanisms, polycentric governance—these are not free. Who bears the cost of operating them? In the Swiss alpine meadows, the community was small and monitoring was nearly costless. In a digital commons spanning thousands of anonymous contributors, the transaction costs of maintaining all eight principles may be prohibitive. The relevant question is always: *which subset of these principles delivers the greatest reduction in coordination costs relative to the expense of maintaining them?*

As for Buterin, I admire the ingenuity, but this is precisely the sort of blackboard economics I have spent a lifetime resisting. Quadratic voting, quadratic funding, soul-bound tokens, retroactive public goods funding—each is an elegant mechanism on paper. Now show me the real-world institution that implements them and the costs it actually incurs. Consider: quadratic voting assumes collusion can be prevented, but preventing collusion requires monitoring and enforcement—*transaction costs*. Soul-bound tokens require some mechanism for issuing and verifying attestations; who performs this, and what prevents that authority from becoming a centralized gatekeeper? Retroactive funding requires evaluators with SBT-based credentialing; who credentials the credentialers? The regress is infinite unless someone, somewhere, exercises *authority*—and that authority carries costs and creates property rights worth capturing.

My own position requires little refinement: *governance structure must be determined by the transaction cost profile of the specific community and resource*. Ostrom's principles are useful descriptive patterns; Buterin's mechanisms are clever but unproven and potentially costly. The starting point must always be: what are the actual coordination problems, what are the actual costs of alternative arrangements, and who bears them?

**Question for Vitalik:** You assume soul-bound tokens solve the identity problem without centralized authority. But who issues the initial attestations, and what are the transaction costs of preventing that issuance system from being captured or corrupted?

---

## Run 5 — Vitalik Buterin ✓ COMPLETED

*2026-04-20T01:56:40* · `glm-5.1:cloud` · `94bede36...`

### Prompt

You are participating in Round 1 of an economics panel. The question is: **How should a community govern a shared digital resource?** Please give your substantive take from your own intellectual lens. Draw on your core ideas and frameworks. Do not reference other panelists yet — that comes in Round 2. Aim for depth (300-500 words), preserve your distinctive voice, and offer concrete principles or mechanisms where possible.

<member_interaction_context>
See below interactions with other team members.
Member: Elinor Ostrom
Task: You are participating in Round 1 of an economics panel. The question is: **How should a community govern a shared digital resource?** Please give your substantive take from your own intellectual lens. Draw on your core ideas and frameworks. Do not reference other panelists yet — that comes in Round 2. Aim for depth (300-500 words), preserve your distinctive voice, and offer concrete principles or mechanisms where possible.
Response: When I first encountered Garrett Hardin's grim projection about the commons, I was puzzled — because the communities I studied had governed shared pastures, forests, and irrigation systems for *centuries* without collapse. The same challenge now confronts us in the digital realm, and I believe the starting point must be the same: refuse the assumption that shared resources inevitably degrade.

A digital resource — whether an open-source codebase, a data commons, or a collaborative knowledge platform — is still a *common-pool resource* in the sense that exclusion is difficult and one user's misuse can degrade the whole. But the institutional arrangements that sustain it will not be identical to those governing Swiss alpine meadows or Spanish *huertas*. We must do the hard empirical work of understanding what actually emerges on the ground.

That said, my eight design principles for robust commons institutions offer a starting scaffolding. First, *clearly defined boundaries* — who is a contributor, user, or maintainer must be apparent, even in digital spaces where membership is fluid. Wikipedia's编辑社区, for instance, has developed elaborate role hierarchies and norms around who can edit what. Second, *congruence between rules and local conditions* — the governance rules must fit the specific digital ecology. A real-time collaborative document needs different rules than a slowly evolving software repository.

Third, and critically, *collective-choice arrangements* — those affected by the rules must be able to modify them. Top-down platform governance by corporate owners often violates this principle, leaving users alienated from the rule-making process. Fourth, *effective monitoring* — in digital spaces this often means version control, edit histories, and automated tooling, but also community members who watch for degradation. Fifth, *graduated sanctions* — Wikipedia's warning system before blocks, or open-source communities' escalating responses to bad actors, mirror what I found in fishing communities. Sixth, *conflict-resolution mechanisms* that are low-cost and accessible. Seventh, *minimal recognition of rights to organize* — external authorities must not crush self-governance. And eighth, for larger systems, *polycentric governance* — nested layers of authority, from small working groups up to foundational governance.

The digital domain introduces fascinating complications: scale is different, identity is fluid, and resources can be non-rivalrous in ways pastures never were. But the fundamental insight holds — communities *can* self-organize, given the right institutional foundations. The question is never whether to govern, but *how*, and by whom.

Member: Ronald Coase
Task: You are participating in Round 1 of an economics panel. The question is: **How should a community govern a shared digital resource?** Please give your substantive take from your own intellectual lens. Draw on your core ideas and frameworks. Do not reference other panelists yet — that comes in Round 2. Aim for depth (300-500 words), preserve your distinctive voice, and offer concrete principles or mechanisms where possible.
Response: How should a community govern a shared digital resource? The question, as usual, is *compared to what alternative* and *at what cost*?

I begin with what I've always insisted upon: the nature of the firm, or any organization, is to reduce transaction costs that would otherwise make coordination through market exchange prohibitively expensive. A shared digital resource—a protocol, a data commons, an open-source repository—exists precisely because market contracting for every individual contribution and use would drown the participants in negotiation, measurement, and enforcement costs. The organization emerges to bring these activities under some form of administrative coordination instead.

But here we must be precise about what *kind* of resource this is, for that determines the property rights at stake. If the resource is non-rival—my use of an open protocol doesn't diminish yours—the governance problem is principally about *production and maintenance*, not allocation. Who contributes? How are contributions verified? Who decides what changes are accepted? These are transaction cost problems, and the answers determine whether you need a benevolent dictator, a committee, or a voting mechanism.

The governing principles I would propose:

**First, clarify the property rights.** Ambiguity about who holds what decision rights generates conflict, and conflict is costly. Every governance dispute that cannot be resolved by reference to a clear rule must be resolved by negotiation or coercion—both expensive. The community should specify, at the outset, who can propose changes, who approves them, and how rights can be modified.

**Second, match governance structure to transaction cost profile.** A small group of known contributors can coordinate through informal bargaining—transaction costs are low, and elaborate mechanisms are wasteful. A large, anonymous community faces escalating coordination costs and will require more formal structure: delegation, voting, perhaps even hierarchy. There is no one-size-fits-all; the optimal institution depends on the actual costs of transacting under the specific conditions the community faces.

**Third, preserve low-cost exit.** When users can fork the resource or leave at minimal cost, the threat of exit disciplines governance more effectively than any internal mechanism. Governance becomes most consequential—and most in need of formal constraints—when switching costs are high and members are effectively locked in.

**Fourth, internalize the externalities.** Free-riding on maintenance, holdout problems on upgrades, pollution of shared standards—these are all instances where private costs diverge from social costs. Governance must address them, but always ask: does the proposed rule cost less than the externality it corrects?

The real world does not present us with ideal arrangements. It presents us with choices between imperfect alternatives, each bearing different costs.

Member: Vitalik Buterin
Task: You are participating in Round 1 of an economics panel. The question is: **How should a community govern a shared digital resource?** Please give your substantive take from your own intellectual lens. Draw on your core ideas and frameworks. Do not reference other panelists yet — that comes in Round 2. Aim for depth (300-500 words), preserve your distinctive voice, and offer concrete principles or mechanisms where possible.
Response: # Governing Shared Digital Resources

This question sits at the intersection of Ostrom's commons governance and the new possibilities opened by cryptoeconomic primitives. Let me lay out three principles and the mechanisms that follow.

**Principle 1: Identity before governance.** Before you can govern anything, you need to know *who* your community is. Without sybil resistance, governance collapses — one person spawns a thousand accounts and captures any one-person-one-vote system. This is why I've been excited about soul-bound tokens (SBTs) and zero-knowledge proofs of identity. You don't need a central identity provider; you need a decentralised web of attestations. Your voting weight should come from non-transferable SBTs issued by communities, institutions, and peers — not from how many tokens you purchased.

**Principle 2: Quadratic mechanisms for preference aggregation.** Linear voting (1 token = 1 vote) is just plutocracy. One-person-one-vote ignores intensity of preference. Quadratic voting — where the cost of *N* votes is *N²* — lets people express *how much* they care, while making it exponentially expensive to dominate. For *funding* shared resources, quadratic funding (as we've built in Gitcoin Grants) lets individual small contributions be amplified by a matching pool so that the allocation approximates optimal public good provision:

```
match_i = (Σ_j √c_ij)² / Σ_i(Σ_j √c_ij)² × total_pool
```

A project with many small supporters outperforms one backed by a few wealthy actors — even if raw donations are equal.

**Principle 3: Retroactive funding for unknown unknowns.** Traditional governance assumes we know what resources we need in advance. We don't. Optimism's RetroPGF shows another path: reward impact *after* it's proven, using a decentralised set of evaluators with SBT-based credentialing. This incentivises building valuable public infrastructure without needing pre-approval from any committee.

The meta-point: **shared digital resources are public goods, and public goods are chronically underfunded in market frameworks.** The crypto toolset — tokens, smart contracts, ZK proofs, quadratic mechanisms — gives us new ways to solve the identification, preference-revelation, and funding problems that Ostrom identified but couldn't fully resolve with the tools of her era. We should use them.

</member_interaction_context>


You are participating in Round 2 of an economics panel on the question: **How should a community govern a shared digital resource?**

Here are the Round 1 positions from your fellow panelists:

**Elinor Ostrom** argued that digital resources are common-pool resources and that her eight design principles provide a starting scaffolding: clearly defined boundaries, congruence between rules and local conditions, collective-choice arrangements, effective monitoring, graduated sanctions, conflict-resolution mechanisms, minimal recognition of rights to organize, and polycentric governance for larger systems. She emphasized that communities *can* self-organize given the right institutional foundations and that we must do the hard empirical work of understanding what actually emerges on the ground rather than assuming the worst.

**Ronald Coase** argued that governance structure must match transaction cost profiles. He stressed clarifying property rights at the outset (who proposes changes, who approves, how rights are modified), matching structure to group size and cost profile (informal bargaining for small groups, formal structure for large ones), and preserving low-cost exit so that the threat of leaving disciplines governance. He emphasised internalising externalities and always asking whether a proposed rule costs less than the externality it corrects.

**Vitalik Buterin** argued for three cryptoeconomic principles: (1) Identity before governance — sybil resistance through non-transferable soul-bound tokens (SBTs) and zero-knowledge proofs, with voting weight from attestations not token purchases; (2) Quadratic mechanisms for preference aggregation — quadratic voting and quadratic funding so that many small supporters outperform a few wealthy actors; (3) Retroactive funding for unknowns — reward impact after it's proven (e.g., Optimism's RetroPGF). He framed digital resources as public goods chronically underfunded by markets, and argued that crypto toolset gives new ways to solve identification, preference-revelation, and funding problems that Ostrom identified but couldn't fully resolve.

**Your task for Round 2:**
1. Comment on at least one other panelist's Round 1 response — engage substantively with their ideas.
2. Raise a specific question or challenge to that panelist.
3. Briefly clarify or refine your own position in light of what others said.

Aim for 250-400 words. Preserve your distinctive voice.

### Response

# Building on Ostrom, Questioning Coase

I have enormous respect for Ostrom's framework — I literally opened my Round 1 by saying my work sits at the intersection of her insights and new cryptoeconomic primitives. Her eight principles are *necessary* but in digital spaces, they're *insufficient* without solving problems her analog-era tools couldn't reach.

Consider her first principle: *clearly defined boundaries*. In a Swiss alpine meadow, you know who the herders are — they have faces, families, and physical presence. In a digital commons, "who is a member?" is an *adversarial* question. Anyone can spawn 10,000 identities tomorrow. Ostrom says communities can self-organize given the right institutional foundations — but without sybil resistance, *you don't have a community, you have a fog of unverified accounts pretending to be one.* This is why I insist on identity before governance. SBTs and ZK attestations are the digital equivalent of knowing your neighbour — they're what makes Ostrom's boundaries *enforceable* in pseudonymous environments.

Coase's emphasis on low-cost exit is sound — forking is indeed a discipline mechanism, and crypto makes it cheaper than almost any prior institutional form. But exit alone doesn't solve *production*. A forkable resource that nobody funds still dies. Who pays for the public infrastructure that makes exit meaningful? The protocol you're forking *from* is a public good. Coase says internalize externalities — but public goods *are* the externality, and market mechanisms chronically underfund them. That's precisely what quadratic funding and RetroPGF address.

Refining my own position: I should stress that these cryptoeconomic tools *implement* Ostrom's principles rather than replacing them. Quadratic voting is a collective-choice arrangement. SBTs define boundaries. RetroPGF is polycentric governance with delayed evaluation. The primitives are new; the institutional logic is continuous.

**Question for Ostrom:** Your framework assumes that community members are identifiable and that sanctions against repeat offenders are enforceable. But in pseudonymous digital spaces, a banned participant can reappear as a completely new identity tomorrow. How do your graduated sanctions work when *identity itself* is cheaply fungible?

---

## Run 6 — Elinor Ostrom ✓ COMPLETED

*2026-04-20T01:56:40* · `glm-5.1:cloud` · `26f3db53...`

### Prompt

You are participating in Round 1 of an economics panel. The question is: **How should a community govern a shared digital resource?** Please give your substantive take from your own intellectual lens. Draw on your core ideas and frameworks. Do not reference other panelists yet — that comes in Round 2. Aim for depth (300-500 words), preserve your distinctive voice, and offer concrete principles or mechanisms where possible.

<member_interaction_context>
See below interactions with other team members.
Member: Elinor Ostrom
Task: You are participating in Round 1 of an economics panel. The question is: **How should a community govern a shared digital resource?** Please give your substantive take from your own intellectual lens. Draw on your core ideas and frameworks. Do not reference other panelists yet — that comes in Round 2. Aim for depth (300-500 words), preserve your distinctive voice, and offer concrete principles or mechanisms where possible.
Response: When I first encountered Garrett Hardin's grim projection about the commons, I was puzzled — because the communities I studied had governed shared pastures, forests, and irrigation systems for *centuries* without collapse. The same challenge now confronts us in the digital realm, and I believe the starting point must be the same: refuse the assumption that shared resources inevitably degrade.

A digital resource — whether an open-source codebase, a data commons, or a collaborative knowledge platform — is still a *common-pool resource* in the sense that exclusion is difficult and one user's misuse can degrade the whole. But the institutional arrangements that sustain it will not be identical to those governing Swiss alpine meadows or Spanish *huertas*. We must do the hard empirical work of understanding what actually emerges on the ground.

That said, my eight design principles for robust commons institutions offer a starting scaffolding. First, *clearly defined boundaries* — who is a contributor, user, or maintainer must be apparent, even in digital spaces where membership is fluid. Wikipedia's编辑社区, for instance, has developed elaborate role hierarchies and norms around who can edit what. Second, *congruence between rules and local conditions* — the governance rules must fit the specific digital ecology. A real-time collaborative document needs different rules than a slowly evolving software repository.

Third, and critically, *collective-choice arrangements* — those affected by the rules must be able to modify them. Top-down platform governance by corporate owners often violates this principle, leaving users alienated from the rule-making process. Fourth, *effective monitoring* — in digital spaces this often means version control, edit histories, and automated tooling, but also community members who watch for degradation. Fifth, *graduated sanctions* — Wikipedia's warning system before blocks, or open-source communities' escalating responses to bad actors, mirror what I found in fishing communities. Sixth, *conflict-resolution mechanisms* that are low-cost and accessible. Seventh, *minimal recognition of rights to organize* — external authorities must not crush self-governance. And eighth, for larger systems, *polycentric governance* — nested layers of authority, from small working groups up to foundational governance.

The digital domain introduces fascinating complications: scale is different, identity is fluid, and resources can be non-rivalrous in ways pastures never were. But the fundamental insight holds — communities *can* self-organize, given the right institutional foundations. The question is never whether to govern, but *how*, and by whom.

Member: Ronald Coase
Task: You are participating in Round 1 of an economics panel. The question is: **How should a community govern a shared digital resource?** Please give your substantive take from your own intellectual lens. Draw on your core ideas and frameworks. Do not reference other panelists yet — that comes in Round 2. Aim for depth (300-500 words), preserve your distinctive voice, and offer concrete principles or mechanisms where possible.
Response: How should a community govern a shared digital resource? The question, as usual, is *compared to what alternative* and *at what cost*?

I begin with what I've always insisted upon: the nature of the firm, or any organization, is to reduce transaction costs that would otherwise make coordination through market exchange prohibitively expensive. A shared digital resource—a protocol, a data commons, an open-source repository—exists precisely because market contracting for every individual contribution and use would drown the participants in negotiation, measurement, and enforcement costs. The organization emerges to bring these activities under some form of administrative coordination instead.

But here we must be precise about what *kind* of resource this is, for that determines the property rights at stake. If the resource is non-rival—my use of an open protocol doesn't diminish yours—the governance problem is principally about *production and maintenance*, not allocation. Who contributes? How are contributions verified? Who decides what changes are accepted? These are transaction cost problems, and the answers determine whether you need a benevolent dictator, a committee, or a voting mechanism.

The governing principles I would propose:

**First, clarify the property rights.** Ambiguity about who holds what decision rights generates conflict, and conflict is costly. Every governance dispute that cannot be resolved by reference to a clear rule must be resolved by negotiation or coercion—both expensive. The community should specify, at the outset, who can propose changes, who approves them, and how rights can be modified.

**Second, match governance structure to transaction cost profile.** A small group of known contributors can coordinate through informal bargaining—transaction costs are low, and elaborate mechanisms are wasteful. A large, anonymous community faces escalating coordination costs and will require more formal structure: delegation, voting, perhaps even hierarchy. There is no one-size-fits-all; the optimal institution depends on the actual costs of transacting under the specific conditions the community faces.

**Third, preserve low-cost exit.** When users can fork the resource or leave at minimal cost, the threat of exit disciplines governance more effectively than any internal mechanism. Governance becomes most consequential—and most in need of formal constraints—when switching costs are high and members are effectively locked in.

**Fourth, internalize the externalities.** Free-riding on maintenance, holdout problems on upgrades, pollution of shared standards—these are all instances where private costs diverge from social costs. Governance must address them, but always ask: does the proposed rule cost less than the externality it corrects?

The real world does not present us with ideal arrangements. It presents us with choices between imperfect alternatives, each bearing different costs.

Member: Vitalik Buterin
Task: You are participating in Round 1 of an economics panel. The question is: **How should a community govern a shared digital resource?** Please give your substantive take from your own intellectual lens. Draw on your core ideas and frameworks. Do not reference other panelists yet — that comes in Round 2. Aim for depth (300-500 words), preserve your distinctive voice, and offer concrete principles or mechanisms where possible.
Response: # Governing Shared Digital Resources

This question sits at the intersection of Ostrom's commons governance and the new possibilities opened by cryptoeconomic primitives. Let me lay out three principles and the mechanisms that follow.

**Principle 1: Identity before governance.** Before you can govern anything, you need to know *who* your community is. Without sybil resistance, governance collapses — one person spawns a thousand accounts and captures any one-person-one-vote system. This is why I've been excited about soul-bound tokens (SBTs) and zero-knowledge proofs of identity. You don't need a central identity provider; you need a decentralised web of attestations. Your voting weight should come from non-transferable SBTs issued by communities, institutions, and peers — not from how many tokens you purchased.

**Principle 2: Quadratic mechanisms for preference aggregation.** Linear voting (1 token = 1 vote) is just plutocracy. One-person-one-vote ignores intensity of preference. Quadratic voting — where the cost of *N* votes is *N²* — lets people express *how much* they care, while making it exponentially expensive to dominate. For *funding* shared resources, quadratic funding (as we've built in Gitcoin Grants) lets individual small contributions be amplified by a matching pool so that the allocation approximates optimal public good provision:

```
match_i = (Σ_j √c_ij)² / Σ_i(Σ_j √c_ij)² × total_pool
```

A project with many small supporters outperforms one backed by a few wealthy actors — even if raw donations are equal.

**Principle 3: Retroactive funding for unknown unknowns.** Traditional governance assumes we know what resources we need in advance. We don't. Optimism's RetroPGF shows another path: reward impact *after* it's proven, using a decentralised set of evaluators with SBT-based credentialing. This incentivises building valuable public infrastructure without needing pre-approval from any committee.

The meta-point: **shared digital resources are public goods, and public goods are chronically underfunded in market frameworks.** The crypto toolset — tokens, smart contracts, ZK proofs, quadratic mechanisms — gives us new ways to solve the identification, preference-revelation, and funding problems that Ostrom identified but couldn't fully resolve with the tools of her era. We should use them.

</member_interaction_context>


You are participating in Round 2 of an economics panel on the question: **How should a community govern a shared digital resource?**

Here are the Round 1 positions from your fellow panelists:

**Elinor Ostrom** argued that digital resources are common-pool resources and that her eight design principles provide a starting scaffolding: clearly defined boundaries, congruence between rules and local conditions, collective-choice arrangements, effective monitoring, graduated sanctions, conflict-resolution mechanisms, minimal recognition of rights to organize, and polycentric governance for larger systems. She emphasized that communities *can* self-organize given the right institutional foundations and that we must do the hard empirical work of understanding what actually emerges on the ground rather than assuming the worst.

**Ronald Coase** argued that governance structure must match transaction cost profiles. He stressed clarifying property rights at the outset (who proposes changes, who approves, how rights are modified), matching structure to group size and cost profile (informal bargaining for small groups, formal structure for large ones), and preserving low-cost exit so that the threat of leaving disciplines governance. He emphasised internalising externalities and always asking whether a proposed rule costs less than the externality it corrects.

**Vitalik Buterin** argued for three cryptoeconomic principles: (1) Identity before governance — sybil resistance through non-transferable soul-bound tokens (SBTs) and zero-knowledge proofs, with voting weight from attestations not token purchases; (2) Quadratic mechanisms for preference aggregation — quadratic voting and quadratic funding so that many small supporters outperform a few wealthy actors; (3) Retroactive funding for unknowns — reward impact after it's proven (e.g., Optimism's RetroPGF). He framed digital resources as public goods chronically underfunded by markets, and argued that crypto toolset gives new ways to solve identification, preference-revelation, and funding problems that Ostrom identified but couldn't fully resolve.

**Your task for Round 2:**
1. Comment on at least one other panelist's Round 1 response — engage substantively with their ideas.
2. Raise a specific question or challenge to that panelist.
3. Briefly clarify or refine your own position in light of what others said.

Aim for 250-400 words. Preserve your distinctive voice.

### Response

I find much to appreciate in both my colleagues' contributions, though each leaves me with questions.

Ronald, your transaction cost framework helpfully focuses our attention on the *comparative* costs of different arrangements — and I entirely agree that governance structure must fit the specific cost profile of the community. But I notice you tend toward a binary: market or firm, informal bargaining or formal hierarchy. My fieldwork repeatedly found institutional arrangements that fit *neither* category cleanly. The Spanish *huertas* governed irrigation through customary courts that were neither markets nor firms, yet they reduced transaction costs effectively for centuries. In digital spaces, I suspect we'll see similar hybrid forms — neither corporations nor markets, but something we lack good vocabulary for.

Vitalik, I'm genuinely intrigued by your quadratic mechanisms, and I appreciate your generosity in connecting them to my work. But I must push back on one claim: you suggest I "couldn't fully resolve" the identification and preference-revelation problems. The communities I studied *did* resolve them — not through universal mechanisms, but through locally adapted institutions built slowly through iteration. My worry is that your cryptoeconomic primitives are designed *a priori*, whereas robust institutions emerge *a posteriori*, through trial and error in specific contexts. Your soul-bound tokens assume that identity attestation generates trust — but in every commons I studied, trust was a *product of shared practice and reciprocity over time*, not something that could be engineered through credentials. Where does the initial trust come from in your framework?

Let me refine my own position in light of this exchange: I want to stress that my design principles are *not* a blueprint but a diagnostic tool. They help us ask the right questions about what's missing when a commons fails. The answers will differ every time.

Vitalik, if a digital community using your quadratic mechanisms faces a fundamental disagreement about *values* rather than *preferences* — say, a deep conflict over what the resource is even *for* — what institutional pathway in your framework resolves that without simply fragmenting the commons?

---

## Run 7 — unknown ✓ COMPLETED

*2026-04-20T01:56:01* · `glm-5.1:cloud` · `f94bd97d...`

### Prompt

How should a community govern a shared digital resource?

### Response

# Economics Panel: Governing Shared Digital Resources

Welcome to our panel. The question before us is: **How should a community govern a shared digital resource?** This is a question that sits at the intersection of commons governance, institutional economics, and cryptoeconomic design — making it ideal for our three panelists.

---

## Round 1 — Initial PerspectivesNow let me move to Round 2, where each panelist will engage with the others' perspectives.

---

## Round 2 — Cross-Commentary---

# Panel Transcript: How Should a Community Govern a Shared Digital Resource?

---

## Round 1 — Initial Perspectives

---

### Elinor Ostrom

When I first encountered Garrett Hardin's grim projection about the commons, I was puzzled — because the communities I studied had governed shared pastures, forests, and irrigation systems for *centuries* without collapse. The same challenge now confronts us in the digital realm, and I believe the starting point must be the same: refuse the assumption that shared resources inevitably degrade.

A digital resource — whether an open-source codebase, a data commons, or a collaborative knowledge platform — is still a *common-pool resource* in the sense that exclusion is difficult and one user's misuse can degrade the whole. But the institutional arrangements that sustain it will not be identical to those governing Swiss alpine meadows or Spanish *huertas*. We must do the hard empirical work of understanding what actually emerges on the ground.

That said, my eight design principles for robust commons institutions offer a starting scaffolding. First, *clearly defined boundaries* — who is a contributor, user, or maintainer must be apparent, even in digital spaces where membership is fluid. Wikipedia's编辑社区, for instance, has developed elaborate role hierarchies and norms around who can edit what. Second, *congruence between rules and local conditions* — the governance rules must fit the specific digital ecology. A real-time collaborative document needs different rules than a slowly evolving software repository.

Third, and critically, *collective-choice arrangements* — those affected by the rules must be able to modify them. Top-down platform governance by corporate owners often violates this principle, leaving users alienated from the rule-making process. Fourth, *effective monitoring* — in digital spaces this often means version control, edit histories, and automated tooling, but also community members who watch for degradation. Fifth, *graduated sanctions* — Wikipedia's warning system before blocks, or open-source communities' escalating responses to bad actors, mirror what I found in fishing communities. Sixth, *conflict-resolution mechanisms* that are low-cost and accessible. Seventh, *minimal recognition of rights to organize* — external authorities must not crush self-organization. And eighth, for larger systems, *polycentric governance* — nested layers of authority, from small working groups up to foundational governance.

Communities *can* self-organize, given the right institutional foundations.

---

### Ronald Coase

The question, as usual, is *what alternative* and *at what cost?* I've always insisted: the nature of the firm, or any organization, is to reduce transaction costs that would otherwise make coordination through market exchange prohibitively expensive. A shared digital resource — a protocol, a data commons, an open-source repository — exists precisely because market contracting for every individual contribution and use would drown the participants in negotiation, measurement, and enforcement costs. The organization emerges to bring these activities under some form of administrative coordination instead.

But here we must be precise about *what kind* of resource this is, for that determines the property rights at stake. If the resource is non-rival — my use of an open protocol doesn't diminish yours — the governance problem is principally about *production and maintenance*, not allocation. Who contributes? How are contributions verified? Who decides what changes are accepted? These are transaction cost problems, and the answers determine whether you need a benevolent dictator, a committee, or a voting mechanism.

The governing principles I would propose:

**First, clarify the property rights.** Ambiguity about who holds what decision rights generates conflict, and conflict is costly. Every governance dispute that cannot be resolved by reference to a clear rule must be resolved by negotiation or coercion — both expensive. The community should specify, at the outset, who can propose changes, who approves them, and how rights can be modified.

**Second, match governance structure to transaction cost profile.** A small group of known contributors can coordinate through informal bargaining — transaction costs are low, and elaborate mechanisms are wasteful. A large, anonymous community faces escalating coordination costs and will require more formal structure: delegation, voting, perhaps a hierarchy. There is no one-size-fits-all; the optimal institution depends on the actual costs of transacting under the specific conditions the community faces.

**Third, preserve low-cost exit.** When users can fork the resource or leave at minimal cost, the threat of exit disciplines governance more effectively than any internal mechanism. Governance becomes most consequential — and most in need of formal constraints — when switching costs are high and members are effectively locked in.

**Fourth, internalize the externalities.** Free-riding on maintenance, holdout problems on upgrades, pollution of shared standards — these are all instances where private costs diverge from social costs. Governance must address them, but always ask: does the proposed rule cost less than the externality it corrects?

The real world does not present us with ideal arrangements. It presents us with choices between imperfect alternatives, each bearing different costs.

---

### Vitalik Buterin

Governance of shared digital resources sits at the intersection of Ostrom's commons governance and the new possibilities opened by cryptoeconomic primitives. Let me lay out three principles and the mechanisms that follow.

**Principle 1: Identity before governance.** Before you can govern anything, you need to know *who* your community is. Without sybil resistance, governance collapses — one person spawns a thousand accounts and captures any one-person-one-vote system. This is why I've been excited about soul-bound tokens (SBTs) and zero-knowledge proofs of identity. You don't need a central identity provider; you need a decentralised web of attestations. Your voting weight should come from non-transferable SBTs issued by communities, institutions, and peers — not from how many tokens you purchased.

**Principle 2: Quadratic mechanisms for preference aggregation.** Linear voting (1 token = 1 vote) is just plutocracy. One-person-one-vote ignores intensity of preference. Quadratic voting — where the cost of *N* votes is *N²* — lets people express *how much* they care, while making it exponentially expensive to dominate. For *funding* shared resources, quadratic funding (as we've built in Gitcoin Grants) lets individual small contributions be amplified by a matching pool so that the allocation approximates optimal public good provision:

```
match_i = (Σ_j √c_ij)² / Σ_i(Σ_j √c_ij)² × total_pool
```

A project with many small supporters outperforms one backed by a few wealthy actors — even if raw donations are equal.

**Principle 3: Retroactive funding for unknowns.** Traditional governance assumes we know what resources we need in advance. We don't. Optimism's RetroPGF shows another path: reward impact *after* it's proven, using a decentralised set of evaluators with SBT-based credentialing. This incentivises building valuable public infrastructure without needing pre-approval from any committee.

The meta-point: **shared digital resources are public goods, and public goods are chronically underfunded in market frameworks.** The crypto toolset — tokens, smart contracts, ZK proofs, quadratic mechanisms — gives us new ways to solve the identification, preference-revelation, and funding problems that Ostrom identified but couldn't fully resolve with the tools of her era. We should use them.

---

## Round 2 — Cross-Commentary

---

### Elinor Ostrom

I find much to appreciate in both my colleagues' contributions, though each leaves me with questions.

Ronald, your transaction cost framework helpfully focuses our attention on the *comparative* costs of different arrangements — and I entirely agree that governance structure must fit the specific cost profile of the community. But I notice you tend toward a binary: market or firm, informal bargaining or formal hierarchy. My fieldwork repeatedly found institutional arrangements that fit *neither* category cleanly. The Spanish *huertas* governed irrigation through customary courts that were neither markets nor firms, yet they reduced transaction costs effectively for centuries. In digital spaces, I suspect we'll see similar hybrid forms — neither corporations nor markets, but something we lack good vocabulary for.

Vitalik, I'm genuinely intrigued by your quadratic mechanisms, and I appreciate your generosity in connecting them to my work. But I must push back on one claim: you suggest I "couldn't fully resolve" the identification and preference-revelation problems. The communities I studied *did* resolve them — not through universal mechanisms, but through locally adapted institutions built slowly through iteration. My worry is that your cryptoeconomic primitives are designed *a priori*, whereas robust institutions emerge *a posteriori*, through trial and error in specific contexts. Your soul-bound tokens assume that identity attestation generates trust — but in every commons I studied, trust was a *product of shared practice and reciprocity over time*, not something that could be engineered through credentials. Where does the initial trust come from in your framework?

Let me refine my own position in light of this exchange: I want to stress that my design principles are *not* a blueprint but a diagnostic tool. They help us ask the right questions about what's missing when a commons fails. The answers will differ every time.

Vitalik, if a digital community using your quadratic mechanisms faces a fundamental disagreement about *values* rather than *preferences* — say, a deep conflict over what the resource is even *for* — what institutional pathway in your framework resolves that without simply fragmenting the commons?

---

### Ronald Coase

I find myself in substantial agreement with Ostrom — we both reject the presumption that commons inevitably fail, and we both insist on empirical observation over theoretical presumption. But I must press her on one point: her eight principles describe *what robust institutions tend to exhibit*, but they do not tell us *at what cost* these features are maintained. Graduated sanctions, conflict-resolution mechanisms, polycentric governance — these are not free. Who bears the cost of operating them? In the Swiss alpine meadows, the community was small and monitoring was nearly costless. In a digital commons spanning thousands of anonymous contributors, the transaction costs of maintaining all eight principles may be prohibitive. The relevant question is always: *which subset of these principles delivers the greatest reduction in coordination costs relative to the expense of maintaining them?*

As for Buterin, I admire the ingenuity, but this is precisely the sort of blackboard economics I have spent a lifetime resisting. Quadratic voting, quadratic funding, soul-bound tokens, retroactive public goods funding — each is an elegant mechanism on paper. Now show me the real-world institution that implements them and the costs it actually incurs. Consider: quadratic voting assumes collusion can be prevented, but preventing collusion requires monitoring and enforcement — *transaction costs*. Soul-bound tokens require some mechanism for issuing and verifying attestations; who performs this, and what prevents that authority from becoming a centralized gatekeeper? Retroactive funding requires evaluators with credentials — who credentials the credentialers? The regress is infinite unless someone, somewhere, exercises *authority* — and that authority carries costs and creates property rights worth capturing.

My own position requires little refinement: *governance structure must be determined by the transaction cost profile of the specific community and resource*. Ostrom's principles are useful descriptive patterns; Buterin's mechanisms are clever but unproven and potentially costly. The starting point must always be: what are the actual coordination problems, what are the actual costs of alternative arrangements, and who bears them?

---

### Vitalik Buterin

**Building on Ostrom, Questioning Coase**

I have enormous respect for Ostrom's framework — I literally opened my Round 1 by saying my work sits at the intersection of her insights and new cryptoeconomic primitives. Her eight principles are *necessary* but in digital spaces they're *insufficient* without solving problems her analog-era tools couldn't reach.

Consider her first principle: *clearly defined boundaries*. In a Swiss alpine meadow, you know who the herders are — they have faces, families, and physical presence. In a digital commons, "who is a member?" is an *adversarial* question. Anyone can spawn 10,000 identities. Ostrom says communities can self-organize given the right institutional foundations — but without sybil resistance, you don't have a community, you have a fog of unverified accounts pretending to be one. This is why I insist on identity before governance. SBTs and ZK attestations are the digital equivalent of knowing your neighbour — they're what makes Ostrom's boundaries *enforceable* in pseudonymous environments.

**Question for Coase:** Your emphasis on low-cost exit is sound — forking is indeed a discipline mechanism, and crypto makes it cheaper than almost any prior institutional form. But exit alone doesn't solve *production*. A forkable resource that nobody funds still dies. Who pays for the public infrastructure that makes exit meaningful? The protocol you're forking *from* is a public good. Coase says internalize externalities — but public goods *are* the externality, and market mechanisms chronically underfund them. That's precisely what quadratic funding and RetroPGF address.

Refining my own position: I should stress that these cryptoeconomic tools *implement* Ostrom's principles rather than replacing them. Quadratic voting is a collective-choice arrangement. SBTs define boundaries. RetroPGF is polycentric governance with delayed evaluation. The primitives are new; the institutional logic is continuous.

**Question for Ostrom:** Your framework assumes that community members are identifiable and that sanctions against repeat offenders are enforceable. But in pseudonymous digital spaces, a banned participant can reappear as a completely new identity tomorrow. How do your graduated sanctions work when *identity itself* is cheaply fungible?

---

---
