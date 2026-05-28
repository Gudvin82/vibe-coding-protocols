# Release Readiness

Before publishing a release:

- [ ] `VERSION` updated
- [ ] `CHANGELOG.md` updated
- [ ] release notes created
- [ ] `SHA256SUMS` updated
- [ ] `bash scripts/check-version-consistency.sh` passed
- [ ] `python3 scripts/check-newlines.py` passed
- [ ] `bash scripts/vibe-check.sh --audit --json` passed
- [ ] script tests passed
- [ ] example tests passed
- [ ] release gates reviewed in `docs/hardening-thresholds.md`
- [ ] no fake metrics
- [ ] no fake real case study
- [ ] no guaranteed security claims
- [ ] tag points to the final commit
- [ ] release object created manually

## Status language

Use one of these when summarizing readiness:
- `READY`
- `READY WITH RISKS`
- `BLOCKED`
- `NOT ASSESSED`

## Reminder

A release can be technically tidy and still require risk acceptance.
Do not turn a clean markdown/tooling pass into a fake production guarantee.
