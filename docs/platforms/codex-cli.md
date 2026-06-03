# Codex CLI

## Status

Supported via docs, prompts, rules, and repository workflow surfaces.
No official plugin or vendor endorsement is claimed unless separately implemented later.

## Recommended entrypoint

- AI_EVALUATION_GUIDE.md, AGENTS.md, vcp_cli

## What to ask the tool

Ask Codex to use `vcp_cli` commands, `.vcp/index.json`, and cards first when context is limited.

## What not to ask

Do not ask it to treat README-only skim as a complete evaluation.

## Avoid copying everything blindly

Use route selection and Adoption Packs first. Prefer `--dry-run` and manual merge decisions over bulk copy.

## Validation commands

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli route --profile production
python3 -m vcp_cli adopt --pack production --dry-run
python3 -m vcp_cli manifest validate
```
