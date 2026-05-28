# UI Component Ownership Protocol

Use when frontend or UI code works but styling ownership is unclear,
pages or routes are full of visual hardcoding, components rely on caller
overrides, or design consistency is degrading.

## Core principle

A component owns its own visual styling.
External code may control:
- semantic component modes;
- layout composition.

External code must not control component appearance through cosmetic overrides.

## Decision rule

- if a style describes how the component looks, move it inside the component;
- if a style describes where the component sits among other elements,
  keep it in a layout wrapper.

## Bad practices and refactor targets

- passing style, className, inline CSS or utility classes to change component appearance;
- splitting visual definition between component and caller;
- wrappers overriding padding, color, background, border, radius, shadow,
  typography or dimensions;
- using a component as an unfinished visual base assembled at call site;
- duplicating visual rules across pages;
- CSS-mirroring props such as padding, background, borderRadius, shadow
  or borderColor when they define visual identity;
- local page components that should be reusable components.

## Target architecture

- pages, screens and routes are composition layers;
- components are visually self-contained;
- layout wrappers own layout only;
- semantic props express product-level variants.

Examples of semantic props:
- `variant`
- `size`
- `tone`
- `state`
- `colorScheme`
- `fullWidth`
- `disabled`

Layout wrappers may own:
- direction;
- gap or spacing when it describes external rhythm;
- flex or grid behavior;
- alignment or justification;
- responsive placement;
- positioning.

## Allowed exceptions

Allowed exceptions may include:
- low-level design primitives;
- headless UI components;
- documented slot APIs;
- polymorphic components;
- theme providers and design tokens;
- migration layers with an explicit removal plan;
- one-off third-party integration wrappers where the external API requires `className` or `style`.

Rules for exceptions:
- exceptions must be documented near the component or in design-system docs;
- exceptions must not become arbitrary page-level styling;
- page or route code still should not assemble final component appearance ad hoc;
- prefer semantic props and tokens over raw cosmetic overrides;
- any retained `className` or `style` escape hatch must explain why it exists
  and when it should be removed or constrained.

## Workflow

Work slice by slice:
- inspect the current UI system and conventions;
- check existing components before creating new ones;
- identify style overrides, inline styles, class assembly,
  repeated visual fragments and local page components;
- split styling into visual ownership vs layout composition;
- move visual styling into components;
- keep layout outside;
- simplify APIs;
- remove harmful style, className or cosmetic pass-through props where safe;
- preserve behavior;
- validate after each file or coherent slice.

## Behavior preservation

Do not change:
- product behavior;
- data flow;
- permissions;
- routing;
- persistence;
- business logic;
- interactions;
- accessibility behavior;
- loading states;
- empty states;
- error states;
- responsive behavior.

## Validation

Run the smallest meaningful validation:
- formatter;
- typecheck;
- lint;
- unit test;
- component test;
- build;
- browser, screenshot or manual check when appropriate.

If validation fails, fix it before moving on.

## Per-file or per-slice report

Include:
- what was wrong before;
- what visual styling moved inside components;
- what stayed outside as layout;
- props added, simplified or removed;
- local components moved into `components/` or shared UI layers;
- exceptions retained and why they are safe;
- why the result is cleaner;
- validation run;
- remaining risks.

## Avoid

- broad visual redesign;
- changing product behavior;
- leaving temporary override mechanisms;
- creating duplicate components when an existing component can be extended;
- weakening design system primitives;
- the smallest textual diff that still leaves ownership unclear.
