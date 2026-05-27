## What changed

## Why

## Checklist

- [ ] I did not add real secrets
- [ ] I did not add fake metrics
- [ ] I did not claim guaranteed security
- [ ] I updated docs if needed
- [ ] I ran checks

## Validation

```bash
bash scripts/check-toolkit.sh
bash scripts/scan-placeholders.sh
python3 scripts/validate-links.sh
bash scripts/vibe-check.sh --help
```
