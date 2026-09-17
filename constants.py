"""
constants.py
Central place for LOOKISM TCG game constants.
"""

STARTING_TOKENS = 250

# Card leveling
MAX_CARD_LEVEL = 10
XP_PER_LEVEL = 100

# 5% stat increase per level after level 1
LEVEL_STAT_BONUS = 0.05

# Battle
MIN_DAMAGE = 1

WIN_XP_REWARD = 50
LOSS_XP_REWARD = 20

WIN_TOKEN_REWARD = 50
LOSS_TOKEN_REWARD = 10

# Rarities
RARITY_COMMON = "Common"
RARITY_UNCOMMON = "Uncommon"
RARITY_RARE = "Rare"
RARITY_EPIC = "Epic"
RARITY_LEGENDARY = "Legendary"

RARITIES = [
    RARITY_COMMON,
    RARITY_UNCOMMON,
    RARITY_RARE,
    RARITY_EPIC,
    RARITY_LEGENDARY,
]

# Deck
MIN_DECK_SIZE = 1
MAX_DECK_SIZE = 5

# Battle limit
MAX_BATTLE_ROUNDS = 100