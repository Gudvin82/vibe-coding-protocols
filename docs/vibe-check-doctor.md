# Vibe-Check Doctor

Use doctor mode when you want a quick toolkit and environment summary.

```bash
bash scripts/vibe-check.sh --doctor
bash scripts/vibe-check.sh --doctor --json
```

## What it reports

- toolkit `VERSION`;
- methodology version;
- git repository presence;
- remote origin;
- checksum manifest presence;
- core tooling availability;
- optional scanner availability;
- recommended route.

## Remote safety

Doctor mode can warn when the remote looks like the source toolkit repository.
That is a reminder to confirm you are not editing or pushing to the template or source repo by mistake.

## Related docs

- [docs/update-copied-artifacts.md](./update-copied-artifacts.md)
- [docs/troubleshooting.md](./troubleshooting.md)
