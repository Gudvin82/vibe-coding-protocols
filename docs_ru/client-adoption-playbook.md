<!-- vcp-version: v0.9.5 -->
<!-- methodology-version: v1.4 -->
# Client Adoption Playbook

Используйте этот playbook, когда VCP внедряется в реальную команду, клиентский проект или портфель продуктов.

## Definition of success

После `v0.9.5` внедрение VCP для команд и клиентов должно стать более практичным и менее расплывчатым.

Успех означает:
- консультант или tech lead может ясно объяснить, где VCP помогает, а где его границы;
- команда выбирает один понятный rollout path вместо чтения всего репозитория подряд;
- настройка AI tools становится copy-ready, а не импровизированной;
- trust-check, PR Gate и audit backlog работают как реальные практики, а не как абстрактные обещания;
- leadership получает конкретные evidence и rollout artifacts вместо общих заявлений про AI governance.

## Canonical client flow

Используйте этот 8-step flow как базовый путь для первого внедрения:

1. Сформулировать цель и boundary для клиента или команды.
2. Провести discovery и technical intake.
3. Выбрать VCP track и уровень rigor.
4. Подготовить customer repo scaffold и agent kit.
5. Запустить trust-check и выделить начальные риски.
6. Открыть audit backlog и назначить ownership.
7. Использовать PR Gate и release evidence во время pilot sprint.
8. Завершить pilot retrospective, reporting и решением о scale rollout.

## Three entry files for client/team adoption

Если возникает вопрос «с каких файлов реально начинать?», используйте эти три entry files:

1. `START_HERE.md`
2. `docs/client-adoption-playbook.md`
3. `docs/integrations/agent-kits.md`

Почему именно они:
- `START_HERE.md` помогает выбрать маршрут;
- этот playbook показывает rollout lifecycle;
- `docs/integrations/agent-kits.md` показывает, что именно копировать в реальные AI coding environments.

## Этапы

### 1. Discovery
- Цель: понять, где AI coding уже используется.
- Входы: активные репозитории, инструменты, основные опасения.
- Выходы: гипотеза adoption package и первый список рисков.
- См.: `docs/client-discovery.md`.

### 2. Technical intake
- Цель: разобрать архитектуру, release flow, tests и risky zones.
- Выходы: intake summary, candidate track и первые backlog items.
- См.: `docs/technical-intake-workshop.md`.

### 3. Track selection
- Цель: выбрать самый честный и минимальный VCP route.
- Выходы: recommended track, rigor level и первые artifacts.
- См.: `docs/track-selection-for-clients.md`.

### 4. Customer repo scaffold
- Цель: подготовить минимальный local control layer.
- Выходы: starter files, agent instructions и PR Gate placeholders.
- См.: `docs/customer-repo-scaffold.md`.

### 5. AI governance и risk model
- Цель: явно определить allowed / risky / review-required AI usage.
- Выходы: local policy notes, trust-check baseline и backlog categories.

### 6. Sprint operating model
- Цель: встроить VCP в реальную cadence поставки без лишней бюрократии.
- Выходы: pilot cadence, work-package discipline и review rhythm.

### 7. Executive reporting
- Цель: перевести rollout evidence в понятный для leadership статус.
- Выходы: rollout summary, risk trend и next decision.
- См.: `docs/executive-reporting.md`.

### 8. Retrospective и scale
- Цель: понять, что стандартизировать, что упростить и что не масштабировать.
- Выходы: pilot retrospective и scale/no-scale recommendation.

## First command set

```bash
python3 -m vcp_cli trust-check --json
python3 -m vcp_cli onboard --json
python3 -m vcp_cli agents kit --target copilot --json
```

## Boundary

Это не hosted governance platform.
Это local-first operating model, templates, checks и evidence surfaces для controlled AI development.
