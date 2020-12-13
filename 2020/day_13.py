#!/usr/bin/env python3

"""Advent of Code 2020 Day 13 - Shuttle Search."""


with open ('input.txt', 'r') as f:
    rows = [row.strip() for row in f.readlines()]

earliest_depart = int(rows[0])
bus_ids = [int(x) for x in rows[1].split(',') if x != "x"]

closest_departure = None
for bus_id in bus_ids:
    departure_time = bus_id
    while departure_time < earliest_depart:
            departure_time += bus_id

    if closest_departure is None or departure_time < closest_departure[0]:
        closest_departure = (departure_time, bus_id)

# Answer One
print("Product of bus ID and wait:",
      (closest_departure[0] - earliest_depart) * closest_departure[1])
