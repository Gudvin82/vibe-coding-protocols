# PyPI Publishing

`v0.8.2` keeps PyPI publication as a manual maintainer action.
It does not claim that VCP is already published publicly.

## What is real in the repository

- local install metadata exists;
- local build/install validation can be run;
- a publication workflow scaffold exists;
- documentation explains the approval path.

## What is not real by default

- no automatic public publication;
- no claim that `pip install vcp-cli` works today;
- no claim that trusted publishing is already configured.

## Safe maintainer checklist

1. Confirm package name availability.
2. Choose token or trusted-publishing setup.
3. Test `python3 -m build` locally if the environment supports it.
4. Publish only after explicit maintainer approval.
5. Update README/docs only after publication is actually live.
