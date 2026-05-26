# Vibe Coding Protocols — English entry point

Practical protocols, prompts, checklists and markdown templates for safer AI-assisted / vibe coding projects.

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

## What should I copy first?

- New project:
  [prompts/product-brief-prompt.md](./prompts/product-brief-prompt.md) +
  [protocols/ai-project-starter-protocol.md](./protocols/ai-project-starter-protocol.md)
- Existing AI-generated project:
  [protocols/ai-project-hardening-protocol.md](./protocols/ai-project-hardening-protocol.md) +
  [templates/AUDIT_BACKLOG.md](./templates/AUDIT_BACKLOG.md)
- AI IDE setup:
  [AGENTS.md](./AGENTS.md), [CLAUDE.md](./CLAUDE.md), [.cursorrules](./.cursorrules),
  [.windsurfrules](./.windsurfrules), [.github/copilot-instructions.md](./.github/copilot-instructions.md)
- Perimeter / operations:
  [checklists/perimeter-security-checklist.md](./checklists/perimeter-security-checklist.md) +
  [templates/SECURITY_OPERATIONS_BASELINE.md](./templates/SECURITY_OPERATIONS_BASELINE.md)

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
```

![Automated Vibe Check example output](./assets/vibe-check-output.png)

See:
- [docs/automated-vibe-check.md](./docs/automated-vibe-check.md)
- [scripts/vibe-check.sh](./scripts/vibe-check.sh)

## Examples

- [examples/todo-app-vibe/](./examples/todo-app-vibe/)
- [examples/telegram-bot-vibe/](./examples/telegram-bot-vibe/)
- [examples/landing-page-vibe/](./examples/landing-page-vibe/)
- [examples/saas-backend-vibe/](./examples/saas-backend-vibe/)

All examples are synthetic and sanitized.

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
