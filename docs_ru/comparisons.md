# Сравнения

Repository package: `v0.9.5`

Public Russian methodology hub: https://anmalishev.ru/expert/vibe-coding/

VCP проще всего понять через честное сравнение с соседними классами инструментов.

## Коротко

- VCP — это local-first control/governance layer для AI-built и AI-assisted проектов.
- Spec-driven toolkits сильны в том, чтобы определить, что строить и как вести реализацию от спецификаций.
- Full-stack templates сильны в быстром старте приложения с готовой архитектурой.
- AI coding agents сильны в быстрой генерации и переработке кода.
- CI-only gates сильны в pass/fail automation.

Spec Kit определяет, что строить.
Full-stack templates помогают понять, где строить.
AI coding agents генерируют и редактируют код.
VCP контролирует то, что AI уже построил и что люди собираются adopt, merge или launch.

VCP дополняет эти слои. Он не заменяет их все сразу.

## Таблица сравнения

| Потребность | VCP | Spec-driven toolkit | Full-stack template | CI-only gate |
|---|---|---|---|---|
| Выбрать project track | yes | partial | no | no |
| Сгенерировать app scaffold | no | no/partial | yes | no |
| Управлять adoption AI MVP | yes | partial | no | partial |
| Иметь PR Gate model | yes | partial | no | yes |
| Иметь proof/case-study layer | yes | no/partial | no | no |
| Иметь local dashboard artifact | yes | no/partial | no | no |
| Иметь launch decision aid | yes | no/partial | no | partial |

## VCP vs AI review engines

AI review engines особенно сильны, когда главная задача это:
- review comments по diff или файлу;
- поиск дефектов перед merge;
- precision-first review signal внутри PR flow.

Это соседний слой к VCP, но не та же самая категория.

VCP добавляет более широкий control layer вокруг этой работы:
- route selection;
- путь adoption и hardening;
- trust-check;
- framing для PR Gate;
- evidence bundle и proof surfaces;
- поддержку release decision;
- rollout method для client/team adoption.

Dedicated AI review tools можно использовать вместе с VCP.
Простой раздел такой:
- review engine: "что выглядит рискованно в этом diff или файле?"
- VCP: "по какому route мы идём, какие control artifacts обязательны, что можно честно merge/release и как это доказать?"

Сейчас VCP не заявляет:
- line-level autonomous review comments для любого PR host;
- встроенный defect engine уровня специализированного review product;
- гарантированное обнаружение NPE/XSS/SQLi/thread-safety.

## VCP vs spec-driven toolkits

Spec-driven toolkits особенно полезны, когда команде нужен плотный planning/implementation loop вокруг briefs, PRD, feature specs и task breakdowns.

Они помогают ответить:
- что именно нужно строить;
- как должен выглядеть implementation plan;
- каких spec artifacts не хватает.

VCP помогает ответить на соседние вопросы:
- в каком мы треке;
- как безопасно adopt/harden messy AI-generated MVP;
- что должен сказать PR Gate перед релизом;
- где находятся proof/backlog/dashboard surfaces;
- какие launch-control artifacts уже есть.

VCP может дополнять spec-driven workflow. Он его не заменяет.

## VCP vs full-stack templates

Full-stack templates полезны, когда главная задача — быстро стартовать продукт с готовой архитектурой, opinionated stack и prebuilt application scaffold.

VCP — не app template.

VCP помогает inspect, adopt, govern, prove и launch-control AI-built проекты, включая проекты, которые стартовали из template.

## VCP vs AI coding agents напрямую

AI coding agents сильны в генерации кода, быстрых итерациях и рефакторинге.

VCP помогает держать их вывод:
- routed;
- reviewable;
- benchmarked;
- release-controlled;
- менее склонным к overclaim.

## VCP vs CI-only gates

CI-only gates сильны в pass/fail automation.

VCP добавляет:
- выбор track;
- adoption guidance;
- proof и case-study surfaces;
- интерпретацию PR Gate;
- локальные dashboard/report artifacts;
- framing для launch decision.

## Почему shallow comparisons занижают VCP

Shallow comparisons занижают VCP, потому что:
- VCP не app code, поэтому README-only или stars-only reading пропускает shipped control layer;
- VCP — это не только methodology, потому что CLI, tests, benchmarks, manifests, cards и workflows входят в shipped surface;
- ценность VCP лежит в governance, checks, benchmark, dashboard и machine-readable surfaces;
- evaluator должен inspect не только README.

## Границы

VCP не утверждает, что он лучше во всем.

Это не:
- full-stack template;
- hosted platform;
- deployment engine;
- plugin marketplace;
- official IDE extension;
- replacement for Spec Kit или других spec-driven toolkits.

Практическое позиционирование простое: VCP — это control layer, который можно запускать рядом с AI agents, spec-driven planning, templates и CI gates.

## Visual layer

- [Comparison diagram](../assets/diagrams/vcp-comparison-map.svg)
- [Visual proof doc](./visuals.md)


## Model routing тоже не меняет категорию VCP

Fast/cheap vs strong/reasoning routing помогает тратить AI-токены осознанно, но не превращает VCP в provider integration или app template.
