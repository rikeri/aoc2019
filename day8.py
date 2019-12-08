with open("input8.txt", "r") as f:
  image = f.read()

height = 6
width = 25
area = height*width
# image = "123456789012"
num_layers = len(image) // area
def countof(digit, string): return len([c for c in string if c == digit])

layers = []
for i in range(0, len(image)-1, area):
  layer = image[i:i+area]
  zerocount = countof("0", layer)
  layers.append((zerocount, layer))
layers.sort()
layer = layers[0][1]
onecount = countof("1", layer)
twocount = countof("2", layer)
print(onecount * twocount) # puzzle 1