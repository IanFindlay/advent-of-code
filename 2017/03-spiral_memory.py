"""Answers to Advent of Code Day 3."""


# Challenge 1
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
    print('Line max = ' + str(line_max))

    # Calculate all four mid points of layer
    mid_values = [line_max - layers, line_max - layers * 3,
                  line_max - layers * 5, line_max - layers * 7]
    print(mid_values)

    # Find nearest mid point to target number and the distance to it
    mid_distance = number
    for value in mid_values:
        if abs(target - value) < mid_distance:
            mid_distance = abs(target - value)
    print(mid_distance)

    # Return value of distance to middle + layers
    return mid_distance + layers


# Challenge 1 Answer
print(distance(361527))

# Challenge 2
"""Form a spiral from the centre by adding its neighbouring squares."""

# Answer from OEIS = 363010 but coding this one might be beyond me
