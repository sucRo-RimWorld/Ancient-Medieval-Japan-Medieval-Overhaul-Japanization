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

## Pending loaded tests

1. Read actual installed RimWorld 1.6 Core trader XML for **Steel**; inspect all trader classes, category paths, and sell/buy generators. Do not copy numerical amounts from modded/older logs.
2. Test `Vanilla + Ironmaking`, `MO + Ironmaking`, `MO + Japanization`, and `MO + Japanization + Ironmaking`. For the integrated MO profile run `metalChain` ON/OFF × `vanillaMine` ON/OFF as a 2×2, with `woodChain` paired representative cases.
3. Capture actual loaded `TraderKindDef`, Faction, StockGenerator type, item source, sale vs purchase, quantity and price for base, caravan and any relevant orbital/external merchant.
4. Check `ResourcesRaw` and `DankPyon_RawOres` inclusion, **deep-resource ore and ingot generation/actual mining**, direct ingot surface deposits and Mine Shaft output, trade restocking and simulated 1–2-year iron purchases/production. The deep-ingot path must be tested even with metalChain ON.
5. Check combined MO + AMJ + user's supported race/Faction Mod profile for new seller paths. Do not globally rewrite unrelated stock generators to force a pass.
6. Only then choose item-specific stock-range changes and executable automated tests. No runtime changes or exact numeric balance are authorized by this static audit.

See `Docs/Design.md`, `Docs/Research/MedievalOverhaulJapanizationIntegrationMatrix.md`, and `Docs/Research/MedievalOverhaulJapanizationProductionPatchManifest.md`.
