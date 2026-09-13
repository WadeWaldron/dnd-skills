---
name: create-shop
description: Generates a thematic shop with available inventory based on settlement size and item scarcity modifiers.
---

# Create Shop

This skill provides a structured workflow for generating a merchant's inventory and shop atmosphere, ensuring that item availability follows the logic of the local economy.

## Step 1: Set Settlement Die Type
Determine the size of the settlement where the shop is located. This sets the **Settlement Die** used for item availability and quantity.

| Settlement Type     | Settlement Die | Description                                                |
| :------------------ | :------------- | :--------------------------------------------------------- |
| **Outpost/Village** | 1d4            | Isolated, limited supplies, local focus.                   |
| **Town**            | 1d8            | Standard market with common goods.                         |
| **City**            | 1d12           | Diverse economy, rare items are occasionally found.        |
| **Metropolis**      | 1d20           | Trade hub where almost anything can be acquired.           |

## Step 2: Determine Pricing

Use the `roll-dice` skill to roll the **Settlement Die** to determine the pricing for the shop. The result of the roll will be used to adjust the prices of all items in the shop's inventory according to the following table:

| Roll Result | Price Modifier | Description                                                         |
| :---------- | :------------- | :------------------------------------------------------------------ |
| **1-3**     | 110% Cost      | **Scarcity Pricing:** Low supply or high demand increases the cost. |
| **4-9**     | 100% Cost      | **Standard Pricing:** The fair market value listed in the tables.   |
| **10+**     | 90% Cost       | **Competitive Pricing:** High volume and competition lower the cost.|

*Note: Since small settlements (d4/d8) rarely roll 10+, they almost never offer competitive pricing, whereas cities (d12/d20) frequently do.*

- **Crisis Adjustment:** If the region is suffering from a shortage (like the Barkskin Plague), add 10% - +50% to the pricing adjustment to reflect the severity of the crisis.
- **Haggling:** A successful DC 15 Persuasion check (Charisma) can reduce the price by 10%.

## Step 3: Shop Flavor
Briefly define the shop's vibe:
1. **Name:** Give it a thematic name (e.g., "The Cracked Anvil," "The Salty Crate").
2. **Proprietor:** A short description of the shopkeeper.
3. **The Hook:** One sensory detail (sound, smell, or unique sight) that makes the shop memorable.

## Step 4: Determine Quantity
Players will roll the **Settlement Die** at the table to determine an item's availability. Each item has a **Scarcity Modifier** that adjusts the roll to reflect how common or rare the item is in that settlement. The result is the exact quantity the shop has in stock.

- **Quantity formula**: `[Settlement Die Roll] + [Scarcity Modifier]`
- **Out of Stock**: If the result is **0 or lower**, the shop has none.
- **In stock**: If the result is **1 or higher**, the shop has that many of the item in stock.

---

## Appendix: Reference Tables

### Adventuring Gear

