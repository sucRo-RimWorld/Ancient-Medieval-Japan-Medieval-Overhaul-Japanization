# AMJ - Medieval Overhaul Japanization Coordination

This is the authoritative coordination surface for this repository.

Use it only for status, handoff, blockers, and workstream coordination. Confirmed design belongs in `Docs/Design.md`, `Docs/Research/`, machine ledgers, production XML/code/assets, and tests.

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
- hard dependency: Medieval Overhaul;
- role: MO Patch + MO Retexture;
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
- hard dependency: `DankPyon.Medieval.Overhaul`

No GitHub Actions workflow is enabled yet. Add CI only after the static checks are stable enough to avoid notification spam.

First implementation unit:
- implement target research visibility/prerequisite graph from the authoritative research graph and CSV;
- do not begin with texture swaps or isolated recipes before graph/unlock ownership is stable.

### ADD-CHANGENOTE-20261008 — Versioned Workshop update notes

**Owner:** Ancient-Medieval-Japan-Medieval-Overhaul-Japanization packaging/release
**Status:** SOURCE IMPLEMENTED — dedicated metadata CI pending; gameplay/release gates unchanged

Project `Docs/WorkshopChangenotes.md` now applies here: `About/Manifest.xml`, `About/Changelog.txt` and `About.xml` agree on `0.1.0-dev`. A narrow new workflow checks the metadata and YADA retention without running unowned gameplay tests. These subscriber metadata files have no effect on gameplay, packageId or Mod dependency rules. No Steam publishing or new runtime verification occurred.

**Additional high-yield MO source (2026-10-08):** static inventory found GolemRock_Iron_MapGen (ore 450) and GolemRock_Iron_Incident (ore 1000), connected respectively to the common MapGenerator and GolemImpactor Incident; metalChain OFF changes their mineable outputs to IronIngot. Japanization must audit the fantasy Golem MapGen/Incident/Faction/Pawn chain and iron supply together. Standalone Ironmaking does not alter upstream MO. No runtime patch or decision to delete the Defs has been made. Durable detail: `Docs/Research/MedievalOverhaulJapanizationIronSupplyAudit.md`.
