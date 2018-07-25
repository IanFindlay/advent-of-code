"""Advent of Code Day 20 - Particle Swarm"""

import re
import collections


def make_dict():
    """Make a dictionary out of the particle data."""
    with open('input.txt') as f:
        data = [line.strip() for line in f.readlines()]

    particles = {}
    for num, particle in enumerate(data):
        p, v, a = re.findall(r'<(-?\d+),(-?\d+),(-?\d+)>', particle)
        particles[num] = ((([int(x) for x in p])), ([int(x) for x in v]),
                           ([int(x) for x in a]))

    return particles


def find_closest():
    """Simulate particles until one of them is shown to remain closest to zero."""
    closest = [10000,]     # Dummy value so set == 1 parameter doesn't trigger
    while True:
        closest_dist = 1000000
        temp_closest = None
        for num, info in particle_dict.items():

            for i in range(3):
                info[1][i] += info[2][i]
                info[0][i] += info[1][i]

            from_zero = sum([abs(x) for x in info[0]])

            if from_zero < closest_dist:
                closest_dist = from_zero
                temp_closest = num

        closest.append(temp_closest)

        if len(set(closest[-200:])) == 1:
            break

    return closest[-1]


def collisions():
    """Simulate the particles removing any that collide then return those left."""
    tick = 0
    while tick < 1000:  # Large number so remaining particles should have diverged
        position_count = collections.defaultdict(int,)
        for __, info in particle_dict.items():
            for i in range(3):
                info[1][i] += info[2][i]
                info[0][i] += info[1][i]

            position_count[tuple(info[0])] += 1

        to_del = []
        for key, value in position_count.items():
            if value > 1:
                to_del.append(key)

        collided = []
        for position in to_del:
            for key, values in particle_dict.items():
                if tuple(values[0]) == position:
                    collided.append(key)

        for num in collided:
            del particle_dict[num]

        tick += 1

    return len(particle_dict)


if __name__ == '__main__':

    particle_dict = make_dict()

    # Answer One
    print("The particle that will stay closest to 0,0,0:", find_closest())

    particle_dict = make_dict()

    # Answer Two
    print("Number of particles that remain after collisions:", collisions())
