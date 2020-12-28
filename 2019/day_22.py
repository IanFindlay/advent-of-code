"""Advent of Code 2019 Day 22 - Slam Shuffle."""


def deal_new_stack(cards):
    """Return reversed cards."""
    cards.reverse()
    return cards


def cut(cards, cut_size):
    """Perform a cut on the cards."""
    return cards[cut_size:] + cards[:cut_size]


def deal_with_increment(cards, increment):
    """Deal cards into new order based upon an increment."""
    num_cards = len(cards)
    pos = 0
    new_cards = cards.copy()
    for card in cards:
        new_cards[pos] = card
        pos = (pos + increment) % num_cards
    return new_cards



with open('inputs/day_22.txt') as f:
    shuffle = [line.strip() for line in f.readlines()]

deck = list(range(10007))
for instruction in shuffle:
    if 'new' in instruction:
        deck = deal_new_stack(deck)
    elif 'cut' in instruction:
        deck = cut(deck, int(instruction.split()[-1]))
    elif 'increment' in instruction:
        deck = deal_with_increment(deck, int(instruction.split()[-1]))

# Answer One
print("Index of card 2019 post-shuffling:", deck.index(2019))


"""
Reduce each shuffle type to its effect on the offset (which card appears first)
and the increment (the difference between adjacent numbers) as all deck states
can be encoded through those two paramneters.
Run through the shuffle instructions once, tracking the changes to the offset
and increment, and then iterate these tracked changes the required amount.
The iteration of increment is simply exponential whereas the iteration of the
offset is largely a geometric series.
"""

num_cards = 119315717514047
iterations = 101741582076661
increment = 1
offset = 0
for curr_shuffle in shuffle:
    if 'new' in curr_shuffle:
        increment *= -1
        offset += increment
    elif 'cut' in curr_shuffle:
        offset += int(curr_shuffle.split()[-1]) * increment
    else:
        increment *= pow(int(curr_shuffle.split()[-1]), -1, num_cards)

total_increment = pow(increment, iterations, num_cards)
total_offset = offset * (1 - pow(increment, iterations, num_cards))
total_offset *= pow(1 - increment, -1, num_cards)

value_2020 = (2020 * total_increment + total_offset) % num_cards

# Answer Two
print("Number on card at position 2020:", value_2020)
