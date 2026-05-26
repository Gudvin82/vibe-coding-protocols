# Repository Maintenance

## Maintenance goals

- keep links valid;
- keep prompts copyable;
- keep templates sanitized;
- avoid vendor lock-in;
- avoid accidental publication of sensitive operational details.

## Before every public update

Проверьте:
1. нет `.env`;
2. нет private paths;
3. нет реальных токенов;
4. нет customer data;
5. нет copied third-party skills;
6. все ссылки работают;
7. README и changelog синхронизированы.

## What not to automate too early

На первом релизе не обязательно добавлять GitHub Actions.

Позже можно добавить:
- markdown lint;
- link checker;
- spell check;
- secret scan for repo hygiene.
