with open("input8.txt", "r") as f:
  image = f.read()

height = 6
width = 25
area = height*width
num_layers = len(image) // area
def countof(digit, string): return len([c for c in string if c == digit])

layers = []
for i in range(0, len(image)-1, area):
  layer = image[i:i+area]
  zerocount = countof("0", layer)
  layers.append((zerocount, layer))
layer = sorted(layers)[0][1]
onecount = countof("1", layer)
twocount = countof("2", layer)
print(onecount * twocount) # puzzle 1

render = ["2"]*area
for i in range(area):
  for _, l in layers:
    if render[i] != "2" or l[i] == "2":
      continue
    render[i] = l[i]

raster = ["#" if c == "1" else " " for c in render]

for i in range(0, area, width):
  print("".join(raster[i:i+width])) # puzzle 2