from time import time
import data
from random import randint

import core.killer.universal as universal
import core.killer.trapper as trapper
import core.killer.blight as blight
import core.killer.doctor as doctor

debug = True

def perform_ingame_action():
    selected_killer = data.Killer[data.config.get('killer', section='general').upper()]

    should_perform_universal = randint(0, 2) == 0 # 33% chance to perform universal action

    if (should_perform_universal):
        random_action = randint(0, 1)

        if random_action == 0:
            universal.walk_and_attack()

        elif random_action == 1:
            universal.attack_random_direction()
    else:
        if (selected_killer == data.Killer.OTHER):
            universal.walk_and_attack()

        elif (selected_killer == data.Killer.TRAPPER):
            random_action = randint(0, 0)

            if random_action == 0:
                trapper.place_and_pick_trap()         

        elif (selected_killer == data.Killer.BLIGHT):
            random_action = randint(0, 0)

            if random_action == 0:
                blight.rush()
        
        elif (selected_killer == data.Killer.DOCTOR):
            if (doctor.static_blast_used == None or time() - doctor.static_blast_used > 50):
                doctor.static_blast()
            else:
                random_action = randint(0, 0)

                if random_action == 0:
                    doctor.shock_therapy()