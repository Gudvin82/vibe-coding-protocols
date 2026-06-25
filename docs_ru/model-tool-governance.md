# Model / Tool Governance

Текущий пакет репозитория: `v0.9.5`

AI models, datasets, agent tools, inference endpoints, UI tools и evaluation
components должны рассматриваться как зависимости проекта.
Им нужны review, owner и documented boundaries.

## Зачем это нужно

Команды уже проверяют package dependencies.
AI-assisted команды должны так же проверять:
- какая модель или tool используется;
- куда уходят данные;
- какие license/terms действуют;
- что инструменту разрешено делать;
- какой есть fallback, если он недоступен или заблокирован.

## Что документировать

Для каждой зависимости нужно фиксировать:
- name;
- type;
- source/provider;
- local/cloud/hybrid;
- license;
- terms/usage notes;
- data sensitivity;
- approved usage;
- prohibited usage;
- review owner;
- risk level;
- fallback option;
- last reviewed;
- evidence links.

## Границы

- VCP не даёт legal advice.
- VCP не сертифицирует license compliance.
- VCP не сертифицирует vendor security или production readiness.
- VCP помогает командам единообразно документировать и проверять AI dependencies.
