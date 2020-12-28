"""Advent of Code Day 23 - Coprocessor Conflagration"""

import re
import collections
import math


def is_num(string):
    """Return whether or not a string can be interpreted as an integer."""
    try:
        int(string)
    except ValueError:
        return False
    return True


def coprocessor(instructions):
    """Return the final recovered note of a list of instructions."""
    muls = 0
    i = 0
    while i < len(instructions):
        instruction = instructions[i]
        mod, target, *change = re.findall(r'-?\w+', instruction)

        if mod == 'set':
            if is_num(change[0]):
                registers[target] = int(change[0])
            else:
                registers[target] = registers[change[0]]

        elif mod == 'sub':
            if is_num(change[0]):
                registers[target] -= int(change[0])
            else:
                registers[target] -= registers[change[0]]

        elif mod == 'mul':
            if is_num(change[0]):
                registers[target] *= int(change[0])
            else:
                registers[target] *= registers[change[0]]
            muls += 1

        elif mod == 'jnz':
            if is_num(change[0]):
                if is_num(target):
                    if int(target) != 0:
                        i += int(change[0])
                        continue
                else:
                    if registers[target] != 0:
                        i += int(change[0])
                        continue
            else:
                if is_num (target):
                    if int(target) != 0:
                        i += int(registers[change[0]])
                        continue
                else:
                    if registers[target] != 0:
                        i += registers[change[0]]
                        continue
        i += 1

    return muls


if __name__ == '__main__':

    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0,
                 'e': 0, 'f': 0, 'g': 0, 'h': 0,}

    with open('inputs/day_23.txt') as f:
        data = [line.strip() for line in f.readlines()]

    print("Number of times 'mul' is invoked:", coprocessor(data))

    # Part Two
    """
    Line 29 is the only exit point and g must equal 0 for it to occur
    Above only happens when b and c are the same value at line 27/28
    If g isn't 0 b increments (only time it does) by the suspiciously prime 17
    h only increases if f == 0 at line 25
    So h is essentially counting the non-primes between initial b and c
    b initialises to 107900 and c to 124900 (17000 higher i.e. 1000 times 17 inc)
    """

    composites = 0
    for num in range(107900, 124900 + 1, 17):
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                composites += 1
                break

# Answer Two
print("Value of register h with debug mode off:", composites)
