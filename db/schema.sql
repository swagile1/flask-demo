DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name TEXT NOT NULL,
    location TEXT NOT NULL
);

INSERT INTO users (name, location)
    VALUES
        ("Shane", "Oregon"),
        ("Loreli", "California"),
        ("Dana", "British Columbia"),
        ("Remi", "British Columbia"),
        ("Mike", "British Columbia");
