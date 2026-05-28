# Vibe Coding Protocols

[English version](./README.md)

[![Версия repo](https://img.shields.io/badge/repo-v0.3.0-blue)](./CHANGELOG.md)
[![Методология](https://img.shields.io/badge/methodology-v1.4-purple)](https://anmalishev.ru/expert/vibe-coding/)
[![Лицензия](https://img.shields.io/github/license/Gudvin82/vibe-coding-protocols)](./LICENSE)
[![Vibe Check](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml/badge.svg)](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml)
[![Latest Release](https://img.shields.io/github/v/release/Gudvin82/vibe-coding-protocols)](https://github.com/Gudvin82/vibe-coding-protocols/releases)

**Это не коллекция промптов.**

VCP — это operating layer для AI-assisted разработки:
маршруты, Memory Bank артефакты, stop conditions, checks, hardening, incident recovery и release gates.

Пакет репозитория: `v0.3.0`

Веб-методология: `Vibe Coding Protocols v1.4`

## Отдай этот repo своей AI IDE

Вставь это в Claude Code, Codex, Cursor, Windsurf или Copilot:

```text
Study this repository as a workflow toolkit.

Do not write code yet.

First choose my route:
Lite, Starter, Hardening or Extended.

Then return:
1. files to copy first;
2. files not to copy;
3. first validation command;
4. underestimated risks;
5. next smallest safe step.
```

## Когда это использовать

- когда у тебя уже есть AI-generated code и нужно понять, что небезопасно до показа клиенту;
- когда ты стартуешь новый vibe-coded проект и хочешь минимальные rails для архитектуры, безопасности и релиза;
- когда ты solo builder и хочешь легкий процесс, а не корпоративную бюрократию;
- когда ты small team / CTO и задаешь правила, как AI может безопасно менять код.

## Быстрый старт

1. Открой [START_HERE.md](./START_HERE.md).
2. Выбери маршрут: Lite, Starter, Hardening или Extended.
3. Для нового проекта скопируй `templates/AGENTS.md` как `AGENTS.md` и `templates/PROJECT_MAP.md`.
4. Если поверхностей несколько, добавь `ARCHITECTURE_MAP.md` до генерации кода.
5. Запусти `bash scripts/vibe-check.sh --starter` или `--audit`.

## Рекомендуемая установка: review-first

```bash
curl -fsSL https://raw.githubusercontent.com/Gudvin82/vibe-coding-protocols/main/scripts/init-minimal.sh -o init-minimal.sh
curl -fsSL https://raw.githubusercontent.com/Gudvin82/vibe-coding-protocols/main/SHA256SUMS -o SHA256SUMS
less init-minimal.sh
bash init-minimal.sh --starter
```

`curl | bash` не показывается как основной путь.
Для real projects используй review-first setup.
Дополнительные варианты установки и checksum notes:
[docs/advanced-install.md](./docs/advanced-install.md).

## Что важно помнить

- root `AGENTS.md` настраивает этот репозиторий;
- в свой проект копируй `templates/AGENTS.md` как `AGENTS.md`;
- `vibe-check` — это readiness signal, а не security certification;
- `--doctor`, `--init-report` и `--update-advice` помогают с онбордингом и обновлением артефактов;
- GitHub остается canonical source;
- wrappers и VS Code extension в `v0.3.0` пока только experimental skeletons.

## Полезные ссылки

- [docs/lite-adoption-path.md](./docs/lite-adoption-path.md)
- [docs/architecture-map.md](./docs/architecture-map.md)
- [docs/hardening-thresholds.md](./docs/hardening-thresholds.md)
- [docs/update-copied-artifacts.md](./docs/update-copied-artifacts.md)
- [docs/prompt-drift-control.md](./docs/prompt-drift-control.md)
- [docs/windows.md](./docs/windows.md)
- [docs/community.md](./docs/community.md)
- [docs/mirrors.md](./docs/mirrors.md)
- GitVerse mirror: <https://gitverse.ru/GudWin82/vibe-coding-protocols>
- [docs/comparison.md](./docs/comparison.md)
- [docs/release-v0.3.0.md](./docs/release-v0.3.0.md)
