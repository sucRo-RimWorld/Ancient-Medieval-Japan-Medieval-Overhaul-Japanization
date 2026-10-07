# Medieval Overhaul Japanization Common Clothing Mapping

**Status:** Project-owned pre-split design audit for `AMJ - Medieval Overhaul Japanization`.

This document closes the ordinary/commoner clothing gap in the MO 1.6.2.2
Japanization audit. It reuses existing MO apparel Defs where their loaded
coverage/layer/gameplay role can honestly carry a Japanese referent.

It does **not** create a standalone AMJ Clothing module. The existing project
boundary remains: purpose-built new Japanese clothing Defs belong to the
separate Clothing candidate or supported external Japanese apparel Mods if
that later proves necessary.

Audited source:
- author-provided `3219596926.zip`
- Medieval Overhaul `1.6.2.2`
- SHA-256 `6ed379d7c400db43b3af2a9a7fd6203f7f7e99ca1a670d36b0f73fd1adccc9e3`

## 1. Historical baseline

National Museum of Japanese History reconstruction based mainly on the
`大山寺縁起絵巻` gives a useful ordinary-life reference for the Muromachi
period:

- male farmer: folded eboshi, short-sleeved unlined `直垂`, four-panel
  `袴`;
- female farmer: sedge hat and short-sleeved unlined `小袖`;
- the reconstructed garments are hemp-based.

The museum's clothing-history material also records that the `小袖` became a
central outer garment through the medieval period rather than being an
Edo-only form.

References:
- 国立歴史民俗博物館, 中世農民男子衣装 復元 / H-1514
  https://khirin.rekihaku.ac.jp/en/db/nmjh_collection/list/503.html
- 国立歴史民俗博物館, 中世農民女子衣装 復元 / H-1515
  https://khirin.rekihaku.ac.jp/en/pid/nmjh_collection/H-1515.html
- 国立歴史民俗博物館, 江戸モード大図鑑 — 小袖の中世成立説明
  https://archive.rekihaku.ac.jp/exhibitions/project/old/991005/index.html

This does not mean every pawn must be dressed in the same reconstructed
outfit. It gives the baseline that a Japanese commoner set should be built
from plant-fiber garments rather than mandatory Western padded surcoats,
leather vests, leather boots and leather gloves.

---

## 2. Current MO settlement problem

`DankPyon_SettlementPeasant` currently hard-requires:

- `DankPyon_Apparel_Padded_Surcoat`;
- `DankPyon_Footwear_BootsLeather`;
- `DankPyon_Handwear_GlovesLeather`;
- Vanilla `Apparel_Pants`.

Its specific requirements also force:
- `WoolMegasloth` for the padded surcoat/pants;
- `Leather_Plain` for gloves/boots.

`DankPyon_SettlementGuard` is even more heavily Westernized. It hard-requires:

- padded surcoat;
- leather tunic;
- MO trousers;
- padded chausses;
- leather gloves;
- leather boots;

and its specific requirements force fantasy/foreign material choices such as
`DankPyon_Leather_Troll`.

**Decision:** the Japanized settlement base must not preserve these hard
requirements. The loadout should be rebuilt around a light textile base, with
armor/archery accessories added only by the role that actually needs them.

---

## 3. Common torso carrier

### `DankPyon_Apparel_Sackcloth` -> `小袖`

Loaded role:
- OnSkin;
- Neck / Torso / Shoulders;
- 40 stuff;
- Fabric or Leathery;
- WorkToMake 1,600;
- mass 0.25;
- no research prerequisite;
- Peasant / BrigandThug / MedievalBasic tags.

**Decision: REINTERPRET + RETEXTURE as the basic `小袖` carrier.**

Why this Def:
- its light OnSkin role is much closer to ordinary clothing than
  `Padded_Surcoat`;
- its low labor/mass fits a common basic garment;
- the player does not need an advanced research node just to produce it.

Required patches:
- remove `Leathery` from accepted stuff; use textile/fabric only;
- rewrite label/description;
- replace ragged sackcloth graphic with a simple short-sleeved medieval
  Japanese garment;
- keep the public garment generic enough for both ordinary work clothing and
  under-layer use;
- do not force one specific fiber Def at the Japanization layer. Hemp/ramie
  integration can be added conditionally by an owning material/agriculture
  Mod, while MO/Vanilla Fabric remains the fallback.

The single unisex Def is a RimWorld abstraction. Japanization should not create
separate male/female ThingDefs only to reproduce every historical cut.

### `DankPyon_Apparel_Padded_Surcoat`

Loaded role:
- OnSkin;
- Neck / Shoulders / Torso;
- mass 4;
- WorkToMake 10,000;
- armor multiplier .30;
- cold-insulation multiplier .50;
- currently `ComplexClothing`-gated.

