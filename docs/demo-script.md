# Demo Script

This file is for reproducible terminal capture later.
It is not a claim that a GIF or video already exists.

## 30-second demo

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli evaluate
python3 -m vcp_cli route --profile production
python3 -m vcp_cli adopt --pack production --dry-run
python3 -m vcp_cli backlog report
python3 -m vcp_cli score
```

## Public Growth demo

```bash
python3 -m vcp_cli route --profile public-growth
python3 -m vcp_cli adopt --pack public-growth --dry-run
```

## Backlog demo

Use dry-run only:

```bash
python3 -m vcp_cli backlog add --title "Demo item" --type idea --priority P3 --dry-run
python3 -m vcp_cli backlog report
```

## Capture guidance

Possible tools:
- asciinema
- terminalizer
- OBS plus terminal crop

Recommended future filenames:
- `assets/demo/vcp-30s-demo.gif`
- `assets/demo/vcp-30s-demo.cast`

If no capture file exists, describe this as a demo script, not a demo GIF.

Related:
- [quickstart-walkthrough.md](./quickstart-walkthrough.md)
