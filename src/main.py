from time import sleep
from util.console import log, console, print_stats
from rich.text import Text
import config
from mss import mss
import core.brain as brain
import threading
import gui  # Import the gui module

from util.screenshot import Screenshot
import win32gui 

if __name__ == '__main__':
    console.print(Text("\n! IGNORE ALL ERRORS ABOVE !\n", style="bold black on red"))
    log(Text("Initializing...", style="green"))

    # Start the GUI in a separate thread
    gui_thread = threading.Thread(target=gui.run_overlay, daemon=True)
    gui_thread.start()

    # Start the GUI app in a separate thread
    gui_app_thread = threading.Thread(target=gui.create_main_gui, daemon=True)
    gui_app_thread.start()

    with mss() as sct:
        config.ss = Screenshot(sct)
        console.clear()
        log(Text("Initialized!", style="green"))

        while True:
            # Get the title of the currently focused window
            window = win32gui.GetForegroundWindow()
            window_title = win32gui.GetWindowText(window)

            # Check if the focused window is "DeadByDaylight-Win64-Shipping.exe" or titled "DeadByDaylight"
            if "DeadByDaylight" in window_title:
                brain.loop()
            else:
                log(Text("Script paused, because Dead by Daylight is not focused!", style="red"))
                sleep(1)
