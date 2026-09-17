"""
levels.py
Card leveling logic for the LOOKISM TCG bot.
"""

from constants import MAX_CARD_LEVEL, XP_PER_LEVEL, LEVEL_STAT_BONUS
def xp_required_for_level(level):
    """Total XP required to reach a level."""
    if level <= 1:
        return 0

    return min(
        level - 1,
        MAX_CARD_LEVEL - 1
    ) * XP_PER_LEVEL

def get_level_from_xp(xp):
    """Calculate a card's level from its total XP."""
    xp = max(0, xp)

    level = (xp // XP_PER_LEVEL) + 1

    return min(level, MAX_CARD_LEVEL)

def xp_until_next_level(level, xp):
    """Return how much XP is needed for the next level."""
    if level >= MAX_CARD_LEVEL:
        return 0

    required = xp_required_for_level(level + 1)

    return max(0, required - xp)

def calculate_level_up(old_level, new_xp):
    """
    Return:
        (new_level, leveled_up)
    """
    new_level = get_level_from_xp(new_xp)
    new_level = max(old_level, new_level)
    return new_level, new_level > old_level


def get_stat_multiplier(level):
    """Return the stat multiplier for a card level."""

    level = max(1, min(level, MAX_CARD_LEVEL))

    return 1 + ((level - 1) * LEVEL_STAT_BONUS)

def get_scaled_stats(base_hp, base_attack, base_defense, level):
    """
    Scale a card's base stats according to its level.
    Returns:
        {
            "hp": ...,
            "attack": ...,
            "defense": ...
        }
    """

    multiplier = get_stat_multiplier(level)
    return {
        "hp": round(base_hp * multiplier),
        "attack": round(base_attack * multiplier),
        "defense": round(base_defense * multiplier),
    }