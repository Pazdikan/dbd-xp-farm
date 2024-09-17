import pyautogui
from time import sleep
from util.console import console
from rich.text import Text

def walk_and_attack():
    console.log("Universal action: Walk and attack")

    pyautogui.keyDown("w")
    sleep(0.5)
    pyautogui.keyUp("w")

    pyautogui.keyDown("s")
    sleep(0.5)
    pyautogui.keyUp("s")

    # Coords of the "banner" (survivor disconneted etc.); if no banner is present, it just attacks like normal
    pyautogui.click(x=1379, y=658)
    pyautogui.click(x=1379, y=658)
    pyautogui.click(x=1379, y=658)