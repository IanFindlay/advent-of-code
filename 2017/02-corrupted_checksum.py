"""Answers to Advent of Code Day 2."""

import pyperclip


# Challenge 1
def difference_checksum(string):
    """Take number rows and return the sum of each rows high/low difference."""
    total = 0
    # Split string so each row is its own embedded list
    row_list = []
    rows_split = string.split('\n')
    for i in rows_split:
        row_string = str(i)
        row = row_string.split()
        row_list.append(row)

    # Sort each row into ascending order, calculate difference and add to total
    for row in row_list:
        sorted_list = sorted(row, key=int)
        total += int(sorted_list[-1]) - int(sorted_list[0])

    return total


# Challenge 2
def divisible_cheksum(string):
    """Take rows of numbers and return the sum of their divisible pairs."""
    total = 0
    # Split string so each row is its own embedded list
    row_list = []
    rows_split = string.split('\n')
    for i in rows_split:
        row_string = str(i)
        row = row_string.split()
        row_list.append(row)

    # For each number in row, see if it divides with no remainder
    for row in row_list:
        for number in row:
            count = 0
            while count < len(row) - 1:
                # Check division order and that it divides with no remainder
                if (int(number) > int(row[count + 1])
                        and int(number) % int(row[count + 1]) == 0):
                    total += int(number) // int(row[count + 1])
                count += 1

    return total


# Challenge 1 Answer
try:
    print(difference_checksum(pyperclip.paste()))
except ValueError:
    print('Invalid input, try copying the table data again')

# Challenge 2 Answer
try:
    print(divisible_cheksum(pyperclip.paste()))
except ValueError:
    print('Invalid input, try copying the table data again')
