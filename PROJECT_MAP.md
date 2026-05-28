<!-- vcp-artifact: PROJECT_MAP_REPOSITORY -->
<!-- vcp-version: v0.4.1 -->
<!-- methodology-version: v1.4 -->

# PROJECT_MAP.md

## Overview
- Vibe Coding Protocols is a markdown-first toolkit for AI-assisted delivery.
- Main outcome: safer routing, planning, hardening, maintenance refactoring and release discipline.
- Current stage: public toolkit, active maintenance and protocol expansion.

## Entrypoints
- README: `README.md`
- route chooser: `START_HERE.md`
- docs map: `docs/README.md`
- protocol index: `protocols/README.md`
- command index: `commands/README.md`
- main validation script: `scripts/vibe-check.sh`

## Main routes
- Lite: `docs/lite-adoption-path.md`
- Starter: `protocols/ai-project-starter-protocol.md`
- Hardening: `protocols/ai-project-hardening-protocol.md`
- Extended: `protocols/ai-project-extended-protocol.md`
- Maintenance refactoring: `protocols/maintenance/care-refactoring.md`
- UI component ownership: `protocols/maintenance/ui-refactoring.md`

## Protocol support files
- maintenance route index: `protocols/maintenance/README.md`
- care command: `commands/care-refactoring.md`
- UI command: `commands/ui-refactoring.md`
- refactoring report template: `templates/reports/refactoring-report.md`
- UI refactoring report template: `templates/reports/ui-refactoring-report.md`

## Docs and references
- versioning: `docs/versioning.md`
- release readiness: `docs/release-readiness.md`
- hardening thresholds: `docs/hardening-thresholds.md`
- architecture planning: `docs/architecture-map.md`
- wrappers and productization: `docs/npm-wrapper.md`, `docs/python-wrapper.md`, `docs/vscode-extension.md`

## Scripts / checks
- version consistency: `scripts/check-version-consistency.sh`
- newline guard: `scripts/check-newlines.py`
- toolkit structure: `scripts/check-toolkit.sh`
- links: `scripts/validate-links.sh`
- audit signal: `bash scripts/vibe-check.sh --audit --json`

## Active / deferred surfaces
- active now: starter, hardening, extended and maintenance protocol lanes; docs; templates; scripts; CI
- deferred until later: published npm package, published Python package, published VS Code extension
- not in scope: GUI, stack lock-in, guaranteed security claims

## Known risks
- external raw fetchers may disagree with blob or clone state;
- public docs must stay sanitized and trust-disciplined;
- protocol sprawl must stay indexed and route-driven.
