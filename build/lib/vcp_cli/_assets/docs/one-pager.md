# One-Pager

## Problem

AI-assisted development can move quickly, but it often drifts into vague scope,
outdated context, risky edits and weak handoff.

## Solution

Vibe Coding Protocols is a configuration and workflow layer around AI coding
agents.

It combines:
- route selection;
- copy-ready templates;
- lightweight checks;
- audit backlog discipline;
- agent rules;
- review and release guidance.

## Who it is for

- solo builders;
- MVP teams;
- consultants and client projects;
- teams adopting Claude Code, Codex, Cursor, Windsurf or Copilot workflows.

## What to copy first

Start with:
1. `templates/AGENTS.md`
2. `templates/PROJECT_MAP.md`
3. `templates/AUDIT_BACKLOG.md`
4. `prompts/product-brief-prompt_en.md` or `prompts/product-brief-prompt.md`

## What `vibe-check` does

`vibe-check` is a lightweight readiness signal.

It helps check:
- structure and memory files;
- `.gitignore` and env hygiene;
- obvious secret-like patterns;
- route coverage;
- optional scanners when available.

## What it does not replace

It does not replace:
- human review;
- formal security work;
- pentests;
- production monitoring;
- legal or compliance review.

## Three measurable signals to track

- time to Product Brief;
- files changed per AI task;
- findings caught before deploy.

Track them with real project data only.

## Start here

If you are not sure which route fits, open [START_HERE.md](../START_HERE.md).
