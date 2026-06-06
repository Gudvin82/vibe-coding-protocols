# Control Spine

<!-- vcp-version: v0.9.1 -->
<!-- methodology-version: v1.4 -->

VCP Control Spine is the canonical product spine for controlled AI-assisted delivery.

Tiny spine:

`Charter -> Intent -> Plan -> Gate -> Proof`

Full spine:

`Intake -> Charter -> Intent -> Route -> Plan -> Work Package -> Gate -> Proof -> Release Decision -> Maintain`

## Stages

### Intake
- Purpose: classify the situation before AI work expands.
- Input: user request, repo state, risk context.
- Output artifact: intake notes or route recommendation.
- Related command: `python3 -m vcp_cli classify --json`
- Required: yes for brownfield/launch/deep-hardening.
- Typical risks: skipping context, reading random files first.

### Charter
- Purpose: define project control rules.
- Input: project governance expectations.
- Output artifact: charter report or `.vcp/project-control-charter.example.json` style payload.
- Related command: `python3 -m vcp_cli charter validate .vcp/project-control-charter.example.json --json`
- Required: controlled / launch / deep-hardening.
- Typical risks: unclear ownership and approval boundaries.

### Intent
- Purpose: capture what changes and why before AI edits code.
- Input: user request / product need.
- Output artifact: change intent report or `.vcp/change-intent.example.json`.
- Related command: `python3 -m vcp_cli change intent --json`
- Required: standard and above.
- Typical risks: code starts before scope is explicit.

### Route
- Purpose: select the right guided path.
- Input: repo/project state.
- Output artifact: route recommendation.
- Related command: `python3 -m vcp_cli route --profile production --json`
- Required: standard and above.
- Typical risks: wrong path, wrong rigor.

### Plan
- Purpose: shape the next safe work slice.
- Input: route + intent + charter.
- Output artifact: adoption/workflow plan.
- Related command: `python3 -m vcp_cli workflow plan --id mvp-to-launch --json`
- Required: standard and above.
- Typical risks: jumping from request straight to mutation.

### Work Package
- Purpose: define the auditable execution unit.
- Input: plan + affected surfaces.
- Output artifact: work package record.
- Related docs: `docs/work-package-lifecycle.md`
- Required: controlled / launch / deep-hardening.
- Typical risks: no owner, no evidence target, no review checklist.

### Gate
- Purpose: decide what must pass before merge/release.
- Input: work package + diff + risks.
- Output artifact: PR Gate / review-accept-merge record.
- Related command: `python3 -m vcp_cli pr-gate explain --json`
- Required: controlled / launch / deep-hardening.
- Typical risks: unreviewed medium/high-risk changes.

### Proof
- Purpose: make claims auditable.
- Input: validation outputs, benchmark, receipt, trust-check.
- Output artifact: proof snapshot / evaluation receipt.
- Related command: `python3 -m vcp_cli evaluator receipt --json`
- Required: all public/release-facing work.
- Typical risks: overclaim, stale numbers, missing limits.

### Release Decision
- Purpose: decide if exposure is acceptable.
- Input: gate + proof + known limits.
- Output artifact: launch/release decision.
- Related docs: `docs/launch-decision-checklist.md`
- Required: launch and release.
- Typical risks: demo/release without evidence.

### Maintain
- Purpose: keep control surfaces current after release.
- Input: backlog, retro, incidents, drift.
- Output artifact: backlog / retrospective / maintenance follow-up.
- Related command: `python3 -m vcp_cli backlog report --json`
- Required: ongoing operation.
- Typical risks: drift after initial adoption.
