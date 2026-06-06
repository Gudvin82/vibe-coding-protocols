<!-- vcp-version: v0.9.1 -->
<!-- vcp-version: v0.9.0 -->
<!-- methodology-version: v1.4 -->
<!-- vcp-version: v0.8.4 -->

<!-- vcp-version: v0.8.2 -->

<!-- vcp-artifact: PROJECT_MAP -->
<!-- vcp-version: v0.8.2 -->

# PROJECT_MAP.md

## Overview
- [FILL IN: what this project does]
- [FILL IN: main user or business flow]
- Current stage: [FILL IN: idea / MVP / staging / production-like]

## Compact planning references
- Architecture Map: `ARCHITECTURE_MAP.md`, if the project has multiple surfaces
- Architecture Source of Truth: `ARCHITECTURE_SOURCE_OF_TRUTH.md`, if a detailed architecture document exists

## Backlog synchronization rule
- If a backlog item has architecture impact `component-level`, update this map when routes, components, or ownership change.
- If a backlog item has architecture impact `cross-layer` or `production-critical`, update this map and `ARCHITECTURE_SOURCE_OF_TRUTH.md` or create a linked follow-up backlog item.

## Entrypoints
- frontend entrypoints: [FILL IN]
- backend entrypoints: [FILL IN]
- CLI / workers / schedulers: [FILL IN]

## Routes / Endpoints
- public routes: [FILL IN]
- API routes: [FILL IN]
- admin routes: [FILL IN]
- internal-only endpoints: [FILL IN]

## Components / Modules
- key UI modules: [FILL IN]
- domain services: [FILL IN]
- integrations: [FILL IN]
- workers / queues: [FILL IN]

## Data model
- key entities: [FILL IN]
- important relations: [FILL IN]
- high-growth tables / collections: [FILL IN]

## Integrations
- third-party APIs: [FILL IN]
- webhooks: [FILL IN]
- bot / Telegram / CRM / BI: [FILL IN]

## Scripts / Commands
- install: [FILL IN]
- dev: [FILL IN]
- build: [FILL IN]
- test: [FILL IN]
- lint: [FILL IN]
- migrations: [FILL IN]
- deploy: [FILL IN]
- maintenance refactoring command, if used: `/care-refactoring`
- UI ownership command, if used: `/ui-refactoring`

## Active / Deferred surfaces
- active now: [FILL IN]
- deferred until later: [FILL IN]
- not in scope: [FILL IN]

## Known risks
- technical debt: [FILL IN]
- security gaps: [FILL IN]
- scalability concerns: [FILL IN]
- missing docs / tests / scanners: [FILL IN]
- maintainability hotspots worth a future refactoring pass: [FILL IN]

Example:
- active now: public landing page, auth, billing callback
- deferred until later: mobile app, admin analytics, partner API
