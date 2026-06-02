<!-- vcp-artifact: AUDIT_BACKLOG -->
<!-- vcp-version: v0.5.4 -->
<!-- methodology-version: v1.4 -->

# Audit Backlog

Use this backlog to record findings after Hardening or Extended review.

## How to use

- Do not ask AI to fix everything at once.
- Move findings into a backlog before implementation starts.
- Separate Critical and High from the rest.
- Every item should have an owner, status, evidence and discovery source.
- Record accepted risks explicitly, not in chat history.

## Statuses

- Open
- In progress
- Waiting review
- Fixed
- Verified
- Deferred
- Accepted risk

## Critical

| ID | Category | Task | Risk | Evidence | Discovered by | Status | Owner |
|---|---|---|---|---|---|---|---|
| SEC-001 | Security | [FILL IN: short task] | [FILL IN: why it matters] | [FILL IN: file, command or screenshot] | human / AI / scanner / user report | Open | [FILL IN] |
| PAY-001 | Payments | [FILL IN: short task] | [FILL IN: why it matters] | [FILL IN: file, command or screenshot] | human / AI / scanner / user report | Open | [FILL IN] |

## High

| ID | Category | Task | Risk | Evidence | Discovered by | Status | Owner |
|---|---|---|---|---|---|---|---|
| DEP-001 | Supply Chain | [FILL IN: short task] | [FILL IN: why it matters] | [FILL IN: file, command or screenshot] | human / AI / scanner / user report | Open | [FILL IN] |
| LEGAL-001 | Legal | [FILL IN: short task] | [FILL IN: why it matters] | [FILL IN: file, command or screenshot] | human / AI / scanner / user report | Open | [FILL IN] |

## Medium

| ID | Category | Task | Risk | Evidence | Discovered by | Status | Owner |
|---|---|---|---|---|---|---|---|
| QA-001 | Device QA | [FILL IN: short task] | [FILL IN: why it matters] | [FILL IN: file, command or screenshot] | human / AI / scanner / user report | Open | [FILL IN] |
| TEST-001 | Tests | [FILL IN: short task] | [FILL IN: why it matters] | [FILL IN: file, command or screenshot] | human / AI / scanner / user report | Open | [FILL IN] |

## Low

| ID | Category | Task | Risk | Evidence | Discovered by | Status | Owner |
|---|---|---|---|---|---|---|---|
| DOC-001 | Documentation | [FILL IN: short task] | [FILL IN: why it matters] | [FILL IN: file, command or screenshot] | human / AI / scanner / user report | Open | [FILL IN] |

## Accepted risks

| ID | Risk | Why accepted | Review date | Owner |
|---|---|---|---|---|
| RISK-001 | [FILL IN: accepted risk] | [FILL IN: why accepted] | [FILL IN] | [FILL IN] |

## Categories

- Security
- Supply Chain
- Architecture
- Tests
- Monitoring
- DevOps
- Documentation
- UX
- Performance
- Data / Privacy
- AI / Cost
- Legal
- Compliance
- Payments
- Fiscalization
- Device QA
- Browser QA
- Accessibility
- Analytics / Cookies
- Marketing consent

## Mini-rules

- Critical items block merge or deploy until there is an explicit decision.
- High items should have a fix plan before production.
- Medium and Low can be planned, but should not disappear.
- If a risk is accepted, it should be an explicit decision with a review date.
