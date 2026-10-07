# Medieval Overhaul Japanization — DBH for Medieval Mapping

**Status:** Project-owned pre-split compatibility design for
`AMJ - Medieval Overhaul Japanization`.

This document audits the supplied DBH for Medieval 1.6-era XML against the
ancient-to-medieval Japan profile. It refines the earlier rule that DBH for
Medieval is an official optional compatibility target.

The goal is **not** to preserve every object merely because the upstream Mod
labels it “medieval.” Each building/research node is checked against Japanese
history and the actual loaded mechanic.

Audited local source:
- author-supplied `Defs.zip`;
- extracted XML under `Defs/` and `Patches/`;
- `DBHforMedieval.dll` is available but this pass does not claim a full
  decompilation/runtime audit.

---

## 1. Core compatibility rule

Japanization may patch DBH for Medieval only when all of the following are
true:

1. DBH / DBH for Medieval is installed;
2. the content is part of the supported ancient-to-medieval Japanese profile;
3. the patch is needed because Japanization restructures MO, or because the
   upstream “medieval” presentation would otherwise introduce a clearly
   out-of-period Japanese technology.

DBH remains the owner of:
- PipeNet;
- water storage/pumping semantics;
- hygiene/thirst/bladder consumers;
- its C# buildings/jobs.

Waterworks remains a separate open-canal infrastructure Mod and does not become
a DBH PipeNet implementation.

---

## 2. Research-node dispositions

| DefName | Upstream role | Japanization disposition | Working historical meaning / action |
|---|---|---|---|
| `ES_HygienicConcept` | “unsanitary leads to disease” concept | **REINTERPRET** | keep only as an empirical cleanliness/health abstraction; rewrite the germ-theory-style description; remove `Plumbing` as a conceptual prerequisite |
| `ES_MedievalFixtures` | toilets/showers/bath fixtures | **SPLIT_OUTPUTS + REINTERPRET** | rebuild as a washing/bathing-fixture node; retain only valid wash/bath outputs; do not use it to medievalize sewer toilets |
| `ES_ManualPumps` | hand pumps | **HIDE** | piston/handle pump is not a normal ancient/medieval Japanese technology |
| `ES_WindPumps` | wind pumps | **HIDE** | powered wind pumping is outside the baseline profile |
| `ES_AnimalSupplies` | pet/livestock supplies | **SPLIT_OUTPUTS / LOW PRIORITY** | retain only historically neutral livestock-water equipment if needed; pet bowl/litter-box bundle is not a core Japanization technology branch |
| `ES_BasicIrrigation` | basic irrigation area | **KEEP / EARLY** | generic irrigation knowledge is valid and may remain independent |
| `ES_IntermediateIrrigation` | canals/inter-row irrigation | **REINTERPRET + REPOSITION** | retain the DBH irrigation-network abstraction; remove `Plumbing` as the historical prerequisite; use `ES_BasicIrrigation` as the main progression parent |
| `ES_BoilWater` | heat water in kettle | **KEEP / EARLY** | basic hot-water preparation; valid prerequisite for bathing/washing equipment |

The exact public Japanese labels remain implementation/localization work. The
research graph should avoid modern scientific wording such as germ theory and
modern “bathroom fixtures.”

---

## 3. Water-source / pump decisions

### Vanilla/DBH `PrimitiveWell` — KEEP as the preferred baseline source

DBH for Medieval patches `PrimitiveWell` with:
- DBH Pipe comp;
- `WaterInlet`;
- user-grid placement;
- a DBH-compatible drinking Job.

This is a much better baseline Japanese water-source carrier than the
hand-pump buildings.

Japanese vertical wells are archaeologically old; ordinary lifting methods used
buckets, ropes, lever systems and pulleys. Reference works note that hand pumps
were adopted after 1897.

Historical anchor:
- コトバンク「井戸」
  https://kotobank.jp/word/%E4%BA%95%E6%88%B8-31656

**Direction:**
- keep PrimitiveWell available;
- Japanization does not need to invent a new well Def;
- Japanese art/description may be patched if the loaded DBH/Vanilla well is
  visually unsuitable;
