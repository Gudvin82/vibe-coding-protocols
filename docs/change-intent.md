# Change Intent

Repository package: `v0.9.5`

Change Intent is VCP's local control layer for planned change.

Before an AI agent edits code, the project can capture:
- what is changing;
- why it is changing;
- expected user or business outcome;
- affected surfaces;
- risk level;
- required checks;
- recommended VCP path;
- human approval requirement;
- rollback note.

This is governance and control, not automatic code mutation.

## Files

- `schemas/change-intent.schema.json`
- `.vcp/change-intent.example.json`
- `templates/reports/change-intent.md`

## CLI

- `python3 -m vcp_cli change intent --json`
- `python3 -m vcp_cli change intent validate .vcp/change-intent.example.json --json`
