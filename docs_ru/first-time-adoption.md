# First-Time Adoption

<!-- vcp-version: v0.9.1 -->
<!-- methodology-version: v1.4 -->

## VCP за 60 секунд

VCP — локальный слой контроля для AI-built проектов.

Используйте VCP, когда:
- AI собрал MVP, и его нужно безопасно довести;
- требования размыты;
- начался architecture drift;
- нужны PR Gate, audit backlog, release readiness и proof;
- нужно, чтобы AI-агенты работали по контролируемому процессу.

Старт:
1. Прочитайте `START_HERE.md`
2. Запустите `python3 -m vcp_cli trust-check --json`
3. Выберите путь: new / existing / MVP-to-Launch / launch / deep hardening
4. Откройте Control Catalog
5. Запустите flagship demo
6. Если вы внедряете VCP в Claude Code, Codex, Cursor, GitHub Copilot или GitHub Actions, используйте copy-ready agent kits, а не случайное копирование root-файлов.

## Не начинайте с полного чтения

Не начинайте с чтения всего репозитория. Сначала используйте route selector, control catalog и token-budgeted evaluator path.

Рекомендуемые next steps:
- `docs_ru/integration-setup.md`
- `docs_ru/agent-kits.md`
