#!/usr/bin/env python3

"""Advent of Code 2020 Day 06 - Custom Customs."""


with open ('input.txt', 'r') as forms:
    groups = [group_answers for group_answers in forms.read().split('\n\n')]

overall_yes = 0
for group in groups:
    group_yes = set()
    for member_yes in group.split('\n'):
        for char in member_yes:
            group_yes.add(char)

    overall_yes += len(group_yes)

# Answer One
print("Sum of all groups yes counts:", overall_yes)
