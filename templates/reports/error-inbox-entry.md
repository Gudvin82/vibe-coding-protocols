<!-- vcp-artifact: ERROR_INBOX_ENTRY -->
<!-- vcp-version: v0.5.4 -->
<!-- methodology-version: v1.4 -->

# Error Inbox Entry

## Summary

Short redacted summary of the error signature.

## First seen

## Last seen

## Source

Name the log stream, platform, or documented command source.

## Environment

## Service / container / gateway

## Severity

Use one of: `P0 outage`, `P1 user-impacting`, `P2 degraded behavior`, `P3 background/noise but real`.

## Count / repetition

State whether this is one event or a deduplicated group.

## Minimal trace

Keep only the shortest safe trace fragment needed for triage.

## Redacted context

Summarize request, route, state, or job context without leaking sensitive material.

## Suspected category

Use one of:
- auth/session
- payment/billing
- state transition
- third-party API
- database
- infrastructure
- API gateway
- frontend/runtime
- unknown

## User impact

## Related deploy / release

## Secrets / PII redaction status

Confirm what was removed or generalized.

## Next triage action

## Links

## Do not do in monitor

- Do not fix here.
- Do not root-cause here.
- Do not deploy here.
