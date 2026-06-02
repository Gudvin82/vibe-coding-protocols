# Automation Guidance

Use automation only for bounded, read-only, repetitive tasks unless the project explicitly defines a stronger workflow.

## Safe automation fit

Production Error Capture is a reasonable automation candidate because it is:

- read-only;
- time-bounded;
- repetitive;
- redaction-focused;
- not a deploy or fix workflow.

## Recommended automation prompt shape

- read only;
- use the project-documented log command;
- inspect only the recent window, default 30 minutes;
- filter real errors only;
- redact secrets and personal data;
- write to `.vcp/runtime/error-inbox/`;
- no root cause;
- no fixes;
- no commits;
- report count and file paths.

## Scheduling options

Conceptually acceptable choices include:

- Codex automations when available;
- Claude scheduled workflows when available;
- cron jobs;
- GitHub Actions scheduled workflows for non-production-safe dry runs only;
- external monitoring or observability systems that call the workflow safely.

## Model guidance

- use a cheaper or smaller model for bounded capture when reliability is acceptable;
- use stronger model or human review for triage, hardening, or fixes.

## Never automate by default

- production fixes;
- deploys;
- restarts;
- root-cause analysis claims;
- secret handling outside documented redaction policy.
