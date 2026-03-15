---
name: spec-bundle
description: 'Build an implementation-ready spec bundle when a plain PRD is no longer enough: minimum useful contracts, schema, test plan, blueprint, gates, ADRs, boundaries, and GitHub-ready task breakdown. Use when ambiguity or architecture risk would otherwise slow execution.'
---

# Spec Bundle

## Metadata
- Trigger when: a plain PRD is too soft and the implementation needs contracts, schema, test planning, or architecture boundaries to move safely.
- Do not use when: a short brief is enough and extra artifacts would be paperwork theater.

## Skill Purpose

Create only the spec artifacts that materially reduce ambiguity, rework, or review pain so implementation can start from clear contracts and gates instead of vibes.

## Instructions
1. Decide the smallest honest bundle first: core bundle, architecture pack, and optional ADRs only when the risk profile justifies them. If scaffolding helps, use `/Users/nick/.codex/skills/spec-bundle/scripts/init_bundle.py` with the appropriate flags. Use `/Users/nick/.codex/skills/spec-bundle/references/bundle-shape.md` only when you need the exact shape.
2. Fill only the artifacts that change implementation quality: `prd.md`, `contracts.md`, `schema.sql`, `test-plan.md`, `epics.md`, and only add `blueprint.md`, `gate-matrix.md`, or `adr/` when architecture risk, gating, or irreversible decisions make them worth keeping.
3. Validate traceability and consistency. Contracts must point to consuming tasks, gates must name blocking evidence, and bundle artifacts must be updated together when requirements or architecture move.

## Non-Negotiable Acceptance Criteria
- One source of truth per concern: scope, contracts, DB shape, validation, and task breakdown stay separated.
- Architecture pack artifacts exist only when the risk is real.
- Local/cloud boundaries are explicit when they matter.
- If an artifact would be fake theater, leave it out or mark it intentionally deferred.

## Output
- The created or updated bundle artifacts on disk.
- A short note on bundle size: core only, architecture pack, or architecture pack plus ADRs.
- Any unresolved gate or assumption that still blocks clean implementation.
- `Next skill options` (only if needed): `$justdoit` — convert the bundle into a live execution plan; `$adr-log` — capture an irreversible architectural choice; `$issue-control-loop` — move the bundle into a durable GitHub issue workflow; `$agx-orchestrator` — dispatch bounded execution after the bundle is stable.
