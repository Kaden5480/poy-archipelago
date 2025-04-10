using Mono.Cecil.Cil;

namespace PoYArchipelagoPatcher {
    public class Inst {
        public OpCode opcode;
        public object operand;

        public Inst(OpCode opcode, object operand) {
            this.opcode = opcode;
            this.operand = operand;
        }

        public Inst(OpCode opcode) : this(opcode, null) {}
    }
}
