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
**Status:** IN PROGRESS — dedicated repository created; design/tooling migration underway

Repository:
`sucRo-RimWorld/Ancient-Medieval-Japan-Medieval-Overhaul-Japanization`

Confirmed baseline:
- formal Mod name: `AMJ - Medieval Overhaul Japanization`;
- hard dependency: Medieval Overhaul;
- role: MO Patch + MO Retexture;
- not a new Core and not the global tech-lock layer;
- independent AMJ modules stay independent;
- Project pre-split design is being migrated here and will be reduced to a project-level pointer after migration.

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

**Status:** OPEN — begins after migration validation

First implementation unit:
- implement target research visibility/prerequisite graph from the authoritative research graph and CSV;
- do not begin with texture swaps or isolated recipes before graph/unlock ownership is stable.
