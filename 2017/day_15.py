"""Advent of Code Day 15 - Dueling Generators"""


def judgement(seed_a, seed_b):
    """Return amount of times last 16 binary digits of generators match."""
    sample = 0
    count = 0
    while sample <= 40000000:
        new_a = seed_a * 16807 % 2147483647
        new_b = seed_b * 48271 % 2147483647

        bin_a = bin(new_a)
        bin_b = bin(new_b)

        last16_a = bin_a[-16:]
        last16_b = bin_b[-16:]

        if last16_a == last16_b:
            count += 1

        seed_a = new_a
        seed_b = new_b
        sample += 1

    return count


def aligned(seed_a, seed_b):
    """Return amount of times last 16 binary digits of aligned generators match."""
    sample = 0
    count = 0

    while sample < 5000000:
        gen_a = False
        gen_b = False

        while gen_a is False and gen_b is False:

            while gen_a is False:
                new_a = seed_a * 16807 % 2147483647

                if new_a % 4 == 0:
                    gen_a = True

                else:
                    seed_a = new_a


            while gen_b is False:
                new_b = seed_b * 48271 % 2147483647

                if new_b % 8 == 0:
                    gen_b = True

                else:
                    seed_b = new_b

        bin_a = bin(new_a)
        bin_b = bin(new_b)

        last16_a = bin_a[-16:]
        last16_b = bin_b[-16:]

        if last16_a == last16_b:
            count += 1

        seed_a = new_a
        seed_b = new_b
        sample += 1

    return count


# Answer One
print("Final count:", judgement(116, 299))

# Answer Two
print("Final count when the generators are aligned:", aligned(116, 299))
