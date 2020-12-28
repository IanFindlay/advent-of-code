"""Advent of Code Day 21 - Scrambled Letters and Hash"""

from itertools import permutations


def scramble(password, operations):
    """Scramble a string via a list of operations."""
    pass_list = [char for char in password]
    for operation in operations:
        parse = operation.split(' ')
        if parse[0] == 'swap':
            if parse[1] == 'position':
                temp = pass_list[int(parse[2])]
                pass_list[int(parse[2])] = pass_list[int(parse[-1])]
                pass_list[int(parse[-1])] = temp
            else:
                x_pos = pass_list.index(parse[2])
                y_pos = pass_list.index(parse[-1])
                temp = pass_list[x_pos]
                pass_list[x_pos] = pass_list[y_pos]
                pass_list[y_pos] = temp

        if parse[0] == 'rotate':
            if parse[1] == 'left':
                for _ in range(int(parse[2])):
                    pass_list.append(pass_list.pop(0))

            elif parse[1] == 'right':
                for _ in range(int(parse[2])):
                    pass_list.insert(0, pass_list.pop(-1))

            elif parse[1] == 'based':
                index = pass_list.index(parse[-1])
                for _ in range(index + 1):
                    pass_list.insert(0, pass_list.pop(-1))
                if index >= 4:
                    pass_list.insert(0, pass_list.pop(-1))

        if parse[0] == 'reverse':
            start = int(parse[2])
            end = int(parse[-1])
            pass_str = ''.join(pass_list)
            if start == 0:
                new_str = pass_str[end::-1] + pass_str[end+1:]
            else:
                new_str = pass_str[0:start] + pass_str[end:start-1:-1] + pass_str[end + 1:]

            pass_list = [char for char in new_str]

        if parse[0] == 'move':
            pass_list.insert(int(parse[-1]), pass_list.pop(int(parse[2])))

    return ''.join(pass_list)


with open('inputs/day_21.txt') as f:
    lines = [line.strip() for line in f.readlines()]

# Answer One
print("Scrambled password:", scramble('abcdefgh', lines))

perms = permutations('abcdefgh')
for perm in perms:
    if scramble(perm, lines) == 'fbgdceah':
        # Answer Two
        print("Unscrambled password:", ''.join(perm))
        break
