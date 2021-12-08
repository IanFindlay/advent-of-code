#!/usr/bin/env python3

"""Advent of Code 2021 Day 8 - Seven Segment Search"""


with open('inputs/day_08.txt', 'r') as aoc_input:
    displays = {}
    for num, line in enumerate(aoc_input.readlines()):
        patterns, outputs = line.split('|')
        patterns = patterns.strip().split(' ')
        outputs = outputs.strip().split(' ')
        displays[num] = (patterns, outputs, {}, {})


unique = 0
for key, value in displays.items():
    outputs = value[1]
    for output in outputs:
        if len(output) in (2, 3, 4, 7):
            unique += 1

# Answer One
print("Number of times 1, 4, 7 or 8 appear in output values:", unique)

output_sum = 0
for key, value in displays.items():
    patterns, outputs, mappings, segments = value
    unsolved = [set(pattern) for pattern in patterns]

    for pattern in patterns:
        if len(pattern) == 2:
            mappings[1] = set(pattern)
            unsolved.remove(set(pattern))
        elif len(pattern) == 3:
            mappings[7] = set(pattern)
            unsolved.remove(set(pattern))
        elif len(pattern) == 4:
            mappings[4] = set(pattern)
            unsolved.remove(set(pattern))
        elif len(pattern) == 7:
            mappings[8] = set(pattern)
            unsolved.remove(set(pattern))

    # Difference between 1 and 7 gets the top 'a' row
    segments['a'] = mappings[7].difference(mappings[1]).pop()

    # 3 is 5 letter that contains all of 7
    for pattern in unsolved:
        if len(pattern) == 5:
            if len(set(mappings[7]).intersection(pattern)) == 3:
                mappings[3] = pattern
                unsolved.remove(pattern)
                break

    # 6 only 6 letter without all of 7 in it
    for pattern in unsolved:
        if len(pattern) == 6:
            diff_to_7 = mappings[7].difference(pattern)
            if diff_to_7:
                mappings[6] = pattern
                segments['c'] = diff_to_7.pop()
                unsolved.remove(pattern)

    # 5 is 5 letters without 'c' in whereas 2 has it in
    for pattern in unsolved:
        if len(pattern) == 5:
            if segments['c'] in pattern:
                mappings[2] = pattern
            else:
                mappings[5] = pattern

    unsolved.remove(mappings[2])
    unsolved.remove(mappings[5])

    # 9 is 5 but with c
    expected_9 = mappings[5].copy()
    expected_9.add(segments['c'])
    for pattern in unsolved:
        if pattern == expected_9:
            mappings[9] = pattern
        else:
            mappings[0] = pattern

    output_value = ''
    for output in outputs:
        for key, value in mappings.items():
            if value == set(output):
                output_value += str(key)

    output_sum += int(output_value)

# Answer Two
print("Sum of all output values:", output_sum)
