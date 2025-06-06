CREATE_DATABASE_PASSWORDS = """
CREATE TABLE
    IF NOT EXISTS passwords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        login TEXT NOT NULL,
        password TEXT NOT NULL,
        time_to_change DATETIME,
        extra TEXT,
        profile_id INTEGER,
        FOREIGN KEY (profile_id) REFERENCES profiles (id) ON DELETE CASCADE);
"""

CREATE_DATABASE_PROFILE = """
CREATE TABLE
    IF NOT EXISTS profile (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        service_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        phone TEXT,
        email_password TEXT NOT NULL
        );
"""
