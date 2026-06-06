# Trust Check

Repository package: `v0.8.6`

Используй trust check, когда нужен локальный read-only audit на согласованность репозитория.

## Команда

```bash
python3 -m vcp_cli trust-check --json
```

Installed CLI form:

```bash
vcp trust-check --json
```

## Что он проверяет

- согласованность version surfaces;
- parity между README и README_ru;
- parity русской документации;
- противоречия roadmap-only overclaim;
- sync между workflow и docs;
- корректность integration statuses;
- наличие benchmark report;
- hygiene CHANGELOG;
- наличие release notes.

## Чего он не доказывает

Trust Check не доказывает:
- production safety;
- launch success;
- security certification;
- hosted platform readiness.

Это repository trust and consistency check.
