-- Space Fort PBC / Animal Scrypt / Madken — Stage 1 Minimal Schema
-- Compatible with SQLite (local-first) and Supabase / PostgreSQL

CREATE TABLE IF NOT EXISTS companions (
    id TEXT PRIMARY KEY,
    owner_id TEXT NOT NULL,
    name TEXT NOT NULL,
    chassis_spec_json TEXT NOT NULL, -- JSON: proportion, translucent_tint, optic_accent, stage
    authored_lore TEXT NOT NULL,     -- Immutable character lore; separated from user facts
    voice_constraints_json TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS memory_records (
    id TEXT PRIMARY KEY,
    companion_id TEXT NOT NULL REFERENCES companions(id) ON DELETE CASCADE,
    category TEXT NOT NULL CHECK (category IN ('interest', 'project', 'routine', 'observation')),
    content TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('PROPOSED', 'APPROVED', 'DELETED')),
    visibility TEXT NOT NULL CHECK (visibility IN ('PRIVATE', 'FRAGMENT_CANDIDATE')),
    created_at TEXT NOT NULL,
    approved_at TEXT
);

CREATE TABLE IF NOT EXISTS fragment_exchanges (
    id TEXT PRIMARY KEY,
    memory_id TEXT NOT NULL REFERENCES memory_records(id) ON DELETE CASCADE,
    sender_companion_id TEXT NOT NULL REFERENCES companions(id),
    recipient_companion_id TEXT NOT NULL REFERENCES companions(id),
    shared_summary TEXT NOT NULL,
    sender_approved INTEGER NOT NULL DEFAULT 0,
    recipient_approved INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL,
    approved_at TEXT,
    revoked_at TEXT
);

CREATE TABLE IF NOT EXISTS ritual_objects (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    participants_json TEXT NOT NULL, -- JSON array of companion IDs
    state TEXT NOT NULL CHECK (state IN ('DORMANT', 'RESONATING', 'CRYSTALLIZED')),
    vitality_points INTEGER NOT NULL DEFAULT 0,
    continuity_log_json TEXT NOT NULL DEFAULT '[]',
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS capability_leases (
    id TEXT PRIMARY KEY,
    granter_companion_id TEXT NOT NULL REFERENCES companions(id),
    grantee_user_id TEXT NOT NULL,
    worker_role TEXT NOT NULL CHECK (worker_role IN ('archivist', 'researcher', 'reminder', 'steward_readonly')),
    scope_description TEXT NOT NULL,
    expires_at TEXT NOT NULL,
    revoked INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS royalty_ledger (
    id TEXT PRIMARY KEY,
    parent_companion_id TEXT NOT NULL REFERENCES companions(id),
    child_companion_id TEXT NOT NULL REFERENCES companions(id),
    creator_id TEXT NOT NULL,
    buyer_id TEXT NOT NULL,
    gross_amount_cents INTEGER NOT NULL CHECK (gross_amount_cents >= 0),
    creator_royalty_cents INTEGER NOT NULL CHECK (creator_royalty_cents >= 0),
    platform_fee_cents INTEGER NOT NULL CHECK (platform_fee_cents >= 0),
    net_settlement_cents INTEGER NOT NULL CHECK (net_settlement_cents >= 0),
    settlement_mode TEXT NOT NULL DEFAULT 'SIMULATED_TEST_LEDGER',
    created_at TEXT NOT NULL
);