| Item                             | Cost     | Weight       | Scarcity Modifier |
| :------------------------------- | :------- | :----------- | :---------------- |
| Abacus                           | 2 gp     | 2 lb.        | 0                 |
| Acid (vial)                      | 25 gp    | 1 lb.        | -2                |
| Alchemist's fire (flask)         | 50 gp    | 1 lb.        | -3                |
| Antitoxin (vial)                 | 50 gp    | —            | -2                |
| Backpack                         | 2 gp     | 5 lb.        | +2                |
| Ball bearings (bag of 1,000)     | 1 gp     | 2 lb.        | +1                |
| Barrel                           | 2 gp     | 70 lb.       | +1                |
| Basket                           | 4 sp     | 2 lb.        | +1                |
| Bedroll                          | 1 gp     | 7 lb.        | +2                |
| Bell                             | 1 gp     | —            | +1                |
| Blanket                          | 5 sp     | 3 lb.        | +1                |
| Block and tackle                 | 1 gp     | 5 lb.        | 0                 |
| Book                             | 25 gp    | 5 lb.        | -1                |
| Bottle, glass                    | 2 gp     | 2 lb.        | +1                |
| Bucket                           | 5 cp     | 2 lb.        | +2                |
| Caltrops (bag of 20)             | 1 gp     | 2 lb.        | 0                 |
| Candle                           | 1 cp     | —            | +2                |
| Case, crossbow bolt              | 1 gp     | 1 lb.        | +1                |
| Case, map or scroll              | 1 gp     | 1 lb.        | 0                 |
| Chain (10 feet)                  | 5 gp     | 10 lb.       | 0                 |
| Chalk (1 piece)                  | 1 cp     | —            | +2                |
| Chest                            | 5 gp     | 25 lb.       | -1                |
| Climber's kit                    | 25 gp    | 12 lb.       | -1                |
| Clothes, common                  | 5 sp     | 3 lb.        | +2                |
| Clothes, costume                 | 5 gp     | 4 lb.        | 0                 |
| Clothes, fine                    | 15 gp    | 6 lb.        | -2                |
| Clothes, traveler's              | 2 gp     | 4 lb.        | +1                |
| Component pouch                  | 25 gp    | 2 lb.        | -1                |
| Crowbar                          | 2 gp     | 5 lb.        | +1                |
| Fishing tackle                   | 1 gp     | 4 lb.        | +1                |
| Flask or tankard                 | 2 cp     | 1 lb.        | +2                |
| Grappling hook                   | 2 gp     | 4 lb.        | 0                 |
| Hammer                           | 1 gp     | 3 lb.        | +1                |
| Hammer, sledge                   | 2 gp     | 10 lb.       | 0                 |
| Healer's kit                     | 5 gp     | 3 lb.        | 0                 |
| Holy water (flask)               | 25 gp    | 1 lb.        | -3                |
| Hourglass                        | 25 gp    | 1 lb.        | -2                |
| Hunting trap                     | 5 gp     | 25 lb.       | -1                |
| Ink (1 ounce bottle)             | 10 gp    | —            | -1                |
| Ink pen                          | 2 cp     | —            | +1                |
| Jug or pitcher                   | 2 cp     | 4 lb.        | +2                |
| Ladder (10-foot)                 | 1 sp     | 25 lb.       | +1                |
| Lamp                             | 5 sp     | 1 lb.        | +1                |
| Lantern, bullseye                | 10 gp    | 2 lb.        | -1                |
| Lantern, hooded                  | 5 gp     | 2 lb.        | 0                 |
| Lock                             | 10 gp    | 1 lb.        | -1                |
| Magnifying glass                 | 100 gp   | —            | -5                |
| Manacles                         | 2 gp     | 6 lb.        | 0                 |
| Mess kit                         | 2 sp     | 1 lb.        | +1                |
| Mirror, steel                    | 5 gp     | ½ lb.        | -1                |
| Oil (flask)                      | 1 sp     | 1 lb.        | +1                |
| Paper (one sheet)                | 2 sp     | —            | 0                 |
| Parchment (one sheet)            | 1 sp     | —            | 0                 |
| Perfume (vial)                   | 5 gp     | —            | -1                |
| Pick, miner's                    | 2 gp     | 10 lb.       | +1                |
| Piton                            | 5 cp     | ¼ lb.        | +1                |
| Poison, basic (vial)             | 100 gp   | —            | -4                |
| Pole (10-foot)                   | 5 cp     | 7 lb.        | +1                |
| Pot, iron                        | 2 gp     | 10 lb.       | +1                |
| Potion of healing                | 50 gp    | ½ lb.        | -3                |
| Pouch                            | 5 sp     | 1 lb.        | +2                |
| Quiver                           | 1 gp     | 1 lb.        | +1                |
| Ram, portable                    | 4 gp     | 35 lb.       | -2                |
| Rations (1 day)                  | 5 sp     | 2 lb.        | +2                |
| Robes                            | 1 gp     | 4 lb.        | +1                |
| Rope, hempen (50 feet)           | 1 gp     | 10 lb.       | +2                |
| Rope, silk (50 feet)             | 10 gp    | 5 lb.        | -1                |
| Sack                             | 1 cp     | ½ lb.        | +2                |
| Scale, merchant's                | 5 gp     | 3 lb.        | 0                 |
| Sealing wax                      | 5 sp     | —            | 0                 |
| Shovel                           | 2 gp     | 5 lb.        | +1                |
| Signal whistle                   | 5 cp     | —            | +1                |
| Signet ring                      | 5 gp     | —            | 0                 |
| Soap                             | 2 cp     | —            | +1                |
| Spellbook                        | 50 gp    | 3 lb.        | -4                |
| Spikes, iron (10)                | 1 gp     | 5 lb.        | +1                |
| Spyglass                         | 1,000 gp | 1 lb.        | -10               |
| Tent, two-person                 | 2 gp     | 20 lb.       | 0                 |
| Tinderbox                        | 5 sp     | 1 lb.        | +1                |
| Torch                            | 1 cp     | 1 lb.        | +2                |
| Vial                             | 1 gp     | —            | 0                 |
| Waterskin                        | 2 sp     | 5 lb. (full) | +2                |
| Whetstone                        | 1 cp     | 1 lb.        | +1                |

### Armor

