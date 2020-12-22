"""Advent of Code Day 15 - Science for Hungry People"""

import re


with open('inputs/day_15.txt') as f:
    info = f.readlines()

nutri_info = []
for ingredient in info:
    capacity = int(re.search(r'capacity ([0-9-]+)', ingredient).group(1))
    durability = int(re.search(r'durability ([0-9-]+)', ingredient).group(1))
    flavor = int(re.search(r'flavor ([0-9-]+)', ingredient).group(1))
    texture = int(re.search(r'texture ([0-9-]+)', ingredient).group(1))
    calories = int(re.search(r'calories ([0-9-]+)', ingredient).group(1))

    nutri_info.append([capacity, durability, flavor, texture, calories])

ratios = []
for sugar in range(0, 101):
    for sprinkles in range(0, 101 - sugar):
        for candy in range(0, 101 - sprinkles - sugar):

            chocolate = 100 - (sugar + sprinkles + candy)
            ratios.append([sugar, sprinkles, candy, chocolate])


highest = 0
for ratio in ratios:

    capacity = (ratio[0] * nutri_info[0][0] + ratio[1] * nutri_info[1][0]
    + ratio[2] * nutri_info[2][0] + ratio[3] * nutri_info[3][0])

    durability = (ratio[0] * nutri_info[0][1] + ratio[1] * nutri_info[1][1]
    + ratio[2] * nutri_info[2][1] + ratio[3] * nutri_info[3][1])

    flavor = (ratio[0] * nutri_info[0][2] + ratio[1] * nutri_info[1][2]
    + ratio[2] * nutri_info[2][2] + ratio[3] * nutri_info[3][2])

    texture = (ratio[0] * nutri_info[0][3] + ratio[1] * nutri_info[1][3]
    + ratio[2] * nutri_info[2][3] + ratio[3] * nutri_info[3][3])

    calories = (ratio[0] * nutri_info[0][4] + ratio[1] * nutri_info[1][4]
    + ratio[2] * nutri_info[2][4] + ratio[3] * nutri_info[3][4])

    if capacity <= 0 or durability <= 0 or flavor <= 0 or texture <= 0:
        continue

    if calories != 500:    # Comment out for Part One
        continue

    score = capacity * durability * flavor * texture

    if score > highest:
        highest = score

print("Highest Cookie Score =", highest)
