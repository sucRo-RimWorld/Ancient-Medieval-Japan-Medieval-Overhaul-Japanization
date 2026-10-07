> **Project ownership note (2026-10-07):** migrated from Ancient-Medieval-Japan-Grains because AMJ - Medieval Overhaul Japanization has no dedicated repository yet. This Project copy is the current pre-split research source.

# Medieval Overhaul Japanization Faction / Loadout Audit

## Status

This document is the faction and PawnKind follow-up to:

- `MedievalOverhaulJapanizationResearchAudit.md`
- `MedievalOverhaulJapanizationMilitaryMapping.md`

It records why military Japanization cannot stop at research and ThingDef
visibility. Medieval Overhaul 1.6.2.2 directly selects Western weapons and
apparel through PawnKind `weaponTags`, `apparelTags`, and
`apparelRequired`.

This is a design audit, not an implementation claim.

Audited archive:

- `3219596926.zip`
- MO 1.6.2.2
- SHA-256 `6ed379d7c400db43b3af2a9a7fd6203f7f7e99ca1a670d36b0f73fd1adccc9e3`

## Core conclusion

**Japanization must patch MO PawnKinds/loadouts together with the weapon and
armor research/Def changes.**

Hiding a Western item from player production is insufficient when a PawnKind
still:

- requires that exact Def through `apparelRequired`;
- selects it through an apparel/weapon tag;
- belongs to an MO faction whose role/name is explicitly Western or fantasy.

The compatibility-safe approach is:

1. keep upstream ThingDefs where practical;
2. decide which Defs remain visible/usable under Japanization;
3. patch MO PawnKinds to select only the retained Japanese-mapped equipment;
4. patch exact `apparelRequired` references that point to hidden/repurposed
   Western equipment;
5. validate every affected pawn kind can still generate legal gear;
6. then patch faction-facing names/presentation as needed.

## 1. Exact required-item dependencies

Representative hard requirements in the 1.6.2.2 PawnKind XML include:

### Player / scenario pawn kinds

- `DankPyon_HedgeKnight`
  - requires `DankPyon_Footwear_BootsPlate`
  - requires `DankPyon_Handwear_GlovesPlate`
  - uses `DankPyon_Longsword` weapon tag
  - uses hedge-knight apparel tags
- `DankPyon_PlayerMercenary`
  - selects arming sword, morning star, military pick, handaxe, falchion,
    boar spear, billhook, polehammer and longsword tags
  - uses mercenary/heavy-mercenary apparel tags

### Settlement / noble-house pawn kinds

- `DankPyon_SettlementArcher`
  - uses crossbow weapon tag
  - requires quiver and chain-kettle helmet
- `DankPyon_SettlementFootman`
  - uses billhook / polehammer / pike tags
  - requires a closed chain flat-top helmet
- `DankPyon_SettlementKnight`
  - uses morning-star / arming-sword tags
  - requires full plate
- `DankPyon_SettlementLord`
  - selects named greatsword/flanged-mace/greataxe/two-handed-hammer roles
  - requires Zweihander helmet and Zweihander cuirass
- Amboise / Soren / Oswin / Hesse variants
  - directly require heraldic hauberks, heraldic great helms and heater shields.

### General medieval pawn kinds

- `DankPyon_Medieval_Arbalester`
  - uses crossbow and arbalest weapon tags
- `DankPyon_Zweihander`
  - uses greatsword
  - requires full plate + plate boots + plate gloves
- `DankPyon_Medieval_Knight`
  - uses greatsword / two-handed hammer
  - requires full plate + plate boots + plate gloves
- `DankPyon_Medieval_Lord`
  - requires gilded armet + gilded full plate + plate boots/gloves
- `DankPyon_BrigandLeader`
  - selects noble sword, warhammer, arming sword, two-handed hammer,
    greatsword and named greataxe
  - requires splinted boots/gloves.

### Ulrik faction pawn kinds

- `DankPyon_Ulrik_Initiate`
  - requires adorned mail and splinted hand/foot protection
- `DankPyon_Ulrik_Warrior`
  - requires adorned warrior armor and adorned chain headgear
