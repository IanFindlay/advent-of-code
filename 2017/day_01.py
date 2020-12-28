"""Advent of Code Day 1 - Inverse Captcha"""


def captcha_dupes(numbers):
    """Sum only the digits that match the one next in a cyclic string."""
    Total = 0
    for i in range(len(numbers)):
        if numbers[i] == numbers[i - 1]:
            Total += int(numbers[i])
    return Total


def captcha_halfway(numbers):
    """Sum the digits that match the one half way around a cyclic string."""
    total = 0
    for i in range(int(len(numbers) / 2)):
        if numbers[i] == numbers[i + int(len(numbers) / 2)]:
            total += int(numbers[i])

    return total * 2


with open('inputs/day_01.txt') as f:
    captcha = f.read().strip()

# Answer One
print("Captcha:", captcha_dupes(captcha))

# Answer Two
print("Second Captcha:", captcha_halfway(captcha))
