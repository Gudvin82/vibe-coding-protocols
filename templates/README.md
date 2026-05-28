# Templates

This is the copy-ready artifact pack for your own project.

## Which agent file should I copy?

- Root `AGENTS.md` configures this repository.
- Root `CLAUDE.md` configures Claude Code for this repository.
- Do not copy root `AGENTS.md` blindly into your project.
- For your own project, copy `templates/AGENTS.md` as `AGENTS.md`.
- For Claude Code, use `templates/AGENTS.claude.md` or adapt it into your project's `CLAUDE.md`.
- For Cursor or Windsurf, use `templates/AGENTS.cursor.md` or `templates/AGENTS.windsurf.md`.

## Version markers

Copy-ready templates include lightweight markers such as:

```html
<!-- vcp-artifact: AGENTS -->
<!-- vcp-version: v0.4.0 -->
<!-- methodology-version: v1.4 -->
```

These markers help you compare local copies with newer toolkit versions.
Review changes manually.
Do not overwrite customized local files blindly.

## Core memory files across the toolkit

- `README.md`
- `AGENTS.md` or `CLAUDE.md`
- `PROJECT_MAP.md`
- `ARCHITECTURE_MAP.md`, when multiple surfaces need a compact plan
- `ARCHITECTURE_SOURCE_OF_TRUTH.md`, if needed
- `AUDIT_BACKLOG.md`, for hardening
- `docs/PROMPTS.md` or `PROMPTS.md`, if prompts are tracked
- `SECURITY.md` or `SECURITY_BASELINE.md`, for public or production projects
- `METRICS_BOARD.md`, if you want to track adoption with real project data

## Planning artifacts

- [ARCHITECTURE_MAP.md](./ARCHITECTURE_MAP.md)
- [PROJECT_MAP.md](./PROJECT_MAP.md)
- [ARCHITECTURE_SOURCE_OF_TRUTH.md](./ARCHITECTURE_SOURCE_OF_TRUTH.md)
- [reports/refactoring-report.md](./reports/refactoring-report.md)
- [reports/ui-refactoring-report.md](./reports/ui-refactoring-report.md)

## Filled synthetic examples

- [examples/AUDIT_BACKLOG.filled.example.md](./examples/AUDIT_BACKLOG.filled.example.md)
- [examples/THIRD_PARTY_REGISTRY.filled.example.md](./examples/THIRD_PARTY_REGISTRY.filled.example.md)
- [examples/SECURITY_OPERATIONS_BASELINE.filled.example.md](./examples/SECURITY_OPERATIONS_BASELINE.filled.example.md)

## Recommended companions

- [../docs/architecture-map.md](../docs/architecture-map.md)
- [../docs/artifact-versioning.md](../docs/artifact-versioning.md)
- [../docs/update-copied-artifacts.md](../docs/update-copied-artifacts.md)
- [../docs/ide-rules-dry-policy.md](../docs/ide-rules-dry-policy.md)
- [../docs/hardening-thresholds.md](../docs/hardening-thresholds.md)
- [../docs/release-readiness.md](../docs/release-readiness.md)
- [../docs/scanner-integration.md](../docs/scanner-integration.md)
- [../docs/migration/README.md](../docs/migration/README.md)

Important:
- these are public templates;
- these are not real private project docs;
- real `AGENTS.md`, `PROJECT_MAP.md`, `ARCHITECTURE.md`, incident docs and internal runbooks often contain sensitive details and should stay private, sanitized or encrypted.
