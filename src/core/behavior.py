import config
from random import randint

import killer.universal as universal
import killer.trapper as trapper
import killer.blight as blight

def perform_ingame_action():
    if (config.killer == config.Killer.OTHER):
        universal.walk_and_attack()
        
    elif (config.killer == config.Killer.TRAPPER):
        random_action = randint(0, 4)

        if random_action == 0:
            universal.walk_and_attack()
        else:
            trapper.place_and_pick_trap()

    elif (config.killer == config.Killer.BLIGHT):
        random_action = randint(0, 4)

        if random_action == 0:
            universal.walk_and_attack()
        else:
            blight.rush()