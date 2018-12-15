"""Advent of Code Day 14 - Chocolate Charts"""


part_one, part_two = False, False
to_make = '323081'
make_list = [int(x) for x in to_make]
found = 0
recipies = [3, 7]
num_recipies = 2
elf_1, elf_2 = 0, 1
while not part_one or not part_two:
    new = recipies[elf_1] + recipies[elf_2]
    if new < 10:
        new = (new,)
    else:
        new = divmod(new, 10)

    for recipie in new:
        recipies.append(recipie)
        num_recipies += 1
        if recipie == make_list[found]:
            found += 1
            if found == len(make_list):
                # Answer Two
                print("Recipies before:", num_recipies - len(to_make))
                part_two = True
                break
        else:
            found = 1 if recipie == make_list[0] else 0

    elf_1 = (elf_1 + recipies[elf_1] + 1) % num_recipies
    elf_2 = (elf_2 + recipies[elf_2] + 1) % num_recipies

    # Answer One
    if not part_one:
        if num_recipies == int(to_make) + 10:
            last_10 = ''.join([str(x) for x in recipies[-10:]])
            print("10 Recipies after:", last_10)
            part_one = True
