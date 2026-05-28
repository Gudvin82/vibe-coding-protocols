# UI Refactoring Command

Invocation: `/ui-refactoring`

Use when UI code works but pages, routes or screens own visual styling that
should belong inside reusable components.

Required inputs:
- target route, screen, component set or frontend area;
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

Per-file or per-slice loop:
1. Inspect current UI conventions and existing components.
2. Identify visual overrides, inline styles, duplicated visual fragments
   and local page components.
3. Move visual styling into components.
4. Keep layout styling outside.
5. Simplify props where safe.
6. Validate after each coherent slice.
7. Report what moved, what stayed outside and which exceptions were retained.

Validation is required after each coherent slice.

Final report format:
- overall result;
- files or slices inspected;
- ownership problems found;
- visual styling moved into components;
- layout styling kept outside;
- props added, simplified or removed;
- components extracted or reused;
- allowed exceptions retained;
- why exceptions are safe;
- behavior and accessibility preserved;
- validation run;
- remaining risks;
- suggested commit message.

See [../protocols/maintenance/ui-refactoring.md](../protocols/maintenance/ui-refactoring.md).
