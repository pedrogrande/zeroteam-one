Here is a precise, document-ready integration plan — covering every change needed and exactly where each one goes. The Proof of Value Layer touches both documents in different ways.

***

## Overview of All Changes

| Document | Change type | Location |
|---|---|---|
| `framework-principles-v4.md` | New section | After Conformance Profiles, before Proportionality Matrix |
| `framework-principles-v4.md` | Small extension | L3 — Knowledge Compounds |
| `framework-principles-v4.md` | Small addition | Quick Reference (new named capabilities note) |
| `framework-principles-v4.md` | Version bump | Header + What's New |
| `structured-trust-framework.md` | One paragraph | "What the Framework Does" section |
| `structured-trust-framework.md` | One sentence | Blockchain Trust Layer description |

***

## Change 1 — New Section in `framework-principles-v4.md`

**Placement:** Insert after the High-Stakes / DAO Profile conformance block and before the Proportionality Matrix. This placement is deliberate — the PoVL depends on the Blockchain Trust Layer, which is the highest conformance tier, and it sets context before the proportionality guidance. 

***

### The Proof of Value Layer

**What it is**

The Proof of Value Layer is not a principle. It is the natural consequence of three principles — T2, T4, and L3 — operating together at system level.

When every output is proven (T2), every action witnessed (T4), and patterns crystallise from outcomes (L3), the accumulated evidence doesn't just make individual work trustworthy — it makes *the framework itself* provably effective. The Proof of Value Layer is the intelligence surface that aggregates this structural evidence into effectiveness signals, and the Blockchain Trust Layer is what makes those signals independently verifiable by any party.

**The important distinction:** This is not a reporting dashboard built on top of the framework. It is what the framework structurally produces as a byproduct of doing what it already does.

**Why this matters**

A framework that asks stakeholders to trust that it works is making the same category error it was built to prevent. The Proof of Value Layer closes the loop: the framework shouldn't ask anyone to trust its claims about effectiveness — it should produce structural proof, verifiable by any party, using the same evidence-first approach applied to everything else.

**What produces it**

| Source principle | Contribution |
|---|---|
| **T2 – Proof Is the Product** | Every task produces structured, attributed evidence — the raw material for effectiveness signals |
| **T4 – All Actions Witnessed** | Every action logged immutably — aggregate patterns are computable from first principles |
| **L3 – Knowledge Compounds** | Patterns accumulate confidence from outcomes — effectiveness trends emerge over time |

**What makes it independently verifiable**

The Blockchain Trust Layer anchors cryptographically-signed effectiveness snapshots at defined intervals. These are not self-reported metrics — they are evidence trails verifiable by any party without access to the originating system. Regulators, funders, partners, and clients can verify independently. This is what distinguishes Proof of Value from a compliance dashboard.

**Cross-sector signals (derivable from any deployment)**

These signals emerge from the framework's structural evidence regardless of domain:

- **Verification cycle time** — time from submission to independent verification; reduction indicates trust velocity increasing
- **Rework rate** — proportion of tasks requiring correction after verification; decline indicates structural quality improving
- **Dispute/contestation rate** — frequency of output challenges; trend indicates earned trust building or eroding
- **Uncertainty resolution time** — time from L1 raise to resolution; improvement indicates specification quality compounding
- **Verifier consensus rate** — proportion of quorum decisions reaching consensus without escalation
- **Cross-boundary proof acceptance** — rate at which proofs generated in one organisational context are accepted by external parties without re-verification; indicates portable trust building

**Domain-specific signal extensions**

Cross-sector signals are the foundation. Domain communities define additional signals meaningful in their context, registered as domain adaptations — not defined by the framework itself:

| Domain | Example signals |
|---|---|
| Legal / Regulated | Compliance breach rate; audit query resolution time; regulatory examination outcomes |
| Financial services | Counterparty risk cost reduction; settlement failure rate; credit decision contestation rate |
| Healthcare / Clinical | Adverse event rate attributable to information quality; contestation-to-correction cycle time |
| DAO / Web3 | On-chain dispute resolution rate; cross-org proof acceptance rate; governance participation trend |
| Software | Production incident rate attributable to verification gaps; deployment rollback rate |

**Ontological implementation**

