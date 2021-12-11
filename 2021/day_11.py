#!/usr/bin/env python3

"""Advent of Code 2021 Day 11 - Dumbo Octopus"""

def print_octopi():
    for y, row in enumerate(lines):
        row_str = ''
        for x, _ in enumerate(row):
            row_str += str(octopi[(x, y)])
        print(row_str)

with open('inputs/day_11.txt', 'r') as aoc_input:
    lines = [line.strip() for line in aoc_input.readlines()]

octopi = {}
for y, row in enumerate(lines):
    for x, level in enumerate(row):
        octopi[(x, y)] = int(level)

num_flashes = 0
for _ in range(100):

    flashed = set()
    for coords, level in octopi.items():
        octopi[coords] = level + 1

    for coords, level in octopi.items():
        if level > 9 and coords not in flashed:
            flashed.add(coords)

            to_flash = [coords]
            while to_flash:
                x, y = to_flash.pop()
                adjacent = [
                        (x + 1, y), (x - 1, y), (x + 1, y + 1), (x - 1, y - 1),
                        (x, y + 1), (x, y - 1), (x + 1, y - 1), (x - 1, y + 1)
                ]

                for next_to in adjacent:
                    if octopi.get(next_to, None):
                        octopi[next_to] += 1

                        if octopi[next_to] > 9 and next_to not in flashed:
                            flashed.add(next_to)
                            to_flash.append(next_to)


    for coords in flashed:
        octopi[coords] = 0
        num_flashes += 1

# Answer One
print("Total flashes after 100 steps:", num_flashes)
