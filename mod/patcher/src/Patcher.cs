using System.Collections.Generic;

using Mono.Cecil;

namespace PoYArchipelagoPatcher {
    public static class Patcher {
        // The DLLs this patcher targets
        public static IEnumerable<string> TargetDLLs { get; } = new string[] {
            "Assembly-CSharp.dll",
        };

        /**
         * <summary>
         * Applies very early patches.
         * </summary>
         */
        public static void Patch(AssemblyDefinition assembly) {
            Patches.NormalPaths.Patch(assembly);
            Patches.Locations.Patch(assembly);
        }
    }
}
