#!/usr/bin/env python3

"""Advent of Code 2021 Day 25 - Sea Cucumber"""


with open('inputs/day_25.txt', 'r') as aoc_input:
    lines = [line.strip() for line in aoc_input.readlines()]

east_cucumbers = set()
south_cucumbers = set()
for y, row in enumerate(lines):
    for x, value in enumerate(row):
        if value == '>':
            east_cucumbers.add((x, y))
        elif value == 'v':
            south_cucumbers.add((x, y))

steps = 0
while True:
    new_east = set()
    new_south = set()

    for coords in east_cucumbers:

        x, y = coords
        forward_x = (x + 1) % len(lines[0])
        forward = (forward_x, y)

        if forward not in east_cucumbers and forward not in south_cucumbers:
            new_east.add(forward)
        else:
            new_east.add(coords)

    for coords in south_cucumbers:

        x, y = coords
        forward_y = (y + 1) % len(lines)
        forward = (x, forward_y)

        if forward not in new_east and forward not in south_cucumbers:
            new_south.add(forward)
        else:
            new_south.add(coords)

    steps += 1
    if new_east == east_cucumbers and new_south == south_cucumbers:
        break

    east_cucumbers = new_east
    south_cucumbers = new_south

# Answer One
print(f'First step on which no sea cucumbers move: {steps}')
