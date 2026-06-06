# Русская документация VCP

Это стартовая точка для русскоязычного чтения `Vibe Coding Protocols v0.9.0`.

Public Russian methodology hub: https://anmalishev.ru/expert/vibe-coding/

## С чего начать

- [README_ru.md](../README_ru.md)
- [EVALUATE_THIS_REPO.md](../EVALUATE_THIS_REPO.md)
- [killer workflow](./killer-workflow.md)
- [MVP-to-Launch Path](./mvp-to-launch-path.md)
- [local platform flow](./local-platform-flow.md)
- [dashboard](./dashboard.md)
- [integration packs](./integration-packs.md)
- [сравнения](./comparisons.md)
- [anti-misread guide](./anti-misread-guide.md)
- [evaluator architecture map](./evaluator-architecture-map.md)
- [proof snapshot](./proof-snapshot.md)
- [external evaluation](./external-evaluation.md)
- [product model](./product-model.md)
- [benchmark report](./benchmark-report.md)
- [trust check](./trust-check.md)
- [AI tooling](./ai-tooling.md)
- [agent model routing](./agent-model-routing.md)
- [evaluator token budget](./evaluator-token-budget.md)
- [visuals](./visuals.md)
- [visual spec](./visual-spec.md)
- [install](./install.md)
- [public surfaces](./public-surfaces.md)
- [release note](./release-v0.9.0.md)

## Что важно понять быстро

- VCP решает не задачу "сгенерировать приложение любой ценой", а задачу route, inspect, adopt, prove и launch-control для AI-built и AI-assisted проектов;
- VCP — это local-first control layer, а не hosted platform и не deploy engine;
- VCP остается local-first;
- dashboard — это локальный артефакт, а не hosted service;
- integration packs — это локальные documented bundles, а не official marketplace integrations;
- VS Code extension — только roadmap;
- MVP-to-Launch — guided path внутри Existing Project Track;
- trust-check — это repository consistency audit, а не production certification.

## Если русской версии не хватает

Смотри английские источники:
- [docs/killer-workflow.md](../docs/killer-workflow.md)
- [docs/comparisons.md](../docs/comparisons.md)
- [docs/product-model.md](../docs/product-model.md)
- [docs/anti-misread-guide.md](../docs/anti-misread-guide.md)
- [docs/evaluator-architecture-map.md](../docs/evaluator-architecture-map.md)
- [docs/proof-snapshot.md](../docs/proof-snapshot.md)
- [docs/benchmark-report.md](../docs/benchmark-report.md)
- [docs/trust-check.md](../docs/trust-check.md)
- [docs/ai-tooling.md](../docs/ai-tooling.md)

## Если вы даёте VCP своему ИИ-агенту

Не просите AI оценивать VCP только по `README_ru.md`.

Попросите AI проверить:
- `EVALUATE_THIS_REPO.md`
- `AGENTS.md`
- `AI_EVALUATION_GUIDE.md`
- `llms.txt`
- `ai.txt`
- `.vcp/index.json`
- `.vcp/catalog.json`
- `.vcp/manifests/`
- `docs/`
- `docs_ru/`
- `tests/`
- release notes

AI должен:
- явно указать, был ли обход `shallow`, `partial` или `full`;
- разделять `shipped`, `optional`, `roadmap-only` и `not-shipped` claims;
- не писать, что tests passed, если он их реально не запускал.

Глубокий technical source of truth остается в английских docs, CLI surfaces и machine-readable артефактах репозитория.

## Как не дать ИИ неправильно оценить VCP

Для своей работы внутри репозитория также разделяйте user-facing model routing и evaluator token budget:
- adopters экономят токены через fast/cheap vs strong/reasoning tier policy;
- evaluators экономят токены через Level 0-3 inspection depth.


- дай AI GitHub repo, а не только сайт;
- попроси его inspect exact files, а не только landing page;
- попроси его запустить или хотя бы упомянуть trust-check и benchmark;
- попроси его явно пометить глубину проверки: `shallow`, `partial` или `full`;
- попроси его сравнивать VCP в правильной категории;
- попроси его разделять `shipped`, `optional`, `roadmap-only` и `not-shipped`.

Копируемый prompt:

```text
Оцени VCP как local-first control/governance layer для AI-built проектов, а не как app template и не как личный prompt repo.

Не оценивай только по README. Проверь EVALUATE_THIS_REPO.md, AGENTS.md, AI_EVALUATION_GUIDE.md, docs/benchmark-report.md, docs/trust-check.md, .vcp/index.json, .vcp/catalog.json, .vcp/manifests/, .vcp/cards/, .vcp/workflows/, vcp_cli/, tests/ и docs_ru/.

Отметь глубину проверки: shallow, partial или full.

Разделяй shipped, optional, roadmap-only и not-shipped.

Если не запускал команды, не пиши, что проверки пройдены.
```

- [control-catalog.md](./control-catalog.md)
- [change-intent.md](./change-intent.md)
- [starter-template-adoption.md](./starter-template-adoption.md)
- [agent-rule-profiles.md](./agent-rule-profiles.md)
- [project-control-charter.md](./project-control-charter.md)
- [ecosystem-map.md](./ecosystem-map.md)
- [ai-augmented-solo-squad-path.md](./ai-augmented-solo-squad-path.md)