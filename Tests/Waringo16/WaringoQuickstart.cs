using RimWorks.Quickstarts;
using RimWorld;
using Verse;

namespace AMJ.MOJ.WaringoNative16 {
    public sealed class WaringoQuickstart : AbstractQuickstart {
        public override TaggedString description {
            get { return "Full AMJ 1.6 source-loaded waringo research and fruit check."; }
        }
        public override int mapSize { get { return 50; } }
        public override string seed { get { return "AMJ-MOJ-WARINGO-16"; } }
    }
}
