#!/usr/bin/env python3

"""Advent of Code 2021 Day 05 - Hydrothermal Venture"""


import re

with open('inputs/day_05.txt', 'r') as aoc_input:
    lines = [re.findall(r'(\d*),(\d*)', x) for x in aoc_input.readlines()]

coords_dict = {}
for line in lines:
    x_coords, y_coords = zip(line[0], line[1])
    x_coords = [int(x) for x in x_coords]
    y_coords = [int(x) for x in y_coords]

    start_x = min(x_coords)
    end_x = max(x_coords)
    start_y = min(y_coords)
    end_y = max(y_coords)

    current_x = start_x
    current_y = start_y

    while current_x <= end_x:

        if start_y != end_y:
            break

        coords = (current_x, current_y)

        coord_value = coords_dict.get(coords, '.')

        if coord_value == '.':
            coords_dict[coords] = 1
        else:
            coords_dict[coords] += 1

        current_x += 1

    current_x = start_x

    while current_y <= end_y:

        if start_x != end_x:
            break

        coords = (current_x, current_y)

        coord_value = coords_dict.get(coords, '.')

        if coord_value == '.':
            coords_dict[coords] = 1
        else:
            coords_dict[coords] += 1

        current_y += 1

dangerous_zones = 0
for coords, value in coords_dict.items():
    if value > 1:
        dangerous_zones += 1

# Answer One
print("Number of dangerous zones:", dangerous_zones)

for line in lines:
    current_x = int(line[0][0])
    current_y = int(line[0][1])
    end_x = int(line[1][0])
    end_y = int(line[1][1])

    # Already been processed in part one
    if current_x == end_x or current_y == end_y:
        continue

    while True:
        coords = (current_x, current_y)
        coord_value = coords_dict.get(coords, '.')

        if coord_value == '.':
            coords_dict[coords] = 1
        else:
            coords_dict[coords] += 1

        if current_x == end_x:
            break

        if current_x < end_x:
            current_x += 1
        else:
            current_x -= 1

        if current_y < end_y:
            current_y += 1
        else:
            current_y -= 1


dangerous_zones = 0
for coords, value in coords_dict.items():
    if value > 1:
        dangerous_zones += 1

# Answer Two
print("Number of dangerous zones including diagonals:", dangerous_zones)
