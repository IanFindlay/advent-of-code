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


def update_axis_sets(axis_sets, axis, pos_values, vel_values):
    """Update axis_sets dictionary with values if new otherwise return True."""
    new_tuple = tuple(pos_values) + tuple(vel_values)
    if new_tuple in axis_sets[axis]:
        return True
    else:
        axis_sets[axis].add(new_tuple)
        return False


def prime_factors(n):
    """Return tuple of prime factors of n."""
    factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            n /= i
            factors.append(i)
        else:
            i += 1

    return tuple(factors)


with open('input.txt', 'r') as f:
    scan = f.read().strip().split('\n')

original_moon_positions = {}
original_moon_velocities = {}
moons = ['Callisto', 'Ganymede', 'Europa', 'Io']
for moon in scan:
    split_values = moon.strip().split(',')
    x = int(split_values[0][3:])
    y = int(split_values[1][3:])
    z = int(split_values[2][3: -1])
    moon_name = moons.pop()
    original_moon_positions[moon_name] = [x, y, z]
    original_moon_velocities[moon_name] = [0, 0, 0]

moon_positions = original_moon_positions.copy()
moon_velocities = original_moon_velocities.copy()
for _ in range(1000):
    moon_steps(moon_positions, moon_velocities)

total_energy = 0
for moon in moon_positions:
    potential = sum([abs(x) for x in moon_positions[moon]])
    kinetic = sum([abs(x) for x in moon_velocities[moon]])
    total_energy += potential * kinetic

# Answer One
print("Total energy in the system:", total_energy)

moon_positions = original_moon_positions.copy()
moon_velocities = original_moon_velocities.copy()

# Find cycle lengths of each axis then the LCM
moons = ['Io', 'Europa', 'Ganymede', 'Callisto']
x_pos = []
y_pos = []
z_pos = []
for moon in moons:
    x, y, z = moon_positions[moon]
    x_pos.append(x)
    y_pos.append(y)
    z_pos.append(z)

axis_sets = {'x': set(), 'y': set(), 'z': set()}
axis_sets['x'].add((tuple(x_pos) + (0, 0, 0)))
axis_sets['y'].add((tuple(y_pos) + (0, 0, 0)))
axis_sets['z'].add((tuple(z_pos) + (0, 0, 0)))

cycles = [None, None, None]
steps = 0
while None in cycles:
    moon_steps(moon_positions, moon_velocities)
    x_pos, x_vel = [], []
    y_pos, y_vel = [], []
    z_pos, z_vel = [], []
    for moon in moons:
        x, y, z = moon_positions[moon]
        x_pos.append(x)
        y_pos.append(y)
        z_pos.append(z)
        x, y, z = moon_velocities[moon]
        x_vel.append(x)
        y_vel.append(y)
        z_vel.append(z)

    if not cycles[0] and update_axis_sets(axis_sets, 'x', x_pos, x_vel):
        cycles[0] = steps
    if not cycles[1] and update_axis_sets(axis_sets, 'y', y_pos, y_vel):
        cycles[1] = steps
    if not cycles[2] and update_axis_sets(axis_sets, 'z', z_pos, z_vel):
        cycles[2] = steps

    steps += 1

lcm_factors = {}
for cycle_length in cycles:
    factors = prime_factors(cycle_length)
    for factor in factors:
        count = factors.count(factor)
        if factor not in lcm_factors or count > lcm_factors[factor]:
            lcm_factors[factor] = count

lcm = 1
for factor, power in lcm_factors.items():
    lcm *= factor * power

# Answer Two
print("Number of cycles until previous state reached:", lcm)
