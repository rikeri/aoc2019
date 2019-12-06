# # works when the input is sorted
# for line in omap.split("\n"):
#   orbitee, orbiter = line.split(")")
#   orbits[orbiter] = orbits[orbitee] + 1
# print(sum(orbits.values()))

with open("input6.txt", "r") as f:
  lines = f.read().strip().split("\n")

pointers = {}
for line in lines:
  orbitee, orbiter = line.split(")")
  if orbitee in pointers:
    pointers[orbitee].append(orbiter)
  else:
    pointers[orbitee] = [orbiter]

orbits = {}
orbits["COM"] = 0

# run a dfs starting with COM
queue = ["COM"]
while queue:
  current = queue.pop(0)
  if current not in pointers:
    continue
  for orbiter in pointers[current]:
    orbits[orbiter] = orbits[current] + 1
    queue.append(orbiter)

print(pointers)
print(sum(orbits.values()))