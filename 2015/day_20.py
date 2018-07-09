"""Advent of Code Day 20 - Infinite Elves and Infinite Houses"""


def find_factors(number):
    """Returns the prime factorisation of a number."""
    factors = set()
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            factors.add(i)
            factors.add(number // i)
    
    return factors


present_goal = 29000000
door = 1
while True:
    factors = find_factors(door)
    presents = sum([n * 10 for n in factors])
    if presents >= present_goal:
        break
    door += 1

# Answer One
print("Lowest Numbered House =", door)

factor_dict = {}
door = 1
while True:
    factors = find_factors(door)
    for factor in factors:
        factor_dict.setdefault(factor, 0)
        factor_dict[factor] += 1
    presents = sum([n * 11 for n in factors if factor_dict[n] <= 50])
    if presents >= present_goal:
        break
    door += 1

# Answer Two
print("Lowest With 50 Limit =", door)
