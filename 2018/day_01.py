"""Advent of Code Day 1 - Chronal Calibration"""


with open('input.txt') as f:
    shifts = [int(x) for x in f.readlines()]

# Answer One
print("The final frequency is:", sum(shifts))

frequencies = set([0])
frequency = 0
no_repeats = True
while no_repeats:
    for shift in shifts:
        frequency += shift
        if frequency in frequencies:
            no_repeats = False
            break
        frequencies.add(frequency)

# Answer Two
print("The first repeated frequency is:", frequency)
