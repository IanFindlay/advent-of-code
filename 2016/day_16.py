"""Advent of Code Day 16 - Dragon Checksum"""


def dragon(binary):
    """Apply a modified dragon curve transformation and returns the result."""
    dragoned = binary + '0'
    for char in binary[-1::-1]:
        if char == '1':
            dragoned += '0'
        else:
            dragoned += '1'
    return dragoned


def calc_checksum(to_sum):
    """Calculate the checksum of a string and return it."""
    i = 0
    summed = ''
    while i < len(to_sum) - 1:
        if to_sum[i] == to_sum[i+1]:
            summed += '1'
        else:
            summed += '0'

        i += 2

    return summed


to_fill = 35651584           # Change to 272 for part one
data = '01111010110010011'

while len(data) < to_fill:
    data = dragon(data)

checksum = data[:to_fill]

while True:
    checksum = calc_checksum(checksum)
    if len(checksum) % 2 == 1:
        break

# Answer One / Answer Two
print("Checksum:", checksum)
