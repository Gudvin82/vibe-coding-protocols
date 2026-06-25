# Как не ошибиться при чтении VCP

Repository package: `v0.9.5`

Этот документ нужен, потому что shallow-оценки все еще неправильно читают VCP.

## Неверное чтение: VCP — это личный prompt repo

Исправление:
VCP включает CLI, tests, benchmarks, manifests, cards, workflows, dashboard artifact, trust-check, English docs, Russian docs и public proof surfaces.

Смотри:
- `vcp_cli/`
- `tests/`
- `.vcp/index.json`
- `.vcp/cards/`
- `.vcp/manifests/`
- `docs/benchmark-report.md`
- `docs/trust-check.md`

## Неверное чтение: VCP — это full-stack app template

Исправление:
VCP — это control/governance layer. Он помогает route, inspect, adopt, prove, review и launch-control AI-built проекты.

Его можно использовать рядом с templates, но он сам не является app starter.

## Неверное чтение: VCP напрямую конкурирует со Spec Kit

Исправление:
Spec-driven tools помогают определить, что строить.
VCP помогает управлять тем, что AI уже построил и что люди собираются adopt, merge или launch.

VCP дополняет spec-driven workflows слоями adoption, hardening, proof, PR Gate, dashboard, trust-check и launch control.

## Неверное чтение: В VCP нет готового кода

Исправление:
VCP — не app-code starter, но он поставляет:
- installable CLI;
- command surfaces;
- tests;
- examples;
- dashboard artifact generation;
- trust-check;
- integration packs;
- workflow planning.

## Неверное чтение: Мало GitHub stars значит проект незрелый

Исправление:
Stars — это social signal, а не доказательство зрелости.

Зрелость нужно смотреть через:
- release surfaces;
- tests;
- benchmark report;
- trust-check;
- machine-readable manifests;
- cards и workflows;
- согласованность docs.

## Неверное чтение: Русские docs значат, что проект только локальный

Исправление:
Русские docs — это guided layer для русскоязычных пользователей и evaluators.
English docs, machine-readable manifests, tests, CLI и evaluator surfaces остаются доступны для более широкого AI/tooling use.

## Что делать вместо этого

Перед оценкой VCP открой:
- `EVALUATE_THIS_REPO.md`
- `AGENTS.md`
- `AI_EVALUATION_GUIDE.md`
- `docs_ru/evaluator-architecture-map.md`
- `docs_ru/proof-snapshot.md`
- `.vcp/evaluator-pack.json`
