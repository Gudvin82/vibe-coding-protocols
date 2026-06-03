# JetBrains / Junie

## Status

Supported via docs, prompts, rules, and repository workflow surfaces.
No official plugin or vendor endorsement is claimed unless separately implemented later.

## Recommended entrypoint

- templates/AGENTS.md, AI_EVALUATION_GUIDE.md, docs/platforms/README.md

## What to ask the tool

Ask Junie to follow the docs/prompts workflow and validation discipline.

## What not to ask

Do not ask it to claim official plugin or ecosystem support that is not implemented.

## Avoid copying everything blindly

Use route selection and Adoption Packs first. Prefer `--dry-run` and manual merge decisions over bulk copy.

## Validation commands

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli route --profile production
python3 -m vcp_cli adopt --pack production --dry-run
python3 -m vcp_cli manifest validate
```
