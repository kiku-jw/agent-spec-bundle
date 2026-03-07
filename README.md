# Agent Spec Bundle

`Agent Spec Bundle` is a small public kit for turning a loose PRD into something an engineering agent can actually build from.

The point is simple:

- PRD explains the product.
- A bundle explains the implementation shape.

This repo gives you both:

- a reusable `spec-bundle` skill
- a scaffold script
- a compact set of templates for the artifacts that usually matter

## What is inside

- `SKILL.md` — the skill itself
- `scripts/init_bundle.py` — scaffold a new bundle folder
- `references/bundle-shape.md` — when each artifact is worth keeping
- `assets/templates/` — starter files for:
  - `prd.md`
  - `contracts.md`
  - `schema.sql`
  - `test-plan.md`
  - `epics.md`

## Quick start

```bash
python3 scripts/init_bundle.py --out ./spec/live2reels --project-name "Live2Reels"
```

That creates:

- `prd.md`
- `contracts.md`
- `schema.sql`
- `test-plan.md`
- `epics.md`

Use only the files that reduce ambiguity. This is not a paperwork hobby.

## When this is useful

Use a full bundle when:

- the work will span sessions
- more than one system or repo is involved
- another agent or reviewer will touch it
- contracts, schema, or background jobs matter
- you want GitHub-ready tasks instead of rethinking the project every time

Skip the full bundle when a short brief is enough.

## Why this exists

A lot of “AI PRDs” read nicely and still leave the implementer guessing.

The missing pieces are usually boring but decisive:

- request/response shapes
- queue and job states
- data model
- acceptance criteria
- epic breakdown

That is what this kit is trying to make easier.
