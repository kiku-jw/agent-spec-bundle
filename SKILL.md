---
name: spec-bundle
description: Build an implementation-ready spec bundle for an agent: not just a PRD, but the minimum useful set of contracts, schema, test plan, boundaries, and GitHub-ready task breakdown.
---

# Spec Bundle

Use this skill when a plain PRD is no longer enough.

Typical prompts:

- `собери пакет для агента`
- `сделай implementation-ready spec`
- `PRD мало, нужен полный bundle`
- `добавь contracts / schema / test plan`
- `разложи это в bundle, который можно отдавать Codex`

## What to do

1. Decide first if a full bundle is honest.
   - For small or reversible work, a short brief is enough.
   - Use a bundle only when extra artifacts will reduce ambiguity, rework, or review pain.
2. If the bundle is warranted, scaffold it:

```bash
python3 scripts/init_bundle.py --out /absolute/path/to/spec-bundle --project-name "Project Name"
```

3. Fill only the artifacts that change implementation quality:
   - `prd.md`
   - `contracts.md`
   - `schema.sql`
   - `test-plan.md`
   - `epics.md`
4. Make the bundle ready for action, not for admiration.

## When to read the reference

If you need the exact bundle shape, when to include each artifact, or what good output looks like, read:

- `references/bundle-shape.md`

## Rules

- Do not turn this into paperwork religion.
- A bundle exists to remove ambiguity, not to sound senior.
- Keep one source of truth per thing: scope in `prd.md`, contracts in `contracts.md`, DB shape in `schema.sql`, validation in `test-plan.md`, breakdown in `epics.md`.
- Always make the local/cloud boundary explicit when it matters.
- If an artifact would be fake theater, leave it out or mark it as intentionally deferred.
