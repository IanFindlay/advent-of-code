"""Advent of Code 2019 Day 10 - Monitoring Station."""

import math


with open("input.txt", "r") as f:
    space = [list(row) for row in f.read().strip().split('\n')]

space_dict = {}
y = 0
for row in space:
    x = 0
    for col in row:
        value = space[y][x]
        if value == '#':
            space_dict[(x, y)] = space[y][x]
        x += 1
    y += 1

detection_dict = {}
for coords, value in space_dict.items():
    los = []
    for location, item in space_dict.items():
        if location == coords:
            continue
        x , y = location
        dx = x - coords[0]
        dy = y - coords[1]
        angle = math.atan2(dx,dy)

        los.append(angle)

    detection_dict[coords] = los

most_detected = None
for asteroid, inline in detection_dict.items():
    num_detected = len(set(inline))
    if not most_detected or num_detected > most_detected[1]:
        most_detected = (asteroid, num_detected)

# Answer One
print("Other asteroids detected from the best location:", most_detected)

