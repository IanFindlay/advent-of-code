"""Advent of Code Day 18 - Like a Rogue"""

with open('input.txt') as f:
    start = f.read().strip()

def map_traps(prev_pat, row_limit):
    """Work out the number of safe tiles in a trapped room."""
    safe = prev_pat.count('.')
    row = 1
    while row < row_limit:
        next_row = ''
        trap_patterns = ('^^.', '.^^', '^..', '..^')

        pattern = '.{}{}'.format(prev_pat[0], prev_pat[1])
        if pattern in trap_patterns:
            next_row += '^'
        else:
            next_row += '.'

        i = 1
        while i < len(prev_pat) - 1:
            pattern = '{}{}{}'.format(prev_pat[i-1], prev_pat[i], prev_pat[i+1])
            if pattern in trap_patterns:
                next_row += '^'
            else:
                next_row += '.'

            i += 1

        pattern = '{}{}.'.format(prev_pat[i-1], prev_pat[1+1])
        if pattern in trap_patterns:
            next_row += '^'
        else:
            next_row += '.'

        safe += next_row.count('.')
        prev_pat = next_row
        row += 1

    return safe


# Answer One
print("Safe tiles within 40 rows:", map_traps(start, 40))

# Answer Two
print("Safe tiles within 400000 rows:", map_traps(start, 400000))
