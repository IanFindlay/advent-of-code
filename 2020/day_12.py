#!/usr/bin/env python3

"""Advent of Code 2020 Day 12 - Rain Risk."""


with open ('inputs/2020_12.txt', 'r') as f:
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

coords = [0, 0]
waypoint = [1, 10]
for instruction in instructions:
    action = instruction[0]
    value = int(instruction[1:])

    if action == 'N':
        waypoint[0] += value
    elif action == 'S':
        waypoint[0] -= value
    elif action == 'E':
        waypoint[1] += value
    elif action == 'W':
        waypoint[1] -= value
    elif action == 'L':
        for n in range(value // 90):
            new_waypoint = [None, None]
            new_waypoint[1] = -waypoint[0]
            new_waypoint[0] = waypoint[1]
            waypoint = new_waypoint
    elif action == 'R':
        for n in range(value // 90):
            new_waypoint = [None, None]
            new_waypoint[1] = waypoint[0]
            new_waypoint[0] = -waypoint[1]
            waypoint = new_waypoint
    elif action == 'F':
        coords = [coords[0] + waypoint[0] * value,
                  coords[1] + waypoint[1] * value]

# Answer Two
print("Actual Manhattan distance from starting point:",
      sum([abs(coord) for coord in coords]))
