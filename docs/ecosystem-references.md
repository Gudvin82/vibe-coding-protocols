# Ecosystem References

These references are for positioning, architecture inspiration, and contribution discipline, not copied content.

## Spec-first tooling reference

Useful pattern:
- specs before implementation;
- PRD / feature / task lifecycle;
- CLI bootstrap for structured planning.

Boundary:
- do not copy brand, flow, claims, or file names;
- do not claim compatibility;
- do not claim executable implementation generation unless implemented.

## Workflow automation reference

Useful pattern:
- trigger;
- steps;
- action;
- output;
- validation.

Boundary:
- VCP workflows are a local guidance/catalog layer;
- VCP is not a workflow automation platform and does not clone Zapier/Pipedream behavior.

## Layer diagnostics reference

Useful pattern:
- layer-by-layer checks;
- evidence;
- likely reason;
- next action.

Boundary:
- diagnostics stay local and repository/process-oriented;
- VCP is not a network, censorship, or production-monitoring diagnostic tool.

## Catalog UX reference

Useful pattern:
- platform badges;
- filters;
- recommended markers;
- metadata-first discovery.

Boundary:
- VCP is not an app catalog;
- VCP uses cards and manifests to navigate a delivery framework, not a marketplace.

## Event schema reference

Useful pattern:
- severity;
- timestamp;
- source;
- evidence;
- redaction status.

Boundary:
- VCP event records are generic workflow artifacts;
- VCP does not claim SIEM/IDS/IPS compatibility and does not add offensive/security engine behavior.

## Packaging note

Use ecosystem references to understand organization patterns, not to borrow maturity claims.
Do not imply that a local wrapper equals a published package or a stable registry distribution.
