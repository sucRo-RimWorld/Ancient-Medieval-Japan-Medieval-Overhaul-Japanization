> **Project ownership note (2026-10-07):** migrated from Ancient-Medieval-Japan-Grains because AMJ - Medieval Overhaul Japanization has no dedicated repository yet. This Project copy is the current pre-split research source.

# Medieval Overhaul Japanization Military Mapping Audit

## Status and scope

This document is the Def-level follow-up to
`Docs/Research/MedievalOverhaulJapanizationResearchAudit.md`.

It audits the actual Medieval Overhaul 1.6.2.2 military/equipment Defs gated by
research nodes that `AMJ - Medieval Overhaul Japanization` intends to
restructure. It is a **design audit**, not an implementation claim.

Audited archive:

- Workshop archive: `3219596926.zip`
- MO payload: 1.6.2.2
- SHA-256: `6ed379d7c400db43b3af2a9a7fd6203f7f7e99ca1a670d36b0f73fd1adccc9e3`

The counts below include Defs whose `recipeMaker/researchPrerequisite` or
`researchPrerequisites` requires the node, including multi-prerequisite
adorned items. Upstream DefNames should be preserved wherever practical.

## Mapping rule

Japanization should not invent a Japanese name merely to keep every Western MO
weapon visible.

For each MO Def:

1. **Retexture + relabel** only if the gameplay role, material meaning and
   broad historical period map cleanly to a Japanese counterpart.
2. **Keep function, change research branch** if the object is valid but MO puts
   it in a Western/fantasy progression.
3. **Hide from normal production** if no honest Japanese counterpart is needed.
   Prefer hiding/disconnecting over deleting the upstream Def, to reduce
   compatibility breakage.
4. **Do not collapse distinct gameplay stats** merely for historical tidiness.
   If two MO Defs provide genuinely different gameplay roles and both have
   defensible Japanese referents, both may remain.
5. **Do not preserve redundant Western variation** solely because the upstream
   art has many variants. Heraldic/faction/color variants can be consolidated
   or hidden when they do not add Japanese gameplay value.

---

## 1. Crossbow and fixed-bow branch

### Actual MO coupling

`DankPyon_Crossbow` gates:

- `DankPyon_Crossbow` — handheld crossbow
- `DankPyon_Turret_Scorpio` — fixed scorpio
- scorpio bolt recipes

`DankPyon_HeavyCrossbow` gates:

- `DankPyon_CrossbowHeavy` — arbalest
- `DankPyon_Turret_Ballista` — fixed ballista
- ballista bolt recipes

`DankPyon_Ballista` additionally gates both fixed weapons and both ammunition
families.

`DankPyon_Trebuchet` gates:

- `DankPyon_Turret_Trebuchet`
- stone-boulder ammunition recipes

`DankPyon_RepeaterBallista` gates:

- `DankPyon_Turret_RepeaterBallista`

### Japanization direction

| MO Def / group | First-pass treatment | Rationale |
|---|---|---|
| `DankPyon_Crossbow` | **Retexture + relabel candidate: 弩** | Eighth-century Japanese military crossbow mechanisms are directly attested. Move to ancient state-military technology rather than a late Western crossbow branch. |
| `DankPyon_CrossbowHeavy` | **Further audit** | A stronger handheld crossbow may be defensible, but “arbalest” should not be translated mechanically. Preserve only if stats support a meaningful strong-bow/strong-crossbow distinction. |
| `DankPyon_Turret_Scorpio` | **Retexture + relabel candidate: fixed 弩 / 弩台** | Japanese scholarship distinguishes portable and installed crossbow use. Exact MO footprint, crew model, rate of fire and ammunition must fit before final naming. |
| `DankPyon_Turret_Ballista` | **Retexture candidate, pending stat/size audit** | Could represent a heavier installed 弩 if it remains an ancient defensive emplacement rather than a Roman/European siege engine in behavior. |
| `DankPyon_Turret_Trebuchet` | **Hide by default** | Yuan/Mongol forces brought stone-throwing weapons to Japan, but that does not justify a normal domestic Japanese technology branch. |
| `DankPyon_Turret_RepeaterBallista` | **Hide by default** | No sufficiently strong AMJ-period Japanese standard-tech justification has been established. |

### Structural correction

MO currently couples handheld crossbows and fixed siege weapons. Japanization
should split the unlock logic into at least:

- **portable 弩 technology**;
- **installed 弩 technology** (if final equipment audit passes);
- **foreign/unsupported siege equipment hidden from normal research**.

Do not retain the upstream linear
`Crossbow -> Heavy Crossbow -> Ballista -> Trebuchet/Repeater` progression.

---

## 2. Light protection, shields and chain branch

### `DankPyon_ProtectiveClothing`: 17 MO Defs

The node currently gates a mixed family:

- padded chausses;
- light lamellar;
- padded armor;
- leather boots/gloves;
- padded flat-top / kettle / nasal helmets;
- Zweihander hat;
- round shield;
- four heraldic heater-shield variants;
- kite shield;
- Lindwurm shield;
- living-tree shield.

### Direction

The **research concept** can remain as an early defensive-equipment branch, but
the content cannot be retained wholesale.

- `DankPyon_Apparel_Light_Lamellar` is the strongest direct reuse candidate:
  lamellar construction maps much more naturally to Japanese armor than the
  Western padded/plate ladder.
- Generic padded protection may remain where its gameplay role is culture-neutral.
- Western helmet silhouettes (nasal, kettle, flat-top) require Japanese
  retexture/relabel or hiding.
- Heater/kite/heraldic shield variants should not survive merely as renamed
  Japanese shields. Japanization should keep only shield roles that have a
  defensible Japanese counterpart and gameplay purpose.
- Lindwurm/living-tree fantasy shields should be hidden from the historical
  Japanization path.
- The “Zweihander” identity is explicitly Western and must not survive unchanged.

### `DankPyon_ChainArmor`: 23 gated MO Defs

This node gates:

- hauberk / heavy hauberk;
- splinted chausses, boots and gloves;
- chain coif / full chain coif;
- chain nasal, kettle and flat-top helmet families;
- heavy barbrute, open bascinet, Zweihander helmet;
- four Zweihander heraldic variants;
- four adorned mail/chain items that also require `DankPyon_AdornedArmor`.

### Direction

Do **not** treat this as a ready-made Japanese “chain armor tier.”

Japanese chain protection can justify retaining a **limited chain-equipment
branch**, but the MO set is overwhelmingly Western in garment and helmet form.
The node should therefore be curated Def-by-Def:

- preserve a small number of distinct chain-protection gameplay roles if a
  Japanese referent and period are supportable;
- retexture/relabel those retained roles;
- hide redundant bascinet/flat-top/nasal/Zweihander variants rather than invent
  fictional Japanese equivalents;
- remove `ChainArmor` as a mandatory prerequisite for the later Japanese
  armor branch.

A medieval Japanese chain mapping remains lower-confidence than the lamellar /
dōmaru / later plate-heavy mapping and needs dedicated historical verification
before final labels are selected.

---

## 3. Plate armor and late armor branch

### Vanilla `PlateArmor` gates 23 MO Defs

The full XML dependency audit finds these MO-gated items:

Body / limb armor:

