# Aider

## Status

cli-compatible

This is a repository workflow path, not an official vendor plugin.

## Recommended VCP entrypoints

- `AI_EVALUATION_GUIDE.md`
- `vcp_cli`
- `.vcp/index.json`

## What to paste into the agent

Start with `AGENTS.md`, then `AI_INTAKE.md`, then `.vcp/index.json` if context is limited.
Ask the tool to choose the smallest safe workflow instead of copying the whole repository.

## Compatible files

- `AI_EVALUATION_GUIDE.md`

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

This works best when shell access is available so the tool can run local VCP commands instead of relying on pasted guidance only.
