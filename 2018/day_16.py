"""Advent of Code Day 16 - Chronal Classification"""

import collections
import re


def add_register(registers, opcode):
    value = registers[opcode[1]] + registers[opcode[2]]
    registers[opcode[3]] = value
    return registers


def add_immediate(registers, opcode):
    value = registers[opcode[1]] + opcode[2]
    registers[opcode[3]] = value
    return registers


def multiply_register(registers, opcode):
    value = registers[opcode[1]] * registers[opcode[2]]
    registers[opcode[3]] = value
    return registers


def multiply_immediate(registers, opcode):
    value = registers[opcode[1]] * opcode[2]
    registers[opcode[3]] = value
    return registers


def bitand_register(registers, opcode):
    value = registers[opcode[1]] & registers[opcode[2]]
    registers[opcode[3]] = value
    return registers


def bitand_immediate(registers, opcode):
    value = registers[opcode[1]] & opcode[2]
    registers[opcode[3]] = value
    return registers


def bitor_register(registers, opcode):
    value = registers[opcode[1]] | registers[opcode[2]]
    registers[opcode[3]] = value
    return registers


def bitor_immediate(registers, opcode):
    value = registers[opcode[1]] | opcode[2]
    registers[opcode[3]] = value
    return registers


def set_register(registers, opcode):
    registers[opcode[3]] = registers[opcode[1]]
    return registers


def set_immediate(registers, opcode):
    registers[opcode[3]] = opcode[1]
    return registers


def greater_ir(registers, opcode):
    value = 1 if opcode[1] > registers[opcode[2]] else 0
    registers[opcode[3]] = value
    return registers


def greater_ri(registers, opcode):
    value = 1 if registers[opcode[1]] > opcode[2] else 0
    registers[opcode[3]] = value
    return registers


def greater_rr(registers, opcode):
    value = 1 if registers[opcode[1]] > registers[opcode[2]] else 0
    registers[opcode[3]] = value
    return registers


def equality_ir(registers, opcode):
    value = 1 if opcode[1] == registers[opcode[2]] else 0
    registers[opcode[3]] = value
    return registers


def equality_ri(registers, opcode):
    value = 1 if registers[opcode[1]] == opcode[2] else 0
    registers[opcode[3]] = value
    return registers


def equality_rr(registers, opcode):
    value = 1 if registers[opcode[1]] == registers[opcode[2]] else 0
    registers[opcode[3]] = value
    return registers


def function_dispatch(registers, assigned, opcode):
    """Dispatcher - gets key from opcode then runs appropriate function."""
    functions = {
        'ar': add_register,
        'ai': add_immediate,
        'mr': multiply_register,
        'mi': multiply_immediate,
        'bar': bitand_register,
        'bai': bitand_immediate,
        'bor': bitor_register,
        'boi': bitor_immediate,
        'sr': set_register,
        'si': set_immediate,
        'gir': greater_ir,
        'gri': greater_ri,
        'grr': greater_rr,
        'eir': equality_ir,
        'eri': equality_ri,
        'err': equality_rr
    }

    key = assigned[opcode[0]]
    functions[key](registers, opcode)


def main():
    """Parse input, run and then decode instructions."""
    with open('input.txt') as f:
        lines = [x.strip() for x in f.readlines()]

    cpu_regex = re.compile(r'\[(\d+), (\d+), (\d+), (\d+)\]')
    cpu_data = []
    i = 0
    while True:
        found = cpu_regex.search(lines[i])

        # To account for split input break if space encountered
        if not found:
            start_second = i
            break

        before = [int(x) for x in found.group(1, 2, 3, 4)]

        opcode = [int(x) for x in lines[i+1].split()]

        found = cpu_regex.search(lines[i+2])
        after = [int(x) for x in found.group(1, 2, 3, 4)]

        i += 4  # Skip lines used above + space between data in input
        cpu_data.append((before, opcode, after))

    # Check data against each function and note if return matches after
    opcodes = collections.defaultdict(set)
    three_or_more = 0
    for data in cpu_data:
        possible = 0
        before, opcode, after = data

        if add_register(before.copy(), opcode) == after:
            possible += 1
            opcodes[opcode[0]].add('ar')

        if add_immediate(before.copy(), opcode) == after:
            possible += 1
            opcodes[opcode[0]].add('ai')

        if multiply_register(before.copy(), opcode) == after:
            possible += 1
            opcodes[opcode[0]].add('mr')

        if multiply_immediate(before.copy(), opcode) == after:
            possible += 1
            opcodes[opcode[0]].add('mi')

        if bitand_register(before.copy(), opcode) == after:
            possible += 1
            opcodes[opcode[0]].add('bar')

        if bitand_immediate(before.copy(), opcode) == after:
            possible += 1
            opcodes[opcode[0]].add('bai')

        if bitor_register(before.copy(), opcode) == after:
            possible += 1
            opcodes[opcode[0]].add('bor')

        if bitor_immediate(before.copy(), opcode) == after:
            possible += 1
            opcodes[opcode[0]].add('boi')

        if set_register(before.copy(), opcode) == after:
            possible += 1
            opcodes[opcode[0]].add('sr')

        if set_immediate(before.copy(), opcode) == after:
            possible += 1
            opcodes[opcode[0]].add('si')

        if greater_ir(before.copy(), opcode) == after:
            possible += 1
            opcodes[opcode[0]].add('gir')

        if greater_ri(before.copy(), opcode) == after:
            possible += 1
            opcodes[opcode[0]].add('gri')

        if greater_rr(before.copy(), opcode) == after:
            possible += 1
            opcodes[opcode[0]].add('grr')

        if equality_ir(before.copy(), opcode) == after:
            possible += 1
            opcodes[opcode[0]].add('eir')

        if equality_ri(before.copy(), opcode) == after:
            possible += 1
            opcodes[opcode[0]].add('eri')

        if equality_rr(before.copy(), opcode) == after:
            possible += 1
            opcodes[opcode[0]].add('err')

        if possible >= 3:
            three_or_more += 1

    # Answer One
    print("Three or more:", three_or_more)

    # Loop through opcodes and assign ones with one function not already assigned
    assigned = {}
    while True:
        unknown = True
        for opcode, potential in opcodes.items():
            functions = [x for x in potential if x not in assigned.values()]
            if len(functions) == 1:
                assigned[opcode] = functions[0]
                unknown = False

        # Nothing left to assign
        if unknown:
            break

    # Parse second half of input starting from where cpu finished (start_second)
    instructions = []
    for line in lines[start_second:]:
        instruction = [int(x) for x in line.strip().split()]
        if instruction:
            instructions.append(instruction)

    # Set registers and run instructions
    registers = [0, 0, 0, 0]
    for instruction in instructions:
        function_dispatch(registers, assigned, instruction)

    # Answer Two
    print("Register 0:", registers[0])


if __name__ == '__main__':
    main()
