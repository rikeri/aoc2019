with open("input1.txt", "r") as f:
  inputs = f.read()
  inputs = [int(i) for i in inputs.split()]

def fuel(mass):
  return mass//3 - 2 

print(sum(map(fuel, inputs)))  # puzzle 1

def fuel2(mass):
  f = fuel(mass)
  if f <= 0:
    return 0
  return f + fuel2(f)

print(sum(map(fuel2, inputs)))  # puzzle 2