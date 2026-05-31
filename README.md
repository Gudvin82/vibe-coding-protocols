# Vibe Coding Protocols

[Русская версия](./README_ru.md)

[![Repo Version](https://img.shields.io/badge/repo-v0.5.0-blue)](./CHANGELOG.md)
[![Methodology](https://img.shields.io/badge/methodology-v1.4-purple)](https://anmalishev.ru/expert/vibe-coding/)
[![AI Intake Ready](https://img.shields.io/badge/AI%20Intake-ready-brightgreen)](./AI_INTAKE.md)
[![CLI Local](https://img.shields.io/badge/CLI-local-blue)](./docs/cli.md)
[![Manifests](https://img.shields.io/badge/manifests-v1-blue)](./vcp.manifest.json)
[![Benchmarks](https://img.shields.io/badge/benchmarks-local-blue)](./benchmarks/ai-adoption/README.md)
[![No Offensive Tooling](https://img.shields.io/badge/no-offensive--tooling-yes-success)](./docs/security-tooling-landscape.md)
[![Script First](https://img.shields.io/badge/script--first-compatible-lightgrey)](./docs/cli.md)

**Not a prompt collection.**

VCP is a controlled AI delivery framework for AI-assisted software development.
It provides routes, protocols, adoption packs, validation, review gates, manifests, benchmarks and project memory so AI agents do not write or change code chaotically.

Repository package: `v0.5.0`

Web methodology: `Vibe Coding Protocols v1.4`

## Give this repo to your AI

Start with [AI_INTAKE.md](./AI_INTAKE.md), not with a shallow README skim.
If agent rules are needed, prefer [templates/AGENTS.md](./templates/AGENTS.md) over copying root `AGENTS.md`.
Then route through:
- [START_HERE.md](./START_HERE.md)
- [docs/protocol-index.md](./docs/protocol-index.md)
- [docs/adoption-packs.md](./docs/adoption-packs.md)
- [templates/prompts/evaluate-vcp-for-my-repo.md](./templates/prompts/evaluate-vcp-for-my-repo.md)

## Try the product layer

```bash
python3 -m vcp_cli route --profile shared-engine
python3 -m vcp_cli adopt --pack shared-engine --dry-run
python3 -m vcp_cli review plan
python3 -m vcp_cli score
python3 -m vcp_cli benchmark run
```

```text
Route: Full Hardening
Adoption pack: Shared Engine / Multi-product
Review gate: Post-Task Code Review before next feature
First action: create PROJECT_MAP and Architecture Source of Truth before code changes
```

## Start here

| Situation | Start here |
|---|---|
| New project or idea | [Starter Protocol](./protocols/ai-project-starter-protocol.md) |
| Existing AI-generated MVP | [Hardening Protocol](./protocols/ai-project-hardening-protocol.md) |
| Production, regulated or shared engine repo | [AI_INTAKE.md](./AI_INTAKE.md) + [adoption packs](./docs/adoption-packs.md) |
| Working code that is hard to change | [Maintenance Refactoring](./protocols/maintenance/care-refactoring.md) |
| UI styling or component ownership drift | [UI Component Ownership](./protocols/maintenance/ui-refactoring.md) |
| Active diff that must be accepted before moving on | [Post-Task Code Review](./protocols/review/post-task-code-review.md) |
| Public docs or marketing site | [Public Site Readiness](./docs/public-site-readiness.md) |

## What is product-grade in v0.5.0

- Unified local CLI surface
- Machine-readable manifests
- Route chooser
- Adoption dry-run planner
- Post-task review gate helper
- Heuristic score report
- AI adoption benchmark scenarios
- Demo output
- Sanitized case-study structure

## New: Post-Task Code Review Gate

After meaningful AI-generated changes, do not immediately start the next feature.
Run `/loop-code-review` or use the Post-Task Code Review Protocol:
review active git changes,
fix actionable findings,
run validation,
and accept only after review plus validation are green.

## Current CLI surface

- [docs/cli.md](./docs/cli.md)
- [vcp.manifest.json](./vcp.manifest.json)
- [docs/demo.md](./docs/demo.md)
- [docs/demo-output.md](./docs/demo-output.md)
- [benchmarks/ai-adoption/README.md](./benchmarks/ai-adoption/README.md)

## What VCP is not

- not a hacking toolkit;
- not an exploit framework;
- not a pentest suite;
- not a bug bounty automation suite;
- not a red-team operator;
- not a DDoS, RAT, phishing or payload tool collection;
- not a production security certification;
- not a legal compliance certification;
- not a replacement for developers, tests, security review, legal review or human judgment.

## Key links

- [AI_INTAKE.md](./AI_INTAKE.md)
- [docs/cli.md](./docs/cli.md)
- [docs/route-map.md](./docs/route-map.md)
- [docs/protocol-index.md](./docs/protocol-index.md)
- [docs/adoption-packs.md](./docs/adoption-packs.md)
- [docs/security-tooling-landscape.md](./docs/security-tooling-landscape.md)
- [docs/public-site-readiness.md](./docs/public-site-readiness.md)
- [docs/seo-ai-crawler-readiness.md](./docs/seo-ai-crawler-readiness.md)
- [docs/community-feedback.md](./docs/community-feedback.md)
- [docs/release-v0.5.0.md](./docs/release-v0.5.0.md)
- [docs/known-limitations.md](./docs/known-limitations.md)