- `DankPyon_Apparel_Brigandine`
- `DankPyon_Apparel_Breast_Plate`
- `DankPyon_Apparel_Zweihanders_Cuirass`
- `DankPyon_Apparel_Zweihanders_CuirassFloof`
- `DankPyon_Apparel_FullPlateGilded`
- `DankPyon_Apparel_Lindwurm`
- `DankPyon_Apparel_ChaussesPlate`
- `DankPyon_Footwear_BootsPlate`
- `DankPyon_Handwear_GlovesPlate`
- `DankPyon_Apparel_AdornedHeavyPlate` (also `DankPyon_AdornedArmor`)

Helmets:

- armet / gilded armet;
- closed bascinet;
- klappvisor bascinet variants;
- hounskull;
- great helm;
- sallet variants;
- wolf-ribs bascinet;
- Lindwurm scale helmet;
- adorned great helm (also `DankPyon_AdornedArmor`).

### Japanization direction

The **research role** should become a late-medieval Japanese advanced-armor
branch rather than “European plate armor.”

Historical anchors support:

- high-quality `胴丸` in the Muromachi period;
- later plate-heavy `当世具足`;
- late-16th-century adoption and Japanese manufacture of armor influenced by
  European cuirasses (`南蛮胴具足`).

This does **not** mean every MO plate item maps one-to-one to a Japanese suit.
Instead:

- select a small set of body/helmet roles that correspond to meaningful stages
  or equipment tradeoffs;
- map those to Japanese armor families through label/description/retexture;
- hide redundant Western helmet subtypes and faction variants;
- hide Lindwurm fantasy armor;
- avoid using “plate armor” as the Japanese public label if the surviving Def
  family represents Japanese composite armor rather than a European full-plate
  suit.

The final late-armor research may unlock several retained MO Defs while hiding
the rest; it does not need to preserve the upstream count.

---

## 4. Adorned armor

`DankPyon_AdornedArmor` gates six Ulrik/oathbound-flavored items:

- adorned mail shirt;
- adorned warrior armor;
- adorned heavy plate;
- adorned heavy mail coif;
- adorned flat-top chainveil helmet;
- adorned great helm.

Descriptions explicitly refer to trophies/holy symbols and MO's Western
religious/heraldic context.

### Direction

Do not merely translate “adorned” into a Japanese label.

Two possible final outcomes:

1. **reinterpret as high-status decorative armor** if the stat premium and
   crafting cost provide an independent gameplay role, with Japanese decorative
   fittings/lacing/heraldic presentation; or
2. **hide/consolidate** if the distinction is primarily Ulrik/Western flavor.

This node should no longer depend mechanically on an unchanged European
`ChainArmor -> PlateArmor` ladder.

---

## 5. Bow branch

MO-specific direct unlocks:

- `DankPyon_HuntingBow` -> `DankPyon_Bow_Hunting`
- `DankPyon_WarBow` -> `Bow_War`

MO also relocates Vanilla `RecurveBow` as “archery” and uses Vanilla
`Greatbow`.

### Direction

Retain the **gameplay distinction** if the stats support it, but rebuild the
research meaning around Japanese bows rather than Western bow evolution.

Candidate structure:

- early hunting/ordinary bow;
- military archery / `弓術`;
- stronger or specialist war-bow role only where it produces a useful gameplay
  distinction.

Do not infer a strict historical Japanese progression merely from MO damage
tiers. Final Def names/images must be selected after stat comparison.

---

## 6. Polearms

Actual MO outputs:

### Basic

- militia spear;
- warfork;
- pitchfork;
- hooked blade.

### Military

- boar spear;
- spetum;
- billhook;
- pike + four heraldic pike variants;
- swordlance.

### Noble

- halberd.

### Direction

The three MO tiers should not survive as
“basic / military / noble polearms.”

Japanization should instead curate a Japanese long-weapon family:

- spear roles -> `槍` / long-spear roles;
- suitable bladed-polearm roles -> `薙刀` or related long-blade families where
  stats and animation fit;
- suitable long-blade-on-pole role -> `長巻` only if the weapon behavior fits;
- selected fork/hook agricultural tools may remain tools rather than military
  prestige progression;
- heraldic pike variants should be consolidated or hidden unless they provide
  non-cosmetic value;
- halberd/spetum/billhook must not each receive an invented Japanese equivalent
  merely to preserve every Def.

Historical evidence supports naginata use before and through the medieval
period and spear prominence in late medieval warfare, but final one-to-one
mapping must follow the MO weapon stats.

---

## 7. Maces, hammers and picks

MO outputs:

### Basic

- bludgeon;
- goedendag;
- two-handed mace;
- two-handed mallet.

### Military

- blacksmith hammer;
- pickaxe;
- military pick;
- two-handed hammer;
- polehammer;
- nomad mace;
- morning star;
- winged mace.

### Noble

- warhammer;
- two-handed flanged mace.

### Direction

This is a **curation branch**, not a translation branch.

- Keep culture-neutral work tools where their dual combat role still makes sense.
- Retain only a small number of dedicated blunt-weapon performance niches when
  a Japanese counterpart is historically defensible.
- Do not invent Japanese “morning star,” “winged mace,” “goedendag,” etc.
- If several Western Defs collapse onto the same Japanese gameplay concept,
  choose the best stat/material slot and hide the redundant ones.
- Rename/remove the “noble” tier.

Exact kanabō/tetsubō mappings are intentionally **not fixed yet**; stronger
historical sourcing and stat/graphic comparison are required first.

---

## 8. Blades and axes

### `DankPyon_BasicBlades`

- butcher's cleaver;
- hatchet;
- woodcutter's axe;
- falchion.

### `DankPyon_MilitaryBlades`

- handaxe;
- bardiche;
- longaxe;
- longsword.

### Vanilla `LongBlades` additionally gates MO

- fencing sword;
- fighting axe;
- greataxe;
- greatsword.

### Direction

Split **tools/axes** from **swordcraft** conceptually.

Tool-side candidates:

- cleaver / hatchet / wood axe -> Japanese utility chopping/cleaving roles such
  as `鉈` / `手斧` / `斧` where stats fit;
- keep only enough axe variants to preserve meaningful tool/combat tradeoffs.

Sword-side candidates:

- use the strongest fitting MO stat slots to represent Japanese blade families
  such as `太刀`, later `打刀`, and oversized battlefield sword roles;
- do not map falchion/longsword/fencing sword/greatsword one-for-one by shape;
- Heian/Kamakura tachi and late-medieval uchigatana/large-sword forms give
  historical anchors, but exact Def allocation requires damage, cooldown,
  material and work-cost comparison.

The current European
`BasicBlades -> MilitaryBlades -> LongBlades`
ladder should be replaced by a Japanese craft/use progression, not translated.

---

## 9. Gunpowder branch

`DankPyon_Gunpowder` gates:

- gunpowder gathering recipes;
- `DankPyon_Handgonne`;
- acid flask;
- fire pot;
- flash pot;
- smoke pot.

### Direction

The research itself moves to the **late-Sengoku end of AMJ** and is detached
from `Alchemy`.

- `DankPyon_Handgonne` is a strong candidate to become a matchlock /
  `火縄銃` role **only if** its gameplay stats and animation are suitable.
