# Medieval Overhaul Japanization Clothing / Textile Mapping

**Status:** Project-owned pre-split audit for `AMJ - Medieval Overhaul Japanization`.

This document covers only MO-owned textile resources, ordinary clothing and
generated-settlement apparel that must be curated so retained MO factions/sites
do not leak a Western domestic clothing baseline.

It is **not** a general AMJ clothing-pack design. New Japanese garments with a
distinct gameplay role remain a future owning-Mod/existing-Mod question.

Audited upstream:
- Medieval Overhaul 1.6.2.2
- author-provided archive `3219596926.zip`
- archive SHA-256:
  `6ed379d7c400db43b3af2a9a7fd6203f7f7e99ca1a670d36b0f73fd1adccc9e3`

## 1. Historical baseline for ordinary clothing

The National Museum of Japanese History reconstruction based mainly on the
`大山寺縁起絵巻` gives a strong medieval-commoner anchor:

- male farmer: short-sleeved, unlined `直垂` + four-panel `袴`;
- female farmer: short-sleeved, unlined `小袖`;
- the garments are **hemp/asa cloth**.

Kyoto National Museum also identifies `小袖` as a source of later kimono and
notes its origin as commoner clothing / undergarment before its later
development as outerwear.

Sources:
- 国立歴史民俗博物館, 中世農民女子衣装 復元:
  https://khirin.rekihaku.ac.jp/en/pid/nmjh_collection/H-1515.html
- 国立歴史民俗博物館, 中世農民男子衣装 / 直垂 / 袴 collection records:
  https://khirin.rekihaku.ac.jp/en/db/nmjh_collection/list/503.html
- 京都国立博物館, キモノと流行―小袖の美―:
  https://www.kyohaku.go.jp/old/jp/theme/floor1_4/f1_4_koremade/1F-4_20220209.html

The gameplay abstraction does **not** need to force historically different
male/female outfits into separate PawnKind rules. A simple top + legwear set can
stand for ordinary work clothing while descriptions acknowledge the abstraction.

---

## 2. MO fibre loop: Flax/Linen -> 苧麻/麻布

MO already owns a complete fibre chain:

- `DankPyon_Plant_Flax`
- `DankPyon_RawFlax`
- `DankPyon_MakeLinen` / bulk
- `DankPyon_SpinFlax`
- `DankPyon_Linen`

This is more valuable as a reused Japanese fibre loop than as a Western flax
branch.

Japanese historical material strongly supports hemp/ramie fibre as a major
premodern textile base:

- Rekihaku summarizes ancient-to-medieval Japan before cotton as a
  hemp/plant-fibre textile culture and explicitly includes `大麻`,
  `芋麻`, and `カラムシ`;
- the national cultural-property database states that hemp fibres including
  ramie were widely used as common people's clothing materials before cotton,
  and records Echigo ramie cloth in `吾妻鏡`;
- NDL bibliographic research treats `古代・中世における苧麻と布` as a
  continuous historical subject.

Sources:
- 国立歴史民俗博物館「木綿以降―江戸時代の繊維革命―」:
  https://archive.rekihaku.ac.jp/exhibitions/plant/column/2019/393.pdf
- 国指定文化財等データベース「越後縮の紡織用具及び関連資料」:
  https://kunishitei.bunka.go.jp/heritage/detail/301/67
- 国立国会図書館『苧麻・絹・木綿の社会史』:
  https://ndlsearch.ndl.go.jp/books/R100000002-I000007562569

### Decision

| MO Def | Japanization | Action |
|---|---|---|
| `DankPyon_Plant_Flax` | **苧麻 / カラムシ** | retain Def, relabel/retexture/description; move from generic MO intermediate-agriculture placement to an early textile-fibre branch |
| `DankPyon_RawFlax` | **青苧 / 苧麻繊維** | retain Def identity; rewrite presentation |
| `DankPyon_Linen` | **麻布** | retain Def identity/stuff role; rewrite presentation |
| `DankPyon_MakeLinen` / bulk | **苧績み・麻布加工** | preserve recipe identity where practical; rewrite job/labels and research placement |
| `DankPyon_SpinFlax` | **ramie/hemp fibre processing** | retain process identity for compatibility; rename/reconnect to the Japanized fibre loop |

