"""Advent of Code Day 23 - Coprocessor Conflagration"""

import re
import collections


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
        print(instruction)
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

    with open('input.txt') as f:
        data = [line.strip() for line in f.readlines()]

    print("Number of times 'mul' is invoked:", coprocessor(data))

    # Part Two - Need to find out what the code is doing/what pattern lay underneath it
