# Project Backlog

`PROJECT_BACKLOG.md` is the working kanban for tasks, ideas, bugs, production-error follow-up, review follow-up, and implementation status.
It is not the same artifact as `AUDIT_BACKLOG.md`.

## Difference from Audit Backlog

- `PROJECT_BACKLOG.md` tracks delivery work, feature requests, bug fixes, refactors, docs work, operations work, and implementation flow.
- `AUDIT_BACKLOG.md` tracks findings, hardening gaps, accepted risks, and audit evidence.

## Kanban states

- `TODO`
- `DOING`
- `DONE`
- `ARCHIVED / NOT TAKEN`

Status is represented by the section that contains the row.
The CLI exposes status explicitly when listing or reporting items.

## Standardized item fields

Required backlog data model:

- ID
- Priority
- Type
- Title
- Route
- Source
- Status
- Owner
- Created
- Updated
- Architecture impact
- Validation required
- Review required
- Linked docs
- Notes

The markdown table keeps status implicit through the section.
Everything else should be visible in the row.

## Allowed values

### Type

- `idea`
- `feature`
- `bug`
- `refactor`
- `security`
- `docs`
- `operations`
- `tech-debt`
- `api-integration`
- `review-finding`
- `prod-error`
- `audit-follow-up`

### Priority

- `P0`
- `P1`
- `P2`
- `P3`

### Source

- `user`
- `ai`
- `audit`
- `prod-error`
- `review`
- `roadmap`
- `manual`

### Route

- `Starter`
- `Hardening`
- `Maintenance`
- `UI Ownership`
- `Post-Task Review`
- `Third-party API Intake`
- `Operations`
- `Public Site`
- `Backlog`
- `Unknown`

### Architecture impact

- `none`
- `docs-only`
- `component-level`
- `cross-layer`
- `production-critical`

Small projects may keep owner, linked docs, and notes concise.
Production or shared-engine projects should fill all fields intentionally.

## ID convention

Default VCP backlog IDs use:

- `VCP-001`
- `VCP-002`
- `VCP-003`

Copied projects may use custom prefixes such as:

- `PROJECT-001`
- `SP-001`
- `AG-001`
- `APP-001`

Rules:

- IDs must be unique.
- Archived items keep their IDs.
- Do not renumber existing items.
- If an item is split, create new IDs and link the parent in notes.
- If duplicates are merged, keep the oldest ID and reference merged IDs in notes.

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
- `don't forget`

then propose adding the item to `TODO`.

If the user says:

- `doing`
- `start`
- `take this`
- `implement now`

then add or move the item to `DOING`.

If the user says:

- `done`
- `completed`
- `closed`

then move it to `DONE` only when validation and review evidence exist, or mark evidence as missing.

If the user says:

- `not now`
- `won't do`
- `archive`
- `not taking`

then move or add it to `ARCHIVED / NOT TAKEN` with reason.

## Architecture docs integration

If a backlog item changes architecture, data flow, external dependencies, auth or session logic, persistence, scoring, public API, deployment, or shared engine behavior, the agent should:

- update `PROJECT_MAP.md`;
- update `ARCHITECTURE_SOURCE_OF_TRUTH.md` if present;
- mention the change in the backlog item;
- or create a follow-up backlog item if the update cannot happen in the same task.

Architecture impact guidance:

- `none`: no architecture update required.
- `docs-only`: update relevant docs or add note.
- `component-level`: update `PROJECT_MAP.md` if ownership, file map, or route shape changed.
- `cross-layer`: update `PROJECT_MAP.md` and `ARCHITECTURE_SOURCE_OF_TRUTH.md`.
- `production-critical`: stop unless the user approves scope. Requires architecture update, validation plan, post-task review, and usually a release gate.

If architecture impact is `cross-layer` or `production-critical` and no architecture update is possible, stop and ask the user.

## Operations integration

Daily error triage should create or update backlog items for actionable errors.
Recommended mapping:

- P0 outage -> priority `P0`, type `prod-error`, route `Operations` or `Hardening`
- P1 user-impacting issue -> priority `P1`
- third-party API failure -> route `Third-party API Intake`
- regression after release -> route `Post-Task Review`
- repeated maintainability-related error -> route `Maintenance`

Backlog items created from production errors should link the inbox entry path in `Linked docs` or `Notes`.

## Post-task review integration

Review findings should become backlog items when they are:

- real but out of current scope;
- non-blocking but important;
- product decisions rather than immediate fixes;
- tech debt;
- additional testing work;
- work that cannot be safely fixed now.

Blocking findings should be fixed before `DONE` unless the user explicitly defers and accepts the risk.

## CLI surface

Current CLI surface:

```bash
python3 -m vcp_cli backlog validate
python3 -m vcp_cli backlog template
python3 -m vcp_cli backlog list --json
python3 -m vcp_cli backlog add --title "..." --type idea --priority P2 --dry-run --json
python3 -m vcp_cli backlog move --id VCP-001 --status doing --dry-run --json
python3 -m vcp_cli backlog done --id VCP-001 --validation "..." --review "..." --dry-run --json
python3 -m vcp_cli backlog archive --id VCP-001 --reason "Not in scope" --dry-run --json
python3 -m vcp_cli backlog report --json
```

Write commands create runtime backups before modification and validate the file after writing.
The CLI does not silently rewrite unrelated files.
