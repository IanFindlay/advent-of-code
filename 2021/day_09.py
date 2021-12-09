#!/usr/bin/env python3

"""Advent of Code 2021 Day 9 - Smoke Basin"""


with open('inputs/day_09.txt', 'r') as aoc_input:
    rows = [line.strip() for line in aoc_input.readlines()]

height_map = {}
for y, row in enumerate(rows):
    for x, height in enumerate(row):
        height_map[(x, y)] = int(height)

low_points = []
low_points_sum = 0
for coords, height in height_map.items():
    x, y = coords
    adjacent = ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
    lowest = True
    for neighbour in adjacent:
        if height_map.get(neighbour, 10) <= height:
            lowest = False
            break

    if lowest:
        low_points.append(coords)
        low_points_sum += height + 1

# Answer One
print("Sum of risk levels of low points:", low_points_sum)

basin_sizes = []
for low_point in low_points:
    part_of_basin = set([low_point])

    coords_to_check_stack = [low_point]
    while coords_to_check_stack:
        x, y = coords_to_check_stack.pop()
        adjacent = ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
        for neighbour in adjacent:
            neighbour_height = height_map.get(neighbour, 0)
            if neighbour_height > height_map[(x, y)] and neighbour_height != 9:
                part_of_basin.add(neighbour)
                coords_to_check_stack.append(neighbour)

    basin_sizes.append(len(part_of_basin))

basin_sizes.sort(reverse=True)

largest_three_product = 1
for size in basin_sizes[:3]:
    largest_three_product *= size

# Answer Two
print("Product of three largest basin sizes:", largest_three_product)
