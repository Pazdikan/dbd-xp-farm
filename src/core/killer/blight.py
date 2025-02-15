import pyautogui
from time import sleep
from util.console import log


def rush():
    log("Blight action: Rush")

    count = 0
    while count < 18:
        rush_logic()
        count += 1

    sleep(12)  # recover rush charges


def rush_logic():
    # for some reason pyautogui.click, rightClick etc only trigger
    # the first rush. not sure why. so i have to "hold" the button
    pyautogui.mouseDown(button="secondary")
    sleep(0.01)
    pyautogui.mouseUp(button="secondary")
    sleep(0.03)
