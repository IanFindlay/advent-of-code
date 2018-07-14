""" Advent of Code Day 3 - Squares With Three Sides"""

import re

def check_triangle(lengths):
    """Check if 3 lengths form a triangle - sum of smallest two > than other."""
    in_order = sorted([int(x) for x in lengths])
    smallest_sum = in_order[0] + in_order[1]
    if smallest_sum > in_order[2]:
        return True


with open('input.txt') as f:
    sides_list = [line.strip() for line in f.readlines()]

triangles = 0
for trio in sides_list:
    if check_triangle(re.findall(r'(\d+)', trio)):
        triangles += 1

# Answer Part One
print("Number of Valid Triangles =", triangles)


# Part Two
a = []
b = []
c = []
# Extract side lengths and group lines into three so real trios are lined up
i = 0
while i < len(sides_list):
    a.append(re.findall(r'(\d+)', sides_list[i]))
    b.append(re.findall(r'(\d+)', sides_list[i + 1]))
    c.append(re.findall(r'(\d+)', sides_list[i + 2]))

    i += 3

triangles = 0
i = 0
while i < len(a):
    j = 0
    while j < 3:
        if check_triangle([a[i][j], b[i][j], c[i][j]]):
            triangles += 1
        j += 1

    i += 1

# Answer Part Two
print("Number of Valid Vertical Triangles", triangles)
