"""Advent of Code 2019 Day 01 - The Tyranny of the Rocket Equation."""


def calculate_recursive_fuel(fuel_mass):
    """Calculate the recursive fuel needed to launch a mass of fuel."""
    new_fuel_mass = fuel_mass // 3 - 2
    if new_fuel_mass <= 0:
        return 0
    return new_fuel_mass + calculate_recursive_fuel(new_fuel_mass)


with open ('inputs/day_01.txt', 'r') as f:
    masses = [int(module_mass) for module_mass in f.readlines()]

naive_fuel_sum = 0
true_fuel_sum = 0
for module_mass in masses:
    fuel = module_mass // 3 - 2
    naive_fuel_sum += fuel
    true_fuel_sum += fuel + calculate_recursive_fuel(fuel)

# Answer One
print("The naive fuel sum is {}".format(naive_fuel_sum))

# Answer Two
print("The true fuel sum is {}".format(true_fuel_sum))

