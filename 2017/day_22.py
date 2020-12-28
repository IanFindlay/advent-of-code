"""Advent of Code Day 22 - Sporifica Virus"""

import collections


def make_dict():
    """Create a coordinate dictionary of the grid."""
    dictionary = {}

    for y in range(len(grid)):
        for x in range(len(grid[0])):

            dictionary[(x, y)] = grid[y][x]

    return dictionary


def infection():
    """Simulate virus activity and return number of infectious bursts."""
    x = len(grid[0]) // 2
    y = len(grid) // 2
    current = (x, y)
    directions = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
    direction = 0
    infectious_bursts = 0
    i = 0
    while i < 10000:

        if not current in grid_dict:
            grid_dict[current] = '.'

        if grid_dict[current] == '.':
            grid_dict[current] = '#'
            direction = (direction - 1) % 4
            infectious_bursts += 1

        else:
            grid_dict[current] = '.'
            direction = (direction + 1) % 4

        change = directions[direction]
        current = (current[0] + change[0], current[1] + change[1])
        i += 1

    return infectious_bursts


def evolved():
    """Simulate evolved virus activity and return number of infectious bursts."""
    x = len(grid[0]) // 2
    y = len(grid) // 2
    current = (x, y)
    directions = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
    direction = 0
    prev_direction = 0
    infectious_bursts = 0
    i = 0
    while i < 10000000:

        if not current in grid_dict:
            grid_dict[current] = '.'

        if grid_dict[current] == '.':
            grid_dict[current] = 'W'
            direction = (direction - 1) % 4

        elif grid_dict[current] == '#':
            grid_dict[current] = 'F'
            direction = (direction + 1) % 4

        elif grid_dict[current] == 'W':
            grid_dict[current] = '#'
            infectious_bursts += 1

        else:
            grid_dict[current] = '.'
            direction = (prev_direction - 2) % 4

        prev_direction = direction
        change = directions[direction]
        current = (current[0] + change[0], current[1] + change[1])
        i += 1

    return infectious_bursts


if __name__ == '__main__':

    with open('inputs/day_22.txt') as f:
        grid = [line.strip() for line in f.readlines()]

    grid_dict = make_dict()

    # Answer One
    print("Total infectious bursts after 10000 bursts:", infection())

    grid_dict = make_dict()

    # Answer Two
    print("Total infectious bursts after evolution:", evolved())
