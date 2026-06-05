<!-- vcp-artifact: AUDIT_BACKLOG -->
<!-- vcp-version: v0.2.0 -->
<!-- methodology-version: v1.4 -->

# AUDIT_BACKLOG

| ID | Category | Task | Risk | Evidence | Status | Owner |
|---|---|---|---|---|---|---|
| AUTH-001 | Auth | Add admin rate limiting | Credential abuse still possible | `app.js` has auth but no rate limit | Open | backend owner |
| OPS-001 | Logging | Add audit trail for admin actions | Sensitive admin actions are not preserved | no durable audit log yet | Open | ops owner |
