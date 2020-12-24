#!/usr/bin/env python3

"""Advent of Code 2020 Day 24 - Lobby Layout."""


with open('inputs/2020_24.txt') as f:
    instructions = [line.strip() for line in f.readlines()]

tiles = {}
# Translate hex grid  movements into cube coordinates
directions = {
        'e': (-1, 1, 0), 'se': (-1, 0, 1), 'sw': (0, -1, 1),
        'w': (1, -1, 0), 'nw': (1, 0, -1), 'ne': (0, 1, -1)
}
for instruction in instructions:
    current_coords = (0, 0, 0)
    index = 0
    while index < len(instruction):
        y, x, z = current_coords
        if instruction[index] not in directions:
            move = "{}{}".format(instruction[index], instruction[index + 1])
            index += 1
        else:
            move = instruction[index]
        dy, dx, dz = directions[move]
        current_coords = (y + dy, x + dx, z + dz)
        index += 1

    current_colour = tiles.get(current_coords, 0)
    tiles[current_coords] = 1 if current_colour == 0 else 0

# Answer One
print("Number of black tiles:", sum([1 for x in tiles.values() if x == 1]))
