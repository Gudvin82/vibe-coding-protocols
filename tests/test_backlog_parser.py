from vcp_cli.backlog import parse_backlog_text, render_backlog, validate_document


def sample_text() -> str:
    return """<!-- vcp-artifact: PROJECT_BACKLOG -->
<!-- vcp-version: v0.5.4 -->
<!-- methodology-version: v1.4 -->

# Project Backlog

## Rules

- Example.

## TODO

| ID | Priority | Type | Title | Route | Source | Owner | Created | Updated | Architecture impact | Validation required | Review required | Linked docs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VCP-001 | P2 | idea | Example todo | Backlog | user | maintainer | 2026-06-02 | 2026-06-02 | none | - | - | - | note |

## DOING

| ID | Priority | Type | Title | Route | Source | Owner | Created | Updated | Architecture impact | Validation required | Review required | Linked docs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VCP-002 | P1 | prod-error | Example doing | Operations | prod-error | maintainer | 2026-06-02 | 2026-06-02 | docs-only | backlog validate | yes | docs/production-observability.md | note |

## DONE

| ID | Priority | Type | Title | Route | Source | Owner | Created | Updated | Architecture impact | Validation required | Review required | Linked docs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VCP-003 | P2 | review-finding | Example done | Post-Task Review | review | maintainer | 2026-06-02 | 2026-06-02 | component-level | checks green | review passed | templates/reports/code-review-report.md | note |

## ARCHIVED / NOT TAKEN

| ID | Priority | Type | Title | Route | Source | Owner | Created | Updated | Architecture impact | Validation required | Review required | Linked docs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VCP-004 | P3 | idea | Example archived | Backlog | ai | maintainer | 2026-06-02 | 2026-06-02 | none | - | - | - | not taking |
"""


def test_parse_and_render_roundtrip():
    doc = parse_backlog_text(sample_text())
    assert len(doc.items) == 4
    assert validate_document(doc) == []
    rendered = render_backlog(doc)
    assert "VCP-003" in rendered
    assert "## ARCHIVED / NOT TAKEN" in rendered
