# Killer Workflow

Repository package: `v0.8.9`

## Объяснение за минуту

VCP превращает raw AI MVP в reviewable launch-control package: route, risk, plan, PR Gate, metrics, dashboard и launch decision.

## Сценарий

У тебя есть небольшой messy AI-generated MVP, и ты хочешь понять:
- можно ли его уже показывать;
- какие риски остались;
- какие следующие launch-control actions нужны.

## Inputs

- существующий repository или cloned project;
- AI-generated MVP или частично governed codebase;
- без предположений о hosted platform.

## Команды

```bash
vcp doctor --json
vcp onboard --json
vcp classify --json
vcp workflow plan --id mvp-to-launch --json
vcp adopt plan --pack saas-ai-mvp-hardening --json
vcp pr-gate explain --json
vcp metrics board --json
vcp dashboard build --output ./vcp-dashboard --json
```

Fallback из cloned repo:

```bash
python3 -m vcp_cli doctor --json
python3 -m vcp_cli onboard --json
python3 -m vcp_cli classify --json
python3 -m vcp_cli workflow plan --id mvp-to-launch --json
python3 -m vcp_cli adopt plan --pack saas-ai-mvp-hardening --json
python3 -m vcp_cli pr-gate explain --json
python3 -m vcp_cli metrics board --json
python3 -m vcp_cli dashboard build --output ./vcp-dashboard --json
```

## Expected outputs

- route и project classification;
- adoption plan;
- PR Gate explanation;
- metrics board summary;
- local dashboard artifact;
- launch-control ссылки на proof, backlog и checklist surfaces.

## Как интерпретировать результат

- `doctor`: подтверждает локальное здоровье runtime/repository.
- `onboard` + `classify`: показывают подходящий track и path.
- `workflow plan`: переводит ситуацию в guided path.
- `adopt plan`: объясняет, что безопасно copy/govern дальше.
- `pr-gate explain`: показывает warn/block logic перед launch.
- `metrics board`: дает компактную review surface.
- `dashboard build`: делает из состояния reviewable local artifact.

## Stop conditions

Остановись и сделай review до более широкого adoption, если:
- route все еще неясен;
- PR Gate предупреждает о unresolved blockers;
- MVP все еще не имеет launch decision clarity;
- появляется соблазн назвать dashboard hosted control plane.

## Next actions

- посмотреть `docs/launch-decision-checklist.md`;
- проверить `docs/proof-layer.md` и `docs/audit-backlog.md`;
- использовать `docs_ru/comparisons.md`, если команде нужна ясность позиционирования.

## Что VCP не делает

VCP не:
- деплоит продукт;
- хостит dashboard;
- сертифицирует production safety;
- заменяет инженерный review.
