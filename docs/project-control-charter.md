# Project Control Charter

Repository package: `v0.9.0`

Project Control Charter is VCP's local governance document for a repo that wants explicit control over AI work.

## Sections

1. Project identity
2. Source of truth
3. Agent permissions
4. Human approval required
5. Required checks
6. Release gates
7. Docs and proof rules
8. Risk levels
9. Rollback expectations
10. Roadmap boundaries

## Files

- `templates/project-control-charter.md`
- `schemas/project-control-charter.schema.json`
- `.vcp/project-control-charter.example.json`

## CLI

- `python3 -m vcp_cli charter validate .vcp/project-control-charter.example.json --json`
