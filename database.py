import sqlite3
connection = sqlite3.connect("lookism.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS players (
    discord_id INTEGER PRIMARY KEY,
    username TEXT,
    tokens INTEGER DEFAULT 250
)
""")
connection.commit()
def player_exists(discord_id):
    cursor.execute(
        "SELECT * FROM players WHERE discord_id = ?",
        (discord_id,)
    )
    return cursor.fetchone() is not None
def create_player(discord_id, username):
    cursor.execute(
        "INSERT INTO players (discord_id, username) VALUES (?, ?)",
        (discord_id, username)
    )
    connection.commit()