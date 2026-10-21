using ProcessorFramework;
using UnityEngine;
using Verse;

namespace AncientMedievalJapan.MedievalOverhaulJapanization
{
    // Only MO drying racks receive this comp. PF continues to own the input,
    // output, process progress, ruin result, work jobs, and save/load state.
    public sealed class CompProperties_DryingRainDamage : CompProperties
    {
        public float fullRainDaysToRuin = 2f;

        public CompProperties_DryingRainDamage()
        {
            compClass = typeof(CompDryingRainDamage);
        }
    }

    public sealed class CompDryingRainDamage : ThingComp
    {
        public override void CompTickRare()
        {
            base.CompTickRare();

            Map map = parent.Map;
            if (map == null || map.weatherManager == null)
            {
                return;
            }

            // RimWorld's SnowRate can also raise RainRate; do not mistake snow
            // for liquid rain, which has its own PF speed penalty.
            if (map.weatherManager.SnowRate > 0f)
            {
                return;
            }

            CompProcessor processor = parent.GetComp<CompProcessor>();
            if (processor == null || processor.activeProcesses == null || processor.activeProcesses.Count == 0)
            {
                return;
            }

            float exposedFraction = Mathf.Clamp01(1f - processor.RoofCoverage);
            float rainRate = Mathf.Clamp01(map.weatherManager.RainRate);
            float daysToRuin = ((CompProperties_DryingRainDamage)props).fullRainDaysToRuin;
            if (exposedFraction <= 0f || rainRate <= 0f || daysToRuin <= 0f)
            {
                return;
            }

            float damage = (GenTicks.TickRareInterval / (GenDate.TicksPerDay * daysToRuin))
                * rainRate * exposedFraction;

            foreach (ActiveProcess process in processor.activeProcesses)
            {
                if (process == null || process.processDef == null || process.Ruined || process.Complete)
                {
                    continue;
                }

                // Saved Straw processes stay untouched even when an old save
                // still contains them after Japanization hid that recipe.
                string processName = process.processDef.defName;
                if (processName != "DankPyon_DriedMeatProcess"
                    && processName != "DankPyon_DriedMeatHumanProcess"
                    && processName != "DankPyon_DriedMeatInsectProcess"
                    && processName != "DankPyon_DriedFishProcess")
                {
                    continue;
                }

                // PF's existing ruinedPercent is saved and consumed by
                // WorkGiver_EmptyProcessor / TakeOutProduct on failure.
                process.ruinedPercent = Mathf.Min(1f, process.ruinedPercent + damage);
            }
        }
    }
}
