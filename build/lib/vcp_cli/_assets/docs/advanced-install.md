# Advanced Install

Use this page only when the review-first setup from
[README.md](../README.md) is not enough.

The main path for real projects remains:

```bash
curl -fsSL https://raw.githubusercontent.com/Gudvin82/vibe-coding-protocols/main/scripts/init-minimal.sh -o init-minimal.sh
curl -fsSL https://raw.githubusercontent.com/Gudvin82/vibe-coding-protocols/main/SHA256SUMS -o SHA256SUMS
less init-minimal.sh
bash init-minimal.sh --starter
```

## Checksum verification

Linux:

```bash
grep "scripts/init-minimal.sh" SHA256SUMS > init-minimal.sha256
sha256sum -c init-minimal.sha256
```

macOS:

```bash
grep "scripts/init-minimal.sh" SHA256SUMS > init-minimal.sha256
shasum -a 256 init-minimal.sh
```

## Fast track for empty or test repositories only

```bash
curl -fsSL https://raw.githubusercontent.com/Gudvin82/vibe-coding-protocols/main/scripts/init-minimal.sh | bash -s -- --starter
```

Do not use `curl | bash` for production, client-facing or otherwise
untrusted third-party intake.

## Install hooks locally

```bash
bash scripts/install-hooks.sh --mode starter
```

Use hooks as a local guardrail, not as a substitute for review.
