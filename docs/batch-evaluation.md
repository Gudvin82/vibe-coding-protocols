# Batch Evaluation

VCP batch evaluation is local and non-mutating.

```bash
python3 -m vcp_cli batch evaluate --targets ./targets.txt --json
```

Use when you have multiple AI-generated MVPs or multiple packages in a workspace and want a summary without mutating targets.

## Expected output

- per-target result;
- aggregate summary;
- failed or missing targets called out explicitly;
- warnings or not-run reasons when applicable.

## Boundaries

- local only;
- no network;
- no mutation;
- no recursive scanning outside the target list.
