from time import time
from enum import Enum

# THIS IS NOT THE CONFIGURATION YOU ARE LOOKING FOR
# SCROLL DOWN TO FIND THE CONFIGURATION FOR USERS

ss = None

State = Enum('State', ['INGAME', 'INLOBBY', 'INQUEUE'])
Killer = Enum('Killer', ['OTHER', "TRAPPER"])

current_state = State.INLOBBY

games = 0
xp = 0
total_time_in_game = 0

script_start_time = time()
game_started_at = None

# CONFIGURATION FOR USERS
# EDITING STUFF BETWEEN COMMENTS BELOW IS SAFE AND WILL NOT BREAK THE SCRIPT

killer = Killer.OTHER # From the list above

xp_limit = 0 # SET TO 0 TO DISABLE
games_limit = 0 # SET TO 0 TO DISABLE

# END OF CONFIGURATION