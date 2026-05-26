Проведи независимое read-only review активных изменений в текущем репозитории.

Важно:
- не используй контекст предыдущей переписки;
- не редактируй файлы;
- не делай commit, reset, stash или push;
- смотри только текущее состояние репозитория, `git status`, `git diff`, затронутые файлы и результаты проверок;
- оцени только изменения в текущем diff, не уходи в unrelated legacy-проблемы.

Проверь:
1. correctness / возможные баги;
2. regressions;
3. security / privacy риски;
4. data integrity;
5. UX / edge cases;
6. maintainability;
7. missing high-value tests;
8. соответствие архитектуре проекта.

Верни результат в формате:

## Findings

Для каждого finding:
- severity: critical / high / medium / low;
- file:line;
- что не так;
- почему это важно;
- как исправить.

## No actionable findings

Если конкретных actionable замечаний нет, скажи это явно.

## Validation notes

Какие проверки стоит запустить или какие результаты проверок ты видел.

## Review verdict

- pass / pass with notes / needs changes

Не требуй косметических правок без пользы. Не предлагай переписывать архитектуру без конкретного риска.

Важно:
- здесь не используется название `/loop-code-review`;
- здесь не используется `9.5/10`;
- здесь не используются `fork_context` / `reasoning_effort`;
- это vendor-neutral independent diff review prompt.