- `DankPyon_Ulrik_Oathbound` / `DankPyon_Ulrik_Lord`
  - require adorned heavy plate, adorned great helm, plate boots/gloves.

### Cultist pawn kinds

Cultist tiers directly require several Western garment/armor Defs and use
hunting-bow/crossbow/arbalest or generic medieval melee tags.

## 2. Weapon-tag dependencies

The XML relies heavily on tags rather than exact ThingDefs. Important tag
families include:

- `DankPyon_ArmingSword`
- `DankPyon_Longsword`
- `DankPyon_Greatsword`
- `DankPyon_NobleSword`
- `DankPyon_MorningStar`
- `DankPyon_Warhammer`
- `DankPyon_Polehammer`
- `DankPyon_Billhook`
- `DankPyon_Pike`
- `DankPyon_Crossbow`
- `DankPyon_Arbalest` / spelling variants used by MO
- `DankPyon_HuntingBow`
- `DankPyon_GreatBow`
- `DankPyon_Warbow`.

### Consequence

When Japanization hides or repurposes a ThingDef, it must audit whether the
Def still participates in a tag used by MO pawn generation.

Preferred options:

1. retain the Def and retexture/relabel it, so existing tag-based selection
   continues to work;
2. remove the Def from the relevant selection surface and ensure another
   retained Def still satisfies the tag;
3. patch the PawnKind to a new/retained tag.

Do not leave a PawnKind with a tag whose only eligible weapon has been hidden
or made unavailable.

## 3. Apparel-tag dependencies

MO uses role tags such as:

- peasant;
- mercenary / heavy mercenary;
- footman;
- knight;
- archer / arbalester helmet;
- brigand;
- lord;
- faction/heraldic variants.

These tags select families whose visual identity is strongly Western.

### Direction

Japanization should prefer **retaining the role tag while changing its eligible
MO apparel family** if the tag is otherwise useful. This minimizes PawnKind
rewrite.

However, when a tag's meaning itself is Western/faction-specific (for example
Zweihander or four heraldic noble-house sets), the tag can be replaced or the
PawnKind can be rewritten.

The final ledger must prove:

- every PawnKind has valid apparel for every required body/layer slot;
- no hidden fantasy/Western item remains as a hard `apparelRequired`;
- no Japanized role accidentally equips mixed Western/Japanese sets through a
  broad inherited tag.

## 4. MO faction presentation

MO 1.6.2.2 contains several faction families with different implications.

### Brigands

`DankPyon_BrigandFaction` is functionally generic banditry.

**First-pass treatment:** retain gameplay role, Japanize presentation/loadouts.

Bandits/raiders are a natural generic role for a medieval-Japan setting. The
Japanization layer can relabel/regear the existing faction without inventing a
new social system.

### Noble House

MO's noble-house content uses:

- `duke` leader title;
- OldWorlder culture;
- castle/heraldic visuals;
- knight/footman/arbalester style PawnKinds;
- Amboise/Soren/Oswin/Hesse heraldic equipment families.

**First-pass treatment:** MO gameplay may be retained, but Western feudal
presentation must not remain unchanged.

Japanization responsibility is limited to making the existing MO faction
consistent with the Japanese setting: labels/titles, MO-owned loadouts and
visuals, and any content that would otherwise expose Western knight/heraldic
gear.

**AMJ Factions remains the owner of new historical Japanese faction structure,
settlement society, temples/shrines, village communities, local powers,
traders and other new faction gameplay.** Japanization must not absorb that
project merely because it patches an MO faction.

### Player kingdom / lone adventurer / mercenary company

These scenario/player FactionDefs use labels such as “New Tavern,”
“New Lone Adventure,” and “New Mercenary Company,” OldWorlder culture, and
Western PawnKinds.

Japanization should patch their presentation/loadouts if they remain available.
Scenario ownership itself remains with the standalone AMJ Scenarios direction
where AMJ-specific starts are provided.

### Knights of Ulrik

`DankPyon_UlrikFaction` is explicitly a Western/fantasy knightly order and its
PawnKinds require adorned mail/full plate tied to Ulrik symbolism.

**First-pass treatment: hide from the standard historical Japanization
profile**, unless a later audit finds a gameplay system that cannot safely be
separated.

