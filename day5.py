with open("input5.txt", "r") as f:
  tx = f.read()

def parse(program:str) -> list:
  return list(map(int, program.split(",")))

def decode_opcode(opcode:int) -> tuple:
  parmms, op = divmod(opcode, 100)
  parmms, parmm1 = divmod(parmms, 10)
  parmms, parmm2 = divmod(parmms, 10)
  parmms, parmm3 = divmod(parmms, 10)
  return op, parmm1, parmm2, parmm3

def run_to_halt(program):
  pc = 0
  opcode = program[pc]
  while opcode != 99:
    op, pm1, pm2, pm3 = decode_opcode(opcode)
    if op == 1:
      program[program[pc+3] if pm3 == 0 else pc+3] = (program[program[pc+1] if pm1 == 0 else pc+1]) + (program[program[pc+2] if pm2 == 0 else pc+2])
    elif op == 2:
      program[program[pc+3] if pm3 == 0 else pc+3] = (program[program[pc+1] if pm1 == 0 else pc+1]) * (program[program[pc+2] if pm2 == 0 else pc+2])
    elif op == 3:
      assert(pm1 == 0), "parameter mode is not positional for first param"
      num = int(input("awaiting input >>> "))
      program[program[pc+1]] = num
    elif op == 4:
      print(program[program[pc+1] if pm3 == 0 else pc+1])
    else:
      raise ValueError(f"Unknown opcode {op} from {opcode} at position {pc}")
    pc += {1: 4, 2: 4, 3: 2, 4: 2}.get(op)
    opcode = program[pc]
  return program[0]

run_to_halt(parse(tx))
