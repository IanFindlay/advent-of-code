#!/usr/bin/env python3

"""Advent of Code 2021 Day 8 - Seven Segment Search"""


with open('inputs/day_08.txt', 'r') as aoc_input:
    displays = []
    for display in aoc_input.readlines():
        patterns, outputs = display.split('|')
        patterns = [set(pattern) for pattern in patterns.strip().split(' ')]
        outputs = [set(pattern) for pattern in outputs.strip().split(' ')]
        displays.append((patterns, outputs, {}))

unique = (2, 3, 4, 7)
total = 0
for display in displays:
    total += sum(map(lambda x: 1 if len(x) in unique else 0, display[1]))

# Answer One
print("Number of times 1, 4, 7 or 8 appear in output values:", total)

output_sum = 0
for display in displays:
    patterns, outputs, mappings = display

    for pattern in patterns:
        if len(pattern) == 2:
            mappings[1] = pattern
        elif len(pattern) == 3:
            mappings[7] = pattern
        elif len(pattern) == 4:
            mappings[4] = pattern
        elif len(pattern) == 7:
            mappings[8] = pattern

    for n in (1, 4, 7, 8):
        patterns.remove(mappings[n])

    # 6 only 6 letter signal without all of 7 in it also yields segment c
    segment_c = None
    for pattern in patterns:
        if len(pattern) == 6:
            diff_to_7 = mappings[7].difference(pattern)
            if  diff_to_7:
                mappings[6] = pattern
                patterns.remove(pattern)
                segment_c = diff_to_7.pop()
                break

    # 3 is 5 letter signal that contains all of 7
    for pattern in patterns:
        if len(pattern) == 5 and len(mappings[7].intersection(pattern)) == 3:
            mappings[3] = pattern
            patterns.remove(pattern)
            break

    # 5 letter signals left (2 and 5) differ in terms of 'c' segment
    for pattern in patterns:
        if len(pattern) == 5:
            if segment_c in pattern:
                mappings[2] = pattern
            else:
                mappings[5] = pattern
    patterns.remove(mappings[2])
    patterns.remove(mappings[5])

    # 9 is 5 but with 'c' segment
    mappings[9] = mappings[5].copy()
    mappings[9].add(segment_c)
    patterns.remove(mappings[9])

    # 0 is only mapping left patterns
    mappings[0] = patterns.pop()

    output_value = ''
    for output in outputs:
        for digit, pattern in mappings.items():
            if pattern == output:
                output_value += str(digit)

    output_sum += int(output_value)

# Answer Two
print("Sum of all output values:", output_sum)
