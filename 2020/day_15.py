#!/usr/bin/env python3

"""Advent of Code 2020 Day 15 - Rambunctious Recitation."""


starting_numbers = [11, 0, 1, 10, 5, 19]
spoken_dict = {}
spoken_set = set()
turn = 1

for number in starting_numbers[:-1]:
    spoken_dict[number] = turn
    spoken_set.add(number)
    turn += 1
last_spoken = starting_numbers[-1]

while turn < 30000000:

    if last_spoken not in spoken_set:
        number = 0
    else:
        number = turn - spoken_dict[last_spoken]

    spoken_dict[last_spoken] = turn
    spoken_set.add(last_spoken)

    if turn == 2020:
        # Answer One
        print("2020th Number spoken:", last_spoken)

    last_spoken = number
    turn += 1

# Answer Two
print("30000000th Number spoken:", last_spoken)
