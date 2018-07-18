"""Advent of Code Day 22 - Grid Computing"""

import re


with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()[2:]]

viable = 0
for node in data:
    used = int(re.search(r'T\s+(\d+)T', node).group(1))
    if used == 0:
        continue

    for comp_node in data:
        avail = int(re.search(r'(\d+)T\s+\d+%', comp_node).group(1))
        if avail >= used and comp_node != node:
            viable += 1

# Answer One
print("Viable pairs:", viable)

# Part Two - Forming the structure and completing by hand seemed the best way after
#  printing out the viable pairs and realising this was a large sliding tile problem

structure = []
i = 0
while i < 24:
    row = []
    j = 0
    while j < len(data):
        node_regex = re.search(r'x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T', data[i + j])
        if node_regex.group(1) == '0' and node_regex.group(2) == '0':
            marker = '!'
        elif node_regex.group(1) == '37' and node_regex.group(2) == '0':
            marker = 'G'
        elif len(node_regex.group(3)) == 3:
            marker = '#'
        elif node_regex.group(4) == '0':
            marker = '_'
        else:
            marker = '.'
        row.append(marker)
        j += 24

    structure.append(row)
    i += 1

with open('output.txt', 'w') as f:

    for row in structure:
        f.write(''.join(row) + '\n')
