# Vibe Coding Protocols — English entry point

**An operating layer for AI-assisted delivery — not just a prompt collection.**

Practical protocols, prompts, checklists and markdown templates for safer AI-assisted / vibe coding projects.

Vibe Coding Protocols helps founders, solo builders and teams turn AI-assisted coding into a controlled delivery workflow: Product Brief, Memory Bank, AI IDE rules, Starter, Hardening, vibe-check, security operations and audit backlog.

## Start in 2 minutes

### New project

1. Copy [AGENTS.md](./AGENTS.md) into your repo.
2. Copy [templates/PROJECT_MAP.md](./templates/PROJECT_MAP.md) as `PROJECT_MAP.md`.
3. Open [prompts/product-brief-prompt.md](./prompts/product-brief-prompt.md).
4. Paste the Product Brief prompt into your AI IDE.
5. Run:

```bash
bash scripts/vibe-check.sh --starter
```

### Existing AI-generated project

1. Copy [templates/AUDIT_BACKLOG.md](./templates/AUDIT_BACKLOG.md).
2. Open [protocols/ai-project-hardening-protocol.md](./protocols/ai-project-hardening-protocol.md).
3. Run:

```bash
bash scripts/vibe-check.sh --hardening
```

### Fastest setup

```bash
curl -fsSL https://raw.githubusercontent.com/Gudvin82/vibe-coding-protocols/main/scripts/init-minimal.sh | bash -s -- --starter
```

Safer alternative:

```bash
curl -fsSL https://raw.githubusercontent.com/Gudvin82/vibe-coding-protocols/main/scripts/init-minimal.sh -o init-minimal.sh
less init-minimal.sh
bash init-minimal.sh --starter
```

## 10-second overview

1. Start with a Product Brief and Starter Protocol.
2. Use AGENTS rules and Memory Bank files to keep scope under control.
3. Run Hardening before merge, deploy or production.
4. Reuse the templates, checklists, examples and vibe-check in your own repository.

## Why this exists

AI IDEs generate code quickly, but context, architecture, security, dependencies,
validation and ownership often stay in chat history instead of living in the project.

This toolkit adds an operating layer around AI-assisted development:
- Product Brief before code;
- Memory Bank files;
- Starter and Hardening paths;
- self-protection and perimeter checks;
- safe third-party intake;
- token-aware code discovery;
- validation and review gates.

## Core vs Extended

### Core path — for 80% of users

- Product Brief
- AGENTS.md
- PROJECT_MAP.md
- Starter Protocol
- Hardening Protocol
- AUDIT_BACKLOG.md
- vibe-check

### Extended path — for production / teams

- Architecture Source of Truth
- Security Operations Baseline
- Perimeter Security Checklist
- External Exposure Checklist
- Third-Party Registry
- Safe Update Workflow
- Secret Rotation and Storage
- Independent Diff Review

## Security layers covered

- Internal project security
- Perimeter and public exposure
- Supply-chain and integration review
- Architecture and documentation safety
- Token-aware AI workflow

See also:
- [checklists/perimeter-security-checklist.md](./checklists/perimeter-security-checklist.md)
- [templates/SECURITY_OPERATIONS_BASELINE.md](./templates/SECURITY_OPERATIONS_BASELINE.md)
- [docs/token-aware-code-discovery.md](./docs/token-aware-code-discovery.md)

## Artifact map

| Artifact | Purpose | Required? | Use when |
|---|---|---|---|
| Product Brief | Clarifies what to build before coding | Core | Any new project |
| AGENTS.md | Rules for AI agents | Core | Any AI IDE workflow |
| PROJECT_MAP.md | File map and code context | Core | Any repo with code |
| AUDIT_BACKLOG.md | Findings and follow-up tasks | Core for hardening | Existing AI-generated code |
| ARCHITECTURE_SOURCE_OF_TRUTH.md | Architecture reference | Extended | Production, team, handoff |
| SECURITY_OPERATIONS_BASELINE.md | Recurring security checks | Extended | Public/production projects |
| THIRD_PARTY_REGISTRY.md | External packages/APIs/repos | Extended | Any integrations |
| vibe-check.sh | Lightweight structure check | Optional but recommended | Local/CI sanity check |

## CI/CD integration

This repository includes a lightweight GitHub Action for `vibe-check`.

It runs on:
- `push`
- `pull_request`

It checks:
- toolkit structure;
- local links;
- placeholder / secrets-like examples;
- starter / hardening / audit mode signals.

It does not replace tests, scanners, pentests or human review.

See:
- [.github/workflows/vibe-check.yml](./.github/workflows/vibe-check.yml)
- [docs/automated-vibe-check.md](./docs/automated-vibe-check.md)

## Mermaid flow previews

Mermaid is kept in the main [README.md](./README.md).

Fallback previews:
- ![Workflow preview](./assets/workflow-mermaid-preview.png)
- ![Stop conditions flow preview](./assets/stop-conditions-flow-preview.png)

## Use with your AI IDE

- Claude Code: start with [CLAUDE.md](./CLAUDE.md)
- Codex: start with [AGENTS.md](./AGENTS.md)
- Cursor: start with [.cursorrules](./.cursorrules)
- Windsurf: start with [.windsurfrules](./.windsurfrules)
- GitHub Copilot / VS Code: use [.github/copilot-instructions.md](./.github/copilot-instructions.md)
- JetBrains / Junie / Antigravity: see [agents/](./agents/)

## Automated Vibe Check

`vibe-check` is a lightweight structure and safety check for projects using the toolkit.
It does not replace tests, scanners, human review or the full Hardening Protocol.

```bash
bash scripts/vibe-check.sh --starter
bash scripts/vibe-check.sh --hardening
bash scripts/vibe-check.sh --audit
bash scripts/init-minimal.sh --dry-run
```

![Automated Vibe Check example output](./assets/vibe-check-output.png)

See:
- [docs/automated-vibe-check.md](./docs/automated-vibe-check.md)
- [scripts/vibe-check.sh](./scripts/vibe-check.sh)
- [scripts/init-minimal.sh](./scripts/init-minimal.sh)

## Badges for your project

If you use the toolkit, you can add a badge to your project README:

[![Built with Vibe Coding Protocols](https://img.shields.io/badge/Built%20with-Vibe%20Coding%20Protocols-blue)](https://github.com/Gudvin82/vibe-coding-protocols)
[![Hardened with VCP](https://img.shields.io/badge/Hardened%20with-VCP-green)](https://github.com/Gudvin82/vibe-coding-protocols)
[![Uses VCP Templates](https://img.shields.io/badge/Uses-VCP%20Templates-purple)](https://github.com/Gudvin82/vibe-coding-protocols)

More badge options:
- [docs/badges.md](./docs/badges.md)

## Who should use this?

- Founders
- Solo builders
- Product teams
- Agencies and client teams

See the full onboarding in [README.md](./README.md).

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

## Official web version

- Hub: [https://anmalishev.ru/expert/vibe-coding/](https://anmalishev.ru/expert/vibe-coding/)
- Starter: [https://anmalishev.ru/expert/vibe-coding-starter.html](https://anmalishev.ru/expert/vibe-coding-starter.html)
- Hardening: [https://anmalishev.ru/expert/ai-project-hardening.html](https://anmalishev.ru/expert/ai-project-hardening.html)
- Templates: [https://anmalishev.ru/expert/templates/](https://anmalishev.ru/expert/templates/)
- Architecture Source of Truth: [https://anmalishev.ru/expert/templates/architecture-source-of-truth.html](https://anmalishev.ru/expert/templates/architecture-source-of-truth.html)
