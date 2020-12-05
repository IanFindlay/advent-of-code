#!/usr/bin/env python3

"""Advent of Code 2020 Day 05 - Binary Binding."""


def decode_binary_space_partition(code: str) -> tuple:
    """Decode binary partition character code and return (row, col) tuple.

    Args:
        code: A 9 character code - The first 7 characters are each either
              "F"ront or "B"ack and the last 3 are either "L"eft or "R"ight.

    Returns:
        tuple consisting of two integers representing row and column.

    """
    row_low = col_low = 0
    row_high = 127
    col_high = 7
    for char in code:
        if char == "F":
            row_high -= (row_high - row_low) // 2 + 1
        elif char == "B":
            row_low += (row_high - row_low) // 2 + 1
        elif char == "L":
            col_high -= (col_high - col_low) // 2 + 1
        elif char == "R":
            col_low += (col_high - col_low) // 2 + 1

    row = row_low if code[6] == "F" else row_high

    col = col_low if code[9] == "L" else col_high

    return (row, col)


with open ('input.txt', 'r') as scanned:
    seat_codes = [seat_code.strip() for seat_code in scanned.readlines()]

seats = set()
seat_ids = set()
for seat_code in seat_codes:
    row, col = decode_binary_space_partition(seat_code)
    seats.add((row, col))
    seat_id = row * 8 + col
    seat_ids.add(seat_id)

# Answer One
print("Highest seat ID scanned:", max(seat_ids))

my_seat_id = None
for row in range(1, 127):
    for col in range(0, 8):
        seat_id = row * 8 + col
        if (row, col) not in seats:
            if seat_id + 1 in seat_ids and seat_id - 1 in seat_ids:
                my_seat_id = seat_id
                break

    if my_seat_id:
        break

# Answer Two
print("ID of my seat:", my_seat_id)
