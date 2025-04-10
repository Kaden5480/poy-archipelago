using Mono.Cecil;
using Mono.Cecil.Cil;
using Mono.Collections.Generic;
using MonoMod.Utils;

namespace PoYArchipelagoPatcher.Patches {
    public static class NormalPaths {
        /**
         * <summary>
         * Patches occurrences of normal, yfyd, and fs related paths
         * to use a custom path instead.
         * </summary>
         * <param name="module">The module to patch</param>
         * <param name="typeName">The name of the type to patch</param>
         * <param name="methodName">The method to patch</param>
         */
        private static void PatchFilePaths(ModuleDefinition module, string typeName, string methodName) {
            MethodDefinition method = module.GetType(typeName).FindMethod(methodName);
            Logger.LogInfo($"Patching: {module}.{typeName}.{methodName}");

            Collection<Instruction> insts = method.Body.Instructions;

            foreach (Instruction inst in insts) {
                if (inst.OpCode.ToString().Equals("ldstr") == false) {
                    continue;
                }

                if (inst.Operand == null) {
                    continue;
                }

                string path = (string) inst.Operand;

                if (path.StartsWith("Mode_Normal/PeaksData_Normal")
                    || path.StartsWith("Mode_YouFallYouDie/PeaksData_YFYD")
                    || path.StartsWith("Mode_FreeSolo/PeaksData_FreeSolo")
                ) {
                    inst.Operand = $"PoY_AP_{path}";
                    Logger.LogDebug($"Replaced {path} with {inst.Operand}");
                }
            }
        }

        /**
         * <summary>
         * Patches occurrences of "global_stats.es3" to use a custom path instead.
         * </summary>
         * <param name="module">The module to patch</param>
         * <param name="typeName">The name of the type to patch</param>
         * <param name="methodName">The method to patch</param>
         */
        private static void PatchGlobalStats(ModuleDefinition module, string typeName, string methodName) {
            MethodDefinition method = module.GetType(typeName).FindMethod(methodName);
            Logger.LogInfo($"Patching: {module}.{typeName}.{methodName}");

            Collection<Instruction> insts = method.Body.Instructions;

            foreach (Instruction inst in insts) {
                if (inst.OpCode.ToString().Equals("ldstr") == false) {
                    continue;
                }

                if (inst.Operand == null) {
                    continue;
                }

                string path = (string) inst.Operand;

                if (path.Equals("global_stats.es3") == true) {
                    inst.Operand = $"PoY_AP_{path}";
                    Logger.LogDebug($"Replaced {path} with {inst.Operand}");
                }
            }
        }

        /**
         * <summary>
         * Applies patches for using custom save data paths.
         * </summary>
         * <param name="assembly">The assembly to patch</param>
         */
        public static void Patch(AssemblyDefinition assembly) {
            ModuleDefinition main = assembly.MainModule;

            // Patch normal save data paths
            PatchFilePaths(main, "BivouacSaveRopes",             "RemoveAllBivouacRopes");
            PatchFilePaths(main, "BivouacSaveRopes",             "LoadStoredropes");
            PatchFilePaths(main, "BivouacSaveRopes",             "SaveStoredRopes");
            PatchFilePaths(main, "CheckStats",                   "CheckLowestScoreGrades");
            PatchFilePaths(main, "CheckStats",                   "DropDownCheckStats");
            PatchFilePaths(main, "GameManager",                  "CreateBackup");
            PatchFilePaths(main, "GameManager",                  "Load");
            PatchFilePaths(main, "GameManager",                  "Save");
            PatchFilePaths(main, "MenuSaveManager",              "CheckAvianProgress");
            PatchFilePaths(main, "MenuSaveManager",              "CheckCanDelete");
            PatchFilePaths(main, "MenuSaveManager",              "CheckOldSaves");
            PatchFilePaths(main, "MenuSaveManager",              "DeleteSlot");
            PatchFilePaths(main, "MenuSaveManager",              "PlaySlot");
            PatchFilePaths(main, "MenuSaveManager",              "SaveNewGame");
            PatchFilePaths(main, "NPCEvents",                    "TimeAttackStoreDefaultArrays");
            PatchFilePaths(main, "RopeCabinDescription",         "SaveHarnessUse");
            PatchFilePaths(main, "TimeAttack",                   "LoadSTTime");
            PatchFilePaths(main, "TimeAttack",                   "SaveTimeAttack");
            PatchFilePaths(main, "TimeAttackSetter",             "LoadBest");
            PatchFilePaths(main, "TimeAttackSetter",             "SaveTimeAttack");
            PatchFilePaths(main, "TimeAttackTierAchievements",   "ScoreTimeAttackAchievement");

            // Patch global stats paths
            PatchGlobalStats(main, "CheckStats",                 "LoadIndividualPeakStats");
            PatchGlobalStats(main, "CheckStats",                 "ShowStats");
            PatchGlobalStats(main, "GameManager",                "LoadAllStats");
            PatchGlobalStats(main, "GameManager",                "LoadIndividualPeakStats");
            PatchGlobalStats(main, "GameManager",                "RemakeStats");
            PatchGlobalStats(main, "GameManager",                "SaveAllStats");
            PatchGlobalStats(main, "GameManager",                "SaveIndividualPeakStats");
            PatchGlobalStats(main, "GameManager",                "SaveTAAchievement");
            PatchGlobalStats(main, "GameManager",                "StatsCorruptionHandle");
            PatchGlobalStats(main, "TimeAttackTierAchievements", "ScoreTimeAttackAchievement");
        }
    }
}
