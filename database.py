import sqlite3
connection = sqlite3.connect("lookism.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS players (
    discord_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    tokens INTEGER DEFAULT 250,
    level INTEGER DEFAULT 1,
    xp INTEGER DEFAULT 0,
    wins INTEGER DEFAULT 0,
    losses INTEGER DEFAULT 0
)
""")
connection.commit()

# Player Functions

def player_exists(discord_id):
    cursor.execute(
        "SELECT 1 FROM players WHERE discord_id = ?",
        (discord_id,)
    )
    return cursor.fetchone() is not None

def create_player(discord_id, username):
    cursor.execute(
        "INSERT INTO players (discord_id, username) VALUES (?, ?)",
        (discord_id, username)
    )
    connection.commit()

def get_player(discord_id):
    cursor.execute(
        "SELECT * FROM players WHERE discord_id = ?",
        (discord_id,)
    )
    return cursor.fetchone()

def update_username(discord_id, username):
    cursor.execute(
        """ UPDATE players
        SET username = ?
        WHERE discord_id = ?
        """,
        (username, discord_id)
    )
    connection.commit()
