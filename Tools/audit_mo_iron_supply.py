#!/usr/bin/env python3
"""Static MO/Vanilla iron-supply XML inventory (not a RimWorld loaded-Def test).

Usage:
  python Tools/audit_mo_iron_supply.py /path/to/3219596926.zip --output audit.json
  python Tools/audit_mo_iron_supply.py /path/to/MO --vanilla-core /path/to/RimWorld/Data/Core --output audit.json
  python Tools/audit_mo_iron_supply.py /path/to/MO.zip --include-optional Mines --output audit.json

Does not execute RimWorld PatchOperations, calculate final trade inventories,
compute deep-resource eligibility, or claim runtime compatibility.
"""
from __future__ import annotations

import argparse
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile

IRON_ITEMS = ("DankPyon_IronOre", "DankPyon_IronIngot", "Steel")
MO_INTEREST = ("DankPyon_IronOre", "DankPyon_IronIngot")
TOGGLE_FILES = (
    "MOSetting_MetalChain.xml", "MOSetting_VanillaMineables.xml", "MOSetting_WoodChain.xml"
)


def _text(node: ET.Element, path: str) -> str:
    return (node.findtext(path) or "").strip()


def _source_xml(source: Path, version: str = "1.6", vanilla: bool = False,
                optional: tuple[str, ...] = ()) -> dict[str, str]:
    """Load XML without extracting the archive; return normalized logical paths."""
    out: dict[str, str] = {}
    if source.is_file():
        with ZipFile(source) as zf:
            for fname in zf.namelist():
                if not fname.lower().endswith(".xml"):
                    continue
                rel = fname.replace("\\", "/")
                if not vanilla:
                    prefix = f"{version}/"
                    pos = rel.find(prefix)
                    if pos < 0:
                        continue
                    rel = rel[pos:]
                    prefixes = (f"{version}/Defs/", f"{version}/Patches/") + tuple(
                        f"{version}/Mods/{folder}/" for folder in optional
                    )
                    if not rel.startswith(prefixes):
                        continue
                if vanilla and "/Defs/" not in "/" + rel:
                    continue
                out[rel] = zf.read(fname).decode("utf-8-sig")
    elif source.is_dir():
        root = source
        if not vanilla:
            root = root / version
            if not root.is_dir():
                raise ValueError(f"MO version directory missing: {root}")
        else:
            if (root / "Data" / "Core" / "Defs").is_dir():
                root = root / "Data" / "Core"
            elif (root / "Core" / "Defs").is_dir():
                root = root / "Core"
        if not root.exists():
            raise ValueError(f"source directory missing: {root}")
        for p in sorted(root.rglob("*.xml")):
            if vanilla and "Defs" not in p.parts:
                continue
            if not vanilla and not (
                p.relative_to(root).parts[0] in ("Defs", "Patches")
                or (len(p.relative_to(root).parts) > 2 and
                    p.relative_to(root).parts[:2] in [("Mods", name) for name in optional])
            ):
                continue
            rel = p.relative_to(root).as_posix()
            if not vanilla:
                rel = f"{version}/{rel}"
            out[rel] = p.read_text(encoding="utf-8-sig")
    else:
        raise FileNotFoundError(source)
    return out


def _collect_roots(files: dict[str, str]) -> tuple[dict[str, ET.Element], list[str]]:
    roots = {}
    errors = []
    for p, s in files.items():
        try:
            roots[p] = ET.fromstring(s)
        except ET.ParseError as e:
            errors.append(f"{p}: {e}")
    return roots, errors


