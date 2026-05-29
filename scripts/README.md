# Scripts

These are lightweight helper scripts for the toolkit itself.

## Included

- `check-toolkit.sh` — verifies required files and no empty markdown files
- `scan-placeholders.sh` — lightweight scan for secret-like placeholders
- `validate-links.sh` — validates local markdown links
- `vibe-check.sh` — lightweight starter / hardening / audit readiness check with optional strict, JSON and scanner stages
- `install-hooks.sh` — installs an optional local pre-commit hook guardrail
- `extract-prompt.sh` — prints a selected modular prompt to stdout
- `update-checksums.sh` — refreshes `SHA256SUMS` for review-first helper scripts
- `vibe-check.ps1` — lightweight Windows wrapper for the Bash-first vibe-check
- `tests/test-vibe-check-basic.sh` — lightweight Bash regression checks
- `init-project.example.sh` — review-first example for copying starter templates into a project
- `init-minimal.sh` — minimal bootstrap helper for starter / hardening / audit packs

## Script-first CLI status

VCP is currently script-first.
See [../docs/cli.md](../docs/cli.md) for the stable entrypoints and wrapper status.

## Notes

- these scripts do not replace hardening;
- they do not scan a target application in depth;
- external scanner integration in `vibe-check.sh` is optional,
  not mandatory;
- `install-hooks.sh` installs a local pre-commit hook only;
  it does not commit,
  push
  or modify production configs;
- `extract-prompt.sh` is a helper,
  not a package manager or CLI framework;
- `update-checksums.sh` helps a review-first install flow
  and does not publish or sign releases;
- `vibe-check.ps1` forwards to Bash,
  it does not reimplement the whole scanner in PowerShell;
- `init-project.example.sh` is intentionally an example,
  not an auto-installer;
- `init-minimal.sh` is not a full CLI;
  it is a small bootstrap helper;
- review `init-minimal.sh` before using it in a real project.
