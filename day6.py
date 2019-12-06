with open("input6.txt", "r") as f:
  lines = f.read().strip().split("\n")

# construct a tree
pointers = {}
for line in lines:
  orbitee, orbiter = line.split(")")
  if orbitee in pointers:
    pointers[orbitee].append(orbiter)
  else:
    pointers[orbitee] = [orbiter]

orbits = {}
orbits["COM"] = 0
parents = {}

# run a dfs starting with COM, keeping track of parents
queue = ["COM"]
while queue:
  current = queue.pop(0)
  if current not in pointers:
    continue
  for orbiter in pointers[current]:
    parents[orbiter] = current
    orbits[orbiter] = orbits[current] + 1
    queue.append(orbiter)

print(sum(orbits.values()))  # puzzle 1

def trace_path(target):
  path = []
  while target in parents:
    path.append(target)
    target = parents[target]
  return list(reversed(path))

def compare_paths(path1, path2):
  common_root = 0
  for n1, n2, i in zip(path1, path2, range(max(len(path1), len(path2)))):
    if n1 != n2:
      common_root = i-1
      break
  unique1 = path1[common_root+1:-1]
  unique2 = path2[common_root+1:-1]
  return len(unique1) + len(unique2)

print(compare_paths(trace_path("YOU"), trace_path("SAN"))) # puzzle 2