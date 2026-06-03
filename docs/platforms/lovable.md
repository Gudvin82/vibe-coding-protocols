# Lovable

## Status

prompt-compatible

This is a repository workflow path, not an official vendor plugin.

## Recommended VCP entrypoints

- `AGENTS.md`
- `AI_INTAKE.md`
- `docs/public-site-readiness.md`

## What to paste into the agent

Start with `AGENTS.md`, then `AI_INTAKE.md`, then `.vcp/index.json` if context is limited.
Ask the tool to choose the smallest safe workflow instead of copying the whole repository.

## Compatible files

- `AGENTS.md`

## Validation commands

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli route --profile production
python3 -m vcp_cli check --fast --json
```

## Limitations

- Not an official plugin or marketplace integration.
- Do not assume the tool understands VCP unless you point it at `AGENTS.md`, `AI_INTAKE.md`, or `.vcp/index.json`.
- Avoid copying every template blindly.

## Notes

Expect to paste or attach the key repo entrypoints manually because prompt-only tools may not persist VCP context between runs.
