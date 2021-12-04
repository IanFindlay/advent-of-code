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
    winners = set()
    for card_num, card in enumerate(cards):
        for row in card:
            if len(set(row)) == 1:
                winners.add(card_num)

        for col_index in range(len(card[0])):
            column = []
            for row in card:
                column.append(row[col_index])
            if len(set(column)) == 1:
                winners.add(card_num)

    if winners:
        return winners

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

num_cards = len(cards)

ball = 0
winning_cards = []
for ball in balls:
    cards = mark_cards(cards, ball)

    winning_indicies = check_for_winner(cards)
    if winning_indicies is not False:
        for index in winning_indicies:
            winning_cards.append((cards[index].copy(), ball))

        cards_copy = []
        for card_index, card in enumerate(cards):
            if card_index not in winning_indicies:
                cards_copy.append(card)


        cards = cards_copy

        if len(cards) == 0:
            break

winning_card, winning_ball = winning_cards[0]
winner_sum = 0
for row in winning_card:
    winner_sum += sum([x for x in row if x != None])

# Answer One
print("Final score of winning card:", winner_sum * winning_ball)

losing_card, losing_ball = winning_cards[-1]
losing_sum = 0
for row in losing_card:
    losing_sum += sum([x for x in row if x != None])

# Answer Two
print("Final score of losing card:", losing_sum * losing_ball)
