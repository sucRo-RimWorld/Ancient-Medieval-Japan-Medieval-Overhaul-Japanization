"""Static contract for the legacy Japanization provider and moved straw ownership.

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

    def test_no_duplicate_migrated_straw_override_in_legacy_mod(self):
        # Agriculture now owns the MO-conditional StrawProcess removal.
        # This protects against accidental duplicate reintroduction here.
        self.assertFalse(PATCH.exists())

    def test_no_duplicate_crop_balance_or_retired_dependency(self):
        self.assertFalse((ROOT / "Patches/Cultivation/MOLentilSowingSkill.xml").exists())
        self.assertNotIn("sucro.ancientmedievaljapan.cropgrowthbalance",
                         ABOUT.read_text(encoding="utf-8"))
        for path in (ROOT / "Patches").rglob("*.xml"):
            self.assertNotIn("DankPyon_Plant_Lentils", path.read_text(encoding="utf-8"))



if __name__ == "__main__":
    unittest.main()
