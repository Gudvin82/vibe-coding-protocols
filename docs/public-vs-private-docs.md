# Public vs Private Docs

Этот репозиторий содержит публичные templates.

## Что здесь можно хранить

- публичные markdown-шаблоны;
- универсальные checklists;
- vendor-neutral prompts;
- sanitized examples;
- общие architecture patterns без sensitive details.

## Что не стоит выкладывать публично

Не публикуйте в открытом repo:
- secrets;
- internal endpoints;
- внутренние IP;
- tokens;
- admin routes;
- private APIs;
- incident details;
- production configs;
- customer data;
- реальные on-call / escalation paths;
- private architecture diagrams с operational specifics.

## Real project docs

Реальные `AGENTS.md`, `PROJECT_MAP.md`, `ARCHITECTURE.md`, incident runbooks, deployment notes и security docs проекта часто содержат sensitive details.

Их лучше хранить:
- private;
- sanitized;
- encrypted;
- вне public webroot.
