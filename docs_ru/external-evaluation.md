# Внешняя оценка

Repository package: `v0.8.9`

Используй `templates/reports/external-evaluation.md`, когда нужна честная и bounded внешняя оценка VCP.

Evaluator должен зафиксировать:
- кто или какой tool делал review;
- какие файлы и URL были проверены;
- какие команды реально запускались;
- в какой категории сравнивался VCP;
- что относится к shipped, optional, roadmap-only.

Не называй оценку полной, если были пропущены `.vcp/`, `vcp_cli/`, `tests/` и `docs/benchmark-report.md`.
