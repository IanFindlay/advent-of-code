#!/usr/bin/env python3

"""Advent of Code 2020 Day 22 - Crab Combat."""


with open('inputs/2020_22.txt') as f:
    player_1, player_2 = [line for line in f.read().split('\n\n')]
    player_1 = [int(x) for x in player_1.split('\n')[1:]]
    player_2 = [int(x) for x in player_2.split('\n')[1:-1]]

while player_1 and player_2:
    one_card = player_1[0]
    two_card = player_2[0]
    if one_card > two_card:
        player_1.extend([one_card, two_card])
    else:
        player_2.extend([two_card, one_card])

    player_1 = player_1[1:]
    player_2 = player_2[1:]

winning_order = player_1 + player_2
winning_score = 0
for rev_index, card in enumerate(winning_order[::-1], 1):
    winning_score += rev_index * card

# Answer One
print("Winning player's score:", winning_score)
