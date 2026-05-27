# Vibe Coding Protocols — русская версия

[English version](./README.md)

**Не просто коллекция prompt-ов.**

Vibe Coding Protocols — это легкий operating layer для AI-assisted разработки:
маршруты, Memory Bank files, stop conditions, checks, hardening, incident recovery и release gates.

Пакет репозитория: `v0.2.0`  
Веб-методология: `Vibe Coding Protocols v1.4`

Если вы читаете с мобильного:
1. [START_HERE.md](./START_HERE.md)
2. [docs/lite-adoption-path.md](./docs/lite-adoption-path.md)
3. [prompts/use-this-repo-prompt_ru.md](./prompts/use-this-repo-prompt_ru.md)

## С чего начать

| Ситуация | Куда идти |
|---|---|
| Только идея | [English Product Brief](./prompts/product-brief-prompt_en.md) или [Russian Product Brief](./prompts/product-brief-prompt.md) |
| Новый AI-assisted проект | [Starter Protocol](./protocols/ai-project-starter-protocol.md) |
| Уже есть AI-generated код | [Hardening Protocol](./protocols/ai-project-hardening-protocol.md) |
| Публичный / client-facing / production | [Extended Protocol](./protocols/ai-project-extended-protocol.md) |
| Нужны AI IDE rules | [START_HERE.md](./START_HERE.md) |

## Какой agent file использовать?

- Root `AGENTS.md` настраивает этот репозиторий.
- Root `CLAUDE.md` настраивает Claude Code для этого репозитория.
- Не копируйте root `AGENTS.md` blindly в свой проект.
- Для своего проекта копируйте `templates/AGENTS.md` как `AGENTS.md`.
- Для Claude Code используйте `templates/AGENTS.claude.md` или адаптируйте его в свой `CLAUDE.md`.
- Для Cursor / Windsurf используйте `templates/AGENTS.cursor.md` и `templates/AGENTS.windsurf.md`.

## Если копировать только один набор

### Solo / MVP

1. Скопируйте `templates/AGENTS.md` как `AGENTS.md`.
2. Скопируйте `templates/PROJECT_MAP.md`.
3. Используйте `prompts/product-brief-prompt_en.md` или RU-версию.
4. Запустите `bash scripts/vibe-check.sh --starter`.

<details>
<summary>Дальше для команды и production</summary>

### Small team

Добавьте:
- `templates/AUDIT_BACKLOG.md`
- `templates/ARCHITECTURE_SOURCE_OF_TRUTH.md`
- CI с `bash scripts/vibe-check.sh --audit`

### Production / client-facing

Добавьте:
- `templates/SECURITY_BASELINE.md`
- `templates/SECURITY_OPERATIONS_BASELINE.md`
- `templates/THIRD_PARTY_REGISTRY.md`
- `templates/INCIDENT_RECOVERY_RUNBOOK.md`
- `templates/METRICS_BOARD.md`

</details>

## Review-first install

```bash
curl -fsSL https://raw.githubusercontent.com/Gudvin82/vibe-coding-protocols/main/scripts/init-minimal.sh -o init-minimal.sh
curl -fsSL https://raw.githubusercontent.com/Gudvin82/vibe-coding-protocols/main/SHA256SUMS -o SHA256SUMS

grep "scripts/init-minimal.sh" SHA256SUMS > init-minimal.sha256
sha256sum -c init-minimal.sha256

less init-minimal.sh
bash init-minimal.sh --starter
```

Для macOS:

```bash
shasum -a 256 init-minimal.sh
```

Pipe-to-bash оставляйте только для пустых или тестовых репозиториев.

## Self-dogfooding

Этот репозиторий гоняет VCP-проверки на самом себе.
См. [docs/self-dogfooding.md](./docs/self-dogfooding.md).

## `vibe-check`

`vibe-check` — это readiness signal, а не security certification.

Основные команды:

```bash
bash scripts/vibe-check.sh --help
bash scripts/vibe-check.sh --starter
bash scripts/vibe-check.sh --hardening
bash scripts/vibe-check.sh --audit
bash scripts/vibe-check.sh --audit --json
bash scripts/vibe-check.sh --doctor
bash scripts/vibe-check.sh --init-report
```

Строгий gate:

```bash
bash scripts/vibe-check.sh --audit
bash scripts/vibe-check.sh --audit --strict
```

Локальная диагностика optional scanners:

```bash
bash scripts/vibe-check.sh --audit --scanners
```

`|| true` не используйте в CI или release gates.

## Примеры и ограничения

- [examples/README.md](./examples/README.md)
- [examples/legacy-ai-mess-vibe](./examples/legacy-ai-mess-vibe/)
- [docs/known-limitations.md](./docs/known-limitations.md)
- [docs/release-readiness.md](./docs/release-readiness.md)
- [docs/adoption-feedback.md](./docs/adoption-feedback.md)

## Полезные ссылки

- [START_HERE.md](./START_HERE.md)
- [docs/lite-adoption-path.md](./docs/lite-adoption-path.md)
- [docs/README.md](./docs/README.md)
- [protocols/README.md](./protocols/README.md)
- [checklists/README.md](./checklists/README.md)
- [templates/README.md](./templates/README.md)
- [templates/AUDIT_BACKLOG_ru.md](./templates/AUDIT_BACKLOG_ru.md)
- [docs/versioning.md](./docs/versioning.md)
- [docs/ide-rules-dry-policy.md](./docs/ide-rules-dry-policy.md)
- [docs/artifact-versioning.md](./docs/artifact-versioning.md)
- [docs/faq.md](./docs/faq.md)
- [docs/troubleshooting.md](./docs/troubleshooting.md)
- [docs/comparison.md](./docs/comparison.md)
