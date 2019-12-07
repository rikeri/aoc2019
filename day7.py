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

def run_to_halt(program, amplifier_index=0):
  increase_pc = True
  pc = 0
  opcode = program[pc]
  got_phase = False
  got_input = False
  while opcode != 99:
    op, pm1, pm2, pm3 = decode_opcode(opcode)

    def i1(): return program[pc+1] if pm1 == 0 else pc+1
    def i2(): return program[pc+2] if pm2 == 0 else pc+2
    def i3(): return program[pc+3] if pm3 == 0 else pc+3

    if op == 1:
      program[i3()] = program[i1()] + program[i2()]
    elif op == 2:
      program[i3()] = program[i1()] * program[i2()]
    elif op == 3:
      assert(pm1 == 0), "parameter mode is not positional for first param"
      if not got_phase:
        got_phase = True
        num = phases[amplifier_index]
      elif not got_input:
        got_input = True
        num = ioputs[amplifier_index]
      program[i1()] = num
    elif op == 4:
      ioputs[amplifier_index + 1] = program[i1()]
    elif op == 5:
      if program[i1()] != 0:
        pc = program[i2()]
        increase_pc = False
    elif op == 6:
      if program[i1()] == 0:
        pc = program[i2()]
        increase_pc = False
    elif op == 7:
      program[i3()] = 1 if program[i1()] < program[i2()] else 0
    elif op == 8:
      program[i3()] = 1 if program[i1()] == program[i2()] else 0
    else:
      raise ValueError(f"Unknown opcode {op} from {opcode} at position {pc}")
    if increase_pc:
      pc += {1: 4, 2: 4, 3: 2, 4: 2, 5:3, 6: 3, 7: 4, 8:4}.get(op, -1)
    increase_pc = True
    opcode = program[pc]
  return program[0]

base_program = parse(tx)
max_output = 0
max_phases = None
for phases in permutations(range(5)):
  ioputs = [0,0,0,0,0,0]
  for amp_i in range(5):
    run_to_halt(base_program.copy(), amp_i)
  if ioputs[-1] > max_output:
    max_output = ioputs[-1]
    max_phases = phases
print(f"Found max output {max_output} with the phase combination {max_phases}")
  