# Medieval Overhaul Japanization Furniture / Architecture Mapping

**Status:** Project-owned pre-split design audit for `AMJ - Medieval Overhaul Japanization`.

This document maps Medieval Overhaul 1.6.2.2 architecture, furniture and domestic-object Defs into the historical Japanization profile. It is a design ledger, not an implementation claim. No production XML, textures, C# or MO files are changed by this document.

Audited source:
- author-provided `3219596926.zip`
- Medieval Overhaul 1.6.2.2
- previously recorded archive SHA-256: `6ed379d7c400db43b3af2a9a7fd6203f7f7e99ca1a670d36b0f73fd1adccc9e3`

## Decision rule

Each MO object is classified by **loaded gameplay role first**, not by whether its current graphic can be made to look vaguely Japanese.

- **KEEP** — function and presentation are already generic enough; only localization/minor visual audit may be needed.
- **REINTERPRET + RETEXTURE** — preserve the existing MO Def/mechanics, but replace label/description/graphic/material/research placement with an honest Japanese referent.
- **CONDITIONAL** — retain only in a later branch/profile or when another owner Mod provides the missing historically valid loop.
- **HIDE** — remove from the normal historical build/research path while preserving the upstream Def for compatibility.
- **GENERATION-CRITICAL** — the Def is directly used by MO settlement/site generation and cannot be hidden or radically changed without patching the generated layouts/loadouts at the same time.

A Japanese name is not enough. If the upstream object's interaction model, footprint, room role or production process contradicts the proposed Japanese referent, hide it or patch the mechanic rather than disguising it with art.

---

## 1. Structural walls, gates and defensive construction

### `DankPyon_CastleWall`

Loaded role:
- impassable high wall;
- HP 1000;
- roof-supporting;
- Stony stuff, 15 stuff;
- directly related to CastleWallEmbrasures / RusticDoor / SlabDoor / Gate.

Generation audit:
- the older raw substring audit found **8,919 occurrences of the `DankPyon_CastleWall*` name family**, which mixed wall and embrasure symbol names;
- exact SymbolDef-aware audit resolves **8,565 layout-cell uses** to `DankPyon_CastleWall` itself:
  - **5,323** settlement cells;
  - **1,349** Big Snake cells;
  - **1,264** large-cultist cells;
  - **629** medium-cultist cells;
- including direct generation links, the source ledger records **8,568 generation references** for the ThingDef;
- `DankPyon_CastleWallEmbrasures` is separate: **342 layout-cell uses** (**334** settlement + **8** large-cultist), **344** generation references including direct links.

**Decision: GENERATION-CRITICAL — REINTERPRET + RETEXTURE.**

Do **not** hide this Def as merely a European castle wall. MO settlement generation depends on it too heavily.

Primary Japanese referent:
- high enclosed **築地塀 / 練塀-class compound wall**, not `石垣`.

Rationale:
- a vertical RimWorld wall is mechanically much closer to an enclosing earthen/plastered wall than to a Japanese castle stone base;
- the nationally designated Nishinomiya Shrine `大練塀` is a Muromachi-middle `築地塀` (1393–1466), giving a direct pre-Edo high-wall reference;
- Japanese castle `石垣` is a retaining/raised-base system and should not be represented by simply renaming an impassable vertical wall.

Required patch:
- Japanese label/description;
- Japanese wall texture family;
- revisit Stony material semantics/cost: earth/clay/wood or another historically credible construction basis is preferable to presenting it as solid cut-stone masonry;
- preserve DefName and generation identity;
- validate all generated settlement/site layouts after the material/graphic change.

Historical anchor:
- Agency for Cultural Affairs, 西宮神社大練塀:
  - https://kunishitei.bunka.go.jp/heritage/detail/102/2359
  - https://kunishitei.bunka.go.jp/heritage/detail/102/2358
  - https://kunishitei.bunka.go.jp/bsys/maindetails/102/2357

