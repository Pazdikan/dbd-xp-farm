import config
from random import randint

import killer.universal as universal
import killer.trapper as trapper

def perform_ingame_action():
    if (config.killer == config.Killer.OTHER):
        universal.walk_and_attack()
        
    elif (config.killer == config.Killer.TRAPPER):
        random_action = randint(0, 5)

        if random_action == 0:
            universal.walk_and_attack()
        else:
            trapper.place_and_pick_trap()