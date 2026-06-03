# Demo Script

This file is for reproducible terminal capture later.
It is not a claim that a GIF or video already exists.

## 2-minute demo

```bash
python3 -m vcp_cli evaluate
python3 -m vcp_cli cards list --recommended
python3 -m vcp_cli spec depth --task "add payment webhook"
python3 -m vcp_cli review-diff
python3 -m vcp_cli score --badge markdown
```

## What to say while recording

- VCP is a foundation and trust layer for AI-assisted product delivery.
- `evaluate` explains what the repository actually contains.
- `cards list --recommended` narrows discovery without reading the whole repo.
- `spec depth` shows whether the change needs no-spec, spec-lite, full-spec, or governed-spec.
- `review-diff` checks risk before merge.
- `score --badge markdown` produces a local readiness signal, not certification.

## Optional capture formats

Recommended tools:
- asciinema
- terminalizer
- Kap / Screen Studio / native screen recording

Recommended future filenames:
- `assets/demo/vcp-2min-demo.cast`
- `assets/demo/vcp-2min-demo.gif`

If no capture file exists, describe this as a demo script, not a demo GIF.
