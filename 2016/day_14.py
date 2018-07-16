""" Advent of Code Day 14 - One-Time Pad"""

import re
import hashlib

def key_stretch(key):
    """Repeatedly hash a key then return it."""
    hashed = 0
    while hashed < 2016:
        key = hashlib.md5('{}'.format(key).encode('utf-8')).hexdigest()
        hashed += 1
    return key


def find_keys(salt, part_two=False):
    """Find hash - triple char with a pentuple of that char within 1000 hashes."""
    hash_cache = {}
    keys = []
    i = 0
    while len(keys) < 64:
        if i in hash_cache:
            hexed = hash_cache[i]
        else:
            hexed = hashlib.md5('{}{}'.format(salt, i).encode('utf-8')).hexdigest()
            if part_two:
                hexed = key_stretch(hexed)

        hash_cache[i] = hexed

        triple_regex = re.search(r'(\w)\1{2}', hexed)
        key = False
        if triple_regex:
            repeated = triple_regex.group(1)

            for num in range(0, i):
                if num in hash_cache:
                    del hash_cache[num]

            j = 1
            while j < 1000:
                if i + j in hash_cache:
                    subhex = hash_cache[i + j]
                else:
                    subhex = hashlib.md5('{}{}'.format(salt, i + j).encode('utf-8')).hexdigest()

                    if part_two:
                        subhex = key_stretch(subhex)

                hash_cache[i + j] = subhex

                pent_regex = re.search(r'({})\1\1\1\1'.format(repeated), subhex)
                if pent_regex:
                    key = True
                    break

                j += 1

        if key:
            keys.append(i)

        i += 1
    return(keys[-1])


salt_str = 'ngcjuoqr'

# Answer One
print("Index that generates the 64th key:", find_keys(salt_str))

# Answer Two
print("Index with key stretching:", find_keys(salt_str, part_two=True))
