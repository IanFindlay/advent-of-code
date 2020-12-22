"""Advent of Code Day 3 - Perfectly Spherical Houses in a Vacuum"""


def houses_visited(part_two=False):
    """Returns the number of unique houses visited."""
    visited = 1
    visited_list = [[0, 0]]
    santa_coords = [0, 0]
    robo_coords = [0, 0]
    santa = True
    for char in directions:
        if santa:
            if char == '^':
                new_coords = [santa_coords[0], santa_coords[1] + 1]
            elif char == 'v':
                new_coords = [santa_coords[0], santa_coords[1] - 1]
            elif char == '<':
                new_coords = [santa_coords[0] - 1, santa_coords[1]]
            elif char == '>':
                new_coords = [santa_coords[0] + 1, santa_coords[1]]

            if new_coords not in visited_list:
                visited_list.append(new_coords)
                visited += 1

            santa_coords = new_coords
            if part_two:
                santa = False

        else:
            if char == '^':
                new_coords = [robo_coords[0], robo_coords[1] + 1]
            elif char == 'v':
                new_coords = [robo_coords[0], robo_coords[1] - 1]
            elif char == '<':
                new_coords = [robo_coords[0] - 1, robo_coords[1]]
            elif char == '>':
                new_coords = [robo_coords[0] + 1, robo_coords[1]]

            if new_coords not in visited_list:
                visited_list.append(new_coords)
                visited += 1

            robo_coords = new_coords
            santa = True

    return visited


with open('inputs/day_03.txt') as f:
    directions = f.read()

# Answer Part One
print("Number of unique houses visited =", houses_visited())

# Answer Part Two
print("Number visited with robots help =", houses_visited(part_two=True))
