# Medieval Overhaul 1.6.2.2 source-ledger manifest

This records the reproducible baseline used by the Project-owned pre-split
`AMJ - Medieval Overhaul Japanization` audit.

## Input

- source: author-provided Medieval Overhaul Workshop archive
- MO version: `1.6.2.2`
- RimWorld source folder: `1.6`
- archive SHA-256:
  `6ed379d7c400db43b3af2a9a7fd6203f7f7e99ca1a670d36b0f73fd1adccc9e3`
- baseline scan: `1.6/Defs/` + `1.6/Patches/`
- optional `1.6/Mods/*` profiles: not included in this baseline

## Generator result

Command shape:

```bash
python Tools/generate_mo_japanization_source_ledger.py \
  3219596926.zip \
  --source-version-label 1.6.2.2 \
  -o mo-source-ledger.csv
```

Observed result:

- XML files scanned: **321**
- emitted Def rows: **2,930**
- unique XML identities: **2,777**
- XML parse errors: **0**
- unsupported identifier-token forms: **0**
- generated CSV bytes: **569,366**
- generated CSV SHA-256:
  `ce12ba1dc1d47643c00f258bfa888b4b66e082472a8c6c5bddf800f2c2cc65cf`

Major baseline Def counts include:

- ThingDef: 1,210
- KCSG.SymbolDef: 785
- RecipeDef: 213
- PawnKindDef: 115
- ProcessorFramework.ProcessDef: 80
- TerrainDef: 79
- ResearchProjectDef: 51
- ThoughtDef: 49
- HediffDef: 48
- KCSG.StructureLayoutDef: 31
- FactionDef: 18

## Corrected generation-reference examples

The generator distinguishes direct XML references from KCSG layout-cell uses
that reach a ThingDef through SymbolDefs.

| ThingDef | direct generation refs | layout cells via SymbolDef | total generation refs |
|---|---:|---:|---:|
| `DankPyon_CastleWall` | 3 | 8,565 | 8,568 |
| `DankPyon_CastleWallEmbrasures` | 2 | 342 | 344 |
| `DankPyon_RusticDoor` | 6 | 911 | 917 |
| `DankPyon_ReinfocedLogGate` | 4 | 122 | 126 |
| `DankPyon_RusticCloset` | 4 | 83 | 87 |
| `DankPyon_RoyalArmchair` | 4 | 38 | 42 |
| `DankPyon_RoyalTudorBed` | 3 | 22 | 25 |

The older hand audit's “8,919 CastleWall references” was a raw substring count
of the `DankPyon_CastleWall*` family and therefore mixed ordinary wall and
embrasure symbol names. It is superseded by the SymbolDef-aware figures above.

## Scope limit

This manifest does not claim:
- final loaded Def resolution;
- optional DLC / compatibility-profile resolution;
- runtime generation success;
- production Japanization Patch success.

Those remain later static + Pickle/RimTest gates.
