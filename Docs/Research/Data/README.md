# MO Japanization machine-readable audit data

This directory contains machine-readable design data for the pre-split `AMJ - Medieval Overhaul Japanization` workstream.

## `MedievalOverhaulJapanizationDecisionLedger.csv`

Purpose:
- machine-readable **design disposition** for audited Medieval Overhaul 1.6.2.2 research, Defs and processes;
- lets later static/runtime tests compare the loaded game against decisions already made in the Project design;
- prevents a future MO update from silently making a hidden Western/fantasy output visible again.

It is **not** the final loaded Def graph and does not claim runtime validation.

### Columns

- `source_version` — audited upstream MO version.
- `def_type` — ResearchProjectDef / ThingDef / ProcessDef / other source type.
- `def_name` — upstream DefName. Preserve upstream names when practical.
- `domain` — broad audit area.
- `decision`
  - `KEEP`
  - `REINTERPRET`
  - `CONDITIONAL`
  - `HIDE`
  - `PATCH_MECHANICS`
  - `SPLIT_OUTPUTS`
- `japanese_referent` — current intended Japanese functional referent, blank when hidden/unresolved.
- `mechanical_patch` — whether label/art alone is insufficient.
- `research_action` — expected research/unlock treatment.
- `generation_sensitive` — whether faction/site/settlement generation must be checked before changing visibility or behavior.
- `compatibility_action` — how the upstream Def identity is preserved.
- `confidence` — current design confidence, not test confidence.
- `notes` — concise rationale.

## Required generated ledger before implementation

Before production Patch XML, generate a separate source/runtime ledger from the actual supported load profiles containing at least:

- final loaded Def type + DefName;
- research prerequisites and visibility;
- recipes/products;
- Processor Framework process attachment;
- parent/inheritance relationships relevant to hidden outputs;
- PawnKind/apparel/weapon references;
- StructureLayoutDef/SymbolDef/site-generation references;
- texPath / graphic family for retained retextures;
- optional-integration origin (DBH for Medieval, Grains, Ironmaking, etc.).

The generated ledger must be compared against the decision ledger.

Minimum gates:
1. no `HIDE` entry is visible/produced/spawned through an unpatched path;
2. no visible research has a hidden blocking prerequisite;
3. no generation-sensitive hidden/replaced Def is still emitted by an unpatched layout/symbol;
4. every `REINTERPRET` retexture resolves to an AMJ-owned texture path;
5. every `PATCH_MECHANICS` entry has an explicit mechanical patch test;
6. upstream MO additions in audited research/furniture/military families cause the ledger check to fail until classified.

Runtime success remains a separate Pickle/RimTest requirement; passing this CSV/static comparison alone is not a runtime PASS.


## `MedievalOverhaulJapanizationLoadoutLedger.csv`

Purpose:
- machine-readable PawnKind/template loadout rewrites implied by the military decision ledger;
- records hard apparel requirements to remove/replace and weapon-tag pools to rewrite;
- prevents hidden Western equipment from re-entering through NPC generation even when its ThingDef remains for compatibility.

The runtime gate must compare every retained concrete PawnKind against this ledger after inheritance and patches are resolved.


## MO source dependency ledger generator

`Tools/generate_mo_japanization_source_ledger.py` reads an author-supplied MO
ZIP or extracted source tree and emits a derived source-level CSV.

Baseline example:

```bash
python Tools/generate_mo_japanization_source_ledger.py \
  /path/to/3219596926.zip \
  --version 1.6 \
  --source-version-label 1.6.2.2 \
  -o /tmp/mo-source-ledger.csv
```

The baseline scans `1.6/Defs/` and `1.6/Patches/`. Optional integration
folders under `1.6/Mods/<folder>/` are opt-in through repeated
`--include-optional` arguments.

The generator resolves KCSG `StructureLayoutDef -> SymbolDef -> ThingDef`
indirection when counting generated-layout usage. This matters because a
ThingDef may appear only a few times directly while its materialized SymbolDef
is used thousands of times in generated layouts.

This remains **source evidence, not final loaded-runtime truth**:
PatchOperations, Def inheritance after loading, active DLC/optional profiles and
runtime C# behavior require separate static/runtime validation.

The full generated CSV is intentionally not committed because it is a large,
reproducible derivative of the third-party MO archive. Audited hashes and
summary counts are recorded in
`MedievalOverhaul-1.6.2.2-SourceLedgerManifest.md`.


## Static design/source comparison checker

`Tools/check_mo_japanization_ledgers.py` compares:

- a generated MO source ledger;
- `MedievalOverhaulJapanizationDecisionLedger.csv`;
- `MedievalOverhaulJapanizationLoadoutLedger.csv`.

Example:

```bash
python Tools/check_mo_japanization_ledgers.py \
  --source /tmp/mo-source-ledger.csv
```

Default mode is a **design-integrity gate**, not a production PASS. It fails on
structural mistakes such as:

- duplicate decision/loadout actions;
- a Project decision pointing at a missing MO-owned Def identity;
- a loadout row pointing at a missing MO PawnKind/ThingDef;
- a loadout weapon tag that has no MO source tag/carrier.

It reports unresolved implementation work as warnings, including:

- `PATCH_MECHANICS` entries that still require an explicit mechanical/runtime
  test;
- hidden Defs that are still referenced by source PawnKinds or generated
  layouts and therefore require production patches/fallbacks.

`--strict` promotes those warnings to failures. **Do not treat strict mode as
expected to pass before the production Japanization patch exists.** The intended
sequence is:

1. source + design-ledger integrity passes;
2. production XML/C# patches are implemented;
3. strict static comparison passes against the patched/final source model;
4. Pickle/RimTest validates the final loaded runtime profiles with ERROR 0.

The checker does not replace RimWorld's actual load/patch resolution.


## `MedievalOverhaulJapanizationRangedBalance.csv`

Small combat-balance comparison ledger for retained MO ranged carriers and
Japanization test candidates.

It currently records:
- Hunting Bow;
- War Bow / 和弓 carrier;
- Crossbow / 弩;
- Heavy Crossbow / 強弩;
- upstream Handgonne;
- `火縄銃 Prototype A`.

`raw_damage_per_second` is only
`alpha_damage / (warmup + cooldown)` and intentionally ignores hit chance,
armor, quality, pawn shooting skill, burst-tick details and runtime modifiers.
It is useful for spotting gross balance mistakes, not for declaring gameplay
balance.

Prototype A remains a test target until automated combat/stat comparison and
runtime testing are complete.


## `MedievalOverhaulJapanizationResearchGraph.csv`

Machine-readable disposition for the complete audited **67-node**
MO-owned + MO-reworked-Vanilla research surface.

It records:
- visible / conditional / hidden / detached state;
- target player-facing meaning;
- final intended prerequisites;
- merge/detach/reinterpret action.

The static checker verifies uniqueness, the expected 67-row surface, prerequisite
resolution, and that visible research does not depend on hidden/detached nodes.

## `MedievalOverhaulJapanizationDBHResearchOverlay.csv`

Machine-readable optional overlay for DBH for Medieval.

It records the retained/hide/later-tech treatment and target prerequisite graph.
The static checker verifies:
- visible DBH nodes do not depend on hidden DBH nodes;
- MO parents resolve to visible nodes in the target MO graph;
- retained historical DBH nodes do not depend on hidden `DankPyon_Windmill`
  or modern `Plumbing`.

Runtime DBH source/behavior validation remains a separate compatibility-profile
test.
