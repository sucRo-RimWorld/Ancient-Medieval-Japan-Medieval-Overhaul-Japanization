# MO iron supply and trade audit — 2026-10-08

**Authority:** Japanization owns conditional adaptations to MO-owned Defs. Static source audit only; not a loaded-game trade PASS.

## Confirmed from author-supplied Medieval Overhaul 1.6 ZIP

| Source (under `1.6/`) | XML finding | Design consequence |
|---|---|---|
| `Defs/ThingDefs_Items/Items_Resources.xml` | `DankPyon_IronIngot`: `ResourcesRaw`, base MarketValue 1.5; `DankPyon_IronOre`: `DankPyon_RawOres`, base MarketValue 0.4 | MarketValue does not establish final trade price or market volume |
| `Defs/ThingCategoryDefs/ThingCategories.xml` | `DankPyon_RawOres` parent = `ResourcesRaw` | Both ores and ingots may be selected by a merchant's broad category generator; confirm final inventory |
| `Defs/TraderKindDefs/TraderKinds_Base_Medieval.xml` | `DankPyon_Base_Medieval_Standard` explicitly sells ingots 500–800; also has `StockGenerator_Category(ResourcesRaw)` | Reducing explicit ingot stock alone may leave category-generated iron |
| `Defs/TraderKindDefs/TraderKinds_Caravan_Medieval.xml` | `DankPyon_Caravan_Medieval_BulkGoodsMerchant` sells ingots 100–200 | Direct trader inflow |
| `Defs/TraderKindDefs/TraderKinds_Caravan_Soren.xml` | `DankPyon_Caravan_Medieval_BulkGoodsMerchant_Soren` sells ingots 200–350; other raw ore/Coal generators are BuyTradeTag/BuySingleDef | Buy-side generator != sales. This trader name appears only in its own definition in the supplied MO 1.6 XML; actual active use remains unverified |
| `Defs/FactionDefs/Factions_NobleHouse.xml` | The NobleHouse parent references normal MO settlement/bulk caravan trader kinds | Def-level route for ordinary MO merchants, not an observed merchant frequency |
| `Patches/ToggleOptions/MOSetting_MetalChain.xml` | **metalChain inactive:** iron mineable output changes from IronOre to IronIngot; Mine Shaft iron-ore recipes output IronIngot; smelter visibility is removed; other Golem outputs also change | When OFF, **direct mining is an iron-smelting bypass** independent of trade; rebalance the resulting ingot output, not merely ore |

Note: XML-specified stock counts do not guarantee the corresponding traders appear or the generated stock matches at runtime; trader Faction and StockGenerator inheritance must be verified.

## Vanilla and external trade limits

The author-supplied archive contains Medieval Overhaul, not the installed `Data/Core/Defs/TraderKindDefs` for RimWorld 1.6. **Current Vanilla Steel seller counts are not verified.** A public third-party iron/coal mod selects `Base_Neolithic_Standard`, `Base_Outlander_Standard`, `Caravan_Outlander_BulkGoods`, `Caravan_Neolithic_BulkGoods`, and `Orbital_BulkGoods` when adding coal trade: https://github.com/Owlchemist/simple-chains-steel/blob/master/Patches/patch.owlchemist.simplechains.steel.xml . These are useful audit entry points, **not** evidence of current Steel quantities or confirmation of active Vanilla trader inventory.

Other race and Faction mods may introduce their own TraderKindDefs or reuse those Vanilla types. No cross-faction steel availability or total world market dominance can be established without a loaded-profile audit.

## Refined design contract

- **Ironmaking standalone:** limited sand-iron sales/buys are owned by Ironmaking. Never silently edit Vanilla or MO trader availability.
- **MO + Japanization without Ironmaking:** preserve MO iron availability and trade. No optional sand-iron references are required.
- **MO + Japanization + Ironmaking, metalChain ON:** this is the **reference balance profile** for sand iron as the main local ironmaking source, with MO ore subsidiary. Japanization adjusts only MO-owned mineables/Mine Shaft/iron-material seller generators, preserving useful imported iron before domestic smelting.
- **metalChain OFF:** supported **compatibility profile**, not the same scarcity guarantee. Preserve the player's choice; never silently force ON. Test direct ingots from MO mineables and Mine Shaft, and do not apply an IronOre-only patch expecting to affect those outputs.
- **Vanilla and other Faction/Orbital Steel traders:** report as external supply to measure; no automatic global filter in Japanization. An opt-in world-wide ancient/medieval economic profile would require its own agreed owner and scope (Project World Rules is an idea, not an implemented dependency).
- Keep imported ready-to-work metal possible before smelting research; avoid making it an always cheaper limitless substitute for domestic iron. Test quantities, visit frequency, silver constraints, hauling, material conversions and buy/sell arbitrage before fixing rates or prices.
- Use StockGenerator-class-aware filtering. Do not confuse `BuyTradeTag` / `BuySingleDef` with seller stock. Treat `ResourcesRaw` stock as another source to check; Soren trader is only a possible source until its active use is demonstrated.

