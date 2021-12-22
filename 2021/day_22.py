#!/usr/bin/env python3

"""Advent of Code 2021 Day 22 - Reactor Reboot"""


import re


with open('inputs/day_22.txt', 'r') as aoc_input:
    steps = [step.strip() for step in aoc_input.readlines()]

coord_range_regex = re.compile(r'-?\d+')
reactor_core = set()
for step in steps:
    state = step.split(' ')[0]
    coord_ranges = coord_range_regex.findall(step)
    coord_ranges = [int(x) for x in coord_ranges]
    x_min, x_max, y_min, y_max, z_min, z_max = coord_ranges

    if x_max < -50 or x_min > 50:
        continue
    if y_max < -50 or y_min > 50:
        continue
    if z_max < -50 or z_min > 50:
        continue

    coord_ranges = [50 if x > 50 else x for x in coord_ranges]
    coord_ranges = [-50 if x < -50 else x for x in coord_ranges]
    x_min, x_max, y_min, y_max, z_min, z_max = coord_ranges

    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            for z in range(z_min, z_max + 1):

                if state == 'on':
                    reactor_core.add((x, y, z))
                else:
                    if (x, y, z) in reactor_core:
                        reactor_core.remove((x, y, z))

# Answer One
print(f'Cubes on: {len(reactor_core)}')
