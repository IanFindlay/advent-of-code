#!/usr/bin/env python3

"""Advent of Code 2021 Day 01 - Sonar Sweep"""


with open('inputs/day_01.txt', 'r') as readings:
    depths = [int(number.strip()) for number in readings.readlines()]

increases = 0
previous = depths[0]
for depth in depths[1:]:
    if depth > previous:
        increases += 1

    previous = depth

# Answer One
print("Number of times the depth increases:", increases)

increases = 0
previous = sum(depths[0:3])
for index, depth in enumerate(depths[1:]):
    depth_window_sum = sum(depths[index: index + 3])
    if depth_window_sum > previous:
        increases += 1

    previous = depth_window_sum

# Answer Two
print("Number of times the sliding window increases:", increases)
