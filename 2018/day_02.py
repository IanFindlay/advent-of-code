"""Advent of Code Day 2 - Inventory Management System"""


def repetition_checksum(ids):
    """Return checksum - No. of ids with doubled letters * No. with tripled."""
    doubles, triples = 0, 0
    for code in ids:
        no_doubles, no_triples = True, True
        for letter in set(code):
            count = code.count(letter)
            if count == 2 and no_doubles:
                doubles += 1
                no_doubles = False
            elif count == 3 and no_triples:
                triples += 1
                no_triples = False

            if not no_doubles and not no_triples:
                break

    return doubles * triples


def one_off(ids):
    """Find id pair that differs by one letter and return common letters."""
    for index, code in enumerate(ids[:-1]):
        for comparison in ids[index+1:]:
            diff = []
            to_compare = zip(code, comparison)
            for pos, pair in enumerate(to_compare):
                if pair[0] != pair[1]:
                    diff.append(pos)
                    if len(diff) > 1:
                        break

            if len(diff) == 1:
                return code[:diff[0]] + code[diff[0]+1:]


if __name__ == '__main__':

    with open('input.txt') as f:
        ids = f.readlines()

    # Answer One
    print("Checksum:", repetition_checksum(ids))

    # Answer Two
    print("Letters in common:", one_off(ids))
