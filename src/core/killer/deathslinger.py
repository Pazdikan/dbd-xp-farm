import pyautogui
from time import sleep, time
import data
from util.console import log

def aim_and_shoot():
    log("Deathslinger action: Aim & Shoot")

    pyautogui.mouseDown(button="right")
    sleep(4)
    pyautogui.mouseDown(button="left")
    sleep(0.1)
    pyautogui.mouseUp(button="left")
    pyautogui.mouseUp(button="right")

def reload():
    log("Deathslinger action: Reload")

    pyautogui.keyDown("ctrlleft")
    sleep(4)
    pyautogui.keyUp("ctrlleft")

    sleep(1)