import rich
from rich.console import Console
from rich.text import Text
import datetime
from time import time
import config
import gui

console = Console()

def log(text: Text):
    console.log(text)
    if gui.overlay != None:
        if isinstance(text, rich.text.Text):
            gui.overlay.update_log(text.plain)
        else:
            gui.overlay.update_log(text)

def get_stats():
    stats = [
        "",
        Text(f" XP: {config.xp} total ({config.xp / config.games} avg per game)", style="black on yellow"),
        Text(f" Games: {config.games} played ", style="black on green"),
        Text(f" Running Time: {str(datetime.timedelta(seconds=int(time() - config.script_start_time)))} ({str(datetime.timedelta(seconds=int(config.total_time_in_game)))} in games; {str(datetime.timedelta(seconds=int((time() - config.script_start_time) - config.total_time_in_game)))} in lobby)", style="white on purple"),
        ""
    ]

    return stats

def print_stats():
    stats = get_stats()
    
    for stat in stats:
        log(stat)