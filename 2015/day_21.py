"""Advent of Code Day 21 - RPG Simulator 20XX"""

import itertools

my_hp = 100
boss_hp = 103
boss_damage = 9
boss_armour = 2

weapon = {'dagger': [8, 4, 0], 'shortsword': [10, 5, 0], 'warhammer': [25, 6, 0],
         'longsword': [40, 7, 0], 'greataxe': [74, 8, 0]}

armour = {'leather': [13, 0, 1], 'chainmail': [31, 0, 2], 'splintmail': [53, 0, 3],
         'bandedmail': [75, 0, 4], 'platemail': [102, 0, 5]}

rings = {'damage1': [25, 1, 0], 'damage2': [50, 2, 0], 'damage3': [100, 3, 0],
         'defense1': [20, 0, 1], 'defense2': [40, 0, 2], 'defense3': [80, 0, 3]}

shop_list = ['dagger', 'shortsword', 'warhammer', 'longsword', 'greataxe',
             'leather', 'chainmail', 'splintmail', 'bandedmail', 'platemail',
             'damage1', 'damage2', 'damage3', 'defense1', 'defense2',
             'defense3']

cost_least = 1000
cost_most = 0
for i in range(len(shop_list)):
    for loadout in itertools.combinations(shop_list, i):
        # Build character
        weapons_list = []
        armour_list = []
        rings_list = []

        for item in loadout:
            if item in weapon:
                weapons_list.append(item)
            elif item in armour:
                armour_list.append(item)
            elif item in rings:
                rings_list.append(item)

        # Check validity of loadout
        if len(weapons_list) == 1 and len(armour_list) < 2 and len(rings_list) < 3:
            
            # Calculate stats
            cost = 0
            my_damage = 0
            my_armour = 0

            for item in weapons_list:
                cost += weapon[item][0]
                my_damage += weapon[item][1]
                my_armour += weapon[item][2]

            for item in armour_list:
                cost += armour[item][0]
                my_damage += armour[item][1]
                my_armour += armour[item][2]

            for item in rings_list:
                cost += rings[item][0]
                my_damage += rings[item][1]
                my_armour += rings[item][2]

            health = my_hp
            boss_health = boss_hp
            mod_damage = my_damage - boss_armour
            boss_attack = boss_damage - my_armour

            # Battle
            fighting = True
            while fighting:
                boss_health -= mod_damage
                if boss_health <= 0:
                    if cost < cost_least:
                        cheapest_victory = loadout
                        cost_least = cost
                    fighting = False

                health -= boss_attack
                if health <= 0:
                    if cost > cost_most:
                        cost_most = cost
                    fighting = False

    i += 1

print("Cheapest Victory =", cost_least)
print("Most Expensive Defeat =", cost_most)
