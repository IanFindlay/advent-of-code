""" Advent of Code Day 8 - Two-Factor Authentication"""

import re


with open('inputs/day_08.txt') as f:
    sequence = [line.strip() for line in f.readlines()]

grid = []
for i in range(6):
    row = []
    for j in range(50):
        row.append('.')
    grid.append(row)

for instruction in sequence:
    if 'rect' in instruction:
        size = re.search(r'(\d+)x(\d+)', instruction)
        width, height = int(size.group(1)), int(size.group(2))
        for i in range(height):
            for j in range(width):
                grid[i][j] = '#'

    elif 'row' in instruction:
        parse = re.search(r'y=(\d+) by (\d+)', instruction)
        row, pixels = int(parse.group(1)), int(parse.group(2))
        for i in range(pixels):
            grid[row].insert(0, grid[row].pop(-1))


    elif 'column' in instruction:
        parse = re.search(r'x=(\d+) by (\d+)', instruction)
        col, pixels = int(parse.group(1)), int(parse.group(2))

        state_list = []
        for row in grid:
            state_list.append(row[col])
        for i in range(pixels):
            state_list.insert(0, state_list.pop(-1))
        for i in range(len(grid)):
            grid[i][col] = state_list[i]

on = 0
for row in grid:
    for col in row:
        if col == '#':
            on += 1

# Answer One
print("Number of Lights On:", on)

# Answer Two
for row in grid:
    print(row)
