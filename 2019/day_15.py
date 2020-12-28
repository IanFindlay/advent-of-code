"""Advent of Code 2019 Day 15 - Oxygen System."""


from collections import defaultdict


class RepairDroid:
    """Class representing an intcode running repair droid."""

    def __init__(self, code):
        """Initialises repair droid with code (dict) and an input list."""
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


def droid_bfs(intcode, explore_full=False):
    """BFS for oxygen system. Returns fewest steps or complete area map."""
    initial_instance = RepairDroid(intcode.copy())
    area_map = {}
    seen = set()
    stack = [(0, 0, 0, initial_instance)]
    while stack:
        x, y, steps, instance = stack.pop()
        code = instance.code
        pointer = instance.pointer

        children = []
        directions = {1: (x, y+1), 2: (x, y-1), 3: (x-1, y), 4: (x+1, y)}
        for input_num, coord_change in directions.items():
            new_coords = coord_change
            if new_coords in seen:
                continue
            new_instance = RepairDroid(code.copy())
            new_instance.inputs.append(input_num)
            new_instance.pointer = pointer
            new_gen = new_instance.run_intcode()

            output = next(new_gen)

            if output == 0:
                area_map[new_coords] = '#'
                seen.add(new_coords)
                continue

            if output == 1:
                area_map[new_coords] = '.'
                seen.add(new_coords)

            else:
                area_map[new_coords] = 'O'
                oxygen_location = new_coords
                if not explore_full:
                    return steps + 1

            children.append(
                (new_coords[0], new_coords[1], steps + 1, new_instance)
            )

        stack += children

    return (oxygen_location, area_map)


intcode_dict = defaultdict(int)
with open('inputs/day_15.txt') as f:
    i = 0
    for instruction in f.read().split(','):
        intcode_dict[i] = int(instruction)
        i += 1

# Answer One
print("Fewest steps required to reach oxygen system:", droid_bfs(intcode_dict))

oxygen_start, full_map = droid_bfs(intcode_dict, True)
oxygen_front = [oxygen_start]
minutes = 0
while oxygen_front:
    open_spaces = []
    for coords in oxygen_front:
        x, y = coords
        directions = [(x, y+1), (x, y-1), (x-1, y), (x+1, y)]
        for direction in directions:
            if full_map[direction] == '.':
                open_spaces.append(direction)
                full_map[direction] = 'O'

    oxygen_front = open_spaces
    minutes += 1

# Answer Two
print("Mintues until area is filled with oxygen:", minutes - 1)
