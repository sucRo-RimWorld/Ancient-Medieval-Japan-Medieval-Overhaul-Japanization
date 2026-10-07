# Medieval Overhaul Japanization — Target Research Graph

**Status:** Project-owned pre-split target graph for `AMJ - Medieval Overhaul Japanization`.

This document supersedes the earlier 67-node first-pass table **for the intended
player-visible research structure**. The original audit remains useful as the
upstream inventory/history of decisions.

No production XML is implemented here. Exact research costs, UI coordinates,
and final labels remain implementation work after a dedicated Japanization
repository exists.

## 1. Core rule

Japanization does not preserve MO's research-node count.

Prefer:
- reusing an existing MO/Vanilla `ResearchProjectDef` identity where a useful
  Japanese gameplay role remains;
- moving retained ThingDefs/Recipes/Processes between existing research nodes;
- hiding redundant Western/fantasy/tier nodes while keeping their Defs for
  compatibility;
- introducing a new ResearchProjectDef only when no existing retained identity
  can represent a genuinely distinct gameplay decision.

The visible graph is organized by **real technique / process / equipment role**,
not by generic “Basic / Intermediate / Advanced / Noble” tiers.

---

## 2. Baseline visible graph

### A. Agriculture / food

```text
DankPyon_BasicAgriculture  農耕
├─ DankPyon_PlowedSoil     耕起
├─ TreeSowing              樹木栽培
│  └─ Cocoa                果樹栽培
└─ DankPyon_Watermill      水車製粉
   [also requires basic woodworking]

DankPyon_BasicCooking      基礎調理
├─ DankPyon_Grill           直火焼き
├─ DankPyon_StewPot         煮炊き
└─ Pemmican                 食品保存
   └─ retained drying-rack preservation outputs
```

Decisions:
- `DankPyon_IntermediateAgriculture` and
  `DankPyon_AdvancedAgriculture`: **hide/merge outputs** into actual
  technique/equipment nodes. Do not keep abstract agriculture tiers.
- `DankPyon_TreeGriffonBerry`: **hide**.
- `DankPyon_IntermediateCooking` and
  `DankPyon_AdvancedCooking`: **hide/merge retained recipes** into actual
  cooking-method nodes.
- `DankPyon_Smoker`: **hide**.
- `DankPyon_Oven`: **hide from baseline**; only a future explicitly
  late-contact/Nanban output set can justify exposing it.
- `Brewing`: **remove from the baseline Japanized MO tree**. A future
  Fermentation/Brewing owner may connect its own research without becoming a
  Japanization dependency.
- MO food buffs remain Recipe/Hediff-level balance decisions and are not
  justified by a research tier alone.

### B. Wood / construction / domestic craft

```text
DankPyon_Lumber             木工
├─ DankPyon_RusticFurniture 生活木工・建具
│  ├─ DankPyon_RusticStorage 収納・保管
│  └─ ComplexFurniture       指物・上等調度
│     └─ DankPyon_RoyalRusticFurniture  上層調度・格式建築
├─ DankPyon_Presser          圧搾加工
└─ DankPyon_Watermill        水車製粉
   [also requires agriculture]

Stonecutting                石材加工
└─ selected Japaneseized wall / ice-storage / kiln outputs

DankPyon_Engineering        機構・土木
└─ only retained mechanisms that genuinely need a higher craft/infrastructure gate
```

Important:
- `DankPyon_CastleWall` stays generation-compatible but maps to a high
  `築地塀 / 練塀`-class enclosure, not a stone castle-base `石垣`.
- `DankPyon_TudorWall` maps to timber-and-earth `土壁`.
- `DankPyon_Kiln` does not become visible merely because the Def exists.
  A historically valid fired-clay output owner must exist first.
- `DankPyon_Windmill`: **hide**.
- `DankPyon_CarrierBirds`: **hide**.
- `DankPyon_Exploration`: may remain as a compact
  `旅支度・測量・探索` node only for actual retained world/exploration
  mechanics; it has **no Carrier Birds prerequisite**. If the final output audit
  shows no meaningful unique gameplay, hide it rather than preserving a label.

### C. Textile / clothing / leather

```text
DankPyon_TextileSpinning   紡績・苧績み
├─ DankPyon_Silk            養蚕・絹
└─ ComplexClothing          裁縫

DankPyon_LeatherTanning    皮革加工
```

Decisions:
- Textile Spinning uses spindle/hand-spinning semantics, not the Western
  spinning-wheel visual as the baseline.
- MO flax-family Defs are reinterpreted as ramie/hemp-fibre processing under
  the existing textile chain.
- common settlement clothing uses the already-selected
  `小袖 / 袴` carriers rather than preserving Western surcoat/tunic/chausses
  research logic.
- Japanization remains an MO apparel reinterpretation layer, not a full
  standalone Japanese clothing pack.

### D. Metal / mining / craft