- Fire/smoke projectile containers require separate historical/use audit.
- Acid/flash fantasy/chemical items should not survive simply because they are
  technically under the same upstream research.
- Gunpowder manufacture, firearm adoption and special thrown munitions may need
  separate unlock groups even if upstream uses one node.

The historical anchor is the 1543 Tanegashima introduction followed by
domestic copying and rapid Sengoku diffusion.

---

## 10. Smithing and tailoring are cross-domain nodes

The Def audit shows that broad Vanilla research nodes are not cleanly scoped.

### `Smithing` currently gates at least 22 MO Defs

Including:

- anvil, bellows, furnace, grinding wheel, quenching bucket;
- repair tools / weapon and armor mending;
- mining tools and tool rack;
- metal strongbox / royal chest;
- oil lamp;
- embedded cleaver;
- slop/ragout/fondue cooking pots;
- the MO handgonne;
- several padded Western helmets.

Therefore Japanization cannot treat `Smithing` as “metal weapons only.”
The node needs unlock redistribution by function.

### `ComplexClothing` currently reaches at least 49 MO Defs

The inherited dependency family includes:

- Western garments and under-armor;
- cloth spinner;
- apparel mending;
- many patched cloth/leather/animal/heraldic rugs.

Therefore:

- tailoring can remain a generic craft concept;
- Western garments require individual Japanization/hide decisions;
- decorative carpet/rug content should not all be retained merely because the
  parent Def inherits `ComplexClothing`;
- MO's industrial cloth spinner should not leak into the historical
  Japanization path.

This is also evidence that automated validation must inspect the **loaded final
Def graph**, not only research XML.

---

## 11. Historical anchors

These are evidence anchors for the family-level decisions, not automatic
one-to-one mappings.

- 文化遺産オンライン / 宮城県: `弩機 伊治城跡出土` — eighth-century
  practical military crossbow mechanism.
  - https://online.bunka.go.jp/heritages/detail/430282
  - https://www.pref.miyagi.jp/soshiki/bunkazai/kouko10-doki.html
- 奈良文化財研究所 / related scholarship: ancient state military crossbow
  deployment; research also distinguishes portable and installed crossbows.
  - https://repository.nabunken.go.jp/dspace/bitstream/11177/8274/1/BA62154222_2_090_114.pdf
  - https://cir.nii.ac.jp/crid/1520853832330876416
- e-Museum: 15th-century Muromachi `胴丸`, demonstrating sophisticated
  Japanese composite armor well before the late plate-heavy branch.
  - https://emuseum.nich.go.jp/detail?content_base_id=100513
- e-Museum: 16th-century `南蛮胴具足` and Japanese manufacture influenced by
  imported European cuirasses, useful as a late-period endpoint rather than a
  generic European plate ladder.
  - https://emuseum.nich.go.jp/detail?content_base_id=100509
- 文化遺産オンライン: Kamakura tachi and later Japanese sword examples.
  - https://bunka.nii.ac.jp/heritages/detail/192513
  - https://bunka.nii.ac.jp/heritages/detail/178082
- ColBase: 16th-century Muromachi `打刀` mounting.
  - https://colbase.nich.go.jp/collection_items/tnm/F-15807
- MLIT Kyushu: 1543 firearm introduction at Tanegashima and subsequent
  domestic copying/spread.
  - https://www.qsr.mlit.go.jp/suishin/story2019/03_8.html

---

## 12. Implementation consequences

Before production XML or texture work:

1. Generate a machine-readable **research -> final loaded Def** ledger for the
   audited MO version.
2. For each retained MO weapon/apparel Def, record:
   - Japanese referent;
   - historical band;
   - label/description action;
   - texPath replacement;
   - research replacement;
   - whether material/recipe changes are required.
3. For each hidden Def, ensure:
   - no visible recipe still produces it;
   - no faction/loadout requires it without fallback;
   - no visible research is blocked by its hidden node;
   - external MO-compatibility mods fail gracefully.
4. Do not delete upstream Defs merely to clean the Architect/research UI.
5. Validate faction pawn kinds and traders after armor/weapon hiding: MO factions
   may explicitly request the Western items Japanization intends to hide.
6. Separate historical Japanization from balance redesign:
   keep upstream combat stats unless a stat itself prevents a truthful mapping.
7. Retexture the **complete loaded graphic-state family** of each retained target
   under [Project RetextureImplementationGuidelines](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/Docs/RetextureImplementationGuidelines.md).

## Faction / PawnKind follow-up

The faction/loadout dependency audit is maintained in
[MedievalOverhaulJapanizationFactionLoadoutAudit.md](MedievalOverhaulJapanizationFactionLoadoutAudit.md).
It records hard `apparelRequired` references, weapon/apparel tags, and MO faction
presentation consequences. Military Def hiding/retexture decisions are not
implementation-ready until that loadout audit's generation gate is satisfied.

## Next audit

The next Def-level pass should cover:

- exact weapon stats/material costs to choose the surviving Japanese mappings;
- cooking/food research outputs;
- domestic/production buildings;
- DBH for Medieval research links after the MO tree is rewritten.


---

## 13. Exact weapon-stat pass

The audited MO 1.6.2.2 XML was compared at actual weapon-stat/material level. This pass is used to decide which upstream Defs can honestly carry Japanese referents.

For melee weapons, the values below are the primary damaging tool entries before stuff/quality multipliers. `raw DPS` is only `power / cooldownTime`; it is a comparison aid, not the final RimWorld DPS calculation.

### Crossbows / fixed crossbows

| Def | Loaded role | Key stats | Material/cost | Decision |
|---|---|---|---|---|
| `DankPyon_Crossbow` | handheld crossbow | projectile 16, range 25.9, warmup 1.35, cooldown 2 | WoodLog 50 + IronIngot 20 | **retain as 弩** |
| `DankPyon_CrossbowHeavy` | arbalest | projectile 21, AP .25, range 28.9, warmup 1.35, cooldown 3; clearly more accurate at medium/long range | WoodLog 60 + IronIngot 25 | **retain candidate as 強弩** |
| `DankPyon_Turret_Scorpio` | 1x1 fixed weapon | projectile 22/AP .25; range 28.9; weapon cooldown 3.5 + turret burst cooldown 5 | WoodLog 100 + IronIngot 30 + ComponentBasic 5 + RawWood stuff | **retain candidate as small installed 弩** |
| `DankPyon_Turret_Ballista` | 2x2 fixed weapon | projectile 40/AP .25; range 45; min range 4; warmup 2 | WoodLog 200 + IronIngot 60 + ComponentBasic 10 + RawWood stuff | **conditional: large installed 弩 only if scale/balance remains credible** |
| `DankPyon_Turret_RepeaterBallista` | 2x2 3-shot fixed weapon | 3-shot burst using Ballista projectile | WoodLog 300 + Steel 120 + ComponentBasic 20 + RawWood stuff | **hide** |
| `DankPyon_Turret_Trebuchet` | long-range artillery | mortar-like, range 500 | siege branch | **hide** |

The stat pass resolves the handheld Heavy Crossbow question more strongly than the previous node-only audit: MO's heavy weapon really is a slower, more accurate and harder-hitting version, so it can carry a distinct `強弩` gameplay role without being a pure cosmetic duplicate.

