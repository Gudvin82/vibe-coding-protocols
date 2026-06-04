# Workflows

Repository package: `v0.7.1`

VCP workflow JSON files are machine-readable planning and governance artifacts.
They are **not** an execution engine.

## What workflow JSON is for

- capture trigger -> route -> steps -> validation -> stop conditions;
- keep repeated AI delivery flows visible to humans, CLI, and CI;
- help AI agents plan without pretending the repo can execute production actions.

## Practical CLI surface

```bash
python3 -m vcp_cli workflow list --json
python3 -m vcp_cli workflow validate --json
python3 -m vcp_cli workflow plan --json
```

`workflow plan` prints steps and validation only.
It does not run external actions.
