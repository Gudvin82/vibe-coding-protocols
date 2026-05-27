# Hardening Thresholds

Use these thresholds as readiness hints, not as guarantees.

## Baseline expectations

- `AUDIT_BACKLOG.md` exists if AI-generated code already exists.
- `PROJECT_MAP.md` exists and names the active/deferred surface.
- `vibe-check --hardening` or `--audit` runs without FAIL.
- major auth, payments, deploy or public-exposure risks are explicit.

## When to move to Extended Protocol

Move to [Extended Protocol](../protocols/ai-project-extended-protocol.md) when the project is:
- public;
- client-facing;
- production-bound;
- handling auth, payments or personal data.

## Notes

Thresholds are a forcing function for review.
They do not replace tests, security work or human judgment.
