# Security Operations

## Why one-time audit is not enough

A one-time audit helps you classify the current state.
Security operations is what keeps the project from drifting back into risk.

## What security operations means here

- recurring checks instead of one-off cleanup;
- clear owners;
- evidence for scans and reviews;
- patch/update policy;
- alerting and escalation;
- accepted risks review;
- backup/restore discipline.

## Recurring security hygiene

Typical recurring checks:
- secret scan;
- dependency scan;
- public exposure check;
- open ports/service inventory;
- security headers review;
- admin access review;
- backup/restore drill;
- third-party registry review.

## Evidence and backlog

Do not rely on memory or chat history.
Store evidence in:
- scanner reports;
- CI logs;
- screenshots;
- manual review notes;
- `AUDIT_BACKLOG.md`;
- `SECURITY_OPERATIONS_BASELINE.md`.

## Owners and accepted risks

Each recurring check needs an owner.
Each accepted risk needs a date, reason and next review point.

## Incident review

When something breaks or leaks:
- capture the timeline;
- classify blast radius;
- rotate/revoke what is needed;
- update the backlog;
- decide what recurring control was missing.
