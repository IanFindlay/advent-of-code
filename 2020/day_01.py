"""Advent of Code 2020 Day 01 - Report Repair."""


with open ('input.txt', 'r') as f:
    entries = set([int(entry) for entry in f.readlines()])

for entry in entries:
    if 2020 - entry in entries:
        answer_one = entry * (2020 - entry)
        break

# Answer One
print("Two entries that add to 2020", answer_one)
