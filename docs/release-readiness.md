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
- [ ] no fake metrics
- [ ] no fake case study
- [ ] no guaranteed security claims
- [ ] tag points to the final commit
- [ ] release object created manually
