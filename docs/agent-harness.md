# Agent Harness

Vibe Coding Protocols is an agent harness for AI-assisted delivery.

It wraps AI coding agents with:
- project memory;
- stop conditions;
- model routing;
- token-aware code discovery;
- evidence maps;
- validation gates;
- independent review;
- audit backlog;
- security operations;
- release and rollback notes.

The goal is not to replace developers, tests or security work.
The goal is to make AI-assisted delivery more controlled, reviewable and repeatable.

## Why agent harness matters

AI output quality depends on more than a prompt.
Without a harness, even strong AI models drift toward broad edits, missing context, weak review loops and unclear ownership.

A harness gives the project a reusable operating layer:
- what the agent should read first;
- what the agent should avoid;
- when the agent must stop;
- how findings are handed off;
- what gets validated before merge or deploy.

## What the harness controls

The harness helps control:
- context entrypoints;
- active versus deferred scope;
- discovery strategy;
- implementation boundaries;
- validation steps;
- review independence;
- security baseline expectations;
- release and rollback notes.

## What it does not control

The harness does not replace:
- product judgment;
- human code review;
- formal security work;
- pentests;
- infrastructure controls;
- legal or compliance review;
- runtime monitoring.

## Harness layers

1. Memory layer
2. Scope layer
3. Discovery layer
4. Implementation layer
5. Review layer
6. Validation layer
7. Security layer
8. Release / handoff layer

### 1. Memory layer

Use stable project memory before code generation or edits:
- `README.md`
- `AGENTS.md` / `CLAUDE.md`
- `PROJECT_MAP.md`
- architecture docs
- `AUDIT_BACKLOG.md`
- `docs/PROMPTS.md`

### 2. Scope layer

Control what is in scope now versus later:
- active/deferred surfaces;
- first safe vertical slice;
- explicit non-goals;
- risky areas requiring approval.

### 3. Discovery layer

Use token-aware discovery before broad edits:
- targeted search;
- evidence maps;
- read-only discovery agents where available;
- no whole-repo reading by default.

### 4. Implementation layer

Keep implementation narrow and reviewable:
- smallest practical diff;
- explicit changed-files plan;
- dependency review before install;
- rollback-aware changes for risky surfaces.

### 5. Review layer

Separate implementation from review when possible:
- independent diff review;
- backlog findings;
- accepted risks documented;
- unresolved decisions surfaced early.

### 6. Validation layer

Validate what changed:
- `vibe-check`;
- focused tests;
- optional scanners;
- release-readiness checks.

### 7. Security layer

Keep baseline operational controls visible:
- secrets hygiene;
- auth/session baseline;
- perimeter review;
- third-party intake;
- security operations evidence.

### 8. Release / handoff layer

Make merge and deploy more repeatable:
- release notes;
- migration notes;
- rollback notes;
- handoff artifacts for the next human or agent.

## Minimal harness for solo builders

A minimal harness can be enough when the project is small and private:
- `README.md`
- `AGENTS.md`
- `PROJECT_MAP.md`
- Starter or Hardening route
- `vibe-check`
- small focused tests
- a lightweight backlog

## Extended harness for teams / production

Use the extended harness when the project is public, paid, client-facing or production-bound:
- Architecture Source of Truth;
- Security Operations Baseline;
- Third-Party Registry;
- perimeter and auth abuse checklists;
- independent review;
- migration and release notes;
- scanner integration.

## AI IDE compatibility

This harness is vendor-neutral.
It can be applied with:
- Claude Code;
- Codex;
- Cursor;
- Windsurf;
- GitHub Copilot;
- JetBrains AI tools;
- Antigravity;
- or manual prompt-driven workflows.

Use the same core idea everywhere:
- stable memory;
- controlled discovery;
- scoped implementation;
- validation before confidence.
