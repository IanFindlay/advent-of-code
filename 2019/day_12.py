"""Advent of Code 2019 Day 12 - The N-Body Problem."""


def moon_steps(moon_positions, moon_velocities):
    """Take a time step simulating the movement of the moons."""
    for moon, position in moon_positions.items():
        for other_moon, other_position in moon_positions.items():
            if moon == other_moon:
                continue
            for i in range(3):
                if position[i] > other_position[i]:
                    moon_velocities[moon][i] -= 1
                elif position[i] < other_position[i]:
                    moon_velocities[moon][i] += 1

    for moon, position in moon_positions.items():
        for i in range(3):
            position[i] += moon_velocities[moon][i]

    return moon_positions


with open('input.txt', 'r') as f:
    scan = f.read().strip().split('\n')

moon_positions = {}
moon_velocities = {}
moons = ['Callisto', 'Ganymede', 'Europa', 'Io']
for moon in scan:
    split_values = moon.strip().split(',')
    x = int(split_values[0][3:])
    y = int(split_values[1][3:])
    z = int(split_values[2][3: -1])
    moon_name = moons.pop()
    moon_positions[moon_name] = [x, y, z]
    moon_velocities[moon_name] = [0, 0, 0]

first_simulation = (moon_positions.copy(), moon_velocities.copy())
for _ in range(1000):
    moon_steps(first_simulation[0], first_simulation[1])

total_energy = 0
for moon in first_simulation[0]:
    potential = sum([abs(x) for x in first_simulation[0][moon]])
    kinetic = sum([abs(x) for x in first_simulation[1][moon]])
    total_energy += potential * kinetic

# Answer One
print("Total energy in the system:", total_energy)





