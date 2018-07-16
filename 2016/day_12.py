""" Advent of Code Day 12 - Leonardo's Monorail"""

from collections import defaultdict


with open('input.txt') as f:
    instructions = [line.strip() for line in f.readlines()]

registers = defaultdict(int)
registers['c'] = 1   # Comment Out for Part One
i = 0
while i < len(instructions):
    parse = instructions[i].split(' ')

    if parse[0] == 'cpy':
        if parse[1].isnumeric():
            registers[parse[2]] = int(parse[1])
        else:
            registers[parse[2]] = registers[parse[1]]

    elif parse[0] == 'inc':
        registers[parse[1]] += 1

    elif parse[0] == 'dec':
        registers[parse[1]] -= 1

    elif parse[0] == 'jnz':
        if parse[1].isnumeric():
            if parse[1] != 0:
                i += int(parse[2]) - 1

        elif registers[parse[1]] != 0:
            i += int(parse[2]) - 1

    i += 1

# Answer One / Answer Two
print("Register A:", registers['a'])