| Armor           | Cost       | Armor Class (AC)          | Weight       | Scarcity Modifier |
|:----------------|:-----------|:--------------------------|:-------------|:------------------|
| **Light Armor** |            |                           |              |                   |
| Padded          | 5 gp       | 11 + Dex modifier         | 8 lb.        | +1                |
| Leather         | 10 gp      | 11 + Dex modifier         | 10 lb.       | +2                |
| Studded Leather | 45 gp      | 12 + Dex modifier         | 13 lb.       | 0                 |
| **Medium Armor**|            |                           |              |                   |
| Hide            | 10 gp      | 12 + Dex modifier (max 2) | 12 lb.       | +1                |
| Chain Shirt     | 50 gp      | 13 + Dex modifier (max 2) | 20 lb.       | -1                |
| Scale Mail      | 50 gp      | 14 + Dex modifier (max 2) | 45 lb.       | -1                |
| Breastplate     | 400 gp     | 14 + Dex modifier (max 2) | 20 lb.       | -3                |
| Half Plate      | 750 gp     | 15 + Dex modifier (max 2) | 40 lb.       | -4                |
| **Heavy Armor** |            |                           |              |                   |
| Ring Mail       | 30 gp      | 14                        | 40 lb.       | -1                |
| Chain Mail      | 75 gp      | 16                        | 55 lb.       | -2                |
| Splint          | 200 gp     | 17                        | 60 lb.       | -3                |
| Plate           | 1,500 gp   | 18                        | 65 lb.       | -5                |
| **Shield**      |            |                           |              |                   |
| Shield          | 10 gp      | +2                        | 6 lb.        | +2                |

### Weapons

| Weapon              | Cost      | Damage           | Scarcity Modifier |
| :------------------ | :-------- | :--------------- | :---------------- |
| **Simple Melee**    |           |                  |                   |
| Club                | 1 sp      | 1d4 bludgeoning  | +2                |
| Dagger              | 2 gp      | 1d4 piercing     | +1                |
| Greatclub           | 2 sp      | 1d8 bludgeoning  | +1                |
| Handaxe             | 5 gp      | 1d6 slashing     | +1                |
| Javelin             | 5 sp      | 1d6 piercing     | +2                |
| Light Hammer        | 2 gp      | 1d4 bludgeoning  | +1                |
| Mace                | 5 gp      | 1d6 bludgeoning  | +1                |
| Quarterstaff        | 2 sp      | 1d6 bludgeoning  | +2                |
| Sickle              | 1 gp      | 1d4 slashing     | +1                |
| Spear               | 1 gp      | 1d6 piercing     | +1                |
| **Simple Ranged**   |           |                  |                   |
| Crossbow, Light     | 25 gp     | 1d8 piercing     | 0                 |
| Dart                | 5 cp      | 1d4 piercing     | +2                |
| Shortbow            | 25 gp     | 1d6 piercing     | +1                |
| Sling               | 1 sp      | 1d4 bludgeoning  | +2                |
| **Martial Melee**   |           |                  |                   |
| Battleaxe           | 10 gp     | 1d8 slashing     | 0                 |
| Flail               | 10 gp     | 1d8 bludgeoning  | 0                 |
| Glaive              | 20 gp     | 1d10 slashing    | -1                |
| Greataxe            | 30 gp     | 1d12 slashing    | -1                |
| Greatsword          | 50 gp     | 2d6 slashing     | -3                |
| Halberd             | 20 gp     | 1d10 slashing    | -1                |
| Lance               | 10 gp     | 1d12 piercing    | -2                |
| Longsword           | 15 gp     | 1d8 slashing     | 0                 |
| Maul                | 10 gp     | 2d6 bludgeoning  | -1                |
| Morningstar         | 15 gp     | 1d8 piercing     | 0                 |
| Pike                | 5 gp      | 1d10 piercing    | 0                 |
| Rapier              | 25 gp     | 1d8 piercing     | -1                |
| Scimitar            | 25 gp     | 1d6 slashing     | 0                 |
| Shortsword          | 10 gp     | 1d6 piercing     | +1                |
| Trident             | 5 gp      | 1d6 piercing     | +1                |
| War Pick            | 5 gp      | 1d8 piercing     | 0                 |
| Warhammer           | 15 gp     | 1d8 bludgeoning  | 0                 |
| Whip                | 2 gp      | 1d4 slashing     | -1                |
| **Martial Ranged**  |           |                  |                   |
| Blowgun             | 10 gp     | 1 piercing       | -3                |
| Crossbow, Hand      | 75 gp     | 1d6 piercing     | -3                |
| Crossbow, Heavy     | 50 gp     | 1d10 piercing    | -2                |
| Longbow             | 50 gp     | 1d8 piercing     | -1                |
| Net                 | 1 gp      | —                | -2                |

### Ammunition

