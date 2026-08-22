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

# Set card quantity
def set_quantity(discord_id, card_id, quantity):
    if quantity <= 0:
        delete_inventory_card(discord_id, card_id)
    else:
        update_quantity(discord_id, card_id, quantity)

# Increase card quantity
def increase_quantity(discord_id, card_id, amount=1):
    quantity = get_card_quantity(discord_id, card_id)
    set_quantity(discord_id, card_id, quantity + amount)

# Decrease card quantity
def decrease_quantity(discord_id, card_id, amount=1):
    quantity = get_card_quantity(discord_id, card_id)
    new_quantity = quantity - amount
    if new_quantity <= 0:
        delete_inventory_card(discord_id, card_id)
    else:
        update_quantity(discord_id, card_id, new_quantity)

# Delete card completely
def delete_card(discord_id, card_id):
    delete_inventory_card(discord_id, card_id)

# Search inventory
def search_inventory(discord_id, card_name):
    inventory = db_get_inventory(discord_id)
    results = []
    for card in inventory:
        if card_name.lower() in str(card).lower():
            results.append(card)
    return results

# Sort inventory
def sort_inventory(discord_id, key=None):
    inventory = db_get_inventory(discord_id)
    if key is None:
        return inventory
    return sorted(inventory, key=key)

# Filter inventory
def filter_inventory(discord_id, filter_function):
    inventory = db_get_inventory(discord_id)
    return list(filter(filter_function, inventory))