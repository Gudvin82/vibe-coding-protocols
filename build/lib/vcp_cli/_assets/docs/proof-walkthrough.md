# Proof Walkthrough

This page shows a clean proof path from unclear AI-assisted repository state to a more controlled VCP state.

The goal is trust clarity, not hype.

## Initial state

An AI-assisted project exists, but readiness is unclear.
There may be code, docs, or workflows, but trust surfaces are incomplete.

## VCP flow

1. `python3 -m vcp_cli evaluate`
2. `python3 -m vcp_cli route --profile production --json` or `python3 -m vcp_cli diagnose --json`
3. `python3 -m vcp_cli review-diff --json`
4. `python3 -m vcp_cli score --json`
5. `python3 -m vcp_cli adopt --pack production --dry-run --json`
6. add PR Gate
7. publish local score badge if the repository owner wants a visible signal

## Output to expect

- risks found;
- route and pack choice made explicit;
- artifacts created or linked;
- validation run;
- what remains unknown;
- what VCP does not guarantee.
- no invented KPI uplift;
- no fake before/after claim.

## Proof boundary

This walkthrough is a trust-oriented adoption path.
It is not a guarantee of production safety, compliance, ranking, AI citation, or business KPI uplift.

## Labels to preserve

- `synthetic`
- `sanitized`
- `maintainer-known`
- `real`

Never upgrade proof language beyond the evidence actually present.
