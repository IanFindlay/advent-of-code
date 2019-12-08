"""Advent of Code 2019 Day 8 - Space Image Format."""


def check_corruption(layers):
    """Return one count * two count of layer with the least zeros in it."""
    least_zeros = (None, None)
    for layer, values in layers.items():
        zeros = values.count(0)
        if not least_zeros[0] or zeros < least_zeros[0]:
            least_zeros = (zeros, layer)

    zeros_layer = layers[least_zeros[1]]
    return zeros_layer.count(1) * zeros_layer.count(2)


def decode_image(layers, height, width):
    """Combine the layers and return the decoded image."""
    final_image = []
    for row in range(height):
        current_row = []
        for col in range(width):
            pixel_pos = col + row * width
            for layer in range(len(layers)):
                pixel = layers[layer][pixel_pos]
                if pixel == 0:
                    current_row.append('#')
                    break
                elif pixel == 1:
                    current_row.append(' ')
                    break
        final_image.append(current_row)

    return final_image


with open('input.txt', 'r') as f:
    digits = [int(x) for x in list(f.read().strip())]

height, width = (6, 25)
size = height * width

i = 0
layers = {}
layer = 0
while i < len(digits):
    layers[layer] = digits[i: i+size]
    i += size
    layer += 1

# Answer One
print("Corruption Check", check_corruption(layers))

# Answer Two
image = decode_image(layers, height, width)
print("Decoded Image:", end='\n\n')
for row in image:
    print(''.join(row))
