#!/usr/bin/env python3

"""Advent of Code 2021 Day 6 - Lanternfish"""


with open('inputs/day_06.txt','r') as aoc_input:
    lanternfish = [int(x) for x in aoc_input.read().split(',')]

lanternfish_copy = lanternfish.copy()

for n in range(80):
    lanternfish = [x - 1 for x in lanternfish]

    i = len(lanternfish) - 1
    while i >= 0:
        if lanternfish[i] == -1:
            lanternfish[i] = 6
            lanternfish.append(8)

        i -= 1

# Answer One
print("Number of Lanternfish after 80 days:", len(lanternfish))

lanternfish_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
for fish in lanternfish_copy:
    lanternfish_dict[fish] += 1

for n in range(256):
    new_fish_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for key in lanternfish_dict.keys():
        new_fish_dict[key - 1] = lanternfish_dict[key]

    for key in new_fish_dict:
        if key == -1:
            new_fish_dict[8] = new_fish_dict[-1]
            new_fish_dict[6] += new_fish_dict[-1]

    lanternfish_dict = new_fish_dict
    del lanternfish_dict[-1]

# Answer Two
print("Number of Lanternfish after 256 days:", sum(lanternfish_dict.values()))
