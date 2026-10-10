# Medieval Overhaul Japanization — Production Patch Manifest

**Status:** Project-owned pre-split implementation manifest.

This is the implementation breakdown for the future dedicated
`AMJ - Medieval Overhaul Japanization` repository.

It does **not** contain production XML and does not make this Project repository
a runtime dependency.

## 1. Patch-order contract

Production patches should be organized by semantic ownership rather than by
file-name luck.

Recommended order:

1. **Research visibility / prerequisite reconstruction**
2. **Unlock redistribution**
3. **ThingDef / RecipeDef / ProcessDef historical curation**
4. **MO-owned label / description / graphic rewrites**
5. **PawnKind / Faction loadout and presentation rewrites**
6. **Official optional compatibility overlays**
7. **static ledger validation**
8. **runtime Pickle / RimTest profiles**

If RimWorld patch ordering makes two packages compete for one field, one package
must become the final semantic owner. Do not rely on accidental “last patch
wins.”

---

## 2. Proposed production file groups

Exact filenames may change, but responsibilities should remain separated.

### `Patches/Research/ResearchVisibility.xml`

Owns:
- hide/remove from the visible Japanized MO tree;
- detach Vanilla research that MO had moved into its medieval tab;
- conditional visibility for late/optional branches.

Driven by:
- `Docs/Research/Data/MedievalOverhaulJapanizationResearchGraph.csv`.

Must cover at least:
- hidden fantasy/Western branches;
- merged abstract agriculture/cooking/mace/noble tiers;
- Vanilla nodes detached from the MO historical progression;
- conditional Candle/Exploration/Oven treatment.

### `Patches/Research/ResearchPrerequisites.xml`

Owns:
- the final visible MO prerequisite graph;
- breaking `Alchemy -> Steel/Gunpowder`;
- breaking `ChainArmor -> PlateArmor`;
- moving crossbows to the ancient military side;
- moving Watermill earlier;
- removing CarrierBirds from Exploration.

Must not:
- add standalone AMJ module research as a mandatory prerequisite;
- encode DBH-specific prerequisites in the baseline MO file.

### `Patches/Research/ResearchUnlockRedistribution.xml`

Owns:
- moving ThingDefs, RecipeDefs and ProcessDefs away from hidden/merged
  ResearchProjectDefs;
- assigning each retained output exactly one intended visible unlock route.

High-risk examples:
- retained recipes from Intermediate/Advanced Cooking;
- retained weapons from Noble/Mace branches;
- Scorpio installed-crossbow unlock after Ballista research is hidden;
- `Polehammer -> 金砕棒` after Mace research nodes are hidden;
- `Falchion -> 打刀` and `Greatsword -> 大太刀` after the sword graph is
  simplified;
- Drying Rack / preservation outputs after generic cooking tiers are removed.

### `Patches/Production/ProductionProcesses.xml`

Owns MO production-system changes caused by Japanization:
- Watermill: retain grain milling, disable baseline 2x lumber process;
- Presser: expose only retained processes;
- Smoker: hide/disconnect baseline process;
- Kiln: do not expose current Western clay-block/decorative-floor chain without
  a valid output owner;
- Drying Rack: retain generic preservation system.

Does **not** own standalone AMJ recipes.

### `Patches/Food/FoodRecipes.xml`

Owns:
- curation of MO-owned Western/fantasy recipes;
- redistribution to BasicCooking / Grill / StewPot / Food Preservation;
- removal/neutralization of inappropriate strong food Hediffs where the
  retained Japanese recipe no longer justifies them.

Does not:
- create a new Sake/Fermentation/Preservation gameplay module;
- copy Grains or Rice recipes.

### `Patches/Textiles/TextilesAndClothing.xml`

Owns:
- MO flax-family reinterpretation to ramie/hemp-fibre semantics;
- common-clothing carrier mapping already fixed by the clothing audit;
- removal of Western settlement-clothing hard requirements;
- MO-owned apparel labels/material constraints where required.

Does not become a full Japanese clothing catalogue.

### `Patches/Architecture/ArchitectureAndFurniture.xml`

Owns:
- TudorWall -> Japanese timber/earth wall;
- CastleWall -> generation-compatible high Japanese compound wall;
- Royal/Rustic furniture reinterpretation;
- hidden Western cosmetic floors/rugs/furniture;
- IceCellar -> 氷室;
- generation-safe substitutions for hidden objects.

Every HIDE decision here must be checked against KCSG
`StructureLayoutDef/SymbolDef` use.

### `Patches/Military/Weapons.xml`

Owns:
- retained weapon carrier labels/stats/research;
- Pike reach patch for `長槍`;
- Handgonne -> single-shot `火縄銃` prototype/final stat patch;
- hiding redundant Western weapon variants.

Driven by:
- military mapping document;
- decision ledger;
- ranged-balance ledger.

### `Patches/Military/Armor.xml`

Owns:
- `挂甲 / 胴丸 / 鎖帷子 / 当世具足 / 南蛮胴` carrier mappings;
- helmet consolidation;
- hiding plate boots/gloves and redundant Western armor variants;
- clan-color variants that preserve MO faction-generation identity.

