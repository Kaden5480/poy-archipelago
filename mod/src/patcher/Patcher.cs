using System;
using System.Collections.Generic;

using Mono.Cecil;
using Mono.Cecil.Cil;
using Mono.Collections.Generic;
using MonoMod.Utils;

namespace PoYArchipelagoPatcher {
    public static class Patcher {
        /**
         * <summary>
         * The DLLs this patcher targets.
         * </summary>
         */
        public static IEnumerable<string> TargetDLLs { get; } = new string[] {
            "Assembly-CSharp.dll",
        };

        private static ModuleDefinition main;

        public static void PatchFilePaths(string typeName, string methodName) {
            MethodDefinition method = main.GetType(typeName).FindMethod(methodName);
            Console.WriteLine($"Patching: {main}.{typeName}.{methodName}");

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
                    Console.WriteLine($"Replaced {path} with {inst.Operand}");
                }
            }
        }

        public static void PatchGlobalStats(string typeName, string methodName) {
            MethodDefinition method = main.GetType(typeName).FindMethod(methodName);
            Console.WriteLine($"Patching: {main}.{typeName}.{methodName}");

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
                    Console.WriteLine($"Replaced {path} with {inst.Operand}");
                }
            }
        }

        public static void Patch(AssemblyDefinition assembly) {
            main = assembly.MainModule;

            PatchFilePaths("BivouacSaveRopes",             "RemoveAllBivouacRopes");
            PatchFilePaths("BivouacSaveRopes",             "LoadStoredropes");
            PatchFilePaths("BivouacSaveRopes",             "SaveStoredRopes");
            PatchFilePaths("CheckStats",                   "CheckLowestScoreGrades");
            PatchFilePaths("CheckStats",                   "DropDownCheckStats");
            PatchFilePaths("GameManager",                  "CreateBackup");
            PatchFilePaths("GameManager",                  "Load");
            PatchFilePaths("GameManager",                  "Save");
            PatchFilePaths("MenuSaveManager",              "CheckAvianProgress");
            PatchFilePaths("MenuSaveManager",              "CheckCanDelete");
            PatchFilePaths("MenuSaveManager",              "CheckOldSaves");
            PatchFilePaths("MenuSaveManager",              "DeleteSlot");
            PatchFilePaths("MenuSaveManager",              "PlaySlot");
            PatchFilePaths("MenuSaveManager",              "SaveNewGame");
            PatchFilePaths("NPCEvents",                    "TimeAttackStoreDefaultArrays");
            PatchFilePaths("RopeCabinDescription",         "SaveHarnessUse");
            PatchFilePaths("TimeAttack",                   "LoadSTTime");
            PatchFilePaths("TimeAttack",                   "SaveTimeAttack");
            PatchFilePaths("TimeAttackSetter",             "LoadBest");
            PatchFilePaths("TimeAttackSetter",             "SaveTimeAttack");
            PatchFilePaths("TimeAttackTierAchievements",   "ScoreTimeAttackAchievement");

            PatchGlobalStats("CheckStats",                 "LoadIndividualPeakStats");
            PatchGlobalStats("CheckStats",                 "ShowStats");
            PatchGlobalStats("GameManager",                "LoadAllStats");
            PatchGlobalStats("GameManager",                "LoadIndividualPeakStats");
            PatchGlobalStats("GameManager",                "RemakeStats");
            PatchGlobalStats("GameManager",                "SaveAllStats");
            PatchGlobalStats("GameManager",                "SaveIndividualPeakStats");
            PatchGlobalStats("GameManager",                "SaveTAAchievement");
            PatchGlobalStats("GameManager",                "StatsCorruptionHandle");
            PatchGlobalStats("TimeAttackTierAchievements", "ScoreTimeAttackAchievement");
        }
    }
}
