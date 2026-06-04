# Integration Roadmap

This page describes VCP integration surfaces with explicit status labels.
It does not claim that roadmap or not-shipped surfaces already exist.

## Status source of truth

Use these files together:
- `docs/integrations/status-model.md`
- `.vcp/integrations.json`

## Current status summary

### Shipped

- local Python CLI;
- installed `vcp` console command after local install;
- local npm wrapper;
- local dashboard artifact generator;
- local metrics board;
- local audit-backlog visualization through generated artifacts.

### Local-template

- GitHub Actions PR Gate workflow template.

### Experimental

- plugin contract draft;
- plugin metadata validation scaffold.

### Roadmap

- public PyPI publication;
- public npm publication;
- VS Code extension.

### Not shipped

- hosted dashboard;
- plugin marketplace;
- Go CLI rewrite;
- web control plane.

## Honesty rules

Do not claim:
- official VS Code extension availability;
- public PyPI or npm publication unless actually published;
- hosted dashboard availability;
- plugin marketplace or remote registry;
- official third-party integrations unless they really exist.

## How to describe integrations safely

Say:
- shipped local CLI;
- local workflow template;
- experimental local plugin scaffold;
- roadmap-only extension direction;
- not-shipped hosted dashboard.
