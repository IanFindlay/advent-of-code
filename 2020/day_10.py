#!/usr/bin/env python3

"""Advent of Code 2020 Day 10 - Adapter Array."""


with open ('inputs/day_10.txt', 'r') as adapters:
    outputs = [int(number.strip()) for number in adapters.readlines()]

outputs.append(max(outputs) + 3)
outputs.append(0)
available_adapters = set(outputs)

joltage_dict = {}
for output in outputs:
    joltage_dict[output] = set()
    for number in range(output - 3, output):
        if number in available_adapters:
            joltage_dict[output].add(number)

used_adapters = set()
while len(used_adapters) < len(available_adapters) - 1:
    for joltage, possible_adapters in joltage_dict.items():
        if len(possible_adapters) == 1:
            used_adapters.update(possible_adapters)
            continue

        unused = set()
        for adapter in possible_adapters:
            if adapter not in used_adapters:
                unused.add(adapter)

        joltage_dict[joltage] = unused

del joltage_dict[0]

diff_of_one = 0
diff_of_three = 0
for adapter, connected_to in joltage_dict.items():
    connected = connected_to.pop()
    if adapter - connected == 1:
        diff_of_one += 1
    elif adapter - connected == 3:
        diff_of_three += 1

# Answer One
print("1-jolt multiplied by 3-jolt differences:", diff_of_one * diff_of_three)

del outputs[-1]  # Remove 0 from output options
adapter_paths = {}
adapter_paths[0] = 1
for adapter in sorted(outputs):
    paths_to = 0
    for n in (1, 2, 3):
        paths_to += adapter_paths.get(adapter - n, 0)
    adapter_paths[adapter] = paths_to

# Answer Two
print("Number of ways to arrange adapters to connect outlet to device:",
      adapter_paths[outputs[-1]])
