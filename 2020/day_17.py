#!/usr/bin/env python3

"""Advent of Code 2020 Day 17 - Conway Cubes."""


def cycle_cubes(active_cubes: set) -> set:
    """."""
    lowest_x = min(active_cubes, key=lambda x: x[0])[0]
    lowest_y = min(active_cubes, key=lambda x: x[1])[1]
    lowest_z = min(active_cubes, key=lambda x: x[2])[2]
    highest_x = max(active_cubes, key=lambda x: x[0])[0]
    highest_y = max(active_cubes, key=lambda x: x[1])[1]
    highest_z = max(active_cubes, key=lambda x: x[2])[2]

    new_active_cubes = set()
    for x in range(lowest_x - 1, highest_x + 2):
        for y in range(lowest_y - 1, highest_y + 2):
            for z in range(lowest_z -1, highest_z + 2):
                coords = (x, y, z)
                neighbours = neighbouring_coords(coords)
                active = 0
                for neighbour in neighbours:
                    if neighbour in active_cubes:
                        active += 1

                if coords in active_cubes and active in (2, 3):
                    new_active_cubes.add(coords)

                else:
                    if active == 3:
                        new_active_cubes.add(coords)

    return new_active_cubes


def neighbouring_coords(coords: tuple) -> list:
    """."""
    neighbours = []
    for x in range(-1, 2):
        new_x = coords[0] + x

        for y in range(-1, 2):
            new_y = coords[1] + y

            for z in range(-1, 2):
                new_coords = (new_x, new_y, coords[2] + z)
                if new_coords != coords:
                    neighbours.append(new_coords)

    return neighbours


with open('inputs/2020_17.txt', 'r') as f:
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
