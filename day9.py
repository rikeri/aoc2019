with open("input9.txt", "r") as f:
  tx = f.read()

def parse(program:str) -> list:
  return list(map(int, program.split(",")))

def decode_opcode(opcode:int) -> tuple:
  parmms, op = divmod(opcode, 100)
  parmms, parmm1 = divmod(parmms, 10)
  parmms, parmm2 = divmod(parmms, 10)
  parmms, parmm3 = divmod(parmms, 10)
  return op, parmm1, parmm2, parmm3

class Intcomputer:

  def __init__(self, program, pc=0, relbase=0):
    self.pc = pc
    self.relbase = relbase
    self.increase_pc = True
    self.program = program
    self.program.extend([0]*2**16)  # this should be enough, right?

  def __str__(self):
    return f"<Intcomputer pc={self.pc} relbase={self.relbase} instr at pc={self.program[self.pc]} program length={len(self.program)}>"

  def run_to_halt(self):

    def param(index, mode):
      return program[self.pc + index] + (self.relbase if mode == 2 else 0) if mode != 1 else self.pc + index

    program = self.program
    opcode = program[self.pc]
    while opcode != 99:
      op, pm1, pm2, pm3 = decode_opcode(opcode)

      i1 = param(1, pm1)
      i2 = param(2, pm2)
      i3 = param(3, pm3)

      if op == 1: # ADD
        program[i3] = program[i1] + program[i2]
      elif op == 2: # MUL
        program[i3] = program[i1] * program[i2]
      elif op == 3:  # INPUT
        assert(pm1 != 1), "parameter mode is not positional or relative for first param"
        num = int(input("awaiting input >>> "))
        program[i1] = num
      elif op == 4:  # OUTPUT
        print(program[i1])
      elif op == 5:  # JNZ
        if program[i1] != 0:
          self.pc = program[i2]
          self.increase_pc = False
      elif op == 6:  # JZ
        if program[i1] == 0:
          self.pc = program[i2]
          self.increase_pc = False
      elif op == 7:  # JLT
        program[i3] = 1 if program[i1] < program[i2] else 0
      elif op == 8:  # JEQ
        program[i3] = 1 if program[i1] == program[i2] else 0
      elif op == 9:  # RELBASE
        self.relbase += program[i1]
      else:
        raise ValueError(f"Unknown opcode {op} from {opcode} at position {self.pc}")
      if self.increase_pc:
        self.pc += {1: 4, 2: 4, 3: 2, 4: 2, 5:3, 6: 3, 7: 4, 8:4, 9:2}.get(op, -1)
      self.increase_pc = True
      opcode = program[self.pc]
    return program[0]

ic = Intcomputer(parse(tx))
ic.run_to_halt()