### `DankPyon_CastleWallEmbrasures`

Loaded role:
- high defensive wall with partial fill;
- HP 800;
- **346 XML references**, about **334** in settlement layouts.

**Decision: GENERATION-CRITICAL — REINTERPRET + RETEXTURE, exact opening form pending.**

Keep the defensive firing-opening role because removing the Def would disturb generated fortifications.

Do not yet lock the Japanese name to a specific late-Sengoku firearm loophole. A generic `狭間付き塀` / defensive opening is safer until the exact graphic, firing behavior and chronology are matched.

Implementation gate:
- verify that the opening functions for bows/guns in a way compatible with the chosen referent;
- preserve generation dimensions and pathing;
- avoid a graphic that implies an Edo castle wall if the node remains available earlier.

### `DankPyon_TudorWall`

Loaded role:
- timber-framed wall with wattle/daub infill;
- HP 450;
- fixed `DankPyon_Clay 3` + 2 stuff;
- only its own Def reference in the current XML audit.

**Decision: REINTERPRET + RETEXTURE.**

This is unusually reusable mechanically. Rename/retexture toward a Japanese **timber-and-earth infill / 土壁 construction**, keeping the wood + clay logic.

Do not keep the Tudor label or black-and-white Tudor visual grammar.

Historical anchor:
- nationally designated Muromachi buildings preserve extensive `土壁` construction; for example the Muromachi-period Jōshōji complex description records earthen walls as part of the surviving building fabric:
  - https://kunishitei.bunka.go.jp/heritage/detail/102/00004234

### Doors and gates

| MO Def | Decision | Japanization direction | Generation note |
|---|---|---|---|
| `DankPyon_RusticDoor` | **REINTERPRET + RETEXTURE** | ordinary wooden door / plank door; preserve door mechanics | **920 refs**, heavily settlement-used |
| `DankPyon_LogGate` | **REINTERPRET + RETEXTURE** | simple heavy wooden gate | settlement-used |
| `DankPyon_Gate` | **REINTERPRET + RETEXTURE** | reinforced wooden compound gate | **75 refs** |
| `DankPyon_ReinfocedLogGate` | **REINTERPRET + RETEXTURE** | stronger timber gate; remove meaningless ComplexFurniture placement if necessary | **129 refs**, mostly settlements |
| `DankPyon_RusticDoor1x2c` | **REINTERPRET + RETEXTURE** | wide/tall wooden door/gate variant | generation audit before hiding |
| `DankPyon_Gate1x2c` | **REINTERPRET + RETEXTURE** | larger compound gate | generation audit before hiding |
| `DankPyon_SlabDoor` / `SlabDoor1x2c` | **HIDE by default** | a massive repurposed stone-slab door is a poor normal Japanese architectural fit | `SlabDoor` has **78 refs**; hiding requires layout replacement |

The stone-slab door is the important exception: its normal player build path should be hidden, but because MO structures reference it, Japanization must replace those layout symbols with a retained Japanese gate/door rather than deleting the Def blindly.

### Trenches

`DankPyon_RTrench`:
- standable;
- pathCost 300;
- HP 800;
- Beauty -5;
- Stony stuff;
- behaves as a built obstruction, not an impassable ditch.

**Decision: HIDE from baseline.**

Do not relabel it `空堀` or `堀`. Its mechanics do not represent a true ditch/moat well enough. A future moat/ditch system belongs to its actual feature owner rather than being faked by this MO emplacement.

---

## 2. Ordinary furniture / storage

### Chests and clothing storage

#### `DankPyon_RusticChest`

Loaded role:
- 1x1 storage;
- protects stored items from deterioration;
- small Beauty/bed comfort role;
- **19 references**.

**Decision: KEEP / RETEXTURE lightly.**

A simple wooden chest maps naturally to Japanese `櫃` / chest storage.

#### `DankPyon_RoyalChest`

