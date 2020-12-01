#!/usr/bin/env python3

"""Advent of Code 2020 Day 01 - Report Repair."""


with open ('input.txt', 'r') as expense_report:
    entries = set([int(line) for line in expense_report.readlines()])

for entry in entries:
    if 2020 - entry in entries:
        answer_one = entry * (2020 - entry)
        break

# Answer One
print("Product of the two entries that add to 2020:", answer_one)

answer_two = False
for entry in entries:
    remaining_amount = 2020 - entry
    for entry_two in entries:
        if remaining_amount - entry_two in entries and entry_two != entry:
            answer_two = entry * entry_two * (remaining_amount - entry_two)
            break

    if answer_two:
        break

# Answer Two
print("Product of the three entries that add to 2020:", answer_two)
