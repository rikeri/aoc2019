from math import gcd, sqrt, atan2, pi

with open("input10.txt", "r") as f:
  amap = f.read()

grid = [list(r) for r in amap.split()]
asteroid_locations = set()

width, height = len(grid[0]), len(grid)

for y in range(height):
  for x in range(width):
    if grid[y][x] == "#":
      asteroid_locations.add((x, y))

def degrees_of(vector, zeropoint=90):
  return (atan2(vector[1], vector[0]) * (180/pi) + 90) % 360

def normalized_vector(origin, target):
  x, y = origin
  tx, ty = target
  dx, dy = tx - x, ty - y 
  distance = sqrt(dx**2 + dy**2)
  cd = gcd(dx, dy)
  dx, dy = dx//cd, dy//cd
  return (dx, dy), distance

visible_asteroid_counts = {}
asteroid_vectors = {}

for a in asteroid_locations:
  vectors = {}
  others = asteroid_locations - {a}
  for ta in others:
    vector, distance = normalized_vector(a, ta)
    if vector in vectors:
      vectors[vector].append((distance, ta))
    else:
      vectors[vector] = [(distance, ta)]
  asteroid_vectors[a] = vectors
  astercount = len(vectors)
  visible_asteroid_counts[a] = astercount

sortedroids = list(sorted(visible_asteroid_counts.items(), key=lambda t: t[1]))
candidate = sortedroids[-1]
print(f"Asteroid {candidate[0]} is best and can see {candidate[1]} asteroids") # puzzle 1

station = candidate[0]
elimination_counts = {}
s_vectors = asteroid_vectors[station]
count = 0
while any(s_vectors.values()):
  for v in sorted(s_vectors.keys(), key=lambda vec: degrees_of(vec)):
    if not s_vectors[v]:
      continue
    count += 1
    asteroid = s_vectors[v].pop(0)
    elimination_counts[count] = asteroid

twouhundredth = elimination_counts[200][1]
print(twouhundredth[0] * 100 + twouhundredth[1])  # puzzle 2
