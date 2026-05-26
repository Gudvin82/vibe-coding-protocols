# Vibe Coding Protocols

[![Repo Version](https://img.shields.io/badge/repo-v0.1.2-blue)](./CHANGELOG.md)
[![Methodology](https://img.shields.io/badge/methodology-v1.4-purple)](https://anmalishev.ru/expert/vibe-coding/)
[![License](https://img.shields.io/badge/license-CC%20BY%204.0-green)](./LICENSE)
[![Updated](https://img.shields.io/badge/updated-May%202026-brightgreen)](./CHANGELOG.md)
[![Website](https://img.shields.io/badge/website-anmalishev.ru-black)](https://anmalishev.ru/)
[![Toolkit](https://img.shields.io/badge/type-markdown%20toolkit-informational)](https://github.com/Gudvin82/vibe-coding-protocols)
[![Claude Code Ready](https://img.shields.io/badge/Claude%20Code-ready-blueviolet)](./CLAUDE.md)
[![Codex Ready](https://img.shields.io/badge/Codex-ready-blue)](./AGENTS.md)
[![Cursor Ready](https://img.shields.io/badge/Cursor-ready-black)](./.cursorrules)
[![Windsurf Ready](https://img.shields.io/badge/Windsurf-ready-00A3FF)](./.windsurfrules)
[![Copilot Ready](https://img.shields.io/badge/GitHub%20Copilot-ready-2ea44f)](./.github/copilot-instructions.md)
[![Toolkit Smoke](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/toolkit-smoke.yml/badge.svg)](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/toolkit-smoke.yml)
[![Link Check](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/link-check.yml/badge.svg)](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/link-check.yml)
[![Vibe Check](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml/badge.svg)](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml)

**Practical protocols, prompts, checklists and markdown templates for safer AI-assisted / vibe coding projects.**

Languages:
- English: [README_en.md](./README_en.md)
- Русский: [README_ru.md](./README_ru.md)

## 10-second overview

1. **Start** — turn an idea into a Product Brief and first safe vertical slice.
2. **Build** — use `AGENTS.md`, `PROJECT_MAP.md` and AI IDE rules to keep scope controlled.
3. **Harden** — audit AI-generated code before merge, deploy or production.
4. **Reuse** — copy markdown templates, prompts and checklists into your project.

## Why this exists

AI IDEs can generate code quickly, but projects often fail because context,
architecture, security, dependencies, tests, deployment and ownership are not controlled.

Vibe Coding Protocols adds an operating layer around AI-assisted development:
- Product Brief before code;
- active / deferred surfaces;
- Memory Bank files;
- AI IDE rules;
- Starter workflow;
- Hardening workflow;
- audit backlog;
- self-protection and perimeter checks;
- safe third-party intake;
- token-aware code discovery;
- validation and review gates.

## What problem does it solve?

Common AI-generated project problems:
- AI starts coding before the product is clear;
- generated code spreads across too many files;
- dependencies are added without review;
- architecture exists only in chat history;
- security checks happen too late;
- secrets, logs or internal docs become public;
- external APIs, repos and packages are trusted too quickly;
- the project cannot scale after the first users;
- AI burns tokens reading the whole repository;
- nobody knows whether the project is ready for merge or deploy.

This toolkit turns those risks into checklists, prompts, templates and lightweight automation.

## Quick start

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

## What should I copy first?

- New project:
  `prompts/product-brief-prompt.md` +
  `protocols/ai-project-starter-protocol.md`
- Existing AI-generated project:
  `protocols/ai-project-hardening-protocol.md` +
  `templates/AUDIT_BACKLOG.md`
- AI IDE setup:
  `AGENTS.md`, `CLAUDE.md`, `.cursorrules`,
  `.windsurfrules`, `.github/copilot-instructions.md`
- Architecture docs:
  `templates/ARCHITECTURE_SOURCE_OF_TRUTH.md`
- Security operations:
  `templates/SECURITY_OPERATIONS_BASELINE.md` +
  `checklists/perimeter-security-checklist.md`
- Safe integrations:
  `templates/THIRD_PARTY_REGISTRY.md` +
  `docs/safe-update-workflow.md`

## When to use which path?

| Situation | Start here |
|---|---|
| I only have an idea | [Product Brief prompt](./prompts/product-brief-prompt.md) |
| I want to start a new AI project | [Starter Protocol](./protocols/ai-project-starter-protocol.md) |
| I already have AI-generated code | [Hardening Protocol](./protocols/ai-project-hardening-protocol.md) |
| I want reusable files | [Templates](./templates/README.md) |
| I need project documentation | [Architecture Source of Truth](./templates/ARCHITECTURE_SOURCE_OF_TRUTH.md) |
| I want quick structure check | [Automated Vibe Check](./docs/automated-vibe-check.md) |
| I want examples | [examples/README.md](./examples/README.md) |

## Use with your AI IDE

### Claude Code
Copy [CLAUDE.md](./CLAUDE.md) or
[agents/CLAUDE.md.example](./agents/CLAUDE.md.example) into your project and start with
[prompts/master-prompt-short.md](./prompts/master-prompt-short.md).

### Codex
Use [AGENTS.md](./AGENTS.md) plus the relevant protocol and prompt files.
If external links are unavailable, paste the needed markdown files directly into the task.

### Cursor
Use the protocols as planning documents, copy [.cursorrules](./.cursorrules) or
[agents/CURSOR.md.example](./agents/CURSOR.md.example), and apply Stop Conditions
before larger Composer edits.

### Windsurf
Use [.windsurfrules](./.windsurfrules) or
[agents/WINDSURF.md.example](./agents/WINDSURF.md.example) as a Cascade scope guard:
active surfaces, deferred surfaces, approval gates and validation.

### GitHub Copilot / VS Code
Place [.github/copilot-instructions.md](./.github/copilot-instructions.md)
in your project, combine it with [AGENTS.md](./AGENTS.md), and use
[scripts/init-project.example.sh](./scripts/init-project.example.sh)
as a review-first helper.

### JetBrains / Junie / Antigravity
Use the examples in [agents/](./agents/) to adapt the workflow for
small diffs, stop conditions, Memory Bank updates and approval gates.

## Automated Vibe Check

`vibe-check` is a lightweight structure and safety check for projects using the toolkit.

It does not replace tests, scanners, human review or the full Hardening Protocol.
It helps you catch missing project memory, missing audit files and obvious workflow gaps early.

```bash
bash scripts/vibe-check.sh --starter
bash scripts/vibe-check.sh --hardening
bash scripts/vibe-check.sh --audit
```

Example output:

```text
PASS: README.md present
PASS: .gitignore present
PASS: AI instructions file present
WARN: AUDIT_BACKLOG.md is missing for hardening mode
WARN: public root AGENTS.md exists; make sure public docs are sanitized
SUMMARY: PASS=3 WARN=2 FAIL=0
```

![Automated Vibe Check example output](./assets/vibe-check-output.png)

See:
- [docs/automated-vibe-check.md](./docs/automated-vibe-check.md)
- [scripts/vibe-check.sh](./scripts/vibe-check.sh)

## Repository map

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
│   ├── ARCHITECTURE_SOURCE_OF_TRUTH.md     # Architecture reference template
│   ├── THIRD_PARTY_REGISTRY.md             # Safe integration registry
│   └── SECURITY_OPERATIONS_BASELINE.md     # Recurring security hygiene baseline
├── checklists/
│   ├── starter-checklist.md
│   ├── hardening-checklist.md
│   ├── self-protection-checklist.md
│   ├── perimeter-security-checklist.md
│   ├── external-exposure-checklist.md
│   ├── safe-integration-checklist.md
│   ├── database-load-scalability-checklist.md
│   ├── ai-generated-migrations-rollback.md
│   ├── ai-generated-test-strategy.md
│   └── device-browser-qa-checklist.md
├── examples/
│   ├── todo-app-vibe/
│   ├── telegram-bot-vibe/
│   ├── landing-page-vibe/
│   └── saas-backend-vibe/
├── docs/
│   ├── automated-vibe-check.md
│   ├── security-operations.md
│   ├── safe-update-workflow.md
│   ├── token-aware-code-discovery.md
│   └── secret-rotation-and-storage.md
├── scripts/
├── .github/
├── ANTI_PATTERNS.md
└── ROADMAP.md
```

## Examples

Start with [examples/README.md](./examples/README.md).

Recommended walkthroughs:
- [examples/todo-app-vibe/](./examples/todo-app-vibe/) — Starter to Hardening for a small app
- [examples/telegram-bot-vibe/](./examples/telegram-bot-vibe/) — bot-specific abuse and hardening findings
- [examples/landing-page-vibe/](./examples/landing-page-vibe/) — light route for a public landing page
- [examples/saas-backend-vibe/](./examples/saas-backend-vibe/) — backend-heavy audit with scanners, migrations and rate limits

All examples are synthetic / sanitized. They are walkthroughs, not production templates.

## Security layers covered

This toolkit is not a security product, but it helps you structure security work across several layers:

1. **Internal project security**
   Secrets, environment files, logs, backups, admin routes, workers, browser automation and private docs.

2. **Perimeter and exposure**
   Public endpoints, closed ports, admin allowlists, WAF/CDN, rate limits, bot abuse,
   security headers and recurring exposure checks.

3. **Supply-chain and integrations**
   External APIs, packages, repositories, templates, GitHub Actions, Docker images and update workflows.

4. **Architecture and documentation safety**
   `PROJECT_MAP.md`, `AGENTS.md` and Architecture Source of Truth, with
   private / sanitized / encrypted storage policy.

5. **Token-aware AI workflow**
   Memory Bank, read order, scoped code discovery and independent diff review.

## New in security operations

- [Perimeter Security Checklist](./checklists/perimeter-security-checklist.md)
- [External Exposure Checklist](./checklists/external-exposure-checklist.md)
- [Security Operations Baseline](./templates/SECURITY_OPERATIONS_BASELINE.md)
- [Secret Rotation and Storage](./docs/secret-rotation-and-storage.md)
- [Safe Update Workflow](./docs/safe-update-workflow.md)
- [Token-Aware Code Discovery](./docs/token-aware-code-discovery.md)

## Workflow

```mermaid
flowchart TD
    A[Idea] --> B[Product Brief]
    B --> C[Starter Protocol]
    C --> D[First safe vertical slice]
    D --> E{Existing code ready?}
    E -->|No| C
    E -->|Yes| F[Light Hardening]
    F --> G[Audit Backlog]
    G --> H[Fixes and validation]
    H --> I[Independent diff review]
    I --> J{Ready?}
    J -->|No| G
    J -->|Yes| K[Merge / staging / deploy]
```

## Stop conditions flow

```mermaid
flowchart TD
    A[AI proposes change] --> B{Touches risky area?}
    B -->|Auth / payments / DB / deps / more than 10 files| C[Stop and ask approval]
    B -->|Small safe change| D[Implement smallest practical diff]
    D --> E[Run validation]
    E --> F{Validation green?}
    F -->|No| G[Fix or rollback]
    F -->|Yes| H[Report changed files and next steps]
```

## Badges for your project

If you use the toolkit, you can add a badge to your project README:

[![Built with Vibe Coding Protocols](https://img.shields.io/badge/Built%20with-Vibe%20Coding%20Protocols-blue)](https://github.com/Gudvin82/vibe-coding-protocols)
[![Hardened with VCP](https://img.shields.io/badge/Hardened%20with-VCP-green)](https://github.com/Gudvin82/vibe-coding-protocols)
[![Uses VCP Templates](https://img.shields.io/badge/Uses-VCP%20Templates-purple)](https://github.com/Gudvin82/vibe-coding-protocols)

```markdown
[![Built with Vibe Coding Protocols](https://img.shields.io/badge/Built%20with-Vibe%20Coding%20Protocols-blue)](https://github.com/Gudvin82/vibe-coding-protocols)
```

```markdown
[![Hardened with VCP](https://img.shields.io/badge/Hardened%20with-VCP-green)](https://github.com/Gudvin82/vibe-coding-protocols)
[![Uses VCP Templates](https://img.shields.io/badge/Uses-VCP%20Templates-purple)](https://github.com/Gudvin82/vibe-coding-protocols)
```

More badge options:
- [docs/badges.md](./docs/badges.md)

## What this is not

- not a guarantee of security;
- not a replacement for human review;
- not a replacement for a pentest;
- not legal advice;
- not accounting advice;
- not a DDoS protection product;
- not a magic prompt that automatically makes any project production-ready.

## Author

Created by **Anatoly Malyshev**.

Website: [https://anmalishev.ru/](https://anmalishev.ru/)

Anatoly Malyshev is an AI solutions and automation practitioner focused on practical AI agents,
CRM/1C/BI integrations, analytics workflows, Telegram bots, mini apps and AI-assisted project hardening.

This toolkit grew out of hands-on work with AI-generated projects: turning vague ideas into Product Briefs,
keeping AI coding sessions scoped, documenting architecture, auditing generated code, and preparing projects for safer merge/deploy decisions.

The goal is practical: help founders, indie hackers, developers and teams use AI IDEs without losing architecture,
security context or delivery control.

Based in Saint Petersburg, working with clients and projects across Russia and remote-first teams.

## Links, website and languages

- Hub: [https://anmalishev.ru/expert/vibe-coding/](https://anmalishev.ru/expert/vibe-coding/)
- Starter: [https://anmalishev.ru/expert/vibe-coding-starter.html](https://anmalishev.ru/expert/vibe-coding-starter.html)
- Hardening: [https://anmalishev.ru/expert/ai-project-hardening.html](https://anmalishev.ru/expert/ai-project-hardening.html)
- Templates: [https://anmalishev.ru/expert/templates/](https://anmalishev.ru/expert/templates/)
- Architecture Source of Truth: [https://anmalishev.ru/expert/templates/architecture-source-of-truth.html](https://anmalishev.ru/expert/templates/architecture-source-of-truth.html)
- English: [README_en.md](./README_en.md)
- Русский: [README_ru.md](./README_ru.md)

## Repository and methodology versions

- Repository version: `v0.1.2`
- Web methodology version: `Vibe Coding Protocols v1.4`
- This repository is a markdown/toolkit packaging of the public web methodology from `anmalishev.ru`.

Repository versioning (`v0.x`) tracks the GitHub toolkit packaging.  
Methodology versioning (`v1.x`) tracks the web protocols at `anmalishev.ru`.

## Disclaimer

Read [DISCLAIMER.md](./DISCLAIMER.md) before using the toolkit.

## License

The repository is primarily published under `CC BY 4.0`.

If you adapt this toolkit, preserve attribution to the author and a link to the original repository or website.

Standalone executable scripts in [scripts/](./scripts/) are licensed separately under `MIT`.
