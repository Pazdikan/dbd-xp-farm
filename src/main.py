import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

from time import sleep
from util.console import log, console, print_stats
from rich.text import Text
import data
from mss import mss
import core.brain as brain
import threading
import overlay  # Import the gui module
import sys
from util.screenshot import Screenshot
import win32gui

import webserver.webserver as webserver

console.clear()
log(Text("Initializing...", style="green"))

def run_main_app():
    with mss() as sct:
        data.ss = Screenshot(sct)
        log(Text("Everything's ready!", style="green"))

        log(Text("Access web panel via http://localhost:5000/", style="green"))

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

def check_python_version():
    if sys.version_info.major != 3 or sys.version_info.minor != 12:
        log(Text("Current Python version: " + str(sys.version_info.major) + "." + str(sys.version_info.minor), style="red"))
        log(Text("Please run with Python 3.12 to avoid any issues!", style="red"))
        log(Text("If something is not working, do not complain in issues (or open pull request with updates to 3.14)", style="blue"))
        log(Text("\n\nScript will try to run in 10 seconds...", style="green"))
        sleep(10)

if __name__ == '__main__':
    check_python_version()

    log(Text("Main app thread is starting...", style="green"))
    main_app_thread = threading.Thread(target=run_main_app, daemon=True)
    main_app_thread.start()

    log(Text("Overlay thread is starting...", style="green"))
    overlay_thread = threading.Thread(target=overlay.run_overlay, daemon=True)
    overlay_thread.start()

    log(Text("API webserver thread is starting...", style="green"))
    api_app_thread = threading.Thread(target=webserver.run_webserver(), daemon=True)
    api_app_thread.start()