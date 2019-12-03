with open("input2.txt", "r") as f:
  tx = f.read()

base_program = list(map(int, tx.split(",")))

# only solution 2 is here but solution 1 can be found by setting noun and verb
def run_to_halt(program, noun, verb):
  program[1] = noun
  program[2] = verb
  for index, opcode in list(enumerate(program))[::4]:
    if opcode == 99:
      break
    in1 = program[index+1]
    in2 = program[index+2]
    out = program[index+3]
    if opcode == 1:
      program[out] = program[in1] + program[in2]
    elif opcode == 2:
      program[out] = program[in1] * program[in2]
  return program[0]

for x in range(len(base_program)-1):
  for y in range(len(base_program)-1):
    p = base_program.copy()
    r = run_to_halt(p, x, y)
    if r == 19690720:
      print(f"\nFound noun {x} verb {y}")
      print(f"Puzzle result is thus {100*x + y}")
      break 
  else:  # python's way of breaking out of nested loops
    continue
  break