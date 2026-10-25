# AMJ - Medieval Overhaul Japanization Coordination

## MOJ-CARROT-PUMPKIN-COPY-PROPOSAL-20261025 — staged, author text approval pending

**Owner:** Japanization crop descriptions. Proposal branch `feat/mo-carrot-pumpkin-description-proposal-20261025` holds four original MO Plant/Raw ThingDef description replacements and four matching JA DefInjected descriptions. All labels, crop mechanics, research, item balance and graphics unchanged; image work explicitly skipped. Author's historical wording approval is required **before main merge**; do not confuse a reviewed static XPath4/4 source contract with loaded game tests. Formal proposed English/Japanese wording is in `Docs/Design.md` and production XML of this branch, backed by ALIC history and Agriculture's adopted Eastern carrot/Japanese pumpkin botanical targets. Avoid duplicating the work in Agriculture or asking the author to relay owner handoff. Consolidated 1.6 native testing remains later work, not automatically triggered.

## MOJ-AGRI-CARROT-PUMPKIN-PRESENTATION-20261025 — Agriculture botanical target requires MO display ownership

**Cross-repository owner notice, not permission for unapproved text/art:** Agriculture [PR #254](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Agriculture/pull/254), merged main `29a2f0a0534d391ebcfbe25256bd7b25c81f1338`. Agricultural plant-species targets are **Eastern Asian-type carrot** (late 16th–17th century/early Edo boundary; do not claim a common ancient crop or a specifically named modern Kintoki cultivar) and **Japanese pumpkin `Cucurbita moschata`** (16th-century arrival; not modern Western pumpkin `C. maxima`). Agriculture retains current active carrot growth6/yield6/sowSkill4 and pumpkin growth8/yield20/sowSkill8/fertilityMin70%; no production coefficient, crop trade/harvest, era research, images, or texts changed by this review. The prior seven Western pumpkin cooking Bills are excluded by Agriculture; never re-enable them merely to make existing MO localization prose truthful.

**Japanization owner task:** The original MO `DankPyon_Plant_Carrots` description and the Workshop Japanese translation `Lucifel.MedievalOH.JPT` describe a bright orange taproot, while `DankPyon_Plant_Pumpkins` describes a massive bright-orange fruit. Do not label these exact original graphics as fully faithful Eastern carrot/Japanese pumpkin without provenance/asset acceptance. Assess original MO English and Japanese description and seed/crop research presentation together; proposed historical Japanese game prose requires author approval under current editorial rules. **User expressly skipped image work**: no retexture, PNG generation, visual acceptance or stopping other crop work on that basis. Original MO DefNames and all source references must be retained. Numeric gameplay belongs to Agriculture, not Japanization. Source and scenario boundaries: [Agriculture canonical balance review](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Agriculture/blob/main/Docs/Balance/Crops/MO_CarrotPumpkinBalance_20261025.md). No change to production source and no native game testing is claimed.


## MOJ-CGB-TRANSFER-20261019 — crop ownership moved to Grains

**MERGED:** Japanization [PR #17](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Medieval-Overhaul-Japanization/pull/17), `ee05de61c1eeaca9749d0450e3847b56d4b3ae4e`. Former independent CGB hard dependency `sucro.ancientmedievaljapan.cropgrowthbalance` and Japanization's MO lentil sowMinSkill=2 patch removed. Grains [#183](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Grains/pull/183) `89a71ea1b223d46bcab2dec46eadb8f2189c70cf` now owns both six Vanilla/seven MO crop timings and lentil skill2. Retain Japanization's MO plus **five** currently package-identified AMJ world modules requirement (Environment, Grains, Scenarios, Waterworks, Ironmaking); other additions follow the canonical suite policy. Previous six-module and Japanization-owned lentil notes are superseded. Static source-only migration; native Japanization + merged Grains acceptance remains OPEN.


This is the authoritative coordination surface for this repository.

Use it only for status, handoff, blockers, and workstream coordination. Confirmed design belongs in `Docs/Design.md`, `Docs/Research/`, machine ledgers, production XML/code/assets, and tests.

## MOJ-WFF-ENV-MERGE-20261017 — current dependency handoff

**Owner:** Japanization full-suite dependency contract. 2026-10-17 author transferred the former Wild Food Foraging's 12-resource production scope into Environment. Current `About/About.xml` already requires Environment; **no WFF packageId, new dependency, hidden Foraging production provider or duplicate patch should be added**. Continue to require future genuinely independent AMJ modules (Culture, Rice Cultivation etc.) once they exist. Formal source: `Docs/Design.md` and `Docs/Research/MedievalOverhaulJapanizationIntegrationMatrix.md`; historical WFF sources remain archival. No runtime code/Steam changes.

## Status vocabulary

- **OPEN** — needs work
- **IN PROGRESS** — currently being investigated or implemented
- **BLOCKED** — waiting on a prerequisite
- **DONE** — completed and reflected in the proper source of truth
- **ARCHIVED** — retained for history but no longer active

## MOJ-001 — Repository promotion and Project migration

**Requested by:** author (2026-10-08 JST)  
**Owner:** this repository  
**Status:** DONE — dedicated repository established and Project-owned design/tooling migrated

Repository:
`sucRo-RimWorld/Ancient-Medieval-Japan-Medieval-Overhaul-Japanization`

Confirmed baseline:
- formal Mod name: `AMJ - Medieval Overhaul Japanization`;
- **2026-10-16 author correction supersedes this migration baseline:** dependency is **MO + the entire active AMJ world suite**, not MO-only; current package-identified required entries are Environment, Grains, Scenarios, Waterworks, Ironmaking and Crop Growth Balance. Additional AMJ world modules become mandatory after their actual package ID and viable release exist. Other AMJ Mods remain independent without Japanization. This is a full-suite integration, not a MO-only rescue layer;
- role: MO Patch + Retexture for the full AMJ world;
- not a new Core and not the global tech-lock layer;
- independent AMJ modules stay independent;
- Project pre-split design has been migrated here; Project now keeps only ownership/roadmap pointers.

Implementation order after migration:
1. research visibility/prerequisites;
2. unlock redistribution;
3. production/food/textile/architecture/military Def patches;
4. PawnKind/Faction generation patches;
5. DBH for Medieval optional overlay;
6. other owner integrations;
7. static ledger checks;
8. Pickle/RimTest runtime profiles.

## MOJ-002 — Production implementation

**Status:** OPEN — migration validation complete; first Research Patch unit is next

Migration evidence:
- repository initialization: `65ca35f5e99a5cc72d568a548af86e873d104d38`
- ownership / Design / About baseline: `5dfaad2a092c158aac5551f23304a693023d1f88`
- research/data/tooling migration: `677bb363e24ce7e9c210cade2d4e04530828ad20`
- Project pointer cleanup: `97c3a5da8d0ad6d72754ac3467ac7c2c75b6582e`

Package identity:
- `sucro.ancientmedievaljapan.medievaloverhauljapanization`
- **2026-10-16 revised:** hard dependencies in current `About/About.xml` = `DankPyon.Medieval.Overhaul` + six package-identified AMJ world modules; **no MO-only Japanization**. Future independent AMJ components, including Culture and Rice Cultivation, are pending ID/payload and must join the required set before any completed-suite release claim. Author's 2026-10-17 consolidation moved all 12 formerly WFF-owned wild foods into existing required **Environment**: **never add a separate WFF dependency**. Archived/deprecated and generic CCTO/third-party Mods are not silently required.

No GitHub Actions workflow is enabled yet. Add CI only after the static checks are stable enough to avoid notification spam.

First implementation unit:
- implement target research visibility/prerequisite graph from the authoritative research graph and CSV;
- do not begin with texture swaps or isolated recipes before graph/unlock ownership is stable.

### ADD-CHANGENOTE-20261008 — Versioned Workshop update notes

**Owner:** Ancient-Medieval-Japan-Medieval-Overhaul-Japanization packaging/release
**Status:** SOURCE IMPLEMENTED — dedicated metadata CI pending; gameplay/release gates unchanged

Project `Docs/WorkshopChangenotes.md` now applies here: `About/Manifest.xml`, `About/Changelog.txt` and `About.xml` agree on `0.1.0-dev`. A narrow new workflow checks the metadata and YADA retention without running unowned gameplay tests. These subscriber metadata files have no effect on gameplay, packageId or Mod dependency rules. No Steam publishing or new runtime verification occurred.

**Additional high-yield MO source (2026-10-08):** static inventory found GolemRock_Iron_MapGen (ore 450) and GolemRock_Iron_Incident (ore 1000), connected respectively to the common MapGenerator and GolemImpactor Incident; metalChain OFF changes their mineable outputs to IronIngot. Japanization must audit the fantasy Golem MapGen/Incident/Faction/Pawn chain and iron supply together. Standalone Ironmaking does not alter upstream MO. No runtime patch or decision to delete the Defs has been made. Durable detail: `Docs/Research/MedievalOverhaulJapanizationIronSupplyAudit.md`.

## MOJ-FULLSUITE-STRAW-20261016 — Full AMJ requirement and Straw source

**Owner:** Japanization production and Grains already-owned MO threshing. **Status:** SOURCE IMPLEMENTED, STATIC AND NATIVE GATES OPEN. User rejected the mistaken 'MO-only + Japanization with optional AMJ' architecture: Japanization must always run with the full AMJ world suite. `About/About.xml`, `Docs/Design.md` and `Docs/Research/MedievalOverhaulJapanizationIntegrationMatrix.md` now align. Japanization's production `Patches/Production/DisableHayToStraw.xml` suppresses only the small/large MO Drying Rack menu entries for `DankPyon_StrawProcess`; the ProcessDef and other preservation processes remain in place for compatibility. Normal grain Straw supply is Grains' conditional MO threshing output; hay from grass remains direct. Existing saved processors, NPC/world/trade straw availability, final 1.6/1.7 Defs and pre-harvest Straw demand are NOT yet verified. The incomplete future AMJ component set means **no complete-suite release**. Verify static contract and native 1.6 loaded behavior before any release or save migration claim. Project main Coordination receives owner/status routing separately; do not request user handoff.

## MOJ-IRON-CONTRACT-20261010 — Ironmaking identifiers available

**Owner:** Japanization's optional additional MO resource/research overlay.  
**Status:** INTERFACE RECEIVED; loaded-game validation / production adaptation pending.

Ironmaking's actual owner source was merged through [PR #7](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Ironmaking/pull/7), commit `f458279c2adb072e55858742bb754913fb27f00c`. PackageId is `sucro.ancientmedievaljapan.ironmaking`. Ironmaking owns `AMJ_IronSand`, `AMJ_IronSandDeposit`, `AMJ_Charcoal`, `AMJ_IronBloom`, `AMJ_SmallIronFurnace`, `AMJ_ForgeIronBloom` etc., and its **ordinary** MO compatibility already redirects bloom finishing to `DankPyon_Anvil`→`DankPyon_IronIngot`. Japanization must not implement a duplicate baseline compatibility Patch. Pending is Japanization's optional, Ironmaking-presence-gated MO research and MO-owned mining/Mine Shaft/trader adjustment, after actual load and iron supply measurement. No numeric MO rebalance or loaded-game PASS is claimed. The detailed interface contract lives in `Docs/Research/MedievalOverhaulJapanizationProductionPatchManifest.md` and is not duplicated here.

**2026-10-13 new research owner input:** Ironmaking PR #34 (merge `ba627a3ced00fea0e166df83bd785d232431971a`) introduced `AMJ_InitialIronmaking`. The owner already supplies normal MO research-tab routing; Japanization's additional conditional research-graph adaptation remains OPEN. Updated identifier and scope are recorded in the formal production patch manifest.
