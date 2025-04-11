using System.Reflection;

using Mono.Cecil;
using Mono.Cecil.Cil;
using MonoMod.Utils;

namespace PoYArchipelagoPatcher.Patches {
    public static class Locations {
        /**
         * <summary>
         * Injects different file paths depending on
         * the instance of GameManager.
         * </summary>
         * <param name="instance">The instance of GameManager</param>
         * <param name="filePath"></param>
         */
        public static string InjectPath(object instance, string filePath) {
            // If the location manager was called, use a different path
            if (instance.GetType().ToString() == "PoYArchipelago.Patches.LocationManager") {
                filePath = $"{filePath}.locs";
            }

            Logger.LogDebug($"Injecting: {filePath}");
            return filePath;
        }

        /**
         * <summary>
         * Patches a method in GameManager to use custom locations
         * depending on the instance of GameManager being called on.
         * </summary>
         * <param name="module">The module to patch</param>
         * <param name="methodName">The name of the method to patch</param>
         */
        private static void PatchManager(ModuleDefinition module, string methodName) {
            TypeDefinition gameManager = module.GetType("GameManager");
            MethodDefinition method = gameManager.FindMethod(methodName);

            MethodReference injectMethod = method.Module.ImportReference(
                typeof(Locations).GetMethod(
                    "InjectPath",
                    BindingFlags.Public | BindingFlags.Static
                )
            );

            Logger.LogInfo($"Patching: {module}.GameManager.{methodName}");

            Helper.InsertAfter(
                method,
                new[] {
                    new Inst(OpCodes.Ldloc_0),
                    new Inst(OpCodes.Ldloc_1),
                    new Inst(OpCodes.Call, null),
                    new Inst(OpCodes.Stloc_2),
                },
                new[] {
                    new Inst(OpCodes.Ldarg_0),
                    new Inst(OpCodes.Ldloc_2),
                    new Inst(OpCodes.Call, injectMethod),
                    new Inst(OpCodes.Stloc_2),
                }
            );
        }

        /**
         * <summary>
         * Applies patches for storing location checks.
         * </summary>
         * <param name="assembly">The assembly to patch</param>
         */
        public static void Patch(AssemblyDefinition assembly) {
            ModuleDefinition main = assembly.MainModule;

            PatchManager(main, "Load");
            PatchManager(main, "Save");
        }
    }
}
