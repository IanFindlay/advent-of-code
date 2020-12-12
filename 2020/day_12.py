#!/usr/bin/env python3

"""Advent of Code 2020 Day 12 - Rain Risk."""


with open ('input.txt', 'r') as f:
    instructions = [row.strip() for row in f.readlines()]

coords = [0, 0]
directions = {0: 'E', 1: 'S', 2: 'W', 3: 'N'}
current_direction = 0
for instruction in instructions:
    action = instruction[0]
    value = int(instruction[1:])

    if action == 'N':
        coords[0] += value
    elif action == 'S':
        coords[0] -= value
    elif action == 'E':
        coords[1] += value
    elif action == 'W':
        coords[1] -= value
    elif action == 'L':
        current_direction = (current_direction - (value / 90)) % 4
    elif action == 'R':
        current_direction = (current_direction + (value / 90)) % 4
    elif action == 'F':
        facing = directions[current_direction]
        if facing == 'N':
            coords[0] += value
        elif facing == 'S':
            coords[0] -= value
        elif facing == 'E':
            coords[1] += value
        elif facing == 'W':
            coords[1] -= value

# Answer One
print("Manhattan distance from starting point:",
      sum([abs(coord) for coord in coords]))
