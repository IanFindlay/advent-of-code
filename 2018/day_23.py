"""Advent of Code Day 23 - Experimental Emergency Teleportation"""

import collections
import re


with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]

nano_regex = re.compile(r'<(-?\d+),(-?\d+),(-?\d+)>,\s+r=(\d+)')
nanobots = {}
largest_radius = (0, (0, 0, 0))
for line in lines:
    x, y, z, radius = [int(x) for x in nano_regex.search(line).groups()]
    nanobots[(x, y, z)] = radius
    if radius > largest_radius[0]:
        largest_radius = (radius, (x, y, z))

radius, coords = largest_radius
in_range = 0
# Find how many nanobots are in range
for nanobot in nanobots:
    x, y, z = nanobot
    distance = abs(coords[0] - x) + abs(coords[1] - y) + abs(coords[2] - z)
    if distance <= radius:
        in_range += 1

# Answer One
print("Nanobots in range:", in_range)

# Part two - Can't think of a solution that would complete quickly enough
