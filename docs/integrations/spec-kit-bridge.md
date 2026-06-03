# Spec Kit Bridge

Spec-first tools help define what to build.
VCP helps teams build with AI and ship with control.

VCP works with spec-first and non-spec-first AI workflows.
It is not a clone of spec-first tooling, and it should stay useful when the right answer is no-spec or spec-lite.
It can sit beside spec-first tooling, or operate without it when the project does not need a heavy spec lane.

## Mode 1 — with spec-first tools

- import PRD, feature spec, and tasks into VCP artifacts;
- run spec freshness;
- link tasks into `PROJECT_BACKLOG.md`;
- run `review-diff` before merge;
- run PR Gate and score before release.

## Mode 2 — without full spec-first tooling

- use `no-spec` for tiny low-risk fixes;
- use `spec-lite` for smaller features;
- use `full-spec` or `governed-spec` only when risk requires it.

## Mode 3 — brownfield / retrofit

- capture observed behavior with spec retrofit;
- record gaps;
- use diagnostics and hardening;
- add review gates and release discipline.

## Boundaries

- no claim of official integration;
- no claim of endorsement;
- no subordinate framing such as “use VCP only after Spec Kit”;
- no copied external workflow.
