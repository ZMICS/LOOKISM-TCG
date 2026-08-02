#inventory helper functions
from database import (
    create_inventory_entry,
    get_inventory_row,
    get_inventory as db_get_inventory,
    update_quantity,
    delete_inventory_card,
    get_card_quantity,
)

#check if player owns a card
def has_card(discord_id, card_id):
    return get_inventory_row(discord_id, card_id) is not None

#add card to inventory
def add_card(discord_id, card_id):
    if has_card(discord_id, card_id):
        quantity = get_card_quantity(discord_id, card_id)
        update_quantity(discord_id, card_id, quantity + 1)
    else:
        create_inventory_entry(discord_id, card_id)

#remove one copy of card
def remove_card(discord_id, card_id):
    if not has_card(discord_id, card_id):
        return False
    quantity = get_card_quantity(discord_id, card_id)
    if quantity > 1:
        update_quantity(discord_id, card_id, quantity - 1)
    else:
        delete_inventory_card(discord_id, card_id)
    return True

#Get all cards in a player's inventory
def get_inventory(discord_id):
    return db_get_inventory(discord_id)

#Get the quantity of a specific card in a player's inventory
def get_card_quantity(discord_id, card_id):
    row = get_inventory_row(discord_id, card_id)
    if row:
        # inventory_id, discord_id, card_id, quantity, xp, level, upgrade_stage
        return row[3] 
    return 0