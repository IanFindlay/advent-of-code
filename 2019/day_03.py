"""Advent of Code 2019 Day 03 - Crossed Wires."""



def wire_path(wire):
    """Plot wire path and return coords set and coords: No. of steps dict."""
    wired = set()
    steps = {}
    num_steps = 1
    wire_end = [0, 0]
    for path in wire:
        direction = path[0]
        distance = int(path[1:])

        if direction == 'R':
            for moved in range(1, distance + 1):
                wired.add((moved + wire_end[0], wire_end[1]))
                steps[(moved + wire_end[0], wire_end[1])] = num_steps
                num_steps += 1
            wire_end[0] = distance + wire_end[0]


        elif direction == 'L':
            for moved in range(1, distance + 1):
                wired.add((wire_end[0] - moved, wire_end[1]))
                steps[(wire_end[0] - moved, wire_end[1])] = num_steps
                num_steps += 1
            wire_end[0] = wire_end[0] - distance


        elif direction == 'U':
            for moved in range(1, distance + 1):
                wired.add((wire_end[0], moved + wire_end[1]))
                steps[(wire_end[0], moved + wire_end[1])] = num_steps
                num_steps += 1
            wire_end[1] = distance + wire_end[1]


        elif direction == 'D':
            for moved in range(1, distance + 1):
                wired.add((wire_end[0], wire_end[1] - moved))
                steps[(wire_end[0], wire_end[1] - moved)] = num_steps
                num_steps += 1
            wire_end[1] = wire_end[1] - distance

    return wired, steps


with open('inputs/day_03.txt') as f:
    wire_paths = [path.split(',') for path in f.read().split()]

wire_path_1, num_steps_1 = wire_path(wire_paths[0])
wire_path_2, num_steps_2 = wire_path(wire_paths[1])
intersections = wire_path_1 & wire_path_2

nearest = None
for crossed in intersections:
    manhat_distance = abs(crossed[0]) + abs(crossed[1])
    if not nearest or manhat_distance < nearest:
        nearest = manhat_distance

# Answer One
print("Manhattan distance from central port to nearest intersection:", nearest)

fewest_steps = None
for crossed in intersections:
    combined_steps = num_steps_1[crossed] + num_steps_2[crossed]
    if not fewest_steps or combined_steps < fewest_steps:
        fewest_steps = combined_steps

# Answer Two
print("Fewest combined steps to reach an intersection:", fewest_steps)

