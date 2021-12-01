#!/usr/bin/env python3

"""Advent of Code 2021 Day 01 - Sonar Sweep"""


with open('inputs/day_01.txt', 'r') as readings:
    depths = [int(number.strip()) for number in readings.readlines()]

increased = sum([1 for i in range(1, len(depths)) if depths[i] > depths[i-1]])

# Answer One
print("Number of times the depth increases:", increased)


increased = sum([1 for i in range(1, len(depths)) if depths[i] > depths[i-3]])

# Answer Two
print("Number of times the sliding window increases:", increased)