## Additional MO 1.6 source paths: Vanilla mineables, optional Mines and fuel import

The source ZIP adds three relevant branches beyond `metalChain` and iron trader stock:

| Source (under `1.6/`) | Verified XML behavior | Scope / testing requirement |
|---|---|---|
| `Patches/ToggleOptions/MOSetting_VanillaMineables.xml` | The `vanillaMine` **inactive** branch sets `MineableSteel` and `MineableComponentsIndustrial` scatter commonality to `0` and removes them from `PreciousLump`. Both active and inactive branches add `DankPyon_MineableIron` to `PreciousLump`. | Test the toggle together with `metalChain`; do not assume Vanilla mineable Steel is always absent when MO loads. These are XML operations, not proof of the final generated map. |
| `LoadFolders.xml` and `Mods/Mines/Patches/Recipes_Mining.xml` | The 1.6 `Mods/Mines` folder is included only if `wexman.mines` is active. Its `Excavate_Steel` recipe's `products` is patched to `DankPyon_IronOre>10`. | Optional **third-party Mines extraction path**, additional to MO Mine Shaft; when loaded, account for the output and `metalChain` interaction instead of claiming every iron source was covered. |
| `Patches/ToggleOptions/MOSetting_WoodChain.xml` | Its active `woodChain` branch adds `DankPyon_RawWood` 250~400 to `Caravan_Neolithic_BulkGoods`, `Caravan_Outlander_BulkGoods`, `Visitor_Neolithic_Standard`, `Visitor_Outlander_Standard`. | MO already patches four Vanilla trader types, although **this is wood, not metal**. Fuel-input availability may indirectly affect the economics of charcoal ironmaking; do not mistake these as iron seller changes. |

### Supply balance as an auditable system

Measure supply **by time window and conversion to the same usable-metal output**, not by counting unlike items as equivalent. Categories:

- local: mapped `MineableSteel`, `DankPyon_MineableIron`, sand-iron deposits, MO Mine Shaft and optional `wexman.mines`;
- external: Vanilla/MO/other-Faction sellers, orbital suppliers, trade caravans, sites/quests, starting stock, disassembly and recovered material;
- conversion: yield, fuel use, construction costs, work and required research for each path.

For an interval `T`, compare `E_local(T)`, `E_traded(T)`, and `E_other(T)` in **usable iron equivalents**, after loss/process restrictions. This is a measurement framework, not a formula for guaranteeing exact historical ratios. A higher raw inventory number is not automatically higher accessible iron supply when money, tech, labor and visits constrain access. Compare local-production alternatives at a fixed representative demand as well as total sources.

**Testing priorities:**
1. **Core 2x2:** `metalChain` ON/OFF × `vanillaMine` ON/OFF with MO + Japanization + Ironmaking, plus the unchanged MO + Ironmaking comparison. Record actual map ores/Steel, Mine Shaft recipes and usable metal conversion.
2. **Fuel pair:** `woodChain` ON/OFF on representative metalChain-ON maps. Observe RawWood vendor stock, AMJ/MO coal access, recipe-input price and source availability. Only promote to more exhaustive profile coverage if it changes ironmaking balance.
3. **Optional Mines profile:** co-load `wexman.mines` to verify `Excavate_Steel` outputs and whether metalChain OFF provides an alternate direct ingot route. The MO source only proves the isolated 1.6 Mines compatibility patch; final runtime products are not yet confirmed.
4. **Trader profile:** inspect installed Vanilla 1.6 `Data/Core/Defs/TraderKindDefs` (not available in provided files) plus the actually enabled race/Faction traders and MO seller inheritance. Verify *sales* vs *purchases*, `ResourcesRaw` selection and repeated generated stock; the obsolete 1.4/modified-mod XML values are **not** acceptable substitutes for 1.6 observations.

**Acceptance rule:** Only the **metalChain-ON reference profile** is targeted for "sand iron as the principal local smelting raw material" under a Japanized MO environment. With `vanillaMine` ON, direct Vanilla Steel mining may materially change that outcome; report it separately and decide on any Japanization-owned MO-profile-only mineable adjustment **after** player-facing setting semantics and runtime tests. Neither setting may be silently flipped to pass a test. Ironmaking alone must never suppress Vanilla or MO's existing mineables. Global Vanilla/other-Faction Steel traders remain outside Japanization's blanket patch jurisdiction.

