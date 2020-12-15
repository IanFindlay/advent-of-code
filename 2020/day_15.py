#!/usr/bin/env python3

"""Advent of Code 2020 Day 15 - Rambunctious Recitation."""


starting_numbers = [11, 0, 1, 10, 5, 19]
spoken_dict = {}
spoken_set = set()
last_spoken = None
turn = 1
while turn <= 2020:

    if starting_numbers:
        number = starting_numbers[0]
        spoken_dict[number] = [turn]
        spoken_set.add(number)
        starting_numbers = starting_numbers[1:]

    else:
        if last_spoken not in spoken_set:
            number = 0
        else:
            if len(spoken_dict[last_spoken]) == 1:
                number = 0
            else:
                before_prev, prev = spoken_dict[last_spoken]
                number = prev - before_prev

        if number not in spoken_set:
            spoken_set.add(number)
            spoken_dict[number] = [turn]
        else:
            spoken_dict[number].append(turn)
            if len(spoken_dict[number]) == 3:
                spoken_dict[number] = spoken_dict[number][1:]

    last_spoken = number
    turn += 1

# Answer One
print("2020th Number spoken:", last_spoken)
