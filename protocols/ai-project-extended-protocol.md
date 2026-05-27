# AI Project Extended Protocol

Use when the project is public, client-facing, production-bound, or handles auth, payments or personal data.

## Step 1. Architecture Source of Truth

Create or update `ARCHITECTURE_SOURCE_OF_TRUTH.md`.
Make sure the document covers the main flows, integrations, storage, deploy path and known risks.

## Step 2. Security Baseline

Add `SECURITY_BASELINE.md` and confirm that auth, secrets, public exposure and supply-chain notes are explicit.

## Step 3. Third-Party Registry

Track external APIs, repositories, packages and hosted services in `THIRD_PARTY_REGISTRY.md`.

## Step 4. Perimeter / Auth Abuse checklist

Run the perimeter and auth abuse checklists for public exposure, login abuse and high-risk routes.

## Step 5. Incident Recovery Runbook

Add `INCIDENT_RECOVERY_RUNBOOK.md` before calling the project production-ready.

## Step 6. Metrics Board

Use `METRICS_BOARD.md` if you want to track real adoption and workflow signals.
Do not invent numbers.

## Step 7. CI vibe-check --audit

Add `bash scripts/vibe-check.sh --audit` to CI.
Use `--strict` only when warning-level drift should fail the gate.

## Step 8. Accepted risks

Document unresolved risks in `AUDIT_BACKLOG.md` or an accepted-risks section before deploy.

## Exit criteria

- Architecture Source of Truth exists and is actionable.
- Security baseline exists and is not empty.
- Third-party registry is present.
- Incident runbook exists.
- `vibe-check --audit` is green enough for the chosen route.
- Accepted risks are explicit.
