# AUDIT_BACKLOG

| ID | Finding | Discovered by | Evidence | Severity | Owner | Status | Next step |
|---|---|---|---|---|---|---|---|
| ENV-001 | Earlier starter slice had no `.env.example` for config guidance | human | starter review notes | Medium | starter owner | Fixed | keep `.env.example` in sync with config changes |
| VAL-001 | Input validation only checks title length and type | AI | `src/index.js` request parsing | Medium | backend owner | Open | add stronger schema validation before public deploy |
| ERR-001 | Error handling is minimal and not structured for observability | human | `src/index.js` catch blocks return generic JSON | Medium | backend owner | Open | add structured error logging policy |
| ABUSE-001 | No rate-limit note for create/complete endpoints | AI | routes `/api/tasks` and `/api/tasks/:id/complete` | High | security owner | Open | document rate-limit expectations in Security Baseline |
| TEST-001 | No test yet for invalid JSON request body | human | `tests/smoke.test.js` covers health/create/complete only | Medium | QA owner | Open | add invalid-body and malformed payload tests |
| DEP-001 | Dependency review not run for future additions | scanner | no third-party registry in example folder | Low | maintainer | Open | document third-party intake before adding packages |
| LOG-001 | Logging policy missing for request, error and abuse events | AI | architecture and code review | Medium | platform owner | Open | define minimal logging and retention guidance |
