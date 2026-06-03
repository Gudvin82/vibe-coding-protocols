# 2-minute VCP demo

## What this demo shows

- evaluate the repo;
- inspect AI-readable index/cards;
- classify task/spec depth;
- review current diff;
- generate score badge.

## Commands

```bash
python3 -m vcp_cli evaluate
python3 -m vcp_cli cards list --recommended
python3 -m vcp_cli spec depth --task "add payment webhook"
python3 -m vcp_cli review-diff
python3 -m vcp_cli score --badge markdown
```

## Expected result

You should understand:

- what VCP covers;
- which workflow applies;
- what gates are required;
- what readiness score can be published.

## Optional GIF / terminal recording

No fake demo artifact is committed by default.

Recommended manual recording:
- asciinema
- terminalizer
- Kap / Screen Studio / native screen recording

Recommended output:
- `assets/demo/vcp-2min-demo.cast`
- `assets/demo/vcp-2min-demo.gif`

Visual overview: `docs/visual-overview.md`
