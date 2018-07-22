"""Advent of Code Day 3 - Spiral Memory"""


def distance(target):
    """Find how far input is away from the centre of a number spiral."""
    # Find which odd square layer contains the input
    layers = 0
    number = 1
    line_max = 0
    while line_max < target:
        number += 2
        line_max = number * number
        layers += 1

    # Calculate all four mid points of layer
    mid_values = [line_max - layers, line_max - layers * 3,
                  line_max - layers * 5, line_max - layers * 7]

    # Find nearest mid point to target number and the distance to it
    mid_distance = number
    for value in mid_values:
        if abs(target - value) < mid_distance:
            mid_distance = abs(target - value)

    # Return value of distance to middle + layers
    return mid_distance + layers


def next_coords(x, y):
    """Return the next coordinate pair of an anticlockwise spiral."""
    if y == 0 and x == 0:
        coords = (1, 0)
    elif y > -x and x > y:
        coords = (x, y + 1)
    elif y > -x and y >= x:
        coords = (x - 1, y)
    elif y <= -x and x >= y:
        coords = (x + 1, y)
    elif y <= -x and x < y:
        coords = (x, y - 1)

    return coords


puzzle_input = 361527
# Initial Coordinates and Values Dictionary
x, y = 0, 0
values = { (0, 0): 1 }

while values[(x, y)] <= puzzle_input:
    x, y = next_coords(x, y)
    offsets = [-1, 0, 1]
    values[(x, y)] = (sum(values.get((x + i, y + j), 0)
                          for i in offsets for j in offsets))

# Answer One
print("Steps required:", distance(361527))

# Answer Two
print("Answer value: " + str(values[(x, y)]))
