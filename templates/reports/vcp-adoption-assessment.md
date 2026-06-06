<!-- vcp-version: v0.9.3 -->
<!-- methodology-version: v1.4 -->
<!-- vcp-version: v0.8.4 -->

<!-- vcp-version: v0.8.2 -->

<!-- vcp-artifact: REPORT_VCP_ADOPTION_ASSESSMENT -->
<!-- vcp-version: v0.8.2 -->

# VCP Adoption Assessment

## Target project classification

State whether the target is a new project, existing MVP, existing production system, regulated or sensitive system, shared engine, maintenance target, UI ownership target, or public-site readiness target.

## Production and risk signals

List user exposure, payments, personal data, compliance, public API, shared engine, legal or security claim signals that affected the route decision.

## Selected route

Name the route and explain why it fits better than the nearest alternative.

## Selected adoption pack

Name the adoption pack and list why it matches the target project stage and risk level.

## Files inspected

List the VCP files actually inspected before making the recommendation.

## Files recommended

List the files to copy, adapt or reference first. Keep the list scoped.

## Files intentionally skipped

List files not recommended for this target and explain why they were skipped.

## Stop conditions to add

List stop conditions the target project should add before AI edits continue.

## Architecture / project map needs

State whether `PROJECT_MAP.md`, `ARCHITECTURE_MAP.md` or `ARCHITECTURE_SOURCE_OF_TRUTH.md` are needed and why.

## Security / hardening needs

State the minimum hardening, disclosure, release-gate or security-scope artifacts needed.

## Maintenance / refactoring needs

State whether a maintenance pass is needed now, later or not at all.

## Public site readiness needs

State whether public docs, site trust, AI crawler readiness or schema/checklist work is relevant.

## Validation plan

List the smallest meaningful validation commands or evidence required before adoption is considered safe.

## Missing context

List missing project facts that limit confidence.

## Confidence

Use one of: `High`, `Medium`, `Low`.
If confidence is `Low` or `Medium` because key context is missing, do not present the recommendation as final.

## Next action

State the next smallest safe step.

## Suggested commit message

Provide a commit message only if the adoption recommendation includes a concrete copy or docs-update step.
