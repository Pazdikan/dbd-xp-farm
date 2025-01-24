from random import randint
import pyautogui
from time import sleep
from core.killer import universal
from util.console import log

is_cloaked = True

def cloak():
    log("Wraith action: Cloak")

    pyautogui.mouseDown(button="right")
    sleep(1.5)
    pyautogui.mouseUp(button="right")

    is_cloaked = True

    sleep(3)

def uncloak():
    log("Wraith action: Uncloak")

    pyautogui.mouseDown(button="right")
    sleep(3.5)
    pyautogui.mouseUp(button="right")

    is_cloaked = False

    sleep(3)