Loaded role:
- ornate high-value chest;
- iron + gold;
- Beauty 30.

**Decision: REINTERPRET + RETEXTURE.**

Map to a decorated/lacquered high-status `唐櫃` / chest rather than a Western treasure chest.

Historical anchors:
- 12th-century Heian `鳳凰円文螺鈿唐櫃`:
  - https://emuseum.nich.go.jp/detail?content_base_id=100670
- 1357 Nanboku-chō `住之江蒔絵唐櫃`:
  - https://emuseum.nich.go.jp/detail?content_base_id=100537

#### `DankPyon_RusticCloset` / `RusticCloset1x2c`

Loaded role:
- actual apparel storage + bed comfort bonus;
- `RusticCloset` has **95 references**, including **41 settlement references**.

**Decision: GENERATION-IMPORTANT — REINTERPRET + RETEXTURE.**

Do not present it as a standing European wardrobe. Recast the storage role toward clothing chests/shelving/cabinetry appropriate to Japanese rooms while preserving storage behavior.

### Shelves / cupboards / display-storage families

MO contains a large visual-storage family: shelves, cupboards, sacks, crates, bales, ingot piles, carts, weapon racks and filled display variants.

**Decision rule:**
- generic functional storage forms may remain;
- Western food-display variants such as bread/cheese/wine cupboards are curated with the underlying food branch and should not remain merely as decorative Japanized props;
- fantasy-drug/gem/chalice display variants follow their content branch, not furniture ownership;
- do not create new Japanese storage Defs solely to replace every decorative variant;
- where a generic retained storage Def already works, prefer a Japanese texture/label over duplicate Defs.

---

## 3. Tables, seating and beds

### Important boundary with `AMJ - Premodern Culture`

Japanization owns the **MO Def presentation** here. It does **not** own Vanilla culture rules such as `AteWithoutTable`, `SleptOnGround`, privacy or room expectations.

Therefore:
- MO tables/seats/beds can be reinterpreted/retextured into Japanese forms;
- changing whether a pawn considers floor dining/sleep culturally acceptable belongs to the separate Premodern Culture candidate;
- Japanization must not silently expand into a global Thought overhaul.

### Ordinary tables and seating

MO has:
- log tables 1x2 / 1x3 / 1x4 / 2x4;
- log chair;
- log benches;
- rustic stool/chair/noble chair;
- multiple rustic/reinforced tables;
- round table;
- counters;
- end tables.

**Decision: family-level REINTERPRET + RETEXTURE, with pruning.**

Keep enough Defs to preserve useful gameplay footprints, generated-layout compatibility and dining/work seating choices. Do not preserve every Western visual variation just because a Def exists.

Target visual grammar:
- lower/simple wooden dining/work surfaces where the interaction cell allows it;
- stools/benches/floor-seat-inspired forms where the pawn interaction still reads honestly;
- avoid literal high-backed European chairs, tavern benches and banquet tables when a Japanese counterpart does not fit.

Do **not** call a standard RimWorld chair `座布団` if the pawn is visibly using chair-height geometry. If the renderer/graphic footprint cannot support the floor-level referent honestly, use a generic wooden seat or hide the redundant Def.

Existing Japanese furniture Mods, especially Erin's Japanese Furniture, already provide purpose-built futon, zabuton, low table, tatami, andon, shoji/fusuma etc. Japanization should not add duplicate new Defs simply to compete with them.

### Ordinary bed families

MO has:
- log bed/double;
- wicker bed/double;
- straw bed/double;
- fur bed/double;
- red/green/blue rustic bed variants.

**Decision: REINTERPRET + RETEXTURE, then consolidate visible variants.**

The `Building_Bed` function can represent a Japanese sleeping place without requiring a Western bedframe, so the mechanics are reusable.

