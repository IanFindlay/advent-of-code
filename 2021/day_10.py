#!/usr/bin/env python3

"""Advent of Code 2021 Day 10 - Syntax Scoring"""


with open('inputs/day_10.txt', 'r') as aoc_input:
    lines = [line.strip() for line in aoc_input.readlines()]

match_dict = {'(': ')', '{': '}', '<': '>', '[': ']'}

corrupted_chars = []
i = len(lines)
while i >= 0:
    i -= 1
    open_chunk_symbols = []
    for char in lines[i]:
        if char in match_dict.keys():
            open_chunk_symbols.append(char)
        elif char != match_dict[open_chunk_symbols.pop()]:
                corrupted_chars.append(char)
                del lines[i]
                break

illegal_char_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
syntax_error_score = 0
for char in corrupted_chars:
    syntax_error_score += illegal_char_points[char]

# Answer One
print("Total syntax error score:", syntax_error_score)

completion_strings = []
for line in lines:
    open_chunk_symbols = []
    for char in line:
        if char in match_dict.keys():
            open_chunk_symbols.append(char)
        else:
            open_chunk_symbols.pop()

    finishing_chars = ''
    for remaining in open_chunk_symbols:
        finishing_chars = match_dict[remaining] + finishing_chars

    completion_strings.append(finishing_chars)


completion_char_points = {')': 1, ']': 2, '}': 3, '>': 4}
completion_scores = []
for completion_string in completion_strings:
    completion_score = 0
    for char in completion_string:
        completion_score *= 5
        completion_score += completion_char_points[char]

    completion_scores.append(completion_score)

# Answer Two
print("Middle completion score:",
        sorted(completion_scores)[len(completion_scores) // 2])
