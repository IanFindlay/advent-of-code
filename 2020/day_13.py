#!/usr/bin/env python3

"""Advent of Code 2020 Day 13 - Shuttle Search."""


with open ('inputs/2020_13.txt', 'r') as f:
    rows = [row.strip() for row in f.readlines()]

early_time = int(rows[0])
bus_ids = rows[1].split(',')

shortest_wait = None
for bus_id in [int(x) for x in bus_ids if x != 'x']:
    difference = ((early_time // bus_id + 1) * bus_id) - early_time
    if shortest_wait is None or difference < shortest_wait[0]:
        shortest_wait = (difference, bus_id)

# Answer One
print("Product of bus ID and wait:", shortest_wait[0] * shortest_wait[1])

time = 1
interval = 1
for index, bus in enumerate([int(x) if x != 'x' else 1 for x in bus_ids]):
    while True:
        if (time + index) % bus == 0:
            interval *= bus
            break
        time += interval

# Answer Two
print("Earliest time where bus departure offsets match their indicies:", time)
