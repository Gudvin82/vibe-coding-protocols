# Production Error Capture

Purpose: capture real production errors safely into a local error inbox.

Core principle:

```text
Capture real production errors safely. Do not fix, deploy, root-cause, or change production from the monitor.
```

## Read-only boundary

- Read-only only.
- Inspect a bounded recent window, default 30 minutes.
- Use the project-documented canonical log path.
- Filter real errors only.
- Ignore access-log noise and healthy events.
- Write only minimal useful error records into `.vcp/runtime/error-inbox/`.
- Do not search for root cause here.
- Do not fix here.
- Do not deploy here.
- Do not change config here.
- Do not store secrets, tokens, cookies, raw authorization headers, or personal data.
- Do not commit runtime error files.

## Required discovery before monitoring

Before any monitoring run, identify:

- production environment name;
- service, container, worker, or gateway identifiers;
- API gateway, proxy, or edge log source if applicable;
- canonical log access command or documented path;
- allowed time window;
- allowed log levels or filters;
- redaction requirements;
- monitor owner;
- whether access is authorized.

Examples of acceptable discovery sources:

- runbook;
- documented shell command;
- cloud logging CLI wrapper;
- container logging instruction;
- platform dashboard instructions;
- Terraform or infra outputs;
- `Makefile`, `justfile`, or ops script.

If no documented log path exists:

- stop and ask;
- do not invent commands;
- do not invent credentials;
- do not scrape dashboards;
- do not bypass access control.

## Error filtering rules

Capture candidates such as:

- `ERROR` level entries;
- exceptions and stack traces;
- `5xx` responses when they indicate a real error;
- unhandled rejections;
- suspicious auth, payment, session, or state-transition anomalies;
- failed migrations;
- webhook failures;
- dead-letter or poison-queue events;
- timeout spikes;
- repeated critical failures;
- gateway or edge errors when they are truly error-level.

Ignore by default:

- ordinary access logs;
- `INFO` noise;
- healthchecks;
- 2xx and 3xx traffic;
- expected 4xx unless suspicious;
- known benign noise;
- duplicate repeats after one representative record is captured.

Deduplicate repeated identical failures into one inbox entry with:

- count;
- first seen;
- last seen;
- one redacted trace fragment.

## Safe error inbox

Preferred runtime location:

```text
.vcp/runtime/error-inbox/
```

Why not root `errors/`:

- easier to commit by accident;
- easier to confuse with source files;
- less obviously runtime-only.

Safe filename pattern:

```text
.vcp/runtime/error-inbox/YYYY-MM-DD_HHMM_<safe_error_slug>.md
```

Redaction rules:

- replace tokens with `[REDACTED_TOKEN]`;
- replace cookies with `[REDACTED_COOKIE]`;
- replace auth headers with `[REDACTED_AUTH_HEADER]`;
- avoid full request or response bodies;
- keep only minimal context needed for triage;
- if PII is present, summarize rather than paste raw values.

## Output requirements

A capture run should leave:

- one or more error inbox entries using `templates/reports/error-inbox-entry.md`;
- a short capture summary using `templates/reports/production-error-capture-report.md`;
- zero production changes.

## Stop conditions

Stop or escalate if:

- the task would require changing production state;
- the command path is undocumented;
- the log source is not authorized;
- the data cannot be safely redacted;
- the error appears P0 or P1 and needs immediate human escalation;
- the monitor would need root-cause analysis to continue.

## What success looks like

Success is not “issue fixed”.
Success is:

- real errors were captured safely;
- noise was filtered;
- redaction was preserved;
- follow-up can happen through triage, backlog, hardening, review, or maintenance.