Do not add a separate AMJ `HempCloth` Def merely to obtain a Japanese name.

The MO `DankPyon_SpinningWheel` remains subject to the earlier textile audit:
the Western wheel form is not accepted merely because the recipe is useful.
Japanization should retexture/reinterpret the work station toward a historically
valid hand fibre-processing/spinning setup, or route the retained recipe through
a compatible manual bench.

Industrial `DankPyon_ClothSpinner` remains outside the historical profile.

### MO cloth-chain setting compatibility

MO's own `clothChain` toggle changes this exact loop.

When the cloth chain is active:
- flax/ramie plant -> raw fibre -> spinning recipe -> linen/cloth.

When it is inactive, MO currently:
- changes `DankPyon_Plant_Flax` to harvest `DankPyon_Linen` directly;
- removes the recipe users from the normal/bulk linen recipes;
- disables the industrial cloth spinner path.

**Decision: Japanization does not force the user's MO cloth-chain setting.**

Both modes remain supported:
- clothChain ON -> `苧麻 -> 青苧/原麻 -> 麻布`;
- clothChain OFF -> simplified `苧麻 -> 麻布`.

Labels/descriptions/material semantics must therefore remain valid even when the
intermediate `DankPyon_RawFlax` step is bypassed.

Source-level impact audit:
- `DankPyon_RawFlax`: 20 exact source occurrences across 6 baseline files,
  concentrated in fibre recipes/processes and storage/bale definitions;
- `DankPyon_Linen`: 75 exact source occurrences across 17 baseline files,
  including sacks/storage, tents, furniture/joy props, ruins/loot, armor
  backing/costs, faction/trader stock and fibre processing.

This broad reuse is acceptable for `麻布`: sacks, tents, cloth furnishings and
armor backing all remain semantically plausible. It also means Japanization
must change the resource consistently rather than only relabeling apparel.

### Scope caveat

This does not yet decide MO cotton's normal historical placement. Cotton is a
separate late-period audit. The ramie/hemp loop is sufficient to support the
baseline commoner-clothing set without making cotton a prerequisite.

---

## 3. Ordinary upper garment

### `DankPyon_Apparel_Sackcloth` -> simple `麻衣`

Loaded MO role:
- OnSkin;
- neck / torso / shoulders;
- 40 stuff;
- WorkToMake 1,600;
- mass .25;
- low armor;
- craftable at CraftingSpot;
- already carries the `DankPyon_Peasant` tag.

**Decision: REINTERPRET + LIGHT MECHANICAL PATCH.**

Use this as the generic simple common-work upper-garment carrier.

Japanization:
- public label should be a generic **麻衣** / simple hemp garment rather than
  “sackcloth”;
- visual may draw from simple medieval `小袖 / 単衣 / 直垂` workwear but
  should not claim that one RimWorld Def exactly represents every garment;
- restrict normal material semantics to Fabric rather than leather scraps;
- generated MO peasants/guards should use `DankPyon_Linen` after that Def is
  Japanized to `麻布`.

This is mechanically far closer to ordinary farm clothing than MO's padded
surcoat.

---

## 4. Legwear

### `DankPyon_Apparel_Trousers` -> `袴`

The Def inherits MO's ordinary OnSkin pants base:
- Legs;
- 50 stuff;
- WorkToMake 2,000;
- mass 1;
- Fabric or Leathery in the upstream base.

**Decision: REINTERPRET + RETEXTURE as ordinary `袴`.**

Japanization should:
- use Fabric material semantics;
- generate it from Japanized `麻布` for ordinary settlement roles;
- remove the Western “burgher/nobility trousers” description.

The medieval farmer reconstruction gives a direct `袴` reference.

### Vanilla `Apparel_Pants` in SettlementPeasant

MO's abstract SettlementPeasant currently hard-requires Vanilla
`Apparel_Pants`.

