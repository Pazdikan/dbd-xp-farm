from time import time
from enum import Enum
from util.config import Config
import sys

debug = False

debug = any(arg in ("--debug", "-d") for arg in sys.argv)

ss = None

State = Enum("State", ["INGAME", "INLOBBY", "INQUEUE", "PREGAME"])
Killer = Enum(
    "Killer", ["OTHER", "TRAPPER", "BLIGHT", "DOCTOR", "WRAITH", "DEATHSLINGER"]
)

current_state = State.INLOBBY

if debug:
    current_state = State.PREGAME

games = 0
xp = 0
bloodpoints = 0
starting_iri_shards = 0
iri_shards = 0
total_time_in_game = 0

script_start_time = time()
game_started_at = None

config = Config()

selected_killer = config.get("killer", section="general").upper()
