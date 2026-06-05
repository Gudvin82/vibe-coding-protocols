# Maintenance Refactor Before

> Synthetic example. Not a real project claim.

## Problem

A working internal module mixes controller logic,
validation,
business rules
and SDK calls in one file.

## Why it is risky

The next feature will likely copy the same mixed-responsibility pattern.
Behavior is hard to verify quickly.

## VCP route

Maintenance Refactoring.

## Before

- one large module;
- duplicated conditional rules;
- no obvious owner layer;
- behavior only understandable by reading multiple unrelated helpers.

## Expected validation/report

- scoped `refactoring-report.md`;
- focused characterization test or equivalent validation path;
- preserved contracts called out explicitly.
