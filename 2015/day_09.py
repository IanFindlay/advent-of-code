"""Advent of Code Day 9 - All in a Single Night"""

import itertools
import re

with open('input.txt') as f:
    routes = [route.strip() for route in f]

# Parse routes and make list of places for permutation
places = set()
for route in routes:
    info = route.split(' ')
    start = info[0]
    destination = info[2]
    places.add(start)
    places.add(destination)
    
# Generate journey permutations
permutations = list(itertools.permutations(places))

# Go through permutations calculating distance
shortest = 1000
longest = 0
for permutation in permutations:
    overall_distance = 0
    i = 0
    while i < len(permutation) - 1:
        start = permutation[i]
        destination = permutation[i + 1]

        # Copy routes list as a string for regex purposes
        regex_routes = ' '.join(routes)
        journey_regex = re.compile(r'{} to {} = (\d*)'.format(start, destination))
        alt_regex = re.compile(r'{} to {} = (\d*)'.format(destination, start))

        # Search for permutation from input.txt info in both possible formats
        if journey_regex.search(regex_routes):
            distance = journey_regex.search(regex_routes).group(1)
        else:
            distance = alt_regex.search(regex_routes).group(1)

        overall_distance += int(distance)
        
        i += 1
    
    if overall_distance < shortest:
        shortest = overall_distance
    
    if overall_distance > longest:
        longest = overall_distance
    
print("Answer One: The Shortest Route Has a Distance of {}".format(shortest))

print("Answer Two: The Longest Route Has a Distance of {}".format(longest))
