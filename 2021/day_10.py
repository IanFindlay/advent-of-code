#!/usr/bin/env python3

"""Advent of Code 2021 Day 10 - """


with open('inputs/day_10.txt', 'r') as aoc_input:
    lines = [line.strip() for line in aoc_input.readlines()]

opening_chars = ('(', '{', '<', '[')
match_dict = {'(': ')', '{': '}', '<': '>', '[': ']'}
illegal_char_points = {')': 3, ']': 57, '}': 1197, '>': 25137}

corrupted = []
for line in lines:
    open_chunk_symbols = []
    line_corrupted = False
    for char in line:
        if char in opening_chars:
            open_chunk_symbols.append(char)
        else:
            if char != match_dict[open_chunk_symbols.pop()]:
                line_corrupted = True


        if line_corrupted:
            corrupted.append((line, char))
            break

syntax_error_score = 0
for line in corrupted:
    syntax_error_score += illegal_char_points[line[1]]

# Answer One
print("Total syntax error score:", syntax_error_score)
