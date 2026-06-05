# Run State and Checkpoints

Run state exists to make longer local evaluations resumable and reviewable.

Files:
- `.vcp/runs/README.md`
- `.vcp/runs/example-run-state.json`

Dashboard behavior:
- summarize `.vcp/runs/*.json` when present;
- label example-only history clearly if only the example file exists;
- never imply a background daemon or scheduler.

This is a local file model only.
No daemon, scheduler, or background worker is shipped.
