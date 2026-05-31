# Vibe Coding Protocols

[Русская версия](./README_ru.md)

[![Repo Version](https://img.shields.io/badge/repo-v0.5.1-blue)](./CHANGELOG.md)
[![Methodology](https://img.shields.io/badge/methodology-v1.4-purple)](https://anmalishev.ru/expert/vibe-coding/)
[![AI Intake Ready](https://img.shields.io/badge/AI%20Intake-ready-brightgreen)](./AI_INTAKE.md)
[![CLI Local](https://img.shields.io/badge/CLI-local-blue)](./docs/cli.md)
[![Manifests](https://img.shields.io/badge/manifests-v1-blue)](./vcp.manifest.json)
[![Benchmarks](https://img.shields.io/badge/benchmarks-local-blue)](./benchmarks/ai-adoption/README.md)

**Not a prompt collection.**

VCP is a controlled AI delivery framework for AI-assisted software development.
It provides routes, protocols, adoption packs, validation, review gates, manifests, benchmarks and project memory so AI agents do not write or change code chaotically.

Repository package: `v0.5.1`

Web methodology: `Vibe Coding Protocols v1.4`

## Give this repo to your AI

Start with [AI_INTAKE.md](./AI_INTAKE.md), not with a shallow README skim.
If agent rules are needed, prefer [templates/AGENTS.md](./templates/AGENTS.md) over copying root `AGENTS.md`.
Then route through:
- [START_HERE.md](./START_HERE.md)
- [docs/protocol-index.md](./docs/protocol-index.md)
- [docs/adoption-packs.md](./docs/adoption-packs.md)
- [templates/prompts/evaluate-vcp-for-my-repo.md](./templates/prompts/evaluate-vcp-for-my-repo.md)

## Windows and external API safety

Windows users can use the Python CLI from PowerShell for core VCP workflows.
Bash scripts remain supported for legacy parity.
When adding any external API, run Third-party API Intake before writing integration code.
Public or free API does not mean production-safe.

## Start here

| Situation | Start here |
|---|---|
| New project or idea | [Starter Protocol](./protocols/ai-project-starter-protocol.md) |
| Existing AI-generated MVP | [Hardening Protocol](./protocols/ai-project-hardening-protocol.md) |
| Production, regulated or shared engine repo | [AI_INTAKE.md](./AI_INTAKE.md) + [adoption packs](./docs/adoption-packs.md) |
| Working code that is hard to change | [Maintenance Refactoring](./protocols/maintenance/care-refactoring.md) |
| UI styling or component ownership drift | [UI Component Ownership](./protocols/maintenance/ui-refactoring.md) |
| External API, SDK or webhook proposal | [Third-party API Intake](./protocols/integrations/third-party-api-intake.md) |
| Active diff that must be accepted before moving on | [Post-Task Code Review](./protocols/review/post-task-code-review.md) |
| Public docs or marketing site | [Public Site Readiness](./docs/public-site-readiness.md) |

## Current CLI surface

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli check --fast
python3 -m vcp_cli route --profile production --json
python3 -m vcp_cli route --profile third-party-api --json
python3 -m vcp_cli adopt --pack third-party-api --dry-run --json
python3 -m vcp_cli manifest validate
python3 -m vcp_cli benchmark run
python3 -m vcp_cli score --json
```

Windows PowerShell:

```powershell
py -m vcp_cli doctor
py -m vcp_cli check --fast
py -m vcp_cli route --profile production --json
```

## What VCP is not

- not a hacking toolkit;
- not an exploit framework;
- not a pentest suite;
- not a bug bounty automation suite;
- not a public API directory;
- not a public API recommendation engine;
- not a production security certification;
- not a legal compliance certification;
- not a replacement for developers, tests, security review, legal review or human judgment.

## Key links

- [AI_INTAKE.md](./AI_INTAKE.md)
- [docs/cli.md](./docs/cli.md)
- [docs/windows.md](./docs/windows.md)
- [docs/protocol-index.md](./docs/protocol-index.md)
- [docs/adoption-packs.md](./docs/adoption-packs.md)
- [docs/security-tooling-landscape.md](./docs/security-tooling-landscape.md)
- [docs/tooling-roadmap.md](./docs/tooling-roadmap.md)
- [docs/known-limitations.md](./docs/known-limitations.md)
- [docs/release-v0.5.1.md](./docs/release-v0.5.1.md)