**Decision: CONDITIONAL, not normal commoner clothing.**

Remove it from settlement Peasant/Guard hard requirements.

It may later be retained as a padded cold-weather/protective garment if a
separate exact historical mapping is justified, but Japanization must not call
a four-kilogram padded Western surcoat the default Japanese commoner's shirt.

### `DankPyon_Apparel_Leather_Tunic`

Loaded role:
- Middle layer;
- Neck / Torso / Shoulders;
- leathery only;
- armor multiplier .30;
- WorkToMake 5,000.

**Decision: HIDE from the baseline commoner/settlement apparel pool.**

Japanese armor roles are already carried by the dedicated lamellar / dōmaru /
chain / late-armor Defs. A leather vest does not need an invented commoner
mapping merely to preserve MO's Western layering.

---

## 4. Lower-body carrier

### `DankPyon_Apparel_Trousers` -> `袴`

This Def inherits MO's normal pants base:

- OnSkin;
- Legs;
- 50 stuff;
- Fabric or Leathery through the inherited base;
- mass 1;
- WorkToMake 2,000;
- current inherited `ComplexClothing` prerequisite.

**Decision: REINTERPRET + RETEXTURE as the basic `袴` carrier.**

Required patches:
- remove leathery stuff from the ordinary garment;
- move it out of the upstream `ComplexClothing` dependency and into the
  early/basic Japanized tailoring path;
- Japanese loose-trouser graphic;
- use ordinary textile material.

This is a gameplay abstraction. The historical source shows a four-panel
`袴` on a male farmer, while female work dress could use a long `小袖`
without the same visible lower garment. RimWorld's unisex apparel/nudity
system does not justify adding separate gendered clothing Defs solely for that
difference.

### `DankPyon_Apparel_Hose`

This is mechanically the same family/base as MO trousers and exists mainly as
another Western legwear presentation.

**Decision: HIDE from the baseline.**

Do not invent a second Japanese lower garment merely to preserve the upstream
variation.

### `DankPyon_Apparel_ChaussesPadded`

Loaded role:
- Middle layer;
- Legs;
- mass 4;
- armor multiplier .30;
- WorkToMake 8,000;
- Protective Clothing prerequisite.

**Decision: HIDE from the ordinary/commoner profile.**

Do not relabel padded chausses as `脚絆`. Their full-leg padded armor behavior
does not match ordinary Japanese gaiters closely enough.

---

## 5. Footwear

### `DankPyon_Footwear_BootsLeather` -> `草鞋`

Loaded role:
- Feet / Middle layer;
- 25 Leathery stuff;
- mass .25;
- WorkToMake 1,000;
- armor multiplier .18;
- cold insulation .40;
- **MoveSpeed +0.05**;
- Protective Clothing prerequisite.

The movement bonus gives this Def a useful gameplay role for a light walking
shoe, but the leather construction and armor research are wrong.

**Decision: PATCH MATERIALS + REINTERPRET as `草鞋`.**

Required patches:
- remove Leathery construction;
- use a plant-fiber/straw-like recipe with no hard dependency on another AMJ
  Mod;
- move to early/basic craft rather than Protective Clothing;
- reduce/remove armor and leather-derived insulation behavior if it remains
  materially significant after the recipe change;
- keep a modest movement benefit if balance testing confirms it remains useful.

Do **not** hard-require footwear on every settlement peasant. Historical
Japanese ordinary life included barefoot use, while grass footwear was common
for travel/work and later broadly used.

Historical anchors:
- `草鞋` appears in Heian/Kamakura sources and was used for travel/agricultural
  work;
- Kamakura/Muromachi warriors also used `足半`, a short grass sandal with
  strong footing.
  - https://kotobank.jp/word/%E8%8D%89%E9%9E%8B-551772
  - https://kotobank.jp/word/%E8%B6%B3%E5%8D%8A-25299

The single Def should remain the general `草鞋` role; do not add a second
`足半` Def unless later gameplay needs a distinct military-footing item.

---

## 6. Handwear becomes archery equipment

### `DankPyon_Handwear_GlovesLeather` -> `弽`

Loaded role:
- Hands / Middle;
- 25 Leathery stuff;
- WorkToMake 1,000;
- armor multiplier .18;
- cold insulation .40;
- **WorkSpeedGlobal +5%**;
- **ShootingAccuracyPawn +2**;
- Protective Clothing prerequisite.

This is not appropriate as mandatory peasant/guard clothing, but its leather
hand-protection + shooting bonus maps well to Japanese archery handwear.

**Decision: PATCH MECHANICS + REINTERPRET as `弽（ゆがけ）`.**

