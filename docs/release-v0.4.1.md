# Vibe Coding Protocols v0.4.1 — Security Policy and Maintenance Adoption Polish

## Summary

`v0.4.1` sharpens repository security policy,
clarifies what maintenance refactoring should and should not do,
and makes maintenance-lane adoption easier for existing users.

## What changed

- rewrote the public repository security policy;
- added a methodology-scope explainer for security-related expectations;
- added maintenance risk classification and escalation rules;
- added allowed exceptions for mature design-system and headless UI cases;
- improved maintenance report templates with practical guidance;
- added filled synthetic maintenance report examples;
- added a migration guide for existing users adopting maintenance artifacts;
- added an honest tooling roadmap.

## Maintenance adoption focus

This patch does not add a new methodology lane.
It clarifies how to use the existing maintenance routes responsibly,
especially for post-MVP projects that already work.

## Security scope

See:
- [../SECURITY.md](../SECURITY.md)
- [security-methodology-scope.md](./security-methodology-scope.md)

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
- public root `AGENTS.md`;
- public root `PROJECT_MAP.md`.
