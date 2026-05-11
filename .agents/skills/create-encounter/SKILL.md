---
name: create-encounter
description: This skill will create an encounter of an appropriate level based on the party's level, size, and desired difficulty. It will calculate the XP threshold for the encounter and then look up appropriate creatures to fill that encounter.
---

# Create Encounter

This skill will create an encounter of an appropriate level based on the party's level, size, and desired difficulty. It will calculate the XP threshold for the encounter and then look up appropriate creatures to fill that encounter.

When the skill is executed, it will ask the user for the party's level, size, and the desired difficulty of the encounter (easy, medium, hard, or deadly). It will also accept details of the encounter such as the environment, creature types, and other preferences. It will then:
1. Calculate the encounter XP threshold (the target difficulty) using the **calculate-xp-threshold** skill.
2. Use the resulting XP threshold to look up appropriate creatures using the **lookup-creatures** skill.
3. Select creatures from the list of results to build a balanced encounter that fits the XP budget and desired difficulty.
4. Present the final encounter to the user, including the selected creatures, their stats, and a summary of the encounter.

## Step 1: Get Party Level

**If the party level is not provided:**
1. Ask the user: "What is the party's level?"
2. Wait for the user's response and store it as `party_level`.

**If the party level is provided:**
1. Store the provided party level as `party_level`.

## Step 2: Get Party Size

**If the party size is not provided:**
1. Ask the user: "What is the party's size (number of characters)?"
2. Wait for the user's response and store it as `party_size`.

**If the party size is provided:**
1. Store the provided party size as `party_size`.

## Step 3: Get Desired Difficulty

**If the desired difficulty is not provided:**
1. Ask the user: "What is the desired difficulty of the encounter? (easy, medium, hard, or deadly)"
2. Wait for the user's response and store it as `desired_difficulty`.

**If the desired difficulty is provided:**
1. Store the provided desired difficulty as `desired_difficulty`.

## Step 4: Get Additional Encounter Details
You can gather more details about the encounter to help with creature selection.

**If a description of the encounter is not provided:**
1. Ask the user: "Can you provide a brief description of the encounter? (e.g., 'This encounter takes place in a dark forest and should include undead creatures.')"
2. Wait for the user's response and store it as `encounter_description`.
3. Extract relevant details from the description to use as filters for creature selection (e.g., environment, creature types).

**If a description of the encounter is provided:**
1. Store the provided encounter description as `encounter_description`.
2. Extract relevant details from the description to use as filters for creature selection (e.g., environment, creature types).

From the description, you want to extract filters such as:
- **Size**: Tiny, Small, Medium, Large, Huge, Gargantuan, Titanic
- **Creature Type**: Aberration, Beast, Celestial, Construct, Dragon, Elemental, Fey, Fiend, Giant, Humanoid, Monstrosity, Ooze, Plant, Undead
- **Subtype**: Angel, Animal, Any Lineage, Demon, Devil, Lycanthrope, Outsider, Shapechanger, Swarm, dwarf, elf, gnoll, goblinoid, grimlock, human, kobold, lizardfolk, merfolk, orc, sahuagin, titan
- **Group**: Angels, Animals, Animated Objects, Black Dragon, Blue Dragon, Brass Dragon, Bronze Dragon, Copper Dragon, Demons, Devils, Dinosaurs, Dragons, Elementals, Elf, Fungi, Genies, Ghouls, Giants, Goblins, Gold Dragon, Golems, Green Dragon, Hags, Kobolds, Liches, Lizardfolk, Lycanthropes, Mephits, Merfolk, Miscellaneous Creatures, Mummies, NPCs, Nagas, Oozes, Orcs, Red Dragon, Silver Dragon, Skeletons, Sphinxes, Vampires, White Dragon, Zombies
- **Environment**: Abyss, Any, Arctic, Astral Plane, Caverns, Caves, Coastal, Desert, Ethereal Plane, Feywild, Forest, Grassland, Hell, Hill, Hills, Ice, Jungle, Laboratory, Lake, Mountain, Mountains, Ocean, Plane Of Air, Plane Of Earth, Plane Of Fire, Plane Of Water, Ruin, Ruins, Settlement, Sewer, Shadowfell, Swamp, Temple, Tomb, Tundra, Underdark, Underwater, Urban, Volcano, Water
- **Other Preferences**: e.g., flying creatures, swarm of small creatures, a single powerful creature, etc.

## Step 5: Calculate XP Threshold
Use the **calculate-xp-threshold** skill to determine the XP requirements for the encounter.

1. Locate the `calculate-xp-threshold` skill.
2. Execute the skill with the collected party level, size, and desired difficulty.
3. Capture the output from the skill including:
   - **Encounter XP**: The party's difficulty threshold (constant)
   - **Monster XP**: The total XP that monsters should have (varies by random monster count)
   - **Average XP per Monster**: The average XP value per individual monster
   - **Monster Count**: A randomly generated number of creatures (favors smaller encounters)
   - **Encounter Multiplier**: The scaling factor based on monster count

