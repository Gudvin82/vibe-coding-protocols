# Secure Agent Training Pack

Текущий пакет репозитория: `v0.9.5`

Это lightweight onboarding layer для более безопасной AI-assisted работы.
Это не game engine и не security certification.

## Для чего использовать

Пакет помогает обучать участников и reviewers вовремя останавливать unsafe AI
behavior до того, как он превратится в drift, overclaim, risky release behavior
или опасные repo-wide changes.

## Покрываемые сценарии

1. AI хочет менять auth code без review.
2. Агент добавляет dependency без license/security review.
3. AI пишет public claim без evidence.
4. Multi-agent reviews конфликтуют.
5. Secret попадает в prompt/code.
6. PR готовится без tests/trust-check.
7. Агент делает broad rewrite вне scope.
8. AI называет release production-ready без evidence.
9. Агент меняет CI/release files без approval.
10. AI предлагает dangerous shell command.

## Связанные surfaces

- [Team Enablement Pack](./team-enablement-pack.md)
- [PR Readiness](./pr-readiness.md)
- [GitHub-native Control Checklist](./github-native-control-checklist.md)
- [Current Limitations](./current-limitations.md)