Do not relabel “Ulrik” into a Japanese religion or warrior order while keeping
the same religious/fantasy semantics. If its gameplay role is valuable, that
role should be reimplemented or reused only after a separate system-level
audit.

### Cultists / Shadow Sect

The faction is hidden and tied to MO hideout/raid content; its description even
warns not to deactivate it if MO hideouts are to be raided.

**First-pass treatment: compatibility audit required before suppression.**

Unlike a simple visible faction, removing it may break site/quest generation.
Japanization should first determine whether:

- it can remain hidden as an implementation faction while its pawn visuals are
  Japanized;
- the hideout system can target another compatible faction;
- the content should be disabled together as one branch.

Do not remove the FactionDef in isolation.

### Forest / witch / giant-creature factions

These are hidden animal/fantasy factions. Historical Japanization should not
automatically convert European-fantasy monsters into yōkai by relabeling them.

**First-pass treatment:** separate fantasy-content audit; default historical
profile should not depend on them.

## 5. Boundary with AMJ Factions

The responsibilities are:

### Japanization owns

- patching MO FactionDefs enough to remove overt Western/fantasy presentation
  from the retained MO gameplay;
- patching MO PawnKinds/loadouts so retained factions use the Japanized MO
  equipment set;
- suppressing MO faction/content branches that are incompatible with the
  historical profile when safe to do so;
- compatibility with MO quests/sites that depend on those FactionDefs.

### AMJ Factions owns

- new Japanese historical faction archetypes and social structure;
- Japanese settlement/role design that does not already exist as a reusable MO
  gameplay role;
- historically differentiated village, local-warrior, temple/shrine,
  outlaw/trader, etc. systems if implemented;
- new faction-specific mechanics and content.

Thus Japanization may transform an MO “noble house” presentation enough to
avoid a Western castle/knight leak, but it must not become the repository where
the complete AMJ Japanese faction system is designed.

## 6. Implementation gate

Before any military Def is hidden in production XML, an automated audit must
cover at least:

1. all MO PawnKinds and inherited PawnKind parents;
2. exact `apparelRequired` references;
3. `specificApparelRequirements`;
4. weapon/apparel tag resolution after all patches;
5. traders/rewards/loot tables that can still generate the hidden Defs;
6. FactionDefs and PawnGroupMakers;
7. scenario/player FactionDefs;
8. quests/sites that reference Ulrik, cultists, noble houses or brigands;
9. runtime generation of every retained MO combat PawnKind with ERROR 0.

The military retexture/visibility pass is incomplete until this loadout gate
passes.


---

## 7. Concrete PawnKind fallback mapping

The armor/weapon carrier audit now provides enough retained Defs to define the
fallback direction for MO human PawnKinds.

The key rule is:

> Patch the PawnKind/loadout to retained Japanized carriers. Do not keep a
> misleading Western item visible merely because an upstream PawnKind requires
> it.

### Settlement peasant / guard base

`DankPyon_SettlementPeasant` and `DankPyon_SettlementGuard` are abstract
templates used by the noble-house settlement set.

Current issues include:
- padded surcoat / leather tunic / trousers / chausses;
- Western boots/gloves;
- work-weapon pools with warfork/pitchfork/etc.

**Direction:**
- keep the economic/combat role;
- the common-clothing pass is now closed at Def level:
  - `DankPyon_Apparel_Sackcloth -> 小袖`;
  - `DankPyon_Apparel_Trousers -> 袴`;
  - `DankPyon_Footwear_BootsLeather -> 草鞋` as optional footwear after a
    plant-fiber/material patch;
  - `DankPyon_Handwear_GlovesLeather -> 弽` as archery-only equipment,
    **not** generic gloves;
  - `DankPyon_Apparel_Quiver -> 箙`, subject to a bow-only cooldown-effect
    gate;
- padded surcoat / leather tunic / padded chausses are removed from the normal
  settlement base;
- hard-coded `WoolMegasloth`, `DankPyon_Leather_Troll` and ordinary
  leather glove/boot material forcing is removed;
- work tools that remain useful may stay;
- military-looking Western farm/polearm variants should be removed from the
  random pool when a retained Japanese tool/weapon carrier already fills the
  role.