## Additional static audit — MO ore and ingot deep-resource candidates

Author-supplied MO archive SHA-256: `6ed379d7c400db43b3af2a9a7fd6203f7f7e99ca1a670d36b0f73fd1adccc9e3`. XML under `1.6/Defs/ThingDefs_Items/Items_Resources.xml` declares **both** iron ore and iron ingots as deep-resource candidates:

| ThingDef | deepCommonality | deepCountPerPortion | deepLumpSizeRange | MarketValue |
|---|---:|---:|---|---:|
| `DankPyon_IronOre` | 5 | 45 | 20~30 | 0.4 |
| `DankPyon_IronIngot` | 5 | 45 | 20~30 | 1.5 |

The `metalChain` toggle source contains no operation modifying either resource's `deepCommonality` or `deepCountPerPortion`. This creates a **possible direct-ingot deep-drilling bypass even in the metalChain-ON balance reference profile**. Source declaration does **not** confirm active deep generation, deep drilling in a Neolithic/Medieval research profile, or actual extractable ingot count; these remain runtime questions.

The static XML scan in this work session parsed **389 MO 1.6 XML files with 0 parse errors**, and identified 6 MO iron/fuel-related trading stock generators: three direct ingot seller generators, one raw resource category seller generator, one `BuyTradeTag(DankPyon_RawOres)` generator and one `BuySingleDef(DankPyon_Coal)` generator. **Buy generators must never be counted as seller inventories**. The category seller is a possible route, not proof that any specific iron item appears on a given visit.

Supply ledger / acceptance tests must now distinguish **surface, deep, Mine Shaft, external Mines, imports, sand iron, recovered/quest material**. Do not impose a numerical reduction of mineable scatter, deepCommonality or trade ranges before measuring loaded quantities, and do not patch the MetalChain setting behind the user's back.

## Executable source inventory (2026-10-08)

Reusable static tool: `Tools/audit_mo_iron_supply.py`; fixture-based tests: `Tests/test_iron_supply_audit.py`.

```bash
python -m unittest discover -s Tests -p test_iron_supply_audit.py -v
python Tools/audit_mo_iron_supply.py /path/to/3219596926.zip --output /tmp/mo-iron-baseline.json
python Tools/audit_mo_iron_supply.py /path/to/3219596926.zip --include-optional Mines --output /tmp/mo-iron-mines.json
python Tools/audit_mo_iron_supply.py /path/to/3219596926.zip --vanilla-core /path/to/RimWorld/Data/Core --output /tmp/mo-iron-with-vanilla.json
```

The tool reads archive or extracted XML and **does not apply RimWorld PatchOperations, resolve all inheritance, or generate actual trader stock**. The basic profile intentionally excludes every conditional `1.6/Mods/*` folder; `--include-optional FOLDER` selects one explicitly. On the author-supplied 1.6 archive: **321 baseline XMLs / 322 with optional Mines, parse errors 0 in each**. The earlier 389 XML scan included 68 optional XMLs unconditionally and **must not** be mistaken for one active load profile. Four fixture tests passed locally before committing this version.

The tool also extracts `butcherProducts` declarations. MO's `DankPyon_IronOre` source contains `<butcherProducts><DankPyon_IronIngot>1</DankPyon_IronIngot></butcherProducts>`; this is a **declared metadata path only**, not proof that a playable butcher/table Recipe converts ore directly to ingots. Test actual consumption/Recipe exposure rather than claiming an exploit from the XML field alone.

**Next gate:** obtain installed Vanilla Core 1.6 trader XML and then loaded Def/StockGenerator samples from the actual active Mod configuration. Source-only tests must never claim runtime coverage.

## Source-derived extraction and trader-use audit (2026-10-08)

The reusable parser now emits `extraction` rows for declared `ThingDef.building.mineableThing` and `RecipeDef.products`, including original XML path, work and scatter data. It also produces `trader_xml_links` showing literal use sites outside the TraderKind's own declaration. **`resolved_active: null` means XML reference counts cannot establish actual trader generation, including possible C# calls.**

The basic MO 1.6 profile exposes **11 declared iron-related extraction entries**, including `DankPyon_MineableIron` with 40 ore output. The Soren TraderKind has no external literal reference in the baseline MO XML. These are static facts, not confirmed game events or active trader frequencies. The additional parser assertions passed the four local fixture tests, while a runtime test remains pending.

## Large MO Golem-rock iron routes (source-level audit)

The ordinary `DankPyon_MineableIron` yields 40 `DankPyon_IronOre`. There are two additional **fantasy-associated** source ThingDefs under `Defs/ThingDefs_Buildings/Buildings_Natural.xml`:

