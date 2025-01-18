import rich
from rich.console import Console
from rich.text import Text
import datetime
from time import time
import data
import overlay

console = Console()

def log(text: Text):
    console.log(text)
    if overlay.overlay != None:
        if isinstance(text, rich.text.Text):
            overlay.overlay.update_log(text.plain)
        else:
            overlay.overlay.update_log(text)

def get_stats():
    stats = [
        "",
        Text(f" XP: {int(data.xp)} total ({int(data.xp / data.games)} avg per game)", style="black on yellow"),
        Text(f" Games: {data.games} played ", style="black on green"),
        Text(f" Running Time: {str(datetime.timedelta(seconds=int(time() - data.script_start_time)))} ({str(datetime.timedelta(seconds=int(data.total_time_in_game)))} in games; {str(datetime.timedelta(seconds=int((time() - data.script_start_time) - data.total_time_in_game)))} in lobby)", style="white on purple"),
        ""
    ]

    return stats

def print_stats():
    stats = get_stats()
    
    for stat in stats:
        log(stat)