```text
DankPyon_Mining            採鉱

Smithing                   鍛冶
├─ DankPyon_Steel           鋼加工
├─ DankPyon_BasicBlades     刃物・工具
│  └─ DankPyon_MilitaryBlades  太刀鍛造
│     └─ LongBlades            中世刀剣発達
├─ DankPyon_BasicPolearms   鉾・初期長柄武器
│  └─ DankPyon_MilitaryPolearms  槍・薙刀・長槍
├─ DankPyon_ProtectiveClothing   甲冑製作
│  ├─ DankPyon_ChainArmor        鎖帷子 [late side branch]
│  └─ PlateArmor                 当世具足 [late branch; NOT via ChainArmor]
│     └─ DankPyon_AdornedArmor   装飾甲冑
└─ DankPyon_Jewelry         飾金具・装身具
```

Notes:
- Ironmaking owns Japanese iron production. Japanization uses `Smithing` and
  `DankPyon_Steel` as the **MO-side metalworking connection**, not as a
  replacement Japanese smelting loop.
- `DankPyon_ChainArmor -> PlateArmor` is broken. Chain is a late
  supplementary side branch, not the mandatory middle rung.
- `DankPyon_NoblePolearms`: **hide**, redistribute any retained weapon.
- `DankPyon_BasicMaces`, `DankPyon_MilitaryMaces`,
  `DankPyon_NobleMaces`: **hide as visible research nodes**. The single
  retained `金砕棒` carrier moves under the medieval military
  polearm/heavy-weapon craft branch or Smithing as implementation balance
  prefers; there is no need for a three-tier mace research ladder.
- `DankPyon_Alchemy`: **hide from baseline** after Steel/Tar/Gunpowder are
  detached. Any historically valid medicine/herbal content requires a
  separately justified retained output; fantasy alchemy is not used to keep the
  node alive.
- `DankPyon_Plasteel`: **hide**.
- `DankPyon_Tar`: **hide**.

### E. Bow / crossbow / firearm

```text
DankPyon_HuntingBow        弓製作・狩猟弓
└─ RecurveBow              弓術
   └─ DankPyon_WarBow       軍用和弓

DankPyon_Crossbow          弩
└─ DankPyon_HeavyCrossbow  強弩
   └─ retained small installed 弩 (Scorpio carrier)

DankPyon_Gunpowder         火薬・火縄銃 [late Sengoku]
```

Decisions:
- `Greatbow`: remove from the **Japanized MO progression** unless a later
  loaded-stat check proves it adds a distinct role beyond retained
  `Bow_War`. Vanilla Def existence is not deleted.
- `DankPyon_Ballista`: **hide**; Scorpio already fills the installed-crossbow
  niche.
- `DankPyon_Trebuchet`, `DankPyon_RepeaterBallista`: **hide**.
- Gunpowder is detached from Alchemy and placed at the late-Sengoku edge.
- `DankPyon_Handgonne` requires the already-defined single-shot matchlock
  mechanical patch; retexture-only conversion is forbidden.

---

## 3. Nodes removed from the visible Japanized MO tree

### Historical/fantasy mismatch

- `DankPyon_CarrierBirds`
- `DankPyon_Windmill`
- `DankPyon_Plasteel`
- `DankPyon_Tar`
- `DankPyon_TreeGriffonBerry`
- `DankPyon_Smoker`
- `DankPyon_Ballista`
- `DankPyon_Trebuchet`
- `DankPyon_RepeaterBallista`

### Redundant abstract tiers

- `DankPyon_IntermediateAgriculture`
- `DankPyon_AdvancedAgriculture`
- `DankPyon_IntermediateCooking`
- `DankPyon_AdvancedCooking`
- `DankPyon_NoblePolearms`
- `DankPyon_BasicMaces`
- `DankPyon_MilitaryMaces`
- `DankPyon_NobleMaces`

Retained outputs from these nodes move to the closest actual
technique/equipment node. Hidden ResearchProjectDefs remain present for
compatibility unless implementation proves removal safe.

### Vanilla nodes MO should stop presenting as Japanese-medieval progression

- `Devilstrand`
- `PsychoidBrewing`
- `CarpetMaking`
- `PassiveCooler`

Japanization removes these from the reconstructed MO historical flow. It does
not globally delete the Vanilla research/Def outside the MO/Japanization
profile.

`Brewing` is likewise not a baseline Japanese-MO research branch; it remains
available to the appropriate external/standalone owner profile rather than
being relabeled into sake brewing inside Japanization.

---

## 4. Conditional / late branches

### Candle making

`DankPyon_CandleMaking` may remain as a **late-medieval optional craft
branch**. It does not gate basic lighting, because the baseline already has
torch/oil lighting.

### Oven / baking

`DankPyon_Oven` is hidden in the baseline. Re-enable only if an explicitly
supported late-contact recipe subset gives it a gameplay purpose without
reintroducing the Western pie/cake/bread progression wholesale.

### Exploration

`DankPyon_Exploration` is retained only if its actual world/gameplay outputs
survive the final output audit. It no longer depends on Carrier Birds.

### Apiary

