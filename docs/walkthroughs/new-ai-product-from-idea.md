# New AI Product From Idea

This walkthrough is a fictional but realistic example of the New Project Track.

Example product:

`Customer appointment portal for a small service business.`

## Initial idea

The founder wants a simple customer-facing booking portal with confirmation messages and an internal staff dashboard.

## AI intake

Initial route signals:

- customer-facing product;
- persistence and notifications likely;
- not a toy task;
- release discipline needed before public launch.

## Spec depth decision

Recommended depth:

- `full-spec` moving to `governed-spec` once auth, notifications, and customer data are confirmed.

## Question engine output

Key questions:

- who are the primary users: customers, staff, admins;
- what data is stored;
- what notifications are sent;
- what counts as success for first release;
- what is explicitly out of scope.

## Product brief

A short product brief defines:

- the problem;
- the primary user;
- first release scope;
- non-goals;
- constraints.

## PRD / feature spec outline

Main areas:

- appointment creation;
- time-slot availability;
- internal staff management;
- confirmation flow;
- validation and rollout plan.

## Acceptance criteria

Examples:

- customers can create appointments only in available time slots;
- staff can confirm and cancel appointments;
- duplicate booking is prevented;
- validation covers booking edge cases.

## Tasks

- define data model;
- implement booking flow;
- implement staff confirmation flow;
- add validation tests;
- prepare release-readiness checklist.

## Backlog entries

Backlog captures:

- MVP booking flow;
- notification follow-up;
- internal dashboard improvements;
- release and review tasks.

## Architecture memory

Project memory records:

- booking domain;
- actor model;
- persistence assumptions;
- public surface implications;
- release notes path.

## First review gate

Before merge:

- run validation;
- check architecture memory;
- run review-diff;
- review PR Gate implications.

## Release readiness notes

Before public launch:

- version surfaces must align;
- rollout and rollback notes must exist;
- dependency and notification assumptions must be visible.

## What VCP does not guarantee

- VCP does not guarantee product-market fit;
- it does not guarantee correct AI implementation;
- it does not replace product judgment or release ownership.
