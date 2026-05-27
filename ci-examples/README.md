# CI Examples

These files are examples, not a promise of full product support
for every CI platform.

Use them as a starting point and adapt them to your own:
- repository layout;
- shell image;
- dependency setup;
- validation gates.

Included examples:
- `gitlab-ci.yml`
- `circleci-config.yml`
- `bitbucket-pipelines.yml`

Each example keeps the flow minimal:
- check out the repository;
- run `bash scripts/vibe-check.sh --audit`;
- run `python3 scripts/validate-links.sh`;
- run `bash scripts/scan-placeholders.sh`.
