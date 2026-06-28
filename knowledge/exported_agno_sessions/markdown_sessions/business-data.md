<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# What would be the high level data entities/models found in many small businesses? eg. products, services, customers, sales, team members, projects, tasks, etc

This is the foundational design decision for the platform — getting these entities right determines how well the agents can reason across the business. Here's a comprehensive model organised by domain, designed for an SMB context where simplicity matters as much as completeness.

## The Core Entity Domains

### 👤 People \& Relationships

The relational core of every business — who the business knows and how they're connected.

- **Contact** — the universal person record (name, email, phone, address); both customers and suppliers start here
- **Customer** — extends Contact with commercial relationship data (acquisition source, lifetime value, status, segments)
- **Supplier / Vendor** — extends Contact with procurement data (payment terms, lead times, categories)
- **Team Member** — extends Contact with employment data (role, rate, start date, permissions)
- **Lead** — a prospective customer not yet converted (source, score, stage)

***

### 🏪 Offerings

What the business sells or delivers.

- **Product** — physical or digital goods (SKU, price, cost, inventory count, unit)
- **Service** — time or expertise sold (description, rate type, duration estimate)
- **Package / Bundle** — a named grouping of products/services sold together
- **Price List** — named pricing sets (standard, wholesale, VIP) that override default prices per customer or context

***

### 💰 Sales \& Revenue

The commercial transaction flow from interest to payment.

- **Opportunity** — a potential sale in progress (contact, estimated value, stage, probability, close date)
- **Quote** — a formal offer sent to a customer (line items, expiry, terms)
- **Order** — a confirmed sale (linked to quote or direct, fulfilment status)
- **Invoice** — a payment request (line items, due date, status: draft/sent/paid/overdue)
- **Payment** — a record of money received (amount, method, date, linked invoice)
- **Credit Note** — a reverse or partial refund against an invoice

***

### 📦 Fulfilment \& Delivery

How the work or goods get to the customer.

- **Booking / Appointment** — a scheduled service delivery (contact, service, time, location, status)
- **Job / Work Order** — a unit of work to be done (linked to order, assigned team member, status)
- **Delivery** — physical dispatch record (order, carrier, tracking, date)

***

### 💸 Finance \& Accounting

The financial health layer.

- **Expense** — a business cost (category, amount, date, supplier, receipt reference)
- **Transaction** — an atomic financial event in the internal ledger (debit/credit, account, amount, date)
- **Account (Chart of Accounts)** — financial categories (revenue, COGS, operating expenses, assets, liabilities)
- **Tax Rate** — named tax configurations (GST 10%, GST-free, etc.) applied to line items
- **Budget** — planned spending or revenue targets by period and category

***

### 📋 Work \& Operations

How the team organises and executes its work.

- **Project** — a bounded body of work with a goal, timeline, and budget (linked to customer or internal)
- **Task** — an atomic unit of work (title, assignee, due date, status, linked to project or standalone)
- **Time Entry** — a logged record of time worked (team member, task/job, duration, billable flag, rate)
- **Note** — a free-form observation attached to any entity (contact, job, project, invoice)

***

### 📣 Marketing \& Engagement

How the business reaches and retains customers.

- **Campaign** — a marketing initiative (channel, audience segment, dates, goal)
- **Message** — an individual communication sent or received (email, SMS, direction, linked contact)
- **Conversation** — a thread of messages on a channel (linked to contact, agent, status: open/resolved)
- **Segment** — a named group of contacts matching defined criteria (used for targeting)

***

### 📄 Documents \& Assets

Persistent artefacts the business creates or holds.

- **Document** — any generated file (quote PDF, contract, proposal) with metadata and blob reference
- **Template** — a reusable document or message pattern (invoice template, email template)
- **Asset** — a business-owned item (equipment, vehicle, licence) with value and maintenance records

***

### ⚙️ Platform \& Configuration

The meta-layer the agents use to understand and operate the business.