However:
- use floor-level bedding / mat / framed sleeping-place visuals only where the occupied-cell interaction remains visually credible;
- do not create one new Japanese Def per color;
- redundant colored Western variants may be hidden from the player build menu while keeping upstream Defs for compatibility/generation;
- Premodern Culture, not Japanization, decides whether floor-level sleeping avoids `SleptOnGround`.

---

## 4. Royal/high-status furniture

MO settlement generation directly uses many Royal Defs, so a broad “hide the Western royal furniture” rule is unsafe.

### Generation/reference summary

The earlier substring-oriented audit slightly overcounted several families. The SymbolDef-aware source ledger gives:

| Def | generation refs | via layout SymbolDefs | Main issue |
|---|---:|---:|---|
| `DankPyon_RoyalArmchair` | 42 | 38 | Western chair-height elite seating |
| `DankPyon_RoyalEndTable` | 26 | 24 | bedside-table semantics |
| `DankPyon_RoyalTudorBed` | 25 | 22 | Western double-bed presentation |
| `DankPyon_RoyalDresser` | 21 | 18 | Western dresser semantics |
| `DankPyon_RoyalCloset` | 18 | 15 | “closet” label; actual role is bed-comfort furnishing |
| `DankPyon_RoyalBookshelf` | 15 | 12 | research facility |
| `DankPyon_RoyalTable2x2c` | 13 | 12 | banquet/high table presentation |
| `DankPyon_RoyalTable2x4c` | 2 | 1 | oversized banquet-table presentation |
| `DankPyon_RoyalThrone` | 0 in baseline XML | 0 | Royalty integration must be audited through the conditional Royalty profile |

### Historical interior reference

Rekihaku's Heian aristocratic-interior teaching materials, based on `類聚雑要抄`, explicitly show:
- `畳`;
- `脇息`;
- `円座`;
- lamps/washing implements;
- `二階厨子` and `二階棚`;
- `御帳台` as an assembled sleeping/private space for high-ranking persons.

Sources:
- https://www.rekihaku.ac.jp/assets/pdf/learning/stuff/shidou_heian.pdf
- https://www.rekihaku.ac.jp/assets/pdf/learning/stuff/kaisetsu_heian.pdf

These provide a much stronger visual/semantic basis than reskinning every Western royal chair/dresser one-for-one.

### Def decisions

#### `DankPyon_RoyalCloset`

Actual mechanic:
- 1x1;
- Gold 30;
- Beauty 30;
- bed Comfort +0.1;
- description claims clothing storage, but the audited Def is principally a bed-facility furnishing.

**Decision: REINTERPRET + RETEXTURE.**

Use a high-status cabinet/`厨子`-class room furnishing rather than a standing European closet. Rewrite the description to match the actual facility mechanic.

#### `DankPyon_RoyalBookshelf`

Actual mechanic:
- 1x1;
- silk + gold;
- Beauty 30;
- ResearchSpeedFactor +0.075.

**Decision: REINTERPRET + RETEXTURE.**

Map to an elite document/book shelf/cabinet (`書棚` / `文庫` / `厨子棚` class) while preserving the research-support role. Do not imply a European bound-book library if the visual does not support it.

#### `DankPyon_RoyalArmchair`

Actual mechanic:
- Fabric/Leathery + Gold 30;
- Comfort 0.95;
- Beauty 30;
- usable at tables/workstations.

**Decision: REINTERPRET + RETEXTURE, geometry-gated.**

A high-status `円座` / formal floor-seat is historically attractive, but only use that exact referent if the pawn/table interaction can visually support it. Otherwise use a generic high-status Japanese seat rather than a literal Western armchair.

Because it has 47 references, hiding it without rewriting settlement layouts is not acceptable.

#### `DankPyon_RoyalThrone`

Actual role:
- ornate king/queen chair;
- Beauty 45, Comfort 0.95;
- Royalty patch references.

**Decision: REINTERPRET + RETEXTURE to formal authority seating / `御座`, conditional on Royalty semantics.**

