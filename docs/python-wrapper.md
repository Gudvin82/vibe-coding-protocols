# Python Wrapper Skeleton

VCP also includes an experimental Python entrypoint skeleton.

Files:
- `pyproject.toml`
- `vcp_cli/__main__.py`

## Purpose

This is preparation for a future Python-friendly entrypoint.
It currently delegates to `scripts/vibe-check.sh`.

Examples:

```bash
python -m vcp_cli doctor
python -m vcp_cli init-report
python -m vcp_cli starter
python -m vcp_cli route production
python -m vcp_cli score --json
python -m vcp_cli manifest validate
```

## Scope

`route`, `adopt`, `score` and `manifest validate` are lightweight convenience commands. They do not spawn or run external AI reviewers.


- experimental;
- not published to PyPI;
- no promise of Windows-native parity yet;
- intended as a lightweight wrapper, not a second implementation.
