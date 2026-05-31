## What changed

## Why

## Route or pack affected

## Review gate impact

## Checklist

- [ ] I did not add real secrets
- [ ] I did not add fake metrics
- [ ] I did not claim guaranteed security
- [ ] I updated docs if needed
- [ ] I updated manifests if references changed
- [ ] I updated benchmarks if route logic changed
- [ ] I ran local checks

## Validation

```bash
python3 scripts/check-newlines.py
python3 scripts/validate-links.sh
bash scripts/check-version-consistency.sh
bash scripts/check-toolkit.sh
bash scripts/vibe-check.sh --audit --json
python3 -m vcp_cli --help
python3 -m vcp_cli manifest validate
python3 -m vcp_cli benchmark run
```
