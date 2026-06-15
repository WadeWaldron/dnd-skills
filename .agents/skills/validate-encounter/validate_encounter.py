#!/usr/bin/env python3
"""
Validate a D&D 5e encounter's difficulty based on 2024 rules.
"""

import argparse
import json
import sys

def get_scaling_factor(count):
    if count >= 15: return 4.0
    if count >= 11: return 3.0
    if count >= 7: return 2.5
    if count >= 3: return 2.0
    if count == 2: return 1.5
    return 1.0

def validate_encounter(easy, medium, hard, deadly, monsters):
    """
    monsters: list of dicts with {"name": str, "xp": int, "count": int}
    """
    total_raw_xp = sum(m["xp"] * m["count"] for m in monsters)
    total_monster_count = sum(m["count"] for m in monsters)
    
    scaling_factor = get_scaling_factor(total_monster_count)
    adjusted_xp = total_raw_xp * scaling_factor
    
    difficulty = "Trivial"
    if adjusted_xp >= deadly:
        difficulty = "Deadly"
    elif adjusted_xp >= hard:
        difficulty = "Hard"
    elif adjusted_xp >= medium:
        difficulty = "Medium"
    elif adjusted_xp >= easy:
        difficulty = "Easy"
        
    return {
        "total_raw_xp": total_raw_xp,
        "total_monster_count": total_monster_count,
        "scaling_factor": scaling_factor,
        "adjusted_xp": adjusted_xp,
        "difficulty": difficulty,
        "thresholds": {
            "easy": easy,
            "medium": medium,
            "hard": hard,
            "deadly": deadly
        }
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate D&D 5e encounter difficulty")
    parser.add_argument("--easy", type=int, required=True)
    parser.add_argument("--medium", type=int, required=True)
    parser.add_argument("--hard", type=int, required=True)
    parser.add_argument("--deadly", type=int, required=True)
    parser.add_argument("--target", type=str, choices=["easy", "medium", "hard", "deadly"], help="Target difficulty level")
    parser.add_argument("--monsters", type=str, required=True, help='JSON string: [{"name": "Orc", "xp": 450, "count": 3}]')

    args = parser.parse_args()
    
    try:
        monsters = json.loads(args.monsters)
        result = validate_encounter(args.easy, args.medium, args.hard, args.deadly, monsters)
        
        print(f"Monsters: {result['total_monster_count']} total")
        print(f"Raw XP: {result['total_raw_xp']}")
        print(f"Adjusted XP: {result['adjusted_xp']} ({result['scaling_factor']}x multiplier)")
        print(f"Resulting Difficulty: {result['difficulty'].upper()}")
        
        if args.target:
            target = args.target.upper()
            if result['difficulty'].upper() == target:
                print(f"STATUS: SUCCESS (Matches target difficulty {target})")
            else:
                print(f"STATUS: FAIL (Expected {target}, but encounter is {result['difficulty'].upper()})")
                
                # Simple advice
                if result['adjusted_xp'] > result['thresholds'][args.target.lower()]:
                    diff = result['adjusted_xp'] / result['scaling_factor'] - result['thresholds'][args.target.lower()] / result['scaling_factor']
                    print(f"ADVICE: Encounter is too strong. Try removing approximately {int(diff)} raw monster XP.")
                else:
                    diff = result['thresholds'][args.target.lower()] / result['scaling_factor'] - result['adjusted_xp'] / result['scaling_factor']
                    print(f"ADVICE: Encounter is too weak. Try adding approximately {int(diff)} raw monster XP.")

        print(f"--- Thresholds ---")
        print(f"Easy:   {result['thresholds']['easy']}")
        print(f"Medium: {result['thresholds']['medium']}")
        print(f"Hard:   {result['thresholds']['hard']}")
        print(f"Deadly: {result['thresholds']['deadly']}")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
