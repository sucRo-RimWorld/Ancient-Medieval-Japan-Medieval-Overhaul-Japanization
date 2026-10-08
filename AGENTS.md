# Ancient & Medieval Japan - Medieval Overhaul Japanization（中世日本 - Medieval Overhaul日本化） Agent Instructions

This repository is the authoritative design and implementation owner for **Ancient & Medieval Japan - Medieval Overhaul Japanization（中世日本 - Medieval Overhaul日本化）**.

Before starting work:

1. Read this file.
2. Read the authoritative coordination log at `main:Docs/Coordination.md`.
3. Read `Docs/Design.md` and the relevant `Docs/Research/` source for the task.

## Source hierarchy

- Confirmed mod design and ownership boundaries -> `Docs/Design.md`.
- Detailed historical/technical audits -> `Docs/Research/`.
- Machine-readable decisions and validation inputs -> `Docs/Research/Data/`.
- Current cross-workstream handoff/status -> `main:Docs/Coordination.md`.
- Permanent repository operating rules -> `AGENTS.md`.
- Runtime truth -> committed XML/Patches/Defs/Textures/C# and tests.

Repository sources take precedence over accumulated chat history or memory.

## Coordination

Do not use the user as a messenger between chats, agents, repositories, or workstreams.

If another repository must act, record the request/handoff in that repository's authoritative `main:Docs/Coordination.md`.

`Docs/Coordination.md` is status/handoff only. Confirmed specifications must also be reflected in Design, Research, code/XML, localization, or tests.

The authoritative Coordination file exists only on `main`. Do not create branch-specific copies.

## Scope

This mod:
- requires Medieval Overhaul;
- is MO Patch + Retexture, not a new AMJ Core;
- reconstructs MO research, Def/Recipe/Process exposure, equipment, buildings, generation, presentation and selected mechanics around ancient-to-medieval Japan;
- preserves upstream MO Def identity where compatibility benefits from it;
- keeps independent AMJ gameplay modules independent and integrates them only through optional compatibility;
- does not treat World Tech Level or another global tech-lock mod as a hard dependency;
- excludes Edo/early-modern completed systems from the baseline AMJ scope.

Do not absorb Grains, Ironmaking, Rice, Waterworks, Hot Springs, Fermentation/Brewing, Clothing, Factions, or other standalone-owner gameplay loops merely because MO has related infrastructure.

## Reuse granularity

Audit and patch MO at the smallest honest level: ResearchProjectDef / ThingDef / RecipeDef / ProcessDef / PawnKind / StructureLayout/Symbol / graphic family.

Do not keep an invalid Western/fantasy process merely because its building, framework, or C# is useful.

Prefer:
1. keep as-is when valid;
2. reinterpret/retexture when gameplay role genuinely maps;
3. patch mechanics when art/label alone would be misleading;
4. hide/disconnect when no honest baseline role exists.

## Retexture ownership

This repository owns Japanese retextures of **MO-owned Defs**.

Other AMJ modules own art for their own Defs. Avoid multiple AMJ mods overwriting the same MO texPath.

A retexture is incomplete until directional variants, masks, stuff/quality states and generated-site use are audited.

## Testing

Prefer automated testing with RimTest Redux and Pickle. Human manual testing is for visual/interaction checks that automation cannot cover.

Before enabling or modifying GitHub Actions:
- inspect existing workflow triggers;
- run equivalent static/local checks where possible;
- do not push a sequence of knowingly failing workflow changes that generates notification spam.

Static validation should use the ledgers under `Docs/Research/Data/` and tooling under `Tools/`.

Runtime supported profiles must reach ERROR 0 before release claims.

## Compatibility

Hard dependency:
- Medieval Overhaul (`DankPyon.Medieval.Overhaul`)

All other integrations are optional unless Design explicitly changes this.

A standalone AMJ owner remains responsible for its ordinary MO compatibility. This repository owns only the additional adaptation required because Japanization itself reconstructed MO behavior/research/content.

## Historical / design changes

When changing a policy or mapping, audit related research, generation, PawnKinds, recipes/processes, optional integrations and tests before editing one isolated field.

Do not substitute a Japanese label/texture for a mechanically different object merely to preserve upstream content count.

## Reporting GitHub changes

Only report that files were updated when the change was actually committed to GitHub. Always provide actual commit SHA(s).

## World Tech Level recommendation (AMJ common)

**Confirmed:** 2026-10-08 JST.

> AMJとして古代～中世に限定した世界を構成する場合は World Tech Level の Medieval 設定を推奨。

This is a conditional recommendation for assembling an era-limited AMJ world, not a mandatory dependency or a prerequisite for using this individual Mod. Distinguish it from feature-specific compatibility/recommendations when preparing public descriptions. Do not claim that Medieval tech filtering guarantees Japanese historical/cultural suitability or removes every inappropriate event.

Canonical policy: [Project architecture — era-limited world recommendation](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/Docs/Architecture.md#era-limited-world-recommendation).

The proposed **Ancient & Medieval Japan - World Rules** remains an uncommitted idea in Project `Docs/Ideas.md`; its ownership, filter scope and relationship/dependency to World Tech Level must be decided separately. Do not add global Incident/Quest/Trader/MapGen filtering to this Mod merely because the recommendation exists.

## Shared rules owner — AMJ Project

Project owns all AMJ-common policy. Before applying a shared rule, read the current [SharedRules index](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/Docs/SharedRules.md) and the relevant canonical document there. This repository owns only its Mod-specific specification/procedure; do not develop shared rules in Grains or another runtime Mod.

For AMJ Workshop previews (including text-only image ideas), read Project `Docs/WorkshopCoverStyle.md`, `Docs/GoldenPaths/WorkshopCoverPipeline.md` and `Docs/References/AMJ_WorkshopCover_Manifest.md`, and inspect the actual registered Project reference/base/mask. Present a text composition proposal before generating a new cover. An image-idea request alone does not authorize generation. Never regenerate the common pixels or restore an obsolete cover layout.

## Add Changenote release metadata

Follow the Project `Docs/WorkshopChangenotes.md` canonical version/changelog rule. Keep `About/About.xml` `modVersion`, `About/Manifest.xml` `version` and the current heading in `About/Changelog.txt` identical. Include both in the subscriber payload and run `python Tests/validate_add_changenote.py`. This is author-side publishing tooling, not a player dependency or a completed-release claim.
