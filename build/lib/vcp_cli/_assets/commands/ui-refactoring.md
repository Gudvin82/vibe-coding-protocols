# UI Refactoring Command

Invocation: `/ui-refactoring`

Use when UI code works but pages,
routes
or screens own visual styling that
should belong inside reusable components.

Required inputs:
- target route,
screen,
component set
or frontend area;
- current UI behavior that must stay stable;
- relevant validation command if known.

Component ownership rule:
- component appearance belongs inside the component;
- external code may control semantic variants and layout composition only.

Allowed exceptions:
- documented primitives or headless components;
- slot or polymorphic APIs;
- theme-token layers;
- migration escape hatches with a removal plan;
- third-party wrappers that require `className` or `style`.

Exception safety rules:
- document the exception near the component or design-system docs;
- keep it in the primitives or integration layer,
  not arbitrary page code;
- prefer semantic props and tokens over raw visual overrides;
- if temporary,
  include a constraining or removal plan.

Risk levels:
- Low: move repeated visual fragment into an existing component.
- Medium: extract a new shared component and update several call sites.
- High: redesign shared primitives,
  global theme,
  routing layout
  or accessibility behavior.

Per-file or per-slice loop:
1. Inspect current UI conventions and existing components.
2. Align with the existing design system.
3. Identify visual overrides,
   inline styles,
   duplicated visual fragments
   and local page components.
4. Move visual styling into components.
5. Keep layout styling outside.
6. Simplify props where safe.
7. Validate after each coherent slice.
8. Report what moved,
   what stayed outside
   and which exceptions were retained.

Validation is required after each coherent slice.
Preserve focus,
labels,
keyboard behavior,
loading states,
empty states,
error states
and responsive behavior.

Final report format:
- overall result;
- files or slices inspected;
- ownership problems found;
- visual styling moved into components;
- layout styling kept outside;
- props added,
  simplified
  or removed;
- components extracted or reused;
- allowed exceptions retained;
- why exceptions are safe;
- behavior and accessibility preserved;
- validation run;
- remaining risks;
- suggested commit message.

See [../protocols/maintenance/ui-refactoring.md](../protocols/maintenance/ui-refactoring.md).
