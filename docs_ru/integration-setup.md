# Как внедрять VCP в Claude Code, Codex, Cursor, GitHub Copilot и GitHub

Используйте эту страницу, если хотите внедрить VCP в другой репозиторий через:

- Claude Code;
- Codex;
- Cursor;
- GitHub Copilot;
- GitHub Actions.

Это repository integration workflow, а не official plugin suite.

## Общий принцип

Для каждого инструмента:

1. копируйте только подходящий instruction file;
2. держите route selection явным;
3. запускайте локальную validation после установки;
4. не копируйте весь VCP вслепую.

## Claude Code

Рекомендуемые файлы:

- `templates/AGENTS.md` -> `AGENTS.md`
- `templates/AGENTS.claude.md` -> `CLAUDE.md`

Экспорт:

```bash
python3 -m vcp_cli agents template --agent claude --output ./CLAUDE.md --confirm
```

## Codex

Рекомендуемые файлы:

- `templates/AGENTS.md` -> `AGENTS.md`
- `templates/agents/CODEX.md` -> `CODEX.md`

Экспорт:

```bash
python3 -m vcp_cli agents template --agent codex --output ./CODEX.md --confirm
```

## Cursor

Рекомендуемые файлы:

- `templates/AGENTS.md` -> `AGENTS.md`
- `templates/AGENTS.cursor.md` -> `CURSOR_RULES.md`
- при необходимости адаптируйте `CURSOR_RULES.md` в `.cursorrules` или editor-native rules surface

Экспорт:

```bash
python3 -m vcp_cli agents template --agent cursor --output ./CURSOR_RULES.md --confirm
```

## GitHub Copilot

Рекомендуемые файлы:

- `templates/AGENTS.md` -> `AGENTS.md`
- `templates/agents/COPILOT_INSTRUCTIONS.md` -> `.github/copilot-instructions.md`

Экспорт:

```bash
mkdir -p .github
python3 -m vcp_cli agents template --agent copilot --output ./.github/copilot-instructions.md --confirm
```

## GitHub Actions

Рекомендуемый файл:

- `ci-examples/github-actions/vcp-pr-gate.yml` -> `.github/workflows/vcp-pr-gate.yml`

Это repository-side PR Gate example, а не GitHub Marketplace action.

## Минимальная проверка после установки

```bash
python3 -m vcp_cli doctor --json
python3 -m vcp_cli route --profile production --json
python3 -m vcp_cli check --fast --json
```

Если целевой репозиторий не production-heavy, используйте ближайший реальный profile.

## Что это не означает

- это не official plugin;
- это не automatic model switching;
- это не automatic PR creation;
- это не automatic merge/deploy approval;
- это не native slash-command support, если сам инструмент этого не умеет.