The MO Apiary is not justified by Rustic Furniture. If retained, it belongs to
a specialized production unlock rather than the ordinary furniture node. No
new visible node is created merely for the Apiary until that branch's gameplay
value is confirmed.

---

## 5. DBH for Medieval overlay

DBH for Medieval remains optional. When present with Japanization, the visible
overlay is:

```text
DankPyon_BasicAgriculture
└─ ES_BasicIrrigation
   └─ ES_IntermediateIrrigation
      ├─ ES_IrrigationCanal
      └─ ES_SluiceGate

ES_HygienicConcept          衛生・清潔の経験知
┐
├─ ES_MedievalFixtures      洗浄・入浴設備
┘  [also requires ES_BoilWater]
ES_BoilWater                湯沸かし
   ├─ ES_WashingKit
   └─ ES_MedievalFixtures
      └─ ES_SimpleBathtub -> 湯槽

PrimitiveWell               retained low-tech DBH water source
ES_ExcretionPit             retained low-tech latrine
```

Exact prerequisite decisions:

| DBH research / object | Target prerequisite treatment |
|---|---|
| `ES_BasicIrrigation` | add/reuse `DankPyon_BasicAgriculture` as the MO/Japanization integration parent |
| `ES_IntermediateIrrigation` | require `ES_BasicIrrigation`; **remove `Plumbing`** |
| `ES_BoilWater` | early independent DBH node; no modern Plumbing parent |
| `ES_HygienicConcept` | early independent empirical-cleanliness node; remove modern/germ-theory framing and Plumbing dependency |
| `ES_MedievalFixtures` | require `ES_HygienicConcept` + `ES_BoilWater`; expose only retained washing/bathing outputs |
| `ES_ManualPumps` / `ES_ManualPump` | hidden/disconnected |
| `ES_WindPumps` / `WindPump` | hidden/disconnected; remove `DankPyon_Windmill` prerequisite rather than rerouting it |
| `ES_SimpleToilet` | hidden from baseline |
| `ES_FilterDevice` / `ES_Filter` | hidden from baseline |
| DBH `SewageOutlet` | remove from the retained MedievalFixtures unlock set |
| `PrimitiveWell` | retain; no new Japanization well Def |
| `ES_ExcretionPit` | retain as primitive latrine |
| later DBH `ElectricPumps` | when later tech is deliberately allowed, bypass hidden ES_WindPumps so Industrial DBH is not deadlocked |
| later DBH `SepticTanks` | do not preserve DBH-for-Medieval's historical “water purification” reinterpretation merely to support the hidden filter branch |

DBH irrigation remains its own PipeNet/sprinkler abstraction and does not
become Waterworks.

---

## 6. Optional AMJ integration edges

These are **conditional edges**, not baseline prerequisites.

### Grains

- Grains keeps its own ordinary `MO + Grains` compatibility.
- Japanization preserves/repositions the MO Millstone/wheat/flour research path
  expected by that contract.
- No Grains research is copied into this graph.

### Ironmaking

- `Smithing` / `DankPyon_Steel` are the MO-side connection points.
- Ironmaking owns sand iron and Japanese furnace progression.
- Additional MO ore/Mine-Shaft rebalance exists only in
  `MO + Japanization + Ironmaking`.

### Rice / Preservation / Fermentation / Brewing

- each owner keeps its own gameplay/research;
- Japanization only adapts retained MO equipment/research visibility where the
  owner has an optional compatibility path;
- no independent owner becomes a prerequisite of Japanization.

---

## 7. Graph invariants

Production implementation must prove:

1. no visible research depends on a hidden research node;
2. every retained visible MO output has exactly one intended visible unlock
   route;
3. every hidden ResearchProjectDef may remain for compatibility but unlocks no
   baseline-visible Western/fantasy output;
4. `ChainArmor` is not a prerequisite of `PlateArmor`;
5. `Alchemy` is not a prerequisite of Steel or Gunpowder;
6. `CarrierBirds` is not a prerequisite of Exploration;
7. `Windmill` is not a prerequisite of any retained baseline item or optional
   DBH item;
8. retained DBH irrigation has no `Plumbing` prerequisite;
9. hidden DBH pump/filter/toilet branches do not block deliberately enabled
   later DBH technology;
10. Grains/Ironmaking/other standalone owners remain functional without
    Japanization;
11. static decision/loadout/source-ledger checks pass;
12. runtime supported profiles pass Pickle/RimTest with ERROR 0.

---

## 8. Production manifest consequence

The future Japanization repository should implement the graph in this order:

1. **Research visibility/prerequisite patch**
2. **unlock redistribution patch** for ThingDefs/RecipeDefs/ProcessDefs
3. **MO Def label/description/retexture patch**
4. **PawnKind/Faction loadout patch**
5. **DBH-for-Medieval optional overlay**
6. **other optional owner integrations**
7. static ledger validation
8. Pickle/RimTest runtime profiles

Do not begin by changing textures or individual recipes before the research
graph/unlock redistribution is defined, or hidden Western branches will leak
back through another unlock path.
