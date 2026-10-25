# Ancient & Medieval Japan - Medieval Overhaul Japanization（中世日本 - Medieval Overhaul日本化）

## Status — retirement migration / 廃止移管中

**2026-10-25 author decision:** Stop development and planned standalone publication of the all-suite Japanization Mod. Each functional AMJ Mod now owns optional Medieval Overhaul adaptation in its respective domain. This legacy repository remains **temporarily active only for features that have no accepted successor** and to preserve archived designs and previously verified source. Do not delete its package or DLL while legacy saves can still contain its components.

**作者方針:** MO日本化は各機能Modで任意互換として直接実施する。Japanizationの独立公開・一括日本化の新規開発は停止し、既存実装は安全な単位で担当Modに移管する。本リポジトリは旧セーブや未移管機能のため暫定維持する。

### Migrated to Agriculture / Agricultureへ移管済み

[Agriculture PR #258](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Agriculture/pull/258), merged main `ced45d030c39ac1273d71a83fd4111d1941700da`, owns these **MO-conditional** files:

- Japanese apple tree and fruit text and the original MO `Cocoa` fruit-tree/silkworm research text;
- Eastern carrot and Japanese pumpkin plant/item descriptions;
- MO flax→ramie, raw fiber/cloth and associated production/research descriptions;
- removal of the Hay→Straw process menu item from both MO drying racks;
- five accompanying Japanese DefInjected XML files, loaded only with MO.

The previous four production patches and five localization sources were removed here after the Agriculture copy was merged and source-verified, to avoid duplicate overrides. No agricultural DefName, recipe/item coefficient or texture changed.

### Still present in this legacy Mod / 未移管

- `Patches/Production/DisableGriffonOrdinaryAcquisition.xml` — Griffon ordinary incident/trading access restriction; future fauna/event/world-generation owner **unassigned**.
- `Patches/Production/RoofedDryingRacks.xml` — Roofed MO drying racks and food-drying weather factors; future preservation owner **unassigned**.
- `Patches/Production/RainDamageDryingRacks.xml`, `1.6/Assemblies/AncientMedievalJapanMOJDrying.dll`, `Source/AMJ.MOJ.Drying/` — rain spoilage `ThingComp`, still connected to original MO racks. Its legacy class/save references prohibit unverified removal or renaming.

The old hard-dependency metadata remains unchanged for this **unreleased legacy development package**. It is not a recommendation for a new full-suite dependency chain. No new requirement on Agriculture, Environment or other owners is introduced.

### Evidence and limitations

Existing original RimWorld 1.6 Japanese acceptance [Actions #40168425002](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/40168425002) was for the old **Japanization-present** source pins; it does **not** validate the distributed Agriculture-only profile or modernized optional translation precedence. Confirm all remaining runtime features have successor owners and preserve old-save references before final archival or unpublishing.

Formal migration state: `Docs/Design.md`, Project `Docs/Architecture.md` and `Docs/Roadmap.md`. Historical full-suite research mapping remains archival only.
