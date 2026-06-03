# Spec Kit Bridge

Spec-first tools help define what to build.
VCP helps govern how AI-assisted changes move safely toward merge and production.

VCP is not a clone of spec-first tooling.
It should stay useful when the right answer is no-spec or spec-lite.

## Use VCP after spec-first planning

- import PRD, feature spec, and tasks into VCP spec artifacts;
- run spec freshness;
- link tasks into `PROJECT_BACKLOG.md`;
- run `review-diff` before merge;
- run diagnostics and release checks before shipping.

## Use VCP without full spec-first tooling

- `no-spec` for tiny low-risk fixes;
- `spec-lite` for smaller features;
- `full-spec` or `governed-spec` only when risk requires it.

## Use VCP for brownfield projects

- capture observed behavior with spec retrofit;
- record gaps;
- harden the repo;
- add review gates and release discipline.

## Boundaries

- no claim of official integration;
- no claim of endorsement;
- no aggressive replacement framing;
- no copied external workflow.
