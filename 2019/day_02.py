"""Advent of Code 2019 Day 02 - 1202 Program Alarm."""


def run_intcode(memory, noun, verb):
    """Assign noun and verb then run intcode program on memory."""
    memory[1] = noun
    memory[2] = verb
    pointer = 0
    while True:
        opcode = memory[pointer]
        if opcode == 99:
            return memory[0]

        param_one = memory[pointer + 1]
        param_two = memory[pointer + 2]
        param_three = memory[pointer + 3]

        if opcode == 1:
            memory[param_three] = memory[param_one] + memory[param_two]

        elif opcode == 2:
            memory[param_three] = memory[param_one] * memory[param_two]

        pointer += 4


def find_gravity_assist_inputs(memory, desired_output):
    """Find noun and verb that gives desired_output when intcode is run."""
    for noun in range(0, 100):
        for verb in range(0, 100):
            output = run_intcode(memory[:], noun, verb)
            if output == desired_output:
                return 100 * noun + verb
    return False


with open('inputs/day_02.txt', 'r') as f:
    integers = [int(opcode) for opcode in f.read().split(',')]

# Answer One
print("Output prior to fire: {}".format(run_intcode(integers[:], 12, 2)))

# Answer Two
print("Inputs required for gravity assist calculation: {}".format(
    find_gravity_assist_inputs(integers, 19690720)
))