Detailed source: `MedievalOverhaulJapanizationCommonClothingMapping.md`.

### Settlement archer

Abstract template: `DankPyon_SettlementArcher`.

Current:
- weapon tag `DankPyon_Crossbow`;
- hard requires `DankPyon_Apparel_Quiver`;
- hard requires `DankPyon_Headgear_ChainKettleHelmet`;
- faction children hard-require one of four heraldic hauberks.

**Direction:**
- the retained ordinary helmet carrier is
  `DankPyon_Headgear_ChainKettleHelmet` -> Japanese ordinary `兜`, so the
  helmet requirement can remain on the same Def after retexture;
- the four heraldic-hauberk Defs remain as clan-color `胴丸` variants, which
  minimizes child-PawnKind rewrites;
- the crossbow weapon tag must **not** be assumed correct merely because the
  crossbow Def survives elsewhere. Japanization relocates `弩` to the ancient
  state-military branch; the medieval noble-house archer role should normally
  use the retained Japanese bow branch unless a specific profile deliberately
  represents crossbow troops;
- quiver presentation must be audited with the bow branch.

Thus crossbow survival and settlement-archer loadout are separate decisions.

### Settlement footman

Abstract template: `DankPyon_SettlementFootman`.

Current:
- billhook / polehammer / pike weapon tags;
- hard requires `DankPyon_Headgear_ClosedChain_FlatTopHelmet`;
- child houses additionally require heraldic hauberks.

**Direction:**
- replace weapon pool with retained `槍 / 長槍 / 薙刀` carriers;
- use `DankPyon_MeleeWeapon_FightingSpear`, patched
  `DankPyon_MeleeWeapon_Pike`, and/or
  `DankPyon_MeleeWeapon_Longaxe` according to role weighting;
- replace the closed-chain-flat-top hard helmet requirement with the retained
  ordinary Japanese helmet carrier
  `DankPyon_Headgear_ChainKettleHelmet`, rather than preserving another
  Western helmet variant;
- keep faction child heraldic-hauberk Def identity after those Defs are
  reinterpreted as clan-color `胴丸`.

### Settlement knight / elite warrior

Abstract template: `DankPyon_SettlementKnight`.

Current:
- morning-star / arming-sword weapon tags;
- hard requires `DankPyon_Apparel_FullPlate`;
- each house child additionally hard-requires a heraldic great helm and a
  heraldic heater shield.

**Direction:**
- keep `DankPyon_Apparel_FullPlate`, now mapped to `当世具足`;
- keep `DankPyon_MeleeWeapon_ArmingSword`, now mapped to `太刀`;
- remove morning-star from the default elite pool unless the later blunt audit
  retains a Japanese carrier;
- retain each heraldic-great-helm Def as a clan-color Japanese helmet variant;
- **remove heater-shield hard requirements** from the four child PawnKinds;
- do not invent Japanese heater/kite shields merely to preserve the original
  loadout.

### Settlement local lord

Abstract template: `DankPyon_SettlementLord`.

Current:
- named Western greatsword / flanged mace / greataxe / two-handed hammer pool;
- hard requires `DankPyon_Headgear_ZweihanderHelm`;
- hard requires `DankPyon_Apparel_Zweihanders_CuirassFloof`.

**Direction:**
- patch the hard apparel requirements away from the Zweihander family;
- use retained high-status Japanese armor carriers instead:
  - `DankPyon_Apparel_FullPlate` -> `当世具足`;
  - advanced/elite retained helmet carrier;
- weapon pool should use retained Japanese weapon carriers. A named upstream
  Greatsword can survive only if it is Japanized as a named/high-quality
  `大太刀`; named Western mace/axe/hammer roles do not survive merely for
  variety;
- the local-lord role remains an MO gameplay role, not a new AMJ social-class
  system.

### Generic MO lord

`DankPyon_Medieval_Lord` currently hard-requires:
- `DankPyon_Headgear_ArmetGilded`;
- `DankPyon_Apparel_FullPlateGilded`;
- `DankPyon_Footwear_BootsPlate`;
- `DankPyon_Handwear_GlovesPlate`.