- **Business Profile** — the tenant's identity (name, ABN, address, industry, logo, contact defaults)
- **Business Rule** — named logic the agents must respect (*"always offer 30-day terms to returning customers"*)
- **Workflow** — a validated sequence of actions (the `workflows/` knowledge layer)
- **Agent Permission** — what each agent role is allowed to read, propose, or execute autonomously
- **Event Log** — the immutable record of every agent action and business event (the append-only store)
- **Learning** — a stored correction or preference extracted from owner feedback

***

## How They Relate

The key relationships that make the agent's reasoning coherent:

```
Contact ──────── is a ──────── Customer
                            └── Supplier
                            └── Team Member
                            └── Lead

Customer ─── has many ─── Opportunities ─── become ─── Quotes ─── become ─── Orders
                                                                         └── Invoices ─── have ─── Payments

Order ─── fulfilled via ─── Booking / Job / Delivery

Job ─── assigned to ─── Team Member
    └── tracked via ─── Time Entries
    └── part of ─── Project ─── has many ─── Tasks

Invoice ─── line items reference ─── Products / Services / Packages
        └── applies ─── Tax Rate
        └── overridden by ─── Price List

Any entity ─── can have ─── Notes, Documents, Messages
Any action  ─── writes to ─── Event Log
```


***

## Agent-Specific Entities (the `agent_` schema)

Following the Dash dual-schema pattern, the agents build *derived* entities on top of the business data — never modifying source records:

- **customer_health_score** — computed from payment history, engagement, support tickets
- **cashflow_forecast** — projected from open invoices, recurring orders, known expenses
- **churn_risk** — signals from usage patterns, overdue payments, complaint history
- **job_profitability** — actual vs estimated time and cost per job or project
- **monthly_summary** — pre-aggregated financial snapshot used for conversational reporting

***

## Industry Variations to Plan For

Not every SMB needs every entity — the onboarding conversation should activate the right subset:


| Business Type | Primary Entities | Less Relevant |
| :-- | :-- | :-- |
| Trades / Services | Booking, Job, Time Entry, Invoice | Product inventory, Campaign |
| Retail | Product, Order, Delivery, Inventory | Project, Time Entry |
| Consulting / Freelance | Project, Task, Time Entry, Invoice | Delivery, Inventory |
| Hospitality / Food | Booking, Product, Order, Supplier | Project, Campaign |
| Professional Services | Contact, Opportunity, Document, Invoice | Inventory, Delivery |

The platform activates entity groups based on business type at onboarding, and the Builder Agent can extend the schema as the business evolves — exactly as Dash's Engineer creates new views when new data patterns emerge.
<span style="display:none">[^1][^10][^11][^12][^13][^14][^15][^2][^3][^4][^5][^6][^7][^8][^9]</span>

<div align="center">⁂</div>

[^1]: https://learn.microsoft.com/en-us/dynamics365/customer-insights/data/table-schemas

[^2]: https://www.nigelfrank.com/insights/microsoft-dynamics-365-the-common-data-model-explained/

[^3]: https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/data-entities

[^4]: https://www.linkedin.com/pulse/common-data-model-what-how-does-relate-your-microsoft-sharon-smith

[^5]: https://www.epcgroup.net/ms-dynamics-365-common-data-model-explained

[^6]: https://business.adobe.com/blog/basics/what-is-data-modeling

[^7]: https://erpsoftwareblog.com/2017/07/powerapps-flow-common-data-model-pillars-of-d365/

[^8]: https://erstudio.com/blog/entity-relationship-models-and-diagrams-explained-with-er-studio/

[^9]: https://www.beyondkey.com/blog/dynamics-365-common-data-model/

[^10]: https://opentextbc.ca/dbdesign01/chapter/chapter-8-entity-relationship-model/

[^11]: https://www.pa.com.au/media/sifbw4ed/common-data-model-poster.pdf

[^12]: https://www.strategy.com/software/blog/want-your-business-to-be-more-efficient-you-need-data-modeling

[^13]: https://cobalt.net/dynamics-365-finally-right-sized-crmerp-system-smbs/

[^14]: https://en.wikipedia.org/wiki/Entity–relationship_model

[^15]: https://dynatechconsultancy.com/blog/unlocking-the-power-of-microsoft-dynamics-365-with-the-common-data-model-a-comprehensive-guide

