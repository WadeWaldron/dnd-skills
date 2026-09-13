#!/usr/bin/env python3
"""
Look up creatures from monsters.json based on XP values.

This script searches for creatures in D&D 5e that match specific XP criteria,
useful for building encounters with specific XP budgets.
"""

import json
import argparse
from pathlib import Path


def load_creatures():
    """Load creatures from monsters.json."""
    json_path = Path(__file__).parent / "monsters.json"
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data.get("creatures", [])


def find_creatures(target_xp=None, tolerance_percent=20, max_results=10, 
                   sizes=None, creature_types=None, subtypes=None, 
                   groups=None, environments=None, names=None):
    """
    Find creatures that match filters.
    
    Args:
        target_xp: Optional target XP value.
        tolerance_percent: Acceptable deviation from target XP (default 20%)
        max_results: Maximum number of results to return (default 10)
        sizes: Optional list of size filters
        creature_types: Optional list of type filters
        subtypes: Optional list of subtype filters
        groups: Optional list of group filters
        environments: Optional list of environment filters
        names: Optional list of exact names to find
    
    Returns:
        List of creatures
    """
    creatures = load_creatures()
    matching = []

    # Filter by exact names if provided (Phase 2)
    if names:
        names_lower = [n.lower().strip() for n in names]
        matching = [c for c in creatures if c["name"].lower() in names_lower]
        return matching

    # Filter by XP range if provided
    if target_xp:
        tolerance = target_xp * (tolerance_percent / 100)
        min_xp = target_xp - tolerance
        max_xp = target_xp + tolerance
        matching = [c for c in creatures if min_xp <= c["xp"] <= max_xp]
    else:
        matching = creatures
    
    # Apply additional filters
    if sizes:
        sizes_lower = [s.lower().strip() for s in sizes]
        matching = [c for c in matching if c.get("size", "").lower() in sizes_lower]
    
    if creature_types:
        types_lower = [t.lower().strip() for t in creature_types]
        matching = [c for c in matching if c.get("type", "").lower() in types_lower]
    
    if subtypes:
        subtypes_lower = [s.lower().strip() for s in subtypes]
        matching = [c for c in matching if c.get("subtype", "").lower() in subtypes_lower]
    
    if groups:
        groups_lower = [g.lower().strip() for g in groups]
        matching = [c for c in matching if c.get("group", "").lower() in groups_lower]
    
    if environments:
        environments_lower = [e.lower().strip() for e in environments]
        matching = [c for c in matching if any(env.lower() in environments_lower 
                                               for env in c.get("environments", []))]
    
    # Sort and Limit
    if target_xp:
        matching.sort(key=lambda c: abs(c["xp"] - target_xp))
    else:
        # Default sort by XP ascending if no target
        matching.sort(key=lambda c: c["xp"])
    
    return matching[:max_results]


def print_summary(creatures):
    """Print a compact table of creatures."""
    if not creatures:
        print("No creatures found matching those criteria.")
        return

    print(f"{'Name':<25} | {'CR':<5} | {'XP':<7} | {'Type':<15} | {'Size':<10}")
    print("-" * 75)
    for c in creatures:
        ctype = c["type"]
        if c.get("subtype"):
            ctype += f" ({c['subtype']})"
        print(f"{c['name']:<25} | {c['cr']:<5} | {c['xp']:<7} | {ctype[:15]:<15} | {c['size']:<10}")


