# Vibe Coding Protocols v0.4.0 — Maintenance Refactoring Protocols

## Summary

`v0.4.0` adds a post-MVP maintenance lane for existing AI-generated projects:
scoped behavior-preserving refactoring, challenge checkpoints,
characterization tests and UI component ownership cleanup.

## What changed

- added a first-class maintenance route for existing working projects;
- added a dedicated UI ownership cleanup route for frontend refactoring;
- added operational commands for both routes;
- added reusable report templates for refactoring passes;
- updated route selection docs, protocol indexes and version references.

## New protocols

- `protocols/maintenance/README.md`
- `protocols/maintenance/care-refactoring.md`
- `protocols/maintenance/ui-refactoring.md`

## New commands

- `commands/care-refactoring.md`
- `commands/ui-refactoring.md`

## New templates

- `templates/reports/refactoring-report.md`
- `templates/reports/ui-refactoring-report.md`

## When to use

Use this release when a project already works but is becoming hard to maintain,
risky to extend, duplicated, visually inconsistent or difficult to understand.
A valid outcome may still be: no changes needed.

## Compatibility

- repository package: `v0.4.0`
- methodology version: `v1.4`
- existing starter and hardening routes remain supported

## Validation

Recommended checks:
- `python3 scripts/check-newlines.py`
- `python3 scripts/validate-links.sh`
- `bash scripts/check-version-consistency.sh`
- `bash scripts/check-toolkit.sh`
- `bash scripts/vibe-check.sh --audit --json`

## Known WARN-only items

Typical WARN-only items may still include:
- `API_KEY` marker in git history;
- `SECRET` marker in git history;
- public root `AGENTS.md` in a public repository.