Ancient-Japan scholarship explicitly distinguishes portable and installed crossbows. This supports the *category* of fixed crossbows, but it does not prove that the exact 2x2 MO Ballista with 40 damage / range 45 matches a Japanese installation. Therefore Scorpio is the stronger installed-`弩` reuse candidate and Ballista remains conditional.

Reference:
- https://cir.nii.ac.jp/crid/1520853832330876416

### MO Handgonne is not a retexture-only matchlock

`DankPyon_Handgonne` currently has:

- range **12.9**;
- warmup **1.35**;
- `burstShotCount = 3`;
- effectively immediate burst spacing (`ticksBetweenBurstShots = 1`);
- 15-damage bullet;
- AP .10;
- cooldown 10;
- WoodLog 20 + IronIngot 65;
- Gunpowder + Smithing prerequisites.

**Decision: do not simply relabel/retexture this Def as 火縄銃.**

A three-shot near-instant handgonne burst is mechanically unlike a Sengoku matchlock. If Japanization uses this upstream Def as the late-Sengoku firearm, it must patch the firing Verb/stat profile to a truthful single-shot firearm role; otherwise hide it and let a compatible Japanese weapon Mod provide the firearm.

This is a valid case for gameplay patching because the upstream stat itself prevents a truthful Japanese referent.

---

## 14. Melee stat curation

### Sword / long-blade slots

| Def | Primary attack | AP | Raw DPS | Stuff / fixed cost | First exact-stat treatment |
|---|---:|---:|---:|---|---|
| `Falchion` | Cut 18 / 2.10 | .20 | 8.57 | Metallic 55 | **candidate only** for a lighter/common Japanese sword slot; too close to Arming Sword to guarantee retention |
| `ArmingSword` | Cut 19.25 / 2.15 | .20 | 8.95 | Metallic 60 | **strong retain candidate: 太刀-class ordinary military sword** |
| `FencingSword` | Stab 18.25 / 2.05 | .20 | 8.90 | Metallic 60 | **hide by default**; no need to invent a Japanese fencing-sword equivalent |
| `NobleSword` | Cut 21.15 / 2.21 | .20 | 9.57 | Metallic 75; work 25k | **hide/consolidate**; “noble sword” premium is largely better represented by normal item quality |
| `Longsword` | Cut 26 / 2.79 | .25 | 9.32 | Metallic 100 | **conditional**; retain only if a distinct Japanese long-blade role is selected |
| `Greatsword` | Cut 31.25 / 3.15 | .25 | 9.92 | Metallic 150; VEF range 2.84 | **strong retain candidate: 大太刀-class oversized battlefield blade** |

Historical anchors support real medieval `太刀`, later `打刀`, and large Japanese blade families, but the table shows that MO has more Western sword slots than AMJ needs.

**Curation direction:**
- keep a normal military sword slot;
- keep one oversized/extended-range blade slot;
- retain a lighter later `打刀` slot only if it creates a real cost/speed/gameplay distinction after research redistribution;
- hide Fencing/Noble/redundant sword slots rather than mapping every Western sword name.

Historical anchors:
- Kamakura `太刀`: https://emuseum.nich.go.jp/detail?content_base_id=100184
- Muromachi 16c `打刀` mounting: https://colbase.nich.go.jp/collection_items/tnm/F-15807

### Axes and work tools

Several MO “weapons” also provide actual work bonuses and should be evaluated as tools rather than discarded with Western battle axes.

| Def | Mechanical specialty | First treatment |
|---|---|---|
| `ButcherCleaver` | +10% butchery efficiency, +25% butchery speed; Cut 16.75 | **keep as food/butchery tool**, Japanese visual/name audit |
| `Hatchet` | plant yield +15.5%, plant work +15.5%; same combat line as cleaver | **keep as small chopping tool / 手斧-class role** |
| `Handaxe` | plant yield +15%, plant work +25%; Cut 18.25 | **candidate as vegetation/鉈-like tool**, exact historical label pending |
| `WoodcuttersAxe` | plant yield +20%, plant work +30%; Cut 23.5 | **keep as dedicated woodcutting axe/tool** |
| `FightingAxe` | no work role; Cut 20 | **hide by default** |
| `Bardiche` | Cut 28 | **hide as Western redundant combat axe** |
| `Greataxe` | Cut 31, AP .40 | **hide as Western redundant combat axe** |
| `Longaxe` | Cut 27.5, AP .40, **VEF range 2.84** | **candidate mechanical carrier for 薙刀-class long cutting weapon**, despite the upstream Def family; retexture/research relocation required |

The Longaxe is a good example of Def-preserving Japanization: internal upstream taxonomy does not matter if the actual loaded combat role—long reach, two-handed cutting—maps more honestly to a Japanese long-bladed weapon than some nominal “polearm” Defs do.

### Spears / polearms

| Def | Primary attack | AP | Range | Treatment |
|---|---:|---:|---:|---|
| `MilitiaSpear` | Stab 16.2 / 2.0 | .25 | default | **retain as basic spear / 手鉾・槍-class slot; final chronology label pending** |
| `BoarSpear` | Stab 17.2 / 2.1 | .25 | default | **hide/consolidate** unless a distinct hunting role is preserved |
| `FightingSpear` | Stab 18.8 / 2.2 | .25 | default | **retain candidate as standard military 槍** |
| `Pike` | Stab 25.45 / 2.95 | .30 | **default in current XML** | **long-spear candidate only if Japanization patches meaningful reach; do not call it 長槍 while it behaves like range-1 melee** |
| `Swordlance` | Cut 25.45 / 2.95 | .30 | default | **hide/consolidate** if Longaxe becomes the stronger 薙刀 carrier |
| `Halberd` | Cut 27 / 2.9 | .30 | default | **hide by default**; high stat alone does not justify inventing another Japanese polearm |
| `HookedBlade` | Cut 23 / 2.9 | .30 | default; plant-work bonus | **tool/weapon candidate only**, not a prestige polearm |
| `Pitchfork` / `Warfork` / `Spetum` / `Billhook` | mixed | — | default | **hide/consolidate unless a real tool role survives** |

A key mechanical finding is that MO's nominal Pike does **not** set `VEF_MeleeWeaponRange`, while Longaxe does. Japanization should therefore map by actual role rather than by English weapon name.

A 1322 Kamakura-period naginata survives in the Tokyo National Museum collection, providing a strong historical anchor for a retained long cutting weapon:
- https://emuseum.nich.go.jp/detail?content_base_id=100463

### Maces / hammers / picks

| Def family | Treatment |
|---|---|
| `BlacksmithHammer` | **keep as work tool** (+25% GeneralLaborSpeed) |
| `Pickaxe` | **keep as mining tool** (+25% MiningSpeed, +20% MiningYield) |
| `MilitaryPick` | **hide/consolidate** unless a dedicated combat-pick role is justified |
| `TwoHandedMallet` | **keep primarily as construction/general-labor tool**; combat is secondary |
| `Bludgeon` | **retain candidate as generic club/staff blunt slot** |
| `MorningStar`, `WingedMace`, `Goedendag`, `Warhammer`, `Polehammer` | **hide by default**; do not invent Japanese equivalents for Western forms |
| `TwoHandedMace` / `TwoHandedFlangedMace` | **historical audit still required** before using an `鉄棒 / 金砕棒` referent |

