#!/usr/bin/env python3

"""Advent of Code 2020 Day 05 - Binary Binding."""


def decode_row(code: str) -> int:
    """."""
    range_low = 0
    range_high = 127
    for char in code:
        if char == "F":
            range_high -= (range_high - range_low) // 2 + 1
        elif char == "B":
            range_low += (range_high - range_low) // 2 + 1

    return range_low if char == "F" else range_high


def decode_col(code: str) -> int:
    """."""
    range_low = 0
    range_high = 7
    for char in code:
        if char == "L":
            range_high -= (range_high - range_low) // 2 + 1
        elif char == "R":
            range_low += (range_high - range_low) // 2 + 1

    return range_low if char == "L" else range_high


with open ('input.txt', 'r') as scanned:
    seat_codes = [seat_code.strip() for seat_code in scanned.readlines()]

highest_id = 0
for seat_code in seat_codes:
    row_code = seat_code[:7]
    col_code = seat_code[7:]
    seat_row = decode_row(row_code)
    seat_col = decode_col(col_code)
    seat_id = seat_row * 8 + seat_col

    if seat_id > highest_id:
        highest_id = seat_id

# Answer One
print("Highest seat ID scanned:", highest_id)

all_seats = set()
for row in range(1, 127):
    for col in range(0, 8):
        all_seats.add((row, col))

possible_seat = set(all_seats)
seat_ids = set()
for seat_code in seat_codes:
    row_code = seat_code[:7]
    col_code = seat_code[7:]
    seat_row = decode_row(row_code)
    seat_col = decode_col(col_code)
    seat_id = seat_row * 8 + seat_col
    seat_ids.add(seat_id)

    possible_seat.remove((seat_row, seat_col))

for seat in possible_seat:
    seat_id = seat[0] * 8 + seat[1]
    if seat_id - 1 in seat_ids and seat_id + 1 in seat_ids:
        my_seat_id = seat_id
        break

# Answer Two
print("ID of my seat:", my_seat_id)
