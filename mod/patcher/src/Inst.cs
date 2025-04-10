using Mono.Cecil.Cil;

namespace PoYArchipelagoPatcher {
    /**
     * <summary>
     * Holds information about an instruction.
     * </summary>
     */
    public class Inst {
        public OpCode opcode;
        public object operand;

        /**
         * <summary>
         * Constructs an instance of Inst.
         * </summary>
         * <param name="opcode">The instruction's opcode</param>
         * <param name="operand">The instruction's operand</param>
         */
        public Inst(OpCode opcode, object operand) {
            this.opcode = opcode;
            this.operand = operand;
        }

        /**
         * <summary>
         * Constructs an instance of Inst.
         * </summary>
         * <param name="opcode">The instruction's opcode</param>
         */
        public Inst(OpCode opcode) : this(opcode, null) {}
    }
}