- runtime test that its DBH inlet can actually support the retained medieval
  network after pump branches are hidden.

### `ES_ManualPump` / `ES_ManualPumps` — HIDE

The upstream description explicitly says the device pumps water via pressure
difference by moving a handle up/down. Its C# comp is a
`WaterPumpingStation` with capacity 750.

This is a piston/handle hand-pump abstraction, not a bucket/tsurube well.

Japanese reference material places adoption of hand pumps after 1897, while
earlier wells used buckets, `釣瓶`, lever or pulley systems.

**Decision:**
- hide `ES_ManualPump`;
- hide `ES_ManualPumps`;
- do not relabel it as `釣瓶`, `はね釣瓶`, or `龍骨車`; its actual
  mechanic/shape is different;
- remove any requirement that retained historical DBH content depend on it.

### `WindPump` / `ES_WindPumps` — HIDE

DBH for Medieval currently:
1. makes `WindPump` require `ES_WindPumps`;
2. makes `ES_WindPumps` depend on `ES_ManualPumps`;
3. when MO is installed, adds `DankPyon_Windmill` directly to
   `WindPump/researchPrerequisites`.

Japanization hides MO's power windmill. The correct fix is **not** to move
`WindPump` to another MO research node; the powered wind pump itself is not
a baseline ancient/medieval Japanese technology.

**Decision:**
- hide `WindPump`;
- hide `ES_WindPumps`;
- the MO `DankPyon_Windmill` added prerequisite becomes irrelevant and should
  be removed/neutralized in the Japanized profile;
- do not substitute a medieval `龍骨車` label. A dragon-bone water-lift is a
  different human-powered mechanism, attested around the medieval/early-modern
  boundary and becoming widespread later.

Historical anchors:
- MAFF pump history: modern agricultural pump equipment begins in Meiji;
  earlier water lifting used wooden devices such as dragon-bone and tread
  wheels:
  https://www.maff.go.jp/kanto/nouson/sekkei/kokuei/tonecho/stock/attach/pdf/01-3.pdf
- コトバンク「竜骨車」:
  https://kotobank.jp/word/%E7%AB%9C%E9%AA%A8%E8%BB%8A-149616

---

## 4. Bathing / washing

### `ES_Kettle` / `ES_BoilWater` — KEEP

The building is a metallic pot placed on a heat cooker to heat water. This is a
generic premodern operation and maps without needing a new system.

**Direction:**
- retain;
- Japanese label/graphic can be audited later;
- place `ES_BoilWater` early;
- do not tie it to modern plumbing.

### `ES_WashingKit` — KEEP + RETEXTURE/REWORD

Loaded role:
- jug + bowl + cloth;
- small hot-water storage;
- table-top washing equipment.

This is a strong generic premodern wash-kit carrier.

**Direction:**
- retain;
- use historically neutral basin/jug/cloth presentation;
- keep as simple washing rather than a modern bathroom fixture.

### `ES_SimpleBathtub` — RETAIN + REINTERPRET as `湯槽`

Loaded role:
- 1x2 wooden bath;
- wooden stuff + small metal cost;
- hot-water storage;
- comfort/joy;
- no modern electric heat source.

The existence of bathing is not the issue. Ancient/medieval Japanese temples
had bathing facilities, and sources/reference works describe wooden or iron
`湯槽`. Medieval temple bathing/施浴 is well attested.

**Decision:**
- retain the mechanic;
- remove “simple modern bathtub” comparison language;
- retexture/relabel toward a wooden `湯槽` / premodern bathing vessel;
- place it under the washing/bathing branch, with hot-water preparation as a
  natural prerequisite;
- do not make it evidence that every ordinary household had a private bath.

Historical anchors:
- Agency for Cultural Affairs, Hokkiji bathing/施浴 history:
  https://kunishitei.bunka.go.jp/heritage/detail/301/00000241
- 世界大百科事典「風呂」:
  https://kotobank.jp/word/%E9%A2%A8%E5%91%82-127856
- 世界大百科事典「湯屋」:
  https://kotobank.jp/word/%E6%B9%AF%E5%B1%8B-652369