The exact-stat pass therefore shrinks the dedicated blunt-weapon family substantially. Work tools remain useful; Western mace taxonomy does not.

---

## 15. Updated weapon-mapping principles

1. **Use actual stats, not upstream English names, to choose the Japanese carrier Def.**
   - A nominal Longaxe may be the best retained Def for a `薙刀` because it actually has extended melee range.
   - A nominal Pike cannot honestly be called `長槍` unless its range behavior is patched.

2. **Stat changes are allowed only where the upstream stat prevents truthful mapping.**
   - Example: the 3-shot Handgonne cannot become a matchlock by art/label alone.
   - Example: a `長槍` referent requires actual reach.

3. **Tool utility is independent from battlefield taxonomy.**
   Cleavers, hatchets, wood axes, hammers and picks can remain for their work bonuses even when related Western combat variants are hidden.

4. **Do not preserve weapon count for its own sake.**
   MO has many Western variants with near-duplicate combat roles. Japanization should expose a smaller coherent Japanese set while keeping upstream DefNames available for compatibility.

5. **Quality should remain the main craftsmanship axis.**
   Do not preserve “noble sword” / heraldic variants merely to represent better craftsmanship when RimWorld item quality already does that.

## Remaining military decisions

The exact-stat pass resolves:
- handheld Crossbow -> `弩`;
- Heavy Crossbow -> `強弩` as a genuine slower/heavier role;
- Scorpio -> strong installed-`弩` candidate;
- Longaxe -> strongest current `薙刀` carrier candidate;
- Greatsword -> strongest current `大太刀` carrier candidate;
- multiple Western sword/mace/polearm variants can be hidden as redundant;
- Handgonne requires mechanical patching, not only retexture, if it becomes `火縄銃`.

Still unresolved before production mapping:
- exact Ballista retention versus only Scorpio;
- final ordinary sword pair (whether both a `太刀` and later `打刀` slot are worth retaining);
- exact basic-spear / standard-spear / long-spear allocation;
- whether a dedicated `鉄棒 / 金砕棒` combat slot has sufficiently strong historical support and gameplay value;
- firearm stat target and whether Japanization owns that target or defers to a compatible Japanese weapon Mod;
- faction/loadout fallback after hidden Defs are removed from normal generation.


---

## 16. Closed sword / spear / fixed-crossbow mapping

The stat pass plus historical review now closes several remaining choices.

### Fixed crossbows: keep Scorpio, hide Ballista in the baseline

Japanization does not need two separate fixed-crossbow tiers merely because MO has both.

- `DankPyon_Turret_Scorpio` already provides a distinct installed-crossbow niche:
  1x1, 22 damage, AP .25, range 28.9.
- `DankPyon_Turret_Ballista` jumps to 2x2, 40 damage and range 45.

Ancient Japanese research supports the category of installed crossbows, but the larger Ballista adds a second European-siege-shaped tier whose exact scale is not independently justified.

**Decision:**
- `DankPyon_Turret_Scorpio` -> retained installed `弩` / `弩台` role;
- `DankPyon_Turret_Ballista` -> **HIDE from the baseline**;
- `DankPyon_Ballista` research -> remove from the visible standard progression unless another retained output requires it;
- Heavy Crossbow remains the handheld `強弩` role;
- Repeater Ballista and Trebuchet remain hidden.

This keeps one portable ordinary crossbow, one portable strong crossbow, and one installed defensive crossbow without recreating MO's European siege ladder.

### Sword family: expose three meaningful Japanese slots

The six MO Western sword slots are mechanically too redundant to preserve wholesale.

#### `DankPyon_MeleeWeapon_ArmingSword` -> `太刀`

Loaded values:
- 60 Metallic stuff;
- WorkToMake 14,500;
- mass 1.25;
- Cut 19.25 / cooldown 2.15 / AP .20.

**Decision: RETAIN + REINTERPRET as the standard medieval `太刀` slot.**

This is the cleanest ordinary military-sword carrier.

Historical anchor:
- Heian/Kamakura and later tachi are extensively preserved; e-Museum documents a 13th-century Nagamitsu tachi and notes the form's medieval transmission/use.
  https://emuseum.nich.go.jp/detail?content_base_id=100184

#### `DankPyon_MeleeWeapon_Falchion` -> later `打刀` sidegrade

Loaded values:
- 55 Metallic stuff;
- WorkToMake 13,000;
- mass 1.0;
- Cut 18 / cooldown 2.10 / AP .20.

**Decision: RETAIN + REINTERPRET as a later, lighter/cheaper `打刀` sidegrade, not an upgrade over tachi.**

The stat difference is small but coherent: slightly cheaper/lighter/faster and slightly less damaging. This avoids inventing a stronger “later sword” ladder.

Research placement must be moved out of the upstream BasicBlades chronology and placed in the late-medieval branch.

Historical anchor:
- e-Museum notes that from the late Muromachi period swords came to be worn as `刀` and `脇指` thrust through the belt.
  https://emuseum.nich.go.jp/detail?content_base_id=100478

#### `DankPyon_MeleeWeapon_Greatsword` -> `大太刀`

Loaded values:
- 150 Metallic stuff;
- WorkToMake 24,000;
- mass 3;
- Cut 31.25 / cooldown 3.15 / AP .25;
- `VEF_MeleeWeaponRange = 2.84`.

**Decision: RETAIN + REINTERPRET as the oversized `大太刀` battlefield slot.**

The extended reach and heavy material/work cost create a real gameplay distinction.

#### Hide redundant Western sword slots

- `DankPyon_MeleeWeapon_FencingSword` -> **HIDE**
- `DankPyon_MeleeWeapon_NobleSword` -> **HIDE**; item quality already represents superior craftsmanship/status
- `DankPyon_MeleeWeapon_Longsword` -> **HIDE**; its heavy sword niche is superseded by the mechanically distinct extended-range Greatsword/`大太刀`

This leaves three Japanese sword roles instead of preserving six Western names.

### Spear family: 鉾 -> 槍 -> 長槍

#### `DankPyon_MeleeWeapon_MilitiaSpear` -> early `鉾`

Loaded values:
- WoodLog 30 + Metallic stuff;
- WorkToMake 9,000;
- Stab 16.2 / cooldown 2.0 / AP .25.

**Decision: RETAIN + REINTERPRET as the early thrusting `鉾` slot.**

Ancient archaeological collections preserve iron spear/hoko weapons, so the early thrusting role does not need to be forced into a medieval-yari label.

Historical anchors:
- early Kofun-period assemblages include iron spears/hoko:
  https://emuseum.nich.go.jp/detail?content_base_id=100596&content_part_id=3
  https://online.bunka.go.jp/special_content/component/216

#### `DankPyon_MeleeWeapon_FightingSpear` -> standard `槍`

Loaded values:
- WoodLog 30 + Metallic stuff;
- WorkToMake 16,000;
- mass 3;
- Stab 18.8 / cooldown 2.2 / AP .25.

**Decision: RETAIN + REINTERPRET as ordinary military `槍`.**

Remove the upstream “Noble Polearms” placement. The weapon belongs in the normal medieval military branch.

