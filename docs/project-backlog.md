# Project Backlog

`PROJECT_BACKLOG.md` is the working kanban for tasks, ideas, bugs, operations follow-up, and implementation status.
It is not the same artifact as `AUDIT_BACKLOG.md`.

## Difference from Audit Backlog

- `PROJECT_BACKLOG.md` tracks tasks, ideas, feature requests, bug fixes, refactors, docs work, operations work, and implementation status.
- `AUDIT_BACKLOG.md` tracks findings, hardening gaps, accepted risks, and audit evidence.

## Kanban states

- `TODO`
- `DOING`
- `DONE`
- `ARCHIVED / NOT TAKEN`

## Required item fields

Keep each item readable and include at least:

- ID
- Title
- Type: `idea`, `feature`, `bug`, `refactor`, `security`, `docs`, `operations`, `tech debt`, `API integration`
- Source: `user`, `AI`, `audit`, `prod error`, `review`, `roadmap`
- Route: `Starter`, `Hardening`, `Maintenance`, `UI Ownership`, `Post-Task Review`, `Third-party API Intake`, `Operations`, `Public Site`, `Backlog`
- Priority: `P0`, `P1`, `P2`, `P3`
- Status
- Owner
- Created
- Updated
- Linked docs
- Architecture impact
- Validation required
- Review required
- Notes

## Architecture impact field

Use one of:

- `none`
- `docs-only`
- `component-level`
- `cross-layer`
- `production-critical`

If architecture impact is `cross-layer` or `production-critical` and no architecture update is possible, stop and ask the user.

## Rules for AI agents

When a user gives a new idea, task, request, or follow-up:

- add or update a `PROJECT_BACKLOG.md` item first;
- do not silently lose ideas in chat;
- if the task is accepted, move it to `DOING`;
- when complete and validated, move it to `DONE`;
- if rejected or deferred, move it to `ARCHIVED / NOT TAKEN` with reason;
- update linked architecture docs when architecture changes;
- update `AUDIT_BACKLOG.md` if the item is an audit or security risk;
- update `THIRD_PARTY_REGISTRY.md` if external APIs or dependencies are involved;
- update the post-task review report after meaningful code changes.

If the user says:

- `add this later`
- `idea`
- `todo`
- `we should`
- `maybe`
- `after release`

then propose adding the item to `TODO`.

If the user says:

- `not now`
- `won't do`
- `archive`
- `not taking`

then move or add the item to `ARCHIVED / NOT TAKEN` with reason.

## Architecture docs integration

If a backlog item changes architecture, data flow, external dependencies, auth or session logic, persistence, scoring, public API, deployment, or shared engine behavior, the agent should:

- update `PROJECT_MAP.md`;
- update `ARCHITECTURE_SOURCE_OF_TRUTH.md` if present;
- mention the change in the backlog item;
- or create a follow-up backlog item if the update cannot happen in the same task.

## CLI surface

VCP keeps backlog CLI support intentionally lightweight:

```bash
python3 -m vcp_cli backlog validate
python3 -m vcp_cli backlog template
```

The CLI does not rewrite user backlog state automatically in v0.5.3.
Manual edits remain the default because they are safer than guessing task intent.
