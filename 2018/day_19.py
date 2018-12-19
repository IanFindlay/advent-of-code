"""Advent of Code Day 19 - Go With The Flow"""

import collections


def function_dispatch(registers, opcode):
    """Dispatcher - gets key from opcode then runs appropriate function."""
    functions = {
        'addr': add_register,
        'addi': add_immediate,
        'mulr': multiply_register,
        'muli': multiply_immediate,
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


def main():
    """Run the program until its completion."""

    with open('input.txt') as f:
        lines = [x.strip() for x in f.readlines()]

    start_ip = int(lines[0].split()[1])

    instructions = []
    for line in lines[1:]:
        split = line.split()
        parsed = (split[0], int(split[1]), int(split[2]), int(split[3]))
        instructions.append(parsed)

    function_calls = collections.defaultdict(int)
    registers = [0, 0, 0, 0, 0, 0]
    position = 0
    while True:
        try:
            instruction = instructions[position]
        except IndexError:
            break
        # Get an idea of the possible slowdown for part two
        function_calls[(position, instruction[0])] += 1

        registers[start_ip] = position

        function_dispatch(registers, instruction)

        position = registers[start_ip] + 1

    # Answer One
    print("Register 0 after program halts:", registers[0])

    # Program analysis for Part Two
    """
    Registers start: [1, 0, 0, 0, 0, 0]
    Registers coded: [0, 1, 2, 3, 4, 5]
                              (ip)

    Three groups of instructions:
        Called pre-main loop (setup main loop numbers)
        Main, lengthy loop
        Small part separating instances of main loop

    Main loop seems to be centered around instructions 3-11:
        3:  mulr 4, 1, 5
        4:  egrr 5, 2, 5
        5:  addr 5, 3, 3
        6:  addi 3, 1, 3
        8:  addi 1, 1, 1
        9:  gtrr 1, 2, 5
        10: addr 3, 5, 3
        11: seti 2, 9, 3

        Loop starts with [0, 1, 10551340, 2, 1, 10550400]

        3:
        register[4] * register[1] --> register[5]
        [0, 1, 10551340, 3, 1, 1]

        4:
        register[5] == 1 if it currently equals register[2]
        [0, 1, 10551340, 4, 1, 0]

        5:
        register[5] + register[3] into register[3]...
        This breaks the loop when register 5 is 1 as it leads to
        instruction[7] which is not part of the loop
        So register 5 has to get up to limiting registers?
        [0, 1, 10551340, 5, 1, 0]

        6:
        register[3] + 1
        IP incremented beyond loop diverting 7
        [0, 1, 10551340, 7, 1, 0]

        {7:
            Not in this loop but a brief diversion from it
            Adds register 4 to register 0 (which is the important register)
        }

        8:
        register[1] += 1
        Increments register meaning instruction[3] increments 5
        [0, 2, 10551340, 8, 1, 0]

        9:
        register[1] > register[2] then register[5] == 1 else 0
        Another increment - this is looking like checking all numbers
        below per-loop build up of register[5]?
        [0, 2, 10551340, 9, 1, 0]

        10:
        register[3] + register[5] --> register[3]
        Same as 5 yet another incrementing function
        When 5 gets to 1 end up at 12 which increments register[4]
        [0, 2, 10551340, 10, 1, 0]

        11:
        register[3] = 2
        Resets ip to preloop (once +1 applied) and finished loop
        [0, 2, 10551340, 2, 1, 0]

        Changes from start of loop:

            register[0] Untouched
            register[1] Incremented
            register[2] Untouched - limit of somekind
            register[3] IP - cycles by definition
            register[4] Untouched but instruction[3] indicates it is used
            register[5] 0 from large number - relation with register 2?


        Rest of program:
        Instruction[0] GOTO 17 values of registers 2 and 4 then enter loop

        Overall:

            Looks like the program generates two large numbers and then checks
            all numbers below the smaller one (register 5 at the start of the
            loop) to see if any other number below it multiplies with it to
            make the larger (register 2) number.
            No connection between the large numbers beyond the smaller being
            some sort of a limit to the factor checking.
            Any factors found with the equality checks results in temporarily
            breaking from the loop above to add it to register 0 and then the
            search begins again.
            So the answer is the sum of all the factors of the largest number
            as the limit imposed by the other one does nothing but stall the
            program beyond the range that needs to be checked for factors
    """

    # Answer Two
    print("Sum of the factors of 10551340: 22674960")


if __name__ == '__main__':

    main()
