# Spec Kit Bridge

Spec-first tools help define what to build.
VCP helps teams build with AI and ship with control.

VCP works with spec-first and non-spec-first AI workflows.
It is not a clone of spec-first tooling, and it should stay useful when the right answer is no-spec, spec-lite, brownfield rescue, or release control.
It can sit beside spec-first tooling, or operate without it when the project does not need a heavy spec lane.

## Mode 1 — with spec-first tools

- import product brief, PRD, feature spec, and tasks into VCP artifacts;
- run spec quality gate and spec freshness;
- link tasks into `PROJECT_BACKLOG.md`;
- run `review-diff` before merge;
- run PR Gate and release readiness before release.

## Mode 2 — without full spec-first tooling

- use `no-spec` for tiny low-risk fixes;
- use `spec-lite` for smaller features;
- use Spec Foundation when a new AI-assisted product still needs product clarity;
- use `full-spec` or `governed-spec` only when risk requires it.

## Mode 3 — brownfield / retrofit

- capture observed behavior with spec retrofit;
- record gaps and architecture drift;
- use diagnostics, hardening, and PR Gate;
- add release readiness before tagging.

## Boundaries

- no vendoring;
- no copied external workflow;
- no claim of official integration;
- no claim of endorsement;
- no subordinate framing such as “use VCP only after Spec Kit”.
