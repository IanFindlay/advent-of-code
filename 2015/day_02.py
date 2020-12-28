"""Advent of Code Day 2 - I Was Told There Would Be No Math"""

def calculate_paper():
    """Calculates and Prints Amount of Paper Required to Wrap Presents."""
    square_feet = 0
    for line in areas:
        length, width, height = line.split('x')
        sides_areas = []
        sides_areas.append(2 * int(length) * int(width))
        sides_areas.append(2 * int(width) * int(height))
        sides_areas.append(2 * int(height) * int(length))

        slack = min(sides_areas) // 2

        square_feet += slack
        for area in sides_areas:
            square_feet += area

    print(square_feet)


def calculate_ribbon():
    """Calculates and Prints Amount of Ribbon Required."""
    feet = 0
    for line in areas:
        side_lengths = line.split('x')
        int_list = sorted([int(x) for x in side_lengths])
        smallest_face = int_list[0] * 2 + int_list[1] * 2
        volume = int_list[0] * int_list[1] * int_list[2]
        feet += smallest_face
        feet += volume

    print(feet)


with open('inputs/day_02.txt') as f:
    areas = f.readlines()


# Answer Part One
calculate_paper()

# Answer Part Two
calculate_ribbon()
