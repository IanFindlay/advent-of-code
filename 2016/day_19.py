"""Advent of Code Day 19 - An Elephant Named Joseph"""

import collections

def elf_exchange(elves):
    """Simulate across from eliminations in a circle with arg no. of points."""
    left = collections.deque()
    right = collections.deque()
    for i in range(1, elves + 1):
        # Split around the middle
        if i < (elves // 2) + 1:
            left.append(i)
        else:
            right.append(i)

    while left and right:
        # If odd pop rounded down middle (left) else pop middle (right)
        if len(left) > len(right):
            left.pop()
        else:
            right.popleft()

        # Rotate the middle split
        right.append(left.popleft())
        left.append(right.popleft())

    return left[0]


num_elves = 3005290

# Answer One - Uses binary 'trick' related to the Josephus problem
print("The winning elf:", int(bin(num_elves)[3:] + '1', 2))

# Answer Two
print("The new winning elf:", elf_exchange(num_elves))
