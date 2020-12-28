"""Advent of Code 2019 Day 6 - Universal Orbit Map."""


with open('inputs/day_06.txt', 'r') as f:
    orbits = f.read().split()

objects_dict = {}
for orbit in orbits:
    orbited, orbiter = orbit.split(')')
    objects_dict[orbiter] = orbited

num_orbits = 0
for orbiter in objects_dict:
    next_orbit = objects_dict.get(orbiter, None)
    while next_orbit:
        next_orbit = objects_dict.get(next_orbit, None)
        num_orbits += 1

# Answer One
print("Number of direct and indirect orbits:", num_orbits)

you_path = {}
on_you_path = set()
transfers = 0
next_orbit = objects_dict.get("YOU", None)
while next_orbit:
    transfers += 1
    you_path[next_orbit] = transfers
    on_you_path.add(next_orbit)
    next_orbit = objects_dict.get(next_orbit, None)

transfers = 0
next_orbit = objects_dict.get("SAN", None)
while next_orbit and next_orbit not in on_you_path:
    transfers += 1
    next_orbit = objects_dict.get(next_orbit, None)

# Answer Two
print("Transfers between you and Santa:", transfers + you_path[next_orbit] - 1)
