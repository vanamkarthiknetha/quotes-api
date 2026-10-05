CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    born INTEGER,
    bio TEXT NOT NULL DEFAULT '',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE quotes (
    id SERIAL PRIMARY KEY,
    author_id INTEGER NOT NULL REFERENCES authors(id),
    text TEXT NOT NULL,
    likes INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
