# AI Ecosystem Watchlist

Текущий пакет репозитория: `v0.9.4`

VCP использует этот watchlist как governance-surface для проверки внешних AI
tools, моделей, developer tooling, training resources и ecosystem references.

VCP не поставляет эти внешние tools.
Он не заявляет official integration, endorsement, bundled support или
собственную поставку этих решений.

## Зачем это нужно

Команды часто перескакивают от трендового репозитория сразу к пилоту.
Watchlist добавляет более безопасный путь:

1. классифицировать инструмент;
2. зафиксировать, почему он важен;
3. записать license и reuse notes;
4. отметить maturity и risks;
5. сопоставить с VCP review path;
6. присвоить статус `watch`, `candidate`, `approved-for-demo`,
   `approved-for-client-review`, `blocked` или `roadmap-only`.

## Что уже существовало

До `v0.9.4` в VCP уже были:
- [Ecosystem Map](./ecosystem-map.md) для позиционирования VCP в широкой AI-экосистеме;
- [AI Tooling](./ai-tooling.md) для практической работы рядом с AI coding tools;
- [Integration Proof Matrix](./integration-proof-matrix.md) для shipped copy-ready kits;
- [Current Limitations](./current-limitations.md) и [Scope Boundary](./scope-boundary.md) для честких границ.

Этот watchlist расширяет эти слои, а не дублирует их.

## Статусы

- `watch`: стоит наблюдать.
- `candidate`: заслуживает scoped review.
- `approved-for-demo`: приемлемо для sandbox/demo.
- `approved-for-client-review`: можно обсуждать или пилотировать с клиентом.
- `blocked`: нельзя принимать без дополнительной проверки.
- `roadmap-only`: признано, но не внедряется сейчас.

## Категории

- agent tooling
- RAG
- vector DB
- inference/deployment
- UI/demo
- evaluation
- security
- MLOps
- local models
- documentation
- developer training

## С чем использовать вместе

Используйте этот watchlist вместе с:
- [Model / Tool Governance](./model-tool-governance.md)
- [AI Stack Adoption Checklist](./ai-stack-adoption-checklist.md)
- [Ecosystem Scouting Workflow](./ecosystem-scouting-workflow.md)
- [Evidence Bundle](./evidence-bundle.md)
- [Current Limitations](./current-limitations.md)

## Важная граница

Это не:
- полный AI-каталог;
- model registry;
- hosted scouting service;
- GitHub trending clone;
- Hugging Face clone.

Это governance-oriented review surface для внедрения внешних AI-компонентов.