Required patches:
- remove it from general Peasant/Guard/Mercenary apparel requirements/tags;
- make it an archery accessory rather than generic work gloves;
- remove `WorkSpeedGlobal +5%`;
- retain/rebalance the shooting benefit after archery balance testing;
- move the crafting prerequisite to the Japanized archery/clothing branch;
- retexture as leather archery hand protection.

Historical anchor:
- `弽` is a leather glove-like archery implement used to protect the shooting
  hand; medieval sources include `弓懸` and paired riding-archery forms.
  - https://kotobank.jp/word/%E5%BC%BD-1431339
  - https://kotobank.jp/word/%E5%BC%93%E6%87%B8%E3%81%91-2090241

The current Def covers both Hands as a RimWorld abstraction; do not create
another Def only to model exact finger coverage.

---

## 7. Quiver

### `DankPyon_Apparel_Quiver` -> `箙`

Loaded role:
- Shoulders / Belt;
- 50 Leathery stuff;
- mass 1;
- WorkToMake 4,500;
- current `ComplexClothing` prerequisite;
- `VEF_RangedCooldownFactor = 0.25`.

**Decision: REINTERPRET + RETEXTURE as `箙`, with a mechanical gate.**

The container role is a strong historical match. `箙` was a portable arrow
carrier used by warriors; reference works place it firmly in medieval military
archery.

Historical anchor:
- https://kotobank.jp/word/%E7%AE%99-37223

However the current cooldown stat is generic ranged-weapon equipment logic. A
quiver/ebira must not improve matchlock or unrelated ranged weapons.

Implementation gate:
1. confirm whether the current MO/VEF cooldown modifier applies to every ranged
   Verb;
2. if it can be restricted by weapon tag/family, apply the bonus only to bows;
3. if not, remove the generic cooldown bonus rather than letting `箙` improve
   firearms/crossbows indiscriminately.

Move the item out of generic `ComplexClothing` and into the archery equipment
branch.

---

## 8. Settlement PawnKind base rewrite

### `DankPyon_SettlementPeasant`

Remove hard requirements:
- `DankPyon_Apparel_Padded_Surcoat`;
- `DankPyon_Footwear_BootsLeather`;
- `DankPyon_Handwear_GlovesLeather`;
- Vanilla `Apparel_Pants`.

New baseline:
- `DankPyon_Apparel_Sackcloth` -> `小袖`;
- `DankPyon_Apparel_Trousers` -> `袴`.

Footwear is optional rather than mandatory.

Remove the hard-coded `WoolMegasloth` / leather material requirements.
Ordinary textile selection should not force fantasy/Western material identity.

### `DankPyon_SettlementGuard`

Remove hard requirements:
- padded surcoat;
- leather tunic;
- padded chausses;
- leather gloves;
- leather boots.

Use the same basic textile base:
- `小袖`;
- `袴`.

Combat subclasses then add only the equipment they need:
- Archer: `弽` + `箙` + retained bow/helmet/faction armor;
- Footman: spear/naginata carrier + retained helmet/armor;
- Knight/elite: retained Japanese heavy armor;
- Lord: retained high-status Japaneseized armor/weapon set.

Remove `WoolMegasloth` / `DankPyon_Leather_Troll` from settlement-specific
material forcing.

This reduces both visual Westernization and needless apparel-layer clutter.

---

## 9. Boundary with standalone AMJ Clothing

This pass is **not** evidence that AMJ needs its own Clothing Mod.

Japanization is allowed to:
- relabel/retexture MO-owned apparel Defs;
- patch their material/research/stat behavior when required for a truthful
  Japanese mapping;
- patch MO PawnKinds so generated MO factions no longer force Western clothes.

Japanization should not:
- add a full catalogue of Japanese daily garments;
- duplicate UNAGI / T's Samurai Faction / Tasty Armory apparel merely for
  variety;
- create gender/class/regional clothing systems unrelated to an MO-owned Def.

If later gameplay needs genuinely new Japanese apparel with no suitable MO or
external carrier, that request returns to the Project-level Clothing candidate.

---

## 10. Implementation/test gate

Before production XML:

1. decision ledger contains every retained/hidden clothing Def above;
2. loadout ledger removes the old Peasant/Guard hard requirements;
3. all four noble-house settlement families generate successfully from the new
   base clothing;
4. no settlement PawnKind forces `WoolMegasloth`,
   `DankPyon_Leather_Troll`, leather boots or generic leather gloves as
   ordinary Japanese clothing;
5. `弽` shooting bonus and `箙` cooldown effect are validated against bows
   and firearms;
6. player recipes for `小袖 / 袴 / 草鞋` have sensible early research and
   materials;
7. Pickle/RimTest generates representative Peasant/Archer/Footman/Knight/Lord
   pawns with ERROR 0 and no hidden Western apparel.

After this pass, the main remaining Japanization blockers are the final
matchlock balance/stat line and the static decision/loadout/source-ledger
comparison test.
