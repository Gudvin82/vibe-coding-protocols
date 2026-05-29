# UI Ownership After

> Synthetic example. Not a real project claim.

## After

- `Card` owns card appearance through semantic props;
- `Button` owns tone and size through semantic props;
- page wrapper keeps grid,
gap
and placement only;
- one documented primitive or third-party slot API remains as a constrained exception.

## Expected validation/report

- UI report explains what moved inside components;
- layout ownership that stays outside is justified;
- retained exception is documented as safe.
