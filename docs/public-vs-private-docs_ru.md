# Public vs Private Documentation

Используйте этот файл, чтобы понять, что можно держать в публичном репозитории,
а что лучше оставить private, sanitized или access-controlled.

## Safe to publish

- публичные markdown-шаблоны;
- универсальные checklists;
- vendor-neutral prompts;
- sanitized examples;
- общие architecture patterns без sensitive operational details;
- release notes и public onboarding docs.

## Keep private

Не публикуйте в открытом repo:
- secrets;
- internal endpoints;
- внутренние IP ranges;
- реальные tokens или credentials;
- admin routes;
- private APIs;
- incident details с operational specifics;
- production configs;
- customer data;
- реальные on-call или escalation paths;
- подробные architecture diagrams, раскрывающие sensitive operations.

## Sanitize before sharing with AI

Перед тем как передавать внутренние документы в AI-инструмент:
- удалите secrets и tokens;
- замените реальные customer names и identifiers;
- уберите internal hostnames и IPs;
- замаскируйте production-only routes и credentials;
- оставьте только тот архитектурный контекст, который нужен для задачи.

## Encrypt or restrict access

Реальные `AGENTS.md`, `PROJECT_MAP.md`, `ARCHITECTURE_SOURCE_OF_TRUTH.md`,
incident runbooks, deployment notes и security docs часто содержат sensitive
details.

Их лучше хранить в private repository, encrypted storage или другой
access-restricted системе, если там есть operational specifics.

## Architecture Source of Truth policy

Публичный template в этом репозитории безопасно копировать и адаптировать.

Реальная проектная версия может содержать:
- private deployment paths;
- internal integration notes;
- details по secret handling;
- rollback contacts;
- incident recovery procedures;
- ownership accepted risks.

Такую реальную версию обычно стоит держать private или тщательно sanitizе.

## Examples

Примеры в этом репозитории — synthetic или sanitized learning material.

Это не реальные production projects и не доказательство того, что публичный
проект можно безопасно раскрывать в таком же виде.