Historical anchor:
- Tokyo National Museum material describes yari as appearing in the Kamakura period and being widely used in warfare from Muromachi onward.
  https://online.bunka.go.jp/heritages/detail/506163

#### `DankPyon_MeleeWeapon_Pike` -> late `長槍`, but only with a reach patch

Loaded values:
- WoodLog 55 + Metallic stuff;
- WorkToMake 15,000;
- mass 2.75;
- Stab 25.45 / cooldown 2.95 / AP .30;
- **no extended melee-range stat in the current MO XML**.

**Decision: PATCH_MECHANICS + REINTERPRET as `長槍`.**

Japanization must add an actual reach distinction before using the long-spear name. Without that patch, hide/consolidate it rather than presenting a range-1 pike as a long spear.

Historical anchors:
- Muromachi 16th-century yari are preserved, and museum explanation explicitly says the spear became a major late-Muromachi battlefield weapon:
  https://online.bunka.go.jp/heritages/detail/603453
- Fukuoka City Museum distinguishes warrior `持槍` from ashigaru `長柄`, supporting a late battlefield long-shaft role:
  https://museum.city.fukuoka.jp/exhibition/528/index02.html

### Naginata carrier

`DankPyon_MeleeWeapon_Longaxe` remains the strongest mechanical `薙刀` carrier:
- Cut 27.5 / cooldown 2.96 / AP .40;
- `VEF_MeleeWeaponRange = 2.84`.

The upstream English taxonomy is irrelevant; actual long-reach cutting behavior is a better fit than MO's nominal Pike or Halberd.

Historical anchor:
- Tokyo National Museum preserves a Kamakura 1322 naginata:
  https://emuseum.nich.go.jp/detail?content_base_id=100463

### Resulting exposed long-weapon set

Baseline Japanization can therefore expose a compact, mechanically differentiated set:

- early `鉾`;
- standard `槍`;
- late `長槍` with real reach;
- `薙刀` as long-reach cutting weapon.

Warfork, pitchfork, spetum, billhook, swordlance, halberd and heraldic pike variants do not need invented Japanese names merely to preserve MO's Western weapon count.

## Remaining military decisions after this pass

Still open:
- blunt dedicated weapon: whether one `鉄棒 / 金砕棒` slot is worth preserving after historical/stat audit;
- exact matchlock stat target for the mechanically patched `DankPyon_Handgonne`;
- armor Def-level curation and faction fallback after Western variants are hidden.

The standard crossbow, sword and spear/naginata carrier sets are now sufficiently defined for the machine-readable decision ledger.


---

## 17. Armor carrier curation

The armor pass now treats MO's Western armor taxonomy as a pool of gameplay
carriers rather than a progression that must survive.

### Main body-armor progression

#### `DankPyon_Apparel_Light_Lamellar` -> `挂甲`

Loaded role:
- 75 stuff;
- WorkToMake 12,000;
- mass 4;
- armor stuff multiplier .52;
- Shell layer;
- neck / shoulders / torso coverage;
- current prerequisite: `DankPyon_ProtectiveClothing`.

**Decision: RETAIN + REINTERPRET as the ancient lamellar `挂甲` slot.**

This is the cleanest direct structural mapping in the MO armor set.

Historical anchor:
- Tokyo National Museum's sixth-century armed-warrior haniwa explicitly
  depicts `挂甲` made by lacing small iron plates and also shows associated
  shoulder, knee, arm and shin protection.
  https://emuseum.nich.go.jp/detail?content_base_id=100200

#### `DankPyon_Apparel_Brigandine` -> `胴丸`

Loaded role:
- 100 Metallic stuff;
- WorkToMake 32,000;
- mass 15;
- armor multiplier .65;
- Shell layer;
- neck / torso / shoulders / arms / legs coverage.

**Decision: RETAIN + REINTERPRET as the principal medieval `胴丸` armor carrier.**

The upstream brigandine construction must not survive as the public historical
description. Recipe/material meaning may need patching toward Japanese
small-plate, leather, iron and lacing construction.

Historical anchors:
- fifteenth-century `胴丸` uses iron/leather small plates and is described as
  a more mobile replacement for heavier older armor:
  https://emuseum.nich.go.jp/detail?content_base_id=101112
  https://emuseum.nich.go.jp/detail?content_base_id=100513

`腹巻` is historically equally important, but Japanization does not need a
second near-duplicate MO body Def solely to display both names. A future
Japanese apparel owner can add a distinct version if it creates a real gameplay
difference.

Historical anchor:
- fifteenth-century `腹巻` became a major/standard armor form in the Muromachi
  period:
  https://online.bunka.go.jp/heritages/detail/480983

#### `DankPyon_Apparel_FullPlate` -> `当世具足`

Loaded role:
- 150 Metallic stuff;
- WorkToMake 38,000;
- mass 15;
- armor multiplier .73;
- Shell layer;
- neck / torso / shoulders / arms / legs coverage.

**Decision: RETAIN + REINTERPRET as the late-medieval heavy `当世具足` slot.**

Do not preserve European full-plate visual semantics. This is the high
protection / high material / high labor carrier for the late Sengoku end of
the armor progression.

Historical anchor:
- late-Muromachi armor transitions toward the new `当世具足` forms, while
  retaining Japanese composite construction:
  https://online.bunka.go.jp/db/heritages/detail/204230

#### `DankPyon_Apparel_Breast_Plate` -> `南蛮胴`

Loaded role:
- 120 Metallic stuff;
- WorkToMake 28,000;
- mass 8;
- armor multiplier .73;
- Shell layer;
- neck / torso / shoulders only;
- same raw armor multiplier as FullPlate but much less coverage/mass.

**Decision: RETAIN + REINTERPRET as a late-Sengoku `南蛮胴` sidegrade.**

This is one of the rare cases where a European-derived upstream armor role has
a direct Japanese late-period historical counterpart. It should be a
torso-focused, lighter sidegrade rather than the universal end-state.

Historical anchor:
- sixteenth-century European cuirasses were imported and imitated in Japan as
  `南蛮胴具足`:
  https://emuseum.nich.go.jp/detail?content_base_id=100509

### Chain armor becomes a side branch, not the middle rung of a ladder

#### `DankPyon_Apparel_Hauberk` -> `鎖帷子`

Loaded role:
- 80 Metallic stuff;
- WorkToMake 27,000;
- mass 6;
- armor multiplier .55;
- **Middle** layer;
- torso / neck / shoulders / arms.

**Decision: RETAIN + REINTERPRET as late-medieval `鎖帷子`.**

The Middle-layer behavior is especially useful: Japanese chain protection can
act as supplementary armor under/with a Shell-layer armor instead of forcing a
European `chain -> plate` progression.

Historical reference:
- Japanese reference works place `鎖帷子` around the late Muromachi period and
  describe it as worn under or over armor for additional protection:
  https://kotobank.jp/word/%E9%8E%96%E5%B8%B7%E5%AD%90-55153

#### `DankPyon_Apparel_Heavy_Hauberk`

**Decision: HIDE from the baseline.**

Its Shell-layer, near-full-body heavy-chain role competes with the Japanese
`胴丸` carrier and would recreate the European chain tier Japanization is
trying to remove.

### Supplementary leg/hand/foot pieces