| Item                         | Cost  | Weight | Scarcity Modifier |
| :--------------------------- | :---- | :----- | :---------------- |
| Arrows (20)                  | 1 gp  | 1 lb.  | +2                |
| Blowgun needles (50)         | 1 gp  | 1 lb.  | 0                 |
| Crossbow bolts (20)          | 1 gp  | 1.5 lb.| +1                |
| Sling bullets (20)           | 4 cp  | 1.5 lb.| +2                |

### Tools

| Tool                     | Cost      | Scarcity Modifier |
| :----------------------- | :-------- | :---------------- |
| **Artisan's Tools**      |           |                   |
| Alchemist's supplies     | 50 gp     | -2                |
| Brewer's supplies        | 20 gp     | -1                |
| Calligrapher's supplies  | 10 gp     | -1                |
| Carpenter's tools        | 8 gp      | +1                |
| Cartographer's tools     | 15 gp     | 0                 |
| Cobbler's tools          | 5 gp      | +1                |
| Cook's utensils          | 1 gp      | +2                |
| Glassblower's tools      | 30 gp     | -2                |
| Jeweler's tools          | 25 gp     | -3                |
| Leatherworker's tools    | 5 gp      | +1                |
| Mason's tools            | 10 gp     | 0                 |
| Painter's supplies       | 10 gp     | 0                 |
| Potter's tools           | 10 gp     | 0                 |
| Smith's tools            | 20 gp     | +1                |
| Tinker's tools           | 50 gp     | -2                |
| Weaver's tools           | 1 gp      | +1                |
| Woodcarver's tools       | 1 gp      | +1                |
| **Gaming Sets**          |           |                   |
| Dice set                 | 1 sp      | +2                |
| Dragonchess set          | 1 gp      | 0                 |
| Playing card set         | 5 sp      | +2                |
| Three-Dragon Ante set    | 1 gp      | 0                 |
| **Musical Instruments**  |           |                   |
| Bagpipes                 | 30 gp     | -2                |
| Drum                     | 6 gp      | +1                |
| Flute                    | 2 gp      | +1                |
| Lute                     | 35 gp     | -1                |
| Lyre                     | 30 gp     | -1                |
| Pan flute                | 12 gp     | 0                 |
| Shawm                    | 2 gp      | 0                 |
| Viol                     | 30 gp     | -1                |
| **Other Tools**          |           |                   |
| Disguise kit             | 25 gp     | -2                |
| Forgery kit              | 15 gp     | -3                |
| Herbalism kit            | 5 gp      | 0                 |
| Navigator's tools        | 25 gp     | -1                |
| Poisoner's kit           | 50 gp     | -4                |
| Thieves' tools           | 25 gp     | -2                |

### Mounts and Vehicles

| Item                | Cost      | Scarcity Modifier |
| :------------------ | :-------- | :---------------- |
| Donkey or Mule      | 8 gp      | +2                |
| Horse, Draft        | 50 gp     | +1                |
| Horse, Riding       | 75 gp     | 0                 |
| Cart                | 15 gp     | +2                |
| Wagon               | 35 gp     | +1                |
| Rowboat             | 50 gp     | +1                |

### Services

| Service                 | Cost     | Scarcity Modifier |
| :---------------------- | :------- | :---------------- |
| Inn Stay (Common)       | 5 sp     | +2                |
| Common Meal             | 3 sp     | +2                |
| Healer (Minor Wounds)   | 10 gp    | -1                |
| Priest (Blessing)       | 25 gp    | -2                |
| Spellcasting (per level)| 10-50 gp | -3                |

### Magic Items

| Rarity      | Base Price Range (gp) | Scarcity Modifier |
| :---------- | :-------------------- | :---------------- |
| Common      | 50–100                | -1                |
| Uncommon    | 101–500               | -4                |
| Rare        | 501–5,000             | -8                |
| Very Rare   | 5,001–50,000          | -13               |
| Legendary   | 50,001+               | -18               |

#### Common Magic Items (Select)

| Item                      | Cost   | Description                                                                 |
| :------------------------ | :----- | :-------------------------------------------------------------------------- |
| **Cloak of Billowing**    | 50 gp  | You can use a bonus action to make this cloak billow dramatically.             |
| **Clockwork Amulet**      | 100 gp | Once per day, you can skip rolling a d20 and treat the result as a 10.         |
| **Enduring Spellbook**    | 100 gp | This book cannot be damaged by fire or water.                               |
| **Heward's Spice Pouch**  | 50 gp  | Use an action to produce a pinch of any common seasoning (salt, pepper, etc). |
| **Pole of Collapsing**    | 50 gp  | A 10-foot pole that can collapse into a 1-foot long rod.                    |
| **Pot of Awakening**      | 100 gp | Plant a shrub in this pot; after 30 days, it becomes an Awakened Shrub.     |
| **Wand of Smiles**        | 50 gp  | Use an action to force a creature to succeed a DC 10 Cha save or smile.     |
