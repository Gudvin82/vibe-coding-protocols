# TAKE_THIS_FIRST.md — How to adopt VCP without copying everything

Use this file when someone gives VCP to an AI agent and says:

> Study this repository and take what is useful for my project.

## Do not copy the whole repository

VCP is a source toolkit. Target projects should adopt only the route, pack, templates, and review gates they need.

If you are also evaluating VCP itself, switch to:
- `FULL_REPO_INTAKE.md`
- `AI_FULL_REPO_AUDIT.md`
- `REPO_CAPABILITIES_INDEX.md`

## Step 1 — classify the target project by track

- New idea / founder brief -> New Project Track
- Existing AI-generated MVP -> Existing Project Track
- Production repo near release -> Existing Project Track with release readiness
- Public website/product -> Public Growth
- Ongoing AI changes -> Review Diff + PR Gate
- Tiny change -> No-spec + validation

## Step 2 — choose route and pack

Run or inspect:

```bash
python3 -m vcp_cli route --profile production --json
python3 -m vcp_cli adopt --pack production --dry-run --json
python3 -m vcp_cli spec depth --task "describe the task" --json
```

Track docs:
- `docs/two-track-model.md`
- `docs/spec-foundation.md`
- `docs/spec-quality-gate.md`
- `docs/walkthroughs/new-ai-product-from-idea.md`
- `docs/walkthroughs/ai-mvp-hardening.md`
- `docs/release-readiness.md`
- `docs/architecture-drift.md`

## Step 3 — copy only selected files

Usually copy:
- relevant templates;
- selected protocol;
- selected command prompt;
- report templates;
- target-project `AGENTS.md` template;
- backlog/report files if needed.

Do not copy:
- VCP repository internals;
- release docs;
- benchmarks unless you are extending VCP;
- manifests unless the target project needs machine-readable VCP metadata;
- unrelated protocols.

## Step 4 — explain what not to take

A good adoption answer must include:
- what to copy;
- what not to copy;
- why;
- expected workflow;
- validation commands;
- stop conditions.

## Output format for AI agents

Return:
- Target project type
- Track
- Recommended route
- Recommended adoption pack
- Spec depth
- Files to copy
- Files not to copy
- Required review gates
- Required validation
- Risks / stop conditions

## Brownfield note

If a working repository already exists but architecture, backlog, or release discipline is weak, prefer the Brownfield Rescue Pack instead of re-running greenfield setup.

## Related prompt and report

- Prompt: `templates/prompts/adopt-vcp-from-link.md`
- Report: `templates/reports/vcp-adoption-decision-report.md`
- Full repo audit report: `templates/reports/ai-repo-audit-coverage-report.md`
- Brownfield report: `templates/reports/brownfield-rescue-report.md`
- Two-track model: `docs/two-track-model.md`
- Version semantics: `docs/version-semantics.md`
- Project memory: `docs/project-memory-model.md`
- Protocol-pack security: `docs/protocol-pack-security.md`

## Кратко по-русски

Если пользователь дал ссылку на VCP и сказал «возьми лучшее», не копируй весь репозиторий. Сначала определи track, потом route, adoption pack и spec depth, и только после этого перечисли нужные файлы и объясни, что брать не надо.
