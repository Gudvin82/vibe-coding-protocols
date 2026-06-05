# Daily Error Triage

Purpose: review accumulated error inbox entries and decide what happens next.

Daily triage is separate from monitoring.
The monitor captures.
Triage classifies and routes.
Fixes happen only in a separate user-approved task.

## What daily triage may do

- deduplicate similar inbox entries;
- classify severity;
- classify suspected category;
- estimate user impact;
- link entries to backlog items;
- decide whether Hardening, Post-Task Review, Third-party API Intake, Maintenance, or Operations follow-up is needed;
- propose fix order;
- archive resolved or benign-noise entries;
- escalate P0 or P1 findings immediately.

## What daily triage must not do automatically

- do not fix production here;
- do not deploy here;
- do not restart services here;
- do not change configuration here;
- do not claim root cause unless a separate investigation was run;
- do not mark issues resolved without evidence.

## Severity guide

- `P0 outage`: broad outage or unusable critical path;
- `P1 user-impacting`: production problem hitting real users or money flow;
- `P2 degraded behavior`: partial failure, retries, intermittent degradation;
- `P3 background/noise but real`: low user impact, still worth tracking.

## Required outputs

A triage pass should leave:

- an updated daily triage report;
- linked `PROJECT_BACKLOG.md` items when follow-up work is needed;
- linked `AUDIT_BACKLOG.md` items if the issue is a risk or hardening finding;
- escalation note for any P0/P1 item.

## P0 / P1 rule

P0 and P1 items should not wait for the next daily batch.
Escalate immediately and stop treating the issue as routine backlog grooming.
