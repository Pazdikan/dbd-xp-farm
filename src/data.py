from time import time
from enum import Enum
from util.config import Config

ss = None

State = Enum('State', ['INGAME', 'INLOBBY', 'INQUEUE'])
Killer = Enum('Killer', ['OTHER', "TRAPPER", "BLIGHT"])

current_state = State.INLOBBY

games = 0
xp = 0
total_time_in_game = 0

script_start_time = time()
game_started_at = None

config = Config()