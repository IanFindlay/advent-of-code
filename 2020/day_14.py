#!/usr/bin/env python3

"""Advent of Code 2020 Day 14 - Docking Data."""

import re

with open ('input.txt', 'r') as f:
    rows = [row.strip() for row in f.readlines()]

memory = {}
instruction_regex = re.compile('mem\[(\d*)\]\s=\s(\d*)')
for row in rows:
    if row.startswith('mask'):
        mask = row.split()[2]
    else:
        mem, value = instruction_regex.findall(row)[0]
        value = format(int(value), '036b')
        masked_value = ''
        for index, bit in enumerate(mask):
            if bit == 'X':
                masked_value += value[index]
            else:
                masked_value += bit

        memory[mem] = int(masked_value, 2)

# Answer One
print("Sum of all values left in memory after initialisation:",
      sum(memory.values()))
