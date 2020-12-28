"""Advent of Code 2019 Day 19 - Tractor Beam."""


from collections import defaultdict


class Drone:
    """Class for an the intcode controlled drone."""

    def __init__(self, code):
        """Initialises intcode code (dict) and an input list."""
        self.code = code
        self.inputs = []
        self.pointer = 0

    def run_intcode(self):
        """Run intcode program on code."""
        relative_base = 0
        while True:
            opcode = self.code[self.pointer]

            if 99 < opcode <= 22210:
                opcode, modes = parse_instruction(opcode)
            else:
                modes = [0, 0, 0]

            if opcode == 99:   # halt
                return

            if modes[0] == 0:
                param_1 = self.code[self.pointer + 1]
            elif modes[0] == 1:
                param_1 = self.pointer + 1
            else:
                param_1 = self.code[self.pointer + 1] + relative_base

            if modes[1] == 0:
                param_2 = self.code[self.pointer + 2]
            elif modes[1] == 1:
                param_2 = self.pointer + 2
            else:
                param_2 = self.code[self.pointer + 2] + relative_base

            if modes[2] == 0:
                param_3 = self.code[self.pointer + 3]
            else:
                param_3 = self.code[self.pointer + 3] + relative_base

            if opcode == 1:   # addition
                self.code[param_3] = self.code[param_1] + self.code[param_2]
                self.pointer += 4

            elif opcode == 2:   # multiplication
                self.code[param_3] = self.code[param_1] * self.code[param_2]
                self.pointer += 4

            elif opcode == 3:   # input
                if self.inputs:
                    self.code[param_1] = self.inputs.pop(0)
                    self.pointer += 2
                else:
                    yield "Waiting on input"

            elif opcode == 4:   # output
                self.pointer += 2
                output = self.code[param_1]
                yield output

            elif opcode == 5:   # jump-if-true
                if self.code[param_1] == 0:
                    self.pointer += 3
                else:
                    self.pointer = self.code[param_2]

            elif opcode == 6:   # jump-if-false
                if self.code[param_1] != 0:
                    self.pointer += 3
                else:
                    self.pointer = self.code[param_2]

            elif opcode == 7:   # less than
                if self.code[param_1] < self.code[param_2]:
                    self.code[param_3] = 1
                else:
                    self.code[param_3] = 0
                self.pointer += 4

            elif opcode == 8:   # equals
                if self.code[param_1] == self.code[param_2]:
                    self.code[param_3] = 1
                else:
                    self.code[param_3] = 0
                self.pointer += 4

            elif opcode == 9:   # adjust relative base
                relative_base += self.code[param_1]
                self.pointer += 2

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


def reset_drone(drone_instance, code, coords):
    """Reset member of Drone class to start with coords as input."""
    drone_instance.inputs = coords
    drone_instance.code = code.copy()
    drone_instance.pointer = 0


intcode_dict = defaultdict(int)
with open('inputs/day_19.txt') as f:
    i = 0
    for instruction in f.read().split(','):
        intcode_dict[i] = int(instruction)
        i += 1

drone = Drone(intcode_dict)
drone_run = drone.run_intcode()
drone_readouts = {}
start = None
for x in range(50):
    for y in range(50):
        reset_drone(drone, intcode_dict, [x, y])
        drone_readouts[(x, y)] = next(drone_run)
        if not start and y != 0 and drone_readouts[(x, y)] == 1:
            start = (x, y)

# Answer One
print("Drones affected by tractor beam:", sum(drone_readouts.values()))

# Start from start (due to diagonal making some early rows erroneously empty)
x, y = start
while True:
    reset_drone(drone, intcode_dict, [x, y])
    bl_corner = next(drone_run)
    if bl_corner:
        reset_drone(drone, intcode_dict, [x + 99, y - 99])
        tr_corner = next(drone_run)
        if tr_corner:
            break
        y += 1
    else:
        x += 1

# Answer Two
print("First 100x100 tractor beam square value:", x * 10000 + y - 99)
