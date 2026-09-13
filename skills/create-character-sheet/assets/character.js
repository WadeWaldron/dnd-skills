/* ============================================================================
   CHARACTER DATA — starting skeleton
   ----------------------------------------------------------------------------
   Fill this in, then open sheet.html.
   No build step. No server. Edit, save, refresh.

   THINGS THE SHEET WORKS OUT FOR YOU — never type these:
     ability modifiers · saving throws · all 18 skill bonuses
     passive Perception · spell save DC · spell attack bonus · initiative
   Change an ability score or the proficiency bonus and everything follows.

   Fields ending in "Html" accept raw HTML: <b> <i> <br>
   plus <span class="note">muted italic</span> and <span class="muted">muted</span>.
   Delete any key you don't need — empty sections don't render.
============================================================================ */

window.CHARACTER = {

  /* ---- identity -------------------------------------------------------- */
  name:      "New Character",
  epithet:   "",              // small italic line under the name; optional
  classLevel:"Class 1",
  subclass:  "",              // optional — shown smaller, under Class & Level
  background:"Background",
  player:    "",
  species:   "Species",
  alignment: "",
  xp:        "",              // leave blank — you'll write it in

  portrait:  "portrait.jpg",  // drop a file with this name in the folder

  // One prose block across the top: personality, ideals, bonds, flaws, all in one.
  descriptionHtml: `<p>Who they are, in a paragraph or two.</p>`,

  /* ---- the numbers ----------------------------------------------------- */
  abilities: { str: 10, dex: 10, con: 10, int: 10, wis: 10, cha: 10 },
  proficiencyBonus: 2,

  saveProf:  [],   // e.g. ["dex","int"]
  skillProf: [],   // e.g. ["stealth","perception","sleightOfHand"]
                   // camelCase: sleightOfHand, animalHandling

  skillNote: {},   // small red tag, e.g. { stealth: "disadv" }

  ac: 10,
  acNote: "",      // small line under the AC number, e.g. "20 w/ Shield"
  hp: 8,
  hitDice: "1d8",
  hitDiceTotal: 1,
  speed: 30,
  darkvision: 0,
  passiveNote: "", // red second line under passive Perception

  /* ---- proficiencies box ----------------------------------------------- */
  armor:     "",
  weapons:   "",
  toolsHtml: "",
  languages: "Common",

  /* ---- spellcasting (delete this whole key for a non-caster) ------------ */
  spellcasting: {
    className: "Class",
    ability:   "int",       // "int" | "wis" | "cha" — drives DC and attack
    slots:     { 1: 2 },    // { 1:4, 2:3, 3:2 } as you level
  },

  /* ---- attacks --------------------------------------------------------- */
  attacks: [
    { name: "Weapon", atk: "+0", dmg: "1d6 slashing" },
  ],
  blankAttackRows: 3,       // empty rows to write new weapons into
  attackNotesHtml: ``,

  /* ---- equipment ------------------------------------------------------- */
  equipmentHtml: `<p>Everything you carry.</p>`,

  // counts that change constantly — printed with a blank line to write in
  consumables: [
    // { name: "Arrows" },
    // { name: "Potion of Healing", note: "2d4+2" },
  ],

  /* ---- features & traits -----------------------------------------------
     `uses: 3` draws three tick boxes at the START of the line.             */
  features: [
    { group: "Species", items: [
      { name: "Trait", text: "What it does." },
    ]},
    { group: "Class", items: [
      { name: "Feature", uses: 2, text: "What it does. 2/long rest." },
    ]},
  ],

  /* ---- spells --------------------------------------------------
     pip — "filled" = always prepared, no slot
           "ritual" = square pip
           "open"   = hollow pip, costs a slot
     Levels beyond 1 go in spellsLevel2, spellsLevel3, … matching the
     keys in spellcasting.slots above.                                      */
  cantrips: [
    // { name: "Cantrip", source: "Class", text: "What it does." },
  ],
  spellsLevel1: [
    // { name: "Spell", source: "Class", pip: "open", text: "What it does." },
  ],
  spellFootnote: "",

  /* ---- the party — a roster section (delete if you don't want it) ------- */
  party: [
    // { name: "Character", player: "Player" },
  ],
  partyBlankRows: 3,     // ruled lines for people who join later
  // partyTitle: "The Party",

  /* ---- companion (delete the key if you have none) ---------------------- */
  // companion: {
  //   title: "Name — Familiar",
  //   statsHtml: "<span class='k'>AC</span> 11 · <span class='k'>HP</span> 1 · Fly 60 ft.",
  //   linesHtml: [ "<span class='k'>Trait.</span> What it does." ],
  // },

  /* ---- free-form reference panels, flowed in with everything else -------- */
  panels: [
    // { title: "Turn Checklist", highlight: true, linesHtml: [
    //   "<span class='k'>1 ·</span> Do this first.",
    // ]},
  ],

  /* ---- biography (delete the key and it stops rendering) ------------------
     Called `biography`, NOT `background` — `background` is the one-line
     Background in the header above, and a repeated key silently overwrites it.
     Each entry in `sections` becomes its own block in the page-2+ flow.
     `aside: true` shades a section and keeps it from splitting across columns. */
  // biography: {
  //   sections: [
  //     { heading: "Where they came from", html: `<p>Prose.</p>` },
  //     { heading: "The secret", aside: true, html: `<p>Prose.</p>` },
  //   ],
  // },

  /* ---- images — as many as you want (portraits, drawings, maps, a page
     from a notebook, a companion's likeness, …). Each is its own block in
     the flow, so adding one just grows the sheet by however much page it
     needs. `height` decides how tall its box is.                          */
  images: [
    // { src: "drawing.jpg", height: "2.4in", caption: "What it is" },
  ],

  /* ==========================================================================
     CARDS  (cards.html) — 2.5×3.35in, 9 per page
     colour: innate | initiate | class | species | campaign | feature
     Body text clips silently past roughly 14 short lines — check new cards.
     Useful inside bodyHtml:
       <span class="hit">DC 15</span>   boxed number you look up mid-fight
       <p class="lede">                 highlighted, not italic
       <p class="note">                 muted italic
       <p class="tiny">                 smaller, for dense lists
  ========================================================================== */
  cards: [
    // { name: "Spell Name", sub: "Level 1 · School", colour: "class",
    //   foot: ["Source", "1 / long rest"],
    //   meta: { Cast: "Action", Range: "60 ft.", Comp: "V, S", Dur: "Instantaneous" },
    //   bodyHtml: `<p>What it does.</p>` },
  ],
};
