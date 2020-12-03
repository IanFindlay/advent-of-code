#!/usr/bin/env python3

"""Advent of Code 2020 Day 03 - Toboggan Trajectory."""


with open ('input.txt', 'r') as password_database:
    rows = [line for line in password_database.readlines()]

index_of_last_row = len(rows) - 1
index_of_last_col = len(rows[0]) - 1

y = x = 0
trees = 0
while y <= index_of_last_row:
    if rows[y][x] == "#":
        trees += 1

    y += 1
    x = (x + 3) % index_of_last_col

# Answer One
print("Number of trees encountered on right 3 down 1 slope:", trees)
