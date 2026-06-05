# Example: Finding Intentionally Not Changed

Synthetic example. Not a real project claim.

## Situation

A maintenance task extracted repeated UI formatting logic into a shared helper.

## Reviewer finding

Non-blocking suggestion:
- move all formatting helpers into a new `shared/ui-formatting/` package.

## Why it was not changed

The active scope was one screen-level cleanup.
Creating a new package would expand scope, move multiple unrelated call sites, and require a broader architecture decision.

## What changed instead

- extracted only the duplicated helper used by the touched screen;
- added a focused regression test for the formatted output.

## Remaining risk

The broader formatting ownership question still exists.
It is documented as follow-up maintenance work, not hidden.

## Acceptance

Accepted because:
- the finding was not blocking;
- the requested larger change was outside scope;
- validation passed;
- the remaining risk was documented.
