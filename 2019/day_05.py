"""Advent of Code 2019 Day 5 - Sunny with a Chance of Asteroids."""


def run_intcode(memory, input_value):
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
            memory[param_1] = input_value
            pointer += 2

        elif opcode == 4:
            diagnostic_code = memory[param_1]
            #print(diagnostic_code)
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

# Answer One
print("Diagnostic Code for ID 1:", run_intcode(list(program), 1))

# Answer Two
print("Diagnostic Code for ID 5:", run_intcode(list(program), 5))
