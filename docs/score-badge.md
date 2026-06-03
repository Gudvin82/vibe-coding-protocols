# Score Badge

`vcp score --badge` generates a local readiness badge string from the current repository score.

It is not a security certification, marketplace listing, or third-party audit.

## Commands

```bash
python3 -m vcp_cli score --badge
python3 -m vcp_cli score --badge markdown
python3 -m vcp_cli score --badge json
```

## Output modes

- `--badge`
  - local text summary with score, status, and generated badge URL
- `--badge markdown`
  - Markdown image snippet for README or docs
- `--badge json`
  - machine-readable score, status, and badge URL

## Example

```md
![VCP Score](https://img.shields.io/badge/VCP_score-86%2F100-yellow)
```

The URL is generated locally. The command does not call `shields.io`.
