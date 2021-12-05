#!/usr/bin/env python3

"""Advent of Code 2021 Day 3 - Binary Diagnostic"""


def convert_to_columns(binary_values):
    """Takes list of strings and returns one with rows and columns swapped."""
    column_conversion = []
    for row_num in range(len(binary_values[0])):
        column_conversion.append('')
        for col_num in range(len(binary_values)):
            column_conversion[-1] += binary_values[col_num][row_num]

    return column_conversion


with open('inputs/day_03.txt', 'r') as aoc_input:
    input_lines = [line.strip() for line in aoc_input.readlines()]

binary_columns = convert_to_columns(input_lines)
gamma = ''
for column in binary_columns:
    if column.count('0') > len(column) / 2:
        gamma += '0'
    else:
        gamma += '1'

epsilon = ''.join(map(lambda bit: '1' if bit == '0' else '0', gamma))

# Answer One
print("Submarine power consumption:", int(gamma, 2) * int(epsilon, 2))

oxy_binaries = input_lines.copy()
oxy_columns = binary_columns.copy()
oxy_criteria = ''
i = 0
while len(oxy_binaries) > 1:
    if oxy_columns[i].count('1') >= len(oxy_columns[i]) / 2:
        oxy_criteria += '1'
    else:
        oxy_criteria += '0'

    oxy_binaries = list(filter(
            lambda binary: binary.startswith(oxy_criteria), oxy_binaries
            )
        )
    oxy_columns = convert_to_columns(oxy_binaries)

    i += 1

co2_binary = input_lines.copy()
co2_columns = binary_columns.copy()
co2_criteria = ''
i = 0
while len(co2_binary) > 1:
    if co2_columns[i].count('1') >= len(co2_columns[i]) / 2:
        co2_criteria += '0'
    else:
        co2_criteria += '1'

    co2_binary = list(filter(
            lambda binary: binary.startswith(co2_criteria), co2_binary
            )
        )
    co2_columns = convert_to_columns(co2_binary)

    i += 1

# Answer Two
print("Submarine life support rating:",
      int(oxy_binaries[0], 2) * int(co2_binary[0], 2))
