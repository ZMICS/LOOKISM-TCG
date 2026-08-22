from database import(
    get_player,
    get_stats, 
    get_tokens,
    get_all_cards
)

from inventory import get_inventory

# Get total cards owned
def get_collection_count(discord_id):
    inventory = get_inventory(discord_id)
    total = 0
    for card in inventory:
        total += card[3]
    return total

# Get total fighter cards
def get_total_fighters(discord_id):
    inventory = get_inventory(discord_id)
    cards = get_all_cards()
    card_data = {}
    for card in cards:
        card_data[card[0]] = card
    total = 0
    for item in inventory:
        card_id = item[2]
        if card_id in card_data:
            card = card_data[card_id]
            if card[2] == "Fighter":
                total += item[3]
    return total

# Get total boost cards
def get_total_boosts(discord_id):
    inventory = get_inventory(discord_id)
    cards = get_all_cards()
    card_data = {}
    for card in cards:
        card_data[card[0]] = card
    total = 0
    for item in inventory:
        card_id = item[2]
        if card_id in card_data:
            card = card_data[card_id]
            if card[2] == "Boost":
                total += item[3]
    return total

# Get player statistics
def get_player_stats(discord_id):
    stats = get_stats(discord_id)
    if stats is None:
        return {
            "wins": 0,
            "losses": 0,
            "total_battles": 0
        }
    wins = stats[0]
    losses = stats[1]
    return {
        "wins": wins,
        "losses": losses,
        "total_battles": wins + losses
    }

# Get strongest card
def get_strongest_card(discord_id):
    inventory = get_inventory(discord_id)
    cards = get_all_cards()
    card_data = {}
    for card in cards:
        card_data[card[0]] = card
    strongest_card = None
    strongest_power = 0
    for item in inventory:
        card_id = item[2]
        if card_id not in card_data:
            continue
        card = card_data[card_id]
        if card[2] != "Fighter":
            continue
        power = card[10]
        if power > strongest_power:
            strongest_power = power
            strongest_card = card
    return strongest_card

# Get strongest card power
def get_strongest_card_power(discord_id):
    card = get_strongest_card(discord_id)
    if card is None:
        return 0
    return card[10]

# Get player level
def get_player_level(discord_id):
    inventory = get_inventory(discord_id)
    if not inventory:
        return 1
    highest_level = 1
    for item in inventory:
        level = item[5]

        if level > highest_level:
            highest_level = level
    return highest_level

# Get collection percentage
def get_collection_percentage(discord_id):
    inventory = get_inventory(discord_id)
    all_cards = get_all_cards()
    total_cards = len(all_cards)
    if total_cards == 0:
        return 0
    unique_owned_cards = len(inventory)
    percentage = (unique_owned_cards / total_cards) * 100
    return round(percentage, 2)

# Get complete player profile
def get_profile(discord_id):
    player = get_player(discord_id)
    if player is None:
        return None
    stats = get_player_stats(discord_id)
    strongest_card = get_strongest_card(discord_id)
    return {
        "username": player[1],
        "tokens": get_tokens(discord_id),
        "wins": stats["wins"],
        "losses": stats["losses"],
        "total_battles": stats["total_battles"],
        "collection_count": get_collection_count(discord_id),
        "fighter_cards": get_total_fighters(discord_id),
        "boost_cards": get_total_boosts(discord_id),
        "strongest_card": (
            strongest_card[1]
            if strongest_card
            else None
        ),
        "strongest_card_power": get_strongest_card_power(discord_id),
        "player_level": get_player_level(discord_id),
        "current_team": None,
        "badges": [],
        "collection_percentage": get_collection_percentage(discord_id)
    }