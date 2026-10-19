# Medieval Overhaul Japanization Integration Matrix

**Status:** authoritative Japanization owner integration matrix. **2026-10-16 author correction supersedes the old MO-only/optional-AMJ package profile:** Japanization requires MO **plus every active AMJ world-suite Mod**; independent owners remain usable without Japanization.

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

This layer **requires all active AMJ world-suite Mods**. Only external systems such as DBH, WTL, VE and optional third-party frameworks are presence-conditional. A newly finished AMJ world module must be added to Japanization hard dependencies before the full-suite release can claim completion.

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

## 3. Integration matrix — one-way full-suite contract

**Runtime contract:** Japanization → MO + active AMJ modules; standalone AMJ modules **never** depend on Japanization. The currently published package IDs are in `About/About.xml`: Environment, Grains (now incorporating the former Crop Growth Balance), Scenarios, Waterworks and Ironmaking (the Grains historical `core` packageId is deliberately preserved). As future AMJ world components acquire stable packageIds and runnable payloads (Culture, Rice Cultivation, Factions, domestic goods, etc.), **they become required**, rather than optional Japanization plugins. No full AMJ Japanization release should be asserted before the planned required set exists. Archived/deprecated or independently generic tools (CCTO, CCTO for VPE) and third-party WTL/DBH are not automatically part of this world-suite contract.

| Profile / partner | Standalone owner keeps | Japanization owns | Japanization requirement | Key invariant |
|---|---|---|---|---|
| **MO only + Japanization** | — | **unsupported configuration** | **invalid** | A MO-only fallback is not a deliverable |
| **Grains** | grain crops, former CGB six Vanilla/seven MO crop timing values and MO lentil sowing skill 2, thresh, MO-only Straw coproduct, normal MO mill/wheat integration | adapt Japanized research/equipment; **hide MO Hay→Straw drying-rack process** | **required now** | Straw comes from cereals; no copy of Grains recipes |
| **Environment** | Japanese biomes, wild grass, Suge Hay 1 | preserve the direct grass→Hay harvest; MO-specific world presentation only | **required now** | grass/hay is not cereal straw |
| **Scenarios** | Japanese starts | MO story/background integration if meaningful | **required now** | no duplicate Scenarios |
| **Waterworks** | freshwater intake and canals | only relevant MO research/presentation reconciliation | **required now** | no arbitrary MO Watermill→canal merger |
| **Ironmaking** | sand iron and original MO-compatible smelting | complete MO research, ore, Mine Shaft, and MO iron trader rebalance for Japanese setting | **required now** | no MO-only rescue profile; Ironmaking itself standalone |
| **Culture, Rice Cultivation, Factions, future independent AMJ world owners** | each owner controls its domain | integrate retained MO content with the full AMJ profile | **required when final packageId and production module exist** | cannot pretend the suite is complete while owner absent |
| **Wild food foraging (former Wild Food Foraging project)** | **Environment owns all 12 adopted resources, natural spawn, food and gathering** | delivered within existing Environment packageId, no duplicate Defs | **already covered by required Environment**, no standalone WFF dependency | old WFF source/tests historical only; implementation and production validation open |
| **DBH / DBH for Medieval** | hygiene, pipes, C# water consumers | narrow Japanized DBH research and material overlay | external optional | no PipeNet/canal replacement |
| **Other third-party Mods / WTL / VE** | own functions | proven optional compatibility only | external optional | no forced third-party stack |

**Straw-specific compatibility:** full-suite Japanization has Grains by construction. Grains’ existing MO threshing output makes a second Hay→Straw source both unnecessary and historically false. The 1.6 source demonstrates that `DankPyon_DryingRack_Small` and `DankPyon_DryingRack_Big` each list `DankPyon_StrawProcess`. The Japanization patch removes **only those two entries**, keeping the original ProcessDef for reference/save compatibility and preserving other dryer processes. Do **not** delete `DankPyon_Straw`, replace its material consumers or redefine `Hay`. Prior art: archived [Medieval Overhaul Patches](https://github.com/ViralReaction/Medieval-Overhaul-Patches), which instead redirects the dryer to a new DriedHay and outputs straw from milling; our smaller patch adds **no** DriedHay or extra drying step. VE comparison: VE's unrelated crop/processing systems do not justify overriding grain ownership or bundling a VE module. Native 1.6/1.7 loaded-Def/save/gameplay verification remains open.

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

Separate **standalone compatibility** from the **single valid integrated Japanization profile**:

### `MO + Ironmaking`

- Ironmaking is standalone;
- MO ore deposits / Mine Shaft and MO-owned iron-material trader stock are left as MO owns them;
- Ironmaking makes only the minimum compatibility changes required for its
  outputs/fuels/material chain.

### `MO + full AMJ suite + Japanization`

- Ironmaking is already required and provides sand-iron gameplay;
- MO's metal research is historically rearranged;
- fantasy/Alchemy coupling is removed as required;
- MO ore and trade supplement, rather than eclipse, AMJ native ironmaking.

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

**Additional extraction boundaries:** MO also has a `vanillaMine` toggle, with its inactive branch suppressing Vanilla `MineableSteel` while the active branch leaves that suppression unapplied. Therefore any historical scarcity result must name both `metalChain` and `vanillaMine`. The MO 1.6 `wexman.mines` optional patch redirects `Excavate_Steel` to IronOre; test if this external Mod is loaded, without assigning ownership of its base functionality to Japanization. MO `woodChain` additionally adds RawWood to four Vanilla caravans/visitors; that affects fuel economics but is **not** a reason to globally curate Vanilla Steel trade. A test matrix covering metalChain × vanillaMine, plus limited woodChain and Mines probes, is documented in `Docs/Research/MedievalOverhaulJapanizationIronSupplyAudit.md`.

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
5. Japanization integrates the **required AMJ suite as a whole**, with conditional overlays **only for external** partners such as DBH.
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

1. **MO + entire current active AMJ world suite + Japanization** — the only supported core Japanization profile.
2. The identical full suite **+ DBH + DBH for Medieval** — optional external overlay, only if implemented.
3. The identical full suite + any accepted third-party compatibility target, only when meaningful.
4. **Negative dependency checks:** MO + Japanization without Grains, Ironmaking or another mandatory AMJ module must be rejected by dependency resolution rather than advertised as supported.
5. Full-suite 1.6/1.7 loaded-Def audit: both drying-rack menu lists lack StrawProcess, while their other processors remain and Grains thresh yields genuine MO Straw.

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
the consequences of that reconstruction for the **entire required AMJ world suite**; external compatibility remains optional**.

Standalone AMJ Mods continue to own the compatibility necessary to remain
standalone.
