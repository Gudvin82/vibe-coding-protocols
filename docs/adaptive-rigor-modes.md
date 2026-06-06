# Adaptive Rigor Modes

<!-- vcp-version: v0.9.1 -->
<!-- methodology-version: v1.4 -->

Adaptive rigor right-sizes VCP to the situation.

## Modes

### fast
- Use when: tiny changes, quick triage, low-risk clarification.
- Required artifacts: none by default; `trust-check` if public/release surface changed.
- Optional artifacts: change intent.
- Recommended commands: `python3 -m vcp_cli trust-check --json`
- Agent rule profile: nano.
- Minimum proof: clear limitation statement.
- Stop conditions: request touches release/public/risky surfaces without more control.

### standard
- Use when: default project work.
- Required artifacts: change intent, route, basic proof.
- Optional artifacts: charter.
- Recommended commands: `change intent`, `route`, `workflow plan`.
- Agent rule profile: mini.
- Minimum proof: route + validation summary.
- Stop conditions: scope or gate unclear.

### controlled
- Use when: important changes.
- Required artifacts: charter, intent, work package, PR Gate, proof.
- Optional artifacts: evaluator receipt.
- Recommended commands: `charter validate`, `change intent`, `pr-gate explain`, `trust-check`.
- Agent rule profile: mini/full.
- Minimum proof: gate + evidence.
- Stop conditions: human approval absent.

### brownfield
- Use when: existing repo / unclear state.
- Required artifacts: classify, control catalog, starter matrix, audit/backlog awareness.
- Optional artifacts: charter.
- Recommended commands: `classify`, `catalog list`, `backlog report`, `onboard`.
- Agent rule profile: mini.
- Minimum proof: route justification.
- Stop conditions: repo state still unknown.

### launch
- Use when: before demo/release/customer exposure.
- Required artifacts: PR Gate, trust-check, benchmark, launch decision.
- Optional artifacts: evaluator receipt.
- Recommended commands: `pr-gate explain`, `trust-check`, `benchmark run`.
- Agent rule profile: full.
- Minimum proof: release decision + trust-check + limitations.
- Stop conditions: evidence or gate incomplete.

### deep-hardening
- Use when: safety/security/high-risk.
- Required artifacts: full profile, threat/risk model, evidence receipt, human approval.
- Optional artifacts: delivery graph.
- Recommended commands: `trust-check`, `benchmark run`, review artifacts.
- Agent rule profile: full.
- Minimum proof: explicit human acceptance.
- Stop conditions: independent human approval unavailable.
