CREATE TABLE usage_records (
    id BIGSERIAL PRIMARY KEY,
    api_key TEXT NOT NULL,
    path TEXT NOT NULL,
    status_code INTEGER NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX usage_records_key_time ON usage_records (api_key, created_at);
