"""Advent of Code Day 14 - Disk Defragmentation"""

import collections


def build_grid(key_string, num_rows, num_cols):
    """Build coordinate grid of used squares."""
    squares = set()
    num = 0
    for row in range(num_rows):
        to_hash = [ord(c) for c in '{}-{}'.format(key_string, str(num))]
        [to_hash.append(length) for length in (17, 31, 73, 47, 23)]
        hexed = hashed(to_hash)
        binned = ''.join([bin(int(c, 16))[2:].zfill(4) for c in hexed])
        num += 1
        for col in range(num_cols):
            if binned[col] == '1':
                squares.add((col, row))

    return squares


def hashed(lengths):
    """Carry out a simulation of a knot tying hash given length inputs."""
    notches = list(range(256))
    skip = 0
    pos = 0
    for __ in range(64):
        for length in lengths:
            to_rev = []
            for i in range(length):
                to_rev.append(notches[(pos + i) % 256])

            for j in range(length):
                notches[(pos + j) % 256] = to_rev.pop()
            pos += skip + length
            skip += 1

    return dense(notches)


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

    return "".join([format(num, '02x') for num in dense])


def identify_regions():
    """Run a DFS of adjacent used squares to find number of distinct regions."""
    regions = 0
    while squares:
        to_process = collections.deque(squares.pop())
        prev = set()
        while to_process:
            y = to_process.pop()
            x = to_process.pop()
            adjacent = ((x+1, y), (x-1, y), (x, y+1), (x, y-1))
            for neighbour in adjacent:
                if neighbour in squares and neighbour not in prev:
                    prev.add(neighbour)
                    to_process.append(neighbour[0])
                    to_process.append(neighbour[1])
        regions += 1
        for processed in prev:
            squares.remove(processed)

    return regions


if __name__ == '__main__':
    seed = 'amgozmfv'
    squares = build_grid(seed, 128, 128)

    # Answer One
    print("Number of used squares:", len(squares))

    # Answer Two
    print("Number of regions:", identify_regions())
