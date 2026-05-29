# UI Ownership Before

> Synthetic example. Not a real project claim.

## Problem

A page assembles final button and card appearance with local utility classes,
inline overrides
and ad hoc spacing tweaks.

## Why it is risky

Visual identity is split across the page and components.
New screens will likely repeat the same drift.

## VCP route

UI Component Ownership.

## Before

- `Card` gets background/radius/shadow from the page;
- `Button` gets tone and padding overrides from the page;
- layout and appearance are mixed together.