Remove “king/queen throne” presentation. Preserve only if Royalty integration can use a Japanese formal seat without requiring false Western court semantics.

If the Royalty throne-assignment mechanics intrinsically require a chair-shaped throne, use a stylized formal seat rather than pretending it is an exact historical household object.

#### `DankPyon_RoyalTable2x2c` / `RoyalTable2x4c`

Actual role:
- high Beauty/gold/silk gathering tables;
- settlement generation uses them.

**Decision: REINTERPRET + RETEXTURE, likely prune the 2x4 player-build variant.**

Use a high-status dining/meeting surface appropriate to Japanese elite interiors. The huge 2x4 banquet-table visual is not automatically retained just because generation uses it; if hidden, its generation symbols/layouts must be replaced with 2x2 or another retained object.

#### `DankPyon_RoyalEndTable`

Actual role:
- directly adjacent to bed head;
- bed Comfort +0.1.

**Decision: REINTERPRET + RETEXTURE.**

Treat as a small elite room furnishing/support stand. `脇息` may inspire visual language, but the mechanic is a bed facility, so do not label it `脇息` unless the function/placement is made honest.

#### `DankPyon_RoyalDresser`

Actual role:
- 2x1;
- bed Comfort +0.10;
- Beauty 5.

**Decision: REINTERPRET + RETEXTURE.**

Use `棚 / 厨子`-class room furnishing rather than a Western chest of drawers.

#### `DankPyon_RoyalTudorBed`

Actual role:
- 2x2 double bed;
- Beauty 100;
- Comfort 0.95;
- BedRestEffectiveness 1.15;
- ImmunityGainSpeedFactor 1.07;
- gold + 200 silk;
- **22 layout-cell uses plus direct generation links in the baseline source ledger**.

**Decision: GENERATION-IMPORTANT — REINTERPRET + RETEXTURE.**

Do not keep the Tudor canopy-bed visual. A high-status Japanese sleeping arrangement can draw visual inspiration from `御帳台` and elite bedding, but the label should remain generic unless the occupied footprint/sleeper orientation actually represents the historical structure.

This Def also contains significant medical/rest bonuses. Retain those only as MO balance unless a later balance pass decides the stat values themselves are inappropriate; do not strengthen them further for historical flavor.

---

## 5. Recreation / gaming objects

### `Dankpyon_CupAndDice`

Loaded role:
- cerebral game;
- JoyGainFactor 1.0;
- small object.

**Decision: REINTERPRET + RETEXTURE to a Japanese small-board/game set, strongest candidate `双六`.**

### `DankPyon_Tarocco`

Loaded role:
- 2x2;
- cerebral gaming;
- requires adjacent chairs/stools;
- JoyGainFactor 1.3.

**Decision: REINTERPRET + RETEXTURE to `囲碁` / board-game table if interaction geometry is acceptable.**

Go is an exceptionally strong pre-Edo referent: Shōsōin holdings include Nara-period go boards and stones.

### `DankPyon_RimWar`

Loaded role:
- 2x3 dedicated “war game” table;
- JoyGainFactor 1.3.

**Decision: HIDE from baseline.**

There is no need to invent a Japanese war-game table solely to preserve a redundant large recreation Def. Keep the Def for compatibility.

Historical anchors:
- Shōsōin game-set catalogue includes go and sugoroku sets:
  - https://shosoin.kunaicho.go.jp/search-result/?operator=AND&p=1&type=treasures&usage=gamesets
- `木画螺鈿双六局`:
  - https://shosoin.kunaicho.go.jp/treasures/?id=0000012217&index=12

---

## 6. Ice-storage family

### `DankPyon_IceCellar`

Loaded role:
- 3x3 storage for ice blocks.

**Decision: REINTERPRET + RETEXTURE to `氷室`.**

