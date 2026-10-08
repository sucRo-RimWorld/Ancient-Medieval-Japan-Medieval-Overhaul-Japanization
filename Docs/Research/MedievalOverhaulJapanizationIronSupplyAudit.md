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

## Pending loaded tests

1. Read actual installed RimWorld 1.6 Core trader XML for **Steel**; inspect all trader classes, category paths, and sell/buy generators. Do not copy numerical amounts from modded/older logs.
2. Test `Vanilla + Ironmaking`, `MO + Ironmaking`, `MO + Japanization`, and `MO + Japanization + Ironmaking` in both metalChain ON and OFF modes as applicable.
3. Capture actual loaded `TraderKindDef`, Faction, StockGenerator type, item source, sale vs purchase, quantity and price for base, caravan and any relevant orbital/external merchant.
4. Check `ResourcesRaw` and `DankPyon_RawOres` inclusion, direct ingot deposits and Mine Shaft output, trade restocking and simulated 1–2-year iron purchases/production.
5. Check combined MO + AMJ + user's supported race/Faction Mod profile for new seller paths. Do not globally rewrite unrelated stock generators to force a pass.
6. Only then choose item-specific stock-range changes and executable automated tests. No runtime changes or exact numeric balance are authorized by this static audit.

See `Docs/Design.md`, `Docs/Research/MedievalOverhaulJapanizationIntegrationMatrix.md`, and `Docs/Research/MedievalOverhaulJapanizationProductionPatchManifest.md`.
