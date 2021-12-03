#!/usr/bin/env python3

"""Advent of Code 2021 Day 03 - Binary Diagnostic"""


def convert_to_columns(binary_values):
    """."""
    column_conversion = []
    for row in range(len(binary_values[0])):
        column_conversion.append('')
        for column in range(len(binary_values)):
            column_conversion[-1] += binary_values[column][row]

    return column_conversion


with open('inputs/day_03.txt', 'r') as aoc_input:
    input_lines = [line.strip() for line in aoc_input.readlines()]

binary_columns = convert_to_columns(input_lines)
gamma = ''
for i in range(len(binary_columns)):
    if binary_columns[i].count('0') > len(binary_columns[i]) / 2:
        gamma += '0'
    else:
        gamma += '1'

epsilon = ''.join(['1' if bit == '0' else '0' for bit in gamma])

# Answer One
print("Submarine power consumption:", int(gamma, 2) * int(epsilon, 2))

oxygen_binary = input_lines.copy()
oxygen_columns = binary_columns.copy()
oxygen = ''
i = 0
while len(oxygen_binary) > 1:

    if oxygen_columns[i].count('1') >= len(oxygen_columns[i]) / 2:
        oxygen += '1'
    else:
        oxygen += '0'

    oxygen_binary = list(filter(
            lambda binary: binary.startswith(oxygen), oxygen_binary))

    oxygen_columns = convert_to_columns(oxygen_binary)

    i += 1

co2_binary = input_lines.copy()
co2_columns = binary_columns.copy()
co2 = ''
i = 0
while len(co2_binary) > 1:

    if co2_columns[i].count('1') >= len(co2_columns[i]) / 2:
        co2 += '0'
    else:
        co2 += '1'

    co2_binary = list(filter(
            lambda binary: binary.startswith(co2), co2_binary))

    co2_columns = convert_to_columns(co2_binary)

    i += 1

# Answer Two
print("Submarine life support rating:",
      int(oxygen_binary[0], 2) * int(co2_binary[0], 2))
