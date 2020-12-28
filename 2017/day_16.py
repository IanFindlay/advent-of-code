"""Advent of Code Day 16 - Permutation Promenade"""


def dance(moves, dances):
    """ Return final position of programs after the dance moves are done."""
    programs = 'abcdefghijklmnop'
    program_list = list(programs)
    move_list = moves.strip().split(',')

    completed_dances = 0
    seen = []
    cycle_length = 0

    while completed_dances < dances:
        for move in move_list:
            move = move.strip()

            if move[0] == 's':
                to_spin = []
                spin = int(move[1:])
                for program in program_list[-(spin): len(program_list)]:
                    to_spin.append(program)
                for program in program_list[: -spin]:
                    to_spin.append(program)
                program_list = to_spin

            elif move[0] == 'x':
                parts = move.split('/')
                swap_1 = int(parts[0][1:])
                swap_2 = int(parts[1])
                value_1 = program_list[swap_1]
                value_2 = program_list[swap_2]
                program_list[swap_1] = value_2
                program_list[swap_2] = value_1

            else:

                parts = move.split('/')
                pos_1 = program_list.index(parts[0][1:])
                pos_2 = program_list.index(parts[1])
                program_list[pos_1] = parts[1]
                program_list[pos_2] = parts[0][1:]

        end_formation = ''.join(program_list)

        if dances == 1:
            return end_formation

        if end_formation in seen:
            cycle_length = completed_dances + 1
            remaining = dances % cycle_length
            completed_dances = dances - remaining
            seen = []

        else:
            completed_dances += 1
            seen.append(programs)

        programs = end_formation

    return programs


with open('inputs/day_16.txt') as f:
    moves = f.read()

# Answer One
print('Position after first dance: ' + str(dance(moves, 1)))

# Answer Two
print('Position after billionth dance: '
        + str(dance(moves, 1000000000)))
