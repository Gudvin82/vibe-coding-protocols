# npm Wrapper

The npm surface is a local wrapper around the Python CLI.

## What works now

```bash
npm install
npm run vcp -- doctor
npm run vcp -- onboard --json
npm run vcp -- classify --json
npm run vcp -- cards validate
```

## Optional local link

```bash
npm link
vcp doctor
vcp onboard --json
```

## What is not claimed

- no public npm publication unless actually released;
- no public `npx vcp` claim unless actually released;
- no separate Node implementation of VCP logic.