This is one of the strongest direct mappings in the whole furniture/architecture audit. Japanese ice chambers are recorded in ancient sources; MAFF notes `氷室` in `日本書紀` and winter ice/snow storage for summer court use.

Historical anchor:
- https://www.maff.go.jp/j/pr/aff/2506/event01.html

### `DankPyon_IceBlock_Maker`

Loaded role:
- 1x1 wooden processor;
- freezes water into ice below -1°C;
- 2-day process.

**Decision: CONDITIONAL KEEP / REINTERPRET.**

Treat it as a game abstraction for winter ice preparation/packing, not as an assertion that a specific historical wooden “ice mold” device existed.

The process is acceptable if it feeds the `氷室` gameplay loop without creating free refrigeration.

### `DankPyon_IceChest`

Loaded role:
- 2x1 insulated chest;
- consumes ice;
- `CompHeatPusherPowered` actively cools surrounding room toward roughly -10°C.

**Decision: HIDE from baseline.**

Mechanically this is a room refrigerator/freezer, not merely insulated ice storage. The `氷室` already provides the historically credible storage branch. Do not keep an active room-freezer merely because it is fueled by ice.

---

## 7. Production-support furniture

### `DankPyon_RusticCookingTools`

Loaded role:
- 2x1;
- iron + wood;
- facility adding +6% work speed to nearby rustic cooking table;
- **101 references**, including settlement layouts.

**Decision: REINTERPRET + RETEXTURE.**

Keep as cooking utensils/tool stand. Remove Western kitchen-table presentation but preserve the generic facility role.

### `DankPyon_TableBaking`

Loaded role:
- 2x1 baking tools;
- +6% oven work speed;
- **28 references**.

**Decision: HIDE from baseline; late Nanban conditional.**

It belongs with the already-late/conditional oven branch. If hidden, replace it in generated layouts so the settlement system does not keep spawning an otherwise unavailable Western baking station.

### `DankPyon_MendingBench`

Loaded role:
- 2x1;
- repairs clothes, armor and weapons;
- consumes MO repair tools.

**Decision: KEEP / RETEXTURE lightly.**

This is a useful generic MO maintenance mechanic. Keeping it in Japanization does **not** absorb the separate Project-level Repair/Reuse candidate; Japanization is simply retaining an MO-owned system for MO users.

### `DankPyon_Apiary`

Loaded role:
- 1x1;
- produces honeycomb / queen-bee outcomes;
- temperature constrained;
- uses a custom producer/refuel behavior.

Historical boundary:
- `日本書紀` records a failed bee-keeping attempt in 643;
- Heian sources record domestic honey tribute;
- late-Heian literature depicts both nobles and commoners keeping bees;
- documentation is sparse through Kamakura/medieval periods;
- systematic old-style apiculture becomes much clearer in Edo.

**Decision: CONDITIONAL KEEP / REINTERPRET, not a core RusticFurniture unlock.**

The existence of pre-Edo bee keeping is enough to avoid calling it anachronistic, but not enough to make an efficient apiary a generic early-medieval household technology.

Move it to a separate rare/specialized production branch if retained, and retexture the hive/enclosure toward a Japanese old-style form. Do not use the RusticFurniture node as its historical justification.

Sources:
- Japan Beekeeping Association:
  - https://beekeeping.or.jp/beekeeping/history/
  - https://beekeeping.or.jp/products/honey/

---

## 8. Kiln and fired-clay output

### `DankPyon_Kiln`

Loaded role:
- 2x2 stone kiln;
- Stonecutting prerequisite;
- described as firing raw clay into bricks;
- current process chain produces `DankPyon_BlocksClay`, which feeds many MO Western/patterned construction/floor outputs.

**Decision: KEEP THE DEF AS A REUSE TARGET, BUT DISABLE/HIDE THE BASELINE CLAY-BLOCK PROCESS UNTIL IT HAS A VALID JAPANESE OWNER/OUTPUT.**

