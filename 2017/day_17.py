"""Advent of Code Day 17 - Spinlock"""

def spinlock():
    """Find the value adjacent to a spinlocks final insertion."""
    steps = 304
    position = 0
    to_insert = 1
    buffer = [0]

    insertions = 2017

    while insertions > 0:

        position = (position + steps) % len(buffer)

        temp_buffer = []
        for value in buffer[:position + 1]:
            temp_buffer.append(value)

        temp_buffer.append(to_insert)
        to_insert += 1

        for value in buffer[position + 1:]:
            temp_buffer.append(value)

        position += 1
        buffer = temp_buffer
        insertions -= 1

    if position == len(buffer) - 1:
        adjacent = 0

    else:
        adjacent = position + 1

    return 'Value after 2017 insertions: ' + str(buffer[adjacent])


def spinlock_sequel():
    """Find the value adjacent to 0 after 50000000 insertions."""
    steps = 304
    position = 0
    to_insert = 1
    buffer_length = 1

    insertions = 50000000

    while insertions > 0:

        position = (position + steps) % buffer_length

        if position == 0:
            adjacent = to_insert

        position += 1
        buffer_length += 1
        to_insert += 1
        insertions -= 1

    return adjacent


# Answer One
print("Value after 2017:", spinlock())

# Answer Two
print("Value after 0 once 50000000 is inserted:", spinlock_sequel())
