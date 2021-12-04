#!/usr/bin/env python3

"""Advent of Code 2021 Day 04 - Giant Squid"""


import re


def mark_cards(cards, number):
    cards_copy = cards.copy()
    for card_index, card in enumerate(cards):
        for row_index, row in enumerate(card):
            for col_index, card_num in enumerate(row):
                if number == card_num:
                    cards_copy[card_index][row_index][col_index] = None

    return cards_copy


def check_for_winner(cards):
    for card in cards:
        for row in card:
            if set(row) == set([None]):
                return card

    for card in cards:
        for col_index in range(len(cards[0])):
            column = []
            for row in card:
                column.append(row[col_index])
            if set(column) == set([None]):
                return card


    return False



with open('inputs/day_04.txt', 'r') as aoc_input:
    sections = aoc_input.read().strip().split('\n\n')

balls = []
cards = []
for part in sections:
    if not balls:
        balls = [int(x) for x in part.split(',')]
        continue

    cards.append([])
    rows = part.split('\n')
    for row in rows:
        cards[-1].append([int(x) for x in re.findall(r'\d\d?', row)])

winner = False
while not winner:
    for ball in balls:
        cards = mark_cards(cards, ball)
        winner = check_for_winner(cards)
        if winner:
            break

print("Winning_card:", winner)
print("Ball", ball)

remaining_sum = 0
for row in winner:
    remaining_sum += sum([x for x in row if x != None])

# Answer One
print("Final score of winning board:", remaining_sum * ball)
