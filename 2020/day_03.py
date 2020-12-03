#!/usr/bin/env python3

"""Advent of Code 2020 Day 03 - Toboggan Trajectory."""


def count_trees_on_slope(area: list, right_step: int, down_step: int) -> int:
    """Return number of trees encounterd in area on slope (right/down step).

    Args:
        area: Rows of characters representing coordinates of a map.
        right_step: Amount to move to the right at each section of the slope.
        down_step: Amount to move down at each section of the slope.

    Returns:
        The number of trees ("#" characters) encountered before reaching past
        the last row of the area.

    """
    # Determine boundaries of the area
    index_of_last_row = len(area) - 1
    index_of_last_col = len(area[0]) - 1

    y = x = 0
    trees = 0
    while y <= index_of_last_row:
        if rows[y][x] == "#":
            trees += 1

        x = (x + right_step) % index_of_last_col
        y += down_step

    return trees


with open ('input.txt', 'r') as password_database:
    rows = [line for line in password_database.readlines()]

trees = count_trees_on_slope(rows, 3, 1)

# Answer One
print("Number of trees encountered on right 3 down 1 slope:", trees)

product_of_trees = trees
product_of_trees *= count_trees_on_slope(rows, 1, 1)
product_of_trees *= count_trees_on_slope(rows, 5, 1)
product_of_trees *= count_trees_on_slope(rows, 7, 1)
product_of_trees *= count_trees_on_slope(rows, 1, 2)


# Answer Two
print("Product of trees encountered on 5 different slopes:", product_of_trees)
