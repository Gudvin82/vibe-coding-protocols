# Vibe Coding Protocols — English entry point

Practical protocols, prompts, checklists and markdown templates for safer AI-assisted / vibe coding projects.

## What this repository is

This is the GitHub toolkit packaging of the public Vibe Coding Protocols methodology.

It helps you:
- start AI-generated projects without chaos;
- create a Product Brief before coding;
- define active / deferred surfaces;
- create `AGENTS.md`, `PROJECT_MAP.md` and `Architecture Source of Truth`;
- audit AI-generated code before merge, deploy or production;
- check security, supply-chain, self-protection and database/load readiness;
- keep an audit backlog and safer AI workflow.

## Versions

- Repository version: `v0.1.1`
- Web methodology version: `Vibe Coding Protocols v1.4`

Repository versioning (`v0.x`) tracks the GitHub toolkit packaging.
Methodology versioning (`v1.x`) tracks the web protocols at
`anmalishev.ru`.

## 10-second overview

1. Start with a Product Brief and Starter Protocol.
2. Use AGENTS rules and Memory Bank files to keep scope under control.
3. Run Hardening before merge, deploy or production.
4. Reuse the templates, checklists and walkthrough examples in your own repository.

## Quick Start

### New project

1. Start with [prompts/product-brief-prompt.md](./prompts/product-brief-prompt.md)
2. Continue with [protocols/ai-project-starter-protocol.md](./protocols/ai-project-starter-protocol.md)
3. Use [templates/AGENTS.md](./templates/AGENTS.md) and
   [templates/PROJECT_MAP.md](./templates/PROJECT_MAP.md)

### Existing AI-generated code

1. Open [protocols/ai-project-hardening-protocol.md](./protocols/ai-project-hardening-protocol.md)
2. Start with Light Hardening
3. Create or update [templates/AUDIT_BACKLOG.md](./templates/AUDIT_BACKLOG.md)

### Give it to your AI IDE

- [CLAUDE.md](./CLAUDE.md)
- [AGENTS.md](./AGENTS.md)
- [.cursorrules](./.cursorrules)
- [.windsurfrules](./.windsurfrules)
- [.github/copilot-instructions.md](./.github/copilot-instructions.md)

## Official web version

- Hub: [https://anmalishev.ru/expert/vibe-coding/](https://anmalishev.ru/expert/vibe-coding/)
- Starter: [https://anmalishev.ru/expert/vibe-coding-starter.html](https://anmalishev.ru/expert/vibe-coding-starter.html)
- Hardening: [https://anmalishev.ru/expert/ai-project-hardening.html](https://anmalishev.ru/expert/ai-project-hardening.html)
- Templates: [https://anmalishev.ru/expert/templates/](https://anmalishev.ru/expert/templates/)
- Architecture Source of Truth:
  [https://anmalishev.ru/expert/templates/architecture-source-of-truth.html](https://anmalishev.ru/expert/templates/architecture-source-of-truth.html)

## Examples

- [examples/todo-app-vibe/](./examples/todo-app-vibe/)
- [examples/telegram-bot-vibe/](./examples/telegram-bot-vibe/)
- [examples/landing-page-vibe/](./examples/landing-page-vibe/)
- [examples/saas-backend-vibe/](./examples/saas-backend-vibe/)

All examples are synthetic and sanitized.

## Automated Vibe Check

`vibe-check` is a lightweight structure and safety check for projects
using the toolkit.

It does not replace tests, scanners, human review or the full
Hardening Protocol.

```bash
bash scripts/vibe-check.sh --starter
bash scripts/vibe-check.sh --hardening
bash scripts/vibe-check.sh --audit
```

Example output:

```text
PASS: README.md exists
PASS: AGENTS.md or CLAUDE.md exists
PASS: .gitignore exists
WARN: AUDIT_BACKLOG.md is missing for hardening mode
WARN: public root AGENTS.md exists; make sure public docs are sanitized
SUMMARY: 3 pass, 2 warn, 0 fail
```

![Automated Vibe Check example output](./assets/vibe-check-output.png)

See:
- [docs/automated-vibe-check.md](./docs/automated-vibe-check.md)
- [scripts/vibe-check.sh](./scripts/vibe-check.sh)

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

## More guides

- [ANTI_PATTERNS.md](./ANTI_PATTERNS.md)
- [docs/multi-agent-workflows.md](./docs/multi-agent-workflows.md)
- [docs/vibe-metrics.md](./docs/vibe-metrics.md)
- [docs/automated-vibe-check.md](./docs/automated-vibe-check.md)
- [docs/pre-commit-hooks.md](./docs/pre-commit-hooks.md)
- [docs/community-issues.md](./docs/community-issues.md)
- [ROADMAP.md](./ROADMAP.md)

## Author

Created by **Anatoly Malyshev**.

Website: [https://anmalishev.ru/](https://anmalishev.ru/)

Anatoly Malyshev is an AI solutions and automation practitioner
focused on practical AI agents, CRM/1C/BI integrations, analytics
workflows, Telegram bots, mini apps and AI-assisted project
hardening.

This toolkit grew out of hands-on work with AI-generated projects:
turning vague ideas into Product Briefs, keeping AI coding sessions
scoped, documenting architecture, auditing generated code, and
preparing projects for safer merge/deploy decisions.

The goal is practical: help founders, indie hackers, developers and
teams use AI IDEs without losing architecture, security context or
delivery control.

Based in Saint Petersburg, working with clients and projects across
Russia and remote-first teams.
