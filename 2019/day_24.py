"""Advent of Code 2019 Day 24 - Planet of Discord."""

from copy import deepcopy


with open('input.txt') as f:
    original_tiles = [list(line) for line in f.read().split()]

tiles = deepcopy(original_tiles)
new_state = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
]

previous_states = set()
while True:
    power_representation = []
    for y in range(5):
        for x in range(5):
            tile = tiles[y][x]

            adjacent = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
            adjacent_bugs = 0
            for row, col in adjacent:
                if row in (-1, 5) or col in (-1, 5):
                    continue

                if tiles[row][col] == '#':
                    adjacent_bugs += 1

            if tile == '#':
                if adjacent_bugs == 1:
                    new_state[y][x] = '#'
                    power_representation.append(2**(y * 5 + x))
                else:
                    new_state[y][x] = '.'

            else:
                if adjacent_bugs in (1, 2):
                    new_state[y][x] = '#'
                    power_representation.append(2**(y * 5 + x))
                else:
                    new_state[y][x] = '.'

    tiles = deepcopy(new_state)

    power_representation = tuple(power_representation)
    if power_representation in previous_states:
        break
    previous_states.add(power_representation)

# Answer One
print("Biodiversity rating:", sum(power_representation))

tiles = {}
for y in range(5):
    for x in range(5):
        if (x, y) == (2, 2):
            continue
        tiles[(0, x, y)] = original_tiles[y][x]

next_state = {}
for second in range(200):

    for l in (-(second + 1), second + 1):
        for y in range(5):
            for x in range(5):
                if (x,y) == (2, 2):
                    continue
                tiles[(l, x, y)] = '.'

    for coords, tile in tiles.items():
        level, x, y = coords

        if x == 2 and y == 2:
            continue

        neighbours = {
            'up': (x, y - 1), 'down': (x, y + 1),
            'left': (x - 1, y), 'right': (x + 1, y)
        }

        adjacent_bugs = 0
        for direction, next_to_coord in neighbours.items():

            col, row = next_to_coord

            if col in (-2, 6) or row in (-2, 6):
                continue

            if row == -1:
                if tiles.get((level - 1, 2, 1), '.') == '#':
                    adjacent_bugs += 1

            elif row == 5:
                if tiles.get((level - 1, 2, 3), '.') == '#':
                    adjacent_bugs += 1

            elif col == -1:
                if tiles.get((level - 1, 1, 2), '.') == '#':
                    adjacent_bugs += 1

            elif col == 5:
                if tiles.get((level - 1, 3, 2)) == '#':
                    adjacent_bugs += 1

            elif col == 2 and row == 2:

                if direction == 'down':
                    for recursive_x in range(5):
                        if tiles.get((level + 1, recursive_x, 0), ',') == '#':
                            adjacent_bugs += 1

                elif direction == 'up':
                    for recursive_x in range(5):
                        if tiles.get((level + 1, recursive_x, 4), '.') == '#':
                            adjacent_bugs += 1

                elif direction == 'right':
                    for recursive_y in range(5):
                        if tiles.get((level + 1, 0, recursive_y), '.') == '#':
                            adjacent_bugs += 1

                elif direction == 'left':
                    for recursive_y in range(5):
                        if tiles.get((level + 1, 4, recursive_y), '.') == '#':
                            adjacent_bugs += 1

            elif tiles.get((level, col, row), '.') == '#':
                adjacent_bugs += 1

        if tile == '#':
            if adjacent_bugs == 1:
                next_state[coords] = '#'
            else:
                next_state[coords] = '.'

        else:
            if adjacent_bugs in (1, 2):
                next_state[coords] = '#'
            else:
                next_state[coords] = '.'

    tiles = deepcopy(next_state)

bugs = 0
for coords, tile_value in tiles.items():
    if tile_value == '#':
        bugs += 1

# Answer Two
print("Bugs present after 200 seconds:", bugs)
