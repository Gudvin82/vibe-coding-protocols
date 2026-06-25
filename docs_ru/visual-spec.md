# Visual spec

Repository package: `v0.9.5`

Используйте этот spec, если Codex-generated SVG получился недостаточно сильным визуально или если позже нужен отдельный ChatGPT image generation pass.

## Общий стиль

- clean modern technical diagram;
- white или very light background;
- dark navy/charcoal text;
- blue/purple accent;
- rounded rectangles;
- arrows;
- GitHub README friendly;
- читаемость на 1200px width;
- no logos;
- no photorealism;
- no mascot;
- no clutter.

## Diagram 1: VCP control layer map

Purpose:
- показать practical control flow от raw AI MVP до trust-check и proof.

Aspect ratio:
- 1600x900

Used in:
- README
- evaluator architecture docs
- website hub

## Diagram 2: VCP product model

Purpose:
- быстро объяснить Core, Guided Paths, Optional Layers и Roadmap-only.

Aspect ratio:
- 1600x1000

Used in:
- README
- product model docs
- website hub

## Diagram 3: VCP comparison map

Purpose:
- не дать shallow evaluator спутать категорию VCP.

Aspect ratio:
- 1600x900

Used in:
- README
- comparisons docs
- website anti-misread section

## Prompt for ChatGPT image generation

Use the prompts from `docs/visual-spec.md` directly if you need an English image-generation pass.

## Optional square social preview

- 1200x1200
- fewer labels
- for social or docs hub preview surfaces
