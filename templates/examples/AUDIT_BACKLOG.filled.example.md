<!-- vcp-version: v0.7.0 -->

<!-- vcp-artifact: AUDIT_BACKLOG_FILLED_EXAMPLE -->
<!-- vcp-version: v0.7.0 -->
<!-- methodology-version: v1.4 -->

# Filled Audit Backlog Example

> Synthetic filled example — not a real case study.

## Why this exists

Use this only as a formatting and quality example.
Do not treat the items below as production advice.

## Critical

| ID | Category | Task | Risk | Evidence | Discovered by | Status | Owner |
|---|---|---|---|---|---|---|---|
| SEC-001 | Security | Move hard-coded admin token to env | Token reuse could expose admin actions | `src/auth.js:14` | AI | Open | backend owner |

## High

| ID | Category | Task | Risk | Evidence | Discovered by | Status | Owner |
|---|---|---|---|---|---|---|---|
| TEST-001 | Tests | Add auth regression test | Auth fix could regress silently | `tests/` missing route coverage | human | In progress | QA owner |
