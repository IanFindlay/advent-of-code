#!/usr/bin/env python3

"""Advent of Code 2020 Day 22 - Crab Combat."""


def play_game(player_1, player_2, part_two=False):
    """."""
    prev_rounds = set()
    while player_1 and player_2:
        one_card = player_1[0]
        two_card = player_2[0]
        if (tuple(player_1), tuple(player_2)) in prev_rounds:
            player_1.extend([one_card, two_card])
            return (1, player_1)
        prev_rounds.add((tuple(player_1), tuple(player_2)))

        if not part_two:
            if one_card > two_card:
                player_1.extend([one_card, two_card])
            else:
                player_2.extend([two_card, one_card])
        else:
            if len(player_1) - 1 >= one_card and len(player_2) - 1 >= two_card:
                one_recursive = player_1[1: one_card + 1].copy()
                two_recursive = player_2[1: two_card + 1].copy()
                winner = play_game(one_recursive, two_recursive, True)
                if winner[0] == 1:
                    player_1.extend([one_card, two_card])
                else:
                    player_2.extend([two_card, one_card])

            else:
                if one_card > two_card:
                    player_1.extend([one_card, two_card])
                else:
                    player_2.extend([two_card, one_card])

        player_1 = player_1[1:]
        player_2 = player_2[1:]

    if player_1:
        return (1, player_1)
    else:
        return (2, player_2)


with open('inputs/2020_22.txt') as f:
    player_1, player_2 = [line for line in f.read().split('\n\n')]
    player_1 = [int(x) for x in player_1.split('\n')[1:]]
    player_2 = [int(x) for x in player_2.split('\n')[1:-1]]

winner, winning_order = play_game(player_1.copy(), player_2.copy())
winning_score = 0
for rev_index, card in enumerate(winning_order[::-1], 1):
    winning_score += rev_index * card

# Answer One
print("Combat winner's score:", winning_score)

winner, winning_order = play_game(player_1, player_2, part_two=True)
winning_score = 0
for rev_index, card in enumerate(winning_order[::-1], 1):
    winning_score += rev_index * card

# Answer Two
print("Recursive Combat winner's score:", winning_score)
