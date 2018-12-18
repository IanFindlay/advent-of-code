"""Advent of Code Day 18 - Settlers of The North Pole"""


with open('input.txt') as f:
    rows = [[x for x in list(y.strip())] for y in f.readlines()]

area = {}
for i, row in enumerate(rows):
    for j, acre in enumerate(row):
        area[(i, j)] = acre

# Make minute to minute changes to area until its state repeats
previous = [area]
minutes = 0
while True:
    next_minute = {}
    for coords, acre in area.items():

        # Build list of acres next to current acre
        next_to = []
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if i == 0 and j == 0:
                    continue
                next_to.append(area.get((coords[0] + i, coords[1] + j), ''))

        if acre == '.':
            if next_to.count('|') >= 3:
                next_minute[coords] = '|'
            else:
                next_minute[coords] = '.'

        elif acre == '|':
            if next_to.count('#') >= 3:
                next_minute[coords] = '#'
            else:
                next_minute[coords] = '|'

        elif acre == '#':
            if next_to.count('#') > 0 and next_to.count('|') > 0:
                next_minute[coords] = '#'
            else:
                next_minute[coords] = '.'

    area = next_minute
    minutes += 1

    # Answer One
    if minutes == 10:
        wooded, lumber = 0, 0
        for acre in area.values():
            if acre == '|':
                wooded += 1
            elif acre == '#':
                lumber += 1

        print("After 10 minutes:", wooded * lumber)

    if area in previous:
        break
    previous.append(area)

# Find where period starts and its length to find state at 1000000000
repeat_index = previous.index(area)
period_length = minutes - repeat_index
after_repeat = 1000000000  % period_length
answer = previous[repeat_index + after_repeat]

# Answer Two
wooded, lumber = 0, 0
for acre in answer.values():
    if acre == '|':
        wooded += 1
    elif acre == '#':
        lumber += 1

# Answer Two
print("After many minutes:", wooded * lumber)
