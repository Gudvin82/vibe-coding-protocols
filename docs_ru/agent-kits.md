# Agent Kits

VCP включает copy-ready setup kits для:
- Claude Code
- Codex
- Cursor
- GitHub Copilot
- GitHub Actions

Это не official plugins.
Это local-first setup kits, templates и безопасный CLI export path.

## Что входит в agent kit

Каждый kit intentionally lightweight:
- короткий README с путями копирования;
- подходящие instruction files;
- optional control files: `PROJECT_CONTROL_CHARTER.md`, `CHANGE_INTENT.md`, `PR_GATE.md`, `LAUNCH_DECISION.md`.

VCP не auto-install эти файлы в целевой репозиторий по умолчанию.

## CLI

```bash
python3 -m vcp_cli agents kit --target claude --json
python3 -m vcp_cli agents kit --target codex --json
python3 -m vcp_cli agents kit --target cursor --json
python3 -m vcp_cli agents kit --target copilot --json
python3 -m vcp_cli agents kit --target github-actions --json
```

Опциональный экспорт в отдельную директорию:

```bash
python3 -m vcp_cli agents kit --target copilot --output ./vcp-copilot-kit --confirm --json
```

Правила безопасности:
- без `--output` записи нет;
- write mode требует `--output`;
- write mode требует `--confirm`;
- overwrite только с `--force`;
- `--dry-run` ничего не пишет.

## Boundary

Это не означает:
- official plugin suite;
- IDE extension;
- native vendor integration;
- marketplace install;
- cloud sync;
- telemetry;
- automatic orchestration.
