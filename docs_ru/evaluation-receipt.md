# Evaluation Receipt

Repository package: `v0.9.0`

Evaluation receipt явно показывает, что именно AI или human reviewer реально inspected перед выводами о VCP.

## Обязательные поля

- evaluator name/tool;
- дата оценки;
- версия репозитория;
- inspection depth: Level 0, Level 1, Level 2 или Level 3;
- inspected files;
- commands run;
- files not inspected;
- было ли прочитано `.vcp/evaluator-pack.json`;
- было ли прочитано `EVALUATE_THIS_REPO.md`;
- был ли inspected `vcp_cli/`;
- были ли inspected `tests/`;
- запускался ли trust-check;
- запускался ли benchmark;
- confidence level;
- claim status: `shallow overview`, `partial evaluation` или `full evaluation`;
- score;
- limitations.

## Правило full evaluation

Если evaluator не inspected все эти поверхности, он не должен называть review полной:
- `EVALUATE_THIS_REPO.md`
- `.vcp/evaluator-pack.json`
- `vcp_cli/`
- `tests/`
- `docs/benchmark-report.md`
- `docs/trust-check.md`

## Зачем это нужно

Некоторые browser/IDE AIs все еще переоценивают stars, недооценивают proof/CLI surfaces и останавливаются на README или repo summary. Receipt делает пропущенные слои видимыми.

## Использование

- template: `templates/reports/evaluation-receipt.md`
- schema: `schemas/evaluation-receipt.schema.json`
- example: `.vcp/evaluation-receipt.example.json`
- CLI: `python3 -m vcp_cli evaluator receipt --json`