**Direction:**
- `ArmetGilded` may remain as the elite/decorated Japanese helmet carrier;
- remove plate boots and plate gloves from the hard requirements;
- do not retain `FullPlateGilded` solely because this PawnKind asks for it.
  Prefer standard `DankPyon_Apparel_FullPlate` with appropriate item quality
  or an explicitly justified Japanese high-status variant.

### Hedge knight / player-start role

`DankPyon_HedgeKnight` currently:
- requires plate boots and gloves;
- uses the Longsword tag.

**Direction:**
- remove plate boots/gloves;
- replace Longsword with the retained standard/heavy Japanese sword carriers;
- patch the role label/presentation if the MO scenario remains exposed;
- AMJ-specific starting-scenario ownership remains with AMJ Scenarios, so
  Japanization only makes the surviving MO role internally consistent.

### Player mercenary

`DankPyon_PlayerMercenary` currently draws from:
- arming sword;
- morning star;
- military pick;
- handaxe;
- falchion;
- boar spear;
- billhook;
- polehammer;
- longsword.

**Direction:**
- narrow the pool to retained Japanese weapon carriers and useful work tools;
- likely core pool: `太刀`, `打刀`, `槍`, `薙刀`, plus selected
  work-tool weapons;
- remove hidden Western weapon tags rather than leaving them available through
  random generation.

## 8. Heraldic house variants after Japanization

The four MO noble-house color families can remain as **presentation variants**
without becoming a full AMJ clan system.

Keep:
- four heraldic-hauberk DefNames -> clan-color/lacing `胴丸` variants;
- four heraldic-great-helm DefNames -> matching clan helmet variants.

Remove/patch:
- heraldic heater shields;
- European coats of arms and house symbolism;
- duke/knight/footman/arbalester terminology;
- Western weapon requirements.

This is a compatibility-preserving use of existing MO Def identity and
generation structure. New historically differentiated Japanese clans/factions,
settlement society and faction mechanics remain AMJ Factions responsibility.

## 9. Updated generation gate

The runtime test must generate at least one pawn from every retained concrete
MO noble-house/player combat PawnKind after the loadout patches.

For each generated pawn assert:
- no hidden Western weapon/apparel Def is equipped;
- every hard required apparel reference resolves;
- no apparel-layer conflict prevents generation;
- no heater shield remains on the Japanized noble-house knight role;
- no plate boots/gloves remain as hard requirements;
- clan-color armor/helmet variants still resolve for all four MO house families;
- weapon tags resolve to at least one allowed retained weapon;
- runtime ERROR 0.

Static XML checks must additionally fail if a future MO update adds a new hard
`apparelRequired` or weapon tag to an audited PawnKind without a corresponding
decision-ledger entry.


---

## 10. Common-clothing loadout closure

The commoner-clothing audit is now complete enough to close the settlement
base-template blocker.

### Peasant base

Replace the current mandatory:
- padded surcoat;
- leather boots;
- leather gloves;
- Vanilla pants;

with:
- `DankPyon_Apparel_Sackcloth` -> `小袖`;
- `DankPyon_Apparel_Trousers` -> `袴`.

Do not hard-require footwear.

### Guard base

Replace the current mandatory:
- padded surcoat;
- leather tunic;
- trousers;
- padded chausses;
- leather gloves;
- leather boots;

with:
- `DankPyon_Apparel_Sackcloth` -> `小袖`;
- `DankPyon_Apparel_Trousers` -> `袴`.

Role subclasses add their own combat kit.

### Archer-only accessories

Settlement Archer additionally uses:
- `DankPyon_Handwear_GlovesLeather` -> `弽`;
- `DankPyon_Apparel_Quiver` -> `箙`.

The quiver cooldown effect must be bow-scoped or removed; it must not become a
generic firearm/crossbow speed buff.

### Material cleanup

Remove settlement-specific forced use of:
- `WoolMegasloth`;
- `DankPyon_Leather_Troll`;
- `Leather_Plain` for mandatory everyday glove/boot slots.

The generated faction should use historically neutral textile/material
selection unless a retained combat item has its own justified material rule.

This completes the ordinary apparel dependency mapping required before the
static loadout comparison test.
