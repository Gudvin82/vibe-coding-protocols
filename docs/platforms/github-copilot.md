# GitHub Copilot

## Status

Supported via docs, prompts, rules, and repository workflow surfaces.
No official plugin or vendor endorsement is claimed unless separately implemented later.

## Recommended entrypoint

- .github/copilot-instructions.md, templates/AGENTS.md, AI_INTAKE.md

## What to ask the tool

Ask Copilot to use repository instructions plus route classification and validation commands.

## What not to ask

Do not ask it to treat instructions as a full replacement for manifests or review gates.

## Avoid copying everything blindly

Use route selection and Adoption Packs first. Prefer `--dry-run` and manual merge decisions over bulk copy.

## Validation commands

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli route --profile production
python3 -m vcp_cli adopt --pack production --dry-run
python3 -m vcp_cli manifest validate
```