#### `DankPyon_Apparel_ChaussesPlate` -> `佩楯` candidate

Loaded role:
- Middle layer inherited from armored-pants base;
- legs coverage;
- 80 Metallic stuff;
- WorkToMake 35,000;
- mass 6;
- armor multiplier .458.

**Decision: RETAIN + REINTERPRET as a `佩楯`-class leg-armor carrier.**

The RimWorld body-group abstraction is broader than the exact historical
coverage, so description/art must be honest about the abstraction.

Historical late-medieval armor sets explicitly preserve `佩楯` as part of the
small-armour ensemble:
- https://online.bunka.go.jp/db/heritages/detail/204230

#### `DankPyon_Handwear_GlovesPlate`

**Decision: HIDE.**

It protects only the Hands body group. Relabeling it `籠手` would be
misleading because Japanese kote protect much more of the arm.

Patch hard `apparelRequired` users instead of preserving the item.

#### `DankPyon_Footwear_BootsPlate`

**Decision: HIDE.**

Do not relabel European armored boots as `臑当`; the Def protects Feet rather
than shins/legs. Patch hard PawnKind requirements instead.

### Helmet carrier set

MO has far more Western helmet forms than Japanization needs.

#### Early helmet carrier

Use **one** of the equal-stat padded-metal helmet Defs
(`PaddedNasalHelmet`, `PaddedKettleHelmet`, `PaddedFlatTopHelmet`) as the
early `冑` carrier and hide/consolidate the others.

Loaded shared role:
- 55 Metallic stuff;
- WorkToMake 12,000;
- mass 2.75;
- armor multiplier .45;
- FullHead.

Strong historical anchor:
- the sixth-century armed-warrior haniwa depicts a riveted iron
  `衝角付冑` with cheek and neck protection.
  https://emuseum.nich.go.jp/detail?content_base_id=100200

Exact carrier selection should minimize PawnKind/tag rewrites.

#### Ordinary medieval helmet carrier

Retain one .50-tier MO helmet as the ordinary medieval `兜` carrier. The
existing `DankPyon_Headgear_ChainKettleHelmet` is favored because MO archers
already hard-require it.

Loaded role:
- 60 Metallic stuff;
- WorkToMake 16,000;
- mass 3;
- armor multiplier .50;
- FullHead.

The graphic/description becomes a Japanese helmet with shikoro rather than a
kettle helm with mail.

#### Advanced helmet carrier

`DankPyon_Headgear_GreatHelm`:
- 80 Metallic stuff;
- WorkToMake 20,000;
- armor multiplier .65.

**Decision: RETAIN + REINTERPRET as an advanced `兜` carrier.**

Do not retain the great-helm shape.

#### Elite helmet carrier

`DankPyon_Headgear_ArmetGilded`:
- 90 Metallic stuff;
- WorkToMake 25,000;
- armor multiplier .70.

**Decision: RETAIN CONDITIONALLY as a high-status/decorated late helmet
carrier.**

It may be used for a lord/elite role after removing the European gilded-armet
presentation. The ordinary `Armet`, Sallet, Bascinet and other Western
variants do not all need separate Japanese equivalents.

### Heraldic variants: retain only where they preserve MO faction identity

The four MO noble-house armor/helmet variants are not merely free-floating
cosmetic clutter: settlement PawnKinds hard-require them.

Current examples:
- four `DankPyon_Apparel_Heraldic_Hauberk*c` variants;
- four `DankPyon_Headgear_HeraldicGreatHelm*c` variants.

**Decision: REINTERPRET these generation-linked variants as clan/family-color
Japanese armor/helmet variants rather than hiding them individually.**

Direction:
- heraldic hauberks -> clan-laced / color-differentiated `胴丸`-class armor;
- heraldic great helms -> matching clan helmet variants;
- remove European coats-of-arms/heraldry;
- use Japanese color/lacing/mon presentation only as a presentation layer for
  the retained MO houses;
- do not turn this into AMJ Factions' full clan/heraldry system.

This is a compatibility-minimizing exception to the general rule of hiding
redundant Western color variants.

### Personal heater shields

MO noble-house knights hard-require heraldic heater shields.

**Decision: remove those hard requirements from the Japanized noble-house
PawnKinds rather than inventing Japanese heater shields.**

Japanization may separately audit one ancient handheld `楯` carrier if the
shield mechanic is useful, but medieval noble-house soldiers should not retain
European heater/kite shields merely because the upstream PawnKinds require them.

---

## 18. Faction/PawnKind fallback produced by the armor pass

The armor decisions imply concrete loadout rewrites.

### Retained generic roles

- peasant/common guard: Japaneseized ordinary clothing + work weapon;
- archer: bow/crossbow according to the rebuilt military branch + ordinary
  retained helmet;
- footman: `槍 / 長槍 / 薙刀` set + ordinary helmet + retained medium armor;
- elite warrior/knight role: `太刀 / 大太刀` + `胴丸` or `当世具足` +
  advanced helmet;
- local lord: high-quality retained Japanese armor/helmet and Japanese weapon
  carrier; not a Zweihander/cuirass/throne-knight costume.

### Required hard-reference rewrites already identified

Patch away or replace:
- `DankPyon_Footwear_BootsPlate`;
- `DankPyon_Handwear_GlovesPlate`;
- `DankPyon_Longsword`;
- chain flat-top / Western helmet hard requirements that are not selected as
  retained carriers;
- heater shields;
- Zweihander helmets/cuirasses;
- named Western greatsword/mace/axe/hammer loadouts where the local-lord role is
  retained.

Preserve generation safely by pointing each PawnKind to retained carrier Defs
rather than deleting the upstream Defs.

### Revised main armor progression

The visible historical profile is intentionally much smaller than MO:

1. `挂甲` — ancient lamellar;
2. `胴丸` — medieval main armor;
3. `鎖帷子` — late supplementary chain side branch;
4. `当世具足` — late heavy armor;
5. `南蛮胴` — late torso-focused sidegrade;
6. optional `佩楯` leg protection.

This replaces the Western linear
`protective clothing -> chain -> plate` ladder with Japanese armor families
that have both historical and gameplay distinctions.


---

## 19. Settlement archer bow carrier

The MO 1.6.2.2 ranged-weapon XML confirms a clean military-bow carrier:

### `Bow_War`

Loaded values:
- projectile `DankPyon_Arrow_War`: 21 damage, AP .25, stopping power 1.8;
- range 31;
- warmup 2.2;
- cooldown 1.45;
- WorkToMake 11,500;
- weapon tag `DankPyon_Warbow`.

**Decision: retain/retexture/relabel as the standard medieval Japanese military
bow / `和弓` carrier.**

This is the default replacement for the MO noble-house settlement archer's
upstream `DankPyon_Crossbow` weapon tag.

The crossbow Def still survives, but its technology is moved to the ancient
state-military `弩` branch. Survival of a Def in Japanization does not mean
every upstream medieval PawnKind continues to use it.

### `DankPyon_Bow_Hunting`

Loaded values:
- projectile damage 16;
- range 27.9;
- warmup 1.75;
- cooldown 1.6;
- WorkToMake 7,000.

