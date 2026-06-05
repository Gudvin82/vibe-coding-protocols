# Validation

Status: sanitized / maintainer-known / no private data

## Commands used

- `python3 -m vcp_cli route --profile public-growth --json`
- `python3 -m vcp_cli spec retrofit --scope public-growth --dry-run --json`
- `python3 -m vcp_cli review-diff --json`
- `python3 -m vcp_cli benchmark run --scenario public-growth-audit`

## What VCP changed

- clarified route choice before editing public surfaces;
- recorded retrofit reasoning instead of relying on chat memory;
- made review, PR Gate, and validation steps explicit;
- made score and trust signals easier to publish without overclaim.

## What was not measured

- no KPI uplift claim;
- no ranking claim;
- no AI citation claim;
- no production conversion metric claim.
