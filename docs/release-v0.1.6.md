# Vibe Coding Protocols v0.1.6 — Enforcement and runnable example

This release deepens the toolkit as an engineering workflow, not just a document set.

## Added

- stronger `vibe-check.sh` with `--help`, `--json`, lockfile checks and richer secret-pattern detection
- `scripts/install-hooks.sh` for optional local pre-commit guardrails
- runnable synthetic example in `examples/todo-app-starter/`
- modular prompts in `prompts/modules/`
- `prompts/backlog-to-issues-prompt.md`
- IDE-specific AGENTS templates for Claude, Cursor and Windsurf
- docs navigation indexes under `docs/guides`, `docs/reference`, `docs/community`, `docs/releases` and `docs/roadmap`
- migration notes for `v0.1.4 -> v0.1.5` and `v0.1.5 -> v0.1.6`

## Improved

- token-aware discovery with a clearer discovery-agent pattern
- AGENTS stop conditions and approval gates
- `AUDIT_BACKLOG.md` tracking with `Discovered by`
- `PROMPTS.md` tracking for failed or rejected attempts
- architecture template onboarding with fill levels
- security baseline wording for CSP and related browser headers

## Notes

- External scanners remain optional.
- This is a readiness toolkit, not a security certification.
- No fake case studies were added.
- `master-prompt-full.md` remains available next to modular prompts.
