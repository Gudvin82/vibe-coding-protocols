<!-- vcp-version: v0.8.7 -->
<!-- methodology-version: v1.4 -->
<!-- vcp-version: v0.8.4 -->

<!-- vcp-version: v0.8.2 -->

<!-- vcp-artifact: DAILY_ERROR_TRIAGE_PROMPT -->
<!-- vcp-version: v0.8.2 -->

Review existing `.vcp/runtime/error-inbox/` entries only after capture exists.
Deduplicate repeated errors, classify severity, note user impact, and decide the next safe route.
Create or update `PROJECT_BACKLOG.md` items before any implementation begins.
Update `AUDIT_BACKLOG.md` when the issue is a hardening or risk signal.
Escalate P0 and P1 immediately.
Do not fix production automatically from triage.
