"""Advent of Code Day 12 - JSAbacusFramework.io"""

import re
import json

with open('input.txt') as f:
    document = f.read()

# Part One
numbers = re.findall(r'-?[0-9]+', document)

total = 0
for number in numbers:
    total += int(number)

# Answer One
print("Sum =", total)


# Part Two
def no_red(obj):
    """Evaluate json objects adding numbers not in dicts containing "red"."""
    if type(obj) == int:
        return obj
    if type(obj) == list:
        return sum([no_red(item) for item in obj])
    if type(obj) == dict:
        if 'red' in obj.values():
            return 0
        return no_red(list(obj.values()))
    return 0


# Answer Two
print("Corrected Sum =", no_red(json.loads(document)))
