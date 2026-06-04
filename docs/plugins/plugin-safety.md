# Plugin Safety Boundary

Plugin support in `v0.8.2` is metadata-first and safety-first.

## Safety rules

- No auto-execution by default.
- No remote registry.
- No network calls in listing or validation.
- No arbitrary shell execution.
- Read-only plugins are safer by default.
- Write-capable plugins must be treated as higher-risk local artifacts.

## Trust levels

Suggested trust language:
- `local-reviewed`
- `local-unreviewed`
- `maintainer-reviewed`
- `unknown`

## What validation means in `v0.8.2`

`plugins validate` checks metadata shape only.
It does not:
- import code;
- run entrypoints;
- install dependencies;
- contact a registry.

This keeps the feature in scaffold territory instead of turning it into a hidden execution engine.
