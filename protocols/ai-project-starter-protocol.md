# AI Project Starter Protocol

A markdown-first starter protocol for new AI-assisted projects.

## Goal

Do not let the AI jump straight into chaotic code generation.
Start with a Product Brief, stack choice, active versus deferred surfaces,
Memory Bank files, an operational baseline and the first safe vertical slice.

## Step -1. Product Brief

Capture first:
- what the product is;
- who it is for;
- what the first measurable outcome is;
- which surfaces are active now;
- which surfaces are explicitly deferred.

Use one of these prompts:
- [English Product Brief prompt](../prompts/product-brief-prompt_en.md)
- [Russian Product Brief prompt](../prompts/product-brief-prompt.md)

## Prompt 0. Technical intake

Before code, the AI should clarify:
- stack;
- deployment target;
- runtime boundaries;
- active and deferred surfaces;
- integrations;
- auth, payment, legal or personal-data risk areas;
- test, build and validation baseline.

See [../prompts/starter-prompts.md](../prompts/starter-prompts.md).

## Stack decision framework

When choosing a stack, the AI should answer:
- which primary database is needed;
- which entities will matter first;
- whether a migration strategy is needed;
- whether background jobs are needed now or later;
- whether cache is needed now or later;
- where the likely bottleneck is;
- what is intentionally deferred.

Do not add complexity without a reason.
If the chosen path creates an obvious growth dead-end, the AI should say so.

## Active and deferred surfaces

Separate clearly:
- active now;
- deferred until later.

Example surfaces:
- web frontend;
- backend or API;
- database;
- bot or AI-agent;
- mobile or mini app;
- payments;
- admin;
- workers or queues.

## Operational baseline

Before production, decide:
- where Product Brief, Architecture, Project Map, AGENTS and Security docs live;
- which docs may live in the repo and which should stay private;
- where secrets live;
- who has access to secrets;
- whether workers, scanners or browser automation are needed;
- whether outbound restrictions are needed;
- where logs and alerts live;
- whether staging is needed.

## Architecture docs storage policy

Architecture Source of Truth is useful, but sensitive.

Recommendations:
- do not keep a full architecture reference in a public webroot;
- store it locally, privately, sanitized or encrypted;
- limit access by role;
- publish only a sanitized version without secrets, internal paths,
  IPs, admin routes or private APIs.

## Safe third-party intake

Before connecting an external repo, template, package or API:
- verify origin;
- verify license;
- verify project activity;
- review install scripts and workflows;
- do not grant production secrets;
- test in sandbox or staging first;
- document version, commit and risks.

## Database and load readiness

Scalability-aware does not mean enterprise-heavy.

At minimum:
- choose the primary database consciously;
- define key entities;
- avoid mixing domain data and temporary data without a reason;
- plan for migrations;
- add indexes for expected query patterns;
- avoid heavy synchronous operations without a reason;
- think about rate limits, retries and idempotency if APIs,
  payments or webhooks are involved.

## Memory Bank

Minimum Memory Bank:
- `README.md`
- `AGENTS.md`
- `PROJECT_MAP.md`
- `ARCHITECTURE.md` or Architecture Source of Truth
- `SECURITY.md`
- `AUDIT_BACKLOG.md`
- `docs/PROMPTS.md`

## AGENTS.md

`AGENTS.md` should define:
- role;
- stop conditions;
- approval gates;
- code discovery first;
- small or atomic diffs;
- reporting after changes;
- no destructive commands without approval.

See the template: [../templates/AGENTS.md](../templates/AGENTS.md).

For Claude Code projects, review `.claude/settings.json` and tool
permissions if present. Tool access is part of the operational baseline.

## Stop conditions

Stop and ask for approval when:
- the change touches more than 10 files;
- the change touches more than 2 layers at once;
- the change adds auth, payments, admin, workers or external APIs;
- the change requires a new dependency;
- the change changes database schema;
- the change rewrites architecture instead of making a small slice;
- tests or build are red and the fix is not obvious.

## AI cost awareness

Do not waste context:
- do not read the whole repo without a reason;
- start with `PROJECT_MAP.md`;
- do not run LLM or API loops without limits;
- record expensive loops in `AUDIT_BACKLOG.md` or `docs/PROMPTS.md`.

## Prompt versioning

If the project is AI-assisted, keep adapted prompts in `docs/PROMPTS.md`.

See the template: [../templates/PROMPTS.md](../templates/PROMPTS.md).

## AI-generated test strategy

The AI should not generate every possible test first.

Prioritize:
- critical path;
- regressions;
- the existing test framework;
- mocked external APIs or LLMs;
- no new test framework without approval;
- a clearly deferred tests list.

## First safe iteration

Before the first vertical slice, the AI should:
- show a changed-files plan;
- say which database queries appear;
- point out N+1 risk if relevant;
- say whether the flow is sync or async;
- mark external API or LLM use in the critical path;
- propose a checkpoint if the change is risky.

After implementation, the AI should report:
- which tables or migrations appeared;
- which query patterns were added;
- which indexes were added or deferred;
- which bottlenecks are expected;
- what belongs in the scalability backlog.

## Starter to Hardening

After the first safe iteration, do not keep piling on features blindly.

Move into Hardening first:
- reuse the Product Brief;
- update `PROJECT_MAP.md`;
- review architecture;
- expand the security baseline;
- populate `AUDIT_BACKLOG.md`;
- run Light Hardening if this is still an early slice.

See [starter-to-hardening-bridge.md](./starter-to-hardening-bridge.md).
