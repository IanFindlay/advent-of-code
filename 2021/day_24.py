#!/usr/bin/env python3

"""Advent of Code 2021 Day 24 - Arithmetic Logic Unit"""


def check_validity(w, z, block_num, to_validate, part_two=False):
    to_validate = to_validate.copy()
    to_validate.append(w)

    # Varied values for this block
    z_value = z_vars[block_num]
    x_value = x_vars[block_num]
    y_value = y_vars[block_num]

    # Check w, or all still valid at this block w values for validity
    if z % 26 + x_value != w and x_value < 0:
        return False

    # Calculate z to get new z value / final validation value
    x = z
    x %= 26
    z //= z_value
    x += x_value
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 25
    y *= x
    y += 1
    z *= y
    y = w + y_value
    y = y * x
    z += y

    if block_num == 13:
        if z == 0:
            return to_validate
        else:
            return False

    # Digits are valid but model number not yet complete so recursion
    if not part_two:
        for i in range(9, 0, -1):
            validity_check = check_validity(i, z, block_num + 1, to_validate)
            if type(validity_check) is list:
                return validity_check
    else:
        for i in range(1, 10):
            validity_check = check_validity(i, z, block_num + 1,
                                            to_validate, part_two=True)

            if type(validity_check) is list:
                return validity_check

    return False


"""
Analysis of Input to Trim Possible Values:

Only three parts of block vary - div z, add x, add y.
7 of these blocks have div z as one and 7 have div z 26

div z 1 blocks always have line 8 (egl x 0) == 1 as line 7 is guaranteed to be
false due to add x value always being above 9 (the max value that w can be set
to after "inp w".)

When x is 1 after above (guaranteed when div z == 1) y ends up as 26:
    - Set to 0 by mul, + 25, * x then add 1

if x is 0 then x == w (1-9) mul y x (line 11) == 0 meaning y == 1

if y is 1 then z - which == z from previous if div z == 1 else a multiple of
26 (or 0 if accumulation hasn't got above 26 yet but I think it is designed to)

y is then set to w - mul 0 (line 14), y_var added, multiplied by x (0 or 1):

y added to z. Need z == 0 for valid at final block which means y has to be -z
or both are 0 (that possible?)

This means that z, despite accumulation, has to be a one digit integer at this
stage or y couldn't get big enough to zero it out.

Therefore whilst div z 26 can either result in adding or removing a digit -
whereas div z 1 always adds one - in valid inputs it has to remove one to
be a single digit at the end for y to have a chance at negating z

So all instances of div z 26 must meet the criteria of:

    Whatever z is for that block % 26 + what add x is going to be == inp w

inp based on model number and we want highest so 9 down to 1 inclusive

Part Two we want lowest so do 1 up to 9 inclusive instead

"""

with open('inputs/day_24.txt', 'r') as aoc_input:
    lines = [line.strip().split(' ') for line in aoc_input.readlines()]


z_vars = []
x_vars = []
y_vars = []

# Collect all numbers that vary for easy use in function via index
i = 4
while i < len(lines):
    z_vars.append(int(lines[i][2]))
    x_vars.append(int(lines[i + 1][2]))
    y_vars.append(int(lines[i + 11][2]))

    i += 18

highest_valid = None
for i in range(9, 0, -1):
    validity_check = check_validity(i, 0, 0, [])
    if type(validity_check) is list:
        highest_valid = ''.join(map(str, validity_check))
        break

# Answer One
print(f'Largest model number accepted by MONAD: {highest_valid}')

lowest_valid = None
for i in range(1, 10):
    validity_check = check_validity(i, 0, 0, [], part_two=True)
    if type(validity_check) is list:
        lowest_valid = ''.join(map(str, validity_check))
        break

# Answer One
print(f'Lowest model number accepted by MONAD: {lowest_valid}')