The kiln itself is not the problem. The current bundled output ecosystem is.

Japanization must not retain:
- Western brick/block progression;
- fleur-de-lis ceramic floors;
- Versailles-style floors;
- other Western decorative floor families

merely to justify the kiln.

Possible future consumers:
- pottery/ceramics;
- roof tile;
- historically valid fired-clay building material;
- another owner Mod that conditionally attaches a justified process.

Until such a process is owned, the player should not see an otherwise-useless Japanized kiln.

This supersedes the earlier shorthand in `ArchitectureAndReligionBoundaries.md` that listed the MO kiln as a generally reusable finished element without qualifying its current output chain.

---

## 9. Floors, rugs and decorative architecture

### Plain/generic floor surfaces

**KEEP selectively:**
- generic rough/cobble/ruined stone surfaces where the material and appearance can plausibly represent ordinary paving;
- earthen floor;
- simple wood floor.

### Western pattern families

**HIDE from baseline:**
- fleur-de-lis patterns;
- Versailles patterns;
- overt Western heraldic decorative floors;
- other purely cosmetic western patterns with no unique gameplay role.

A visual-only decorative floor does not justify a historical reinterpretation if removing it leaves no gameplay gap.

### Rugs / carpets

- do not rename Vanilla/MO carpet/rug systems into `畳`;
- plain generic floor coverings may be retained if they remain useful and visually honest;
- heraldic/cross/fantasy-animal rugs follow their Western/fantasy content branch and should normally be hidden;
- purpose-built Japanese tatami/mat content remains external/future-owner territory.

---

## 10. Generation-safety rule

Furniture/architecture Japanization is not implementation-ready until every **HIDE** decision is checked against:
- `StructureLayoutDef`;
- `SymbolDef`;
- site/quest generation;
- settlement generation;
- player/AI build menus;
- research unlocks.

For a generation-used Def, choose one of:
1. keep the same upstream Def and reinterpret/retexture it;
2. patch all generator symbols/layouts to a retained substitute;
3. disable the entire upstream content branch only if all dependent generation is also disabled safely.

Never hide a player-build Def while allowing MO site generation to keep spawning its Western/fantasy form unnoticed.

High-priority generation-critical examples already proven by the XML audit:
- `DankPyon_CastleWall`: 8,565 layout-cell uses via KCSG symbols; 8,568 generation refs including direct links;
- `DankPyon_CastleWallEmbrasures`: 342 layout-cell uses via KCSG symbols; 344 generation refs including direct links;
- `DankPyon_RusticDoor`: 911 layout-cell uses via KCSG symbols; 917 generation refs including direct links;
- `DankPyon_ReinfocedLogGate`: 122 layout-cell uses via KCSG symbols; 126 generation refs including direct links;
- `DankPyon_RusticCloset`: 83 layout-cell uses via KCSG symbols; 87 generation refs including direct links;
- multiple Royal furniture Defs: 15–47 refs each.

---

## 11. Resulting architecture principle

Japanization should not try to recreate “a full Japanese furniture pack.”

Its job is narrower:

- preserve MO Defs when their mechanics are useful;
- replace Western presentation with an honest Japanese functional referent;
- remove redundant Western cosmetic variants;
- patch MO generation so hidden content cannot leak back into the world;
- leave purpose-built Japanese furniture to existing Japanese furniture Mods or a future owner when a genuinely new mechanic is required;
- leave global dining/sleep/room cultural Thoughts to the separate Premodern Culture candidate.

This preserves MO's strongest value—its mature medieval game systems and generated content—without making AMJ inherit the whole Western domestic-content bundle.

## Next audit

1. exact weapon stat/material-cost mapping for MO Def -> Japanese weapon referents, including Heavy Crossbow / Ballista;
2. machine-readable final loaded Def/research/process/generation ledger;
3. faction/site generation validation against all HIDE decisions;
4. only then draft production Patch XML and retexture manifests.
