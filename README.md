# Vibe Coding Protocols

[Русская версия](./README_ru.md)

[![Repo Version](https://img.shields.io/badge/repo-v0.4.4-blue)](./CHANGELOG.md)
[![Methodology](https://img.shields.io/badge/methodology-v1.4-purple)](https://anmalishev.ru/expert/vibe-coding/)
[![License](https://img.shields.io/github/license/Gudvin82/vibe-coding-protocols)](./LICENSE)
[![Vibe Check](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml/badge.svg)](https://github.com/Gudvin82/vibe-coding-protocols/actions/workflows/vibe-check.yml)
[![Latest Release](https://img.shields.io/github/v/release/Gudvin82/vibe-coding-protocols)](https://github.com/Gudvin82/vibe-coding-protocols/releases)
[![Last Commit](https://img.shields.io/github/last-commit/Gudvin82/vibe-coding-protocols)](https://github.com/Gudvin82/vibe-coding-protocols/commits/main)

**Not a prompt collection.**

VCP is an operating layer for AI-assisted delivery:
routes, Memory Bank files, stop conditions, checks, hardening, incident recovery and release gates.

Repository package: `v0.4.4`

Web methodology: `Vibe Coding Protocols v1.4`

## Give this repo to your AI

Paste this into Claude Code, Codex, Cursor, Windsurf or Copilot:

```text
Study this repository as a workflow toolkit.

Do not write code yet.

First choose my route:
Lite, Starter, Hardening, Maintenance Refactoring, UI Component Ownership or Extended.

Then return:
1. files to copy first;
2. files not to copy;
3. first validation command;
4. underestimated risks;
5. next smallest safe step.
```

## Giving VCP to an AI agent?

Ask it to read [AI_INTAKE.md](./AI_INTAKE.md) first.

Do not ask an agent to just evaluate the repo from `README.md` alone.
VCP has multiple routes:
- new project;
- existing MVP;
- production hardening;
- maintenance refactoring;
- UI ownership;
- public site readiness.

Use [templates/prompts/evaluate-vcp-for-my-repo.md](./templates/prompts/evaluate-vcp-for-my-repo.md)
when asking Claude Code, Codex, Cursor, Windsurf or Copilot to adopt VCP.

## Use this when

- You already have AI-generated code and need to know what is unsafe before showing it to a client.
- You are starting a new vibe-coded project and want minimal rails for architecture, security and release.
- You already have a working project and want scoped refactoring before the next feature locks in bad patterns.
- Your frontend works but pages own visual styling that should belong inside components.
- You are a founder or solo builder who wants a lightweight process, not enterprise bureaucracy.
- You are a small team or CTO defining how AI can safely touch code.

<details>
<summary>How VCP is different</summary>

| Approach | What you get | What is missing |
|---|---|---|
| Prompt collection | Prompts | No gates, checks or handoff |
| IDE rules only | Better agent behavior | No release readiness |
| Security scanner | Technical findings | No project workflow |
| Starter template | Fast bootstrap | Stack lock-in |
| VCP | Routes, artifacts, checks and handoff | Requires adoption discipline |

</details>

If you are on mobile, start with:
1. [START_HERE.md](./START_HERE.md)
2. [docs/lite-adoption-path.md](./docs/lite-adoption-path.md)
3. [prompts/use-this-repo-prompt.md](./prompts/use-this-repo-prompt.md)

## Start here

| Situation | Start here |
|---|---|
| Only an idea | [English Product Brief prompt](./prompts/product-brief-prompt_en.md) |
| New AI-assisted project | [Starter Protocol](./protocols/ai-project-starter-protocol.md) |
| Existing AI-generated code that needs production or security readiness | [Hardening Protocol](./protocols/ai-project-hardening-protocol.md) |
| Existing project that works but is getting risky to change | [Maintenance Refactoring](./protocols/maintenance/care-refactoring.md) |
| Existing frontend with styling or component ownership drift | [UI Component Ownership](./protocols/maintenance/ui-refactoring.md) |
| Public, client-facing or production-bound project | [Extended Protocol](./protocols/ai-project-extended-protocol.md) |
| AI IDE setup | [START_HERE.md](./START_HERE.md) |

Already works but hard to change?
- Use Maintenance Refactoring: `/care-refactoring`
- UI drift or styling chaos? Use UI Component Ownership: `/ui-refactoring`

Existing production repo, shared engine, payments or personal data?
- Read [AI_INTAKE.md](./AI_INTAKE.md)
- Use [docs/adoption-packs.md](./docs/adoption-packs.md)
- Default to Hardening or Full Hardening unless evidence says otherwise

## If you only copy one thing

### Solo / MVP

1. Copy `templates/AGENTS.md` as `AGENTS.md`.
2. Copy `templates/PROJECT_MAP.md`.
3. Use `prompts/product-brief-prompt_en.md`.
4. Run `bash scripts/vibe-check.sh --starter`.

If the project has multiple surfaces, add `ARCHITECTURE_MAP.md` before asking AI to generate code.
Use:
- [templates/ARCHITECTURE_MAP.md](./templates/ARCHITECTURE_MAP.md)
- [prompts/architecture-map-prompt.md](./prompts/architecture-map-prompt.md)

<details>
<summary>Small team and production additions</summary>

### Small team

Add:
- `templates/AUDIT_BACKLOG.md`
- `templates/ARCHITECTURE_SOURCE_OF_TRUTH.md`
- CI with `bash scripts/vibe-check.sh --audit`

### Production / client-facing

Add:
- `templates/SECURITY_BASELINE.md`
- `templates/SECURITY_OPERATIONS_BASELINE.md`
- `templates/THIRD_PARTY_REGISTRY.md`
- `templates/INCIDENT_RECOVERY_RUNBOOK.md`
- `templates/METRICS_BOARD.md`

</details>

## Recommended: review-first setup

```bash
curl -fsSL https://raw.githubusercontent.com/Gudvin82/vibe-coding-protocols/main/scripts/init-minimal.sh -o init-minimal.sh
curl -fsSL https://raw.githubusercontent.com/Gudvin82/vibe-coding-protocols/main/SHA256SUMS -o SHA256SUMS
less init-minimal.sh
bash init-minimal.sh --starter
```

If you want checksum verification:

Linux:

```bash
grep "scripts/init-minimal.sh" SHA256SUMS > init-minimal.sha256
sha256sum -c init-minimal.sha256
```

macOS:

```bash
grep "scripts/init-minimal.sh" SHA256SUMS > init-minimal.sha256
shasum -a 256 init-minimal.sh
```

Optional local guardrail:

```bash
bash scripts/install-hooks.sh --mode starter
```

For advanced install notes, checksum workflow details and the optional fast track
for empty or test repositories only, see
[docs/advanced-install.md](./docs/advanced-install.md).

## Which agent file should I use?

- Root `AGENTS.md` configures this repository.
- Root `CLAUDE.md` configures Claude Code for this repository.
- Do not copy root `AGENTS.md` blindly into your project.
- For your own project, copy `templates/AGENTS.md` as `AGENTS.md`.
- For Claude Code, use `templates/AGENTS.claude.md` or adapt it into your project's `CLAUDE.md`.
- For Cursor or Windsurf, use `templates/AGENTS.cursor.md` or `templates/AGENTS.windsurf.md`.

Core memory files used across the toolkit:
- `README.md`
- `AGENTS.md` or `CLAUDE.md`
- `PROJECT_MAP.md`
- `ARCHITECTURE_MAP.md`, when multiple surfaces or stack choices need a compact visual map
- `ARCHITECTURE_SOURCE_OF_TRUTH.md`, if needed
- `AUDIT_BACKLOG.md`, for hardening
- `docs/PROMPTS.md` or `PROMPTS.md`, if prompts are tracked
- `SECURITY.md` or `SECURITY_BASELINE.md`, for public or production projects

## Self-dogfooding

This repository runs VCP checks on itself.
See [docs/self-dogfooding.md](./docs/self-dogfooding.md).

## New: Post-Task Code Review Gate

After meaningful AI-generated changes, do not immediately start the next feature.
Run `/loop-code-review` or use the Post-Task Code Review Protocol: review active git changes, fix actionable findings, run validation, and accept only after review plus validation are green.

## CLI status

VCP is currently script-first. A unified `vcp` CLI is planned; see [docs/cli.md](./docs/cli.md) for current stable entrypoints and experimental wrapper status.

## Vibe-check

`vibe-check` is a readiness signal.
It is not a security scanner and not a security certification.

```bash
bash scripts/vibe-check.sh --help
bash scripts/vibe-check.sh --starter
bash scripts/vibe-check.sh --hardening
bash scripts/vibe-check.sh --audit
bash scripts/vibe-check.sh --audit --json
```

### Doctor, route suggestion and update advice

```bash
bash scripts/vibe-check.sh --doctor
bash scripts/vibe-check.sh --doctor --json
bash scripts/vibe-check.sh --init-report
bash scripts/vibe-check.sh --init-report --json
bash scripts/vibe-check.sh --update-advice
bash scripts/vibe-check.sh --update-advice --json
```

See:
- [docs/vibe-check-scoring.md](./docs/vibe-check-scoring.md)
- [docs/vibe-check-doctor.md](./docs/vibe-check-doctor.md)
- [docs/vibe-check-init-report.md](./docs/vibe-check-init-report.md)
- [docs/update-copied-artifacts.md](./docs/update-copied-artifacts.md)
- [docs/vibe-check-reference.md](./docs/vibe-check-reference.md)

## Release gates

See:
- [docs/hardening-thresholds.md](./docs/hardening-thresholds.md)
- [docs/release-readiness.md](./docs/release-readiness.md)

Short version:
- Lite -> local MVP only
- Starter -> first vertical slice
- Hardening -> staging candidate
- Extended -> production candidate review
- Release -> deploy gate with explicit blockers and evidence

If auth, payments, personal data or public exposure are involved, do not claim production readiness without Extended review.

## New in v0.4.4: Post-Task Code Review Gate

`v0.4.4` adds a first-class post-task review gate so meaningful AI-generated changes are reviewed before the next feature, merge or release:
- a dedicated review family in [protocols/review/README.md](./protocols/review/README.md);
- the core [Post-Task Code Review Protocol](./protocols/review/post-task-code-review.md);
- the operational command doc [commands/loop-code-review.md](./commands/loop-code-review.md);
- the reusable prompt in [templates/prompts/loop-code-review.md](./templates/prompts/loop-code-review.md);
- the structured report in [templates/reports/code-review-report.md](./templates/reports/code-review-report.md);
- synthetic review examples in [examples/review/README.md](./examples/review/README.md).

## Architecture and planning

Use Architecture Map when you need a 30-second project map before code:
- [docs/architecture-map.md](./docs/architecture-map.md)
- [templates/ARCHITECTURE_MAP.md](./templates/ARCHITECTURE_MAP.md)
- [examples/architecture-map-example.md](./examples/architecture-map-example.md)
- [prompts/architecture-map-prompt.md](./prompts/architecture-map-prompt.md)

## CLI and integrations

CLI status: VCP is currently script-first.
A unified `vcp` CLI is planned; see [docs/cli.md](./docs/cli.md) for current stable entrypoints and experimental wrapper status.

Integration and plugin status:
- [docs/integrations/README.md](./docs/integrations/README.md)
- [docs/ide-plugins.md](./docs/ide-plugins.md)
- [docs/boundary-linting.md](./docs/boundary-linting.md)

AI intake and adoption guides:
- [AI_INTAKE.md](./AI_INTAKE.md)
- [docs/target-project-classifier.md](./docs/target-project-classifier.md)
- [docs/adoption-packs.md](./docs/adoption-packs.md)
- [templates/prompts/evaluate-vcp-for-my-repo.md](./templates/prompts/evaluate-vcp-for-my-repo.md)

## Wrappers and productization skeletons

These are prepared, not published product surfaces:
- experimental npm wrapper: [docs/npm-wrapper.md](./docs/npm-wrapper.md)
- experimental Python wrapper: [docs/python-wrapper.md](./docs/python-wrapper.md)
- experimental VS Code extension skeleton: [docs/vscode-extension.md](./docs/vscode-extension.md)

## Windows

VCP is bash-first.

Recommended Windows options:
- Git Bash
- WSL
- PowerShell wrapper: `scripts/vibe-check.ps1`

Native Windows CLI is not available yet.
See [docs/windows.md](./docs/windows.md).

## Public site and ecosystem

- [docs/public-site-readiness.md](./docs/public-site-readiness.md)
- [docs/seo-ai-crawler-readiness.md](./docs/seo-ai-crawler-readiness.md)
- [docs/ecosystem-references.md](./docs/ecosystem-references.md)
- [docs/security-tooling-landscape.md](./docs/security-tooling-landscape.md)
- [protocols/review/README.md](./protocols/review/README.md)
- [commands/loop-code-review.md](./commands/loop-code-review.md)
- [docs/release-v0.4.4.md](./docs/release-v0.4.4.md)

## Examples and case studies

Examples are synthetic or sanitized learning examples.
They are not claimed as real-world case studies.

- [examples/README.md](./examples/README.md)
- [examples/legacy-ai-mess-vibe](./examples/legacy-ai-mess-vibe/)
- [case-studies/README.md](./case-studies/README.md)
- [case-studies/real-case-submission-template.md](./case-studies/real-case-submission-template.md)
- [case-studies/redaction-guide.md](./case-studies/redaction-guide.md)

## What VCP is not

- not a security scanner;
- not a pentest suite;
- not a plugin marketplace;
- not a replacement for developer, security or legal review.

## Community and distribution

- [docs/community.md](./docs/community.md)
- [docs/distribution-checklist.md](./docs/distribution-checklist.md)
- [docs/mirrors.md](./docs/mirrors.md)
- [docs/mirror-sync.md](./docs/mirror-sync.md)
- [docs/adoption-feedback.md](./docs/adoption-feedback.md)
- [docs/community-feedback.md](./docs/community-feedback.md)

## Known limitations

See:
- [docs/known-limitations.md](./docs/known-limitations.md)
- [docs/prompt-drift-control.md](./docs/prompt-drift-control.md)
- [docs/tooling-roadmap.md](./docs/tooling-roadmap.md)
- [docs/comparison.md](./docs/comparison.md)
- [comparison.md](./comparison.md)

## Current release notes

- [docs/release-v0.4.4.md](./docs/release-v0.4.4.md)
