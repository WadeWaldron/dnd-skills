---
name: create-character-sheet
description: Creates a printable D&D 5e character sheet and spell cards for a player character, driven by a single data file. Use when the user wants to make a character sheet, start a new character, or level one up.
license: CC0-1.0
compatibility: Requires a web browser to view and print the sheet
---

# Create Character Sheet

Builds a printable character sheet and spell cards from one data file. No build
step, no server, no dependencies — edit, save, refresh.

## Creating a character

1. Make a folder named for the character.
2. Copy all three files from [assets/](assets/) into it: `character.js`,
   `sheet.html`, `cards.html`.
3. Fill in `character.js`. Its comments document every key; read the file rather
   than guessing at field names.
4. If the user supplies a portrait, save it in the folder as `portrait.jpg` or
   `.png`. It is optional — a placeholder shows when it's missing.
5. Tell the user to open `sheet.html` and `cards.html` in a browser, and to
   **print at 100%** rather than letting the dialog scale to fit.

`sheet.html` and `cards.html` are the engine. Copy them unchanged and don't edit
them to solve a content problem.

## Filling in character.js

Set `proficiencyBonus` from total character level:

| Level | 1-4 | 5-8 | 9-12 | 13-16 | 17-20 |
| ----- | --- | --- | ---- | ----- | ----- |
| PB    | +2  | +3  | +4   | +5    | +6    |

Everything the sheet can work out for itself, it does — ability modifiers,
saving throws, all 18 skill bonuses, passive Perception, spell save DC, spell
attack bonus, initiative. Never write those into `character.js`.

Leave blank the things that change during play: coins, XP, current and temp HP,
death saves, and anything in `consumables`.

Delete any key the character doesn't need. Empty sections don't render.

## Cards carry the ability text, not the character's numbers

The sheet gets reprinted whenever the character changes. **Cards are printed
once and kept.** A card only stays valid across level-ups if nothing on it
depends on the character's current numbers.

So write the ability, spell or feature description **as it appears in the source
material**. Do not work out what it comes to for this character.

- Keep the rule's own wording: *"your spell save DC"*, *"1d8 + your
  spellcasting ability modifier"*, *"equal to your proficiency bonus"*.
- Don't write `+7 to hit`, `DC 15`, `2d8 + 5`, or `4 uses per long rest` when
  those come from the character's scores, proficiency bonus or level.
- Fixed values that belong to the ability itself — its damage dice, range,
  duration, casting time, component costs — are static. Write those out.

`<span class="hit">…</span>` boxes a number for mid-fight lookup. Use it for a
value the ability fixes, not one derived from the character.

The character's own numbers live on the sheet, which derives them and stays
current. That division is the whole point: sheet for what changes, cards for
what doesn't.

The same caution applies in reverse on the sheet — a DC typed into a feature
description or a panel is a second copy that won't update. Numbers that genuinely
aren't derivable, such as an attack bonus that includes a fighting style, are
fine to write out, because the sheet can't work them out either.

## Traps

**`biography`, not `background`.** `background` is already the one-line
Background in the sheet header. Using it twice is legal JavaScript — the second
one silently wins — and the header prints `[object Object]`.

**`character.js` is JavaScript, not JSON.** That's deliberate: it allows `//`
comments and trailing commas. But an unbalanced brace or a smart quote outside a
string stops the page rendering entirely. A blank sheet is almost always this.
Curly quotes and em dashes are fine *inside* strings.

**Page 1 is a fixed box and clips silently.** If content doesn't fit, cut
content — duplication first, since anything already on a card or a later panel
doesn't need to be in the equipment box too. Do not adjust the zoom or any
page's height to make something fit. Those numbers are tuned against each other,
and changing one breaks the correspondence between screen and print.

**Cards clip silently too, with no warning.** The sheet shows a red overflow bar
naming the page and column; cards have no such check. Card bodies trim past
roughly 14 short lines, so a new card needs a visual check.

## Verifying changes cheaply

`character.js` files grow large. Never read the whole file into a verification
script or shell command — that dumps it into context repeatedly and is the
single biggest source of wasted tokens when working on these.

- **Parses at all?** `node -c character.js` reports syntax errors without
  printing the file.
- **One field's value?** `grep -n "fieldName" character.js`, or a targeted
  `sed -n '/fieldName/,/^  },/p'` — pull the few lines that matter.
- **A derived number?** Work it out from the ability scores and proficiency
  bonus already in context, or grep just those two lines.
- **Structural check?** Run JS against the file, but print only the computed
  result.

Prefer the edit tool over shell commands for changing the file. That produces
diffs and lets hooks run.

If a genuine full-file read is unavoidable — checking overall structure after a
large rewrite — say so and do it once.