- Rekihaku, 1521 `上醍醐西谷風呂指図`:
  https://khirin.rekihaku.ac.jp/en/pid/nmjh_collection/H-743-392-2-12.html

---

## 5. Toilet / sewage

### `ES_ExcretionPit` — KEEP

Loaded role:
- no material cost;
- primitive dug pit;
- Neolithic tech;
- hygiene/social-properness behavior.

This is a valid low-tech toilet abstraction.

Archaeology and documentary research confirms toilets/latrines in ancient and
medieval Japan, including Heian, Kamakura and Sengoku examples.

Historical anchors:
- NDL, `水洗トイレは古代にもあった : トイレ考古学入門`:
  https://ndlsearch.ndl.go.jp/books/R100000002-I000010627462
- NDL, `戦国時代城下町「一乗谷」のトイレ`:
  https://ndlsearch.ndl.go.jp/books/R000000004-I3476503

### `ES_SimpleToilet` — HIDE from baseline

The upstream description explicitly defines it as a toilet that no longer needs
pumping because it is **connected to the sewer line**. It inherits DBH toilet
network behavior.

Japan had ancient/medieval toilets and drains, but that does not make this
specific networked sewer fixture a generic medieval household technology.

**Decision:**
- hide from the normal AMJ historical profile;
- do not relabel it as `厠` while preserving sewer-fixture mechanics;
- use `ES_ExcretionPit` and other historically supportable DBH/Vanilla
  latrine abstractions instead;
- do not let `ES_MedievalFixtures` reintroduce it as a “medieval toilet.”

### DBH `SewageOutlet`

DBH for Medieval moves `SewageOutlet` under `ES_MedievalFixtures`.

**Decision:**
- remove it from the retained medieval-fixtures node;
- do not treat a DBH sewer-network outlet as required Japanese medieval
  infrastructure;
- if a later historically specific drainage/waste system is desired, audit it
  as its own mechanic rather than using the label alone.

---

## 6. Water filtration

### `ES_FilterDevice` — HIDE from baseline

Loaded role:
- 2x2 PipeNet-connected filtration building;
- `WaterFiltration` comp;
- continuously consumes a replaceable `ES_Filter`;
- uses a sand/fiber/charcoal-style narrative;
- upstream requires DBH `SepticTanks`, which DBH for Medieval relabels as
  “water purification.”

A simple cloth/sand filter as a physical possibility does not by itself justify
this **continuous PipeNet treatment building** as a standard ancient/medieval
Japanese technology.

**Decision:**
- hide `ES_FilterDevice` / `ES_Filter` from the baseline Japanized profile;
- do not relabel `SepticTanks` as a medieval Japanese water-purification
  research simply to preserve this building;
- allow WTL/DBH's later-tech profile to own modern treatment if the user enables
  it.

This is another case where implementation mechanics matter more than the
upstream “simple” description.

---

## 7. Irrigation

### `ES_BasicIrrigation` — KEEP

Generic irrigation knowledge is valid and already Neolithic.

### `ES_IntermediateIrrigation` — KEEP / REINTERPRET, remove `Plumbing` parent

Loaded node currently requires:
- DBH `Plumbing`;
- `ES_BasicIrrigation`.

Loaded outputs include:
- `ES_IrrigationCanal`;
- `ES_SluiceGate`.

These are internally DBH network objects:
- `ES_IrrigationCanal` inherits `DubsDirtyPipeBase` and has
  `CompProperties_Pipe mode=Sewage`;
- `ES_SluiceGate` uses DBH `CompProperties_Sprinkler`.

**Decision:**
- keep this branch as the **DBH irrigation-network abstraction**;
- remove generic modern `Plumbing` as the historical research parent;
- retain `ES_BasicIrrigation` as the primary predecessor;
- the visible Japanese presentation should make clear this is an irrigation
  facility, not household sewer/plumbing research;
- do not convert the internal implementation to Waterworks PipeNet/state.

### Waterworks boundary

This DBH irrigation branch and Waterworks are deliberately separate.

