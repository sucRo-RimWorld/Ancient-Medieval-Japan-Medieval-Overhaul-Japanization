#!/usr/bin/env python3
"""Offline fixture checks for static iron-supply auditing (unittest only)."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "Tools"))
from audit_mo_iron_supply import audit

RESOURCE = '''<Defs>
<ThingDef><defName>DankPyon_IronOre</defName><thingCategories><li>DankPyon_RawOres</li></thingCategories><deepCommonality>5</deepCommonality><deepCountPerPortion>45</deepCountPerPortion><butcherProducts><DankPyon_IronIngot>1</DankPyon_IronIngot></butcherProducts></ThingDef>
<ThingDef><defName>DankPyon_IronIngot</defName><thingCategories><li>ResourcesRaw</li></thingCategories><deepCommonality>5</deepCommonality></ThingDef>
</Defs>'''
CATEGORY = '''<Defs><ThingCategoryDef><defName>DankPyon_RawOres</defName><parent>ResourcesRaw</parent></ThingCategoryDef></Defs>'''
TRADER = '''<Defs><TraderKindDef><defName>MO_Example</defName><stockGenerators>
<li Class="StockGenerator_SingleDef"><thingDef>DankPyon_IronIngot</thingDef><countRange>500~800</countRange></li>
<li Class="StockGenerator_Category"><categoryDef>ResourcesRaw</categoryDef><thingDefCountRange>2~4</thingDefCountRange></li>
<li Class="StockGenerator_BuyTradeTag"><tag>DankPyon_RawOres</tag></li>
<li Class="StockGenerator_BuySingleDef"><thingDef>DankPyon_Coal</thingDef></li>
</stockGenerators></TraderKindDef></Defs>'''
VANILLA = '''<Defs><TraderKindDef><defName>Base_Neolithic_Standard</defName><stockGenerators>
<li Class="StockGenerator_SingleDef"><thingDef>Steel</thingDef><countRange>10~20</countRange></li>
</stockGenerators></TraderKindDef></Defs>'''


class AuditTests(unittest.TestCase):
    def make_mo(self, path: Path) -> None:
        with ZipFile(path, "w") as z:
            z.writestr("MO/1.6/Defs/ThingDefs_Items/Items_Resources.xml", RESOURCE)
            z.writestr("MO/1.6/Defs/ThingCategoryDefs/ThingCategories.xml", CATEGORY)
            z.writestr("MO/1.6/Defs/TraderKindDefs/TraderKinds_Base_Medieval.xml", TRADER)
            z.writestr("MO/1.6/Mods/Mines/Patches/Recipes_Mining.xml", "<Patch />")

    def test_mo_zip_inventory_with_buy_sell_split(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            zip_path = Path(td) / "MO.zip"
            self.make_mo(zip_path)
            d = audit(zip_path)
            self.assertEqual(d["parse_errors"], [])
            self.assertFalse(d["vanilla_core_supplied"])
            self.assertEqual({x["thing"] for x in d["mo_resources"]},
                             {"DankPyon_IronOre", "DankPyon_IronIngot"})
            by_class = {x["class"]: x for x in d["traders"]}
            self.assertEqual(by_class["StockGenerator_SingleDef"]["count_range"], "500~800")
            self.assertEqual(by_class["StockGenerator_BuyTradeTag"]["direction"], "buy")
            self.assertEqual(by_class["StockGenerator_BuySingleDef"]["direction"], "buy")
            self.assertEqual(by_class["StockGenerator_BuyTradeTag"]["trade_tag"], "DankPyon_RawOres")
            self.assertEqual(set(by_class["StockGenerator_Category"]["potential_iron_items_from_category"]),
                             {"DankPyon_IronOre", "DankPyon_IronIngot"})
            self.assertEqual({x["thing"] for x in d["risks"] if x["kind"] == "deep_resource_candidate"},
                             {"DankPyon_IronOre", "DankPyon_IronIngot"})

    def test_optional_mod_xml_only_when_explicit(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            mo = Path(td) / "MO.zip"
            self.make_mo(mo)
            baseline = audit(mo)
            with_mines = audit(mo, optional_folders=("Mines",))
            self.assertEqual(baseline["files_parsed"], 3)
            self.assertEqual(with_mines["files_parsed"], 4)
            self.assertEqual(with_mines["optional_folders"], ["Mines"])
            ore = next(x for x in baseline["mo_resources"] if x["thing"] == "DankPyon_IronOre")
            self.assertEqual(ore["butcher_products"], {"DankPyon_IronIngot": "1"})
            with self.assertRaises(ValueError):
                audit(mo, optional_folders=("../Mods",))

    def test_optional_vanilla_core_is_static_and_separate(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            mo = root / "MO.zip"
            self.make_mo(mo)
            path = root / "RimWorld" / "Data" / "Core" / "Defs" / "TraderKindDefs"
            path.mkdir(parents=True)
            (path / "TraderKinds.xml").write_text(VANILLA, encoding="utf-8")
            d = audit(mo, root / "RimWorld")
            self.assertTrue(d["vanilla_core_supplied"])
            vanilla_traders = [x for x in d["traders"] if x["origin"].startswith("Vanilla")]
            self.assertEqual(len(vanilla_traders), 1)
            self.assertEqual(vanilla_traders[0]["thing_def"], "Steel")
            self.assertEqual(vanilla_traders[0]["count_range"], "10~20")
            self.assertEqual(d["parse_errors"], [])

    def test_unparseable_xml_is_reported_without_being_inferred_as_valid(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            mo = Path(td) / "MO.zip"
            with ZipFile(mo, "w") as z:
                z.writestr("1.6/Defs/ThingDefs_Items/broken.xml", "<Defs><ThingDef>")
                z.writestr("1.6/Defs/TraderKindDefs/traders.xml", TRADER)
            d = audit(mo)
            self.assertEqual(len(d["parse_errors"]), 1)


if __name__ == "__main__":
    unittest.main()