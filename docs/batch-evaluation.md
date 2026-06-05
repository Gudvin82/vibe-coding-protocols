# Batch Evaluation

VCP batch evaluation is local and non-mutating.

```bash
python3 -m vcp_cli batch evaluate --targets ./targets.txt --json
```

Behavior:
- evaluates multiple target directories locally;
- no network;
- no mutation;
- per-target results plus aggregate summary;
- missing targets fail clearly;
- `--fail-fast` is optional.
