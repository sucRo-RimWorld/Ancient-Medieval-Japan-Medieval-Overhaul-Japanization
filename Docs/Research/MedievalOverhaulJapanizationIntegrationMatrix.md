# Medieval Overhaul Japanization Integration Matrix

**Status:** Project-owned pre-split architecture for `AMJ - Medieval Overhaul Japanization`.

This document defines how Japanization interacts with standalone AMJ modules
and external MO-adjacent systems without becoming a new Core or stealing their
standalone compatibility responsibilities.

It refines the broad rule “Japanization owns MO-side integration” into a
two-layer ownership model.

---

## 1. Two compatibility layers

### Layer A — standalone Mod ↔ MO compatibility

A standalone AMJ Mod must remain able to work with Medieval Overhaul **without**
requiring Japanization when that combination is part of the Mod's supported
profile.

Therefore the standalone owner keeps the minimum MO compatibility needed for
its own gameplay loop.

Examples:
- Grains can reuse MO wheat / flour / Millstone when MO is present;
- Ironmaking can accept/connect to MO metal/fuel resources where needed and owns ordinary trade exposure for its own sand iron;
- Rice Cultivation may attach rice-specific drying/processing to suitable MO
  equipment;
- a future Fermentation/Preservation Mod may attach its own recipes/processes
  to MO equipment.

Japanization must not absorb those patches in a way that turns
`MO + standalone AMJ Mod` into an unsupported configuration.

### Layer B — Japanized MO profile integration

Japanization owns changes that exist because **MO itself is being reconstructed
into the AMJ historical profile**.

Examples:
- moving/replacing MO research nodes;
- hiding/reinterpreting Western/fantasy MO content;
- Japanizing MO-owned art/names/descriptions;
- patching MO PawnKinds/Factions/loadouts;
- adjusting MO iron-ore/Mine Shaft **and MO-owned iron-material trader supply** only in
  `MO + Japanization + Ironmaking`;
- hiding/rerouting DBH-for-Medieval content whose upstream assumptions become invalid under the historical profile;
- resolving conflicts caused by Japanization's own research/Def changes.

This layer is allowed to depend on the presence of the corresponding optional
AMJ/external Mod, because Japanization itself already requires MO.

---

## 2. Conflict-ownership rule

When both layers touch the same upstream area, **do not duplicate the same
semantic patch in two packages**.

Use this order:

1. The standalone owner defines the contract required for
   `MO + standalone Mod`.
2. Japanization treats that contract as an input and adds only the changes
   required by the Japanized MO profile.
3. If Japanization changes an MO research node/Def that the standalone
   compatibility patch references, Japanization must preserve or explicitly
   adapt that contract.
4. Do not copy the standalone Mod's recipes/Defs into Japanization.
5. Do not move a standalone compatibility patch into Japanization merely
   because the patch happens to target an MO-owned Def.

The deciding question is not “who owns the XML target?” but:

> **Would this patch still be required/useful if MO were present but
> Japanization were absent?**

- **Yes** → normally the standalone feature owner.
- **No; it exists because Japanization changed/rebalanced MO** → Japanization.

This rule prevents Japanization from becoming a mandatory bridge pack.

---

## 3. Integration matrix

