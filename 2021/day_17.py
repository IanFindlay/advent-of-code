#!/usr/bin/env python3

"""Advent of Code 2021 Day 17 - Trick Shot"""

import re


def take_shot(x_vel, y_vel, x_max, y_min, target_area_coords):
    probe_x, probe_y = (0, 0)
    while True:
        probe_x += x_vel
        probe_y += y_vel
        if (probe_x, probe_y) in target_area_coords:
            return True

        if x_vel != 0:
            x_vel -= 1 if x_vel > 0 else -1

        y_vel -= 1

        if probe_y < y_min or probe_x > x_max:
            return False


with open('inputs/day_17.txt', 'r') as aoc_input:
    target_area_regex = r'x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)'
    target_area = re.findall(target_area_regex, aoc_input.read())

x_min, x_max, y_min, y_max = (int(x) for x in target_area[0])
target_area_coords = set()
y = y_min
while y <= y_max:
    x = x_min
    while x <= x_max:
        target_area_coords.add((x, y))
        x += 1
    y += 1

hits = []
x_vel = 0
while x_vel <= x_max:

    y_vel = abs(y_min)
    while y_vel >= y_min:
        shot = take_shot(x_vel, y_vel, x_max, y_min, target_area_coords)
        if shot:
            hits.append((x_vel, y_vel))

        y_vel -= 1

    x_vel += 1

hits.sort(key=lambda x: x[1])
max_height = sum(range(1, hits[-1][1] + 1))

# Answer One
print("Highest y position reached:", max_height)

# Answer Two
print("Number of initial velocity values that hit target area:", len(hits))
