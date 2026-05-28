# Deploy Path

VCP recommends local-first by default.

## Local-first

Before cloud deploy:
- run locally;
- document env vars;
- document database;
- document storage;
- document auth providers;
- document rollback path.

## Cloud-later

Choose cloud only when:
- MVP flow works locally;
- secrets are documented;
- deployment owner is known;
- rollback path exists.

## Deployment prerequisites

For any deploy target, document:
- account owner;
- CLI or tooling;
- credentials storage;
- database provisioning;
- object storage;
- domains and DNS;
- environment variables;
- rollback plan.

Examples: DigitalOcean, Yandex Cloud, Vercel, Render, Fly, self-hosted.
