# Ancient & Medieval Japan - Medieval Overhaul Japanization（中世日本 - Medieval Overhaul日本化）

Official **Ancient & Medieval Japan (AMJ)** integration layer for **Medieval Overhaul**.

This mod keeps Medieval Overhaul's useful medieval systems and Def identities where practical, while reconstructing its research flow, equipment, production, buildings, generated content, labels, and graphics around ancient-to-medieval Japan.

## Status

Early development. Design migration from `Ancient-Medieval-Japan-Project` is in progress.

## Dependency

Required:
- Medieval Overhaul

Optional compatibility is planned for other AMJ modules and selected medieval frameworks. Those modules are not baseline hard dependencies.

## Design principle

This is not a new AMJ Core and not a generic medieval-tech lock.

Japanization works at Def / Recipe / Process / research / generation level:
- retain and reinterpret useful MO systems;
- hide or disconnect Western/fantasy branches with no honest Japanese counterpart;
- preserve upstream Def identities where compatibility benefits from doing so;
- keep independent AMJ gameplay modules independently usable;
- reconstruct MO's visible progression around ancient-to-medieval Japanese technological history.

Edo / early-modern completed systems are outside the baseline AMJ scope.

## Development sources of truth

- `AGENTS.md`
- `Docs/Design.md`
- `main:Docs/Coordination.md`
- `Docs/Research/`
- `Docs/Research/Data/`

The Project meta repository remains the AMJ-wide architecture/roadmap hub, but this repository is now the authoritative owner of Medieval Overhaul Japanization implementation and design.
