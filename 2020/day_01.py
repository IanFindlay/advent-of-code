#!/usr/bin/env python3

"""Advent of Code 2020 Day 01 - Report Repair."""


with open ('inputs/day_01.txt', 'r') as expense_report:
    entries = set([int(line) for line in expense_report.readlines()])

for entry in entries:
    if 2020 - entry in entries:
        answer_one = entry * (2020 - entry)
        break

# Answer One
print("Product of the two entries that sum to 2020:", answer_one)

answer_two = False
for entry in entries:
    remaining_amount = 2020 - entry
    for entry_two in entries:
        if remaining_amount - entry_two in entries and entry_two != entry:
            answer_two = entry * entry_two * (remaining_amount - entry_two)
            break

    if answer_two:
        break

# Answer Two
print("Product of the three entries that sum to 2020:", answer_two)


# As shown above, part two is a simple extension of part one and this is how I
# initially solved it. The recursive solution below is what I immediately
# thought of when reading part two. It is a similar idea to finding out all
# the ways an amount can be made from various coins i.e. for each entry you
# either use it or you don't.

def sums_to_target_product(entries_list: list, target: int,
                           used_and_product: tuple, num_entries: int) -> int:
    """Return product of entries that sum to target using given num_entries.

    For each entry, it can either be a part of the combination or not so
    recursive calls representing these possibilities explores all
    combinations until the solution (function assumes there is only one)
    is found.

    Args:
        entries_list: Entries available.
        target: Value to be reached.
        used_and_product: (number of entries used, product of used entries).
        num_entries: Number of entries required to be used for valid answer.

    Returns:
        Product of entries used in valid solution i.e. used_and_product[1]
        or None if no solution is found.

    """
    if target == 0 and used_and_product[0] == num_entries:
        return used_and_product[1]

    if not entries_list or target <= 0 or used_and_product[0] == num_entries:
        return None


    # Don't use first entry in entries_list path
    not_used = sums_to_target_product(entries_list[1:], target,
                               used_and_product, num_entries)
    if not_used:
        return not_used

    # Use first entry in entries_list path
    used = sums_to_target_product(
            entries_list[1:], target - entries_list[0],
            (used_and_product[0] + 1, used_and_product[1] * entries_list[0]),
            num_entries
    )
    if used:
        return used


list_of_entries = list(entries)

# Answer One
print("Product of the two entries that sum to 2020:",
      sums_to_target_product(list_of_entries, 2020, (0, 1), 2))

# Answer Two
print("Product of the three entries that sum to 2020:",
      sums_to_target_product(list_of_entries, 2020, (0, 1), 3))
