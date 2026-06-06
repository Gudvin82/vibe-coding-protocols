<!-- vcp-version: v0.9.3 -->
<!-- methodology-version: v1.4 -->
# Client Adoption Playbook

Use this playbook when VCP is being introduced into a real client, team, or portfolio context.

## Definition of success

After `v0.9.3`, client/team adoption should feel more practical and less ambiguous.

Success means:
- a consultant or tech lead can explain where VCP starts and where it stops;
- a team can choose one clear rollout path instead of reading the whole repository first;
- AI tool setup is copy-ready instead of improvised;
- trust-check, PR Gate, and backlog operating model are introduced as working habits, not abstract ideas;
- leadership receives concrete rollout evidence instead of generic AI-governance claims.

## Canonical client flow

Use this as the default 8-step flow for a first rollout:

1. Frame the goal and boundary for the client/team.
2. Run discovery and technical intake.
3. Choose the VCP track and rigor level.
4. Prepare the customer repo scaffold and agent kit.
5. Run trust-check and identify initial risks.
6. Start an audit backlog and assign ownership.
7. Use PR Gate and release evidence during the pilot sprint.
8. Close with retrospective, reporting, and scale decision.

## Three entry files for client/team adoption

If someone asks, "Where do we actually begin?", point them to these three files first:

1. `START_HERE.md`
2. `docs/client-adoption-playbook.md`
3. `docs/integrations/agent-kits.md`

Why these three:
- `START_HERE.md` chooses the path;
- this playbook shows the rollout lifecycle;
- `docs/integrations/agent-kits.md` shows what to copy into real AI coding environments.

## Stages

### 1. Discovery
- Goal: understand where AI coding is already happening.
- Inputs: active repos, current tools, risk concerns.
- Outputs: adoption package hypothesis and first risk list.
- See: `docs/client-discovery.md`.

### 2. Technical intake
- Goal: review architecture, release flow, tests, and risky zones.
- Inputs: repo map, CI, product context, recent incidents.
- Outputs: intake summary, candidate track, first backlog items.
- See: `docs/technical-intake-workshop.md`.

### 3. Track selection
- Goal: choose the smallest honest VCP route.
- Inputs: maturity, risk, speed pressure, AI usage.
- Outputs: recommended track, rigor level, first artifacts.
- See: `docs/track-selection-for-clients.md`.

### 4. Customer repo scaffold
- Goal: prepare the minimum local control layer.
- Outputs: copied starter files, agent instructions, PR Gate placeholders.
- See: `docs/customer-repo-scaffold.md`.

### 5. AI governance and risk model
- Goal: make allowed / risky / review-required AI usage explicit.
- Outputs: local policy notes, trust-check baseline, backlog categories.

### 6. Sprint operating model
- Goal: fit VCP into real delivery without turning it into ceremony.
- Outputs: small pilot cadence, work-package discipline, review rhythm.

### 7. Executive reporting
- Goal: translate rollout evidence into leadership-readable status.
- Outputs: rollout summary, risk trend, next decision.
- See: `docs/executive-reporting.md`.

### 8. Retrospective and scale
- Goal: decide what should be standardized, simplified, or not scaled.
- Outputs: pilot retrospective and scale/no-scale recommendation.

## First command set

```bash
python3 -m vcp_cli trust-check --json
python3 -m vcp_cli onboard --json
python3 -m vcp_cli agents kit --target copilot --json
```

## Boundary

This is not a hosted governance platform.
It is a local-first operating model, templates, checks, and evidence surfaces for controlled AI development.
