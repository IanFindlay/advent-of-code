#!/usr/bin/env python3

"""Advent of Code 2020 Day 22 - Crab Cups."""


with open('inputs/2020_23.txt') as f:
    cups = [int(x) for x in f.read().strip()]

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
