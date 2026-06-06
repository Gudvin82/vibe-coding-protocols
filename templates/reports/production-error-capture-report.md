<!-- vcp-version: v0.9.2 -->
<!-- vcp-version: v0.9.1 -->
<!-- vcp-version: v0.9.0 -->
<!-- methodology-version: v1.4 -->
<!-- vcp-version: v0.8.4 -->

<!-- vcp-version: v0.8.2 -->

<!-- vcp-artifact: PRODUCTION_ERROR_CAPTURE_REPORT -->
<!-- vcp-version: v0.8.2 -->

# Production Error Capture Report

## Monitoring scope

State the environment, service, and authorized log source used.

## Discovery confirmation

Record the documented log command or path, time window, and owner/authorization status.

## Capture window

State the exact recent window inspected.

## Filtering rules applied

Explain what counted as a real error and what was ignored as noise.

## Inbox entries created

List file paths under `.vcp/runtime/error-inbox/`.

## Redaction status

Confirm that secrets, tokens, cookies, auth headers, and personal data were redacted or omitted.

## Count summary

Note total captured errors and deduplicated groups.

## Immediate escalation

Record whether any P0/P1 signal required immediate human escalation.

## Do not do in monitor

- Do not fix here.
- Do not root-cause here.
- Do not deploy here.
