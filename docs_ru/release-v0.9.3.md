# Vibe Coding Protocols v0.9.3

## Тема релиза

Route Recommender, Evidence Bundle, PR/Integration Proof и Visual Layer.

## Что добавлено

- proof count synchronization model;
- current limitations page;
- route recommender;
- control scorecard;
- evidence bundle;
- release decision matrix;
- anti-chaos recovery kit;
- guided adoption modes;
- PR readiness pack;
- integration proof matrix;
- AI tool mode packs;
- visual diagrams;
- evaluation status badges;
- trust-check coverage;
- RU docs parity.

## Почему это важно

`v0.9.3` делает VCP проще для первого выбора маршрута, проще для PR/release
handoff и честнее с точки зрения public boundaries.

## Что не входит в релиз

- SaaS;
- hosted dashboard;
- public PyPI/npm publication;
- official VS Code extension;
- marketplace;
- auto-PR;
- auto-merge;
- full security scanner;
- telemetry;
- compliance certification.

## Как проверить

```bash
python3 -m vcp_cli route list --json
python3 -m vcp_cli route recommend --scenario raw-ai-mvp --json
python3 -m vcp_cli scorecard --json
python3 -m vcp_cli pr readiness --json
python3 -m vcp_cli trust-check --json
```

## Для русскоязычных пользователей

Начните с `START_HERE.md`, затем откройте `docs_ru/route-recommender.md`,
`docs_ru/evidence-bundle.md`, `docs_ru/pr-readiness.md` и
`docs_ru/current-limitations.md`.
