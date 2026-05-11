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


def find_creatures_by_xp(target_xp, tolerance_percent=20, max_results=5, 
                         sizes=None, creature_types=None, subtypes=None, 
                         groups=None, environments=None):
    """
    Find creatures that match the target XP value and optional filters.
    
    Args:
        target_xp: Target XP value to search for
        tolerance_percent: Acceptable deviation from target XP (default 20%)
        max_results: Maximum number of results to return (default 5)
        sizes: Optional list of size filters (e.g., ["Small", "Large"])
        creature_types: Optional list of type filters (e.g., ["Dragon", "Humanoid"])
        subtypes: Optional list of subtype filters
        groups: Optional list of group filters
        environments: Optional list of environment filters
    
    Returns:
        List of creatures sorted by XP distance from target
    """
    creatures = load_creatures()
    
    # Calculate tolerance range
    tolerance = target_xp * (tolerance_percent / 100)
    min_xp = target_xp - tolerance
    max_xp = target_xp + tolerance
    
    # Filter creatures within tolerance
    matching = [c for c in creatures if min_xp <= c["xp"] <= max_xp]
    
    # Apply additional filters (OR logic within each filter type)
    if sizes:
        sizes_lower = [s.lower() for s in sizes]
        matching = [c for c in matching if c.get("size", "").lower() in sizes_lower]
    
    if creature_types:
        types_lower = [t.lower() for t in creature_types]
        matching = [c for c in matching if c.get("type", "").lower() in types_lower]
    
    if subtypes:
        subtypes_lower = [s.lower() for s in subtypes]
        matching = [c for c in matching if c.get("subtype", "").lower() in subtypes_lower]
    
    if groups:
        groups_lower = [g.lower() for g in groups]
        matching = [c for c in matching if c.get("group", "").lower() in groups_lower]
    
    if environments:
        environments_lower = [e.lower() for e in environments]
        matching = [c for c in matching if any(env.lower() in environments_lower 
                                               for env in c.get("environments", []))]
    
    # Sort by distance from target XP
    matching.sort(key=lambda c: abs(c["xp"] - target_xp))
    
    return matching[:max_results]


def format_creature(creature):
    """Format a creature as a D&D 5e markdown statblock."""
    output = "---\n\n"
    
    # Header: Name, Size, Type, Alignment
    output += f"# {creature['name']}\n\n"

    # Summary
    output += f"***{creature['summary']}***\n\n"
    
    creature_type = creature["type"]
    if creature.get("subtype"):
        creature_type += f" ({creature['subtype']})"
    
    alignment = creature["alignment"].title()
    output += f"*{creature['size']} {creature_type}, {alignment}*\n\n"
    
    # AC, HP, Speed
    output += f"**Armor Class** {creature['armor_class']}\n\n"
    output += f"**Hit Points** {creature['hit_points']}\n\n"
    
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
    
    output += f"**Speed** {', '.join(speed_parts)}\n\n"

    output += "---\n\n"
    
    # Ability Scores Table
    stats = creature["stats"]
    output += "| STR | DEX | CON | INT | WIS | CHA |\n"
    output += "|:---:|:---:|:---:|:---:|:---:|:---:|\n"
    
    str_score = stats["strength"]
    dex_score = stats["dexterity"]
    con_score = stats["constitution"]
    int_score = stats["intelligence"]
    wis_score = stats["wisdom"]
    cha_score = stats["charisma"]
    
    output += f"|  {str_score:2d} |  {dex_score:2d} |  {con_score:2d} |  {int_score:2d} |  {wis_score:2d} |  {cha_score:2d} |\n\n"
    
    output += "---\n\n"

    # Saving Throws
    saves = creature["saves"]
    save_parts = []
    ability_abbr = {"strength": "STR", "dexterity": "DEX", "constitution": "CON", 
                   "intelligence": "INT", "wisdom": "WIS", "charisma": "CHA"}
    
    for ability in ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]:
        save_value = saves.get(ability)
        if save_value is not None:
            save_parts.append(f"{ability_abbr[ability]} {save_value:+d}")
    
    if save_parts:
        output += f"**Saving Throws** {', '.join(save_parts)}\n\n"
    
    # Skills
    skills = creature.get("skills", {})
    if skills:
        skill_parts = []
        for skill, modifier in sorted(skills.items()):
            skill_name = skill.replace("_", " ").title()
            skill_parts.append(f"{skill_name} {modifier:+d}")
        output += f"**Skills** {', '.join(skill_parts)}\n\n"
    
    # Challenge and XP
    output += f"**Challenge** {creature['cr']} ({creature['xp']} XP)\n\n"

    output += "---\n\n"
    
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Look up creatures by XP value with optional filters"
    )
    parser.add_argument(
        "--xp-target",
        type=float,
        required=True,
        help="Target XP value to search for"
    )
    parser.add_argument(
        "--tolerance",
        type=float,
        default=20,
        help="Acceptable deviation from target XP as percentage (default: 20)"
    )
    parser.add_argument(
        "--count",
        type=int,
        default=5,
        help="Maximum number of results to return (default: 5)"
    )
    parser.add_argument(
        "--size",
        type=str,
        action="append",
        dest="sizes",
        help="Filter by size (e.g., Small, Medium, Large, Huge). Can be specified multiple times."
    )
    parser.add_argument(
        "--type",
        type=str,
        action="append",
        dest="creature_types",
        help="Filter by creature type (e.g., Dragon, Humanoid, Undead). Can be specified multiple times."
    )
    parser.add_argument(
        "--subtype",
        type=str,
        action="append",
        dest="subtypes",
        help="Filter by subtype. Can be specified multiple times."
    )
    parser.add_argument(
        "--group",
        type=str,
        action="append",
        dest="groups",
        help="Filter by group (e.g., Silver Dragon, Demon). Can be specified multiple times."
    )
    parser.add_argument(
        "--environment",
        type=str,
        action="append",
        dest="environments",
        help="Filter by environment (e.g., Mountains, Urban, Underdark). Can be specified multiple times."
    )
    
    args = parser.parse_args()
    
    results = find_creatures_by_xp(
        args.xp_target, 
        args.tolerance, 
        args.count,
        sizes=args.sizes,
        creature_types=args.creature_types,
        subtypes=args.subtypes,
        groups=args.groups,
        environments=args.environments
    )
    
    if results:
        print(f"Found {len(results)} creature(s) matching {args.xp_target} XP (±{args.tolerance}%):\n")
        for creature in results:
            print(format_creature(creature))
            print()
    else:
        print(f"No creatures found matching {args.xp_target} XP (±{args.tolerance}%)")
