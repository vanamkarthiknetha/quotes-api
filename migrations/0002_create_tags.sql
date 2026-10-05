CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL DEFAULT ''
);

CREATE TABLE quote_tags (
    quote_id INTEGER NOT NULL REFERENCES quotes(id),
    tag_id INTEGER NOT NULL REFERENCES tags(id),
    PRIMARY KEY (quote_id, tag_id)
);
