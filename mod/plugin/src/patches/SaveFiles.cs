using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Reflection.Emit;

using HarmonyLib;

namespace PoYArchipelago.Patches {
    /**
     * <summary>
     * Prevent CheckInitialProgressOnce from generating
     * random garbage stats.
     * </summary>
     */
    [HarmonyPatch(typeof(CheckStats), "CheckInitialProgressOnce")]
    static class DisableInitialGlobalStats {
        static bool Prefix() {
            ES3Settings settings = new ES3Settings("PoY_AP_global_stats.es3", ES3.Location.File);
            ES3.Save("receivedInitialScoreSetup", true, settings);
            return false;
        }
    }

    /**
     * <summary>
     * Always disable yfyd/fs modes.
     * </summary>
     */
    [HarmonyPatch(typeof(MenuSaveManager), "CheckModesUnlocked")]
    static class DisableOtherModes {
        static void Postfix(MenuSaveManager __instance) {
            __instance.yfydButton.SetActive(false);
            __instance.freesoloButton.SetActive(false);
        }
    }
}
