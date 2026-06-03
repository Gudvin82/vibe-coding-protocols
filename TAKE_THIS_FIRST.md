# TAKE_THIS_FIRST.md — How to adopt VCP without copying everything

Use this file when someone gives VCP to an AI agent and says:

> Study this repository and take what is useful for my project.

## Do not copy the whole repository

VCP is a source toolkit. Target projects should adopt only the route, pack, templates and review gates they need.

## Step 1 — classify the target project

- New product from idea -> Spec-first / Starter
- Existing AI-generated MVP -> Hardening
- Production project -> Production diagnostics + review gates
- Public website/product -> Public Growth
- Ongoing AI changes -> Review Diff + Backlog
- Tiny change -> No-spec + validation

## Step 2 — choose route and pack

Run or inspect:

```bash
python3 -m vcp_cli route --profile production --json
python3 -m vcp_cli adopt --pack production --dry-run --json
python3 -m vcp_cli spec depth --task "describe the task" --json
```

Visual overview: `docs/visual-overview.md`
2-minute demo: `docs/demo.md`
PR Gate: `docs/pr-gate.md`
Public source-of-truth audit: `docs/public-source-of-truth-audit.md`

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
- Recommended route
- Recommended adoption pack
- Spec depth
- Files to copy
- Files not to copy
- Required review gates
- Required validation
- Risks / stop conditions

## Related prompt and report

- Prompt: `templates/prompts/adopt-vcp-from-link.md`
- Report: `templates/reports/vcp-adoption-decision-report.md`
- Visual overview: `docs/visual-overview.md`

## Кратко по-русски

Если пользователь дал ссылку на VCP и сказал "возьми лучшее", не копируй весь репозиторий. Сначала определи тип проекта, выбери route, adoption pack и spec depth, а потом перечисли только нужные файлы и объясни, что не нужно брать.
