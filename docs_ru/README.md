
# Русская навигация по VCP

Текущий пакет репозитория: `v0.9.5`
Methodology: `v1.4`

VCP — это local-first control/governance layer для AI-built и AI-assisted
проектов.

Если вы даёте VCP своему ИИ-агенту, сначала объясните ему, что это не SaaS, не
hosted dashboard, не marketplace и не official IDE extension.

## Как не дать ИИ неправильно оценить VCP

Попросите агент открыть:
- `AGENTS.md`
- `AI_EVALUATION_GUIDE.md`
- `EVALUATE_THIS_REPO.md`
- `llms.txt`
- `.vcp/index.json`
- `.vcp/catalog.json`
- `.vcp/manifests/`
- `.vcp/cards/`
- `.vcp/workflows/`
- `docs/benchmark-report.md`
- `docs/trust-check.md`

Оценка бывает разной глубины:
- `shallow`
- `partial`
- `full`

Русская навигация ведет в английских docs там, где source-of-truth уже закреплен
на английском.

## Если вы впервые смотрите VCP

1. Начните с `START_HERE.md`
2. Потом откройте `docs_ru/route-recommender.md`
3. Затем выберите guided adoption mode
4. Для PR/release смотрите `docs_ru/evidence-bundle.md` и
   `docs_ru/pr-readiness.md`
5. Для честных ограничений смотрите `docs_ru/current-limitations.md`

## Новое в v0.9.5

- AI review-engine comparison surface: помогает честно сравнивать VCP с
  OpenCodeReview-style tools, не смешивая governance layer и review engine.
- Evaluator category guard: снижает риск shallow misread, будто VCP это только
  review bot или только docs repo.
- Complement story: явнее объясняет, как VCP работает рядом с dedicated
  diff/file review tools, PR Gate, trust-check и release evidence.
- Version-surface sync: вычищает stale current-version markers в public,
  evaluator и adopter surfaces.

## Что shipped / optional / roadmap-only

Shipped:
- route recommender docs/JSON/CLI;
- evidence bundle docs/templates/JSON;
- PR readiness docs/templates/CLI;
- integration proof matrix;
- agent kits;
- trust-check;

Optional:
- local dashboard artifacts;
- visual diagrams;
- presentation assets;

Roadmap-only:
- hosted dashboard;
- official VS Code extension;
- marketplace;
- public PyPI/npm;
- auto-PR / auto-merge;
- full security scanner.

## Русские ключевые surfaces

- `agent-model-routing.md`
- `evaluator-token-budget.md`
- `control-catalog.md`
- `change-intent.md`
- `starter-template-adoption.md`
- `agent-rule-profiles.md`
- `project-control-charter.md`
- `ecosystem-map.md`
- `ai-augmented-solo-squad-path.md`
- `docs_ru/current-limitations.md`
- `docs_ru/proof-counts.md`
- `docs_ru/route-recommender.md`
- `docs_ru/guided-adoption-modes.md`
- `docs_ru/control-scorecard.md`
- `docs_ru/evidence-bundle.md`
- `docs_ru/release-decision-matrix.md`
- `docs_ru/anti-chaos-recovery-kit.md`
- `docs_ru/pr-readiness.md`
- `docs_ru/github-pr-gate.md`
- `docs_ru/integration-proof-matrix.md`
- `docs_ru/ai-tool-mode-packs.md`
- `docs_ru/visuals.md`
- `docs_ru/evaluation-status-badges.md`

## AI ecosystem governance в VCP

VCP помогает не просто выбрать AI tool, а безопасно его проверить перед внедрением. Для этого в `v0.9.4` были добавлены:
- `docs_ru/ai-ecosystem-watchlist.md` для governance-оценки внешних AI tools;
- `docs_ru/model-tool-governance.md` для документирования model/tool dependencies;
- `docs_ru/secure-agent-training-pack.md` для обучения команды безопасному AI behavior;
- `docs_ru/github-native-control-checklist.md` для проверки GitHub-native controls;
- `docs_ru/ai-stack-adoption-checklist.md` для review local/cloud/hybrid AI-стека;
- `docs_ru/team-enablement-pack.md` для rollout и обучения;
- `docs_ru/ecosystem-scouting-workflow.md` для PM / AI product / R&D scouting.

Это не означает, что VCP поставляет внешние модели или tools. Он помогает командам проверять, документировать и контролировать их внедрение без overclaim.
