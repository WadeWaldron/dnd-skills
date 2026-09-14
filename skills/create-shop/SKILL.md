---
name: create-shop
description: Creates a D&D 5e shop with a name, proprietor, pricing based on settlement size, and stock quantities from scarcity modifiers. Use when the user wants a shop, a merchant, a market stall, or to know what gear is for sale in a town.
license: CC0-1.0
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

## Price Lists

Item prices, weights, and Scarcity Modifiers are in [references/price-lists.md](references/price-lists.md). Read the sections for the shop's stock.
