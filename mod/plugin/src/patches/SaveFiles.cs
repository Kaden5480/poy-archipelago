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

    /**
     * <summary>
     * Prevent new instances of GameManager from being destroyed.
     * </summary>
     */
    [HarmonyPatch(typeof(GameManager), "Awake")]
    static class GameManagerAwake {
        static bool Prefix() {
            return GameManager.control == null;
        }
    }

    /**
     * <summary>
     * Allows loading different files depending
     * on the instance of GameManager being operated on.
     * </summary>
     */
    [HarmonyPatch(typeof(GameManager), "Load")]
    static class GameManagerLoad {
        static string GetFilePath(GameManager instance, string filePath) {
            Console.WriteLine("Checking inject");

            if (instance == GameManager.control) {
                Console.WriteLine($"Injecting normal GameManager path: {filePath}");
            }
            return filePath;
        }

        static IEnumerable<CodeInstruction> Transpiler(
            IEnumerable<CodeInstruction> insts
        ) {
            MethodInfo concat = AccessTools.Method(
                typeof(string), "Concat", new Type[] { typeof(string), typeof(string) }
            );
            MethodInfo inject = AccessTools.Method(
                typeof(GameManagerLoad), nameof(GameManagerLoad.GetFilePath)
            );

            return Helper.Replace(
                insts,
                new[] {
                    new CodeInstruction(OpCodes.Ldloc_0),
                    new CodeInstruction(OpCodes.Ldloc_1),
                    new CodeInstruction(OpCodes.Call, concat),
                    new CodeInstruction(OpCodes.Stloc_2),
                },
                new[] {
                    new CodeInstruction(OpCodes.Ldloc_0),
                    new CodeInstruction(OpCodes.Ldloc_1),
                    new CodeInstruction(OpCodes.Call, concat),
                    new CodeInstruction(OpCodes.Stloc_2),
                    new CodeInstruction(OpCodes.Ldarg_0),
                    new CodeInstruction(OpCodes.Ldloc_2),
                    new CodeInstruction(OpCodes.Call, inject),
                    new CodeInstruction(OpCodes.Stloc_2),
                }
            );
        }
    }
}
