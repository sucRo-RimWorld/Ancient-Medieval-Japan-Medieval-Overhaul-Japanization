"""Static contract for full AMJ prerequisite metadata and MO drying-rack surgery.

This test is not a substitute for loaded ProcessorFramework or native game tests.
"""
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
ABOUT = ROOT / "About" / "About.xml"
PATCH = ROOT / "Patches" / "Production" / "DisableHayToStraw.xml"
REQUIRED = {
    "DankPyon.Medieval.Overhaul",
    "sucro.ancientmedievaljapan.environment",
    "sucro.ancientmedievaljapan.core",
    "sucro.ancientmedievaljapan.scenarios",
    "sucro.ancientmedievaljapan.waterworks",
    "sucro.ancientmedievaljapan.ironmaking",
}
RACKS = {"DankPyon_DryingRack_Small", "DankPyon_DryingRack_Big"}
EXPECTED_SUFFIX = (
    '/comps/li[@Class="ProcessorFramework.CompProperties_Processor"]'
    '/processes/li[text()="DankPyon_StrawProcess"]'
)


class FullSuiteAndStrawContract(unittest.TestCase):
    def test_required_current_amj_modules(self):
        root = ET.parse(ABOUT).getroot()
        dependencies = [
            x.text for x in root.findall("./modDependencies/li/packageId")
        ]
        self.assertEqual(len(dependencies), len(set(dependencies)))
        self.assertEqual(set(dependencies), REQUIRED)
        order = {x.text for x in root.findall("./loadAfter/li")}
        self.assertTrue(REQUIRED.issubset(order))
        description = root.findtext("description", default="")
        self.assertIn("MO-only", description)
        self.assertIn("全体", description)

    def test_only_mo_drying_rack_straw_menu_is_removed(self):
        root = ET.parse(PATCH).getroot()
        ops = root.findall("Operation")
        self.assertEqual(len(ops), 2)
        for op in ops:
            self.assertEqual(op.get("Class"), "PatchOperationConditional")
            target = op.findtext("xpath")
            self.assertIsNotNone(target)
            rack = target.split('defName="', 1)[1].split('"', 1)[0]
            self.assertIn(rack, RACKS)
            self.assertEqual(target, f'/Defs/ThingDef[defName="{rack}"]' + EXPECTED_SUFFIX)
            match = op.find("match")
            self.assertEqual(match.get("Class"), "PatchOperationRemove")
            self.assertEqual(match.findtext("xpath"), target)
        self.assertEqual(
            {op.findtext("xpath").split('defName="')[1].split('"')[0] for op in ops},
            RACKS,
        )
        xml = PATCH.read_text(encoding="utf-8")
        self.assertNotIn("PatchOperationRemove\">\n      <xpath>/Defs/ProcessorFramework.ProcessDef", xml)
        self.assertNotIn("Haygrass", xml)


    def test_no_duplicate_crop_balance_or_retired_dependency(self):
        self.assertFalse((ROOT / "Patches/Cultivation/MOLentilSowingSkill.xml").exists())
        self.assertNotIn("sucro.ancientmedievaljapan.cropgrowthbalance",
                         ABOUT.read_text(encoding="utf-8"))
        for path in (ROOT / "Patches").rglob("*.xml"):
            self.assertNotIn("DankPyon_Plant_Lentils", path.read_text(encoding="utf-8"))



if __name__ == "__main__":
    unittest.main()
