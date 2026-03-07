# Bundle Shape

Use this reference when the user wants a real agent-ready build packet rather than a loose PRD.

## What belongs in the bundle

Keep it compact. The default bundle has five files:

1. `prd.md`
2. `contracts.md`
3. `schema.sql`
4. `test-plan.md`
5. `epics.md`

Not every project needs all five. Include only what reduces confusion.

## File-by-file guidance

### `prd.md`

Use for:

- product goal
- scope and non-goals
- user flow
- hard constraints
- success criteria

Good sign:

- a developer can explain what must exist in v1 and what is intentionally out

Bad sign:

- the document reads like launch copy or investor language

### `contracts.md`

Use for:

- API shapes
- IPC / event payloads
- queue/job states
- background-worker inputs and outputs
- external integration boundaries

Good sign:

- another developer can implement against this file without guessing the payload shape

Bad sign:

- it repeats the PRD in prose and has no concrete request/response/state detail

### `schema.sql`

Use for:

- real tables
- relationships
- enum/state columns
- indexes that matter to the first version

Good sign:

- it answers “what will actually be persisted and how is it linked?”

Bad sign:

- the project has meaningful persistence but the data model only exists in your head

### `test-plan.md`

Use for:

- acceptance criteria
- high-value happy paths
- failure modes
- fixtures or sample inputs that matter

Good sign:

- review can check the result against explicit behavior instead of vibes

Bad sign:

- it says “write tests” but does not say what must be true

### `epics.md`

Use for:

- GitHub-ready breakdown
- phase order
- dependencies
- “done means …” for each chunk

Good sign:

- the work can be split into issues without rethinking the whole project

Bad sign:

- the breakdown is either one giant blob or fifty micro-tasks with no narrative

## When a full bundle is worth it

Prefer a full bundle when at least two are true:

- work will span sessions
- more than one repo/system is involved
- rollout or security risk exists
- a second agent or reviewer will touch it
- the project has meaningful data/contracts/background jobs
- the task will likely become a public artifact or reusable product

## When a brief is enough

Skip the full bundle when:

- the work is tiny and reversible
- no durable data or contract exists
- one developer can finish it in one sitting without handoff
- the missing clarity is tactical, not architectural

## Quality bar

The bundle is ready when:

- a coder knows what to build
- a reviewer knows how to judge it
- a future you can reopen it in a week and still trust it

If it does not achieve those three things, shorten it or sharpen it.
