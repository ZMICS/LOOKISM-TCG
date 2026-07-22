import sqlite3
connection = sqlite3.connect("lookism.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS players (
    discord_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    tokens INTEGER DEFAULT 250,
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

    #Token functions
    
def get_tokens(discord_id):
    cursor.execute(
        "SELECT tokens FROM players WHERE discord_id = ?",
        (discord_id)
    )
    result = cursor.fetchone()
    if result:
         return result[0]
    return None
 
def add_tokens(discord_id, amount):
    cursor.execute(
        """
        UPDATE players
        SET tokens = tokens + ?
        WHERE discord_id = ?
        """,
        (amount, discord_id)
    )
    connection.commit()

def spend_tokens(discord_id, amount):
    current_tokens = get_tokens(discord_id, )
    if current_tokens is None:
        return False
    if current_tokens < amount:
        return False
    cursor.execute(
        """
        UPDATE players
        SET tokens = tokens - ?
        WHERE discord_id = ?
        """,
        (amount, discord_id)
    )
    connection.commit()
    return True
        

