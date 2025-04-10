using Mono.Cecil;
using Mono.Cecil.Cil;
using MonoMod.Utils;

namespace PoYArchipelagoPatcher.Patches {
    public static class Locations {
        public static void MyMethod() {
            Logger.LogDebug("Hello, world!");
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
         * Applies patches for storing location checks.
         * </summary>
         * <param name="assembly">The assembly to patch</param>
         */
        public static void Patch(AssemblyDefinition assembly) {
        }
    }
}
