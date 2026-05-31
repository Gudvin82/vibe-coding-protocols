# Python CLI Surface

VCP now includes a real local Python CLI surface.

Files:
- `pyproject.toml`
- `vcp_cli/`
- `bin/vcp`

## Purpose

This is the local product layer for VCP.
It keeps script-first workflows intact while adding:
- route selection;
- adoption dry-run;
- review helper output;
- score output;
- manifest validation;
- benchmark validation.

Examples:

```bash
python3 -m vcp_cli version
python3 -m vcp_cli doctor
python3 -m vcp_cli route --profile production
python3 -m vcp_cli adopt --pack shared-engine --dry-run
python3 -m vcp_cli review plan
python3 -m vcp_cli score --json
python3 -m vcp_cli manifest validate
python3 -m vcp_cli benchmark run
```

## Scope

- local and repo-first;
- no external AI API calls;
- no destructive apply mode by default;
- not published to PyPI yet;
- no promise of Windows-native parity yet.

The CLI is real in `v0.5.0`,
but it is still intentionally conservative.
