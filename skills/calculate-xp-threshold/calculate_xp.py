#!/usr/bin/env python3
"""
Calculate XP thresholds for D&D 5e encounters based on 2024 rules.

This script calculates the experience points (XP) threshold for an encounter
based on the party's level, size, and desired difficulty.
"""

import argparse
import random

# XP thresholds per character by level (2024 D&D rules)
XP_THRESHOLDS_BY_LEVEL = {
    1: {"easy": 25, "medium": 50, "hard": 75, "deadly": 100},
    2: {"easy": 50, "medium": 100, "hard": 150, "deadly": 200},
    3: {"easy": 75, "medium": 150, "hard": 225, "deadly": 300},
    4: {"easy": 125, "medium": 250, "hard": 375, "deadly": 500},
    5: {"easy": 250, "medium": 500, "hard": 750, "deadly": 1100},
    6: {"easy": 300, "medium": 600, "hard": 900, "deadly": 1400},
    7: {"easy": 350, "medium": 750, "hard": 1100, "deadly": 1700},
    8: {"easy": 450, "medium": 900, "hard": 1400, "deadly": 2100},
    9: {"easy": 550, "medium": 1100, "hard": 1600, "deadly": 2400},
    10: {"easy": 600, "medium": 1200, "hard": 1900, "deadly": 2800},
    11: {"easy": 800, "medium": 1600, "hard": 2400, "deadly": 3600},
    12: {"easy": 1000, "medium": 2000, "hard": 3000, "deadly": 4500},
    13: {"easy": 1100, "medium": 2200, "hard": 3400, "deadly": 5100},
    14: {"easy": 1250, "medium": 2500, "hard": 3800, "deadly": 5700},
    15: {"easy": 1400, "medium": 2800, "hard": 4300, "deadly": 6400},
    16: {"easy": 1600, "medium": 3200, "hard": 4800, "deadly": 7200},
    17: {"easy": 2000, "medium": 3800, "hard": 5700, "deadly": 8500},
    18: {"easy": 2100, "medium": 4200, "hard": 6300, "deadly": 9500},
    19: {"easy": 2400, "medium": 4800, "hard": 7200, "deadly": 10900},
    20: {"easy": 2800, "medium": 5600, "hard": 8400, "deadly": 12500},
}

# Monster count scaling factors for encounter scaling (2024 D&D rules)
MONSTER_COUNT_SCALING_FACTORS = {
    1: 1.0,
    2: 1.5,
    3: 2.0,
    4: 2.0,
    5: 2.0,
    6: 2.0,
    7: 2.5,
    8: 2.5,
    9: 2.5,
    10: 2.5,
    11: 3.0,
    12: 3.0,
    13: 3.0,
    14: 3.0,
    15: 4.0,
    16: 4.0,
    17: 4.0,
    18: 4.0,
    19: 4.0,
    20: 4.0,
}


def calculate_xp_threshold(
    party_level: int,
    party_size: int,
) -> dict:
    """
    Calculate the XP thresholds for all difficulty levels.

    Args:
        party_level: The level of the characters in the party (1-20)
        party_size: The number of characters in the party

    Returns:
        A dictionary containing XP thresholds for each difficulty.
    """

    thresholds = XP_THRESHOLDS_BY_LEVEL[party_level]
    
    results = {
        "party_level": party_level,
        "party_size": party_size,
        "easy": thresholds["easy"] * party_size,
        "medium": thresholds["medium"] * party_size,
        "hard": thresholds["hard"] * party_size,
        "deadly": thresholds["deadly"] * party_size,
    }

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate XP thresholds for D&D 5e encounters")
    parser.add_argument("--party-level", type=int, required=True, help="Party level (1-20)")
    parser.add_argument("--party-size", type=int, required=True, help="Number of characters in the party")

    args = parser.parse_args()

    result = calculate_xp_threshold(args.party_level, args.party_size)
    print(f"Party Level: {result['party_level']}")
    print(f"Party Size: {result['party_size']}")
    print(f"--- XP Thresholds ---")
    print(f"Easy:   {result['easy']}")
    print(f"Medium: {result['medium']}")
    print(f"Hard:   {result['hard']}")
    print(f"Deadly: {result['deadly']}")
