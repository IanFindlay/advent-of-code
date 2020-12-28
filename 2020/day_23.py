#!/usr/bin/env python3

"""Advent of Code 2020 Day 23 - Crab Cups."""


with open('inputs/day_23.txt') as f:
    arranged_cups = [int(x) for x in f.read().strip()]
    cups = arranged_cups.copy()

current_cup = cups[0]
for _ in range(100):
    cc_index = cups.index(current_cup)
    removed_three = cups[cc_index + 1: cc_index + 4]
    i = 0
    while len(removed_three) != 3:
        removed_three.append(cups[i])
        i += 1
    for cup in removed_three:
        cups.remove(cup)

    destination_num = current_cup - 1
    if destination_num < min(cups):
        destination_num = max(cups)
    if destination_num in removed_three:
        while True:
            destination_num -= 1
            if destination_num in cups:
                destination_cup = destination_num
                break
            if destination_num < min(cups):
                destination_num = max(cups)
                break

    destination_index = cups.index(destination_num)
    for _ in range(3):
        cups.insert(destination_index + 1, removed_three.pop())

    current_cup = cups[(cups.index(current_cup) + 1) % len(cups)]

one_index = cups.index(1)
labels = ''
index = one_index + 1
while index != one_index:
    labels += str(cups[index])
    index = (index + 1) % len(cups)

# Answer One
print("Labels on the cup after cup 1:", labels)

cups = {}
for index, cup in enumerate(arranged_cups[:-1]):
    cups[cup] = arranged_cups[index + 1]
cups[arranged_cups[-1]] = max(cups) + 1
for i in range(max(cups) + 1, 1000000):
    cups[i] = i + 1
cups[1000000] = arranged_cups[0]

current_cup = arranged_cups[0]
for _ in range(10000000):
    removed_three = []
    cup_to_remove = current_cup
    for _ in range(3):
        cup_to_remove = cups[cup_to_remove]
        removed_three.append(cup_to_remove)

    # Last cup to remove's adjacent is new current cup adjacent
    cups[current_cup] = cups[cup_to_remove]

    destination_num = current_cup - 1
    min_circle = [x for x in range(1, 4) if x not in removed_three]
    max_circle = [x for x in range(999997, 1000001) if x not in removed_three]
    if destination_num < min_circle[0]:
        destination_num = max_circle[-1]
    elif destination_num in removed_three:
        while True:
            destination_num -= 1
            if destination_num not in removed_three:
                break
            if destination_num < min_circle[0]:
                destination_num = max_circle[-1]
                break

    current_adjacent = cups[destination_num]
    cups[destination_num] = removed_three[0]
    cups[removed_three[1]] = removed_three[2]
    cups[removed_three[2]] = current_adjacent

    current_cup = cups[current_cup]

first_cup = cups[1]
product = first_cup * cups[first_cup]

# Answer Two
print("Product of the two cups immediately clockwise from cup 1:", product)
