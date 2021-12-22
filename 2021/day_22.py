#!/usr/bin/env python3

"""Advent of Code 2021 Day 22 - Reactor Reboot"""


import re


class Cuboid:

    def __init__(self, state, coord_ranges):
        self.state = state
        self.x_range = coord_ranges[0:2]
        self.y_range = coord_ranges[2:4]
        self.z_range = coord_ranges[4:6]

    def border(self, self_range, other_range):
        min_value = max(self_range[0], other_range[0])
        max_value = min(self_range[1], other_range[1])

        if max_value - min_value <= 0:
            return False

        return (min_value, max_value)

    def get_intersection_with(self, other_cuboid):
        new_x_range = self.border(self.x_range, other_cuboid.x_range)
        new_y_range = self.border(self.y_range, other_cuboid.y_range)
        new_z_range = self.border(self.z_range, other_cuboid.z_range)

        if not new_x_range or not new_y_range or not new_z_range:
            return False

        new_state =  0 if self.state else 1

        new_coord_ranges = []
        for coord_range in (new_x_range, new_y_range, new_z_range):
            for coord in coord_range:
                new_coord_ranges.append(coord)

        return Cuboid(new_state, new_coord_ranges)

    def get_size(self):
        x = self.x_range[1] - self.x_range[0] + 1
        y = self.y_range[1] - self.y_range[0] + 1
        z = self.z_range[1] - self.z_range[0] + 1

        return x * y * z if self.state else -x * y * z


with open('inputs/day_22.txt', 'r') as aoc_input:
    steps = [step.strip() for step in aoc_input.readlines()]

parsed_steps = []
coord_range_regex = re.compile(r'-?\d+')
for step in steps:
    state = step.split(' ')[0]
    state = 1 if state == 'on' else 0
    coord_ranges = coord_range_regex.findall(step)
    parsed_steps.append((state, [int(x) for x in coord_ranges]))

reactor_core = set()
for step in parsed_steps:
    state, coord_ranges = step
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

                if state:
                    reactor_core.add((x, y, z))
                else:
                    if (x, y, z) in reactor_core:
                        reactor_core.remove((x, y, z))

# Answer One
print(f'Cubes on: {len(reactor_core)}')

cuboids = []
for step in parsed_steps:
    state, coord_ranges = step
    cuboids.append(Cuboid(state, coord_ranges))

processed = [cuboids[0]]
for to_process in cuboids[1:]:

    for intersect_with in processed.copy():

        new_cuboid = intersect_with.get_intersection_with(to_process)
        if new_cuboid:
            processed.append(new_cuboid)

    if to_process.state:
        processed.append(to_process)

on_cubes = 0
for cuboid in processed:
    on_cubes += cuboid.get_size()

# Answer Two
print(f'Cubes on: {on_cubes}')
