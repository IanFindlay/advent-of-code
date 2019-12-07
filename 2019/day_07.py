"""Advent of Code 2019 Day 07 - Amplification Circuit."""


from itertools import permutations


class Amplifier:
    """Class modelling an amplifier that runs an intcode program."""

    def __init__(self, code, inputs):
        """Initialise Amplifier instance.

        Args:
            code (list): List of numbers (an code)
            inputs (list): List of inputs available to the Amplifier

        """
        self.code = code
        self.inputs = inputs
        self.output = None

    def run_intcode(self):
        """Run intcode program."""
        pointer = 0
        while True:
            opcode = self.code[pointer]

            if opcode > 100:
                opcode, modes = parse_instructions_opcode(opcode)
            else:
                modes = [0, 0, 0]

            if opcode == 99:   # halt
                return

            param_1 = pointer + 1 if modes[0] else self.code[pointer + 1]
            param_2 = pointer + 2 if modes[1] else self.code[pointer + 2]

            try:
                param_3 = self.code[pointer + 3]
            except IndexError:
                pass

            if opcode == 1:   # addition
                self.code[param_3] = self.code[param_1] + self.code[param_2]
                pointer += 4

            elif opcode == 2:   # multiplication
                self.code[param_3] = self.code[param_1] * self.code[param_2]
                pointer += 4

            elif opcode == 3:   # input
                if self.inputs:
                    self.code[param_1] = self.inputs.pop(0)
                    pointer += 2
                else:
                    yield

            elif opcode == 4:   # output
                pointer += 2
                self.output = self.code[param_1]
                yield self.output

            elif opcode == 5:   # jump-if-true
                if self.code[param_1] == 0:
                    pointer += 3
                else:
                    pointer = self.code[param_2]

            elif opcode == 6:   # jump-if-false
                if self.code[param_1] != 0:
                    pointer += 3
                else:
                    pointer = self.code[param_2]

            elif opcode == 7:   # less than
                if self.code[param_1] < self.code[param_2]:
                    self.code[param_3] = 1
                else:
                    self.code[param_3] = 0
                pointer += 4

            elif opcode == 8:   # equals
                if self.code[param_1] == self.code[param_2]:
                    self.code[param_3] = 1
                else:
                    self.code[param_3] = 0
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
for phases in phase_settings:
    amp_a = Amplifier(program.copy(), [phases[0], 0]).run_intcode()
    amp_b = Amplifier(program.copy(), [phases[1], next(amp_a)]).run_intcode()
    amp_c = Amplifier(program.copy(), [phases[2], next(amp_b)]).run_intcode()
    amp_d = Amplifier(program.copy(), [phases[3], next(amp_c)]).run_intcode()
    amp_e = Amplifier(program.copy(), [phases[4], next(amp_d)]).run_intcode()
    output_e = next(amp_e)

    if not max_signal or output_e > max_signal:
        max_signal = output_e

# Answer One
print("Highest signal:", max_signal)

phase_options = [5, 6, 7, 8, 9]
phase_settings = list(permutations(phase_options))

max_signal = None
for phases in phase_settings:
    amp_a = Amplifier(program.copy(), [phases[0], 0])
    amp_b = Amplifier(program.copy(), [phases[1]])
    amp_c = Amplifier(program.copy(), [phases[2]])
    amp_d = Amplifier(program.copy(), [phases[3]])
    amp_e = Amplifier(program.copy(), [phases[4]])

    gen_a = amp_a.run_intcode()
    gen_b = amp_b.run_intcode()
    gen_c = amp_c.run_intcode()
    gen_d = amp_d.run_intcode()
    gen_e = amp_e.run_intcode()

    while True:
        try:
            output = next(gen_a)
            if output:
                amp_b.inputs.append(output)
        except StopIteration:
            pass
        try:
            output = next(gen_b)
            if output:
                amp_c.inputs.append(output)
        except StopIteration:
            pass
        try:
            output = next(gen_c)
            if output:
                amp_d.inputs.append(output)
        except StopIteration:
            pass
        try:
            output = next(gen_d)
            if output:
                amp_e.inputs.append(output)
        except StopIteration:
            pass
        try:
            output = next(gen_e)
            if output:
                amp_a.inputs.append(output)
        except StopIteration:
            break

    if max_signal is None or output > max_signal:
        max_signal = output

# Answer Two
print("Highest signal with feedback loop:", max_signal)
