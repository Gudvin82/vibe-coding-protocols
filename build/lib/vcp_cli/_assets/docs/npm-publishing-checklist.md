# npm Publishing Checklist

Use this checklist before claiming public npm or `npx` support.

## Current status

Public npm and `npx` distribution are planned.
Current npm support is local wrapper only.

## Readiness checks

- package name selected and confirmed available;
- `bin` points to `bin/vcp-node.js`;
- version matches the repository package;
- `license` exists;
- `repository` exists;
- `homepage` exists;
- `bugs` URL exists;
- keywords are present and relevant;
- package file list is intentionally scoped;
- `npm pack --dry-run` reviewed;
- `npm link` tested locally;
- `npm run vcp -- doctor` tested;
- `npm run vcp -- evaluate` tested;
- Windows wrapper path tested;
- README wording is honest about publication status.

## Do not claim yet unless true

Do not claim any of the following unless publication really happened:
- `npx vcp` works from the public registry;
- `npm install -g` works from a published package;
- package page exists and is maintained;
- semver support expectations are stable in the public registry.

## Suggested publish rehearsal

```bash
npm install
npm run vcp -- doctor
npm run vcp -- evaluate
npm run vcp -- manifest validate
npm pack --dry-run
npm link
vcp doctor
```

## Related docs

- [npm.md](./npm.md)
- [cli.md](./cli.md)
- [known-limitations.md](./known-limitations.md)
- [public-proof-roadmap.md](./public-proof-roadmap.md)
