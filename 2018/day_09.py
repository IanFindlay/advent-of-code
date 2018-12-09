"""Advent of Code Day 9 - Marble Mania"""

import collections


def marble_game(num_players, num_marbles):
    """Play a game of marbles and return the winning score."""
    circle = collections.deque([0])
    scores = collections.defaultdict(int)
    player = 1

    for marble in range(1, num_marbles + 1):
        if marble % 23 == 0:
            player = player % num_players
            circle.rotate(7)
            scores[player] += circle.pop() + marble
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

        player += 1

    return max(scores.values())


# Answer One
print("Small game:", marble_game(465, 71940))

# Answer Two
print("Large game:", marble_game(465, 7194000))