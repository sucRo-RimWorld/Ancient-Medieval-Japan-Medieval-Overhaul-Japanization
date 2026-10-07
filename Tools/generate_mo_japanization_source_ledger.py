#!/usr/bin/env python3
"""Generate a source-level Medieval Overhaul dependency ledger.

This reads an MO zip/extracted tree and emits derived XML metadata only.
It does not resolve RimWorld patches, inheritance, or runtime-loaded Defs.
"""
from __future__ import annotations

import argparse
import csv
import re
import zipfile
from collections import Counter, defaultdict
from pathlib import Path
import xml.etree.ElementTree as ET

TOKEN_RE = re.compile(r"\b[A-Za-z_][A-Za-z0-9_]*\b")
CATEGORIES = ("pawnkind", "research", "recipe", "generation", "optional_mod", "other")


def norm(path: str) -> str:
    return path.replace("\\", "/")


def _zip_root(names: list[str]) -> str:
    top = {n.split("/", 1)[0] for n in names if "/" in n}
    if len(top) == 1:
        return next(iter(top)) + "/"
    return ""


def load_files(source: str, version: str, optional: list[str]) -> dict[str, str]:
    prefixes = [f"{version}/Defs/", f"{version}/Patches/"]
    prefixes.extend(f"{version}/Mods/{folder.strip('/')}/" for folder in optional)
    files: dict[str, str] = {}
    src = Path(source)
    if src.is_file():
        with zipfile.ZipFile(src) as zf:
            names = zf.namelist()
            root = _zip_root(names)
            for name in names:
                rel = name[len(root):] if root and name.startswith(root) else name
                if not name.lower().endswith(".xml") or not any(rel.startswith(prefix) for prefix in prefixes):
                    continue
                data = zf.read(name)
                try:
                    text = data.decode("utf-8-sig")
                except UnicodeDecodeError:
                    text = data.decode("utf-8", "replace")
                files[norm(rel)] = text
    else:
        for prefix in prefixes:
            base = src / prefix
            if not base.exists():
                continue
            for path in base.rglob("*.xml"):
                rel = norm(str(path.relative_to(src)))
                files[rel] = path.read_text(encoding="utf-8-sig", errors="replace")
    return files


def values(elem: ET.Element, xpath: str) -> list[str]:
    return [node.text.strip() for node in elem.findall(xpath) if node.text and node.text.strip()]


def semis(items: list[str]) -> str:
    return ";".join(dict.fromkeys(item for item in items if item))


def category(path: str) -> str:
    lower = path.lower()
    if "pawnkind" in lower:
        return "pawnkind"
    if "research" in lower:
        return "research"
    if "recipe" in lower:
        return "recipe"
    if "structure" in lower or "symbol" in lower:
        return "generation"
    if "/mods/" in lower:
        return "optional_mod"
    return "other"


def is_layout_file(path: str) -> bool:
    return "/StructureLayoutDef/" in path


def extract_defs(files: dict[str, str], source_version: str):
    rows: list[dict[str, str]] = []
    declarations_by_cat: dict[str, Counter[str]] = {cat: Counter() for cat in CATEGORIES}
    layout_declarations: Counter[str] = Counter()
    parse_errors: list[str] = []

    for path, text in files.items():
        if "/Defs/" not in path:
            continue
        try:
            root = ET.fromstring(text)
        except ET.ParseError:
            parse_errors.append(path)
            continue
        cat = category(path)
        for elem in root:
            def_name = (elem.findtext("defName") or "").strip()
            xml_name = (elem.get("Name") or "").strip()
            ident = def_name or xml_name
            if not ident:
                continue
            ident_kind = "defName" if def_name else "Name"
            declarations_by_cat[cat][ident] += 1
            if is_layout_file(path):
                layout_declarations[ident] += 1

            research: list[str] = []
            rp = elem.find("./recipeMaker/researchPrerequisite")
            if rp is not None and rp.text and rp.text.strip():
                research.append(rp.text.strip())
            research += values(elem, "./recipeMaker/researchPrerequisites/li")
            research += values(elem, "./researchPrerequisites/li")
            process_defs = values(elem, ".//processes/li") + values(elem, ".//processDefs/li")

            rows.append({
                "source_version": source_version,
                "def_type": elem.tag,
                "identity_kind": ident_kind,
                "def_name": ident,
                "abstract": elem.get("Abstract", "False"),
                "parent_name": elem.get("ParentName", ""),
                "source_file": path,
                "label": (elem.findtext("label") or "").strip(),
                "research_prerequisites": semis(research),
                "tex_paths": semis(values(elem, ".//texPath")),
                "weapon_tags": semis(values(elem, "./weaponTags/li")),
                "apparel_tags": semis(values(elem, "./apparel/tags/li") + values(elem, "./apparelTags/li")),
                "apparel_required": semis(values(elem, "./apparelRequired/li")),
                "process_defs": semis(process_defs),
                "symbol_target_thing": (elem.findtext("thing") or "").strip() if elem.tag.endswith("SymbolDef") else "",
            })
    identities = {row["def_name"] for row in rows}
    return rows, identities, declarations_by_cat, layout_declarations, parse_errors


