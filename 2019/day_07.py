"""Advent of Code 2019 Day 07 - ."""

from itertools import permutations


def run_intcode(memory, input_values):
    """Run intcode program on memory set with given input value."""
    diagnostic_code = 0
    pointer = 0
    while True:
        opcode = memory[pointer]

        if opcode > 100:
            opcode, modes = parse_instructions_opcode(opcode)
        else:
            modes = [0, 0, 0]

        if opcode == 99:
            return diagnostic_code

        param_1 = pointer + 1 if modes[0] else memory[pointer + 1]
        param_2 = pointer + 2 if modes[1] else memory[pointer + 2]
        param_3 = memory[pointer + 3]

        if opcode == 1:
            memory[param_3] = memory[param_1] + memory[param_2]
            pointer += 4

        elif opcode == 2:
            memory[param_3] = memory[param_1] * memory[param_2]
            pointer += 4

        elif opcode == 3:
            memory[param_1] = input_values.pop()
            pointer += 2

        elif opcode == 4:
            diagnostic_code = memory[param_1]
            pointer += 2

        elif opcode == 5:
            if memory[param_1] == 0:
                pointer += 3
            else:
                pointer = memory[param_2]

        elif opcode == 6:
            if memory[param_1] != 0:
                pointer += 3
            else:
                pointer = memory[param_2]

        elif opcode == 7:
            if memory[param_1] < memory[param_2]:
                memory[param_3] = 1
            else:
                memory[param_3] = 0
            pointer += 4

        elif opcode == 8:
            if memory[param_1] == memory[param_2]:
                memory[param_3] = 1
            else:
                memory[param_3] = 0
            pointer += 4


def parse_instructions_opcode(value):
    """Return opcode and mode parsed from instruction value."""
    str_value = str(value)
    opcode = int(str_value[-2:])
    modes = [int(x) for x in list(str_value)[:-2]]
    while len(modes) != 3:
        modes.insert(0, 0)
    return (opcode, list(reversed(modes)))


with open('input.txt', 'r') as f:
    program = [int(x) for x in f.read().split(',')]

phase_options = [0, 1, 2, 3, 4]
phase_settings = list(permutations(phase_options))

max_signal = None
for phase_setting in phase_settings:
    memory = program.copy()

    output_a = run_intcode(memory, [0, phase_setting[0]])
    output_b = run_intcode(memory, [output_a, phase_setting[1]])
    output_c = run_intcode(memory, [output_b, phase_setting[2]])
    output_d = run_intcode(memory, [output_c, phase_setting[3]])
    output_e = run_intcode(memory, [output_d, phase_setting[4]])

    if not max_signal or output_e > max_signal:
        max_signal = output_e

# Answer One
print("Highest signal that can be sent to thruster:", max_signal)

