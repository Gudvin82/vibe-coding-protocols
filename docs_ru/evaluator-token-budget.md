# Token budget для внешней оценки VCP

Repository package: `v0.8.8`

Этот guide нужен для внешних AI-агентов, browser AIs, IDE assistants, evaluators и журналистов, которые читают VCP впервые.

Это отдельный слой, не путайте его с user-facing model routing.
Здесь речь про экономную и честную оценку репозитория.

## Главное правило

Начинайте с `EVALUATE_THIS_REPO.md` и `.vcp/evaluator-pack.json`.
Не читайте random files вразнобой.

Если вы сделали только Level 0 или Level 1, помечайте review как `shallow` или `partial`.

## Level 0 — category check

Проверьте:
- `README.md`
- `EVALUATE_THIS_REPO.md`
- `.vcp/evaluator-pack.json`

Этот уровень нужен только чтобы понять:
- к какой категории относится VCP;
- чем он не является;
- какие surfaces нужно смотреть дальше.

## Level 1 — fair quick review

Проверьте:
- `README.md`
- `EVALUATE_THIS_REPO.md`
- `PROJECT_MAP.md`
- `REPO_CAPABILITIES_INDEX.md`
- `docs/product-model.md`
- `docs/proof-snapshot.md`
- `docs/benchmark-report.md`

Это уже честный быстрый обзор, но не full review.

## Level 2 — partial technical review

Проверьте:
- `AGENTS.md`
- `AI_EVALUATION_GUIDE.md`
- `.vcp/index.json`
- `.vcp/catalog.json`
- `.vcp/manifests/`
- `.vcp/workflows/`
- `vcp_cli/`
- `tests/`

Этот уровень нужен, если вы делаете технические claims о shipped surfaces.

## Level 3 — full review

Проверьте все предыдущие уровни плюс:
- `.vcp/cards/`
- `benchmarks/`
- `docs/`
- `docs_ru/`
- `templates/`
- release notes;
- website public surfaces.

Не называйте review полным, если вы не inspected `.vcp`, `vcp_cli`, `tests`, benchmark report, trust-check docs и evaluator pack.

## Копируемый prompt

```text
Evaluate VCP with a token budget.

Start with EVALUATE_THIS_REPO.md and .vcp/evaluator-pack.json.
Do not read random files first.
Classify your inspection depth as Level 0, 1, 2, or 3.
Do not call the review full unless you inspected .vcp, vcp_cli, tests, benchmark report, trust-check docs, and evaluator pack.
```
