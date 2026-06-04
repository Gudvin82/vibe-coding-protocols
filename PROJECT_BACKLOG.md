<!-- vcp-artifact: PROJECT_BACKLOG -->
<!-- vcp-version: v0.6.7 -->
<!-- methodology-version: v1.4 -->

# Project Backlog

## Rules

- Use this backlog for tasks, ideas, bugs, operations follow-up, review follow-up, and product work.
- Do not use it as a replacement for `AUDIT_BACKLOG.md`.
- Keep IDs stable. Do not renumber existing items.
- Create or update a backlog item before implementation starts when a new request arrives.
- If architecture impact is `cross-layer` or `production-critical`, update architecture docs in the same task or create a linked follow-up item.
- Example rows below illustrate the format. Replace them with real project state.

## TODO

| ID | Priority | Type | Title | Route | Source | Owner | Created | Updated | Architecture impact | Validation required | Review required | Linked docs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VCP-001 | P1 | operations | Example: extend production error capture workflow | Operations | roadmap | maintainer | 2026-06-02 | 2026-06-02 | docs-only | doctor + backlog validate | no | docs/production-observability.md | Example row. Keep runtime inbox guidance current. |
| VCP-002 | P2 | api-integration | Example: review new external dependency before coding | Third-party API Intake | ai | maintainer | 2026-06-02 | 2026-06-02 | none | intake report required | yes | templates/THIRD_PARTY_REGISTRY.md | Example row. Registry update required if accepted. |

## DOING

| ID | Priority | Type | Title | Route | Source | Owner | Created | Updated | Architecture impact | Validation required | Review required | Linked docs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VCP-003 | P2 | docs | Example: sync architecture docs after accepted route change | Backlog | review | maintainer | 2026-06-02 | 2026-06-02 | cross-layer | update docs and re-run checks | yes | PROJECT_MAP.md, templates/ARCHITECTURE_SOURCE_OF_TRUTH.md | Example row. Update architecture memory in the same task. |

## DONE

| ID | Priority | Type | Title | Route | Source | Owner | Created | Updated | Architecture impact | Validation required | Review required | Linked docs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VCP-004 | P2 | review-finding | Example: backlog item closed after validated follow-up | Post-Task Review | user | maintainer | 2026-06-02 | 2026-06-02 | component-level | checks green: `vcp check --fast --json` | review passed: `code-review-report` updated | templates/reports/code-review-report.md | Example row. Validation and review evidence are recorded before DONE. |

## ARCHIVED / NOT TAKEN

| ID | Priority | Type | Title | Route | Source | Owner | Created | Updated | Architecture impact | Validation required | Review required | Linked docs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VCP-005 | P3 | idea | Example: low-value suggestion not taken | Backlog | ai | maintainer | 2026-06-02 | 2026-06-02 | none | - | - | - | Example row. Archived because it does not justify scope right now. |
