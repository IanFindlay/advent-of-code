"""Advent of Code 2020 Day 01 - Report Repair."""


with open ('input.txt', 'r') as f:
    entries = set([int(entry) for entry in f.readlines()])

for entry in entries:
    if 2020 - entry in entries:
        answer_one = entry * (2020 - entry)
        break

# Answer One
print("Two entries that add to 2020", answer_one)

for entry in entries:
    target = 2020 - entry
    for entry_2 in entries:
        answer_two = False
        if entry_2 == entry:
            pass
        if target - entry_2 in entries:
            answer_two = entry * entry_2 * (target - entry_2)
            break

    if answer_two:
        break

# Answer Two
print("Three entries that add to 2020", answer_two)
