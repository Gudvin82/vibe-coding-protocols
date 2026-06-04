<!-- vcp-artifact: PROD_LOG_MONITOR_PROMPT -->
<!-- vcp-version: v0.6.6 -->
<!-- methodology-version: v1.4 -->

Read the project-specific operations docs first.
Discover the canonical authorized production log command or log path before doing anything else.
Use a bounded recent window, default 30 minutes unless the project documents another window.
Capture real errors only.
Ignore access-log noise and healthy events.
Redact secrets, tokens, cookies, authorization headers, and personal data.
Write safe inbox entries under `.vcp/runtime/error-inbox/`.
Produce a short capture report with count and file paths.
Do not fix, do not root-cause, do not deploy, do not change configuration, and do not commit runtime files.