### `Patches/PawnKinds/PawnKindLoadouts.xml`

Owns:
- removing hard references to hidden Western equipment;
- replacing weapon tags with retained Japanese carrier tags/Defs;
- noble-house child-PawnKind heater-shield removal;
- commoner/guard/archer/footman/elite/lord loadout consistency.

Driven by:
- `Docs/Research/Data/MedievalOverhaulJapanizationLoadoutLedger.csv`.

### `Patches/Factions/FactionPresentation.xml`

Owns only MO-owned faction presentation:
- Western titles/role names;
- Western heraldic presentation;
- retained Brigand/Noble House role Japanization;
- safe handling of hidden implementation factions/sites.

Does not implement the broader AMJ Factions system.

---

## 3. Official optional compatibility groups

### `Patches/Compatibility/DBHForMedieval.xml`

Condition:
- DBH + DBH for Medieval present.

Driven by:
- `MedievalOverhaulJapanizationDBHForMedievalMapping.md`;
- `Data/MedievalOverhaulJapanizationDBHResearchOverlay.csv`.

Owns:
- DBH-for-Medieval research reroutes caused by the Japanized MO profile;
- removal of `DankPyon_Windmill` from the hidden WindPump branch;
- retained washing/bathing/irrigation output set;
- hiding/disconnecting ManualPump/WindPump/SimpleToilet/Filter baseline content;
- later-tech bypass so hidden medieval pump branches do not deadlock deliberately
  enabled Industrial DBH.

Does not:
- reimplement DBH C#;
- merge DBH irrigation with Waterworks.

### `Patches/Compatibility/Grains.xml`

Condition:
- Grains present.

Owns **only** adaptation required because Japanization moved/reconstructed MO
research.

Does not duplicate Grains' ordinary `MO + Grains` compatibility.

### `Patches/Compatibility/Ironmaking.xml`

Condition:
- Ironmaking present.

Owns:
- Japanized MO research connection to Ironmaking;
- additional MO ore/Mine-Shaft and **MO-owned iron trader stock** rebalance specific to
  `MO + Japanization + Ironmaking`.

**Ironmaking owner interface available (source, NOT loaded-game validated; 2026-10-10):**

- Owner: `sucRo-RimWorld/Ancient-Medieval-Japan-Ironmaking`; actual `About/About.xml` packageId `sucro.ancientmedievaljapan.ironmaking`.
- Resource/MapGen: `AMJ_IronSand`, `AMJ_IronSandDeposit`, `AMJ_IronmakingMaterials`, `AMJ_ScatterIronSand`.
- Processing items: `AMJ_Charcoal`, `AMJ_IronBloom`.
- Worktables and Recipes: `AMJ_CharcoalKiln`, `AMJ_SmallIronFurnace`; `AMJ_BurnCharcoal`, `AMJ_SmeltIronSand`, `AMJ_ForgeIronBloom`.
- **Baseline standalone MO compatibility is already owned by Ironmaking:** its conditional `Patches/Compatibility/MedievalOverhaul.xml` routes `AMJ_ForgeIronBloom` via `DankPyon_Anvil` to `DankPyon_IronIngot` (not Steel), and accepts `DankPyon_Coal` as a smelting fuel. Japanization must NOT duplicate or unconditionally reapply this patch.
- **Japanization-only additional contract:** if Ironmaking is loaded, reconcile Japanized MO research prerequisites and balance MO-owned iron deposits/Mine Shaft/deep or golem sources/trader stock. Do not change AMJ IronSand generation or its Vanilla caravan trade in Japanization. `metalChain` ON is a reference balance; OFF is compatibility with its direct-ingot supplies, without forcing user settings.
- All current yield, price and stock-range values are provisional. No validated loaded Defs/trader or safe numerical rebalance exists. The presence of an actual packageId/DefNames does NOT authorize speculative numerical Patch output.

