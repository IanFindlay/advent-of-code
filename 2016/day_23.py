"""Advent of Code Day 23 - Safe Cracking"""

from collections import defaultdict


def is_num(s):
    """Determine whether a string is a number or not."""
    try:
        int(s)
    except ValueError:
        return False
    return True


def do_ops(start_a):
    """Carry out operations and return the value of register 'a'."""
    registers = defaultdict(int)
    registers['a'] = start_a
    i = 0
    while i < len(ops):
        if ops[i][0] == 0:
            if is_num(ops[i][1]):
                registers[ops[i][2]] = ops[i][1]
            else:
                registers[ops[i][2]] = registers[ops[i][1]]

        elif ops[i][0] == 1:
            registers[ops[i][1]] += 1

        elif ops[i][0] == 2:
            registers[ops[i][1]] -= 1

        elif ops[i][0] == 3:
            if is_num(ops[i][1]):
                if ops[i][1] != 0:
                    if is_num(ops[i][2]):
                        i += ops[i][2] - 1
                    else:
                        i += registers[ops[i][2]] - 1

            elif registers[ops[i][1]] != 0:
                if is_num(ops[i][2]):
                    i += ops[i][2] - 1
                else:
                    i += registers[ops[i][2]] - 1

        elif ops[i][0] == 4:
            jump = i + registers[ops[i][1]]
            if jump >= len(ops):
                i += 1
                continue

            if len(ops[jump]) == 2:
                if ops[jump][0] == 1:
                    ops[jump][0] = 2
                else:
                    ops[jump][0] = 1

            else:
                if ops[jump][0] == 3:
                    ops[jump][0] = 0
                else:
                    ops[jump][0] = 3

        elif ops[i][0] == 5:
            # For part two found slow loop and modified it with this and NOPs
            registers['a'] = registers['b'] * registers['d']

        i += 1

    return registers['a']


op_conv = {
    'cpy': 0,
    'inc': 1,
    'dec': 2,
    'jnz': 3,
    'tgl': 4,
    'mul': 5
}

with open('input.txt') as f:
    ops = [line.strip().split(' ') for line in f.readlines()]

for op in ops:
    op[0] = op_conv[op[0]]
    if is_num(op[1]):
        op[1] = int(op[1])
    if len(op) == 3 and is_num(op[2]):
        op[2] = int(op[2])

# Answer One (Change argument to 7) / Answer Two
print("Register a:", do_ops(12))
