from rich.console import Console
from rich.text import Text
import datetime
from time import time
import config

console = Console()

def print_stats():
    console.print("\n\n")
    console.print(Text(f" XP: {config.xp} total ({config.xp / config.games} avg per game)", style="black on yellow"))
    console.print(Text(f" Games: {config.games} played ", style="black on green"))
    console.print(Text(f" Running Time: {str(datetime.timedelta(seconds=int(time() - config.script_start_time)))} ({str(datetime.timedelta(seconds=int(config.total_time_in_game)))} in games; {str(datetime.timedelta(seconds=int((time() - config.script_start_time) - config.total_time_in_game)))} in lobby)"), style="white on purple")
    console.print("\n\n")