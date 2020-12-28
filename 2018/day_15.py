"""Advent of Code Day 15 - Beverage Bandits"""


def build_units(elf_power):
    """Build Unit objects for units in arena and place them in the arena."""
    with open('inputs/day_15.txt') as f:
        arena = [list(row.strip()) for row in f.readlines()]

    units = []
    for y, row in enumerate(arena):
        for x, __ in enumerate(row):
            if arena[y][x] == 'E':
                unit = Unit('E', (y, x), elf_power)
                units.append(unit)
                arena[y][x] = unit
            elif arena[y][x] == 'G':
                unit = Unit('G', (y, x), 3)
                units.append(unit)
                arena[y][x] = unit

    return (arena, units)


class Unit:
    """Object representing a fighter(unit)."""

    def __init__(self, race, coords, attack):
        """Initialise Unit object with race, coords and attack power."""
        self.race = race
        self.coords = coords
        self.health = 200
        self.attack = attack

    def __repr__(self):
        return self.race

    def update_coords(self, new_coords, arena):
        """Update a unit's coordinates and move them in the arena."""
        row, col = self.coords
        arena[row][col] = '.'
        new_row, new_col = new_coords
        arena[new_row][new_col] = self
        self.coords = new_coords

    def check_adjacent(self, arena, enemy_check=False):
        """Check adjacent spaces of unit and return open spaces or enemies."""
        open_spaces = set()
        enemies = []
        row, col = self.coords
        adjacent = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for space in adjacent:
            value = arena[space[0]][space[1]]
            if enemy_check:
                if isinstance(value, Unit) and value.race != self.race:
                    enemies.append(value)
            elif value == '.':
                open_spaces.add(space)

        return enemies if enemy_check else open_spaces

    def take_damage(self, damage):
        """Decrease health by damage amount."""
        self.health -= damage

    def kill_unit(self, arena):
        """Remove unit from the arena map as it has been killed."""
        row, col = self.coords
        arena[row][col] = '.'


def battle(arena, units, part_two=False):
    """Battle the units in the arena until one side is eliminated."""
    elves = len([unit for unit in units if unit.race == 'E'])
    goblins = len(units) - elves
    rounds = 0
    while elves and goblins:
        # Clear dead then Sort units by reading order
        units = [unit for unit in units if unit.health > 0]
        units.sort(key=lambda unit: (unit.coords[0], unit.coords[1]))
        for unit in units:
            if unit.health <= 0:
                continue

            # If final blow wasn't the last units attack rounds needs fixed
            if not elves or not goblins:
                rounds -= 1
                break

            # Check for enemies and attack if found
            attackable = unit.check_adjacent(arena, enemy_check=True)
            if attackable:
                unit_killed = make_attack(attackable, unit)

            # Move, recheck for enemies and attack if found
            else:
                open_spaces = set()
                for other in units:
                    if other.race != unit.race and other.health > 0:
                        open_spaces = open_spaces | other.check_adjacent(arena)

                if not open_spaces:
                    continue

                move = make_move(unit.coords, open_spaces, arena)

                if not move:
                    continue

                unit.update_coords(move, arena)

                attackable = unit.check_adjacent(arena, enemy_check=True)
                if attackable:
                    unit_killed = make_attack(attackable, unit)
                else:
                    unit_killed = False

            # If kill clear from arena, check both sides remain
            if unit_killed:
                unit_killed.kill_unit(arena)
                race = unit_killed.race

                if race == 'E':
                    elves -= 1
                    if part_two:
                        return False
                else:
                    goblins -= 1

        rounds += 1

        print_arena(rounds, arena)

    remaining_health = sum([unit.health for unit in units if unit.health > 0])
    return rounds * remaining_health


def make_attack(attackable, attacker):
    """Choose best target from attackable, attack then return if killed."""
    # Sort units by health then reading order
    attackable.sort(
        key=lambda unit: (unit.health, unit.coords[0], unit.coords[1])
    )
    to_attack = attackable[0]
    to_attack.take_damage(attacker.attack)

    return to_attack if to_attack.health <= 0 else False


def make_move(start, open_spaces, arena):
    """Dijkstra to find closest open space that is first in reading order"""
    visited = set()
    distances = {start: (0, None)}
    shortest = None
    nearest = None
    node = (start, None)
    while True:
        node_coords, node_first_step = node
        row, col = node_coords
        adjacent = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for square in adjacent:
            if square in visited:
                continue

            if arena[square[0]][square[1]] != '.':
                continue

            first_step = node_first_step if node_first_step else square
            current_distance = distances.get(square, (1000, None))[0]
            new_distance = distances[node_coords][0] + 1
            if new_distance < current_distance:
                distances[square] = (new_distance, first_step)

            elif new_distance == current_distance:
                reading_order = [distances[square][1], first_step]
                reading_order.sort(key=lambda coords: (coords[0], coords[1]))
                distances[square] = (new_distance, reading_order[0])

        visited.add(node[0])

        # Create nodes from distances filter out visited
        nodes = [(x, distances[x][1]) for x in distances if x not in visited]

        if not nodes:
            break
        # Choose node with smallest distance
        nodes.sort(key=lambda node: distances[node[0]][0], reverse=True)
        node = nodes.pop()

        new_coords, first_step = node

        if nearest and distances[new_coords][0] > nearest:
            break

        if new_coords in open_spaces:
            if not shortest:
                shortest = (new_coords, first_step)
            else:
                # Keep first_step that's earliest in reading order
                reading_order = [shortest, (new_coords, first_step)]
                reading_order.sort(
                    key=lambda coords: (coords[1][0], coords[1][1])
                )
                shortest = reading_order[0]
            nearest = distances[new_coords][0]

    if not shortest:
        return False

    return shortest[1]


def print_arena(rounds, arena):
    """Print the arena with race, health info for units at the side."""
    print("Round {}:".format(rounds))
    for row in arena:
        arena_row = ''.join([str(x) for x in row])
        units = ''
        for col in row:
            if isinstance(col, Unit):
                units += "({}: {}), ".format(col.race, col.health)
        print(arena_row, units.strip(', '))


def main():
    """Find outcome of battle then attack boosted one where no elves die."""
    arena, units = build_units(3)

    # Answer One
    outcome = battle(arena, units)
    print("Initial outcome:", outcome)

    attack_power = 4
    while True:
        arena, units = build_units(attack_power)
        outcome = battle(arena, units, part_two=True)
        if outcome:
            break
        attack_power += 1

    # Answer Two
    print("Outcome of first no death elf victory:", outcome)


if __name__ == '__main__':
    main()
