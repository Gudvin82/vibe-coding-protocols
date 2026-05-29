<!-- vcp-artifact: PROJECT_MAP_REPOSITORY -->
<!-- vcp-version: v0.4.2 -->
<!-- methodology-version: v1.4 -->

# PROJECT_MAP.md

## Overview

- Vibe Coding Protocols is a markdown-first toolkit for AI-assisted delivery.
- Main outcome: safer routing,
  planning,
  hardening,
  maintenance refactoring,
  public-site readiness
  and release discipline.
- Current stage: public toolkit,
  active maintenance
  and protocol expansion.

## Entrypoints

- README: `README.md`
- route chooser: `START_HERE.md`
- docs map: `docs/README.md`
- protocol index: `docs/protocol-index.md`
- command index: `commands/README.md`
- main validation script: `scripts/vibe-check.sh`
- current CLI story: `docs/cli.md`

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
- security review scope template: `templates/reports/security-review-scope.md`
- protocol metadata template: `templates/protocol-pack-metadata.yml`

## Docs and references

- versioning: `docs/versioning.md`
- release notes: `docs/release-v0.4.2.md`
- release readiness: `docs/release-readiness.md`
- hardening thresholds: `docs/hardening-thresholds.md`
- architecture planning: `docs/architecture-map.md`
- CLI and wrappers: `docs/cli.md`, `docs/npm-wrapper.md`, `docs/python-wrapper.md`
- integrations: `docs/integrations/README.md`
- plugin honesty: `docs/ide-plugins.md`
- boundary honesty: `docs/boundary-linting.md`
- public-site readiness: `docs/public-site-readiness.md`, `docs/seo-ai-crawler-readiness.md`
- ecosystem references: `docs/ecosystem-references.md`
- defensive security positioning: `docs/security-tooling-landscape.md`

## Scripts and checks

- version consistency: `scripts/check-version-consistency.sh`
- newline guard: `scripts/check-newlines.py`
- toolkit structure: `scripts/check-toolkit.sh`
- links: `scripts/validate-links.sh`
- audit signal: `bash scripts/vibe-check.sh --audit --json`
- local hooks: `scripts/install-hooks.sh`

## Active / deferred surfaces

- active now: starter,
  hardening,
  extended,
  maintenance,
  integration docs,
  public-site docs,
  templates,
  scripts
  and CI;
- deferred until later: mature unified CLI,
  mature IDE plugins,
  AST boundary linting,
  published wrappers;
- not in scope: GUI,
  stack lock-in,
  offensive security tooling,
  guaranteed security claims.

## Known risks

- public docs must stay sanitized and trust-disciplined;
- protocol sprawl must stay indexed and route-driven;
- current tooling is intentionally lightweight and must not be overclaimed;
- external reviewers may judge raw readability as a trust signal,
  so markdown formatting must stay disciplined.
