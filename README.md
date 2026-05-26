# Vibe Coding Protocols

![Repo Version](https://img.shields.io/badge/repo-v0.1.0-blue)
![Methodology](https://img.shields.io/badge/methodology-v1.4-purple)
![License](https://img.shields.io/badge/license-CC%20BY%204.0-green)
![Updated](https://img.shields.io/badge/updated-May%202026-brightgreen)
![Website](https://img.shields.io/badge/website-anmalishev.ru-black)
![Toolkit](https://img.shields.io/badge/type-markdown%20toolkit-informational)

**Practical protocols, prompts and markdown templates for safer AI-assisted / vibe coding projects.**

Use this toolkit to:
- start AI-generated projects without chaos;
- create a Product Brief before coding;
- define active / deferred surfaces;
- set up `AGENTS.md`, `PROJECT_MAP.md` and `Architecture Source of Truth`;
- audit AI-generated code before merge, deploy or production;
- check security, supply-chain, self-protection and database/load readiness;
- keep an audit backlog and use AI IDEs more safely.

Official web version:
[https://anmalishev.ru/expert/vibe-coding/](https://anmalishev.ru/expert/vibe-coding/)

## Repository and methodology versions

- Repository version: `v0.1.0`
- Web methodology version: `Vibe Coding Protocols v1.4`
- This repository is a markdown/toolkit packaging of the public web methodology from `anmalishev.ru`.

## What this is

Vibe Coding Protocols is a practical methodology for building, auditing and hardening AI-generated projects.

It helps you:
- start an AI project without chaos;
- create a Product Brief before coding;
- choose a stack and starter path;
- define active / deferred surfaces;
- create `AGENTS.md`, `PROJECT_MAP.md` and `Architecture Source of Truth`;
- audit AI-generated code before merge, deploy or production;
- check security, supply-chain, self-protection, database/load readiness and production readiness;
- maintain an audit backlog;
- use Claude Code, Codex, Cursor, Windsurf and other AI IDEs more safely.

## Use with your AI IDE

### Claude Code
Copy [CLAUDE.md](./CLAUDE.md) or [agents/CLAUDE.md.example](./agents/CLAUDE.md.example) into your project and start with [prompts/master-prompt-short.md](./prompts/master-prompt-short.md).

### Codex
Use [AGENTS.md](./AGENTS.md) plus the relevant protocol and prompt files. If external links are unavailable, paste the needed markdown files directly into the task.

### Cursor
Use the protocols as planning documents, copy [.cursorrules](./.cursorrules) or [agents/CURSOR.md.example](./agents/CURSOR.md.example), and apply Stop Conditions before larger Composer edits.

### Windsurf
Use [.windsurfrules](./.windsurfrules) or [agents/WINDSURF.md.example](./agents/WINDSURF.md.example) as a Cascade scope guard: active surfaces, deferred surfaces, approval gates and validation.

## Official web version

- Hub: [https://anmalishev.ru/expert/vibe-coding/](https://anmalishev.ru/expert/vibe-coding/)
- Starter: [https://anmalishev.ru/expert/vibe-coding-starter.html](https://anmalishev.ru/expert/vibe-coding-starter.html)
- Hardening: [https://anmalishev.ru/expert/ai-project-hardening.html](https://anmalishev.ru/expert/ai-project-hardening.html)
- Templates: [https://anmalishev.ru/expert/templates/](https://anmalishev.ru/expert/templates/)
- Architecture Source of Truth: [https://anmalishev.ru/expert/templates/architecture-source-of-truth.html](https://anmalishev.ru/expert/templates/architecture-source-of-truth.html)

## Quick Start

### If you only have an idea

1. Open [prompts/product-brief-prompt.md](./prompts/product-brief-prompt.md)
2. Create a Product Brief
3. Continue with [protocols/ai-project-starter-protocol.md](./protocols/ai-project-starter-protocol.md)

### If you already have AI-generated code

1. Open [protocols/ai-project-hardening-protocol.md](./protocols/ai-project-hardening-protocol.md)
2. Start with Light Hardening
3. Create or update [templates/AUDIT_BACKLOG.md](./templates/AUDIT_BACKLOG.md)

### If you want to give this repo to your AI

Use:
- [prompts/master-prompt-short.md](./prompts/master-prompt-short.md)
- [prompts/master-prompt-full.md](./prompts/master-prompt-full.md)

If your AI cannot open links, paste the required markdown files from this repository directly.

## Repository tree

```text
vibe-coding-protocols/
├── protocols/
│   ├── ai-project-starter-protocol.md      # Start a new AI project safely
│   ├── ai-project-hardening-protocol.md    # Audit existing AI-generated code
│   ├── starter-to-hardening-bridge.md      # Move from first slice to audit
│   └── ai-ide-compatibility.md             # Claude Code / Codex / Cursor / Windsurf
├── prompts/
│   ├── master-prompt-short.md              # Route the project before coding
│   ├── product-brief-prompt.md             # Product Brief / technical intake
│   ├── starter-prompts.md                  # Starter prompt blocks
│   └── hardening-prompts.md                # Hardening prompt blocks
├── templates/
│   ├── AGENTS.md                           # Reusable AI agent policy template
│   ├── PROJECT_MAP.md                      # File map and system context
│   ├── AUDIT_BACKLOG.md                    # Findings and follow-up backlog
│   └── ARCHITECTURE_SOURCE_OF_TRUTH.md     # Architecture reference template
├── agents/
│   ├── CLAUDE.md.example                   # Detailed Claude Code adaptation
│   ├── CODEX.md.example                    # Detailed Codex adaptation
│   ├── CURSOR.md.example                   # Detailed Cursor adaptation
│   └── WINDSURF.md.example                 # Detailed Windsurf adaptation
├── examples/                               # Synthetic walkthroughs and mini playbooks
├── checklists/                             # Quick operational checklists
├── docs/                                   # Attribution, releases, versioning, notes
├── scripts/                                # Lightweight MIT-licensed helper scripts
└── .github/workflows/                      # Toolkit-only automation helpers
```

## Repository structure

- [protocols/](./protocols/) — markdown versions of the hub, Starter, Hardening and bridge files
- [prompts/](./prompts/) — short and full prompt blocks by stage
- [templates/](./templates/) — Artifact Pack and reusable project templates
- [agents/](./agents/) — AI IDE adaptation examples for Claude Code / Codex / Cursor / Windsurf
- [examples/](./examples/) — synthetic walkthroughs and minimal file trees
- [checklists/](./checklists/) — quick operational checklists
- [docs/](./docs/) — versioning, attribution, releases, public vs private docs and maintenance notes
- [scripts/](./scripts/) — lightweight repository checks for links, placeholders and required files

## Author

Created by Анатолий Малышев.

Website: [https://anmalishev.ru/](https://anmalishev.ru/)

Анатолий Малышев works with practical AI solutions for business: AI agents, CRM/1C/BI integrations, end-to-end analytics, Telegram bots and mini apps.

Geography: Saint Petersburg, Moscow and Russia.

## Who this is for

- solo founders;
- indie hackers;
- vibe coders;
- developers using Claude Code / Codex / Cursor / Windsurf;
- CTOs and teams adopting AI-assisted development;
- people who already have an AI-generated MVP and want to harden it.

## Optional automation

This repository includes lightweight GitHub Actions and local scripts for the toolkit itself:
- markdown and required file presence checks;
- local markdown link validation;
- placeholder scanning for secret-like examples.

These checks do not replace project hardening, security scanners, pentests or human review.

Content files in this repository are licensed under `CC BY 4.0`. Helper scripts inside [scripts/](./scripts/) are provided under `MIT` via [scripts/LICENSE-MIT](./scripts/LICENSE-MIT).

## Adoption and feedback

This is a new public toolkit. If you use it:
- star the repository;
- open an issue with feedback;
- share what AI IDE you used;
- suggest missing examples or playbooks.

No usage numbers are claimed yet.

## What this is not

- not a guarantee of security;
- not a replacement for human review;
- not a replacement for a pentest;
- not legal advice;
- not accounting advice;
- not a magic prompt that automatically makes any project production-ready.

## Russian overview

Этот репозиторий — markdown/toolkit-версия методологии `Vibe Coding Protocols` с сайта Анатолия Малышева.

Он помогает:
- запускать AI-проекты без хаоса;
- собирать Product Brief до генерации кода;
- задавать active / deferred surfaces;
- заводить `AGENTS.md`, `PROJECT_MAP.md` и `Architecture Source of Truth`;
- делать hardening AI-generated проекта перед merge / deploy / production;
- вести `AUDIT_BACKLOG.md` и безопаснее использовать AI IDE.

В будущем можно добавить `README.en.md` и `README.ru.md`, если репозиторию понадобится раздельная локализация.

## License

The repository is primarily published under `CC BY 4.0`.

If you adapt this toolkit, preserve attribution to the author and a link to the original repository or website.

Standalone executable scripts in [scripts/](./scripts/) are licensed separately under `MIT`.

Details: [LICENSE](./LICENSE)

## Disclaimer

Read [DISCLAIMER.md](./DISCLAIMER.md) before using the toolkit.
