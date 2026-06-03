# Claude Code

## Status

Supported via docs, prompts, rules, and repository workflow surfaces.
No official plugin or vendor endorsement is claimed unless separately implemented later.

## Recommended entrypoint

- AGENTS.md, AI_INTAKE.md, templates/AGENTS.md

## What to ask the tool

Ask Claude Code to classify the repo, choose the route, inspect only relevant files, and report validation before final output.

## What not to ask

Do not ask it to copy the whole toolkit blindly or claim vendor-native integration.

## Avoid copying everything blindly

Use route selection and Adoption Packs first. Prefer `--dry-run` and manual merge decisions over bulk copy.

## Validation commands

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli route --profile production
python3 -m vcp_cli adopt --pack production --dry-run
python3 -m vcp_cli manifest validate
```
