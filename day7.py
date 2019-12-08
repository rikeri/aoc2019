from itertools import permutations

with open("input7.txt", "r") as f:
  tx = f.read()

def parse(program:str) -> list:
  return list(map(int, program.split(",")))

def decode_opcode(opcode:int) -> tuple:
  parmms, op = divmod(opcode, 100)
  parmms, parmm1 = divmod(parmms, 10)
  parmms, parmm2 = divmod(parmms, 10)
  parmms, parmm3 = divmod(parmms, 10)
  return op, parmm1, parmm2, parmm3

class Amplifier():
  def __init__(self, program, amplifier_index):
    self.amplifier_index = amplifier_index
    self.program = program
    self.increase_pc = True
    self.got_phase = False
    self.pc = 0
    self.halted = False

  def __str__(self):
    name = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E"}.get(self.amplifier_index)
    return f"{name} pc:{self.pc}, halted:{self.halted}, gp:{self.got_phase}, ioputs:{ioputs}"

  def run_to_output(self):
    if self.halted:
      return
    program = self.program
    amp_i = self.amplifier_index
    opcode = program[self.pc]

    got_input = False
    return_after_pc = False
    while opcode != 99:
      op, pm1, pm2, pm3 = decode_opcode(opcode)

      def i1(): return program[self.pc+1] if pm1 == 0 else self.pc+1
      def i2(): return program[self.pc+2] if pm2 == 0 else self.pc+2
      def i3(): return program[self.pc+3] if pm3 == 0 else self.pc+3

      if op == 1:
        program[i3()] = program[i1()] + program[i2()]
      elif op == 2:
        program[i3()] = program[i1()] * program[i2()]
      elif op == 3:
        assert(pm1 == 0), "parameter mode is not positional for first param"
        if not self.got_phase:
          self.got_phase = True
          num = phases[amp_i]
        else:
          num = ioputs[amp_i]
        program[i1()] = num
      elif op == 4:
        ioputs[(amp_i + 1)%5] = program[i1()]
        return_after_pc = True
      elif op == 5:
        if program[i1()] != 0:
          self.pc = program[i2()]
          self.increase_pc = False
      elif op == 6:
        if program[i1()] == 0:
          self.pc = program[i2()]
          self.increase_pc = False
      elif op == 7:
        program[i3()] = 1 if program[i1()] < program[i2()] else 0
      elif op == 8:
        program[i3()] = 1 if program[i1()] == program[i2()] else 0
      else:
        raise ValueError(f"Unknown opcode {op} from {opcode} at position {self.pc}")
      if self.increase_pc:
        self.pc += {1: 4, 2: 4, 3: 2, 4: 2, 5:3, 6: 3, 7: 4, 8:4}.get(op, -1)
      self.increase_pc = True
      if return_after_pc:
        return
      opcode = program[self.pc]
    self.halted = True

base_program = parse(tx)
max_output = 0
max_phases = None
for phases in permutations(range(5, 10)):
  ioputs = [0,0,0,0,0]  # connection between machines
  amplifiers = [Amplifier(base_program.copy(), amp_i) for amp_i in range(5)]
  while not all(a.halted for a in amplifiers):
    for a in amplifiers:
      a.run_to_output()
  if ioputs[-1] > max_output:
    max_output = ioputs[0]
    max_phases = phases
print(f"Found max output {max_output} with the phase combination {max_phases}")
  