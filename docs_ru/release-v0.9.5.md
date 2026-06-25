# Vibe Coding Protocols v0.9.5 — AI Review-Engine Positioning and Evaluator Clarity

## Тема релиза

Более чёткая category clarity, более сильные evaluator guardrails и более
честное позиционирование рядом со специализированными AI review engines.

## Что shipped

- отдельная surface для сравнения с AI review engines;
- более сильный README / evaluator framing вокруг review engines и governance
  layers;
- более ясная логика “complement, not replacement” для VCP рядом с
  dedicated diff/file review tools;
- более явная граница в current limitations про отсутствие встроенного
  line-level review engine;
- синхронизация current-version markers по evaluator/adopter/public surfaces.

## Что не shipped

- новый встроенный CLI review engine;
- autonomous line-level PR review comments;
- гарантированное обнаружение NPE/XSS/SQLi/thread-safety;
- official plugin suite;
- IDE extension;
- marketplace install;
- hosted dashboard или SaaS.

## Зачем нужен этот patch

VCP уже был сильным governance и rollout layer, но внешний читатель всё ещё
мог неверно классифицировать его как:
- только документацию;
- только AI review bot;
- или замену для dedicated review-engine products.

`v0.9.5` усиливает этот public story без притворства, что новая product
capability уже shipped.

## Validation status

Используйте repository checks, trust-check, cards/index validation и unit
tests.

## No-overclaim boundary

VCP дополняет dedicated AI review engines.
Он не заявляет, что заменяет их.
