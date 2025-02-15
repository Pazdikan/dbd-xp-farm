import pyautogui
from time import sleep, time
from util.console import log

static_blast_used = None


def static_blast():
    log("Doctor action: Static Shock")

    global static_blast_used
    static_blast_used = time()

    pyautogui.keyDown("ctrlleft")
    sleep(3)
    pyautogui.keyUp("ctrlleft")

    sleep(3)


def shock_therapy():
    log("Doctor action: Shock Therapy")

    pyautogui.mouseDown(button="right")
    sleep(2)
    pyautogui.mouseUp(button="right")

    sleep(3)
