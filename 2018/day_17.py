"""Advent of Code Day 17 - Reservoir Research"""

import re


def hit_block(start):
    """Work out if water is settled or not, update active/scan."""
    y, x = start
    # Check left
    left_x = x - 1
    checked = [start]
    settled = True
    while True:

        if scan[(y+1, left_x)] == '.':
            scan[(y, left_x)] = '|'
            active_water.append((y, left_x))
            settled = False
            break

        # Hits unsettled water
        if scan[(y+1, left_x)] == '|':
            settled = False
            break

        # Contained side
        elif scan[(y, left_x)] == '#':
            break

        checked.append((y, left_x))
        left_x -= 1

    # Check right
    right_x = x + 1
    while True:

        if scan[(y+1, right_x)] == '.':
            scan[(y, right_x)] = '|'
            active_water.append((y, right_x))
            settled = False
            break

        # Hits unsettled water
        if scan[(y+1, right_x)] == '|':
            settled = False
            break

        # Contained side
        elif scan[(y, right_x)] == '#':
            break

        checked.append((y, right_x))
        right_x += 1

    # Update original tile and append new source if original is settled
    if settled:
        scan[start] = '~'
        active_water.append((y-1, x))

    # Mark all checked tiles
    for tile in checked:
        if settled:
            scan[tile] = '~'
        else:
            scan[tile] = '|'


# Parse input
with open('inputs/day_17.txt') as f:
    lines = [x.strip() for x in f.readlines()]

max_y, min_y = 0, 1000
max_x, min_x = 0, 1000
vein_regex = re.compile(r'(x|y)=(\d+), (x|y)=(\d+)..(\d+)')
clay = set()
for line in lines:
    vein = vein_regex.search(line)
    first = (vein.group(1), vein.group(2))
    second = (vein.group(3), vein.group(4))
    end = int(vein.group(5))

    if first[0] == 'x':
        coords = (int(second[1]), int(first[1]))
    else:
        coords = (int(first[1]), int(second[1]))

    clay.add(coords)

    # Process spread values
    if second[0] == 'x':
        for i in range(coords[1] + 1, end + 1):
            clay.add((coords[0], i))

    if second[0] == 'y':
        for i in range(coords[0] + 1, end + 1):
            clay.add((i, coords[1]))

    if coords[0] > max_y:
        max_y = coords[0]
    if coords[0] < min_y:
        min_y = coords[0]
    if coords[1] > max_x:
        max_x = coords[1]
    if coords[1] < min_x:
        min_x = coords[1]

# Make dictionary representing scan
scan = {}
for y in range(max_y + 1):
    for x in range(min_x - 1, max_x + 1):
        if (y, x) in clay:
            scan[(y, x)] = '#'
        else:
            scan[(y, x)] = '.'

scan[(0, 500)] = '+'

active_water = [(0, 500)]
while active_water:
    y, x = active_water.pop()

    # Down as far as able
    down_y = y + 1
    while True:

        # Check not out of range
        if down_y > max_y:
            break

        below = scan[(down_y, x)]
        if below == '.':
            scan[(down_y, x)] = '|'
            down_y += 1

        elif below in ('#', '~'):
            hit_block((down_y - 1, x))
            break

        else:
            break

in_reach = 0
permanent = 0
for tile, value in scan.items():
    if value in ('~', '|') and tile[0] >= min_y:
        in_reach += 1
    if value == '~':
        permanent += 1

# Answer One
print("Tiles reached by water:", in_reach)


# Answer Two
print("Permanent water tiles:", permanent)
