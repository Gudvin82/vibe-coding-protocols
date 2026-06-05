# Launch Decision Checklist

Repository package: `v0.8.4`

This checklist is a local launch decision aid.
It is not a production certification.

## Status labels

- `go`
- `go-with-warnings`
- `no-go`
- `needs-human-review`
- `not-applicable`

## Checklist

1. Product intent clear.
2. First user journey documented.
3. Install/run path works.
4. Environment variables documented.
5. Tests or checks are present.
6. API/contracts risks reviewed if applicable.
7. Auth/billing/data boundaries reviewed if applicable.
8. Proof layer present or explicitly missing.
9. PR Gate status reviewed.
10. Release version surfaces synchronized.
11. Known blockers listed.
12. Human owner assigned.
13. Next action selected.

## How to use it

Use this after route selection, proof review, backlog review, PR Gate review, and dashboard generation.

Recommended companion docs:
- `docs/mvp-to-launch-path.md`
- `docs/pr-gate-approval-model.md`
- `docs/proof-layer.md`
- `docs/project-memory.md`
- `docs/audit-backlog.md`
- `docs/dashboard.md`

## Boundaries

- local review aid only;
- no deploy action;
- no publish action;
- no readiness guarantee;
- no production certification.
