using System;
using System.Collections.Generic;

using Mono.Cecil;
using Mono.Cecil.Cil;
using Mono.Collections.Generic;
using MonoMod.Utils;

namespace PoYArchipelagoPatcher {
    public static class Patcher {
        // The DLLs this patcher targets
        public static IEnumerable<string> TargetDLLs { get; } = new string[] {
            "Assembly-CSharp.dll",
        };

        // The main module definition
        private static ModuleDefinition main;

        /**
         * <summary>
         * Patches occurrences of normal, yfyd, and fs related paths
         * to use a custom path instead.
         * </summary>
         */
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

        /**
         * <summary>
         * Patches occurrences of "global_stats.es3" to use a custom path instead.
         * </summary>
         */
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

        public static void MyMethod() {
            Console.WriteLine("Hello, world!");
        }

        public static void Testing(AssemblyDefinition assembly) {
            ModuleDefinition main = assembly.MainModule;

            TypeDefinition type = main.GetType("CoffeeDrink");
            MethodDefinition method = type.FindMethod("LoadArmSettings");

            Helper.InsertAfter(
                method,
                new[] {
                    new Inst(OpCodes.Ldarg_0),
                    new Inst(OpCodes.Ldarg_0),
                    new Inst(OpCodes.Ldfld, type.FindField("climbing")),
                    new Inst(OpCodes.Ldfld, main.GetType("Climbing").FindField("letGoForce")),
                    new Inst(OpCodes.Stfld, type.FindField("defaultLetGoForce")),
                },
                new[] {
                    new Inst(
                        OpCodes.Call,
                        method.Module.ImportReference(typeof(Patcher).GetMethod("MyMethod"))
                    ),
                }
            );
        }

        /**
         * <summary>
         * Applies very early patches for allowing
         * custom save files.
         * </summary>
         */
        public static void Patch(AssemblyDefinition assembly) {
            main = assembly.MainModule;

            Testing(assembly);

            /*
            // Patch normal save data paths
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

            // Patch global stats paths
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
            */
        }
    }
}
