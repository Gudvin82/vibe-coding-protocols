# Versioning

This project has two related version lines:

- **Repository package version** (`v0.1.x`) — tracks the GitHub toolkit packaging: README, scripts, examples, CI, installer, docs and release polish.
- **Web methodology version** (`v1.4`) — tracks the public methodology pages at `anmalishev.ru`.

Current state:
- Repository package: `v0.1.6`
- Web methodology: `Vibe Coding Protocols v1.4`

This split is intentional:
- the website is the public reading / methodology surface;
- the GitHub repository is the markdown / fork / copy / toolkit package.

A future repository `v1.0.0` release may be used after external feedback,
real adoption signals and a stable toolkit interface.

## What would make repository v1.0.0?

The repository should move to `v1.0.0` only after at least some of the following are true:

- external users have tried the toolkit and provided feedback;
- installer and vibe-check behavior is stable;
- README onboarding is clear for new users;
- examples are tested and useful;
- issue templates and contribution flow are working;
- at least one real or anonymized case study exists;
- GitHub Actions are stable;
- versioning and release notes are consistent;
- the project has a clear compatibility policy for scripts and templates.

## Prompt versioning inside real projects

Если проект ведется через AI, полезно сохранять адаптированные prompt-блоки в `docs/PROMPTS.md`.

Минимум:
- дата;
- версия протокола;
- какой prompt использовался;
- какой был результат;
- какие файлы были изменены;
- какие риски остались.
