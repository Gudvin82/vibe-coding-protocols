# Proof Layer

The VCP proof layer is the structure that turns repository claims into bounded, inspectable evidence.

It exists so VCP can show what it helped detect, what it helped prevent, and what is still unknown without inventing proof.

## Proof labels

Every substantial proof surface should declare one or more of:
- `real`
- `sanitized`
- `maintainer-known`
- `synthetic`
- `template`

## What a stronger proof layer should show

- before state or initial operating condition;
- route decision and why that route was selected;
- commands actually run;
- artifacts created or recommended;
- risks surfaced;
- what VCP prevented or slowed down on purpose;
- validation evidence;
- remaining unknowns.

## What VCP may say honestly

VCP may say:
- which control gaps were made visible;
- which adoption slice was recommended;
- which checks were added;
- which actions were kept non-destructive;
- which parts of a case remain synthetic or sanitized.

## What VCP must not say

VCP must not:
- invent independent adopters;
- invent before/after metrics;
- imply production safety certification;
- imply SEO/GEO/AI visibility guarantees;
- hide that a case is synthetic, sanitized, or maintainer-known.

## Proof path for first-time readers

Use together:
- `docs/proof-pack.md`
- `docs/mvp-to-launch-path.md`
- `docs/demos/raw-ai-mvp-to-controlled-launch.md`
- `docs/mvp-adoption-track.md`
- `docs/launch-decision-checklist.md`
- `case-studies/README.md`
- `templates/reports/adoption-case-study.md`
