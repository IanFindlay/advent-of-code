"""Answers to Advent of Code Day 18."""


def duet(directions):
    """Return the final recovered note of a list of instructions."""
    registers = {}
    sound = 0
    recovered = 0
    instruction_list = directions.strip().split('\n')

    count = 0
    while count < len(instruction_list):
        instruction = instruction_list[count]

        modification = instruction[:3]
        target = instruction[4]
        change = instruction[6:]
        int_change = False

        if target not in registers and target.isalpha() is True:
            registers[target] = 0

        if change.isalpha() is False and change != '':
            change = int(change)
            int_change = True

        if modification == 'snd':
            if target.isalpha() is True:
                sound = registers[target]
            else:
                sound = target

        elif modification == 'set':
            if int_change is True:
                registers[target] = change
            else:
                registers[target] = registers[change]

        elif modification == 'add':
            if int_change is True:
                registers[target] += change
            else:
                registers[target] += registers[change]

        elif modification == 'mul':
            if int_change is True:
                registers[target] *= change
            else:
                registers[target] *= registers[change]

        elif modification == 'mod':
            if int_change is True:
                registers[target] = registers[target] % change
            else:
                registers[target] = registers[target] % registers[change]

        elif modification == 'rcv':
            if target.isalpha() is True and registers[target] != 0:
                recovered = sound
            elif target.isalpha() is False and target != 0:
                recovered = sound
            if recovered != 0:
                break

        elif modification == 'jgz':
            if target.isalpha() is True and registers[target] > 0:
                if int_change is True:
                    count += change - 1
                else:
                    count += registers[change] - 1

            elif target.isalpha() is False and int(target) > 0:
                if int_change is True:
                    count += change - 1
                else:
                    count += registers[change] - 1

        count += 1

    print('First Non-Zero Recovered Frequency: ' + str(recovered))


with open('input.txt') as f:
    INSTR = f.read()
    duet(INSTR)