def format_creature(creature):
    """Format a creature as a D&D 5e markdown statblock."""
    output = "---\n\n"
    
    # Header: Name, Size, Type, Alignment
    output += f"# {creature['name']}\n\n"

    # Summary (only if exists)
    if creature.get("summary"):
        output += f"***{creature['summary']}***\n\n"
    
    creature_type = creature["type"]
    if creature.get("subtype"):
        creature_type += f" ({creature['subtype']})"
    
    alignment = creature["alignment"].title()
    output += f"*{creature['size']} {creature_type}, {alignment}*\n\n"
    
    # AC, HP, Speed
    ac_line = f"**Armor Class** {creature['armor_class']}"
    if creature.get("armor_desc"):
        ac_line += f" ({creature['armor_desc']})"
    output += f"{ac_line}\n\n"

    hp_line = f"**Hit Points** {creature['hit_points']}"
    if creature.get("hit_dice"):
        hp_line += f" ({creature['hit_dice']})"
    output += f"{hp_line}\n\n"
    
    # Speed
    speed_dict = creature["speed"]
    speed_parts = []
    if speed_dict.get("walk"):
        speed_parts.append(f"{speed_dict['walk']} ft.")
    if speed_dict.get("climb"):
        speed_parts.append(f"climb {speed_dict['climb']} ft.")
    if speed_dict.get("fly"):
        speed_parts.append(f"fly {speed_dict['fly']} ft.")
    if speed_dict.get("swim"):
        speed_parts.append(f"swim {speed_dict['swim']} ft.")
    
    if speed_parts:
        output += f"**Speed** {', '.join(speed_parts)}\n\n"

    output += "---\n\n"
    
    # Ability Scores Table with Modifiers
    stats = creature["stats"]
    output += "| STR | DEX | CON | INT | WIS | CHA |\n"
    output += "|:---:|:---:|:---:|:---:|:---:|:---:|\n"
    
    def get_mod(score):
        mod = (score - 10) // 2
        return f"{score} ({mod:+d})"

    str_f = get_mod(stats["strength"])
    dex_f = get_mod(stats["dexterity"])
    con_f = get_mod(stats["constitution"])
    int_f = get_mod(stats["intelligence"])
    wis_f = get_mod(stats["wisdom"])
    cha_f = get_mod(stats["charisma"])
    
    output += f"| {str_f} | {dex_f} | {con_f} | {int_f} | {wis_f} | {cha_f} |\n\n"
    
    output += "---\n\n"

    # Saving Throws
    saves = creature.get("saves", {})
    save_parts = []
    ability_abbr = {"strength": "STR", "dexterity": "DEX", "constitution": "CON", 
                   "intelligence": "INT", "wisdom": "WIS", "charisma": "CHA"}
    
    for ability in ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]:
        save_value = saves.get(ability)
        if save_value is not None:
            save_parts.append(f"{ability_abbr[ability]} {save_value:+d}")
    
    if save_parts:
        output += f"**Saving Throws** {', '.join(save_parts)}\n\n"
    
    # Skills & Passive Perception
    skills = creature.get("skills", {})
    skill_parts = []
    passive_perc = skills.pop("passive_perception", None)
    
    if skills:
        for skill, modifier in sorted(skills.items()):
            skill_name = skill.replace("_", " ").title()
            skill_parts.append(f"{skill_name} {modifier:+d}")
        output += f"**Skills** {', '.join(skill_parts)}\n\n"
    
    # Defenses & Senses
    defenses = creature.get("defenses", {})
    dmg = defenses.get("damage", {})
    if dmg.get("vulnerabilities"):
        output += f"**Damage Vulnerabilities** {dmg['vulnerabilities']}\n\n"
    if dmg.get("resistances"):
        output += f"**Damage Resistances** {dmg['resistances']}\n\n"
    if dmg.get("immunities"):
        output += f"**Damage Immunities** {dmg['immunities']}\n\n"
    if defenses.get("condition_immunities"):
        output += f"**Condition Immunities** {defenses['condition_immunities']}\n\n"

    traits = creature.get("traits", {})
    senses = traits.get("senses", "")
    if passive_perc:
        passive_str = f"passive Perception {passive_perc}"
        if senses:
            senses += f", {passive_str}"
        else:
            senses = passive_str
    
    if senses:
        output += f"**Senses** {senses}\n\n"
    
    languages = traits.get("languages")
    if languages:
        output += f"**Languages** {languages}\n\n"

    # Challenge and XP
    output += f"**Challenge** {creature['cr']} ({creature['xp']} XP)\n\n"

    output += "---\n\n"

    # Traits (Special Abilities)
    special_abilities = traits.get("special_abilities")
    if special_abilities:
        for trait in special_abilities:
            output += f"***{trait['name']}.*** {trait['desc']}\n\n"

    # Actions
    actions = creature.get("actions", {})
    
    if actions.get("standard"):
        output += "### Actions\n\n"
        for action in actions["standard"]:
            output += f"***{action['name']}.*** {action['desc']}\n\n"

    if actions.get("bonus"):
        output += "### Bonus Actions\n\n"
        for action in actions["bonus"]:
            output += f"***{action['name']}.*** {action['desc']}\n\n"

    if actions.get("reaction"):
        output += "### Reactions\n\n"
        for action in actions["reaction"]:
            output += f"***{action['name']}.*** {action['desc']}\n\n"

    if actions.get("legendary"):
        leg = actions["legendary"]
        if isinstance(leg, dict) and leg.get("actions"):
            output += f"### Legendary Actions\n\n"
            count = leg.get("count", 3)
            output += f"The {creature['name']} can take {count} legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The {creature['name']} regains spent legendary actions at the start of its turn.\n\n"
            for action in leg["actions"]:
                output += f"***{action['name']}.*** {action['desc']}\n\n"

    return output

    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lookup creatures by XP and filters.")
    parser.add_argument("--target-xp", type=int, help="Target XP value")
    parser.add_argument("--tolerance", type=int, default=20, help="Tolerance percentage (default 20)")
    parser.add_argument("--max-results", type=int, default=10, help="Max results (default 10)")
    parser.add_argument("--sizes", help="Comma-separated sizes")
    parser.add_argument("--types", help="Comma-separated creature types")
    parser.add_argument("--subtypes", help="Comma-separated subtypes")
    parser.add_argument("--groups", help="Comma-separated groups")
    parser.add_argument("--environments", help="Comma-separated environments")
    parser.add_argument("--names", help="Comma-separated exact names to find")
    parser.add_argument("--full", action="store_true", help="Print full statblocks instead of summary")

    args = parser.parse_args()

    # Helper to split comma strings
    def split_arg(val):
        return [x.strip() for x in val.split(",")] if val else None

    results = find_creatures(
        target_xp=args.target_xp,
        tolerance_percent=args.tolerance,
        max_results=args.max_results,
        sizes=split_arg(args.sizes),
        creature_types=split_arg(args.types),
        subtypes=split_arg(args.subtypes),
        groups=split_arg(args.groups),
        environments=split_arg(args.environments),
        names=split_arg(args.names)
    )

    if args.full:
        for c in results:
            print(format_creature(c))
            print("\n")
    else:
        print_summary(results)
