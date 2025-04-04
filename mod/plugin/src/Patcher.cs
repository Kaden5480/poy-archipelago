using HarmonyLib;
using PoYArchipelago.Patches;

namespace PoYArchipelago {
    public class Patcher {
        public Patcher() {
            PatchEarly();
        }

        /**
         * <summary>
         * Applies early patches.
         * </summary>
         */
        public void PatchEarly() {
            Harmony.CreateAndPatchAll(typeof(Patches.DisableInitialGlobalStats));
            Harmony.CreateAndPatchAll(typeof(Patches.DisableOtherModes));
            Harmony.CreateAndPatchAll(typeof(Patches.GameManagerAwake));
            Harmony.CreateAndPatchAll(typeof(Patches.GameManagerLoad));
        }
    }
}