Waterworks:
- natural surface-water source;
- visible dug open canal;
- binary wet/dry terrain/network;
- no pump/tank/PipeNet.

DBH for Medieval irrigation:
- DBH PipeNet implementation;
- sprinkler-like `SluiceGate`;
- DBH water-network consumers/sources.

Current rule:
- coexist;
- do not suppress either as a duplicate;
- do not force Waterworks as a prerequisite for DBH irrigation;
- do not turn Waterworks into DBH PipeNet;
- a future adapter only exists if a real gameplay consumer demonstrates the
  need.

---

## 8. Proposed DBH research overlay

The machine-readable target overlay is `Docs/Research/Data/MedievalOverhaulJapanizationDBHResearchOverlay.csv`. The combined MO + DBH prerequisite view is also embedded in `Docs/Research/MedievalOverhaulJapanizationTargetResearchGraph.md`.


Working graph for the retained baseline:

```text
ES_BoilWater
    └─> ES_MedievalFixtures   [rewritten as washing/bathing fixtures]
          ├─ ES_WashingKit
          └─ ES_SimpleBathtub -> 湯槽

ES_HygienicConcept            [empirical cleanliness/health; no germ-theory text]
    └─> ES_MedievalFixtures

ES_BasicIrrigation
    └─> ES_IntermediateIrrigation
          ├─ ES_IrrigationCanal
          └─ ES_SluiceGate

PrimitiveWell                 [retained DBH water inlet]
ES_ExcretionPit               [retained low-tech toilet]
```

Baseline hidden/disconnected:

```text
ES_ManualPumps -> ES_ManualPump
ES_WindPumps   -> WindPump
ES_SimpleToilet
ES_FilterDevice / ES_Filter
DBH SewageOutlet from the medieval-fixtures branch
```

Implementation detail:
- `ES_MedievalFixtures` should require both the empirical cleanliness node and
  hot-water preparation **unless runtime UX proves that this creates a
  pointless double gate**. Exact research costs and UI coordinates are not
  fixed here.
- `ES_IntermediateIrrigation` loses `Plumbing` as a prerequisite.

---

## 9. Interaction with higher DBH technology

Japanization does not need to rewrite all DBH Industrial research.

World Tech Level or the user's broader tech profile remains responsible for
Industrial+ availability.

However DBH for Medieval currently rewires some later DBH nodes:
- `ModernFixtures` after `ES_MedievalFixtures`;
- `ElectricPumps` after `ES_WindPumps` + Electricity;
- `SepticTanks` into “water purification.”

Japanization must ensure hidden medieval pump/filter branches do not become
required blockers for later technology **if the user deliberately allows later
tech**.

Therefore:
- do not delete the upstream research Defs;
- hide/disconnect them from the AMJ historical baseline;
- where necessary, restore a sane later-tech prerequisite path that bypasses
  hidden `ES_ManualPumps/ES_WindPumps`;
- do not claim Industrial DBH behavior as AMJ historical content.

---

## 10. Test gate

When production compatibility exists, automated profiles must include at least:

`MO + Japanization + DBH + DBH for Medieval`

Static checks:
- no retained DBH-for-Medieval ThingDef requires hidden `DankPyon_Windmill`;
- `ES_ManualPump`, `WindPump`, `ES_SimpleToilet`, `ES_FilterDevice`
  are not exposed in the historical baseline;
- `ES_MedievalFixtures` does not unlock/reintroduce sewer-only outputs;
- `ES_IntermediateIrrigation` no longer depends on modern `Plumbing`;
- retained Kettle/WashingKit/Bathtub/Irrigation Defs still resolve;
- MO material substitutions reference valid retained material Defs.

Runtime checks:
- PrimitiveWell supplies/participates in the expected DBH network without the
  hidden pump branches;
- Kettle heats/refills water correctly;
- WashingKit and retained `湯槽` can be used;
- ExcretionPit works;
- retained DBH irrigation canal/gate works independently of Waterworks;
- later DBH tech, when deliberately enabled, is not deadlocked by hidden
  medieval pump nodes;
- ERROR 0.

This compatibility is not implementation-complete until those runtime checks
pass.
