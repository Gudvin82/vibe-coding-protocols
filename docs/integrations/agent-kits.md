# Agent Kits

VCP ships copy-ready setup kits for:
- Claude Code
- Codex
- Cursor
- GitHub Copilot
- GitHub Actions

These are not official plugins.
They are local-first setup kits, templates, and safe CLI export paths.

## What an agent kit contains

Each kit is intentionally lightweight:
- a short README with copy destinations;
- the smallest matching instruction file(s);
- optional control files such as `PROJECT_CONTROL_CHARTER.md`, `CHANGE_INTENT.md`, `PR_GATE.md`, and `LAUNCH_DECISION.md`.

VCP does not auto-install these into a target repo by default.

## Shipped targets

- `claude`
- `codex`
- `cursor`
- `copilot`
- `github-actions`

## CLI

Read-only discovery:

```bash
python3 -m vcp_cli agents kit --target claude --json
python3 -m vcp_cli agents kit --target codex --json
python3 -m vcp_cli agents kit --target cursor --json
python3 -m vcp_cli agents kit --target copilot --json
python3 -m vcp_cli agents kit --target github-actions --json
```

Optional export to a separate directory:

```bash
python3 -m vcp_cli agents kit --target copilot --output ./vcp-copilot-kit --confirm --json
```

Safety rules:
- `--json` without `--output` does not write files;
- write mode requires `--output`;
- write mode requires `--confirm`;
- existing files are not overwritten unless `--force` is passed;
- `--dry-run` reports planned writes without creating files.

## Exact adoption paths

Claude Code:
- `templates/agent-kits/claude/AGENTS.md` -> `AGENTS.md`
- `templates/agent-kits/claude/CLAUDE.md` -> `CLAUDE.md`
- `templates/agent-kits/claude/PROJECT_CONTROL_CHARTER.md` -> `PROJECT_CONTROL_CHARTER.md`
- `templates/agent-kits/claude/CHANGE_INTENT.md` -> `CHANGE_INTENT.md`
- `templates/agent-kits/claude/PR_GATE.md` -> `PR_GATE.md`

Codex:
- `templates/agent-kits/codex/AGENTS.md` -> `AGENTS.md`
- `templates/agent-kits/codex/CODEX.md` -> `CODEX.md`
- `templates/agent-kits/codex/PROJECT_CONTROL_CHARTER.md` -> `PROJECT_CONTROL_CHARTER.md`
- `templates/agent-kits/codex/CHANGE_INTENT.md` -> `CHANGE_INTENT.md`
- `templates/agent-kits/codex/PR_GATE.md` -> `PR_GATE.md`

Cursor:
- `templates/agent-kits/cursor/AGENTS.md` -> `AGENTS.md`
- `templates/agent-kits/cursor/CURSOR_RULES.md` -> `CURSOR_RULES.md`
- `templates/agent-kits/cursor/cursorrules.example` -> `.cursorrules`
- `templates/agent-kits/cursor/PROJECT_CONTROL_CHARTER.md` -> `PROJECT_CONTROL_CHARTER.md`
- `templates/agent-kits/cursor/CHANGE_INTENT.md` -> `CHANGE_INTENT.md`
- `templates/agent-kits/cursor/PR_GATE.md` -> `PR_GATE.md`

GitHub Copilot:
- `templates/agent-kits/copilot/AGENTS.md` -> `AGENTS.md`
- `templates/agent-kits/copilot/copilot-instructions.md` -> `.github/copilot-instructions.md`
- `templates/agent-kits/copilot/PROJECT_CONTROL_CHARTER.md` -> `PROJECT_CONTROL_CHARTER.md`
- `templates/agent-kits/copilot/CHANGE_INTENT.md` -> `CHANGE_INTENT.md`
- `templates/agent-kits/copilot/PR_GATE.md` -> `PR_GATE.md`
- `templates/agent-kits/copilot/github-workflow-vcp-pr-gate.yml` -> `.github/workflows/vcp-pr-gate.yml`

GitHub Actions:
- `templates/agent-kits/github-actions/vcp-pr-gate.yml` -> `.github/workflows/vcp-pr-gate.yml`
- `templates/agent-kits/github-actions/PR_GATE.md` -> `PR_GATE.md`
- `templates/agent-kits/github-actions/LAUNCH_DECISION.md` -> `LAUNCH_DECISION.md`

## Boundary

These kits do not mean:
- official plugin suite;
- IDE extension;
- native vendor integration;
- marketplace install;
- telemetry;
- cloud sync;
- automatic orchestration.
