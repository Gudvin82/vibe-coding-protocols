# Artifact Versioning

Copy-ready templates include lightweight version markers so you can tell whether a copied file may be stale.

## Marker format

```html
<!-- vcp-artifact: AGENTS -->
<!-- vcp-version: v0.2.0 -->
<!-- methodology-version: v1.4 -->
```

## Why these markers exist

- copied files drift over time;
- local project customizations are normal;
- users still need a low-friction way to compare old copies with newer toolkit releases.

## How to update local artifacts

1. Compare your local file with the latest template.
2. Keep project-specific edits that still matter.
3. Bring over workflow, wording or structure updates that improve clarity.
4. Update the marker only after review.

## If the file is heavily customized

Do not overwrite it blindly.
Treat the template as a reference and port only the changes that still fit your project.

## Comparing `templates/AGENTS.md` with a local `AGENTS.md`

Start with:
- Stop Conditions
- Memory Bank read order
- token-aware discovery guidance
- approval gates
- reporting expectations

The goal is not to make every copied file identical.
The goal is to make drift visible and reviewable.
