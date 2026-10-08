# Ancient & Medieval Japan - Medieval Overhaul Japanization（中世日本 - Medieval Overhaul日本化） Agent Instructions

## Start here

1. Read this file and `main:Docs/Coordination.md`; locate the latest relevant owner/status/evidence, including later corrections. Historical entries are not current approval.
2. Read Project [AGENTS.md](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/AGENTS.md) and [Docs/SharedRules.md](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/Docs/SharedRules.md): apply its stop conditions, then open only the task-relevant canonical procedures.
3. Read the local specification and affected source/tests below. Shared rules are owned by Project; this file owns only local scope and routing. Missing access or conflicting authority blocks the dependent action, not unrelated safe work.

New features cannot enter implementation before the Project [existing-Mod audit gate](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/Docs/Research/ExistingModAudit.md#implementation-entry-gate) covers VE and non-VE alternatives and records why independent implementation is needed. Existing approved behavior is not redesigned by this rule audit.

## Local task routes and stops

- Specification: `Docs/Design.md`; historical/technical evidence: `Docs/Research/`; decision ledgers: `Docs/Research/Data/`; static tooling: `Tools/`.
- Source XML/C# records implementation, not proof of final loaded behavior. Supported runtime profiles must reach ERROR 0 before release claims; follow Project's evidence and test procedure.
- Preserve MO Def identity where required by compatibility and the independent owners listed below. Inspect the actual final patched Def/state before claiming an integration works.
- Release metadata: `Tests/validate_add_changenote.py`; it does not establish gameplay or complete payload readiness.

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

## Compatibility

Hard dependency:
- Medieval Overhaul (`DankPyon.Medieval.Overhaul`)

All other integrations are optional unless Design explicitly changes this.

A standalone AMJ owner remains responsible for its ordinary MO compatibility. This repository owns only the additional adaptation required because Japanization itself reconstructed MO behavior/research/content.

## Historical / design changes

When changing a policy or mapping, audit related research, generation, PawnKinds, recipes/processes, optional integrations and tests before editing one isolated field.

Do not substitute a Japanese label/texture for a mechanically different object merely to preserve upstream content count.