| Profile / partner | Standalone owner keeps | Japanization owns | Hard dependency? | Key invariant |
|---|---|---|---|---|
| **MO only + Japanization** | n/a | MO research reconstruction, Def/Recipe/Process curation, MO retextures, PawnKind/Faction cleanup | MO only | Japanization must remain useful without any other AMJ Mod |
| **Grains** | dry-field crops, primary processing, fallback wheat/flour/mill; its ordinary MO compatibility such as MO wheat/flour/Millstone reuse | adapt the Japanized MO research graph so Grains' MO contract still works; do not duplicate Grains recipes | optional | `MO + Grains` must work without Japanization |
| **Rice Cultivation** | paddy/rice/items/processing; any rice-specific optional use of MO Drying Rack/equipment | only resolve changes caused by Japanized MO research/equipment visibility | optional | rice never becomes a Japanization feature |
| **Ironmaking** | sand-iron resources, Japanese furnace loop, ironmaking recipes/equipment and ordinary sand-iron trade; ordinary `MO + Ironmaking` compatibility | MO-side research reconnection and additional MO ore/Mine Shaft/**iron-material trader stock** rebalance in `MO + Japanization + Ironmaking` | optional | without Japanization, Ironmaking leaves MO ore and MO iron trading unchanged; with it, imports complement rather than eclipse domestic production |
| **Waterworks** | natural freshwater intake + dug open canals; future consumer API only when a real need exists | currently **nothing**; do not connect MO Watermill to Waterworks merely because both involve water | no integration requirement | MO Watermill remains independent; Waterworks owns no water power |
| **DBH / DBH for Medieval** | DBH owns PipeNet, pumping, storage, hygiene/water consumers; DBH for Medieval owns its C# facilities | Japanize/reroute DBH-for-Medieval research/material/art where it depends on MO; replace hidden Windmill research links | official optional compatibility | DBH canal remains PipeNet/sprinkler system, not Waterworks canal |
| **Hot Springs** | natural spring generation, bathing/tōji, safety/autonomy rules | only MO/DBH-side conflict/research/art resolution; do not absorb bathing gameplay | optional | remote conveyance remains a Hot Springs/Waterworks boundary, not Japanization |
| **Fermentation / Brewing / Preservation** | own fermentation/alcohol/preservation loops and any normal MO equipment hookups required by those Mods | curate MO's own Western food branches and keep Japanized research compatible with optional owner patches | optional | MO Presser/Drying Rack convenience does not transfer gameplay ownership |
| **AMJ Factions** | new Japanese factions, social structure, settlements and faction mechanics | Japanize retained **MO-owned** FactionDefs/PawnKinds and prevent Western gear leakage | optional | transforming MO Noble House is not the same as implementing Japanese faction society |
| **AMJ Clothing / external Japanese clothing Mods** | genuinely new clothing Defs and broader clothing catalogue | MO-owned apparel reinterpretation/retexture and MO PawnKind loadouts | optional | Japanization does not become a full Japanese clothing pack |
| **Living-style Thought / Culture** | Vanilla Thought/Trait/Need/social-norm correction in their own modules | only MO-specific Def/text integration caused by MO content | optional | no global culture overhaul inside Japanization |
| **World Tech Level** | broad world/TechLevel restriction | MO internal historical research reconstruction | strongly recommended, not hard | neither duplicates the other's job |

---

## 4. Grains-specific boundary

Grains already defines a supported `MO + Grains` profile independent of
Japanization.

Therefore Japanization must **not** take ownership of:
- Grains crop balance;
- Grains fallback wheat/flour;
- Grains primary-processing recipes;
- the basic decision to reuse MO wheat/flour/Millstone when MO is installed.

Japanization may:
- move the MO research node that exposes the reused Millstone/wheat path;
- ensure the relocated node still satisfies Grains' compatibility contract;
- Japanize MO Millstone/watermill presentation;
- keep MO Flour/Wheat labels/recipes consistent with the broader Japanized
  profile where that does not overwrite Grains-owned crop balance;
- suppress a duplicate MO food/recipe branch only after confirming Grains'
  route still has a valid consumer.

**Do not create a second “Japanization version” of the Grains MO patch.**

---

## 5. Ironmaking-specific boundary

This profile intentionally has three different meanings:

### `MO + Ironmaking`

- Ironmaking is standalone;
- MO ore deposits / Mine Shaft and MO-owned iron-material trader stock are left as MO owns them;
- Ironmaking makes only the minimum compatibility changes required for its
  outputs/fuels/material chain.

### `MO + Japanization`

- no sand-iron gameplay is invented;
- MO's metal research is historically rearranged;
- fantasy/Alchemy coupling is removed as required;
- MO iron supply, including imports, remains usable because Ironmaking is absent.

### `MO + Japanization + Ironmaking`

Japanization may additionally rebalance **MO-owned supply**:
- surface iron-ore commonality/vein exposure;
- Mine Shaft research/work/output;
- MO-owned iron ingot sales stock (settlement and bulk caravan TraderKindDefs) and category-based resale exposure;
- related MO-side progression.

Goal:
- sand iron becomes the principal Japanese natural-resource route;
- MO iron ore remains a secondary route;
- total available iron does not simply become MO mining + MO trade supply + full sand-iron supply;
- imported iron remains usable before smelting research, but large cheap ingot stocks must not eclipse local smelting;
- Ironmaking owns ordinary sand-iron trade; no unrelated global trader/faction/quest filtering;
- Ironmaking itself does not need to patch MO's resource generator merely to
  support its standalone profile.

MO 1.6's source explicitly configures `DankPyon_IronIngot` for settlement traders (500~800), ordinary bulk caravans (100~200), and Soren bulk caravans (200~350). These are **source-declared ranges**, not tested loaded stock. A Soren `StockGenerator_BuyTradeTag` for raw ore is **buy-side**, not evidence that ores are sold. Verify actual trade inventory and sale/buy behavior with metal-chain ON/OFF. Layer B changes must target only the relevant MO-owned iron stock generators.

**Setting and scope gate:** sand iron as the principal local source is the `metalChain` ON reference balance. OFF switches MO's iron deposits and Mine Shaft ore recipes to direct IronIngot output; it remains a supported compatibility profile without a guaranteed identical scarcity outcome. Do not force ON. The `ResourcesRaw` category can reach IronIngot and the nested RawOres category, so capture actual loaded trader stock, not just explicit SingleDef entries. The source-declared Soren trader has no other direct use reference in the supplied 1.6 MO XML and must not be counted as active supply before runtime validation. Vanilla 1.6 and unrelated Faction/Orbital Steel traders are unverified and outside the conditional MO-only patch. See `Docs/Research/MedievalOverhaulJapanizationIronSupplyAudit.md`.

This is the clearest example of a Layer B patch.

---

## 6. Waterworks / watermill non-integration

Current Waterworks v1 explicitly does **not** own water wheels or mechanical
power and has no required public consumer API.

Therefore:
- MO Watermill does not require Waterworks;
- Japanization does not treat a wet Waterworks canal as the Watermill's power
  prerequisite;
- Waterworks does not acquire a water-power subsystem merely to support MO;
- if a future gameplay feature demonstrates a useful watermill/canal
  interaction, it must be proposed as a new optional integration after
  Waterworks' own core is stable.

This prevents a visually tempting but architecturally false coupling.

---

## 7. DBH for Medieval after the Japanized research tree

DBH for Medieval currently assumes upstream MO research/resources in several
places. Japanization changes some of those assumptions.

Required official compatibility responsibilities:

- do **not** solve the hidden MO `DankPyon_Windmill` prerequisite by moving
  DBH `WindPump` to another Japanized research node. The DBH-for-Medieval
  piston-style `ES_ManualPump` and powered `WindPump` branches are outside
  the baseline ancient/medieval Japanese profile and are hidden/disconnected;
- retain `PrimitiveWell` as the preferred low-tech DBH water-source carrier;
- retain/reinterpret `ES_BoilWater`, `ES_WashingKit`,
  `ES_SimpleBathtub` (as a premodern `湯槽`) and `ES_ExcretionPit`;
- hide the sewer-connected `ES_SimpleToilet` and continuous
  `ES_FilterDevice` baseline branches rather than medievalizing their labels;
- retain the DBH irrigation-network abstraction but remove modern
  `Plumbing` as the historical prerequisite of
  `ES_IntermediateIrrigation`;
- Steel / Component substitutions that deliberately reuse
  `DankPyon_IronIngot` / `DankPyon_ComponentBasic` remain valid unless the
  final metal audit proves otherwise;
- `ES_IrrigationCanal` and `ES_SluiceGate` remain DBH PipeNet/Sprinkler
  infrastructure and must not be merged with Waterworks' open-channel model.

Detailed mapping:
`Docs/Research/MedievalOverhaulJapanizationDBHForMedievalMapping.md`.

The final visible prerequisite DefNames are defined together with the
Japanized MO research graph.

---

## 8. Patch ordering contract

Production implementation should make patch ordering explicit rather than
depend on incidental alphabetical load order.

Conceptual order:

1. MO loads.
2. Standalone AMJ Mods load their Base content.
3. Standalone AMJ Mods' **ordinary MO compatibility** establishes their
   independent `MO + Mod` contract.
4. Japanization performs MO-wide historical restructuring/retexture.
5. Japanization optional integration patches adapt that reconstructed MO to
   detected AMJ/DBH partners.
6. Runtime validation checks the final loaded Def graph.

The actual RimWorld XML mechanism may use `MayRequire`,
`PatchOperationFindMod`, explicit PatchOperations, or code only where
necessary. The design contract is about ownership/order, not a requirement to
use a particular patch primitive.

If load-order mechanics make steps 3–5 unsafe for the same target path,
refactor the patches so one package owns the final write instead of relying on
“last patch wins.”

---

## 9. Test matrix implied by this architecture

Do not test every possible AMJ Cartesian product.

Minimum Japanization profiles:

1. MO + Japanization
2. MO + Japanization + Grains
3. MO + Japanization + Ironmaking
4. MO + Japanization + Grains + Ironmaking
5. MO + Japanization + DBH + DBH for Medieval
6. MO + Japanization + relevant future owner only when its integration exists

Separately, each standalone Mod keeps its own independent compatibility
profiles, for example:
- Vanilla + Grains;
- MO + Grains;
- Vanilla + Ironmaking;
- MO + Ironmaking;
- Waterworks core without MO/Japanization.

For every Japanization profile:
- static decision/loadout/source-ledger integrity;
- final loaded research/Recipe/Process visibility;
- representative PawnKind generation;
- runtime ERROR 0;
- hidden Western/fantasy content must not re-enter through loadouts, sites or
  recipes.

Add a new profile only when a real integration path exists.

---

## 10. Result

Japanization is neither:
- a shared AMJ dependency;
- a home for every MO compatibility patch;
- nor a monolithic “make all installed Mods Japanese” filter.

It is specifically the layer that **reconstructs MO itself and then resolves
the consequences of that reconstruction for supported optional partners**.

Standalone AMJ Mods continue to own the compatibility necessary to remain
standalone.
