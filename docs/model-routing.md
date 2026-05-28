# Model Routing for AI-Assisted Development

Use different AI models or agents for different work.

"Model routing" here means a manual or adaptive workflow pattern for choosing models or agents.
It is not an automatic router unless you build one.

## Default pattern

1. Cheap or fast discovery agent:
   - broad repository search;
   - file map;
   - symbol map;
   - evidence map;
   - no edits.

2. Strong reasoning or implementation agent:
   - reads the evidence map;
   - verifies critical files;
   - makes changes;
   - updates docs and backlog.

3. Independent reviewer:
   - reviews the diff;
   - does not inherit implementation assumptions;
   - reports findings.

## Why

Repository search burns context.
Implementation needs reasoning.
Review needs independence.

Do not use the strongest model for every read-only search if a cheaper or faster model is enough.

This is an optimization pattern, not a guaranteed cost-saving claim.

Actual savings depend on:
- repository size;
- AI IDE;
- model pricing or limits;
- quality of `PROJECT_MAP.md`;
- task complexity.

## Claude Code

Possible routing:
- Haiku or a cheaper model: read-only discovery, file map, evidence map.
- Sonnet or the main model: planning and implementation.
- Separate review pass: independent diff review.

If model selection is not available, simulate this workflow manually:
first ask for an evidence map, then ask for targeted implementation.

## Codex

Possible routing:
- Spark or a cheaper subagent: broad repository discovery.
- Main Codex model: decisions and implementation.
- Independent reviewer: diff review.

The discovery subagent must stay read-only and return compact evidence only.

## Generic AI IDE pattern

Ask the AI:

> Before editing, produce a compact evidence map:
> `path:line`, symbol, snippet or signature, why it matters.
> Do not read or rewrite the whole repository unless needed.

## What good routing looks like

A good routing workflow:
- keeps discovery lightweight;
- prevents giant context dumps into implementation;
- preserves a separate review step;
- makes large repositories less chaotic.

## Live docs when available

If your AI IDE supports Context7, MCP docs or another live-docs provider,
use it for package-specific implementation details and migration notes.
If live docs are unavailable, prefer official docs over memory and record assumptions in `AUDIT_BACKLOG.md`.

## What routing does not solve

Model routing does not automatically fix:
- weak project memory;
- unclear product scope;
- missing tests;
- missing security review;
- bad approval discipline.
