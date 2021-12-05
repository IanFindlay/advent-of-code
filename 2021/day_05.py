#!/usr/bin/env python3

"""Advent of Code 2021 Day 5 - Hydrothermal Venture"""


import re


with open('inputs/day_05.txt', 'r') as aoc_input:
    lines = [re.findall(r'(\d*),(\d*)', x) for x in aoc_input.readlines()]
    lines = [[(int(x), int(y)) for x, y in tup] for tup in lines]

coords_dict = {}
for line in lines:
    current_x, current_y = line[0]
    end_x, end_y = line[1]
    initial_x = current_x  # Needed for column loop entering logic

    if current_y == end_y:

        while True:
            coords = (current_x, current_y)
            if coords_dict.get(coords, '.') == '.':
                coords_dict[coords] = 1
            else:
                coords_dict[coords] += 1

            if current_x == end_x:
                break

            current_x += 1 if current_x < end_x else -1

    if initial_x == end_x:

        while True:
            coords = (current_x, current_y)
            if coords_dict.get(coords, '.') == '.':
                coords_dict[coords] = 1
            else:
                coords_dict[coords] += 1

            if current_y == end_y:
                break

            current_y += 1 if current_y < end_y else -1

dangerous_zones = sum([1 if x > 1 else 0 for x in coords_dict.values()])

# Answer One
print("Number of dangerous zones:", dangerous_zones)

for line in lines:
    current_x, current_y = line[0]
    end_x, end_y = line[1]

    # Already been processed in part one
    if current_x == end_x or current_y == end_y:
        continue

    while True:
        coords = (current_x, current_y)
        if coords_dict.get(coords, '.') == '.':
            coords_dict[coords] = 1
        else:
            coords_dict[coords] += 1

        if current_x == end_x:
            break

        current_x += 1 if current_x < end_x else -1

        current_y += 1 if current_y < end_y else -1

dangerous_zones = sum([1 if x > 1 else 0 for x in coords_dict.values()])

# Answer Two
print("Number of dangerous zones including diagonals:", dangerous_zones)
