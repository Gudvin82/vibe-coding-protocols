# Vibe Coding Protocols v0.4.3 — AI Intake and Adoption Accuracy

## Summary

v0.4.3 adds an explicit AI Intake layer so Claude Code, Codex, Cursor,
Windsurf, Copilot, and other AI agents classify the target project before
judging or applying VCP.
It adds route classification, adoption packs, minimum inspection rules, and
structured adoption assessment reports to reduce shallow repository skims.

## What changed

- Added `AI_INTAKE.md` as the first file an AI agent should read before evaluating VCP.
- Added a target project classifier with route defaults and synthetic examples.
- Added adoption packs so agents choose scoped file sets instead of copying artifacts randomly.
- Added a copy-paste evaluation prompt for repository adoption.
- Added a structured adoption assessment report template.
- Added a synthetic shared-engine production example for dual-product risk.
- Updated README, START_HERE, protocol index and toolkit checks so the intake layer is discoverable.

## Compatibility

- Methodology version remains `v1.4`.
- Existing routes stay intact.
- This release adds a route-selection and adoption-accuracy layer on top of current protocols.

## Validation

- `python3 scripts/check-newlines.py`
- `python3 scripts/validate-links.sh`
- `bash scripts/check-version-consistency.sh`
- `bash scripts/check-toolkit.sh`
- `bash scripts/vibe-check.sh --audit --json`

## Known WARN-only items

- historical `API_KEY` marker in git history
- historical `SECRET` marker in git history
- public root `AGENTS.md`
- public root `PROJECT_MAP.md`
