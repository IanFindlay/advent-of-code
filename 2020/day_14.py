#!/usr/bin/env python3

"""Advent of Code 2020 Day 14 - Docking Data."""

from itertools import product
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

memory = {}
instruction_regex = re.compile('mem\[(\d*)\]\s=\s(\d*)')
for row in rows:
    if row.startswith('mask'):
        mask = row.split()[2]
    else:
        mem, value = instruction_regex.findall(row)[0]
        mem = format(int(mem), '036b')
        masked_mem = ''
        for index, bit in enumerate(mask):
            if bit == '0':
                masked_mem += mem[index]
            else:
                masked_mem += bit

        x_count = masked_mem.count('X')
        for floats in product(('0', '1'), repeat=x_count):
            floats = list(floats)
            float_mem = ''
            for bit in masked_mem:
                if bit == 'X':
                    float_mem += floats.pop()
                else:
                    float_mem += bit

            memory[int(float_mem, 2)] = int(value)

# Answer Two
print("Sum of all values left in memory after Version 2 initialisation:",
      sum(memory.values()))
