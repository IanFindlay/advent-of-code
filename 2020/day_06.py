#!/usr/bin/env python3

"""Advent of Code 2020 Day 06 - Custom Customs."""


with open ('inputs/day_06.txt', 'r') as forms:
    groups = [group_answers.strip() for group_answers in forms.read().split('\n\n')]

overall_yes = 0
for group in groups:
    group_yes = set()
    for member_yes in group.split('\n'):
        for char in member_yes:
            group_yes.add(char)

    overall_yes += len(group_yes)

# Answer One
print("Sum of all groups yes counts:", overall_yes)

overall_group_yes = 0
for group in groups:
    members = group.split('\n')
    group_yes = set([char for char in members[0]])
    for member in members[1:]:
        group_yes = set([char for char in member]).intersection(group_yes)

    overall_group_yes += len(group_yes)

# Answer Two
print("Sum of all group overall yes counts:", overall_group_yes)
