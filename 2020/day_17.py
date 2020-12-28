#!/usr/bin/env python3

"""Advent of Code 2020 Day 17 - Conway Cubes."""


def cycle_cubes(active_cubes: set, part_two=False) -> set:
    """."""
    lowest_x = min(active_cubes, key=lambda x: x[0])[0]
    lowest_y = min(active_cubes, key=lambda x: x[1])[1]
    lowest_z = min(active_cubes, key=lambda x: x[2])[2]
    highest_x = max(active_cubes, key=lambda x: x[0])[0]
    highest_y = max(active_cubes, key=lambda x: x[1])[1]
    highest_z = max(active_cubes, key=lambda x: x[2])[2]

    if part_two:
        lowest_w = min(active_cubes, key=lambda x: x[3])[3]
        highest_w = max(active_cubes, key=lambda x: x[3])[3]

    new_active_cubes = set()
    for x in range(lowest_x - 1, highest_x + 2):
        for y in range(lowest_y - 1, highest_y + 2):
            for z in range(lowest_z -1, highest_z + 2):
                if not part_two:
                    if new_state((x, y, z), active_cubes):
                        new_active_cubes.add((x, y, z))
                else:
                    for w in range(lowest_w - 1, highest_w + 2):
                        if new_state((x, y, z, w), active_cubes, True):
                            new_active_cubes.add((x, y, z, w))

    return new_active_cubes


def new_state(coords, active_cubes: set, part_two=False) -> bool:
    """."""
    neighbours = neighbouring_coords(coords, part_two)
    active = 0
    for neighbour in neighbours:
        if neighbour in active_cubes:
            active += 1

    if coords in active_cubes and active in (2, 3):
        return True

    else:
        if active == 3:
            return True

    return False


def neighbouring_coords(coords: tuple, part_two=False) -> list:
    """."""
    neighbours = []
    for x in range(-1, 2):
        new_x = coords[0] + x

        for y in range(-1, 2):
            new_y = coords[1] + y

            for z in range(-1, 2):
                new_z = coords[2] + z
                if not part_two:
                    new_coords = (new_x, new_y, new_z)
                    if new_coords != coords:
                        neighbours.append(new_coords)
                else:
                    for w in range(-1, 2):
                        new_coords = (new_x, new_y, new_z, coords[3] + w)

                        if new_coords != coords:
                            neighbours.append(new_coords)

    return neighbours


with open('inputs/day_17.txt', 'r') as f:
    rows = [[char for char in row.strip()] for row in f.readlines()]

active_cubes = set()
for x, row in enumerate(rows):
    for y, state in enumerate(row):
        if state == '#':
            active_cubes.add((x, y, 0))

for cycle in range(6):
    active_cubes = cycle_cubes(active_cubes)

# Answer One
print("Cubes left in active state after 6th cycle:", len(active_cubes))

active_cubes = set()
for x, row in enumerate(rows):
    for y, state in enumerate(row):
        if state == '#':
            active_cubes.add((x, y, 0, 0))

for cycle in range(6):
    active_cubes = cycle_cubes(active_cubes, part_two=True)

# Answer Two
print("Cubes left in active state after 6th cycle (four dimensions):",
      len(active_cubes))
