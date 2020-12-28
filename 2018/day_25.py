"""Advent of Code Day 25 - Four Dimensional Adventure"""


class FixedPoint:
    """Initialise fixed point as ranked, self-parented node."""
    def __init__(self, num):
        self.num = num
        self.parent = self
        self.rank = 0


def find(point):
    """Return root of point (parent with parent as self)."""
    if point.parent != point:
        point.parent = find(point.parent)
    return point.parent


def union(point_1, point_2):
    """Combine the sets containing each point via union by rank."""
    # Find both roots and check they aren't already in the same set
    point_1_root = find(point_1)
    point_2_root = find(point_2)
    if point_1_root == point_2_root:
        return

    # Rank merge avoids unchecked O(n) growth of trees if done naively
    if point_1_root.rank < point_2_root.rank:
        point_1_root, point_2_root = point_2_root, point_1_root

    point_2_root.parent = point_1_root
    if point_1_root.rank == point_2_root.rank:
        point_1_root.rank += 1


def manhattan_distance(point_1, point_2):
    """Return Manhattan distance between two points."""
    return sum(abs(a - b) for a, b in zip(point_1, point_2))


def main():
    """Use disjoint-set structure to turn points into constellations."""
    with open('inputs/day_25.txt') as f:
        lines = [[int(x) for x in l.strip().split(',')] for l in f.readlines()]

    # Initialise each point and check against previous to see if union needed
    points = {}
    for i, line in enumerate(lines):
        coords = tuple(line)
        points[coords] = FixedPoint(i)

        for point in points:
            if manhattan_distance(coords, point) <= 3:
                union(points[coords], points[point])

    # Set comprehension of find() for each FixedPoint gives unique roots
    constellations = len({find(x) for x in points.values()})

    # Answer One
    print("Number of constellations:", constellations)


if __name__ == '__main__':
    main()