def count_references(files: dict[str, str], identities: set[str], declarations_by_cat, layout_declarations, symbol_to_thing):
    """Count exact identifier references, resolving KCSG layout symbols to ThingDefs."""
    raw_by_cat: dict[str, Counter[str]] = {cat: Counter() for cat in CATEGORIES}
    layout_direct: Counter[str] = Counter()
    layout_via_symbol: Counter[str] = Counter()
    unsupported = {ident for ident in identities if not TOKEN_RE.fullmatch(ident)}

    for path, text in files.items():
        tokens = TOKEN_RE.findall(text)
        if is_layout_file(path):
            for token in tokens:
                target = symbol_to_thing.get(token)
                if target:
                    layout_via_symbol[target] += 1
                elif token in identities:
                    layout_direct[token] += 1
            continue
        cat = category(path)
        raw_by_cat[cat].update(token for token in tokens if token in identities)

    direct_counts: dict[str, tuple[int, dict[str, int]]] = {}
    for ident in identities:
        per: dict[str, int] = {}
        for cat in CATEGORIES:
            declared = declarations_by_cat[cat].get(ident, 0)
            if cat == "generation":
                declared -= layout_declarations.get(ident, 0)
            per[cat] = max(0, raw_by_cat[cat].get(ident, 0) - declared)
        direct_layout_refs = max(0, layout_direct.get(ident, 0) - layout_declarations.get(ident, 0))
        per["generation"] += direct_layout_refs
        direct_counts[ident] = (sum(per.values()), per)

    return direct_counts, layout_via_symbol, unsupported

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="MO zip archive or extracted MO root")
    parser.add_argument("--version", default="1.6", help="RimWorld version folder to scan (default: 1.6)")
    parser.add_argument("--source-version-label", default=None, help="label written to source_version, e.g. 1.6.2.2")
    parser.add_argument("--include-optional", action="append", default=[], metavar="FOLDER",
                        help="also scan VERSION/Mods/FOLDER (repeatable); baseline omits optional integrations")
    parser.add_argument("-o", "--output", required=True, help="output CSV path")
    args = parser.parse_args()
    files = load_files(args.source, args.version, args.include_optional)
    if not files:
        raise SystemExit("no matching XML files found")
    source_label = args.source_version_label or args.version
    rows, identities, decl_by_cat, layout_declarations, parse_errors = extract_defs(files, source_label)
    symbol_to_thing = {
        row["def_name"]: row["symbol_target_thing"]
        for row in rows
        if row.get("symbol_target_thing") and row["symbol_target_thing"] in identities
    }
    counts, layout_via_symbol, unsupported = count_references(
        files, identities, decl_by_cat, layout_declarations, symbol_to_thing
    )

    fields = [
        "source_version", "def_type", "identity_kind", "def_name", "abstract", "parent_name",
        "source_file", "label", "research_prerequisites", "tex_paths", "weapon_tags", "apparel_tags",
        "apparel_required", "process_defs", "symbol_target_thing",
        "ref_direct_total", "ref_via_symbol_total", "ref_total",
        "ref_pawnkind", "ref_research", "ref_recipe",
        "ref_generation_direct", "ref_generation_via_symbol", "ref_generation",
        "ref_optional_mod", "ref_other",
    ]
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for row in sorted(rows, key=lambda item: (item["def_type"], item["def_name"], item["source_file"])):
            direct_total, per = counts.get(row["def_name"], (0, {}))
            via_generation = layout_via_symbol.get(row["def_name"], 0) if row["def_type"] == "ThingDef" else 0
            row.update({
                "ref_direct_total": direct_total,
                "ref_via_symbol_total": via_generation,
                "ref_total": direct_total + via_generation,
                "ref_pawnkind": per.get("pawnkind", 0),
                "ref_research": per.get("research", 0),
                "ref_recipe": per.get("recipe", 0),
                "ref_generation_direct": per.get("generation", 0),
                "ref_generation_via_symbol": via_generation,
                "ref_generation": per.get("generation", 0) + via_generation,
                "ref_optional_mod": per.get("optional_mod", 0),
                "ref_other": per.get("other", 0),
            })
            writer.writerow(row)
    print(f"files={len(files)} defs={len(rows)} identities={len(identities)} "
          f"parse_errors={len(parse_errors)} unsupported_identities={len(unsupported)} output={out}")
    if parse_errors:
        print("parse_error_files=" + ";".join(parse_errors))
    if unsupported:
        print("unsupported_identity_tokens=" + ";".join(sorted(unsupported)))


if __name__ == "__main__":
    main()
