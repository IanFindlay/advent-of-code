#!/usr/bin/env python3

"""Advent of Code 2021 Day 9 - Smoke Basin"""


with open('inputs/day_09.txt', 'r') as aoc_input:
    lines = [line.strip() for line in aoc_input.readlines()]

height_map = {}
for y, column in enumerate(lines):
    for x, row in enumerate(column):
        height_map[(x, y)] = int(row)

low_points = 0
for coords, height in height_map.items():
    x, y = coords
    adjacent = ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
    lowest = True
    for neighbour in adjacent:
        if height_map.get(neighbour, 10) <= height:
            lowest = False
            break

    if lowest:
        low_points += height + 1

# Answer One
print("Sum of risk levels of low points", low_points)