**Decision: replace that hard requirement with the retained MO
`DankPyon_Apparel_Trousers` / `袴` carrier.**

This keeps the entire generated commoner clothing set inside the known
Japanized MO carrier pool.

---

## 5. Padded/leather Western common clothing

### `DankPyon_Apparel_Padded_Surcoat`

Loaded:
- 70 Fabric;
- WorkToMake 10,000;
- mass 4;
- armor multiplier .30;
- cold multiplier .5;
- explicitly a gambeson-like padded surcoat.

**Decision: HIDE from the baseline ordinary-clothing path.**

It is not needed once:
- common clothing uses `麻衣`;
- actual armor uses the curated Japanese armor branch.

Remove it from SettlementPeasant/Guard hard requirements and generated
specific-apparel requirements.

Do not invent a Japanese padded garment solely to preserve this Def.

### `DankPyon_Apparel_Leather_Tunic`

Loaded:
- Middle layer;
- Leathery only;
- WorkToMake 5,000;
- armor multiplier .30.

**Decision: HIDE from baseline ordinary settlement clothing.**

A generic leather vest is not required for the Japanese commoner/guard loop,
and keeping it between civilian clothing and the proper armor carriers only
recreates the Western layering bundle.

### `DankPyon_Apparel_ChaussesPadded`

Loaded:
- Middle leg armor;
- 70 Fabric/Leathery;
- WorkToMake 8,000;
- mass 4;
- armor multiplier .30.

**Decision: HIDE from baseline.**

The Japanese armor mapping already has a meaningful leg-armor carrier in the
later `佩楯` slot. Do not preserve padded chausses as mandatory guard wear.

---

## 6. Footwear

### `DankPyon_Footwear_BootsLeather` -> `草鞋` only with mechanical patch

Upstream:
- Leathery only;
- Feet / Middle;
- 25 stuff;
- armor multiplier .18;
- cold multiplier .40;
- MoveSpeed +.05;
- hard-required by multiple MO PawnKinds.

Japanese historical fit:
- reference works record `草鞋` in Heian/Kamakura sources;
- by Kamakura/Muromachi, practical straw sandals/waraji were widely used by
  warriors and common people;
- they are plant/straw footwear, not leather boots.

Sources:
- コトバンク「履き物」:
  https://kotobank.jp/word/%E5%B1%A5%E3%81%8D%E7%89%A9-1576815
- コトバンク「草鞋」:
  https://kotobank.jp/word/%E8%8D%89%E9%9E%8B-551772
- コトバンク「草履」:
  https://kotobank.jp/word/%E8%8D%89%E5%B1%A5-89748

**Decision: PATCH_MECHANICS + REINTERPRET as `草鞋`.**

Required before implementation:
- remove Leathery-only construction;
- use a straw/plant-fibre cost, preferably existing MO `DankPyon_Straw` or a
  suitable fibre input;
- reduce/remove inherited leather-like armor/insulation;
- re-evaluate rather than automatically keep the full +5% MoveSpeed bonus.

The Def does **not** remain a hard requirement on every peasant/guard. It is
available useful footwear, not a universal uniform.

Exact cost/stat values remain a balance decision.

---

## 7. Handwear

### `DankPyon_Handwear_GlovesLeather`

Upstream:
- Leathery only;
- Hands / Middle;
- +5% WorkSpeedGlobal;
- +2 ShootingAccuracyPawn;
- armor/insulation bonuses;
- hard-required in MO commoner/guard templates.

**Decision: HIDE from baseline and remove all ordinary settlement hard
requirements.**

There is no need to invent generic Japanese “work gloves” that also grant a
large shooting bonus merely to preserve this upstream Def.

A later historically specific `手甲` cannot be obtained honestly by merely
renaming a Hands-only glove, just as plate gloves could not become `籠手`.

---

## 8. Arrow container

### `DankPyon_Apparel_Quiver` -> `箙`

