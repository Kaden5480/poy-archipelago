using System;
using System.Collections.Generic;
using System.Reflection;

using Mono.Cecil;
using Mono.Cecil.Cil;
using Mono.Collections.Generic;
using MonoMod.Utils;


namespace PoYArchipelagoPatcher {
    public static class Helper {
        /**
         * <summary>
         * Converts an instruction to a string representation.
         * </summary>
         */

        /**
         * <summary>
         * Compares two instructions for equivalence.
         * </summary>
         * <param name="a">The first instruction to check (of type Inst)</param>
         * <param name="b">The second instruction to check (of type Instruction)</param>
         * <returns>True if they're the same, false otherwise
         */
        public static bool InstsEqual(Inst a, Instruction b) {
            // Don't check opcodes if opcode in `a` is null
            if (a.opcode != null && a.opcode != b.OpCode) {
                return false;
            }

            // Skip checking operands if operand in `a` is null
            if (a.operand == null) {
                return true;
            }

            if (b.Operand == null) {
                return a.operand == b.Operand;
            }

            if (a.operand.GetType() != b.Operand.GetType()) {
                return false;
            }

            return a.operand.Equals(b.Operand);
        }

        /**
         * <summary>
         * Finds the indices a pattern of instructions starts at
         * in a given collection.
         * </summary>
         * <param name="insts">The instructions to find the pattern in</param>
         * <param name="pattern">The pattern to search for</param>
         * <returns>The indices this sequence has been found at</returns>
         */
        public static IEnumerable<int> FindSeqs(
            Collection<Instruction> insts,
            Inst[] pattern
        ) {
            int beginning = 0;
            int patternIndex = 0;

            for (int i = 0; i < insts.Count; i++) {
                // If fully matched, return beginning of the sequence
                if (patternIndex >= pattern.Length) {
                    yield return beginning;

                    // Also reset
                    beginning = i;
                    patternIndex = 0;
                }

                // Check if this instruction matches the pattern
                if (InstsEqual(pattern[patternIndex], insts[i]) == false) {
                    // Reset values
                    beginning = i + 1;
                    patternIndex = 0;
                }
                else {
                    // Increase pattern index
                    patternIndex++;
                }
            }
        }

        /**
         * <summary>
         * Finds the first index a pattern of instructions starts at
         * in a given collection.
         * </summary>
         * <param name="insts">The instructions to find the pattern in</param>
         * <param name="pattern">The pattern to search for</param>
         * <returns>The index this sequence has been found at, or -1</returns>
         */
        public static int FindSeq(
            Collection<Instruction> insts,
            Inst[] pattern
        ) {
            foreach (int index in FindSeqs(insts, pattern)) {
                return index;
            }

            return -1;
        }

        /**
         * <summary>
         * Inserts a given sequence of instructions after a pattern.
         * </summary>
         * <param name="method">The method to inject instructions into</param>
         * <param name="pattern">The pattern to search for</param>
         * <param name="seq">The sequence to insert after the pattern</param>
         * <returns>The new instructions</returns>
         */
        public static void InsertAfter(
            MethodDefinition method,
            Inst[] pattern,
            Inst[] seq
        ) {
            Collection<Instruction> insts = method.Body.Instructions;
            ILProcessor processor = method.Body.GetILProcessor();

            List<int> indices = new List<int>();

            foreach (int index in FindSeqs(insts, pattern)) {
                indices.Add(index);
            }

            // Work in reverse
            for (int i = indices.Count - 1; i >= 0; i--) {
                // The index to replace with
                int index = indices[i];

                // Find the end of the pattern, this instruction
                // is where the new sequence will be inserted after
                Instruction inst = insts[index + pattern.Length - 1];

                foreach (Inst seqInst in seq) {
                    Instruction newInst = processor.Create(seqInst.opcode, seqInst.operand);
                    processor.InsertAfter(inst, newInst);
                    inst = newInst;
                }
            }
        }
    }
}
