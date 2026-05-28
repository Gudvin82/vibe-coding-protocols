# Care Refactoring Command

Invocation: `/care-refactoring`

Use when an existing project works but is becoming hard to maintain,
risky to extend, duplicated, inconsistent or difficult to reason about.

Required inputs:
- target area, module, route or file set;
- current behavior that must stay stable;
- relevant validation command if known.

Agent behavior:
1. Read repository instructions and relevant architecture or project-map docs.
2. Check git status before editing.
3. Do discovery first.
4. Propose at most 1 to 3 small scopes.
5. Classify proposed work as low, medium or high risk.
6. Run the challenge checkpoint before production edits.
7. Add or reuse characterization coverage when proportional.
8. Make the smallest useful behavior-preserving change.
9. Run the smallest meaningful validation.
10. Return a scoped final report.

Challenge checkpoint is required.
Characterization tests are required before risky behavior-preserving moves
when they are proportional.

High-risk maintenance changes should default to narrow scope,
separate product task,
or escalation into Hardening or Extended review.

Final report format:
- overall result;
- risk level;
- escalation decision;
- scopes inspected;
- challenge decision;
- scope changed;
- preserved behavior and contracts;
- characterization coverage;
- validation run;
- remaining risks;
- suggested commit message.

See [../protocols/maintenance/care-refactoring.md](../protocols/maintenance/care-refactoring.md).
