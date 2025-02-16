from time import time
from core.killer import deathslinger, wraith
import data
from random import randint

import core.killer.universal as universal
import core.killer.trapper as trapper
import core.killer.blight as blight
import core.killer.doctor as doctor

debug = True
custom_actions = 0


def perform_ingame_action():
    should_perform_universal = randint(0, 4) == 0

    # if data.debug:
    #     should_perform_universal = False
    #     data.selected_killer = data.Killer.BLIGHT.name

    if data.selected_killer == data.Killer.WRAITH and wraith.is_cloaked:
        should_perform_universal = False

    # to prevent bad rng never moving the killer for 10 minutes (actually happened)
    global custom_actions
    if custom_actions >= 5:
        should_perform_universal = True
        custom_actions = 0

    if should_perform_universal:
        random_action = randint(0, 1)

        if random_action == 0:
            universal.walk_and_attack()

        elif random_action == 1:
            universal.attack_random_direction()
    else:
        custom_actions += 1

        if data.selected_killer == data.Killer.OTHER.name:
            universal.walk_and_attack()

        elif data.selected_killer == data.Killer.TRAPPER.name:
            random_action = randint(0, 0)

            if random_action == 0:
                trapper.place_and_pick_trap()

        elif data.selected_killer == data.Killer.BLIGHT.name:
            random_action = randint(0, 0)

            if random_action == 0:
                blight.rush()

        elif data.selected_killer == data.Killer.DOCTOR.name:
            if (
                doctor.static_blast_used == None
                or time() - doctor.static_blast_used > 50
            ):
                doctor.static_blast()
            else:
                random_action = randint(0, 0)

                if random_action == 0:
                    doctor.shock_therapy()

        elif data.selected_killer == data.Killer.WRAITH.name:
            random_action = randint(0, 0)

            if random_action == 0:
                actions = data.ss.take_and_read_actions_screenshot()

                if len(actions) == 0:
                    return

                if any("UNCLOAK" in string for string in actions):
                    wraith.uncloak()
                    return

                if any("CLOAK" in string for string in actions):
                    wraith.cloak()
                    return

        elif data.selected_killer == data.Killer.DEATHSLINGER.name:
            actions = data.ss.take_and_read_actions_screenshot()

            if len(actions) == 0:
                return

            if any("AIM" in string for string in actions):
                deathslinger.aim_and_shoot()
                return

            if any("RELOAD" in string for string in actions):
                deathslinger.reload()
                return
