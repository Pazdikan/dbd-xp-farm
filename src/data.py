from time import time
from enum import Enum
from util.config import Config

# !!! dont touch anything here bro !!!
# !!! dont touch anything here bro !!!
# !!! dont touch anything here bro !!!
# !!! dont touch anything here bro !!!
# !!! dont touch anything here bro !!!
# !!! dont touch anything here bro !!!
# !!! dont touch anything here bro !!!
# !!! dont touch anything here bro !!!
# !!! dont touch anything here bro !!!

debug = False

ss = None

State = Enum('State', ['INGAME', 'INLOBBY', 'INQUEUE'])
Killer = Enum('Killer', ['OTHER', "TRAPPER", "BLIGHT"])

current_state = State.INLOBBY

if debug:
    current_state = State.INGAME

games = 0
xp = 1250
total_time_in_game = 0

script_start_time = time()
game_started_at = None

config = Config()