| Source | Declared iron ore output | Route | Restriction |
|---|---:|---|---|
| `DankPyon_GolemRock_Iron_MapGen` | 450 | `GenStepDef DankPyon_GolemRock_Iron` (order 1120, `GenStep_ScatterThings`, 0.25~0.5 candidates per 10k cells) | Separate `Patches/Core/Add_MapGenerator.xml` attaches it to `MapCommonBase/genSteps`; contains `CompProperties_PawnSpawnerOnDestroy` |
| `DankPyon_GolemRock_Iron_Incident` | 1,000 | `IncidentDef DankPyon_GolemImpactor`, keyed in a `golemDict` | `ThreatBig`, `baseChance=0.5`, `minThreatPoints=500`; requires runtime confirmation of actual event/loot access |

When MO `metalChain` is inactive, the toggle also patches the `building/mineableThing` of **both** iron golem rocks to `DankPyon_IronIngot`. They must not be counted as ordinary iron ore-only map mines, nor should their listed yields be assumed safely obtainable without consequences.

**Japanization ownership:** these are existing MO fantasy/generation/incident systems, not Ironmaking-owned sand iron. Audit whether Japanization's historically curated baseline should suppress or disconnect the MapGen and incident while preserving upstream Def identity for compatibility. Treat any suppression together with related golem pawn/faction/generation requirements and the change in total iron supply; do not make a one-field patch that strands incidents or generated maps. This is **a design/implementation gate, not a committed runtime suppression**.

**Ironmaking ownership:** standalone `MO + Ironmaking` must not silently remove either existing MO route. These conditional high-yield sources belong in the combined iron supply comparison, alongside surface mines, deep resources, Mine Shaft and trade.

## World Tech Level interaction — source-level audit

World Tech Level provides independent Research, Items/trader stock, Mineable Resources, and Map GenStep filters. Its `Sources/WorldTechLevel/Patches/Patch_StockGenerator.cs` clamps `StockGenerator_Category`, `StockGenerator_MiscItems`, and `StockGenerator_Tag` in that specific patch, **not `StockGenerator_SingleDef`**. Thus WTL Medieval filtering cannot be assumed to remove the explicit 500~800 MO IronIngot seller stock; verify loaded inventories before designing optional MO conditional patches.

Vanilla `DeepDrilling` is an Industrial research project. With WTL Medieval and Research filtering ON, the deep-drilling path has lower immediate gameplay relevance, but separate settings, existing saves and other Mods can still change the outcome. Keep the deep ore/ingot candidates in the static audit; avoid reporting them as universally accessible.

Reference:
- https://github.com/m00nl1ght-dev/WorldTechLevel/blob/main/Sources/WorldTechLevel/Patches/Patch_StockGenerator.cs
- https://github.com/m00nl1ght-dev/WorldTechLevel/blob/main/Sources/WorldTechLevel/Patches/Patch_GenStep_ScatterLumpsMineable.cs
- https://github.com/m00nl1ght-dev/WorldTechLevel/blob/main/Sources/WorldTechLevel/Patches/Patch_MapGenerator.cs
- https://rimworldhub.com/wiki/thing/DeepDrilling?type=ResearchProjectDef

## Pending loaded tests

1. Read actual installed RimWorld 1.6 Core trader XML for **Steel**; inspect all trader classes, category paths, and sell/buy generators. Do not copy numerical amounts from modded/older logs.
2. Test `Vanilla + Ironmaking`, `MO + Ironmaking`, `MO + Japanization`, and `MO + Japanization + Ironmaking`. For the integrated MO profile run `metalChain` ON/OFF × `vanillaMine` ON/OFF as a 2×2, with `woodChain` paired representative cases.
3. Capture actual loaded `TraderKindDef`, Faction, StockGenerator type, item source, sale vs purchase, quantity and price for base, caravan and any relevant orbital/external merchant.
4. Check `ResourcesRaw` and `DankPyon_RawOres` inclusion, **deep-resource ore and ingot generation/actual mining**, direct ingot surface deposits and Mine Shaft output, trade restocking and simulated 1–2-year iron purchases/production. The deep-ingot path must be tested even with metalChain ON.
5. Check combined MO + AMJ + user's supported race/Faction Mod profile for new seller paths. Do not globally rewrite unrelated stock generators to force a pass.
6. Only then choose item-specific stock-range changes and executable automated tests. No runtime changes or exact numeric balance are authorized by this static audit.

See `Docs/Design.md`, `Docs/Research/MedievalOverhaulJapanizationIntegrationMatrix.md`, and `Docs/Research/MedievalOverhaulJapanizationProductionPatchManifest.md`.
