from util.console import console
from rich.text import Text
import config
from mss import mss
import core.brain as brain

from util.screenshot import Screenshot

if __name__ == '__main__':
    console.print(Text("\n! IGNORE ALL ERRORS ABOVE !\n", style="bold black on red"))
    console.log(Text("Initializing...", style="green"))


    with mss() as sct:
        config.ss = Screenshot(sct)
        console.clear()
        console.log(Text("Initialized!", style="green"))

        while True:
            brain.loop()