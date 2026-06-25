# Visual Spec

Repository package: `v0.9.4`

Use this spec when Codex-generated SVGs are not visually strong enough or when a later ChatGPT image generation pass should produce polished diagram assets.

## Shared style

- clean modern technical diagram;
- white or very light background;
- dark navy/charcoal text;
- blue/purple accent;
- rounded rectangles;
- directional arrows;
- README-friendly contrast;
- readable at 1200px width;
- no logos;
- no photorealism;
- no mascot;
- no clutter.

## Diagram 1: VCP control layer map

Purpose:
- show the practical control flow from raw AI MVP to trust-check and proof.

Text labels:
- Raw AI MVP / Existing Project
- onboard / classify
- workflow plan
- adopt plan / PR Gate
- metrics / dashboard
- launch decision / trust-check

Layout:
- vertical flow with one box per stage and clear downward arrows.

Colors:
- deep navy text;
- blue accent arrows;
- pale violet or blue stage boxes.

Aspect ratio:
- 1600x900

Used in:
- README
- evaluator architecture docs
- website hub

Prompt for ChatGPT image generation:
```text
Create a clean modern technical diagram on a very light background. Use dark navy text, blue and soft purple accents, rounded rectangles, and simple arrows. No logos, no mascots, no clutter.

Title: VCP control layer map

Show a vertical flow with these labels in order:
1. Raw AI MVP / Existing Project
2. onboard / classify
3. workflow plan
4. adopt plan / PR Gate
5. metrics / dashboard
6. launch decision / trust-check

Make it GitHub README friendly, readable at 1200px width, and export-ready at 1600x900.
```

## Diagram 2: VCP product model

Purpose:
- explain Core, Guided Paths, Optional Layers, and Roadmap-only at a glance.

Text labels:
- Core: CLI, version surfaces, trust-check, benchmark report, manifests/tests
- Guided Paths: 10-minute path, MVP-to-Launch, spec-driven adoption, SaaS hardening
- Optional Layers: dashboard, project memory, audit backlog, integration packs, agent templates
- Roadmap-only: hosted dashboard, VS Code extension, marketplace, PyPI/npm publication if not actually done

Layout:
- 4-column or 4-lane diagram.

Colors:
- each lane gets a subtle distinct accent;
- roadmap-only should look intentionally softer/dimmer.

Aspect ratio:
- 1600x1000

Used in:
- README
- product model docs
- website hub

Prompt for ChatGPT image generation:
```text
Create a clean technical product model diagram with four vertical lanes on a very light background. Use dark navy text, subtle blue and purple accents, rounded rectangles, and clear grouping. No logos, no clutter.

Lane 1 title: Core
Items: CLI, version surfaces, trust-check, benchmark report, manifests/tests

Lane 2 title: Guided Paths
Items: 10-minute path, MVP-to-Launch, spec-driven adoption, SaaS hardening

Lane 3 title: Optional Layers
Items: dashboard, project memory, audit backlog, integration packs, agent templates

Lane 4 title: Roadmap-only
Items: hosted dashboard, VS Code extension, marketplace, PyPI/npm publication if not actually done

Make it readable at 1200px width and export-ready at 1600x1000.
```

## Diagram 3: VCP comparison map

Purpose:
- prevent shallow category confusion.

Text labels:
- Spec Kit = what to build
- Full-stack templates = where to build
- AI agents = generate/edit code
- VCP = control what AI built

Layout:
- 4-box comparison map with VCP visually emphasized as the control layer.

Colors:
- one accent color per category;
- VCP should be the strongest accent.

Aspect ratio:
- 1600x900

Used in:
- README
- comparisons docs
- website anti-misread section

Prompt for ChatGPT image generation:
```text
Create a clean modern comparison diagram on a very light background with four rounded boxes and concise labels. Use dark navy text, blue/purple accents, no logos, no clutter, no photorealism.

Boxes:
- Spec Kit = what to build
- Full-stack templates = where to build
- AI agents = generate/edit code
- VCP = control what AI built

Visually emphasize the VCP box as the control layer without making it flashy. Make it GitHub README friendly and export-ready at 1600x900.
```

## Optional square social preview

- aspect ratio: 1200x1200
- use the product model or control map with fewer labels
- intended for social or docs hub preview surfaces
