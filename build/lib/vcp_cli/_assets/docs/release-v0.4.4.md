# Vibe Coding Protocols v0.4.4 — Post-Task Code Review Gate

## Summary

This release adds a VCP-native post-task review gate for AI-assisted development.
Meaningful AI-generated changes should be independently reviewed and validated before the next task, merge, release or handoff.
The workflow adds read-only review, actionable findings handling, validation after fixes and clear acceptance signals.

This workflow is based on standard software engineering practice.
It is written in VCP-native language and does not copy external prompts or posts.

## What changed

- Added a dedicated review protocol family for post-task acceptance.
- Added the `/loop-code-review` command document.
- Added a reusable review prompt template and a structured code review report template.
- Added synthetic review examples for normal acceptance, no-actionable-findings acceptance and intentionally rejected findings.
- Integrated post-task review into AI intake, adoption packs, route docs, protocol index and toolkit checks.
- Added lightweight `vcp_cli` route, adopt, score and manifest smoke surfaces for the new gate.

## Why this matters

AI-generated changes can look complete while still hiding correctness bugs, scope drift, public contract changes, missing validation or maintainability issues.
Post-task review turns review plus validation into an explicit acceptance gate.

## Compatibility

- Repository package: `v0.4.4`
- Methodology version remains `v1.4`
- Existing Starter, Hardening, Maintenance, UI Ownership and Extended routes remain intact.
- This release adds a change-set review gate on top of those routes.

## Validation

- `python3 scripts/check-newlines.py`
- `python3 scripts/validate-links.sh`
- `bash scripts/check-version-consistency.sh`
- `bash scripts/check-toolkit.sh`
- `bash scripts/vibe-check.sh --audit --json`
- `python3 -m vcp_cli --help`
- `python3 -m vcp_cli score --json`
- `python3 -m vcp_cli manifest validate`

## Known WARN-only items

- historical `API_KEY` marker in git history
- historical `SECRET` marker in git history
- public root `AGENTS.md`
- public root `PROJECT_MAP.md`
