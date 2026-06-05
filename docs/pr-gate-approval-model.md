# PR Gate Approval Model

PR Gate is part of the local launch-control flow.

It helps a team decide whether a change is:
- pass;
- warn;
- block.

## Human review remains required

Examples where human review is required:
- payment or auth paths;
- user data handling;
- release blocker exceptions;
- AI-generated MVP changes with unclear blast radius.

## Use with launch decision

Pair PR Gate with:
- [launch decision checklist](./launch-decision-checklist.md)
- [local platform flow](./local-platform-flow.md)
- [dashboard](./dashboard.md)
