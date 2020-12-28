""" Advent of Code Day 4 - Security Through Obscurity"""

import re

def check_checksum(room):
    """Calculate checksum returning Sector ID if it matches the encoded one."""
    checksum = re.search(r'\[(\w+)]', room).group(1)
    sector_id = int(re.search(r'(\d+)', room).group(1))
    letters = set(re.findall(r'([^-0-9])', room[:-(len(checksum) + 2)]))
    frequencies = {}

    for letter in letters:
        frequencies[letter] = room.count(letter)

    sorted_freq = sorted(frequencies.items(), key=lambda kv: kv[1], reverse=True)

    calc_checksum = []
    for i in range(sorted_freq[0][1], 1, -1):
        top = []
        for freq_tuple in sorted_freq:
            if freq_tuple[1] == i:
                top.append(freq_tuple[0])
            else:
                continue

        sorted_top = sorted(top)
        [calc_checksum.append(letter) for letter in sorted_top]
        if len(calc_checksum) == 5:
            break

    real_checksum = ''.join(calc_checksum[:5])

    if checksum == real_checksum:
        return sector_id

    return 0


def decrypt_name(room):
    """Decrypt shift cypher using Sector ID returning it if 'north' in decrypt."""
    sector_id = int(re.search(r'(\d+)', room).group(1))
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted = ''
    for char in room:
        if char == '-':
            decrypted += ' '
        elif char in alphabet:
            new_char = alphabet[(alphabet.index(char) + sector_id) % 26]
            decrypted += new_char

    if 'north' in decrypted:
        return sector_id

    return 0


with open('inputs/day_04.txt', 'r') as f:
    rooms = [line.strip() for line in f.readlines()]

# Answer One
print("Sum of Valid Rooms:", sum([check_checksum(room) for room in rooms]))

# Answer Two
print("Sector ID of North Pole Storage:", sum(decrypt_name(room) for room in rooms))
