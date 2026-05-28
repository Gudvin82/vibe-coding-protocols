# AI Project Extended Protocol

Use this route when the project is public, client-facing, production-bound,
or handles auth, payments or personal data.

## Step 1. Architecture Source of Truth

Create or update `ARCHITECTURE_SOURCE_OF_TRUTH.md`.
If the project has multiple surfaces, also create `ARCHITECTURE_MAP.md` first.
Make sure the detailed document covers:
- main flows;
- integrations;
- storage and deploy path;
- known risks and constraints.

## Step 2. Security Baseline

Add `SECURITY_BASELINE.md` and confirm that auth, secrets,
public exposure and supply-chain notes are explicit.

## Step 3. Third-Party Registry

Track external APIs, repositories, packages and hosted services
in `THIRD_PARTY_REGISTRY.md`.
Prefer current official docs over model memory when dependencies are updated.

## Step 4. Perimeter / Auth Abuse checklist

Run the perimeter and auth abuse checklists for:
- public exposure;
- login abuse;
- admin routes;
- high-risk endpoints.

## Step 5. Incident Recovery Runbook

Add `INCIDENT_RECOVERY_RUNBOOK.md` before calling the project production-ready.

## Step 6. Metrics Board

Use `METRICS_BOARD.md` if you want to track real workflow signals.
Do not invent numbers.

## Step 7. CI vibe-check --audit

Add `bash scripts/vibe-check.sh --audit` to CI.
Use `--strict` only when warning-level drift should fail the gate.

## Step 8. Accepted risks

Document unresolved risks in `AUDIT_BACKLOG.md`
or in an accepted-risks section before deploy.

## Exit criteria

- Architecture Source of Truth exists and is actionable.
- Architecture Map exists when multiple surfaces or stack choices need quick orientation.
- Security baseline exists and is not empty.
- Third-party registry is present.
- Incident runbook exists.
- `vibe-check --audit` is green enough for the chosen route.
- Accepted risks are explicit.
