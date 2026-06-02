# Known Limitations

## Improved in v0.5.2

- manifest files are moved out of the repository root into `.vcp/manifests/`;
- README and onboarding path are shorter and easier to scan;
- a local npm wrapper exists for shorter Node-first commands;
- `vcp init` gives a guidance-first starting step.

## Still limited

- legacy Bash script parity on native Windows is not complete;
- VCP does not automatically review vendor terms or legal compatibility;
- VCP does not auto-connect or test external APIs;
- VCP does not provide real API monitoring integration;
- authenticated GitHub Release creation still depends on external auth tooling;
- npm distribution is local-wrapper-only until a real published package exists.
