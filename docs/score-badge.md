# Score Badge

`vcp score --badge` generates a local readiness badge string from the current repository score.

It is not a security certification, marketplace listing, or third-party audit.

## Commands

```bash
python3 -m vcp_cli score --badge markdown
python3 -m vcp_cli score --badge json
```

## Output modes

- `--badge markdown`
  - Markdown image snippet for README or docs
- `--badge json`
  - machine-readable score, status, and badge URL

## Example

```md
![VCP Score](https://img.shields.io/badge/VCP_score-100%2F100-brightgreen)
```

## Important warnings

- score badge is not a security certification;
- score is a local readiness signal;
- score depends on checks present in the repo.

The URL is generated locally. The command does not call `shields.io`.
