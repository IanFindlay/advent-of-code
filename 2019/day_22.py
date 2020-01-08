"""Advent of Code 2019 Day 22 - Slam Shuffle."""


deck = list(range(10007))

def deal_new_stack(cards):
    """."""
    cards.reverse()
    return cards


def cut_n(cards, n):
    """."""
    if n > 0:
        cut = cards[0 : n]
        return cards[n:] + cut
    else:
        cut = cards[n:]
        return cut + cards[:n]


def deal_with_inc(cards, inc):
    """."""
    num_cards = len(cards)
    pos = 0
    new_cards = cards.copy()
    for card in cards:
        new_cards[pos] = card
        pos = (pos + inc) % num_cards
    return new_cards


with open('input.txt') as f:
    shuffle = [line.strip() for line in f.readlines()]

for instruction in shuffle:
    if 'new' in instruction:
        deck = deal_new_stack(deck)
    elif 'cut' in instruction:
        deck = cut_n(deck, int(instruction.split()[-1]))
    elif 'increment' in instruction:
        deck = deal_with_inc(deck, int(instruction.split()[-1]))

# Answer One
print("Index of card 2019 post-shuffling:", deck.index(2019))
