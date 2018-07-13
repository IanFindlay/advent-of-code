"""Advent of Code Day 22 - Wizard Simulator 20XX"""

import random


def add_effects(effect, duration):
    """Adds effects to sublists of effects list simulating spell duration."""
    for num in range(duration):
        effects[num].append(effect)


def wizard_turn(hp, boss_hp, mana, mana_spent, spell):
    """Carry out spell effects and then cast new spell.

    Both survive - return [hp, boss_hp, mana, mana_spent]
    Boss dies - return True
    Wizard runs out of mana - blank return
     """
    # Comment out below for part one
    hp -= 1
    if hp < 1:
        return

    for effect in effects[0]:
        if effect == 'p':
            boss_hp -= 3
        elif effect == 'r':
            mana += 101

    del effects[0]
    effects.append([])

    if boss_hp < 1:
        return True

    if spell == 'mm':
        mana -= 53
        mana_spent += 53
        boss_hp -= 4
    elif spell == 'd':
        mana -= 73
        mana_spent += 73
        boss_hp -= 2
        hp += 2
    elif spell == 's':
        mana -= 113
        mana_spent += 113
        add_effects('s', 6)
    elif spell == 'p':
        mana -= 173
        mana_spent += 173
        add_effects('p', 6)
    elif spell == 'r':
        mana -= 229
        mana_spent += 229
        add_effects('r', 5)


    if mana < 1:
        return
    if boss_hp < 1:
        return mana_spent

    return [hp, boss_hp, mana, mana_spent]


def boss_turn(hp, boss_hp, mana):
    """Carry out spell effects and then the bosses attack.

    Both survive - return [hp, boss_hp and mana]
    Boss dies - return True
    Wizard death  - blank return
     """
    boss_damage = 10

    for effect in effects[0]:
        if effect == 'p':
            boss_hp -= 3
        elif effect == 'r':
            mana += 101
        elif effect == 's':
            boss_damage -= 7

    if boss_hp < 1:
        return True

    del effects[0]
    effects.append([])

    hp -= boss_damage

    if hp < 1:
        return

    return [hp, boss_hp, mana]


def battle(current_lowest):
    """Simulate battle returning the amount of mana used if it's less than arg."""
    hp = 50
    mana = 500
    mana_spent = 0
    boss_hp = 71
    fight_recap = []

    while True:
        spell = ''
        selected = False
        while not selected:
            spell = random.choice(spells)
            if spell not in effects[0]:
                fight_recap.append(spell)
                selected = True

        # Wizard's Turn
        post_magic = wizard_turn(hp, boss_hp, mana, mana_spent, spell)

        if not post_magic:
            return

        if type(post_magic) == int:
            if post_magic < current_lowest:
                print("Boss Killed by Spell")
                print(fight_recap)
                return post_magic
            return

        elif type(post_magic) == bool:
            if mana < current_lowest:
                print("Boss Killed by Effect on Wizard's Turn")
                print(fight_recap)
                return mana_spent
            return

        mana_spent = post_magic[3]

        if mana_spent > current_lowest:
            return

        # Boss_turn
        post_boss = boss_turn(post_magic[0], post_magic[1], post_magic[2])

        if not post_boss:
            return

        if type(post_boss) == bool:
            print("Boss Killed by Effect on Bosses Turn")
            print(fight_recap)
            return mana_spent

        hp = post_boss[0]
        boss_hp = post_boss[1]
        mana = post_boss[2]


spells = ['mm', 'd', 's', 'p', 'r']

lowest_mana = 10000
lowest_list = None

waged = 0
while waged < 10000:
    effects = [[], [], [], [], [], []]
    result = battle(lowest_mana)
    if result:
        lowest_mana = result
    waged += 1

print("The Least Amount of Mana for a Victory =", lowest_mana)
