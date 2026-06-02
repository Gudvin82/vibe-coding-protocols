# Vibe Coding Protocols v0.5.4 — Backlog CLI and Workflow Polish

v0.5.4 turns `PROJECT_BACKLOG.md` into a practical AI-assisted Kanban workflow.
It adds safer CLI operations for listing, adding, moving, validating and reporting backlog items,
improves task intake rules,
links backlog updates to architecture memory,
and keeps delivery work separate from audit findings.

## What changed

- expanded the backlog data model with stable fields for priority, source, route, owner, architecture impact, validation, review, linked docs, and notes;
- added local CLI commands for `backlog list`, `backlog add`, `backlog move`, `backlog done`, `backlog archive`, and `backlog report`;
- kept `backlog validate` and `backlog template` as structure helpers;
- added runtime backups for real backlog writes under `.vcp/runtime/backups/`;
- strengthened backlog rules in docs, prompts, report templates, and examples;
- linked backlog work to `PROJECT_MAP.md` and `ARCHITECTURE_SOURCE_OF_TRUTH.md` when architecture impact is non-trivial;
- extended manifests, benchmark scenarios, and smoke tests so backlog workflow regressions surface locally.

## Safety and scope

- `PROJECT_BACKLOG.md` remains separate from `AUDIT_BACKLOG.md`.
- Backlog writes are not destructive by default.
- Dry-run stays available for write commands.
- VCP still does not claim issue-tracker sync, external PM integration, or hidden automation against user repos.

## Validation focus

v0.5.4 extends local validation to cover:

- backlog parser and rendering stability;
- CLI write-path safety and dry-run behavior;
- manifest consistency for backlog commands and scenarios;
- benchmark coverage for backlog add/move/done/archive and architecture-impact routing;
- backup directory ignore rules.
