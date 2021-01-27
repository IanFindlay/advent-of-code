#!/usr/bin/env python3

"""Advent of Code 2020 Day 24 - Lobby Layout."""


with open('inputs/day_24.txt') as f:
    instructions = [line.strip() for line in f.readlines()]

tiles = {}
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
    if current_colour == 0:
        tiles[current_coords] = 1
    else:
        del tiles[current_coords]

# Answer One
print("Number of black tiles:", len(tiles))

for _ in range(100):
    new_tiles = {}
    checked = set()
    for coords in tiles:
        y, x, z = coords
        black_adjacent = 0
        for next_to in directions.values():
            next_to_coords = (next_to[0] + y, next_to[1] + x, next_to[2] + z)
            if next_to_coords in tiles:
                black_adjacent += 1

            elif next_to_coords in checked:
                pass

            else:
                double_black_adjacent = 0
                for double_next_to in directions.values():
                    double_next_coords = (
                            double_next_to[0] + next_to_coords[0],
                            double_next_to[1] + next_to_coords[1],
                            double_next_to[2] + next_to_coords[2]
                    )

                    if double_next_coords in tiles:
                        double_black_adjacent += 1

                if double_black_adjacent == 2:
                    new_tiles[next_to_coords] = 1

                checked.add(next_to_coords)

        if black_adjacent in (1, 2):
            new_tiles[coords] = 1

        checked.add(coords)

    tiles = new_tiles

# Answer Two
print("Number of black tiles after 100 days:", len(tiles))
