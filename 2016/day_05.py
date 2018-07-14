""" Advent of Code Day 5 - How About a Nice Game of Chess?"""

import hashlib


def find_pass(door_id, part_two=False):
    """Find password by finding significant hashed then hexed values."""
    if part_two:
        password = ['', '', '', '', '', '', '', '']
    else:
        password = ''
    number = 0
    found = 0
    while found < 8:
        hexed = hashlib.md5('{}{}'.format(door_id, number).encode('utf-8')).hexdigest()
        if str(hexed)[0:5] == '00000':
            if part_two:
                pos = hexed[5]
                if pos.isnumeric() and int(pos) < 8 and password[int(pos)] == '':
                    password[int(pos)] = str(hexed[6])
                    found += 1
            else:
                password += str(hexed[5])
                found += 1

        number += 1

    if part_two:
        return ''.join(password)

    return password


door_id = 'ojvtpuvg'

# Answer One
print("First Door Password:", find_pass(door_id))

# Answer Two
print("Second Door Password:", find_pass(door_id, part_two=True))