def _resource_records(roots: dict[str, ET.Element]) -> list[dict]:
    records = []
    for file, root in roots.items():
        if "/Defs/" not in file:
            continue
        for thing in root.findall("ThingDef"):
            name = _text(thing, "defName")
            if name not in IRON_ITEMS:
                continue
            records.append({
                "thing": name, "source": file, "parent_xml": thing.get("ParentName", ""),
                "categories": [_text(x, ".") for x in thing.findall("thingCategories/li")],
                "trade_tags": [_text(x, ".") for x in thing.findall("tradeTags/li")],
                "market_value": _text(thing, "statBases/MarketValue") or None,
                "deep_commonality": _text(thing, "deepCommonality") or None,
                "deep_count_per_portion": _text(thing, "deepCountPerPortion") or None,
                "deep_lump_size_range": _text(thing, "deepLumpSizeRange") or None,
                "butcher_products": {n.tag: (n.text or "").strip()
                                     for n in thing.findall("butcherProducts/*")},
                "abstract": thing.get("Abstract", "False") == "True",
            })
    return records


def _categories(roots: dict[str, ET.Element]) -> dict[str, dict]:
    result = {}
    for file, root in roots.items():
        for cat in root.findall("ThingCategoryDef"):
            name = _text(cat, "defName")
            if name:
                result[name] = {"parent": _text(cat, "parent") or None, "source": file}
    return result


def _ancestors(category: str, mapping: dict[str, dict]) -> list[str]:
    chain, seen = [], set()
    curr = category
    while curr and curr not in seen:
        chain.append(curr)
        seen.add(curr)
        curr = mapping.get(curr, {}).get("parent")
    return chain


def _traders(roots: dict[str, ET.Element], category_map: dict[str, dict], resources: list[dict], origin: str) -> list[dict]:
    result = []
    cat_to_items: dict[str, set[str]] = {}
    for rec in resources:
        for cat in rec["categories"]:
            for anc in _ancestors(cat, category_map):
                cat_to_items.setdefault(anc, set()).add(rec["thing"])
    for file, root in roots.items():
        if "TraderKind" not in file:
            continue
        for trader in root.findall("TraderKindDef"):
            name = _text(trader, "defName") or trader.get("Name", "")
            if not name:
                continue
            for index, g in enumerate(trader.findall("stockGenerators/li")):
                clazz = g.get("Class", "")
                direct = _text(g, "thingDef")
                cat = _text(g, "categoryDef")
                tag = _text(g, "tag") or _text(g, "tradeTag")
                is_buyer = clazz.startswith("StockGenerator_Buy")
                related = direct in (*IRON_ITEMS, "DankPyon_Coal") or cat in cat_to_items or "Ore" in tag or "Metal" in tag
                # Retain other generators only when their explicitly listed def is a relevant resource.
                if not related:
                    continue
                result.append({
                    "origin": origin, "trader": name, "source": file, "generator_index": index,
                    "class": clazz, "direction": "buy" if is_buyer else "sell_or_stock",
                    "thing_def": direct or None, "category": cat or None, "trade_tag": tag or None,
                    "potential_iron_items_from_category": sorted(cat_to_items.get(cat, [])) if cat else [],
                    "count_range": _text(g, "countRange") or None,
                    "thing_def_count_range": _text(g, "thingDefCountRange") or None,
                    "total_price_range": _text(g, "totalPriceRange") or None,
                })
    return result


def _toggle_patches(roots: dict[str, ET.Element]) -> list[dict]:
    result = []
    for file, root in roots.items():
        if not any(file.endswith("/" + target) for target in TOGGLE_FILES):
            continue
        for setting in root.findall(".//settings/li"):
            if not setting.text:
                continue
            toggle = setting.text.strip()
            for branch in ("active", "inactive"):
                # Only direct toggle operation branches, not arbitrary nested elements.
                parent = next((x for x in root.iter() if setting in list(x.findall("settings/li"))), None)
                if parent is None:
                    continue
                bnode = parent.find(branch)
                if bnode is None:
                    continue
                for operation in bnode.iter():
                    xpath = _text(operation, "xpath")
                    if not xpath or not any(t in xpath for t in (
                        "MineableSteel", "DankPyon_MineableIron", "DankPyon_MakeOre_IronOre",
                        "Caravan_Neolithic_BulkGoods", "Caravan_Outlander_BulkGoods",
                        "Visitor_Neolithic_Standard", "Visitor_Outlander_Standard", "PreciousLump"
                    )):
                        continue
                    result.append({
                        "toggle": toggle, "branch": branch, "source": file,
                        "operation_class": operation.get("Class", ""), "xpath": xpath,
                        "values": {e.tag: (e.text or "").strip() for e in operation.findall("./value/*")},
                    })
    return result


