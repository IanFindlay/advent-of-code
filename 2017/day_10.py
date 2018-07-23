"""Advent of Code Day 10 - Knot Hash"""


def hashed(lengths, rounds):
    """Carry out a simulation of a knot tying hash given length inputs. """
    notches = list(range(256))
    skip = 0
    pos = 0
    for __ in range(rounds):
        for length in lengths:
            to_rev = []
            for i in range(length):
                to_rev.append(notches[(pos + i) % 256])

            for j in range(length):
                notches[(pos + j) % 256] = to_rev.pop()
            pos += skip + length
            skip += 1

    return notches


def dense(sparse):
    """Turn a sparse hash into a dense hash by XORing 16 digit blocks."""
    dense = []
    position = 0
    while position + 16 <= len(sparse):
        total = sparse[position]
        for pos in range(position + 1, position + 16):
            total = total ^ sparse[pos]
        dense.append(total)
        position += 16

    return dense


if __name__ == '__main__':

    puzzle_input = '230,1,2,221,97,252,168,169,57,99,0,254,181,255,235,167'
    puzzle_list = [int(x) for x in puzzle_input.split(',')]
    ascii_input = [ord(c) for c in ''.join(puzzle_input)]
    [ascii_input.append(length) for length in (17, 31, 73, 47, 23)]

    # Answer One
    notches = hashed(puzzle_list, 1)
    print("Product of first two numbers in hash:", notches[0] * notches[1])

    # Answer Two
    hexed = "".join([format(num, '02x') for num in dense(hashed(ascii_input, 64))])
    print("Knot hash:", hexed)
