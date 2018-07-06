"""Advent of Code Day 12 - JSAbacusFramework.io"""

import re

with open('input.txt') as f:
    document = f.read()

# Part One
numbers = re.findall(r'-?[0-9]+', document)

total = 0
for number in numbers:
    total += int(number)

print("Sum =", total)

# TODO Part Two - Regex won't work need to think of another approach - json?
