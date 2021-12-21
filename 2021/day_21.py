#!/usr/bin/env python3

"""Advent of Code 2021 Day 21 - Dirac Dice"""


class Game:

    def __init__(self, players):
        self.players = players
        self.num_players = len(players)
        self.player_index = 0
        self.next_die = 1
        self.num_rolls = 0
        self.winner = False

    def next_turn(self):
        player = self.players[self.player_index]
        self.next_die = player.take_turn(self.next_die)
        self.num_rolls += 3
        if player.score >= 1000:
            self.winner = player
            return True

        self.player_index = (self.player_index + 1) % self.num_players


class Player:

    def __init__(self, id_num, position):
        self.id = id_num
        self.position = position
        self.score = 0

    def take_turn(self, die_value):
        roll_sum = 0
        for _ in range(3):
            roll_sum += die_value
            die_value = (die_value + 1) % 100
            if not die_value:
                die_value = 100

        self.position = (self.position + roll_sum) % 10
        if not self.position:
            self.position = 10

        self.score += self.position

        return die_value


with open('inputs/day_21.txt', 'r') as aoc_input:
    one_start, two_start = [
            int(x.strip().split()[-1]) for x in aoc_input.readlines()
    ]

game = Game([Player(1, one_start), Player(2, two_start)])

winner = None
while True:
    turn_result = game.next_turn()
    if turn_result:
        break

rolls_taken = game.num_rolls
loser_score = 0
for player in game.players:
    if player != game.winner:
        loser_score = player.score

# Answer One
print("Product of losing score and number of rolls:",
        rolls_taken * loser_score)