- Knowledge dimension stores `effectiveness_signal_concept` Things with computed values and trend direction
- Events dimension aggregates raw inputs (verification completions, rework events, contestations) automatically
- TypeDB rules compute rolling signal values from Events — no manual reporting step
- Blockchain Trust Layer anchors `effectiveness_snapshot_concept` Things at defined intervals
- Domain extensions registered as `domain_signal_extension_concept` Things scoped to domain Group

**Requirements**

- Cross-sector signal computation is automatic — no manual reporting
- Snapshots anchored to Blockchain Trust Layer at intervals appropriate to deployment context
- Domain signal extensions documented and registered before use
- Signal trends visible to governance-entitled Actors, including affected parties (P1)
- Signals feed back into L3 pattern library (which deployment patterns correlate with better signals)

**What this is not**

- Not a performance management tool — signals describe system health, not individual actor performance
- Not a compliance dashboard — signals are structural evidence, not self-reported metrics
- Not optional for Blockchain Trust Layer deployments — independently verifiable Proof of Value is the primary reason to adopt that layer

***

## Change 2 — Small Extension to L3

**Placement:** In the L3 — Knowledge Compounds section, add to the end of *"What this enables"* and *"Ontological implementation"*. 

**Add to "What this enables":**

> At system level, accumulated patterns compose into Proof of Value signals — aggregate evidence of framework effectiveness over time. See: Proof of Value Layer.

**Add to "Ontological implementation":**

> Patterns aggregate into `effectiveness_signal_concept` Things via TypeDB rules (see Proof of Value Layer). Pattern confidence scores feed directly into cross-sector signal computation.

***

## Change 3 — Quick Reference Table note

**Placement:** Immediately below the Quick Reference principles table, before the Conformance Profiles section. 

**Add:**

> **Named capability:** The **Proof of Value Layer** is a system-level capability, not a principle. It is the emergent output of T2 + T4 + L3 operating at aggregate level, made independently verifiable by the Blockchain Trust Layer. See: Proof of Value Layer section.

***

## Change 4 — Version Bump and What's New

**Placement:** Document header and What's New section. 

**Header:** `Version: 4.1`

**Add to What's New:**

> - **Proof of Value Layer**: Named system capability that aggregates structural evidence (T2 + T4 + L3) into independently verifiable effectiveness signals. Cross-sector signals built in; domain-specific signals attach as registered extensions. Blockchain Trust Layer is the portability mechanism.

***

## Change 5 — Executive Overview (`structured-trust-framework.md`)

**Placement:** In "What the Framework Does", add a new paragraph after the five-category description. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_8788bb3e-490d-499d-b897-09db0a68afea/b106ad5d-2c8c-429d-8098-3442af1e217a/structured-trust-framework.md)

**Add:**

> The framework also produces a **Proof of Value Layer** — a system-level capability, not a separate principle, that emerges from the structural evidence the framework generates in the course of normal operation. When every action is witnessed, every output is proven, and patterns crystallise from outcomes, the accumulated evidence makes *the framework itself* provably effective. Effectiveness signals are computable from first principles, require no manual reporting, and — when the Blockchain Trust Layer is active — are independently verifiable by any party without access to the originating system. The framework doesn't ask anyone to trust that it works. It produces proof.

**Placement:** In the Blockchain Trust Layer description (Scope and Applicability section), extend the existing sentence. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_8788bb3e-490d-499d-b897-09db0a68afea/b106ad5d-2c8c-429d-8098-3442af1e217a/structured-trust-framework.md)

**Current:**
> an optional **Blockchain Trust Layer** that extends structural trust cryptographically across organisational boundaries — making governance artifacts independently verifiable by any party without access to the originating system.

**Replace with:**
> an optional **Blockchain Trust Layer** that extends structural trust cryptographically across organisational boundaries — making governance artifacts independently verifiable by any party without access to the originating system, and serving as the portability mechanism for the Proof of Value Layer, anchoring effectiveness evidence so it is auditable by regulators, funders, and partners without self-reported claims.

***

## What Doesn't Change

The 24 principles remain intact and unnumbered in their categories — the PoVL sits *beneath* them as a named emergent capability, which is the right structural position.  The conformance profiles don't need changes beyond what's already implied: PoVL is fully active only in Blockchain Trust Layer deployments, partially surfaced in High-Stakes/DAO (L3 patterns without blockchain anchoring), and not applicable in Core Trust or Full Lifecycle profiles where the evidence infrastructure is still being established. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_8788bb3e-490d-499d-b897-09db0a68afea/b106ad5d-2c8c-429d-8098-3442af1e217a/structured-trust-framework.md)