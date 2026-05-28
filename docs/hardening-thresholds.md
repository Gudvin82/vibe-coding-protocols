# Hardening Thresholds

Use these thresholds as release gates and readiness hints, not as guarantees.

| Gate | Can move forward? | Blockers | Evidence |
|---|---|---|---|
| Lite | Local MVP only | no `AGENTS.md` or `PROJECT_MAP.md` | `vibe-check --starter` |
| Starter | First vertical slice | no Product Brief or no active surface | `PROJECT_MAP.md` + Product Brief |
| Hardening | Staging candidate | secrets, no `AUDIT_BACKLOG.md`, unknown deploy path | hardening report |
| Extended | Production candidate | auth, payments or personal data without review | scanner evidence + rollback |
| Release | Deploy | unresolved critical or high risk | release readiness report |

## Gate statuses

- `READY`
- `READY WITH RISKS`
- `BLOCKED`
- `NOT ASSESSED`

## Rules

- If auth, payments, personal data or public exposure exist, do not make a production-ready claim without Extended review.
- `vibe-check` is not a security certification.
- A green or warn-only check does not replace human review, rollback planning or environment-specific testing.

## Baseline expectations

- `AUDIT_BACKLOG.md` exists when AI-generated code already exists.
- `PROJECT_MAP.md` names active and deferred surfaces.
- `ARCHITECTURE_MAP.md` exists when the project has multiple surfaces or unclear boundaries.
- `vibe-check --hardening` or `--audit` runs without FAIL.
- deploy assumptions, owners and rollback notes are explicit enough to review.
