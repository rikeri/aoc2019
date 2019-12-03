import numpy as np
from matplotlib import pyplot as plt

with open("input3.txt", "r") as f:
  l = f.read()

lines = l.split("\n")
wire1 = lines[0].split(",")
wire2 = lines[1].split(",")
print(wire1)
print(wire2)

wire1_touched_points = set()
wire1_steps = {}
wire2_touched_points = set()
wire2_steps = {}
cross_wire_intersections = set()

def trace_wire(wire, points:set, steps:dict):
  posx, posy = 0,0
  stepstaken = 0
  points.add((0,0))
  steps[(0,0)] = stepstaken
  print("Tracing wire")
  for line in wire:  # this looked prettier before the step count of puzzle 2 was needed
    d = line[0]
    dist = int(line[1:])
    if d == "R":
      for dx in range(posx+1, posx+dist+1):
        stepstaken += 1
        p = (dx, posy)
        points.add(p)
        if p not in steps:
          steps[p] = stepstaken
      posx += dist
    elif d == "L":
      for dx in range(posx-1, posx-dist-1, -1):
        stepstaken += 1
        p = (dx, posy)
        points.add(p)
        if p not in steps:
          steps[p] = stepstaken
      posx -= dist
    elif d == "U":
      for dy in range(posy+1, posy+dist+1):
        stepstaken += 1
        p = (posx, dy)
        points.add(p)
        if p not in steps:
          steps[p] = stepstaken
      posy += dist
    elif d == "D":
      for dy in range(posy-1, posy-dist-1, -1):
        stepstaken += 1
        p = (posx, dy)
        points.add(p)
        if p not in steps:
          steps[p] = stepstaken
      posy -= dist
    else:
      raise SyntaxError("Unknown direction")

trace_wire(wire1, wire1_touched_points, wire1_steps)
trace_wire(wire2, wire2_touched_points, wire2_steps)
cross_wire_intersections = wire1_touched_points.intersection(wire2_touched_points)

sorted_intersections = sorted(list(cross_wire_intersections), key=lambda t: sum(map(abs, t)))
print(sorted_intersections)
closest = sorted_intersections[1]
print("closest intersection is", closest, "with distance", sum(map(abs, closest)))

# task 2
sorted_intersections_stepcount = sorted(list(cross_wire_intersections), key=lambda t: wire1_steps[t] + wire2_steps[t])
closest_step = sorted_intersections_stepcount[1]
print("closest intersection stepwise is", closest_step, "with", wire1_steps[closest_step] + wire2_steps[closest_step], "steps required")

# plot it for good measure
plt.scatter([t[0] for t in wire1_touched_points], [t[1] for t in wire1_touched_points])
plt.scatter([t[0] for t in wire2_touched_points], [t[1] for t in wire2_touched_points], marker="x")
plt.scatter([t[0] for t in cross_wire_intersections], [t[1] for t in cross_wire_intersections], marker="o")
plt.axis("equal")
plt.show()
