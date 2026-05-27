# Artifact Versioning

Copy-ready templates in this repository include lightweight version markers.

Example:

```html
<!-- vcp-artifact: AGENTS -->
<!-- vcp-version: v0.1.11 -->
<!-- methodology-version: v1.4 -->
```

## Why these markers exist

They help answer simple maintenance questions:
- Was this file copied from VCP at all?
- Which repository package version did it come from?
- Was it aligned with methodology `v1.4` at the time?

## How to update local artifacts

1. Compare your local file with the current template.
2. Copy only the parts you still want.
3. Keep your project-specific rules and ownership notes.
4. Update the `vcp-version` marker after review.

Do not overwrite a heavily customized project file blindly.

## If the file is heavily customized

That is normal.

Treat the VCP template as a reference baseline:
- compare structure;
- compare missing safeguards;
- copy only useful improvements;
- keep project-specific operational details private.

## Comparing `templates/AGENTS.md` with a local `AGENTS.md`

A practical workflow:
- open `templates/AGENTS.md` from this repository;
- open your project's `AGENTS.md`;
- diff stop conditions, Memory Bank files and approval gates;
- keep local ownership, deploy and security details;
- update the marker only after the review is complete.

## How `vibe-check` uses markers

`vibe-check` treats missing or older markers as a warning, not a failure.

That is intentional:
- projects may customize artifacts deeply;
- version drift does not always mean the file is wrong;
- the goal is review visibility, not forced replacement.
