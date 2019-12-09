"""Advent of Code 2019 Day 9 - Sensor Boost."""


from collections import defaultdict


def run_intcode(code, inputs):
    """Run intcode program."""
    relative_base = 0
    pointer = 0
    while True:
        opcode = code[pointer]

        if 99 < opcode <= 22210:
            opcode, modes = parse_instruction(opcode)
        else:
            modes = [0, 0, 0]

        if opcode == 99:   # halt
            return

        if modes[0] == 0:
            param_1 = code[pointer + 1]
        elif modes[0] == 1:
            param_1 = pointer + 1
        else:
            param_1 = code[pointer + 1] + relative_base

        if modes[1] == 0:
            param_2 = code[pointer + 2]
        elif modes[1] == 1:
            param_2 = pointer + 2
        else:
            param_2 = code[pointer + 2] + relative_base

        if modes[2] == 0:
            param_3 = code[pointer + 3]
        else:
            param_3 = code[pointer + 3] + relative_base

        if opcode == 1:   # addition
            code[param_3] = code[param_1] + code[param_2]
            pointer += 4

        elif opcode == 2:   # multiplication
            code[param_3] = code[param_1] * code[param_2]
            pointer += 4

        elif opcode == 3:   # input
            if inputs:
                code[param_1] = inputs.pop(0)
                pointer += 2
            else:
                yield

        elif opcode == 4:   # output
            pointer += 2
            output = code[param_1]
            yield output

        elif opcode == 5:   # jump-if-true
            if code[param_1] == 0:
                pointer += 3
            else:
                pointer = code[param_2]

        elif opcode == 6:   # jump-if-false
            if code[param_1] != 0:
                pointer += 3
            else:
                pointer = code[param_2]

        elif opcode == 7:   # less than
            if code[param_1] < code[param_2]:
                code[param_3] = 1
            else:
                code[param_3] = 0
            pointer += 4

        elif opcode == 8:   # equals
            if code[param_1] == code[param_2]:
                code[param_3] = 1
            else:
                code[param_3] = 0
            pointer += 4

        elif opcode == 9:   # adjust relative base
            relative_base += code[param_1]
            pointer += 2

        else:
            print("Invalid or incorrectly parsed instruction.")
            return


def parse_instruction(value):
    """Return opcode and mode parsed from instruction value."""
    str_value = str(value)
    opcode = int(str_value[-2:])
    modes = [int(x) for x in list(str_value)[:-2]]
    while len(modes) != 3:
        modes.insert(0, 0)
    return (opcode, list(reversed(modes)))


# Create defaultdict out of input for memory access
intcode_dict = defaultdict(int)
with open('input.txt', 'r') as f:
    i = 0
    for instruction in f.read().split(','):
        intcode_dict[i] = int(instruction)
        i += 1

# Answer One
boost_program = run_intcode(intcode_dict.copy(), [1])
print("Boost code:", next(boost_program))

# Answer Two
boost_program = run_intcode(intcode_dict.copy(), [2])
print("Distress code coordinates:", next(boost_program))