Canonical source: [Ironmaking owner Design](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Ironmaking/blob/main/Docs/Design.md); source merged [PR #7](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Ironmaking/pull/7), commit `f458279c2adb072e55858742bb754913fb27f00c`.

MO trader audit targets (conditional on Ironmaking):
- `DankPyon_Base_Medieval_Standard` — explicit IronIngot 500~800 and `ResourcesRaw` category;
- `DankPyon_Caravan_Medieval_BulkGoodsMerchant` — IronIngot 100~200;
- `DankPyon_Caravan_Medieval_BulkGoodsMerchant_Soren` — IronIngot 200~350, separate ore/Coal **buy-only** stock generators.
Test actual loaded inventory and `MOSetting_MetalChain` ON/OFF before choosing numeric changes. Imports must remain possible before local smelting research.

**Additional mineables / fuel-input gates:**
- `vanillaMine` OFF suppresses `MineableSteel` scatter and removes it from `PreciousLump`; ON does not apply the same suppression. Test `metalChain` × `vanillaMine` as a 2×2 and verify final mineables/ore/ingot outputs, not just the patch XML.
- MO loads `1.6/Mods/Mines` if `wexman.mines` is active; this external `Excavate_Steel` route is patched to `DankPyon_IronOre` x10. Test this optional route separately before claiming all extraction is balanced.
- `woodChain` ON adds `DankPyon_RawWood` 250~400 to four *Vanilla* caravan/visitor trader kinds; assess as a fuel-input market risk, **not** as an IronIngot seller.
- Fuel changes are paired representative cases before expanding full cross-product profile coverage. Record player-configured settings without silently flipping them.

**Deep-resource gate:** MO 1.6 defines `DankPyon_IronOre` and `DankPyon_IronIngot` with `deepCommonality=5`, `deepCountPerPortion=45`, `deepLumpSizeRange=20~30` for **both** ThingDefs. The metalChain toggle does not explicitly remove these fields. Confirm actual deep-resource generation and mining for both resources under metalChain ON/OFF before declaring sand iron the dominant local raw-material route. A proposed balance patch limited to surface commonality, Mine Shaft and traders is not a complete audit until this bypass is addressed or disproved in a loaded game.

**Static-to-runtime gate:** with metalChain OFF, MO mineables and Mine Shaft output IronIngot directly; reducing IronOre supply alone is ineffective. Check broad `ResourcesRaw` trader stock, the nested `DankPyon_RawOres` category, actual use of the source-only Soren TraderKind, seller-vs-buyer generators and installed Vanilla/third-party traders. ON is the reference economic-balance profile; OFF is a compatibility-only scarcity exception and must not be silently changed. No numerical trader patch before observed loaded stock. Detailed evidence: `Docs/Research/MedievalOverhaulJapanizationIronSupplyAudit.md`.

Does not own Japanese smelting/furnace content, ordinary sand-iron trade, or broad world/Trader filtering.

### Future owner integrations

Rice / Preservation / Fermentation / Brewing / Japanese Clothing etc. receive a
Japanization compatibility file only when:
1. the owner exists;
2. the owner has an ordinary MO compatibility contract where appropriate;
3. Japanization's reconstruction creates an additional integration need.

Do not pre-create empty compatibility files.

---

## 4. Retexture manifest

Retexture work must not be scattered across functional AMJ Mods.

The future Japanization repository owns all MO-owned Japanese texture
replacements.

For each retained MO graphic family record:
- DefName;
- existing texPath;
- all directional/variant/mask graphics;
- target Japanese referent;
- whether label/description/stat changes accompany the art;
- generated-site usage;
- optional-DLC/profile state.

No texture replacement is complete until every loaded graphic state resolves.

---

## 5. Static validation gates

Before runtime testing, CI/static tooling must fail on:

1. an unknown/unclassified MO research node in the audited surface;
2. a visible research node depending on a hidden node;
3. a HIDE decision that still has a baseline visible Recipe/Thing/Process route;
4. a hidden or reinterpreted equipment Def still hard-required by an unpatched
   PawnKind;
5. a generation-sensitive hidden Def still emitted by an unpatched KCSG symbol;
6. a retained Japanization retexture target without an AMJ-owned target path;
7. DBH overlay entries depending on hidden `Windmill` or modern `Plumbing`
   in the historical baseline;
8. a standalone AMJ owner accidentally becoming a baseline Japanization hard
   dependency;
9. an MO trader iron-supply rebalance exposed without Ironmaking or trader stock
   that bypasses the conditional supply balance via another generator.

Inputs:
- decision ledger;
- target research graph;
- loadout ledger;
- DBH research overlay;
- generated MO source dependency ledger.

---

### Optional WTL filtering gate

WTL Medieval with Research/Items/Mineable/Map GenStep filters requires its own representative profile: MO's fixed IronIngot `StockGenerator_SingleDef` is not targeted by WTL's Category/Misc/Tag trader generator clamp. Confirm final iron sellers, sand-iron map generation and research exposure. Vanilla `DeepDrilling` is Industrial and thus is not the first balance priority in a medieval research-filtered world; preserve a separate scenario for prior-research or external deep-drilling accessibility. WTL remains optional.

## 6. Runtime validation profiles

Minimum:
1. MO + Japanization
2. MO + Japanization + Grains
3. MO + Japanization + Ironmaking
4. MO + Japanization + Grains + Ironmaking
5. MO + Japanization + DBH + DBH for Medieval

For each:
- final loaded ResearchProjectDef graph;
- no visible orphan/hidden prerequisite;
- representative retained production chains;
- every retained human MO combat PawnKind generates;
- settlement/site generation does not leak hidden Western content;
- ERROR 0.

Additional profiles are added only when a real optional integration exists.

---

## 7. Repository-creation gate

Production Patch XML, textures, About metadata and runtime tests should begin
only after a dedicated Japanization repository exists.

Until then, Project owns:
- target graph;
- research/history audits;
- machine-readable decision/loadout/overlay ledgers;
- implementation manifest;
- source-ledger/static-check tooling.

When the dedicated repository is created:
1. read its new `AGENTS.md`;
2. migrate confirmed specification and tooling;
3. create its authoritative `Docs/Design.md` and `Docs/Coordination.md`;
4. leave Project with a concise roadmap/pointer;
5. do not maintain two evolving implementation specifications.
