# Use This Repository Prompt (RU)

Используйте этот prompt, если хотите дать AI этот репозиторий как workflow toolkit.

```text
Изучи этот репозиторий как workflow toolkit.

Пока не пиши код.

Сначала посмотри:
1. README.md
2. START_HERE.md
3. docs/lite-adoption-path.md
4. docs/README.md
5. templates/README.md
6. commands/README.md

Потом задай мне вопросы:
1. Это новый проект или уже существующий AI-generated код?
2. Это private MVP, public product, client work или production?
3. Какую AI IDE я использую?
4. Какой стек, язык или фреймворк используется?
5. Есть ли auth, payments, personal data, external APIs или deploy?

После этого верни:
- route: Lite / Starter / Hardening / Extended;
- какие файлы копировать первыми;
- какие файлы пока не нужны;
- первую validation command;
- какие риски я могу недооценивать;
- оценку fit по шкале 1–10;
- следующий smallest safe step.

Не называй templates или architecture docs маршрутами сами по себе.
Если нужны agent rules, предпочитай `templates/AGENTS.md`, а не копирование root `AGENTS.md`.

Если ты не можешь открыть GitHub links, попроси меня вставить README.md и START_HERE.md.
```
