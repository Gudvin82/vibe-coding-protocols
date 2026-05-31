# Vibe Coding Protocols v0.5.1 — Windows-first CLI and Third-party API Intake

## Summary

v0.5.1 improves VCP for Windows developers by making the Python CLI
the preferred cross-platform path and reducing Bash-only friction.
It also adds a Third-party API Intake Protocol so AI agents must
classify, document and review external API dependencies before adding
them to a project.

## What changed

- Python-native `vcp check --fast` path for core validation.
- `doctor` now reports OS, shell, Bash and PowerShell-first capability.
- Windows launchers added in `bin/vcp.cmd` and `bin/vcp.ps1`.
- Windows CI parity path can validate the Python CLI without Bash.
- New Third-party API Intake protocol, command, prompt and report template.
- `THIRD_PARTY_REGISTRY` improved for compact and extended review use.
- New integration examples and benchmark scenario.

## Safety note

VCP does not auto-connect external APIs.
Public or free API does not mean production-safe.
No external API dependency should reach production code without intake, registry review, fallback planning and post-task review.

## Compatibility

- methodology version remains `v1.4`;
- Bash scripts remain supported;
- Linux and macOS workflows remain valid;
- Windows PowerShell is now the preferred cross-platform core CLI path.

## Validation

Required local validation:
- `python3 scripts/check-newlines.py`
- `python3 scripts/validate-links.sh`
- `bash scripts/check-version-consistency.sh`
- `bash scripts/check-toolkit.sh`
- `bash scripts/vibe-check.sh --audit --json`
- `python3 -m vcp_cli check --fast --json`
- `python3 -m vcp_cli route --profile third-party-api --json`
- `python3 -m vcp_cli manifest validate`
- `python3 -m vcp_cli benchmark run`
