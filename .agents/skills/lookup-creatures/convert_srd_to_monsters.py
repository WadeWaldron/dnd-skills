#!/usr/bin/env python3
"""
Convert srd_monsters_wotc_only.json to monsters.json format.
This file contains exactly 322 official D&D 5e SRD creatures.
"""

import json
from pathlib import Path


# Official D&D 5e XP table by Challenge Rating
OFFICIAL_XP_BY_CR = {
    0: 10,
    0.125: 25,
    0.25: 50,
    0.5: 100,
    1: 200,
    2: 450,
    3: 700,
    4: 1100,
    5: 1800,
    6: 2300,
    7: 2900,
    8: 3900,
    9: 5000,
    10: 5900,
    11: 7200,
    12: 8400,
    13: 10000,
    14: 11500,
    15: 13000,
    16: 15000,
    17: 18000,
    18: 20000,
    19: 22000,
    20: 25000,
    21: 33000,
    22: 41000,
    23: 50000,
    24: 62000,
    25: 75000,
    26: 90000,
    27: 105000,
    28: 120000,
    29: 135000,
    30: 155000,
}


def convert_srd_to_monsters():
    """Convert SRD WOTC-only data to monsters.json format."""
    srd_path = Path(__file__).parent / "srd_monsters_wotc_only.json"
    output_path = Path(__file__).parent / "monsters.json"
    
    print(f"Reading from: {srd_path}")
    
    # Load SRD data
    with open(srd_path, 'r') as f:
        srd_data = json.load(f)
    
    creatures = []
    
    for srd_creature in srd_data.get("results", []):
        name = srd_creature.get("name", "")
        cr = srd_creature.get("cr", 0)
        # Use official D&D 5e XP table
        xp = OFFICIAL_XP_BY_CR.get(cr, 0)
        
        creature = {
            "name": name,
            "cr": cr,
            "xp": xp,
            "type": srd_creature.get("type", ""),
            "size": srd_creature.get("size", ""),
            "summary": srd_creature.get("desc", "Unknown creature"),
            "subtype": srd_creature.get("subtype", ""),
            "group": srd_creature.get("group"),
            "environments": srd_creature.get("environments", []),
            "alignment": srd_creature.get("alignment", ""),
            "armor_class": srd_creature.get("armor_class", 10),
            "hit_points": srd_creature.get("hit_points", 1),
            "speed": srd_creature.get("speed", {"walk": 30}),
            "skills": srd_creature.get("skills", {}),
            "stats": {
                "strength": srd_creature.get("strength", 10),
                "dexterity": srd_creature.get("dexterity", 10),
                "constitution": srd_creature.get("constitution", 10),
                "intelligence": srd_creature.get("intelligence", 10),
                "wisdom": srd_creature.get("wisdom", 10),
                "charisma": srd_creature.get("charisma", 10),
            },
            "saves": {
                "strength": srd_creature.get("strength_save"),
                "dexterity": srd_creature.get("dexterity_save"),
                "constitution": srd_creature.get("constitution_save"),
                "intelligence": srd_creature.get("intelligence_save"),
                "wisdom": srd_creature.get("wisdom_save"),
                "charisma": srd_creature.get("charisma_save"),
            }
        }
        creatures.append(creature)
    
    # Create output structure
    output = {
        "creatures": creatures
    }
    
    # Write to file
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"✓ Converted {len(creatures)} official SRD 5.1 creatures")
    print(f"✓ Saved to: {output_path}")


if __name__ == "__main__":
    convert_srd_to_monsters()