Upstream:
- shoulder / Belt utility apparel;
- 50 Leathery stuff;
- mass 1;
- `VEF_RangedCooldownFactor .25`;
- reduces shooting cycle time for bows/crossbows;
- hard-required by MO settlement archers.

Japanese fit is strong:
- `箙` was a battlefield/hunting arrow container;
- Japanese encyclopedic references place its widespread use from the
  mid-Heian period and distinguish it as a warrior's arrow carrier after the
  Kamakura period.

Source:
- コトバンク「箙」:
  https://kotobank.jp/word/%E7%AE%99-37223

**Decision: REINTERPRET + RETEXTURE as `箙`.**

Keep the functional quiver bonus as an MO mechanic for now, but:
- move its research/unlock from generic ComplexClothing to the Japanese
  military-archery branch;
- retexture its complete worn graphic;
- audit the 50-leather material requirement: historical 箙 could use
  wood/bamboo/rattan/leather, so leather-only construction is not necessarily
  the best Japanized recipe;
- retained noble-house settlement archers can continue to hard-require the same
  Def after it becomes `箙`.

Earlier `靫` forms may be useful terminology for ancient profiles, but one
upstream utility Def does not justify duplicate arrow-container items solely
for chronology.

---

## 9. Settlement PawnKind clothing rewrite

### Current upstream problem

`DankPyon_SettlementPeasant` currently hard-requires:
- padded surcoat;
- leather boots;
- leather gloves;
- Vanilla pants;
and even forces wool/leather materials.

`DankPyon_SettlementGuard` hard-requires:
- padded surcoat;
- leather tunic;
- trousers;
- padded chausses;
- leather gloves;
- leather boots.

All archer/footman/knight/lord templates inherit that over-equipped Guard base.

This means even before weapons/armor are considered, the generated MO settlement
already assumes a layered Western clothing kit.

### Japanized base

#### SettlementPeasant

Hard requirement becomes only:
- `DankPyon_Apparel_Sackcloth` -> simple `麻衣`;
- `DankPyon_Apparel_Trousers` -> `袴`.

Specific generated material:
- `DankPyon_Linen` after that Def becomes `麻布`.

No mandatory:
- padded surcoat;
- leather gloves;
- leather boots.

#### SettlementGuard

Use the same lightweight civilian clothing base:
- `麻衣`;
- `袴`.

Do **not** preload all guards with:
- leather tunic;
- padded chausses;
- gloves;
- boots.

Concrete combat PawnKinds add the armor actually appropriate to their role:
- archer -> retained helmet + `箙`;
- footman -> retained helmet and weapon set;
- knight -> `当世具足` carrier;
- lord -> high-status retained armor/helmet.

This also reduces apparel-layer conflicts created by the Japanized armor branch.

### Abstraction caveat

The reconstruction source shows real differences between male and female
medieval farm clothing. RimWorld PawnKind generation does not need to reproduce
those differences through rigid sex-locked uniforms in v1.

The goal is to stop forcing every Japanese farmer into a Western gambeson,
leather boots and shooting gloves. More detailed gender/status/occupation
clothing remains an optional future clothing-content problem.

---

## 10. Responsibility boundary

Japanization owns:
- MO Flax/Linen -> Japanese fibre-loop reinterpretation;
- MO-owned common clothing labels/descriptions/textures where retained;
- MO settlement PawnKind loadout changes needed to stop Western clothing leaks;
- research/material patches required for those retained MO Defs.

Japanization does **not** own:
- a comprehensive historical Japanese clothing pack;
- every period/status/sex-specific garment;
- non-MO external apparel filtering;
- new clothing systems solely for visual variety.

Existing/future Japanese apparel Mods remain valid complementary content.

## Next gate

Before production XML:
1. add these clothing/textile dispositions to the decision ledger;
2. update the loadout ledger for SettlementPeasant/Guard inheritance;
3. static-check that hidden padded/leather commonwear is no longer hard-required
   by retained PawnKinds;
4. confirm the Flax/Linen reinterpretation does not conflict with MO recipes,
   traders, ruins/storage, or optional integrations;
5. then continue to final static comparison tooling and runtime profiles.
