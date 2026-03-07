-- {{PROJECT_NAME}} schema
-- Replace placeholders with real tables, relationships, and indexes.

BEGIN;

CREATE TABLE IF NOT EXISTS example_entities (
    id TEXT PRIMARY KEY,
    status TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS example_entities_status_idx
    ON example_entities(status);

COMMIT;
