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


game = Game([Player(1, 5), Player(2, 10)])

while True:
    turn_result = game.next_turn()
    if turn_result:
        break

rolls = game.num_rolls
loser_score = 0
for player in game.players:
    if player != game.winner:
        loser_score = player.score

# Answer One
print(f'Product of losing score and number of rolls: {rolls * loser_score}')

three_roll_sums = []
for one in (1, 2, 3):
    for two in (1, 2, 3):
        for three in (1, 2, 3):
            three_roll_sums.append(one + two + three)

# 1 pos, 1 score, 2 pos, 2 score, turn
game_initial = (5, 0, 10, 0, 1)
player_one_wins = 0
player_two_wins = 0
games = {game_initial: 1}
while True:
    new_games = {}
    for game, universes in games.items():

        player_num = game[4]

        if player_num == 1:
            pos, score  = game[0], game[1]
        else:
            pos, score  = game[2], game[3]

        for roll_sum in three_roll_sums:
            new_position = (pos + roll_sum) % 10
            if not new_position:
                new_position = 10

            new_score = score + new_position

            if new_score >= 21:
                if player_num == 1:
                    player_one_wins += universes
                else:
                    player_two_wins += universes

            else:
                if player_num == 1:
                    new_value = (new_position, new_score, game[2], game[3], 2)
                else:
                    new_value = (game[0], game[1], new_position, new_score, 1)

                new_games[new_value] = new_games.get(new_value, 0) + universes

    games = new_games

    if not games:
        break

# Answer Two
print(f'Most universes won: {max(player_one_wins, player_two_wins)}')
