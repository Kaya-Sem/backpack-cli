CREATE TABLE collections (
    id SERIAL PRIMARY KEY,
    description TEXT,
    name TEXT NOT NULL
);

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    description TEXT,
    name TEXT NOT NULL,
    image TEXT,
    weight INTEGER CHECK (weight >= 0),
    price INTEGER CHECK (weight >= 0)
);


CREATE TABLE collection_items (
    id SERIAL PRIMARY KEY,
    collection_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    FOREIGN KEY (collection_id) REFERENCES collections(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);
