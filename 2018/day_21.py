"""Advent of Code Day 21 - Chronal Conversion"""


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


def function_dispatch(registers, opcode):
    """Dispatcher - gets key from opcode then runs appropriate function."""
    functions = {
        'addr': add_register,
        'addi': add_immediate,
        'mulr': multiply_register,
        'muli': multiply_immediate,
        'banr': bitand_register,
        'bani': bitand_immediate,
        'borr': bitor_register,
        'bori': bitor_immediate,
        'setr': set_register,
        'seti': set_immediate,
        'gtir': greater_ir,
        'gtri': greater_ri,
        'gtrr': greater_rr,
        'eqir': equality_ir,
        'eqri': equality_ri,
        'eqrr': equality_rr
    }

    key = opcode[0]
    functions[key](registers, opcode)


# Analysis of program
"""
( 0) seti 123 0 2       # Set register 2 to 123

( 1) bani 2 456 2       # Verify bani as per question

( 2) eqri 2 72 2        # Verify bani as per question

( 3) addr 2 4 4         # Register 4 += register 2 so if register 2 == 72
                          reset of IP is skipped

( 4) seti 0 0 4         # Reset IP which restarts the bani verify above

( 5) seti 0 8 2         # Reset register 2 then exits the verification step

# The above is the verification mentioned in the question


( 6) bori 2 65536 5     # Set register 5 to bitor of register 2 (0 from above)

( 7) seti 2238642 0 2   # Set regsiter 2 to large number

( 8) bani 5 255 3       # Bitand of 5 and 255 into regsiter 3
                          (first time register effected)

( 9) addr 2 3 2         # Register 2 += register 3

(10) bani 2 16777215 2  # Bitand to set register 2 before next opcode

(11) muli 2 65899 2     # Register 2 * large number

(12) bani 2 16777215 2  # Same as 10

(13) gtir 256 5 3       # Set register 3 to 0 until register 5 > 256(2^8)
                          register 5 is set from 6

(14) addr 3 4 4         # While register 5 < 256
                          this sets IP to skip next opcode

(15) addi 4 1 4         # IP += 1 so skips next opcode

(16) seti 27 3 4        # If not skipped above then IP set to 27 (28 after +1)

(17) seti 0 8 3         # Sets 3 to 0

(18) addi 3 1 1         # Makes register 1 1 if reached from 17

(19) muli 1 256 1       # Multiplies register 1 * 2^8

(20) gtrr 1 5 1         # Register 1 becomes 1 if greater than register 5

(21) addr 1 4 4         # IP += previous result
                          so skips 22 if register 1 > register 5

(22) addi 4 1 4         # Skips 23 thus entering a loop

(23) seti 25 4 4        # Skips IP to 26

(24) addi 3 1 3         # Register 3 increments by 1

(25) seti 17 2 4        # Goes back to 18 - looping until 23 is hit
                          i.e. register 1 > register 5

(26) setr 3 9 5         # Value of register 5 set to register 3

(27) seti 7 9 4         # Sets IP to 7 so i goes to 8 after +1

(28) eqrr 2 0 3         # From 16 - sets 3 to 1 if register 2 == register 0
                          so initialise 0 (otherwise unused)  to this to
                          make the program terminate the quickest

(29) addr 3 4 4         # If above resulted in 1 then program halts

(30) seti 5 0 4         # Starts again at 6

Approach:
    Find initial value of register 2 at 28 for quickest halt value
    For longest track this value then when it repeats take the one
    before it - previous value kept on a perpetually changing variable
    whereas the repeat checking is done with set for lookup speed
"""


def main():
    """Run opcodes with registers initialised to 0 to identify halt values."""
    with open('input.txt') as f:
        lines = [x.strip() for x in f.readlines()]
        start_ip = int(lines[0].split()[1])
        opcodes = []
        for line in lines[1:]:
            split = line.split()
            parsed = (split[0], int(split[1]), int(split[2]), int(split[3]))
            opcodes.append(parsed)

        reg_twos = set()
        prev_reg_two = None
        registers = [0, 0, 0, 0, 0, 0]
        position = 0
        while True:
            if position == 28:
                if not reg_twos:
                    # Answer One
                    print("Register 0 causing quickest halt:", registers[2])

                # Track register 2 values at this potential halting point
                if registers[2] in reg_twos:
                    # Answer Two
                    print("Register 0 causing slowest halt:", prev_reg_two)
                    break
                prev_reg_two = registers[2]
                reg_twos.add(registers[2])

            opcode = opcodes[position]

            registers[start_ip] = position

            function_dispatch(registers, opcode)

            position = registers[start_ip] + 1


if __name__ == '__main__':
    main()
