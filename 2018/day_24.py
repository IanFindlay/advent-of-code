"""Advent of Code Day 24 - Immune System Simulator 20XX"""

import copy
import re


def build_groups(armies):
    """Parse armies into seperate groups with side flag and return groups."""
    groups = []
    unit_regex = re.compile(r'(\d+).*?(\d+).*?(\d+)\s(\w+).*?(\d+)')
    modifier_regex = re.compile(r'\((.*)\)')
    switch = False
    for line in armies[1:]:
        if line == 'Infection:':
            switch = True
            continue

        parsed = unit_regex.search(line)
        units = int(parsed.group(1))
        hit_points = int(parsed.group(2))
        damage = int(parsed.group(3))
        damage_type = parsed.group(4)
        initiative = int(parsed.group(5))

        # Parse modifiers into weaknesses and immunities if they have them
        modifiers = modifier_regex.search(line)
        if modifiers:
            weaknesses, immunities = parse_modifiers(modifiers)
        else:
            weaknesses, immunities = set(), set()

        side = 'inf' if switch else 'imm'

        groups.append(
            [side, units, hit_points, weaknesses, immunities,
             damage, damage_type, initiative]
        )

    return groups


def parse_modifiers(modifiers):
    """Parse modifiers(regex match object) into type sets then return them."""
    weaknesses, immunities = set(), set()
    sections = modifiers.group(1).split(';')
    for section in sections:
        split = [w.strip(',') for w in section.strip().split(' ')]
        for word in split[2:]:
            if split[0] == 'weak':
                weaknesses.add(word)
            else:
                immunities.add(word)

    return (weaknesses, immunities)


def fight(groups):
    """While two sides remain orchestrate round by round combat.

        Args:
            groups: List of lists containing group data formatted
                    [side, units, hit_points, weaknesses, immunities,
                     damage, damage_type, initiative]

        Return:
            groups: Remaining groups once only one side remains
            False: If there is a stalemate (no deaths in a round)
    """
    while True:
        # Sort groups by effective power then initiative (descending)
        groups.sort(key=lambda x: (x[1] * x[5], x[7]), reverse=True)

        # Select targets then sort by initiative
        attacks = target_selection(groups)
        attacks.sort(key=lambda info: info[0], reverse=True)

        # Make attacks and check for stalemate
        deaths = make_attacks(attacks, groups)
        if not deaths:
            return False

        # Remove destroyed units and return groups if only one side remains
        groups = [x for x in groups if x[1] > 0]
        if len({x[0] for x in groups}) == 1:
            return groups


def target_selection(groups):
    """Return tuple representing an attack, if one available, for each group.

        Args:
            groups: List of lists containing group data formatted
                    [side, units, hit_points, weaknesses, immunities,
                     damage, damage_type, initiative]

        Return:
            attacks: List of (initiative, attacker index, defender index)
    """
    attacks = []
    selected = set()
    for i, attacker in enumerate(groups):
        to_attack = (-1, None)
        for j, defender in enumerate(groups):

            if j in selected or j == i or attacker[0] == defender[0]:
                continue

            damage = calculate_damage(attacker, defender)
            if damage > to_attack[0]:
                to_attack = (damage, j)

            # Tie goes to current as groups are in power, initiative order

        if to_attack[0] <= 0:
            continue

        selected.add(to_attack[1])
        attacks.append((attacker[7], i, to_attack[1]))

    return attacks


def calculate_damage(attacker, defender):
    """Calculate and return effective power of attacker against defender.

        args:
            attacker: [side, units, hit_points, weaknesses, immunities,
                       damage, damage_type, initiative]

            defender: [side, units, hit_points, weaknesses, immunities,
                       damage, damage_type, initiative]

        Return:
            group_damage: effective power modified by weaknesses/immunities
    """
    group_damage = attacker[1] * attacker[5]
    damage_type = attacker[6]
    if damage_type in defender[3]:
        group_damage *= 2
    elif damage_type in defender[4]:
        group_damage = 0
    return group_damage


def make_attacks(attacks, groups):
    """Make attacks between groups (pre-sorted by initiative).

        Args:
            attacks: List of tuples (attacks) each attack formatted
                     (initiative, attacker_index, defender_index)

            groups: List of lists containing group data formatted
                    [side, units, hit_points, weaknesses, immunities,
                     damage, damage_type, initiative]

        Return:
            deaths: Boolean indicating if unit(s) died this round
    """
    deaths = False
    for attack in attacks:

        attacker = groups[attack[1]]
        # Groups with no units can't attack
        if attacker[1] <= 0:
            continue

        defender = groups[attack[2]]
        damage = calculate_damage(attacker, defender)
        defender_health = defender[2]
        killed = damage // defender_health
        defender[1] -= killed

        if killed > 0:
            deaths = True

    return deaths


def main():
    """Build armies, fight unboosted then boost immune side until victory."""
    with open('inputs/day_24.txt') as file:
        armies = [line.strip() for line in file.readlines() if line != '\n']

    groups = build_groups(armies)
    post_fight = fight(copy.deepcopy(groups))

    # Answer One
    units_left = sum([group[1] for group in post_fight])
    print("Units of winning army left:", units_left)

    while True:
        boosted = []
        for group in groups:
            if group[0] == 'imm':
                group[5] += 1
            boosted.append(group)
        groups = boosted
        post_fight = fight(copy.deepcopy(groups))
        if post_fight and post_fight[0][0] == 'imm':
            break

    # Answer Two
    units_left = sum([group[1] for group in post_fight])
    print("Immune units left after smallest winning boost:", units_left)


if __name__ == '__main__':
    main()
