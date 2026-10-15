# Ancient & Medieval Japan - Medieval Overhaul Japanization（中世日本 - Medieval Overhaul日本化）

Official **Ancient & Medieval Japan (AMJ)** integration layer for **Medieval Overhaul**.

This mod keeps Medieval Overhaul's useful medieval systems and Def identities where practical, while reconstructing its research flow, equipment, production, buildings, generated content, labels, and graphics around ancient-to-medieval Japan.

## Status

Early development. Design migration from `Ancient-Medieval-Japan-Project` is in progress.

## Dependency

Required:
- Medieval Overhaul
- AMJ - Environment
- AMJ - Grains
- AMJ - Scenarios
- AMJ - Waterworks
- AMJ - Ironmaking
- AMJ - Crop Growth Balance

Japanization is an **all-AMJ-suite integration**: MO-only or partial-AMJ Japanization profiles are intentionally unsupported. More AMJ world modules (e.g. Culture, Wild Food Foraging, Rice Cultivation) become required as their real package IDs and playable releases become available; the all-suite product is **not release-ready** before then. Generic CCTO, DBH, World Tech Level, VE and other external Mods are outside this suite requirement and remain independently optional. Each underlying AMJ Mod is usable without Japanization.

## Design principle

This is not a new AMJ Core and not a generic medieval-tech lock.

Japanization works at Def / Recipe / Process / research / generation level:
- retain and reinterpret useful MO systems;
- hide or disconnect Western/fantasy branches with no honest Japanese counterpart;
- preserve upstream Def identities where compatibility benefits from doing so;
- keep independent AMJ gameplay modules independently usable;
- reconstruct MO's visible progression around ancient-to-medieval Japanese technological history;
- use Grains grain-threshing straw instead of converting harvested Hay into cereal Straw in drying racks (1.6 source patch; native game verification pending).

Edo / early-modern completed systems are outside the baseline AMJ scope.

## Development sources of truth

- `AGENTS.md`
- `Docs/Design.md`
- `main:Docs/Coordination.md`
- `Docs/Research/`
- `Docs/Research/Data/`

The Project meta repository remains the AMJ-wide architecture/roadmap hub, but this repository is now the authoritative owner of Medieval Overhaul Japanization implementation and design.
