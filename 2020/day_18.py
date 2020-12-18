#!/usr/bin/env python3

"""Advent of Code 2020 Day 18 - Operation Order."""


def do_maths(maths: list) -> int:
    """."""
    num_1 = None
    num_2 = None
    operation = None
    bracketed_start = None
    bracketed_end = None
    bracket_depth = 0
    for index, char in enumerate(maths):

        if char == '+':
            if not bracketed_start:
                operation = '+'
        elif char == '*':
            if not bracketed_start:
                operation = '*'

        elif char == '(':
            if not bracketed_start:
                bracketed_start = index + 1
            else:
                bracket_depth += 1
        elif char == ')':
            if bracketed_start and bracket_depth == 0:
                bracketed_end = index
                result = do_maths(maths[bracketed_start:bracketed_end])
                if not num_1:
                    num_1 = result
                else:
                    num_2 = result
                bracketed_start = bracket_end = None
            else:
                bracket_depth -= 1

        elif not bracketed_start:
            if not num_1:
                num_1 = int(char)
            else:
                num_2 = int(char)

        if num_1 and num_2:
            if operation == '+':
                num_1 = num_1 + num_2
                num_2 = None
            else:
                num_1 = num_1 * num_2
                num_2 = None

    return num_1


with open('inputs/2020_18.txt', 'r') as f:
    rows = [row.split() for row in f.readlines()]

parsed_rows = []
for row in rows:
    parsed_row = []
    for item in row:
        if item.startswith('('):
            for index, char in enumerate(item):
                if char == '(':
                    parsed_row.append(char)
                else:
                    parsed_row.extend(item[index:])

        elif item.endswith(')'):
            adjacent_item = ''
            for char in item:
                if char == ')':
                    if adjacent_item:
                        parsed_row.append(adjacent_item)
                        adjacent_item = ''
                    parsed_row.append(char)
                else:
                    adjacent_item += char

        else:
            parsed_row.append(item)

    parsed_rows.append(parsed_row)

rows = parsed_rows
total = 0
for row in rows:
    result = do_maths(row)
    total += result

# Answer One
print("Sum of the lines' values:", total)
