"""Advent of Code Day 23 - Opening the Turing Lock"""

with open('input.txt') as f:
    instructions = [line.strip() for line in f]

registers = {'a': 1, 'b': 0}     # Change a to 0 for Part One

pos = 0
while pos < len(instructions):
    parsed = instructions[pos].split(' ')
    if len(parsed) == 3:
        if parsed[0] == 'jio':
            if registers[parsed[1].strip(',')] == 1:
                pos += int(parsed[2])
                continue

        elif parsed[0] == 'jie':
            if registers[parsed[1].strip(',')] % 2 == 0:
                pos += int(parsed[2])
                continue
    
    elif parsed[0] == 'hlf':
        registers[parsed[1]] /= 2

    elif parsed[0] == 'tpl':
        registers[parsed[1]] *= 3

    elif parsed[0] == 'inc':
        registers[parsed[1]] += 1

    elif parsed[0] == 'jmp':
        pos += int(parsed[1])
        continue
    
    pos += 1


print("Value of Register b =", registers['b'])
