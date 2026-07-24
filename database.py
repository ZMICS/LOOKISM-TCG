import sqlite3
connection = sqlite3.connect("lookism.db")
cursor = connection.cursor()

#players table
cursor.execute("""
CREATE TABLE IF NOT EXISTS players (
    discord_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    tokens INTEGER DEFAULT 250,
    wins INTEGER DEFAULT 0,
    losses INTEGER DEFAULT 0
)
""")

#cards table
cursor.execute("""
CREATE TABLE IF NOT EXISTS cards(
    card_id INTEGER PRIMARY KEY AUTOINCREMENT,
    card_name TEXT NOT NULL,
    rarity TEXT NOT NULL,
    base_hp INTEGER not NULL,
    base_attack INTEGER NOT NULL,
    base_defense INTEGER NOT NULL,
    punch_damage INTEGER NOT NULL,
    kick_damage INTEGER NOT NULL
)
""")

# inventory table

cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory(
    inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    discord_id INTEGER NOT NULL,
    card_id INTEGER NOT NULL,
    level INTEGER DEFAUKT 1,
    xp INTEGER DEFAULT 0,
    FOREIGN KEY(discord_id) REFERENCES players(discord_id),
    FORIEGN KEY(card_id) REFERENCES cards(card_id)
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
        
# Win loss functions

def add_win(discord_id):
    cursor.execute(
        """
        UPDATE players
        SET wins = wins + 1
        WHERE discord_id = ?
        """,
        (discord_id,)
    )
    connection.commit()

def add_loss(discord_id):
    cursor.execute(
        """
        UPDATE players
        SET losses = losses + 1
        WHERE discord_id = ?
        """,
        (discord_id,)
    )
    connection.commit()

def get_stats(discord_id):
    cursor.execute(
        """
        SELECT wins,losses
        FROM players
        WHERE discord_id = ?
        """,
        (discord_id,)
    )
    return cursor.fetchone()