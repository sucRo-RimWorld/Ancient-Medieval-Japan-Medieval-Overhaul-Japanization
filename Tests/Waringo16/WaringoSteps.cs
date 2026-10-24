using System;
using System.Linq;
using System.Reflection;
using System.Threading.Tasks;
using RimWorks.Pickle;
using RimWorld;
using Verse;

namespace AMJ.MOJ.WaringoNative16 {
    internal static class OnGameThread {
        public static Task Invoke(Action action) {
            var completion = new TaskCompletionSource<bool>();
            var driver = typeof(PickleContext).Assembly.GetType("RimWorks.Pickle.Runtime.PickleDriver", true);
            var post = driver.GetMethod("Post", new[] { typeof(Action) });
            if (post == null) throw new MissingMethodException(driver.FullName, "Post(Action)");
            post.Invoke(null, new object[] { (Action)delegate {
                try { action(); completion.SetResult(true); }
                catch (Exception e) { completion.SetException(e); }
            } });
            return completion.Task;
        }
    }

    [PickleSteps]
    public sealed class WaringoSteps {
        [Then("the loaded Japanese waringo and fruit-tree research match the approved source")]
        public async Task Check(PickleContext ctx) {
            await ctx.WaitFrames(2);
            await OnGameThread.Invoke(delegate {
                ctx.Require(Find.CurrentMap != null, "Real Quickstart map missing");
                string[] ids = {
                    "dankpyon.medieval.overhaul", "sucro.ancientmedievaljapan.environment",
                    "sucro.ancientmedievaljapan.core", "sucro.ancientmedievaljapan.scenarios",
                    "sucro.ancientmedievaljapan.waterworks", "sucro.ancientmedievaljapan.ironmaking",
                    "sucro.ancientmedievaljapan.medievaloverhauljapanization"
                };
                var actual = LoadedModManager.RunningModsListForReading
                    .Select(x => x.PackageId.ToLowerInvariant()).ToArray();
                foreach (string pid in ids)
                    ctx.Require(actual.Contains(pid), "Missing real required Mod: " + pid);
                var apple = DefDatabase<ThingDef>.GetNamedSilentFail("DankPyon_Tree_Apple");
                var fruit = DefDatabase<ThingDef>.GetNamedSilentFail("DankPyon_RawApples");
                var mulberry = DefDatabase<ThingDef>.GetNamedSilentFail("DankPyon_Tree_Mulberry");
                var silk = DefDatabase<ThingDef>.GetNamedSilentFail("DankPyon_Silkworm");
                var cocoa = DefDatabase<ResearchProjectDef>.GetNamedSilentFail("Cocoa");
                ctx.Require(apple != null && apple.plant != null && fruit != null &&
                            mulberry != null && mulberry.plant != null && silk != null &&
                            cocoa != null, "Missing original MO / research Def");
                ctx.Require(apple.label == "和リンゴの木" &&
                            fruit.label == "和リンゴ" &&
                            apple.description.Contains("小ぶり") &&
                            fruit.description.Contains("酸味"),
                            "Loaded Japanese waringo names and descriptions do not match");
                ctx.Require(cocoa.label == "果樹栽培" &&
                            cocoa.description.Contains("養蚕"),
                            "Loaded Japanese fruit research is not the approved display");
                ctx.Require(apple.plant.sowResearchPrerequisites != null &&
                            apple.plant.sowResearchPrerequisites.Contains(cocoa) &&
                            mulberry.plant.sowResearchPrerequisites != null &&
                            mulberry.plant.sowResearchPrerequisites.Contains(cocoa),
                            "Apple/Mulberry fruit-tree unlock is disconnected");
                ctx.Require(Math.Abs(apple.plant.growDays - 33f) < .01f &&
                            Math.Abs(apple.plant.harvestYield - 20f) < .01f &&
                            Math.Abs(apple.plant.harvestAfterGrowth - .30f) < .01f &&
                            apple.plant.harvestedThingDef == fruit,
                            "AMJ preserved apple harvest inputs differ");
                // This exercises the loaded game's real Plant logic, not a simulated
                // calendar, a pawn harvesting Job, or a historical growth balance.
                var map = Find.CurrentMap;
                IntVec3 cell = map.Center;
                foreach (IntVec3 pos in GenRadial.RadialCellsAround(cell, 2f, true)) {
                    if (!pos.InBounds(map)) continue;
                    foreach (Thing thing in pos.GetThingList(map).ToArray())
                        if (!(thing is Pawn)) thing.Destroy(DestroyMode.Vanish);
                    map.terrainGrid.SetTerrain(pos, TerrainDefOf.Soil);
                }
                var plant = ThingMaker.MakeThing(apple) as Plant;
                ctx.Require(plant != null, "Real apple Plant cannot be made");
                GenSpawn.Spawn(plant, cell, map, WipeMode.Vanish);
                plant.HitPoints = plant.MaxHitPoints;
                plant.Growth = .66f;
                ctx.Require(plant.HarvestableNow, "Apple not harvestable past 0.65");
                int early = plant.YieldNow();
                ctx.Require(early >= 9 && early <= 11,
                            "Unexpected early loaded Apple YieldNow=" + early);
                plant.PlantCollected(null, PlantDestructionMode.Cut);
                ctx.Require(!plant.Destroyed && Math.Abs(plant.Growth - .30f) < .001f &&
                            !plant.HarvestableNow,
                            "Original apple tree did not survive and reset after harvest");
                plant.Growth = 1f;
                int full = plant.YieldNow();
                ctx.Require(full >= 19 && full <= 20, "Apple full harvest mismatch=" + full);
                plant.Destroy(DestroyMode.Vanish);
                Log.Message("AMJ_MOJ_WARINGO16_OK early=" + early + " full=" + full +
                            " japanese=1 requiredMods=" + ids.Length);
            });
        }
    }
}
