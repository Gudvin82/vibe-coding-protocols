# Production Observability

VCP does not replace a monitoring stack.
It adds a controlled AI-assisted workflow around production observations that teams already own.

## What VCP adds

- read-only production error capture;
- safe redaction discipline;
- local runtime error inbox records;
- separation between capture and triage;
- routing from real errors into backlog, hardening, maintenance, or review.

## What VCP does not add

- a hosted logging product;
- automatic root-cause analysis;
- automatic remediation;
- automatic deploy or rollback;
- incident management certification.

## Safe default

If the only safe action is observation, use Production Error Capture first.
If action is needed later, move into Daily Error Triage and then a separate fix task.

## Recommended artifacts

- `protocols/operations/production-error-capture.md`
- `protocols/operations/daily-error-triage.md`
- `templates/reports/error-inbox-entry.md`
- `templates/reports/production-error-capture-report.md`
- `PROJECT_BACKLOG.md`
