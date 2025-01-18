import data
from random import randint

import core.killer.universal as universal
import core.killer.trapper as trapper
import core.killer.blight as blight

def perform_ingame_action():
    selected_killer = data.Killer[data.config.get('killer', section='general').upper()]

    if (selected_killer == data.Killer.OTHER):
        universal.walk_and_attack()
        
    elif (selected_killer == data.Killer.TRAPPER):
        random_action = randint(0, 4)

        if random_action == 0:
            universal.walk_and_attack()
        else:
            trapper.place_and_pick_trap()

    elif (selected_killer == data.Killer.BLIGHT):
        random_action = randint(0, 3)

        if random_action == 0:
            universal.walk_and_attack()
        else:
            blight.rush()