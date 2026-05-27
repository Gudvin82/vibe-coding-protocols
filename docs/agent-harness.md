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

"Agent harness" here means a configuration and workflow layer around AI coding agents.
It is not a runtime orchestration engine.

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

## Minimal harness for solo builders

Start with:
- `templates/AGENTS.md`
- `templates/PROJECT_MAP.md`
- `templates/AUDIT_BACKLOG.md`
- `docs/lite-adoption-path.md`
- `vibe-check --starter`

## Extended harness for teams or production

Add:
- architecture source of truth;
- security operations baseline;
- third-party registry;
- incident recovery runbook;
- independent review and release checks.

## AI IDE compatibility

This repository stays vendor-neutral and can be adapted to Claude Code, Codex, Cursor, Windsurf, Copilot, JetBrains and similar tools.
