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
    base_hp INTEGER NOT NULL,
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
    quantity INTEGER DEFAULT 1,
    level INTEGER DEFAULT 1,
    xp INTEGER DEFAULT 0,
    upgrade_stage INTEGER DEFAULT 1,
    FOREIGN KEY(discord_id) REFERENCES players(discord_id),
    FOREIGN KEY(card_id) REFERENCES cards(card_id)
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
        (discord_id,)
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

def set_tokens(discord_id, amount):
    cursor.execute(
        """
        UPDATE players
        SET tokens = ?
        WHERE discord_id = ?
        """,
        (amount, discord_id)
    )
    connection.commit()
        
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

# Card Functions

def create_card(card_name, rarity, base_hp, base_attack, base_defense, punch_damage, kick_damage):
    cursor.execute(
        """
        INSERT INTO cards (card_name, rarity, base_hp, base_attack, base_defense, punch_damage, kick_damage)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (card_name, rarity, base_hp, base_attack, base_defense, punch_damage, kick_damage)
    )
    connection.commit()

def get_card(card_id):
    cursor.execute(
        "SELECT * FROM cards WHERE card_id = ?",
        (card_id,)
    )
    return cursor.fetchone()

def get_all_cards():
    cursor.execute(
        "SELECT * FROM cards"
    )
    return cursor.fetchall()

def get_card_by_name(card_name):
    cursor.execute(
        "SELECT * FROM cards WHERE card_name = ?",
        (card_name,)
    )
    return cursor.fetchone()

def update_card(card_id, hp, attack, defense, punch_damage, kick_damage):
    cursor.execute(
        """
        UPDATE cards
        SET base_hp = ?, base_attack = ?, base_defense = ?, punch_damage = ?, kick_damage = ?
        WHERE card_id = ?
        """,
        (hp, attack, defense, punch_damage, kick_damage, card_id)
    )
    connection.commit()

def delete_card(card_id):
    cursor.execute(
        "DELETE FROM cards WHERE card_id = ?",
        (card_id,)
    )
    connection.commit()

# Inventory Functions

def create_inventory_entry(discord_id, card_id):
    cursor.execute(
        """
        INSERT INTO inventory (discord_id, card_id)
        VALUES (?, ?)
        """,
        (discord_id, card_id)
    )
    connection.commit()

def get_inventory_row(discord_id, card_id):
    cursor.execute(
        "SELECT * FROM inventory WHERE discord_id = ? AND card_id = ?",
        (discord_id, card_id)
    )
    return cursor.fetchone()

def get_inventory(discord_id):
    cursor.execute("SELECT * FROM inventory WHERE discord_id = ?", (discord_id,))
    return cursor.fetchall()

def get_card_quantity(discord_id, card_id):
    cursor.execute(
        "SELECT quantity FROM inventory WHERE discord_id = ? AND card_id = ?",
        (discord_id, card_id)
    )
    result = cursor.fetchone()
    if result:
        return result[0]

    return 0

def update_quantity(discord_id, card_id, quantity):
    cursor.execute(
        "UPDATE inventory SET quantity = ? WHERE discord_id = ? AND card_id = ?",
        (quantity, discord_id, card_id)
    )
    connection.commit()

def update_inventory_xp(discord_id, card_id, xp):
    cursor.execute(
        "UPDATE inventory SET xp = ? WHERE discord_id = ? AND card_id = ?",
        (xp, discord_id, card_id)
    )
    connection.commit()

def update_inventory_level(discord_id, card_id, level):
    cursor.execute(
        "UPDATE inventory SET level = ? WHERE discord_id = ? AND card_id = ?",
        (level, discord_id, card_id)
    )
    connection.commit()

def update_upgrade_stage(discord_id, card_id, stage):
    cursor.execute(
        "UPDATE inventory SET upgrade_stage = ? WHERE discord_id = ? AND card_id = ?",
        (stage, discord_id, card_id)
    )
    connection.commit()

def delete_inventory_card(discord_id, card_id):
    cursor.execute(
        "DELETE FROM inventory WHERE discord_id = ? AND card_id = ?",
        (discord_id, card_id)
    )
    connection.commit()

# Database helpers

def save_database():
    connection.commit() 

def close_database():
    connection.close()