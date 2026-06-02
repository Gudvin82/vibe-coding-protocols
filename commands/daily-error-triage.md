# /daily-error-triage

Use this command after one or more error inbox entries already exist.

## Return

- deduplicated triage summary;
- severity and user-impact classification;
- linked backlog items created or updated;
- whether follow-up belongs in Hardening, Maintenance, Review, Third-party API Intake, or a separate fix task;
- escalations required;
- archived or retained inbox entries.

## Rules

1. Review inbox entries only after capture exists.
2. Classify severity and suspected category.
3. Add or update `PROJECT_BACKLOG.md` items before implementation work starts.
4. Update `AUDIT_BACKLOG.md` when the issue is a real hardening or risk signal.
5. Escalate P0 and P1 immediately.
6. Do not fix production automatically.
