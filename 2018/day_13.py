"""Advent of Code Day 13 - Cart Madness."""


with open('input.txt') as f:
     track = [[x for x in list(line.rstrip())] for line in f.readlines()]

# Find carts, set next_turn to 0 (left) and replace track beneath it
carts = []
for y, line in enumerate(track):
    for x, piece in enumerate(line):
        if piece in ('^', 'v', '>', '<'):
            carts.append(((y, x), piece, 0))

            if piece in ('^', 'v'):
                track[y][x] = '|'
            else:
                track[y][x] = '-'

# Dictionaries for direction conversions
cart_moves = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}
left_turn = {'^': '<', 'v': '>', '>': '^', '<': 'v'}
right_turn = {'^': '>', 'v': '<', '>': 'v', '<': '^'}
back = {'^': '<', 'v': '>', '<': '^', '>': 'v'}
forward = {'^': '>', 'v': '<', '<': 'v', '>': '^'}

# Until one cart remains, sort by row,col then move in order removing crashed
part_one = True
while len(carts) > 1:
    carts = sorted(carts, key=lambda element: (element[0][0], element[0][1]))
    new_carts = []
    while carts:
        cart = carts.pop(0)
        coords, direction, turn = cart
        y, x = coords
        change_y, change_x = cart_moves[direction]
        y, x = y + change_y, x + change_x

        piece = track[y][x]
        if piece == '+':
            if turn % 3 == 0:
                direction = left_turn[direction]
            elif turn % 3 == 2:
                direction = right_turn[direction]
            turn += 1

        elif piece == '\\':
            direction = back[direction]
        elif piece =='/':
            direction = forward[direction]

        cart_check = [x[0] for x in carts] + [x[0] for x in new_carts]
        if (y, x) in cart_check:
            if part_one:
                # Answer One
                print("First crash: {},{}".format(x, y))
                part_one = False

            # Find crashed cart and remove it, skip adding this one to new
            if (y, x) in cart_check:
                carts = [cart for cart in carts if cart[0] != (y, x)]
                new_carts = [cart for cart in new_carts if cart[0] != (y, x)]
            continue

        new_carts.append(((y, x), direction, turn))

    carts = new_carts

# Answer Two
final_cart = carts[0]
print("Final cart: {},{}".format(final_cart[0][1], final_cart[0][0]))
