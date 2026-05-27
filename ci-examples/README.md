# CI Examples

These CI examples are secondary.
The canonical self-dogfooding workflow is GitHub Actions in `.github/workflows/vibe-check.yml`.

Use these files as examples and adapt them to your own:
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
