"""Advent of Code Day 6 - Probably a Fire Hazard"""

import re

# Generate Lights (x, y, 0/1)
lights = []

for x in range(1000):
    for y in range(1000):
        lights.append([x, y, 0])

with open('inputs/day_06.txt') as f:
    instructions = f.readlines()

for instruction in instructions:
    # Parse instruction
    if 'on' in instruction:
        action = 'on'
    elif 'off' in instruction:
        action = 'off'
    if 'toggle' in instruction:
        action = 'toggle'

    # Isolate coord pairs/coords
    coords_regex = re.compile(r'([0-9,]*) through ([0-9,]*)')
    first_coords = coords_regex.search(instruction).group(1)
    last_coords = coords_regex.search(instruction).group(2)
    first_x = int(first_coords.split(',')[0])
    last_x = int(last_coords.split(',')[0])
    first_y = int(first_coords.split(',')[1])
    last_y = int(last_coords.split(',')[1])

    # Select specified rectangle
    x_offset = last_x - first_x
    y_offset = last_y - first_y

    for x in range(first_x, first_x + x_offset + 1):
        for y in range(first_y, first_y + y_offset + 1):
            # Calculate list position
            position = x * 1000 + y

            if action == 'on':
                lights[position] = [x, y, 1]

            elif action == 'off':
                lights[position] = [x, y, 0]

            elif action == 'toggle':
                if lights[position][2] ==  0:
                    lights[position] = [x, y, 1]
                elif lights[position][2] == 1:
                    lights[position] = [x, y, 0]

on = 0
for light in lights:
    if light[2] == 1:
        on += 1

print("Answer One =", on)

lights = []

for x in range(1000):
    for y in range(1000):
        lights.append([x, y, 0])

for instruction in instructions:
    # Parse instruction
    if 'on' in instruction:
        action = 'on'
    elif 'off' in instruction:
        action = 'off'
    if 'toggle' in instruction:
        action = 'toggle'

    # Isolate coord pairs/coords
    coords_regex = re.compile(r'([0-9,]*) through ([0-9,]*)')
    first_coords = coords_regex.search(instruction).group(1)
    last_coords = coords_regex.search(instruction).group(2)
    first_x = int(first_coords.split(',')[0])
    last_x = int(last_coords.split(',')[0])
    first_y = int(first_coords.split(',')[1])
    last_y = int(last_coords.split(',')[1])

    # Select specified rectangle
    x_offset = int(last_x) - int(first_x)
    y_offset = int(last_y) - int(first_y)

    for x in range(first_x, first_x + x_offset + 1):
        for y in range(first_y, first_y + y_offset + 1):
            # Calculate list position
            position = x * 1000 + y

            if action == 'on':
                brightness = lights[position][2]
                lights[position] = [x, y, brightness + 1]

            elif action == 'off':
                brightness = lights[position][2]
                if brightness != 0:
                    lights[position] = [x, y, brightness - 1]

            elif action == 'toggle':
                brightness = lights[position][2]
                lights[position] = [x, y, brightness + 2]

overall_brightness = 0
for light in lights:
    overall_brightness += light[2]

print("Answer Two =", overall_brightness)
