# /prod-log-monitor

Use this command when a project already has an authorized production log path and the safe task is read-only error capture.

## Return

- monitoring scope;
- discovered canonical log command or documented path;
- capture window;
- filtered real errors only;
- error inbox file paths created;
- redaction status;
- count of captured entries;
- explicit confirmation that no fix, deploy, or root-cause analysis was attempted.

## Rules

1. Discover the project-specific canonical log access path first.
2. Use a bounded recent window, default 30 minutes unless the project says otherwise.
3. Capture only real errors, not access-log noise.
4. Redact secrets, tokens, cookies, and personal data.
5. Write inbox entries under `.vcp/runtime/error-inbox/`.
6. Produce a short capture report.
7. Do not fix, deploy, restart, reconfigure, or root-cause from this command.

## Stop if

- no authorized log path exists;
- the required command is undocumented;
- redaction is not possible;
- the task drifts into incident handling instead of capture.
