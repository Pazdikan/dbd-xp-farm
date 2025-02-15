import warnings

import pyautogui

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


def check_python_version():
    if sys.version_info.major != 3 or sys.version_info.minor != 12:
        print(
            "Current Python version: "
            + str(sys.version_info.major)
            + "."
            + str(sys.version_info.minor)
        )
        print(
            "Please run with Python 3.12.* (current: "
            + str(sys.version_info.major)
            + "."
            + str(sys.version_info.minor)
            + "."
            + str(sys.version_info.micro)
            + ") to avoid any issues!"
        )
        print(
            "If something is not working, do not complain in issues (unless you are using Python 3.12.* and this is a bug)"
        )
        print(
            "You can download Python 3.12.8 from https://www.python.org/downloads/release/python-3128/"
        )
        print("\n\nScript will try to run in 12 seconds...")
        sleep(12)


console.clear()
check_python_version()


log(Text("Initializing...", style="green"))

screen_width, screen_height = pyautogui.size()

if screen_width != 1920 or screen_height != 1080:
    log(
        Text(
            "Script requires 1920x1080 resolution! Current: {}x{}".format(
                screen_width, screen_height
            ),
            style="red",
        )
    )
    log(
        Text(
            "Set your resulution to 1920x1080 in Windows display settings.",
            style="blue",
        )
    )
    log(
        Text(
            "\n\nSorry about that, I know that's annoying. I'm too lazy to implement dynamic button positions ;<"
        )
    )
    sys.exit(1)


def run_main_app():
    with mss() as sct:
        data.ss = Screenshot(sct)
        log(Text("Everything's ready!", style="green"))

        log(Text("Access web panel via http://localhost:5000/", style="green"))

        while True:
            window = win32gui.GetForegroundWindow()
            window_title = win32gui.GetWindowText(window)

            if "DeadByDaylight" in window_title:
                brain.loop()
            else:
                log(
                    Text(
                        "Script paused, because Dead by Daylight is not focused!",
                        style="red",
                    )
                )
                sleep(1)


if __name__ == "__main__":
    log(Text("Main app thread is starting...", style="green"))
    main_app_thread = threading.Thread(target=run_main_app, daemon=True)
    main_app_thread.start()

    log(Text("Overlay thread is starting...", style="green"))
    overlay_thread = threading.Thread(target=overlay.run_overlay, daemon=True)
    overlay_thread.start()

    log(Text("API webserver thread is starting...", style="green"))
    api_app_thread = threading.Thread(target=webserver.run_webserver(), daemon=True)
    api_app_thread.start()
