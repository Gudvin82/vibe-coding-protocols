# Google Jules

## Status

experimental

This is a repository workflow path, not an official vendor plugin.

## Recommended VCP entrypoints

- `AGENTS.md`
- `.vcp/index.json`
- `docs/platforms/README.md`

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

Treat this as a best-effort repository workflow and verify outputs manually before trusting it for risky changes.
