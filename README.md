# Vibe Coding Protocols

### Project status

[![Repo Version](https://img.shields.io/badge/repo-v0.1.9-blue)](./CHANGELOG.md)
[![Methodology](https://img.shields.io/badge/methodology-v1.4-purple)](https://anmalishev.ru/expert/vibe-coding/)
[![License](https://img.shields.io/badge/license-CC%20BY%204.0-green)](./LICENSE)
[![Updated](https://img.shields.io/badge/updated-May%202026-brightgreen)](./CHANGELOG.md)
[![Website](https://img.shields.io/badge/website-anmalishev.ru-black)](https://anmalishev.ru/)
[![Toolkit](https://img.shields.io/badge/type-markdown%20toolkit-informational)](https://github.com/Gudvin82/vibe-coding-protocols)

### AI IDE ready

[![Claude Code Ready](https://img.shields.io/badge/Claude%20Code-ready-blueviolet)](./CLAUDE.md)
[![Codex Ready](https://img.shields.io/badge/Codex-ready-blue)](./AGENTS.md)
[![Cursor Ready](https://img.shields.io/badge/Cursor-ready-black)](./.cursorrules)
[![Windsurf Ready](https://img.shields.io/badge/Windsurf-ready-00A3FF)](./.windsurfrules)
[![Copilot Ready](https://img.shields.io/badge/GitHub%20Copilot-ready-2ea44f)](./.github/copilot-instructions.md)

### CI

[![Toolkit Smoke](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/toolkit-smoke.yml/badge.svg)](
  https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/toolkit-smoke.yml
)
[![Link Check](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/link-check.yml/badge.svg)](
  https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/link-check.yml
)
[![Vibe Check](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml/badge.svg)](
  https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml
)

**An agent harness and operating layer for AI-assisted delivery — not just a prompt collection.**

Vibe Coding Protocols helps founders, solo builders and teams turn
AI-assisted coding into a more controlled workflow: Product Brief,
Memory Bank, AI IDE rules, Starter, Hardening, vibe-check, security
baselines, model routing and audit backlog.

Repository package: `v0.1.9`  
Web methodology: `Vibe Coding Protocols v1.4`

Languages:
- English: [README_en.md](./README_en.md)
- Русский: [README_ru.md](./README_ru.md)

## What this is

This repository is a lightweight GitHub toolkit for AI-assisted delivery.

It gives you:
- route selection before coding;
- copy-ready AI IDE rules and Memory Bank files;
- starter and hardening workflows;
- a lightweight `vibe-check` for readiness signals;
- agent harness and model routing guidance;
- synthetic examples and reusable command patterns.

Not sure where to start? Open [START_HERE.md](./START_HERE.md).

## Versioning

This project uses two version lines:

- Repository package `v0.1.x` — GitHub toolkit packaging, scripts, examples, CI and docs.
- Web methodology `v1.4` — public methodology pages on `anmalishev.ru`.

They are related but not identical. The repository may move to `v1.0.0`
after external feedback and stable toolkit adoption.

## Start here

| Situation | Start here |
|---|---|
| Only an idea | [English Product Brief prompt](./prompts/product-brief-prompt_en.md) |
| New project | [Starter Protocol](./protocols/ai-project-starter-protocol.md) |
| Existing AI-generated code | [Hardening Protocol](./protocols/ai-project-hardening-protocol.md) |
| Public / production | [Extended path](#core-vs-extended) |
| AI IDE setup | [AGENTS / CLAUDE / Cursor rules](#repository-map) |

## Start in 2 minutes

### New project

1. Copy `templates/AGENTS.md` into your repo.
2. Copy `templates/PROJECT_MAP.md`.
3. Open one Product Brief prompt:
   - [English Product Brief prompt](./prompts/product-brief-prompt_en.md)
   - [Russian Product Brief prompt](./prompts/product-brief-prompt.md)
4. Paste the prompt into your AI IDE.
5. Run:

```bash
bash scripts/vibe-check.sh --starter
```

### Existing AI-generated project

1. Copy `templates/AUDIT_BACKLOG.md`.
2. Open [Hardening Protocol](./protocols/ai-project-hardening-protocol.md).
3. Run:

```bash
bash scripts/vibe-check.sh --hardening
```

### Review-first minimal setup

```bash
curl -fsSL https://raw.githubusercontent.com/Gudvin82/vibe-coding-protocols/main/scripts/init-minimal.sh -o init-minimal.sh
less init-minimal.sh
bash init-minimal.sh --starter
```

Fast track is for empty or test repositories. For real projects, review the script first.

```bash
curl -fsSL https://raw.githubusercontent.com/Gudvin82/vibe-coding-protocols/main/scripts/init-minimal.sh | bash -s -- --starter
```

Optional local guardrail:

```bash
bash scripts/install-hooks.sh --mode starter
```

Default behavior:
- installs a pre-commit hook in `starter` mode;
- reminds you to use `--mode hardening` or `--mode audit` for existing or
  production-bound projects.

## Core vs Extended

### Core path

Use Core when the project is still private, local, early-stage or MVP-bound.

Core artifacts:
- Product Brief
- `templates/AGENTS.md`
- `templates/PROJECT_MAP.md`
- Starter Protocol
- Hardening Protocol
- `templates/AUDIT_BACKLOG.md`
- `vibe-check`

### Extended path

Use Extended when the project is public, monetized, client-facing or production-bound.

Extended artifacts:
- `templates/ARCHITECTURE_SOURCE_OF_TRUTH.md`
- `templates/SECURITY_OPERATIONS_BASELINE.md`
- `templates/THIRD_PARTY_REGISTRY.md`
- [perimeter checklist](./checklists/perimeter-security-checklist.md)
- [auth abuse checklist](./checklists/auth-abuse-checklist.md)
- [hardening thresholds](./docs/hardening-thresholds.md)
- [incident recovery runbook](./templates/INCIDENT_RECOVERY_RUNBOOK.md)

## Vibe-check

`vibe-check` is a lightweight readiness check.

It helps confirm:
- project memory and baseline files;
- `.gitignore` and env hygiene;
- obvious secret-like patterns;
- starter / hardening / audit route coverage;
- optional scanner integration when tools are already installed.

It is not a security scanner and not a security certification.

```bash
bash scripts/vibe-check.sh --help
bash scripts/vibe-check.sh --starter
bash scripts/vibe-check.sh --hardening
bash scripts/vibe-check.sh --audit
bash scripts/vibe-check.sh --audit --json
bash scripts/vibe-check.sh --audit --scanners || true
```

See:
- [docs/automated-vibe-check.md](./docs/automated-vibe-check.md)
- [docs/scanner-integration.md](./docs/scanner-integration.md)
- [docs/hardening-thresholds.md](./docs/hardening-thresholds.md)

## Agent harness and model routing

This repository treats AI-assisted delivery as an agent harness problem:
- stable memory before edits;
- scoped discovery instead of whole-repo scanning;
- model routing when available;
- validation before confidence;
- backlog and release handoff after changes.

Start with:
- [docs/agent-harness.md](./docs/agent-harness.md)
- [docs/model-routing.md](./docs/model-routing.md)
- [docs/auth-session-security.md](./docs/auth-session-security.md)
- [commands/README.md](./commands/README.md)

## Repository map

```text
vibe-coding-protocols/
├── START_HERE.md
├── protocols/                # Starter and Hardening routes
├── prompts/                  # Product Brief, AI entry, modular prompts
├── templates/                # Copy-ready project artifacts
├── checklists/               # Security, QA and rollout checklists
├── commands/                 # Reusable AI command patterns
├── docs/                     # Guides, reference and releases
├── examples/                 # Synthetic starter and hardening walkthroughs
├── scripts/                  # vibe-check, installers, hooks
└── case-studies/             # Template-only for now
```

Root `AGENTS.md` configures this repository.

## Which agent file should I copy?

- Root `AGENTS.md` configures this repository.
- Root `CLAUDE.md` configures Claude Code for this repository.
- Use `templates/AGENTS.md` as the generic copy-ready agent template for your project.
- Use `templates/AGENTS.claude.md` if you want Claude Code-specific rules.
- Use `templates/AGENTS.cursor.md` or `templates/AGENTS.windsurf.md` for Cursor or Windsurf-specific workflows.

Core memory files used across this toolkit:
- `README.md`
- `AGENTS.md` or `CLAUDE.md`
- `PROJECT_MAP.md`
- `ARCHITECTURE_SOURCE_OF_TRUTH.md`, if needed
- `AUDIT_BACKLOG.md`, for hardening
- `docs/PROMPTS.md` or `PROMPTS.md`, if prompts are tracked
- `SECURITY.md` or `SECURITY_BASELINE.md`, for public or production projects

If you want to copy agent rules into your own project, use:
- [templates/AGENTS.md](./templates/AGENTS.md)
- [templates/AGENTS.claude.md](./templates/AGENTS.claude.md)
- [templates/AGENTS.cursor.md](./templates/AGENTS.cursor.md)
- [templates/AGENTS.windsurf.md](./templates/AGENTS.windsurf.md)

## Examples

Start with [examples/README.md](./examples/README.md).

Recommended examples:
- [examples/todo-app-starter/](./examples/todo-app-starter/) — runnable synthetic starter project
- [examples/todo-app-vibe/](./examples/todo-app-vibe/) — starter to hardening walkthrough
- [examples/telegram-bot-vibe/](./examples/telegram-bot-vibe/) — bot token and abuse risks
- [examples/landing-page-vibe/](./examples/landing-page-vibe/) — public site route
- [examples/saas-backend-vibe/](./examples/saas-backend-vibe/) — backend-heavy hardening path

Examples are synthetic or sanitized learning examples. They are not claimed as
real-world case studies.

Case studies are template-only for now:
- [case-studies/README.md](./case-studies/README.md)

## Docs

Start here when you need more depth:
- [START_HERE.md](./START_HERE.md)
- [docs/agent-harness.md](./docs/agent-harness.md)
- [docs/model-routing.md](./docs/model-routing.md)
- [docs/auth-session-security.md](./docs/auth-session-security.md)
- [docs/hardening-thresholds.md](./docs/hardening-thresholds.md)
- [docs/scanner-integration.md](./docs/scanner-integration.md)
- [docs/metrics-to-track.md](./docs/metrics-to-track.md)
- [templates/INCIDENT_RECOVERY_RUNBOOK.md](./templates/INCIDENT_RECOVERY_RUNBOOK.md)
- [templates/README.md](./templates/README.md)
- [ANTI_PATTERNS.md](./ANTI_PATTERNS.md)

## Author

Created by **Anatoly Malyshev**.

Website: [https://anmalishev.ru/](https://anmalishev.ru/)

Hub:
- [https://anmalishev.ru/expert/vibe-coding/](https://anmalishev.ru/expert/vibe-coding/)
- [https://anmalishev.ru/expert/vibe-coding-starter.html](https://anmalishev.ru/expert/vibe-coding-starter.html)
- [https://anmalishev.ru/expert/ai-project-hardening.html](https://anmalishev.ru/expert/ai-project-hardening.html)

## License

The repository is primarily published under `CC BY 4.0`.

Standalone executable scripts in [scripts/](./scripts/) are licensed separately under `MIT`.

## Distribution notes

Suggested GitHub topics for manual setup:
- `vibe-coding`
- `ai-coding`
- `ai-assisted-development`
- `ai-agents`
- `claude-code`
- `codex`
- `cursor`
- `windsurf`
- `github-copilot`
- `prompt-engineering`
- `developer-tools`
- `software-architecture`
- `security-checklist`
- `production-readiness`

Social preview:
- asset: [assets/social-preview.png](./assets/social-preview.png)
- guide: [docs/social-preview.md](./docs/social-preview.md)
