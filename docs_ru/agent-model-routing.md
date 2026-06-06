# Маршрутизация моделей для AI-агентов

Repository package: `v0.9.0`

Этот документ нужен, когда вы внедряете VCP в свой репозиторий и хотите тратить AI-токены осознанно.

Это user-facing policy для своей работы.
Это не policy для внешней оценки VCP.
И это не automatic model router.

## Почему VCP вообще говорит про model routing

VCP помогает не сжигать дорогие reasoning-модели на простом repository discovery.

Базовое правило простое:
- fast/cheap tier — для поиска, чтения и low-risk discovery;
- strong/reasoning tier — для mutation, архитектурных решений, debugging и release changes.

Можно приводить примеры вроде Haiku и Sonnet, но policy остается provider-neutral.

## Таблица маршрутизации

| Задача | Рекомендуемый tier | Почему |
|---|---|---|
| grep/search files | fast/cheap | deterministic discovery |
| read README/docs | fast/cheap | low-risk context gathering |
| summarize logs/reports | fast/cheap | no mutation |
| locate command/test | fast/cheap | simple lookup |
| write code patch | strong/reasoning | mutation risk |
| change architecture | strong/reasoning | high reasoning load |
| debug complex failure | strong/reasoning | multi-step reasoning |
| update schemas/manifests/tests | strong/reasoning | consistency risk |
| release prep | strong/reasoning | public surface risk |
| security/safety decision | strong/reasoning | high consequence |

## Практическая policy

### Fast/cheap tier

Используйте fast/cheap tier для:
- grep/search;
- чтения файлов;
- поиска команд;
- summarize logs;
- проверки, существует ли нужная surface;
- сбора точных file references.

### Strong/reasoning tier

Используйте strong/reasoning tier для:
- написания patch;
- architecture changes;
- release prep;
- schema/manifest/test updates;
- debugging complex failures;
- safety-sensitive decisions.

## Важные предупреждения

- Не используйте cheap model для unreviewed code edits.
- Не тратьте expensive model на blind file discovery.
- Сначала search/read, потом edit.
- Всегда указывайте, были ли tests реально запущены.
- Если текущая модель слишком слабая для следующего шага, остановитесь и переключитесь до редактирования.

## Что этот документ не заявляет

Этот guide не заявляет:
- automatic model switching внутри Claude/Codex/Cursor;
- hidden provider configuration;
- model API automation;
- guaranteed cost savings.

Это manual routing policy для осознанного выбора tier по задаче.
