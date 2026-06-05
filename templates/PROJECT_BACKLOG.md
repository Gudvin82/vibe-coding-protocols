<!-- vcp-version: v0.8.3 -->

<!-- vcp-artifact: PROJECT_BACKLOG -->
<!-- vcp-version: v0.8.3 -->
<!-- methodology-version: v1.4 -->

# Project Backlog

## Rules

- Use this backlog for tasks, ideas, bugs, operations follow-up, review follow-up, and product work.
- Keep it separate from `AUDIT_BACKLOG.md`.
- IDs must be unique and stable. Do not renumber existing items.
- If an item is split, create new IDs and reference the parent in notes.
- If duplicates are merged, keep the oldest ID and reference merged IDs in notes.
- Add or update an item before implementation starts when a new request arrives.
- If architecture impact is not `none`, update linked architecture docs in the same task or create a follow-up item.
- Example rows below illustrate the format. Replace them with real project state.

## ID convention

- Default VCP prefix: `VCP-001`, `VCP-002`, `VCP-003`
- Copied project prefixes may be customized: `PROJECT-001`, `SP-001`, `APP-001`

## TODO

| ID | Priority | Type | Title | Route | Source | Owner | Created | Updated | Architecture impact | Validation required | Review required | Linked docs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VCP-001 | P1 | operations | Example: add production error capture | Operations | roadmap | maintainer | 2026-06-02 | 2026-06-02 | docs-only | doctor + backlog validate | no | docs/production-observability.md | Example row. Safe read-only monitoring setup. |
| VCP-002 | P2 | api-integration | Example: run third-party API intake before coding | Third-party API Intake | user | maintainer | 2026-06-02 | 2026-06-02 | none | intake report required | yes | templates/THIRD_PARTY_REGISTRY.md | Example row. Registry update required if accepted. |

## DOING

| ID | Priority | Type | Title | Route | Source | Owner | Created | Updated | Architecture impact | Validation required | Review required | Linked docs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VCP-003 | P2 | docs | Example: sync architecture docs after accepted change | Backlog | review | maintainer | 2026-06-02 | 2026-06-02 | cross-layer | update docs and rerun checks | yes | PROJECT_MAP.md, ARCHITECTURE_SOURCE_OF_TRUTH.md | Example row. Architecture memory must stay current. |

## DONE

| ID | Priority | Type | Title | Route | Source | Owner | Created | Updated | Architecture impact | Validation required | Review required | Linked docs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VCP-004 | P2 | bug | Example: validated fix completed | Post-Task Review | prod-error | maintainer | 2026-06-02 | 2026-06-02 | component-level | checks green | review gate recorded | templates/reports/code-review-report.md | Example row. Keep evidence before DONE. |

## ARCHIVED / NOT TAKEN

| ID | Priority | Type | Title | Route | Source | Owner | Created | Updated | Architecture impact | Validation required | Review required | Linked docs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VCP-005 | P3 | idea | Example: not taking this request right now | Backlog | ai | maintainer | 2026-06-02 | 2026-06-02 | none | - | - | - | Example row. Deferred after triage. |
