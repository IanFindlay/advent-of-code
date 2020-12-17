#!/usr/bin/env python3

"""Advent of Code 2020 Day 09 - Encoding Error."""


from itertools import combinations


with open ('inputs/2020_09.txt', 'r') as xmas:
    numbers = [int(number.strip()) for number in xmas.readlines()]

for index, number in enumerate(numbers[25:], 25):
    prev_25 = numbers[index - 25 : index]
    valid_next = set([sum(combo) for combo in combinations(prev_25, 2)])
    if number not in valid_next:
        break

# Answer One
print("First number that is not the sum of two numbers in the previous 25:",
      numbers[index])

target_number = numbers[index]
weakness_found = False
starting_index = 0
while True:
    current_sum = summed_nums = 0
    for number in numbers[starting_index:]:
        current_sum += number
        summed_nums += 1
        if current_sum > target_number:
            break
        if current_sum == target_number:
            weakness_found = True
            break

    if weakness_found:
        break

    starting_index += 1

contiguous_nums = numbers[starting_index: starting_index + summed_nums]
encryption_weakness = min(contiguous_nums) + max(contiguous_nums)

# Answer Two
print("Encryption weakness:", encryption_weakness)