**Decision: retain as a lighter/common hunting-bow role**, with Japanese visual
treatment. It remains distinct from the military `和弓` carrier by damage,
range, accuracy profile and production cost.

This is enough for the current PawnKind pass; the Vanilla RecurveBow/Greatbow
placements can still be simplified separately if they become redundant after
the full loaded research audit.


---

## 20. Blunt-weapon carrier decision

The remaining dedicated blunt branch can be reduced to **one historical combat
carrier plus genuine work tools**.

### Historical anchor: 金砕棒 / 鉄棒 is valid medieval content

Japanese reference works on 棒術 record several club/staff weapons in medieval
war tales. In particular:

- `義経記` and related medieval material include hardwood / octagonal clubs;
- `太平記` includes `金棒`, `くろがねの棒` and `かなさいぼう`;
- the `かなさいぼう` is described as a roughly eight-shaku long heavy staff,
  reinforced with iron and sometimes fitted with iron studs/rings;
- `金棒` itself is attested in the late-fourteenth-century `太平記`.

Sources:
- コトバンク「棒術」
  https://kotobank.jp/word/%E6%A3%92%E8%A1%93-132109
- コトバンク「金棒」
  https://kotobank.jp/word/%E9%87%91%E6%A3%92-465162

### `DankPyon_MeleeWeapon_Polehammer` -> `金砕棒`

Loaded MO role:
- 60 WoodLog + 70 Metallic stuff;
- WorkToMake 16,000;
- mass 2.75;
- blunt head 24 / cooldown 2.92 / AP .25;
- **`VEF_MeleeWeaponRange = 2.84`**.

**Decision: RETAIN + REINTERPRET as the dedicated `金砕棒` combat slot.**

This is another case where the upstream English weapon name is less useful than
the actual loaded behavior. The long-reach, two-handed blunt role fits the
medieval Japanese heavy-staff weapon substantially better than MO's short
one-handed mace families.

The exact art should represent a long wooden/iron-reinforced heavy staff, not a
European polehammer head.

### Hide redundant dedicated Western blunt weapons

Baseline historical Japanization hides/consolidates:
- `DankPyon_MeleeWeapon_MorningStar`;
- `DankPyon_MeleeWeapon_WingedMace`;
- `DankPyon_MeleeWeapon_Goedendag`;
- `DankPyon_MeleeWeapon_TwoHandedMace`;
- `DankPyon_MeleeWeapon_TwoHandedFlangedMace`;
- `DankPyon_MeleeWeapon_Warhammer`;
- dedicated Western hammer/mace variants whose only purpose is another nearby
  blunt stat slot.

Do **not** create separate `金棒`, `鉄棒`, `金砕棒` ThingDefs just to use
all upstream Western mace Defs. One exposed heavy blunt role is enough.

Work tools remain separate:
- blacksmith hammer;
- pickaxe;
- two-handed mallet where its labor bonus remains useful.

This closes the dedicated blunt-weapon question.

---

## 21. Matchlock conversion constraints

### `DankPyon_Handgonne` cannot survive unchanged

Loaded MO values:
- WorkToMake 12,000;
- WoodLog 20 + IronIngot 65;
- mass 4;
- Accuracy Touch/Short/Medium/Long = .87/.83/.73/.61;
- `ShootingAccuracyPawn +2`;
- cooldown 10;
- warmup 1.35;
- range 12.9;
- **3-shot burst with one tick between shots**;
- each projectile: 15 damage, AP .10, stopping power 3.

This is a short-range burst abstraction, not a Japanese matchlock.

### Target behavior for `火縄銃`

Japanization may reuse this Def only with a mechanical patch. The target is
defined first as a **balance envelope**, not a fixed final number:

- **single shot**, never the current 3-shot burst;
- alpha damage **above Heavy Crossbow's 21**;
- armor penetration **above the retained crossbow/strong-crossbow .25 tier**;
- useful range in the same broad battlefield band as Heavy Crossbow / War Bow
  (roughly mid/high-20s rather than 12.9);
- markedly slower reload/cooldown than bows/crossbows, so sustained DPS does not
  simply supersede them;
- poorer long-range accuracy than the mature bow/crossbow branches unless
  shooting skill/quality compensates;
- remove/reconsider the current flat `ShootingAccuracyPawn +2` bonus;
- preserve a strong stopping/impact identity without retaining shotgun-like
  burst behavior.

The envelope above has now been reduced to one **prototype A** for the first
automated balance test:

- damage **30**;
- AP **.35**;
- stopping power **3**;
- range **28**;
- warmup **2.25 s**;
- cooldown **5.5 s**;
- **one projectile**;
- accuracy Touch / Short / Medium / Long:
  **.75 / .78 / .60 / .35**;
- remove the upstream `ShootingAccuracyPawn +2`.

This yields a rough unarmored/raw cycle DPS of **3.87**, very close to the
upstream 3-shot handgonne's **3.96**, while changing its identity from
short-range burst damage to high-alpha/high-penetration single fire. It remains
below War Bow sustained raw DPS (~5.75) and Heavy Crossbow (~4.83), so the gun's
advantage is concentrated in alpha damage, penetration and stopping power
rather than universal ranged superiority.

The comparison ledger is
`Docs/Research/Data/MedievalOverhaulJapanizationRangedBalance.csv`.

**Prototype A is not yet the production stat line.** Pickle/RimTest or a small
deterministic combat/stat benchmark must compare it against War Bow, Crossbow
and Heavy Crossbow, including armored targets, before final XML values are
fixed.

MO's Handgonne currently has no ammunition-consumption Comp. Japanization
should not expand into a new ammunition system merely to historicalize this
one Def. The first implementation keeps MO's non-ammunition abstraction and
patches only the firing/stat behavior. Ammunition can be reconsidered later
only if it creates enough gameplay value to justify a separate scope decision.

### Relationship with Tasty Armory - Sengoku

`Tasty Armory - Sengoku` is important prior art and an optional-compatibility
candidate because it already contains:
- kanabo/ararebo;
- katana/wakizashi;
- yari/nagae-yari/naginata;
- yumi;
- ban-zutsu / tan-zutsu / samurai-zutsu / o-zutsu.

However:
- it requires Tasty Armory - Core;
- it is a broad later-Sengoku equipment pack rather than an MO Japanization
  layer;
- its author explicitly notes that Vanilla-stat balance is not treated as an
  authoritative target.

Therefore Japanization should **not hard-depend on it and should not copy its
Vanilla stats**. It remains:
- a visual/content prior-art source;
- a direct overlap check before adding any new AMJ-owned equipment Def;
- a future optional compatibility target if users install both.

Source:
- Steam Workshop, Tasty Armory - Sengoku
  https://steamcommunity.com/sharedfiles/filedetails/?id=3494429497

## Remaining military work

The weapon-family, armor-carrier and common-clothing mapping questions are now largely closed. Remaining work is:
- runtime/automated benchmark of matchlock Prototype A before fixing production stats;
- validate all final PawnKind loadouts against hidden/reinterpreted Defs;
- validate settlement/site generation after the research/unlock redistribution is implemented;
- keep the static decision/loadout/research/source-ledger gate green as production patches are added.

Common settlement clothing is no longer a military blocker; its authoritative mapping is maintained in `MedievalOverhaulJapanizationCommonClothingMapping.md`.
