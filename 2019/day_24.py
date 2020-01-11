"""Advent of Code 2019 Day 24 - Planet of Discord."""

from copy import deepcopy


with open('input.txt') as f:
    tiles = [list(line) for line in f.read().split()]

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
print(sum(power_representation))