def audit(mo: Path, vanilla_core: Path | None = None,
          optional_folders: tuple[str, ...] = ()) -> dict:
    for name in optional_folders:
        if not name or name in (".", "..") or any(sep in name for sep in ("/", "\\")):
            raise ValueError(f"Invalid optional folder: {name!r}")
    mo_files = _source_xml(mo, optional=optional_folders)
    mo_roots, errors = _collect_roots(mo_files)
    if not mo_roots:
        raise ValueError("No readable MO 1.6 XML")
    mo_resources = _resource_records(mo_roots)
    cats = _categories(mo_roots)
    vanilla_roots = {}
    vanilla_resources: list[dict] = []
    if vanilla_core:
        vanilla_files = _source_xml(vanilla_core, vanilla=True)
        vanilla_roots, parse_errors = _collect_roots(vanilla_files)
        errors.extend(parse_errors)
        vanilla_resources = _resource_records(vanilla_roots)
        cats.update(_categories(vanilla_roots))
    all_resources = mo_resources + vanilla_resources
    all_traders = _traders(mo_roots, cats, all_resources, "MO")
    if vanilla_roots:
        all_traders += _traders(vanilla_roots, cats, all_resources, "Vanilla Core (static)")
    risks = []
    mo_items = {row["thing"]: row for row in mo_resources if not row["abstract"]}
    for thing in MO_INTEREST:
        rec = mo_items.get(thing)
        if rec and rec.get("deep_commonality") not in (None, "", "0"):
            risks.append({"kind": "deep_resource_candidate", "thing": thing,
                          "detail": "Def has deepCommonality; eligibility and extraction not verified in game"})
    if any(t["thing_def"] == "DankPyon_IronIngot" and t["direction"] != "buy" for t in all_traders):
        risks.append({"kind": "explicit_ingot_stock", "detail": "MO sells ingots directly"})
    if any(t["category"] == "ResourcesRaw" and "DankPyon_IronIngot" in t["potential_iron_items_from_category"] for t in all_traders):
        risks.append({"kind": "broad_category_stock", "detail": "Raw resource trader may generate iron; loaded choice unverified"})
    return {
        "scope": "MO 1.6 source XML; optional Vanilla Core source XML; patches NOT applied; no runtime simulation",
        "optional_folders": list(optional_folders),
        "vanilla_core_supplied": bool(vanilla_core), "files_parsed": len(mo_roots) + len(vanilla_roots),
        "parse_errors": errors, "mo_resources": mo_resources,
        "vanilla_resources": vanilla_resources,
        "categories": {x: cats.get(x, {}) for x in ("ResourcesRaw", "DankPyon_RawOres")},
        "traders": all_traders, "toggle_operations": _toggle_patches(mo_roots),
        "risks": risks,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("mo", type=Path, help="Medieval Overhaul archive ZIP or extracted Mod directory")
    ap.add_argument("--vanilla-core", type=Path, help="RimWorld Data/Core (or RimWorld root) for additional static Vanilla trader XML")
    ap.add_argument("--include-optional", action="append", default=[], metavar="FOLDER",
                    help="MO 1.6/Mods folder to include only when its dependency is active; repeat as needed")
    ap.add_argument("--output", type=Path, required=True, help="Output JSON path")
    args = ap.parse_args()
    record = audit(args.mo, args.vanilla_core, tuple(args.include_optional))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[OK] parsed={record['files_parsed']} MO_trader_rows={sum(t['origin']=='MO' for t in record['traders'])} "
          f"vanilla_supplied={record['vanilla_core_supplied']} risks={len(record['risks'])} "
          f"parse_errors={len(record['parse_errors'])}")
    for risk in record["risks"]:
        print(f"[AUDIT] {risk['kind']}: {risk.get('thing', risk['detail'])}")
    if record["parse_errors"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())