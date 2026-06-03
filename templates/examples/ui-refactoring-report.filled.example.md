<!-- vcp-artifact: UI_REFACTORING_REPORT_FILLED_EXAMPLE -->
<!-- vcp-version: v0.6.1 -->
<!-- methodology-version: v1.4 -->

# Filled UI Refactoring Report Example

> Synthetic example. Not a real project claim.
> Synthetic example — not a real client or production project.

## Overall result

One UI slice cleaned up with behavior preserved.

## Files/slices inspected

Reviewed the dashboard page,
`FeatureCard`,
`PrimaryButton`
and one low-level slot-based third-party wrapper.

## Component ownership problems found

Before:
- the page assembled final card and button appearance through repeated class overrides;
- visual ownership for padding,
  background,
  radius
  and tone was split across page and component code.

## Visual styling moved into components

After:
- card background,
  padding,
  border radius,
  shadow
  and button tone styling moved into `FeatureCard` and `PrimaryButton`;
- semantic props now express the supported visual variants.

## Layout styling kept outside

Kept page grid layout,
responsive column placement
and external spacing rhythm in the dashboard wrapper.

## Props added/simplified/removed

Added semantic props:
- `variant`
- `tone`
- `fullWidth`

Removed direct cosmetic page-level overrides for padding,
background
and border styling.

## Components extracted/reused

Reused the existing shared button,
and extracted one local promo tile into the shared card component.

## Allowed exceptions retained

Retained one `className` escape hatch on a documented low-level primitive
used by a third-party slot API.

## Why exceptions are safe

The exception stays at the primitive layer,
is documented near the component,
and is not exposed as arbitrary page-level visual composition.
A future cleanup can constrain or remove it without redesigning the page.

## Behavior/accessibility preserved

Preserved keyboard focus,
button semantics,
labels,
loading state,
empty state
and responsive layout behavior.

## Validation run

- `npm run lint`
- `npm run typecheck`
- manual browser check on dashboard route

## Remaining risks

A legacy promo banner still uses old overrides and should be migrated separately.

## Suggested commit message

Move dashboard card/button styling into owned UI components
