# Wall-mounted drying pole — bounded prior-art comparison

**Status:** implementation candidate on Japanization topic branch; not gameplay-tested or art-accepted. No new drying processing framework.

## What players need
Compact 1-cell and long 2-cell wall attachments for small daily batches under traditional Japanese house eaves without blocking a floor tile. It should reuse the same MO PF recipes, yields and controls rather than introduce another food or processing system.

## Prior art
- **Non-VE:** Medieval Overhaul 1.6.2.2 already has 2×1 (capacity 100) and 2×2 (200) stand-alone drying racks. Japanization already permits roofed placement and supplies rain spoilage; these racks still occupy floor space.
- **Non-VE:** Food Drying (Steam 3664822476, checked 2026-10-22) has non-powered food drying mesh/tray options plus powered machines. Its general drying gameplay is sufficient and remains an independent/optional choice, but its described equipment does not establish a MO-compatible wall-attached small-batch rack.
- **Non-VE:** Dried Fish (3773705093) supplies a free-standing fish rack for cold stockfish, not a MO PF wall-mounted general rack. Wall-Mounted Function Furniture (3807382130) is a separate precedent for wall-hanging functionality, not evidence of food drying.
- **VE:** Vanilla Factions Expanded - Medieval (1854610483), Vanilla Expanded framework/content and the 'Medieval - Less Wood Please' rack variants were compared as medieval-equipment precedents; no documented equivalent MO PF wall-mounted drying pole was confirmed from available descriptions. Avoid adopting broad VE content dependencies for this narrowly defined building.
- **Implementation model:** MO wall banner 1×2 (DankPyon_WallBanner1x2c) directly establishes the 2×1 rotating attachment precedent; MO wall oil lamp / rustic wall torch uses `Placeworker_AttachedToWall`, `building.isAttachment`, BuildingOnTop, wall draw offsets. The wall variant copies these engine settings but owns a new ThingDef.
- **Compatibility and limits:** only Japanization+MO PF profile is supported. The existing MO recipes and preservation outputs remain authoritative. Food Drying compatibility is not claimed. Roof/sun/rain on a wall attachment may reflect the wall cell rather than the eaves-facing outdoor cell; loaded-game verification is required. The original 2026-10-22 sprite set was explicitly REJECTED by the author because N/S/E/W appeared the same. Replacement art must rotate the projected pole axis: N/S horizontal, E/W foreshortened nearly vertical; each direction must be visibly distinct, and both 1×1 and 2×1 variants must exist. New assets are candidates, not author-approved or gameplay-tested.

**Decision:** direct independent food-drying gameplay is unnecessary; two variants of one MO-compatible wall-fixture family is the smallest differentiated feature. Scope stays in MO Japanization. No global PF patch or new bill/Job is authorized.
