"""Advent of Code Day 14 - Reindeer Olympics"""

import re


def calc_distance(speed, run_duration, rest_duration, name):
    """Calculates the distance a Reindeer travels in a given time."""
    splits = [name]
    distance = 0
    time = 0
    running = True
    elapsed = 0
    while time < race_duration:
        if running:
            distance += speed
            elapsed += 1
            if elapsed == run_duration:
                running = False
                elapsed = 0

        else:
            elapsed += 1
            if elapsed == rest_duration:
                running = True
                elapsed = 0

        splits.append(distance)
        time += 1

    tracking.append(splits)
    return distance


with open('inputs/day_14.txt') as f:
    reins = f.readlines()

race_duration = 2503
reindeers = {}
tracking = []

longest = 0
for rein in reins:
    name = re.search(r'(\w+) can', rein).group(1)
    reindeers[name] = 0
    speed = int(re.search(r'(\d+) km/s', rein).group(1))
    duration = int(re.search(r'(\d+) seconds,', rein).group(1))
    rest = int(re.search(r'(\d+) seconds\.', rein).group(1))

    distance = calc_distance(speed, duration, rest, name)
    if distance > longest:
        longest = distance

# Answer Part One
print("Longest Distance Travelled =", longest)


for second in range(1, race_duration + 1):
    furthest = 0
    leader = ''
    for reindeer in tracking:
        if reindeer[second] > furthest:
            furthest = reindeer[second]
            leader = reindeer[0]

    reindeers[leader] += 1

# Answer Part Two
most_points = max(reindeers.values())
print("Most Accumulated Points =", most_points)