**Critical**: The values from the calculate-xp-threshold skill will be essential for guiding creature selection in the next steps, so ensure you capture and utilize them effectively. You will be judged on how well the final encounter matches the XP requirements, desired difficulty, and Monster Count.

## Step 6: Select an encounter style.
Based on the **Monster Count** from the calculate-xp-threshold skill, select an encounter style to guide creature selection. The encounter style will determine how the XP budget is allocated among monsters in the encounter.

- **Single Monster**: Focus on one powerful creature that meets the XP requirements.
- **Two Monsters**: A pair of creatures that together meet the XP requirements. These should be approximately equal in strength to create a balanced fight. It can be two of the same monster or two different monsters.
- **Boss and Minions**: One main creature that takes up approximately 50% of the XP budget, supported by weaker creatures that fill out the rest of the XP. This creates a dynamic encounter with a clear main threat and additional challenges. The weaker creatures should all be of approximately the same strength to create a cohesive group of minions.
- **Horde**: A group of weaker creatures that together meet the XP requirements. Each of the creatures should be approximately equal to each other in terms of XP. This could be a swarm of similar monsters, or a mix of different monsters. However, we want a maximum of 3 different types of monsters in the horde.
- **VS**: Two groups of creatures that are in opposition to each other. Each group should be approximately equal in total XP to create a balanced fight. This could be used for encounters where the party is caught in the middle of a conflict between two factions, or for a unique encounter where the party must choose which side to support.

## Step 7: Look Up Creatures
Use the **lookup-creatures** skill to find appropriate creatures based on the calculated XP threshold, encounter style, and any filters derived from the encounter description. Depending on the style of the encounter, you may need to do multiple lookups with different XP targets (e.g., one for the main monster and one for minions). Ensure you include any relevant filters such as environment or creature type to find creatures that fit the theme of the encounter. Prioritize finding creatures that fit together thematically and narratively based on the encounter description, while also meeting the XP requirements.

1. Locate the `lookup-creatures` skill.
2. Execute the skill with the following parameters:
   - `target_xp`: The required monster XP from the calculate-xp-threshold skill (or a portion of it based on encounter style).
   - `tolerance_percent`: A reasonable tolerance (e.g., 20%) to allow for a range of creatures.
   - `max_results`: A sufficient number of results to choose from (e.g., 10).
   - Additional filters based on encounter description (e.g., environment, creature type).
3. Capture the output from the skill, which will include matching creatures with their stats and summaries

**Critical**: Try to find creatures that closely match the required XP values while also fitting the encounter style and thematic filters. If you cannot find creatures that fit the XP requirements, consider adjusting the filters to find a better match. For example, if your original filter was Ocean, you could try expanding it to include Coastal or any water-based environment to find more options. Or, if you were looking for a specific creature type, such as Undead, you could try changing it to include a related type, such as Fiends, to find more options. You want to find the best possible creatures that fit the XP requirements while also matching the theme and style of the encounter.

If necessary, you can iterate on this step, adjusting the parameters and filters to find the best fit for the encounter. You may find it valuable to do all of the lookups first, then review the results together to make your final selections for the encounter.

## Step 8: Build the Encounter
Based on the results from the lookup-creatures skill, select specific creatures to build the encounter. Consider the following:
- Ensure the number of creatures matches the monster count from the calculate-xp-threshold skill.
- Ensure the total XP of selected creatures is close to the required monster XP.
- Match the encounter style (e.g., one powerful monster for Single Monster, a mix for Mixed, a swarm for Horde).

## Step 9: Generate a Description of the Encounter
Write a summary of the encounter that includes:
- The selected creatures and their stats.
- A narrative description of how the encounter might play out based on the creatures and the encounter style.
- Any special tactics or features of the encounter (e.g., terrain advantages, creature abilities).
- **Important**: A key part of the encounter description is an explanation of why this particular group of creatures appears together in the encounter.

## Step 10: Present the Encounter
Present the final encounter to the user in a clear and engaging format, including:
- A list of the selected creatures with their stats.
- The narrative description of the encounter.
- An explanation of how the encounter fits the desired difficulty and style.

## Example Output

```
## Encounter: Goblin Ambush in the Dark Forest
**Encounter Style**: Skirmish
**Encounter XP**: 1,200 XP (Hard for a level 3 party of 4 characters)
**Selected Creatures**:
- Goblin Boss (XP: 700)
- Goblin (XP: 200)
- Goblin (XP: 200)
- Goblin (XP: 200)
**Total Monster XP**: 1,300 XP (within 20% tolerance of target)
**Encounter Description**:
As the party travels through the dark forest, they are ambushed by a band of goblins led by a cunning Goblin Boss. The goblins use the terrain to their advantage, hiding behind trees and attacking from the shadows. The Goblin Boss directs the attack, using hit-and-run tactics to keep the party off balance. The encounter is challenging but manageable for a level 3 party, providing an exciting combat experience with opportunities for strategic play.
```