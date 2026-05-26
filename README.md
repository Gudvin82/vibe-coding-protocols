# Vibe Coding Protocols

[![Repo Version](https://img.shields.io/badge/repo-v0.1.0-blue)](./CHANGELOG.md)
[![Methodology](https://img.shields.io/badge/methodology-v1.4-purple)](https://anmalishev.ru/expert/vibe-coding/)
[![License](https://img.shields.io/badge/license-CC%20BY%204.0-green)](./LICENSE)
[![Updated](https://img.shields.io/badge/updated-May%202026-brightgreen)](./CHANGELOG.md)
[![Website](https://img.shields.io/badge/website-anmalishev.ru-black)](https://anmalishev.ru/)
[![Toolkit](https://img.shields.io/badge/type-markdown%20toolkit-informational)](https://github.com/Gudvin82/vibe-coding-protocols)
[![Toolkit Smoke](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/toolkit-smoke.yml/badge.svg)](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/toolkit-smoke.yml)
[![Link Check](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/link-check.yml/badge.svg)](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/link-check.yml)

**Practical protocols, prompts, checklists and markdown templates for safer AI-assisted / vibe coding projects.**

Languages:
- English: [README_en.md](./README_en.md)
- Русский: [README_ru.md](./README_ru.md)

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

## Use with your AI IDE

### Claude Code
Copy [CLAUDE.md](./CLAUDE.md) or [agents/CLAUDE.md.example](./agents/CLAUDE.md.example) into your project and start with [prompts/master-prompt-short.md](./prompts/master-prompt-short.md).

### Codex
Use [AGENTS.md](./AGENTS.md) plus the relevant protocol and prompt files. If external links are unavailable, paste the needed markdown files directly into the task.

### Cursor
Use the protocols as planning documents, copy [.cursorrules](./.cursorrules) or [agents/CURSOR.md.example](./agents/CURSOR.md.example), and apply Stop Conditions before larger Composer edits.

### Windsurf
Use [.windsurfrules](./.windsurfrules) or [agents/WINDSURF.md.example](./agents/WINDSURF.md.example) as a Cascade scope guard: active surfaces, deferred surfaces, approval gates and validation.

### GitHub Copilot / VS Code
Place [.github/copilot-instructions.md](./.github/copilot-instructions.md) in your project, combine it with [AGENTS.md](./AGENTS.md), and use [scripts/init-project.example.sh](./scripts/init-project.example.sh) as a review-first helper.

### JetBrains / Junie / Antigravity
Use the examples in [agents/](./agents/) to adapt the workflow for small diffs, stop conditions, Memory Bank updates and approval gates.

## Repository and methodology versions

- Repository version: `v0.1.0`
- Web methodology version: `Vibe Coding Protocols v1.4`
- This repository is a markdown/toolkit packaging of the public web methodology from `anmalishev.ru`.

Repository versioning (`v0.x`) tracks the GitHub toolkit packaging.  
Methodology versioning (`v1.x`) tracks the web protocols at `anmalishev.ru`.

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
│   ├── CLAUDE.md.example                   # Claude Code adaptation
│   ├── CODEX.md.example                    # Codex adaptation
│   ├── CURSOR.md.example                   # Cursor adaptation
│   ├── JETBRAINS.md.example                # JetBrains / Junie adaptation
│   └── VS_CODE.md.example                  # VS Code guidance
├── examples/
│   ├── todo-app-vibe/                      # Starter to Hardening walkthrough
│   ├── telegram-bot-vibe/                  # Bot hardening walkthrough
│   ├── landing-page-vibe/                  # Light hardening walkthrough
│   └── saas-backend-vibe/                  # Full hardening walkthrough
├── checklists/                             # Quick operational checklists
├── docs/                                   # Attribution, badges, roadmap, community, notes
├── scripts/                                # Lightweight helper checks and init example
├── .github/                                # Copilot instructions, issues, workflows
└── ROADMAP.md                              # Practical near-term direction
```

## Official website links

- Hub: [https://anmalishev.ru/expert/vibe-coding/](https://anmalishev.ru/expert/vibe-coding/)
- Starter: [https://anmalishev.ru/expert/vibe-coding-starter.html](https://anmalishev.ru/expert/vibe-coding-starter.html)
- Hardening: [https://anmalishev.ru/expert/ai-project-hardening.html](https://anmalishev.ru/expert/ai-project-hardening.html)
- Templates: [https://anmalishev.ru/expert/templates/](https://anmalishev.ru/expert/templates/)
- Architecture Source of Truth: [https://anmalishev.ru/expert/templates/architecture-source-of-truth.html](https://anmalishev.ru/expert/templates/architecture-source-of-truth.html)

## Walkthrough examples

Start with [examples/README.md](./examples/README.md).

Recommended walkthroughs:
- [examples/todo-app-vibe/](./examples/todo-app-vibe/) — full Starter-to-Hardening path for a small app
- [examples/telegram-bot-vibe/](./examples/telegram-bot-vibe/) — bot-specific hardening findings
- [examples/landing-page-vibe/](./examples/landing-page-vibe/) — light route for a public landing page
- [examples/saas-backend-vibe/](./examples/saas-backend-vibe/) — backend-heavy audit with migrations and scanners

All examples are synthetic / sanitized. They are walkthroughs, not production templates.

## Optional automation

This repository includes lightweight GitHub Actions and local scripts for the toolkit itself:
- markdown and required file presence checks;
- local markdown link validation;
- placeholder scanning for secret-like examples;
- a review-first init script example.

These checks do not replace project hardening, security scanners, pentests or human review.

Content files in this repository are licensed under `CC BY 4.0`. Helper scripts inside [scripts/](./scripts/) are provided under `MIT` via [scripts/LICENSE-MIT](./scripts/LICENSE-MIT).

## Community and adoption

This is a new public toolkit. No usage numbers are claimed yet.

If you use it:
- star the repository;
- open an issue using [Protocol Feedback](./.github/ISSUE_TEMPLATE/protocol_feedback.yml);
- request a walkthrough with [Example request](./.github/ISSUE_TEMPLATE/example_request.yml);
- suggest an AI IDE adaptation or wording improvement.

Helpful docs:
- [ROADMAP.md](./ROADMAP.md)
- [docs/badges.md](./docs/badges.md)
- [docs/community.md](./docs/community.md)
- [docs/awesome-vibe-coding-pr.md](./docs/awesome-vibe-coding-pr.md)
- [docs/vscode-extension-idea.md](./docs/vscode-extension-idea.md)
- [docs/social-preview.md](./docs/social-preview.md)

## Author

Created by Анатолий Малышев.

Website: [https://anmalishev.ru/](https://anmalishev.ru/)

Анатолий Малышев works with practical AI solutions for business: AI agents, CRM/1C/BI integrations, end-to-end analytics, Telegram bots and mini apps.

Geography: Saint Petersburg, Moscow and Russia.

## What this is not

- not a guarantee of security;
- not a replacement for human review;
- not a replacement for a pentest;
- not legal advice;
- not accounting advice;
- not a magic prompt that automatically makes any project production-ready.

## Russian overview

This repository also has a Russian entry point: [README_ru.md](./README_ru.md).

В будущем можно отдельно развивать `README_en.md` и `README_ru.md`, если репозиторию понадобится более глубокая локализация.

## License

The repository is primarily published under `CC BY 4.0`.

If you adapt this toolkit, preserve attribution to the author and a link to the original repository or website.

Standalone executable scripts in [scripts/](./scripts/) are licensed separately under `MIT`.

Details: [LICENSE](./LICENSE)

## Disclaimer

Read [DISCLAIMER.md](./DISCLAIMER.md) before using the toolkit.
