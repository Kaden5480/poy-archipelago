using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Reflection.Emit;

using HarmonyLib;

namespace PoYArchipelago.Patches {
    public static class FileInjects {
        [HarmonyPrefix]
        [HarmonyPatch(typeof(CheckStats), "CheckInitialProgressOnce")]
        static bool TADisableInitial() {
            ES3Settings settings = new ES3Settings("PoY_AP_global_stats.es3", ES3.Location.File);
            ES3.Save("receivedInitialScoreSetup", true, settings);
            return false;
        }
    }
}
