#!/usr/bin/env python3

"""Advent of Code 2020 Day 06 - Custom Customs."""


with open ('input.txt', 'r') as forms:
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
    group_yes = set()
    set_initialised = False
    for member_yes in group.split('\n'):
        member_yes_set = set([char for char in member_yes])

        if not set_initialised:
            group_yes = member_yes_set
            set_initialised = True
        else:
            group_yes = member_yes_set.intersection(group_yes)

    overall_group_yes += len(group_yes)

# Answer Two
print("Sum of all group overall yes counts:", overall_group_yes)
