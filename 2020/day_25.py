#!/usr/bin/env python3

"""Advent of Code 2020 Day 25 - Combo Breaker."""


with open('inputs/day_25.txt') as f:
    card_key, door_key = [int(line.strip()) for line in f.readlines()]

num = 1
loops = 0
while True:
    loops += 1
    num *= 7
    num = num % 20201227
    if num == card_key:
        break

num = 1
for loop in range(loops):
    num = num * door_key
    num = num % 20201227

# Answer One
print("Encryption Key:", num)
